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
import re
from inspect import isclass
from ixnetwork_restpy.errors import NotFoundError
from ixnetwork_restpy.files import Files
from requests import utils


try:
    basestring
except NameError:
    basestring = str


class Base(object):
    """Base

    Designed around __iter__, __next__, __getitem__
    _object_properties is a list of property dicts returned by the server
    _index is the current pointer into the _object_properties
    _properties returns the current properties as dictated by _index
    """
    __slots__ = ('_object_properties', '_connection', '_parent', '_index')

    def __init__(self, parent):
        self._parent = parent
        if self._parent is not None:
            self._connection = parent._connection
        self._set_properties(None, clear=True)

    def __iter__(self):
        self._index = -1
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self._index + 1 >= len(self._object_properties):
            raise StopIteration
        else:
            self._index += 1
        return self[self._index]

    def __getitem__(self, index):
        if isinstance(index, slice) is True:
            start, stop, step = index.indices(len(self))
            item = self.__class__(self._parent)
            for i in range(start, stop, step):
                item._object_properties.append(self._object_properties[i])
            return item
        elif isinstance(index, int) is True:
            if index >= len(self._object_properties):
                raise IndexError
            elif index < 0 and len(self._object_properties) + index in range(len(self._object_properties)):
                index = len(self._object_properties) + index
            item = self.__class__(self._parent)
            item._object_properties.append(self._object_properties[index])
            return item
        else:
            raise NotImplemented('support for index of %s is not implemented' % index)

    @property
    def index(self):
        """The current index of the resources that have been retrieved from the server

        Returns
        -------
        - number: The current index of the retrieved resources
        """
        return self._index

    def __len__(self):
        """The total number of resources that have been retrieved from the server

        Returns
        -------
        - number: The total number of resources retrieved from the server
        """
        return len(self._object_properties)

    @property
    def href(self):
        """The hypertext reference of the current object

        Returns
        ------- 
        - str: The fully qualified hypertext reference of the current object

        Raises
        ------
        - KeyError: The href key does not exist which means no resources have been retrieved from the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_attribute('href')

    @property
    def parent(self):
        """The parent object of the current object

        Returns
        -------
        - obj: The parent object of the current object or None if there is no parent for this object
        """
        return self._parent

    @property
    def _properties(self):
        return self._object_properties[self._index]

    def _clear(self):
        self._object_properties = []
        self._index = len(self._object_properties) - 1

    def _check_arg_type(self, object_to_test, arg_type):
        if isinstance(object_to_test, arg_type) is not True:
            raise TypeError('the parameter supplied is of %s but must be of <type \'%s\'>' % (type(object_to_test), arg_type.__name__))

    def _get_attribute(self, name):
        """The main accessor for all attributes
        """
        if len(self._object_properties) == 0:
            msg = (
                'Failed to get the {}.{} property as the {} object has no '
                'encapsulated resources. '
                ).format(
                    self.__class__.__name__,
                    name,
                    self.__class__.__name__)
            if 'find' in dir(self):
                msg += (
                    'Either the {}.find() method was not called or it failed '
                    'to retrieve any resources from the server.'
                    ).format(
                        self.__class__.__name__)
            raise NotFoundError(msg)
        else:
            return self._properties[name]
            
    def _set_attribute(self, name, value):
        """Update a property on the server and save it locally if there is no exception
        """
        try:
            self._update({name: value})
            self._properties[name] = value
        except Exception as e:
            raise e

    def __str__(self):
        """Get all the instances encapsulated by this container without changing the current index

        Returns:
            str: A string representation of the encapsulated instances
        """
        instances = ''
        for i in range(len(self)):
            properties = self._object_properties[i]
            instances += '\n%s[%s]: %s' % (self.__class__.__name__, i, properties['href'])
            for key in sorted(properties.keys()):
                if key == 'href':
                    continue
                property_name = '%s%s' % (key[0].upper(), key[1:])
                if property_name in self.__class__.__dict__:
                    instances += '\n\t%s: %s' % (property_name, properties[key])
        return instances.strip('\n')

    def _build_payload(self, locals_dict, method_name=None):
        """Build and return a payload dictionary

        Ignore the following:
            key of self
            any key not in the internal dictionary
            value of None or Multivalue

        Returns: 
            dict: if there are items in the payload after processing of the locals_dict is complete
            None: if there are no items in the payload
        """
        from ixnetwork_restpy.multivalue import Multivalue
        payload = {}
        python_method_name = method_name
        if method_name is not None:
            python_method_name = '%s%s' % (method_name[0].upper(), method_name[1:])
        if locals_dict is not None:
            for key, value in locals_dict.items():
                if key == 'self' or value is None or isinstance(value, Multivalue):
                    continue
                if isclass(value) is True:
                    continue
                if method_name is not None:
                    attribute_name = key
                else:
                    attribute_name = key
                payload_value = self._build_value(key, value, method_name=python_method_name)
                if payload_value is not None:
                    payload[attribute_name] = payload_value
        if bool(payload) is True:
            return payload
        else:
            return None

    def _build_value(self, key, value, method_name=None, ignore_is_list=False):
        public_key = '%s%s' % (key[0].upper(), key[1:])
        if isinstance(value, Files):
            if value.is_local_file:
                base = self.href[0:self.href.find('ixnetwork') + len('ixnetwork')]
                filename = utils.quote(value.file_name)
                upload_url = '%s/files?filename=%s' % (base, filename)
                self._connection._execute(upload_url, payload=value)
            return value.file_name
        elif isinstance(value, Base):
            is_list = False
            if method_name is not None:
                if key == 'Arg1':
                    is_list = True
                else:
                    method_param = getattr(self.__class__, method_name).__doc__.replace('\n', '').replace('\t', '').replace(' ', '')
                    is_list = method_param.find('%s(list(' % key) != -1
            elif hasattr(self.__class__, public_key) is True:
                returns = getattr(self.__class__, public_key).__doc__.replace('\n', '').replace('\t', '').replace(' ', '')
                returns_pos = returns.find('Returns')
                is_list = returns_pos != -1 and returns.find('list(', returns_pos) != -1
            if is_list is True and ignore_is_list is False:
                hrefs = []
                for list_value in value:
                    hrefs.append(list_value.href)
                return hrefs
            else:
                return value.href
        elif isinstance(value, list):
            list_values = []
            for list_item in value:
                list_value = self._build_value(key, list_item, ignore_is_list=isinstance(list_item, Base))
                if list_value is not None:
                    list_values.append(list_value)
            return list_values
        else:
            return value

    def _create(self, locals_dict):
        payload = self._build_payload(locals_dict)
        url = '%s/%s' % (self._parent.href, self._SDM_NAME)
        properties = self._connection._create(url, payload)
        self._set_properties(properties)
        return self

    def _set_properties(self, properties, clear=False):
        from ixnetwork_restpy.multivalue import Multivalue

        if clear is True:
            self._clear()
        if properties is None:
            return

        # add an empty object dictionary to the internal list of object dictionaries
        self._object_properties.append(dict())
        self._index = len(self._object_properties) - 1

        # populate the current object dictionary
        # replace /multivalue object reference with a Multivalue object
        for key in properties.keys():
            value = properties[key]
            if key == 'links':
                continue
            else:
                self._properties[key] = value

        # if href is missing then try backfilling it using either links or id
        if 'href' not in self._properties.keys():
            if 'links' in properties.keys():
                self._properties['href'] = properties['links'][0]['href']
            elif 'id' in properties.keys():
                self._properties['href'] = '%s/%s/%s' % (self._parent.href, self._SDM_NAME, properties['id'])

    def _update(self, locals_dict):
        payload = self._build_payload(locals_dict)
        if payload is not None:
            self._connection._update(self.href, payload)
        return self

    def _delete(self):
        try:
            for properties in self._object_properties:
                url = '%s/%s/%s' % (self._parent.href, self._SDM_NAME, properties['id'])
                self._connection._delete(url)
            self._clear()
        except Exception as e:
            raise e

    def _execute(self, operation, child=None, payload=None, response_object=None):
        url = self.href
        if child is not None:
            url = '%s/%s' % (url, child)
        if operation is not None:
            url = '%s/operations/%s' % (url, operation.lower())
        payload = self._build_payload(payload, method_name=operation)
        response = None
        try:
            response = self._connection._execute(url, payload)
        except NotFoundError as notFoundError:
            # required due to SDM exec signatures with the same name but different types of Arg1
            if isinstance(payload['Arg1'], Base):
                payload['Arg1'] = payload['Arg1'].href
                response = self._connection._execute(url, payload)
            else:
                raise notFoundError
        if response_object is None:
            return response

    def refresh(self):
        """Refresh the contents of this object

        Returns
        -------
        - obj: self

        Raises
        ------
        - NotFoundError: The href does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        selects = []
        for properties in self._object_properties:
            selects.append(
                {
                    'from': self.href,
                    'properties': ['*'],
                    'children': [],
                    'inlines': []
                }
            )
        payload = {'selects': selects}
        end = len(self._parent.href)
        if 'ixnetwork' in self._parent.href:
            end = self._parent.href.index('ixnetwork') + len('ixnetwork')
        url = '%s/operations/select' % self._parent.href[0:end]
        responses = self._connection._execute(url, payload)
        self._set_properties(None, clear=True)
        # process from
        for response in responses:
            self._set_properties(response)
        self._index = len(self._object_properties) - 1
        return self

    def _read(self, href):
        response = self._connection._read(href)
        self._set_properties(response, clear=True)
        return self

    def __is_key_value_in_response(self, key_value, response):
        """Return whether or not a key is in a response
        """
        if isinstance(response, list):
            for item in response:
                if self.__is_key_value_in_response(key_value, item) is True:
                    return True
        elif isinstance(response, dict):
            if key_value in response.keys():
                return True
            for value in response.values():
                if self.__is_key_value_in_response(key_value, value) is True:
                    return True
        return False

    def _select(self, locals_dict=dict()):
        selects = []
        for parent in self._parent:
            selects.append(
                {
                    'from': parent.href,
                    'properties': [],
                    'children': [
                        {
                            'child': self._SDM_NAME,
                            'properties': ['*'],
                            'filters': []
                        }
                    ],
                    'inlines': []
                }
            )
        payload = {'selects': selects}
        for key in locals_dict.keys():
            if key == 'self' or locals_dict[key] is None or isclass(locals_dict[key]):
                continue
            child_filter = {
                'property': '%s%s' % (key[0].lower(), key[1:]),
                'regex': locals_dict[key]
            }
            for select in selects:
                select['children'][0]['filters'].append(child_filter)
        end = len(self._parent.href)
        if 'ixnetwork' in self._parent.href:
            end = self._parent.href.index('ixnetwork') + len('ixnetwork')
        url = '%s/operations/select' % self._parent.href[0:end]
        while True:
            responses = self._connection._execute(url, payload)
            if self.__is_key_value_in_response('objRef', responses) is False:
                break
        self._set_properties(None, clear=True)
        # process children of from
        for response in responses:
            if self._SDM_NAME in response.keys():
                if isinstance(response[self._SDM_NAME], list):
                    for item in response[self._SDM_NAME]:
                        self._set_properties(item)
                else:
                    self._set_properties(response[self._SDM_NAME])
        self._index = len(self._object_properties) - 1
        return self

    def _get_ngpf_device_ids(self, locals_dict=dict()):
        """Get NGPF device ids

        NGPF has a /topology/deviceGroup -count attribute that is used to set the devices per port
        Any NGPF class that has an operation that requires a list of session indices will have a GetDeviceIds method generated for it that calls into this method
        All parameters will be optional and defaulted to None
        The first parameter will always be a PortNames parameter defaulted to None
        This method will evaluate all non None criteria for matches

        e.g. System is configured with the following:
            20 vports using the default generated names
            2 topology with 10 vports assigned to each
            User wants to send arp on topology 1 only on ports 1 and 8
                ivp4_obj.SendArp(ipv4_obj.GetDeviceIds(PortName='^(Ethernet - 001|Ethernet - 008)$'))

        1. Find the starting topology reference by walking the href back to topology
        2. Find the starting index range based on the PortName
            2.a all other matches will be constrained by this starting index range


        Returns:
            list: a list of numeric sessionindices
        """
        # setup the device id map
        topology_url = self.href[0:self.href.index('deviceGroup') - 1]
        from ixnetwork_restpy.select import Select
        topology_results = Select(self._connection, topology_url,
                                  from_properties=['vports'],
                                  children=[{'child': 'deviceGroup', 'properties': ['count'], 'filters': []}],
                                  inlines=[{'child': 'vport', 'properties': ['name']}]).go()
        number_of_ports = len(topology_results[0]['vports'])
        total_devices = topology_results[0]['deviceGroup'][0]['count']
        devices_per_port = int(total_devices / number_of_ports)
        if sys.version_info >= (3, 0):
            device_ids = list(range(1, total_devices + 1))
        else:
            device_ids = range(1, total_devices + 1)

        for key, regex_pattern in locals_dict.items():
            if regex_pattern in [None, self]:
                continue
            regex = re.compile(regex_pattern)
            if key == 'PortNames':
                for i in range(len(topology_results[0]['vports'])):
                    if regex.search(topology_results[0]['vports'][i]['name']) is None:
                        device_ids[i * devices_per_port:i * devices_per_port + devices_per_port] = [0] * devices_per_port
            else:
                multivalue = getattr(self, key)
                values = multivalue.Values
                for i in range(len(values)):
                    if regex.search(values[i]) is None:
                        device_ids[i] = 0

        return [x for x in device_ids if x != 0]

    def _map_locals(self, sdm_att_map, locals_dict):
        mapped_dict = {}
        for key in locals_dict.keys():
            if key in sdm_att_map.keys():
                mapped_dict[sdm_att_map[key]] = locals_dict[key]
        return mapped_dict

    def info(self, message):
        """Add an INFO level message to the logger handlers

        Args
        ----
        - message (str): a message to be logged at INFO level
        """
        self._connection._info(message)

    def warn(self, message):
        """Add a WARN level message to the logger handlers

        Args
        ----
        - message (str): a message to be logged at WARN level
        """
        self._connection._warn(message)

    def debug(self, message):
        """Add a DEBUG level message to the logger handlers

        Args
        ----
        - message (str): a message to be logged at DEBUG level
        """
        self._connection._debug(message)

    def _is_str(self, value):
        """Portable determination if value is of type 'string'
        """
        return isinstance(value, ("".__class__, u"".__class__))
