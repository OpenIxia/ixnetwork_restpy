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
import time
import logging
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.connection import Connection
from ixnetwork_restpy.errors import NotFoundError


class TestPlatform(Base):
    """The TestPlatform class is the only class that can be instantiated directly.  
    The package is constructed in an hierarchical format so as a result child resources are accessed through class properties.
    Class properties will return an iterable child container of that class.
    If the class is system managed or user managed it will have a find() method which can be used to retrieve the resources from the server otherwise the one and only one resource will be retrieved from the server.
    """
    _SDM_NAME = None
    TRACE_NONE = Connection.TRACE_NONE
    TRACE_INFO = Connection.TRACE_INFO
    TRACE_WARNING = Connection.TRACE_WARNING
    TRACE_REQUEST = Connection.TRACE_REQUEST
    TRACE_REQUEST_RESPONSE = Connection.TRACE_REQUEST_RESPONSE
    TRACE_ALL = Connection.TRACE_ALL

    def __init__(self, ip_address, rest_port=None, platform=None, log_file_name=None, ignore_env_proxy=False, verify_cert=False, trace=TRACE_NONE, script_watch=True):
        """Establishes an initial connection to an IxNetwork test tool platform. 
        Currently supported platforms are Linux API Server, Windows GUI and ConnectionManager.

        Args
        ----
        - ip_address (str): the ip address of the test tool platform that requests will be made to
        - rest_port (number): the ip port of the test tool platform that the server is listening on. 
            Defaults are linux|connection_manager:443, windows:11009
        - platform (str[windows|linux|connection_manager]): DEPRECATED
            This is now determined by the Connection class.
        - log_file_name (str): the name of the log file that trace logging will be written to
            The default is write to the console
        - ignore_env_proxy (bool): if requests is returning a 504 error use this to bypass local environment proxy settings
        - verify_cert (bool): enable this flag to verify the certificate 
        - trace (str(none|info|warning|request|request_response|all)): set the tracing level of requests and responses.
        - script_watch (bool): disable this to not have REST API requests logged with the server script watch

        Raises
        ------
        - obj(ixnetwork_restpy.errors.ConnectionError)
        """
        super(TestPlatform, self).__init__(None)
        self._connection = Connection(ip_address, rest_port, platform, log_file_name, ignore_env_proxy, verify_cert, trace, script_watch)
        self._uid = ''
        self._set_default_href()

    def _set_default_href(self, href='/api/v1'):
        properties = {
            'href': href,
            'apiKey': self._connection.x_api_key,
            'username': self._uid,
            'trace': self._connection.trace,
            'platform': self._connection.platform,
            'scheme': self._connection._scheme,
            'hostname': self._connection.hostname,
            'restPort': self._connection.rest_port,
            'logFilename': self._connection.log_file_name
        }
        self._set_properties(properties, clear=True)

    def Authenticate(self, uid, pwd):
        """Set the X-Api-Key by authenticating against the connected TestPlatform

        Args
        ----
        - uid (str): The userid to be authenticated
        - pwd (str): The password to be authenticated

        Raises
        ------
        - UnauthorizedError: Access is unauthorized
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._set_default_href('/api/v1/auth/session')
        response = self._execute(None, payload={'username': uid, 'password': pwd})
        self.ApiKey = response['apiKey']
        self._uid = uid
        self._set_default_href()
        return self.ApiKey

    @property
    def Trace(self):
        """Trace http transactions

        Returns
        -------
        - str(TestPlatform.TRACE_NONE | TestPlatform.TRACE_ALL | TestPlatform.TRACE_INFO | TestPlatform.TRACE_WARNING | TestPlatform.TRACE_REQUEST | TestPlatform.TRACE_REQUEST_RESPONSE): Enables tracing of the connection transport request and responses
        """
        return self._get_attribute('trace')
    @Trace.setter
    def Trace(self, trace):
        self._connection.trace = trace

    @property
    def ApiKey(self):
        """
        Returns
        -------
        - bool: An X-Api-Key for authorizing transactions instead of using the authenticate method
        """
        return self._get_attribute('apiKey')
    @ApiKey.setter
    def ApiKey(self, value):
        self._connection.x_api_key = value

    @property
    def Username(self):
        """Returns the name of the user that was authenticated

        Returns
        -------
        - str: The username
        """
        return self._get_attribute('username')

    @property
    def Platform(self):
        """Returns the platform type of the server

        Returns
        -------
        - str(windows | linux | connection_manager): The type of platform IxNetwork is deployed on
        """
        return self._get_attribute('platform')

    @property
    def Hostname(self):
        """Returns the hostname of the server that requests are being submitted to

        Returns
        -------
        - str: The hostname of the server
        """
        return self._get_attribute('hostname')

    @property
    def RestPort(self):
        """Returns the rest port of the server that requests are being submitted to

        Returns
        -------
        - int: The rest port of the server
        """
        return self._connection.rest_port

    @property
    def Scheme(self):
        """Returns the type of scheme

        Returns
        -------
        - str: The type of scheme http or https
        """
        return self._get_attribute('scheme')

    @property
    def LogFilename(self):
        """Returns the name of the log file

        Returns
        -------
        - str: The name of the log file
        """
        return self._get_attribute('logFilename')

    @property
    def Sessions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.sessions.Sessions): An instance of the Sessions class
        """
        from ixnetwork_restpy.testplatform.sessions.sessions import Sessions
        return Sessions(self)
