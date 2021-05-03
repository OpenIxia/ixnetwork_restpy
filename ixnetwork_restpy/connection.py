# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
import sys
import os
import ssl
import datetime
import time
import json
import logging
import pkg_resources
from requests import Session, request, utils
from requests.exceptions import ConnectTimeout
from io import BufferedReader
from ixnetwork_restpy.errors import *
from ixnetwork_restpy.files import Files


try:
    basestring
except NameError:
    basestring = str


class Connection(object):
    """Http/Https transport"""
    X_API_KEY = 'X-Api-Key'
    TRACE_NONE = 'none'
    TRACE_INFO = 'info'
    TRACE_WARNING = 'warning'
    TRACE_REQUEST = 'request'
    TRACE_REQUEST_RESPONSE = 'request_response'
    TRACE_ALL = 'all'
    PLATFORMS = {
        'Jetty': 'linux',
        'nginx/1.17.8': 'linux',
        'SelfHost': 'windows',
        'Kestrel': 'windows',
        'Microsoft-HTTPAPI/2.0': 'connection_manager'
    }

    def __init__(self, hostname, rest_port, platform, log_file_name=None, ignore_env_proxy=False, verify_cert=False, trace='none', script_watch=True):
        """ Set the connection parameters to a rest server

        Args:
            hostname (str): hostname or ip address
            rest_port (int, optional): the rest port of the server
            platform (str):
            log_file_name (str):
            ignore_env_proxy (bool):
            verify_cert (bool): 
            script_watch (bool):
        """
        self.trace = trace
        if len(logging.getLogger(__name__).handlers) == 0:
            handlers = [logging.StreamHandler(sys.stdout)]
            if log_file_name is not None:
                handlers.append(logging.FileHandler(log_file_name, mode='w'))
            formatter = logging.Formatter(fmt='%(asctime)s [%(name)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            formatter.converter = time.gmtime
            for handler in handlers:
                handler.setFormatter(formatter)
                logging.getLogger(__name__).addHandler(handler)
            logging.getLogger(__name__).info('using python version %s' % sys.version)
            try:
                logging.getLogger(__name__).info('using ixnetwork-restpy version %s' % pkg_resources.get_distribution("ixnetwork-restpy").version)
            except Exception as e:
                logging.getLogger(__name__).warning("ixnetwork-restpy not installed using pip, unable to determine version")
        self._verify_cert = verify_cert
        if self._verify_cert is False:
            self._warn('Verification of certificates is disabled')
            if sys.version < '2.7.9':
                import requests.packages.urllib3
                requests.packages.urllib3.disable_warnings()
            else:
                import urllib3
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._headers = {
            Connection.X_API_KEY: None,
            'User-Agent': 'ixnetwork-restpy',
            'Connection': 'keep-alive'
        }
        if script_watch is False:
            self._headers['SDMAPI'] = 'GUIREQUEST'
        if ignore_env_proxy is True:
            os.environ['no_proxy'] = '*' 
        self._hostname = hostname
        if ':' in self._hostname and '[' not in self._hostname:
            self._hostname = '[%s]' % self._hostname
        self._rest_port = rest_port
        self._scheme = 'https'
        self._log_file_name = log_file_name
        self._session = Session()
        self._scheme = self._determine_test_tool_platform(platform)

    def _determine_test_tool_platform(self, platform):
        self._info('Determining the platform and rest_port using the %s address...' % self._hostname)
        if platform is not None:
            self._warn('The `platform` parameter is deprecated and the value `%s` will be ignored.' % platform)
        self._platform = None
        rest_ports = [443, 11009]
        if self._rest_port is not None:
            if self._rest_port in rest_ports:
                rest_ports.remove(self._rest_port)
            rest_ports.insert(0, self._rest_port)
        for rest_port in rest_ports:
            for scheme in ['http', 'https']:
                try:
                    url = '%s://%s:%s/api/v1/auth/session' % (scheme, self._hostname, rest_port)
                    payload = json.dumps({'username': '', 'password': ''})
                    headers = self._headers
                    headers['content-type'] = 'application/json'
                    response = self._request(method='POST', url=url, data=payload, headers=headers, verify=self._verify_cert, timeout=2)
                    if response.status_code in [401, 403, 200]:
                        if 'server' not in response.headers:
                            response.headers['server'] = 'Jetty'
                        for server in Connection.PLATFORMS:
                            if server in response.headers['server']:
                                self._platform = Connection.PLATFORMS[server]
                                self._rest_port = rest_port
                                self._info('Connection established to `%s://%s:%s on %s`' % (scheme, self._hostname, self._rest_port, self._platform))
                                return scheme
                    else:
                        raise Exception()
                except Exception as e:
                    self._warn('Unable to connect to %s://%s:%s.' % (scheme, self._hostname, rest_port))
        raise ConnectionError('Unable to connect to %s. Check the ip address and consider the rest_port parameter.' % self._hostname)

    @property
    def trace(self):
        """str: Trace all requests and responses."""
        return self._trace

    @trace.setter
    def trace(self, value):
        if value == Connection.TRACE_NONE:
            logging.getLogger(__name__).setLevel(logging.CRITICAL)
        elif value == Connection.TRACE_INFO:
            logging.getLogger(__name__).setLevel(logging.INFO)
        elif value == Connection.TRACE_WARNING:
            logging.getLogger(__name__).setLevel(logging.WARNING)
        elif value in [Connection.TRACE_REQUEST, Connection.TRACE_REQUEST_RESPONSE, Connection.TRACE_ALL]:
            logging.getLogger(__name__).setLevel(logging.DEBUG)
        else:
            raise ValueError('the value %s is an incorrect Trace level' % value)
        self._trace = value

    @property
    def platform(self):
        return self._platform

    @property
    def hostname(self):
        return self._hostname

    @property
    def rest_port(self):
        return self._rest_port

    @property
    def scheme(self):
        return self._scheme

    @property
    def log_file_name(self):
        return self._log_file_name

    @property
    def x_api_key(self):
        """str: Get/Set the x-api-key header value."""
        return self._headers[Connection.X_API_KEY]

    @x_api_key.setter
    def x_api_key(self, value):
        self._headers[Connection.X_API_KEY] = value

    def _request(self, **kwargs):
        return self._session.request(**kwargs)

    def _read(self, url):
        return self._send_recv('GET', url)

    def _create(self, url, payload):
        return self._send_recv('POST', url, payload)

    def _update(self, url, payload):
        return self._send_recv('PATCH', url, payload)

    def _delete(self, url, payload=None):
        return self._send_recv('DELETE', url, payload)

    def _execute(self, url, payload):
        return self._send_recv('POST', url, payload)

    def _options(self, url):
        return self._send_recv('OPTIONS', url)

    def _print_request(self, method, url, payload=None):
        if self._trace in [Connection.TRACE_REQUEST, Connection.TRACE_REQUEST_RESPONSE, Connection.TRACE_ALL]:
            data = ''
            if payload is not None:
                if self._trace == Connection.TRACE_ALL:
                    data = payload
                else:
                    data = payload[0:132]
                    if len(payload) > 132:
                        data += ' ...'
            logging.getLogger(__name__).debug('%s %s %s' % (method, url, data))

    def _print_response(self, response):
        if self._trace in [Connection.TRACE_REQUEST_RESPONSE, Connection.TRACE_ALL] \
            and response.headers.get('content-length') \
            and response.headers.get('content-type') \
            and 'application/json' in response.headers['content-type']:
            data = ''
            if self._trace == Connection.TRACE_ALL:
                data = response.content
            elif int(response.headers['content-length']) > 132:
                data = '%s...' % response.content[0:132]
            else:
                data = response.content
            logging.getLogger(__name__).debug('%s %s %s' % (response.status_code, response.reason, data))

    def _info(self, message):
        logging.getLogger(__name__).info(message)

    def _warn(self, message):
        logging.getLogger(__name__).warning(message)

    def _debug(self, message):
        logging.getLogger(__name__).debug(message)

    def _normalize_url(self, url):
        hostname = self._hostname
        if ':' in hostname and '[' not in hostname:
            hostname = '[%s]' % hostname
        connection = '%s://%s:%s' % (self._scheme, hostname, self._rest_port)
        if url.startswith(self._scheme) == False:
            url = '%s/%s' % (connection, url.strip('/'))
        path_start = url.find('://') + 3
        url = '%s%s' % (url[0:path_start], url[path_start:].replace('//', '/'))
        return (connection, url)

    def _get_file(self, url, remote_filename, remote_directory=None, local_filename=None, local_directory=None, return_content=False):
        headers = self._headers
        url = '%s/files?filename=%s' % (url, utils.quote(remote_filename))
        connection, url = self._normalize_url(url)
        if remote_directory is not None:
            url = '%s&absolute=%s' % (url, remote_directory)
        response = self._session.request('GET', url, headers=headers, verify=self._verify_cert)
        if response.status_code == 200:
            if return_content is True:
                return response.content
            if local_filename is None:
                local_filename = remote_filename
            if local_directory is not None:
                local_filename = os.path.join(local_directory, local_filename)
            local_filename = os.path.normpath(local_filename)
            try:
                with open(os.path.normpath(local_filename), 'wb') as fid:
                    fid.write(response.content)
            except Exception as e:
                self._info('cwd:%s filename:%s exception:%s' % (os.getcwd(), local_filename, e))
                raise e
            return local_filename
        else:
            self._process_response_status_code(url, headers, response)

    def _put_file(self, url, local_filename, remote_filename=None):
        headers = self._headers
        headers['Content-Type'] = 'application/octet-stream'
        if remote_filename is None:
            remote_filename = os.path.basename(local_filename)
        url = '%s/files?filename=%s' % (url, utils.quote(remote_filename))
        connection, url = self._normalize_url(url)
        with open(os.path.normpath(local_filename), 'rb') as fid:
            data = fid.read()
        response = self._session.request('POST', url, headers=headers, data=data, verify=self._verify_cert)
        if response.status_code == 201:
            return response.json()
        else:
            self._process_response_status_code(url, headers, response)

    def _delete_file(self, url, remote_filename):
        headers = self._headers
        url = '%s/files?filename=%s' % (url, utils.quote(remote_filename))
        connection, url = self._normalize_url(url)
        response = self._session.request('DELETE', url, headers=headers, verify=self._verify_cert)
        if response.status_code == 204:
            return
        else:
            self._process_response_status_code(url, headers, response)

    def _process_response_status_code(self, url, headers, response, async_status=False):
        errors = []
        # add the initial error
        if async_status is True:
            async_status = response.json()
            if 'message' in async_status and async_status['message'] is not None and 'API CONTENTION' in async_status['message']:
                response.status_code = 409
            else:
                response.status_code = 400
            error = ''
            if 'message' in async_status and async_status['message'] is not None:
                error += ' ' + async_status['message']
            if 'result' in async_status and async_status['result'] is not None:
                error += ' ' + async_status['result']
            errors.append(error)
        else:
            try:
                for error in response.json()['errors']:
                    errors.append(error['detail'])
            except:
                errors.append(response.text)
        # add any /globals/appErrors/error items
        try:
            preamble = url[0:url.find('/', url.find('/sessions/')+len('/sessions/'))]
            url = preamble + '/ixnetwork/globals/appErrors/error'
            error_response = self._session.request('GET', url, headers=headers, verify=self._verify_cert, allow_redirects=False)
            server_info = '\tCurrent Server Errors/Warnings:'
            for error in error_response.json():
                if error['errorLevel'] in ['kError', 'kWarning']:
                    if server_info is not None:
                        errors.append(server_info)
                        server_info = None
                    errors.append('\t%s [%s] [%s] %s' % (
                        error['lastModified'], 
                        error['errorLevel'][1:].upper(), 
                        error['name'],
                        error['description'])
                    )
        except:
            pass
        # raise the appropriate error
        message = '\n'.join(errors)
        if response.status_code == 400:
            raise BadRequestError(message, response.status_code)
        elif response.status_code == 401:
            raise UnauthorizedError(message, response.status_code)
        elif response.status_code == 404:
            raise NotFoundError(message, response.status_code)
        elif response.status_code == 409:
            raise ResourceInUseError(message, response.status_code)
        else:
            raise ServerError(message, response.status_code)

    def _send_recv(self, method, url, payload=None):
        headers = self._headers
        connection, url = self._normalize_url(url)

        data = payload
        if payload is not None:
            if isinstance(payload, dict) or isinstance(payload, list):
                headers['Content-Type'] = 'application/json'
                data = json.dumps(payload)
            elif isinstance(payload, Files):
                headers['Content-Type'] = 'application/octet-stream'
                data = ''
                if payload.is_local_file is True and os.path.exists(os.path.normpath(payload.file_path)) is True:
                    with open(os.path.normpath(payload.file_path), 'rb') as fid:
                        data = fid.read()
                else:
                    response = self._session.request('GET', url.replace('filename=', 'filter='), headers=headers, verify=self._verify_cert, allow_redirects=False)
                    if response.status_code == 200:
                        return
            elif isinstance(payload, basestring):
                headers['Content-Type'] = 'application/json'
                data = payload

        self._print_request(method, url, None if isinstance(payload, Files) else data)
        response = self._request(method=method, url=url, data=data, headers=headers, verify=self._verify_cert, allow_redirects=False)
        self._print_response(response)
        
        if str(response.status_code).startswith('3'):
            url = response.headers['location']
            if url.find('://') != -1:
                self._scheme = url[:url.find('://')]
                self._hostname = url[url.find('://') + 3:url.find('/', url.find('://') + 3)]
                if self._scheme == 'https':
                    self._rest_port = 443
                splitter = ']:' if ']' in self._hostname else ':'
                host_pieces = self._hostname.split(splitter)
                if len(host_pieces) > 1:
                    self._hostname = host_pieces[0]
                    self._rest_port = host_pieces[1]
            else:
                url = '%s://%s:%s%s' % (self._scheme, self._hostname, self._rest_port, url)
            self._print_request(method, url, data)
            response = self._session.request(method, url, data=data, headers=headers, verify=self._verify_cert, allow_redirects=False)
            self._print_response(response)

        if response.status_code == 202:
            while True:
                async_status = response.json()
                if 'state' not in async_status.keys():
                    break
                state = async_status['state']
                if state == 'IN_PROGRESS':
                    time.sleep(1)
                    state_url = async_status['url']
                    if state_url.startswith(self._scheme) is False:
                        state_url = '%s/%s' % (connection, state_url.strip('/'))
                    self._print_request('GET', state_url)
                    response = self._session.request('GET', state_url, headers=headers, verify=self._verify_cert)
                    self._print_response(response)
                elif state == 'SUCCESS':
                    if 'result' in async_status.keys() and async_status['result'] != 'kVoid':
                        return async_status['result']
                    else:
                        return None
                elif self._platform == 'connection_manager' and state in ['ACTIVE', 'STOPPED', 'STARTING']:
                    return response.json()
                else:
                    return self._process_response_status_code(url, headers, response, async_status=True)
        
        while(response.status_code == 409):
            time.sleep(6)
            response = self._session.request(method, url, data=data, headers=headers, verify=self._verify_cert)

        if response.status_code == 204:
            return None
        elif str(response.status_code).startswith('2') is True:
            if response.status_code == 201 and 'links' in response.json().keys():
                href = response.json()['links'][0]['href']
                return self._send_recv('GET', href)
            if response.headers.get('Content-Type'):
                if 'application/json' in response.headers['Content-Type']:
                    return response.json()
            return None
        else:
            self._process_response_status_code(url, headers, response)


