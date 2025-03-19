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
from inspect import isclass, stack
from uhd_restpy.errors import NotFoundError
from uhd_restpy.files import Files
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
    _xpath returns the xpath of an object used by Config Assistant
    _xpathObj returns an object which consists of cached xpath dictionaries used by Config Assistant
    _isDependent denotes a dependent node used for some internal purpose Config Assistant
    """

    _SDM_NAME = None
    # new attributes added to slots for config assistant
    __slots__ = (
        "_object_properties",
        "_connection",
        "_parent",
        "_index",
        "_isDependent",
        "_xpath",
        "_xpathObj",
        "_mode",
        "_children",
        "_rootNode",
        "_dirty_objs",
    )

    def __init__(self, parent, list_op=False):
        self._xpathObj = None
        self._xpath = None
        self._isDependent = False
        self._parent = parent
        self._mode = ["normal"]
        self._rootNode = None
        self._children = {}
        self._dirty_objs = {}
        if self._parent is not None:
            self._connection = parent._connection
            self._xpathObj = parent._xpathObj
            self._mode = parent._mode
            self._children = parent._children
            self._rootNode = parent._rootNode
            self._dirty_objs = parent._dirty_objs

        self._set_properties(None, clear=True)
        # this particular piece of code actually removes the use of fnd operation, used by Config assistant
        # eg config.Vport.Protocols.find() ==> config.Vport.Protocols, similarly
        # eg config.Traffic.TrafficItem.ConfigElement.find() ==> config.Traffic.TrafficItem.ConfigElement
        # whenever class is called we make an xpath automatically by calling automate_xpath function, we avoid it if the
        # call comes from __getitem__ where we actually see the parameter list_op which tells its a list_op or not
        class_functions = dir(self)

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
            elif index < 0 and len(self._object_properties) + index in range(
                len(self._object_properties)
            ):
                index = len(self._object_properties) + index
            # included the list_op argument to inform init if it is a list operation
            item = self.__class__(self._parent, list_op=True)
            item._object_properties.append(self._object_properties[index])
            return item
        else:
            raise NotImplementedError(
                "support for index of %s is not implemented" % index
            )

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
        return self._get_attribute("href")

    @property
    def xpath(self):
        """
            The xpath reference of the current object used by config Assistant

        Returns
        -------
        - str the fully qualified xpath reference of the current object

        Raises
        -------
        - KeyError: The href key does not exist which means no resources have been retrieved from the server
        """
        return self._properties["xpath"]

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
            raise TypeError(
                "the parameter supplied is of %s but must be of <type '%s'>"
                % (type(object_to_test), arg_type.__name__)
            )

    def _get_attribute(self, name):
        """The main accessor for all attributes"""
        if self._mode[0] == "config":
            if name == "href":
                return self._properties[name]
            else:
                return name
        else:
            if len(self._object_properties) == 0:
                msg = (
                    "Failed to get the {}.{} property as the {} object has no "
                    "encapsulated resources. "
                ).format(self.__class__.__name__, name, self.__class__.__name__)
                if "find" in dir(self):
                    msg += (
                        "Either the {}.find() method was not called or it failed "
                        "to retrieve any resources from the server."
                    ).format(self.__class__.__name__)
                raise NotFoundError(msg)
            else:
                return self._properties[name]

    def _set_attribute(self, name, value):
        """Update a property on the server and save it locally if there is no exception"""
        # this first checks if the attribute in enum map and attribute value is a valid enum then specific code for
        # config assistant is added
        # generally if config assistant is use xpathObj will not be none but the mode varies from normal to config
        # we change the mode to normal after commit so tha operations and find works, we need to change the mode back to
        # config if they try to do some config operation that's why we have the elif condition
        if hasattr(self, "_SDM_ENUM_MAP"):
            self._check_for_enum_values(self._SDM_ENUM_MAP, attribute=[name, value])
        if self._mode[0] == "config":
            self._update_xpath_dict(name, value)
        else:
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
        instances = ""
        for i in range(len(self)):
            properties = self._object_properties[i]
            instances += "\n%s[%s]: %s" % (
                self.__class__.__name__,
                i,
                properties["href"],
            )
            for key in sorted(properties.keys()):
                if key == "href":
                    continue
                property_name = "%s%s" % (key[0].upper(), key[1:])
                if property_name in self.__class__.__dict__:
                    instances += "\n\t%s: %s" % (property_name, properties[key])
        return instances.strip("\n")

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
        from uhd_restpy.multivalue import Multivalue

        payload = {}
        python_method_name = method_name
        if method_name is not None:
            python_method_name = "%s%s" % (method_name[0].upper(), method_name[1:])
        if locals_dict is not None:
            for key, value in locals_dict.items():
                if key == "self" or value is None or isinstance(value, Multivalue):
                    continue
                if isclass(value) is True:
                    continue
                if method_name is not None:
                    attribute_name = key
                else:
                    attribute_name = key
                payload_value = self._build_value(
                    key, value, method_name=python_method_name
                )
                if payload_value is not None:
                    payload[attribute_name] = payload_value
        if bool(payload) is True:
            return payload
        else:
            return None

    def _build_value(self, key, value, method_name=None, ignore_is_list=False):
        public_key = "%s%s" % (key[0].upper(), key[1:])
        if isinstance(value, Files):
            if value.is_local_file:
                base = self.href[0 : self.href.find("ixnetwork") + len("ixnetwork")]
                filename = utils.quote(value.file_name)
                upload_url = "%s/files?filename=%s" % (base, filename)
                self._connection._execute(upload_url, payload=value)
            return value.file_name
        elif isinstance(value, Base):
            is_list = False
            if method_name is not None:
                if key == "Arg1":
                    is_list = True
                else:
                    method_param = (
                        getattr(self.__class__, method_name)
                        .__doc__.replace("\n", "")
                        .replace("\t", "")
                        .replace(" ", "")
                    )
                    is_list = method_param.find("%s(list(" % key) != -1
            elif hasattr(self.__class__, public_key) is True:
                returns = (
                    getattr(self.__class__, public_key)
                    .__doc__.replace("\n", "")
                    .replace("\t", "")
                    .replace(" ", "")
                )
                returns_pos = returns.find("Returns")
                is_list = returns_pos != -1 and returns.find("list(", returns_pos) != -1
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
                list_value = self._build_value(
                    key, list_item, ignore_is_list=isinstance(list_item, Base)
                )
                if list_value is not None:
                    list_values.append(list_value)
            return list_values
        else:
            return value

    def _create(self, locals_dict):
        # this first checks if the attribute in enum map and attribute value is a valid enum then specific code for
        # config assistant is added
        # generally if config assistant is use xpathObj will not be none but the mode varies from normal to config
        # we change the mode to normal after commit so tha operations and find works, we need to change the mode back to
        # config if they try to do some config operation that's why we have the elif condition
        if hasattr(self, "_SDM_ENUM_MAP"):
            self._check_for_enum_values(self._SDM_ENUM_MAP, local_dict=locals_dict)
        if self._mode[0] == "config":
            self._create_xpath_dict(self._SDM_NAME, locals_dict)
        else:
            payload = self._build_payload(locals_dict)
            url = "%s/%s" % (self._parent.href, self._SDM_NAME)
            properties = self._connection._create(url, payload)
            self._set_properties(properties)
        return self

    def _set_properties(self, properties, clear=False):
        from uhd_restpy.multivalue import Multivalue

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
            if key == "links":
                continue
            else:
                self._properties[key] = value

        # if href is missing then try backfilling it using either links or id
        if "href" not in self._properties.keys():
            if "links" in properties.keys():
                self._properties["href"] = properties["links"][0]["href"]
            elif "id" in properties.keys():
                self._properties["href"] = "%s/%s/%s" % (
                    self._parent.href,
                    self._SDM_NAME,
                    properties["id"],
                )

    def _update(self, locals_dict):
        if self._mode[0] == "config":
            self._update_xpath_dict(None, None, locals_dict)
        else:
            payload = self._build_payload(locals_dict)
            if payload is not None:
                payload_dict = {}
                for item in self:
                    item_dict = {}
                    item_dict.update(payload)
                    last_href_segment = item.href.split("/")[-1]
                    if last_href_segment.isdigit():
                        href = "/".join(item.href.split("/")[:-1])
                        item_dict["id"] = last_href_segment
                    else:
                        href = item.href
                    if payload_dict.get(href, None) is None:
                        payload_dict[href] = [item_dict]
                    else:
                        payload_dict[href].append(item_dict)
                for href in payload_dict.keys():
                    payload = (
                        payload_dict[href][0]
                        if len(payload_dict[href]) == 1
                        else payload_dict[href]
                    )
                    self._connection._update(href, payload)
            return self

    def _delete(self):
        # added code that if delete is called before commit and using config assistant it throws an exception
        try:
            for properties in self._object_properties:
                if "href" in properties:
                    url = "%s/%s/%s" % (
                        self._parent.href,
                        self._SDM_NAME,
                        properties["id"],
                    )
                    self._connection._delete(url)
            self._clear()
        except Exception as e:
            raise e

    def _execute(self, operation, child=None, payload=None, response_object=None):
        url = self.href
        if child is not None:
            url = "%s/%s" % (url, child)
        if operation is not None:
            url = "%s/operations/%s" % (url, operation.lower())
        payload = self._build_payload(payload, method_name=operation)
        response = None
        try:
            response = self._connection._execute(url, payload)
        except NotFoundError as notFoundError:
            # required due to SDM exec signatures with the same name but different types of Arg1
            if isinstance(payload["Arg1"], Base):
                payload["Arg1"] = payload["Arg1"].href
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
                    "from": properties["href"],
                    "properties": ["*"],
                    "children": [],
                    "inlines": [],
                }
            )
        payload = {"selects": selects}
        end = len(self._parent.href)
        if "ixnetwork" in self._parent.href:
            end = self._parent.href.index("ixnetwork") + len("ixnetwork")
        url = "%s/operations/select" % self._parent.href[0:end]
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
        """Return whether or not a key is in a response"""
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
        # this case is a bit different so both find and ._select hit this function and
        # we check the stack trace if it is find and used before commit we would raise an exception
        # but we have something like traffic._select() from property Traffic under ixnetwork we would automate the xpath
        # creation
        if self._mode[0] == "config":
            if stack()[1][3] != "find":
                self._automate_xpath(no_indexing=True)
                return self
        selects = []
        for parent in self._parent:
            selects.append(
                {
                    "from": parent.href,
                    "properties": [],
                    "children": [
                        {"child": self._SDM_NAME, "properties": ["*"], "filters": []}
                    ],
                    "inlines": [],
                }
            )
        payload = {"selects": selects}
        for key in locals_dict.keys():
            if key == "self" or locals_dict[key] is None or isclass(locals_dict[key]):
                continue
            child_filter = {
                "property": "%s%s" % (key[0].lower(), key[1:]),
                "regex": locals_dict[key],
            }
            for select in selects:
                select["children"][0]["filters"].append(child_filter)
        end = len(self._parent.href)
        if "ixnetwork" in self._parent.href:
            end = self._parent.href.index("ixnetwork") + len("ixnetwork")
        # changing select to xpath=true cause after find if we need to use config assistant again we would need
        # the xpath
        url = "{}/operations/select?xpath={}".format(
            self._parent.href[0:end],
            str(self._xpathObj is not None).lower(),
        )
        while True:
            responses = self._connection._execute(url, payload)
            if self.__is_key_value_in_response("objRef", responses) is False:
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
        topology_url = self.href[0 : self.href.index("deviceGroup") - 1]
        from uhd_restpy.select import Select

        topology_results = Select(
            self._connection,
            topology_url,
            from_properties=["vports"],
            children=[{"child": "deviceGroup", "properties": ["count"], "filters": []}],
            inlines=[{"child": "vport", "properties": ["name"]}],
        ).go()
        number_of_ports = len(topology_results[0]["vports"])
        total_devices = topology_results[0]["deviceGroup"][0]["count"]
        devices_per_port = int(total_devices / number_of_ports)
        if sys.version_info >= (3, 0):
            device_ids = list(range(1, total_devices + 1))
        else:
            device_ids = range(1, total_devices + 1)

        for key, regex_pattern in locals_dict.items():
            if regex_pattern in [None, self]:
                continue
            regex = re.compile(regex_pattern)
            if key == "PortNames":
                for i in range(len(topology_results[0]["vports"])):
                    if regex.search(topology_results[0]["vports"][i]["name"]) is None:
                        device_ids[
                            i * devices_per_port : i * devices_per_port
                            + devices_per_port
                        ] = [0] * devices_per_port
            else:
                multivalue = getattr(self, key)
                values = multivalue.Values
                for i in range(len(values)):
                    if regex.search(values[i]) is None:
                        device_ids[i] = 0

        return [x for x in device_ids if x != 0]

    def _map_locals(self, sdm_att_map, locals_dict):
        mapped_dict = {}

        # Should also handle functions with kwargs
        locals_dict = locals_dict["kwargs"] if "kwargs" in locals_dict else locals_dict

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
        """Portable determination if value is of type 'string'"""
        return isinstance(value, ("".__class__, "".__class__))

    def get_async_response(self):
        return self._connection._get_async_response()

    def _add_xpath(self, locals_dict):
        """
        This function is actually for dependent objects like vlan, bgp_ethernet_stack etc.
        Its different from add function, its only allowed for config assistant
        """
        # if self._index == 0 and not self._isDependent:
        #     self._object_properties = []
        #     self._index = len(self._object_properties) - 1
        #     self._isDependent = True
        if self._mode[0] == "config":
            self._create_xpath_dict(self._SDM_NAME, locals_dict)
        else:
            raise Exception("This feature is only available with Batch Assistance")
        return self

    def _create_xpath(self, name, no_indexing=False):
        """
        This function basically creates the xpath, the no_indexing argument is used to tell which classes does not
        need indexing in their xpath and which classes need them
        """
        # this skip list is for some special use case in Config assistant where we need to avoid indexing for these
        # classes
        skip = ["protocols", "stack"]
        if self.parent.__class__.__name__ == "Ixnetwork":
            path = "/" + name
        else:
            path = self.parent._properties["xpath"] + "/" + name

        self._index += 1
        if not no_indexing and name not in skip:
            self._xpath = path + "[" + str(self._index + 1) + "]"
        else:
            self._xpath = path

    def _create_xpath_dict(self, name, local_dict):
        """
        This function basically creates a dictionary and ultimately pushes it in the xpathObj object
        It has two segments one which creates xpath for normal nodes and one which does for traffic fields
        and ultimately sets the properties.
        """
        if self._parent.__class__.__name__ == "Stack":
            self._parent._stack_index += 1
            local_dict["stack_index"] = self._parent._stack_index
            self._index += 1
        else:
            # self._create_xpath(name)
            self._index += 1
            self._fill_href_child_name()
        # xpath_dict = dict()
        # xpath_dict["xpath"] = self._xpath
        # for key in local_dict.keys():
        #     if key == "self" or local_dict[key] is None:
        #         continue
        #     else:
        #         value = self._get_value(key, local_dict[key])
        #         xpath_dict[key] = value

        # self._xpathObj._config.append(xpath_dict)
        self._set_xpath_properties(local_dict)

    def _set_xpath_properties(self, properties, clear=False):
        """
        This function is at par with the _set_properties but is used for config assistant
        one added feature is that it caches the current object in the parent object properties
        so it helps to maintain the hierarchy.
        """
        if clear is True:
            self._clear()

        temp_dict = dict()
        temp_dict["xpath"] = ""
        temp_dict["sdm_name"] = self._SDM_NAME
        temp_dict["parent_property"] = self.parent._properties
        temp_dict["id"] = self.index + 1
        # temp_dict['href'] = self._create_href(self._SDM_NAME)
        if self._parent.__class__.__name__ == "Stack":
            temp_dict["stack_index"] = self._parent._stack_index
            # self._set_parent_stack_properties(self._parent)
        if properties is not None:
            for key in properties.keys():
                if key == "self" or properties[key] is None:
                    continue
                else:
                    value = self._get_value(key, properties[key])
                    temp_dict[key] = value

        self._object_properties.append(temp_dict)
        self._parent._object_properties[self._parent._index][
            self.__class__.__name__
        ] = self

    def _get_value(self, key, value, ignore_is_list=False):
        """
        This function is at par with _build_value function, used for Config Assistant
        """
        public_key = "%s%s" % (key[0].upper(), key[1:])
        if isinstance(value, Base):
            is_list = False
            if hasattr(self.__class__, public_key) is True:
                returns = (
                    getattr(self.__class__, public_key)
                    .__doc__.replace("\n", "")
                    .replace("\t", "")
                    .replace(" ", "")
                )
                returns_pos = returns.find("Returns")
                is_list = returns_pos != -1 and returns.find("list(", returns_pos) != -1
            if is_list is True and ignore_is_list is False:
                xpath_list = []
                for list_value in value:
                    xpath_list.append(list_value._properties)
                return xpath_list
            else:
                return value._properties
        elif isinstance(value, list):
            list_values = []
            for list_item in value:
                list_value = self._get_value(
                    key, list_item, ignore_is_list=isinstance(list_item, Base)
                )
                if list_value is not None:
                    list_values.append(list_value)
            return list_values
        else:
            return value

    def _update_xpath_dict(self, key, value, properties=None):
        """
        This function actually sets a property in the json, called from _set_attribute function
        """
        dirty_properties = {}
        if properties is not None:
            for key in properties.keys():
                if key == "self" or properties[key] is None:
                    continue
                else:
                    value = self._get_value(key, properties[key])
                    self._properties[key] = value
                    dirty_properties[key] = value
        else:
            final_value = self._get_value(key, value)
            self._properties[key] = final_value
            dirty_properties[key] = final_value

        if "href" in self._properties:
            dirty_properties.update({"href": self.href})
            parent_href = ""
            if self.parent.__class__.__name__ == "Ixnetwork":
                parent_href = "/"
            elif self.href.split("/")[-1].isdigit():
                parent_href = "/".join(self.href.split("/")[:-2])
            else:
                parent_href = "/".join(self.href.split("/")[:-1])

            if parent_href not in self._dirty_objs:
                self._dirty_objs[parent_href] = []
                self._dirty_objs[parent_href].append(
                    {self._SDM_NAME: [dirty_properties]}
                )
            else:
                child_present = False
                for dirty_child in self._dirty_objs[parent_href]:
                    if self._SDM_NAME in dirty_child.keys():
                        property_present = False
                        for dirty_prop in dirty_child[self._SDM_NAME]:
                            if self.href in dirty_prop:
                                dirty_prop.update(dirty_properties)
                                property_present = True
                                break
                        if not property_present:
                            dirty_child[self._SDM_NAME].append(dirty_properties)
                        child_present = True
                        break

                if not child_present:
                    self._dirty_objs[parent_href].append(
                        {self._SDM_NAME: [dirty_properties]}
                    )
        # if "xpath" not in self._properties:
        #     self._create_xpath(self._SDM_NAME)
        # xpath_present = False
        # for dict in self._xpathObj._config:
        #     if dict["xpath"] == self._properties["xpath"]:
        #         dict[key] = final_value
        #         xpath_present = True
        #         break
        # if not xpath_present:
        #     temp_dict = {"xpath": self._properties["xpath"], key: value}
        #     self._xpathObj._config.append(temp_dict)

    def _automate_xpath(self, no_indexing=False):
        """
        This function automatically adds an xpath to the object
        """
        self._create_xpath_dict(self._SDM_NAME, {"no_indexing": no_indexing})

    def _find_xpath_obj(self):
        if self._xpath is None:
            self._create_xpath(self._SDM_NAME)
            self._fill_href_child_name()
            self._set_xpath_properties(None)
        return self

    def _create_template_xpath(self):
        """
        This function basically forms the xpath for traffic fields and protocol templates
        """
        self._parent._stack_index += 1
        template_name = self._SDM_NAME + "-" + str(self._parent._stack_index)
        self._xpath = self._parent._xpath + "[@alias = '" + template_name + "']"

    def _fill_href_child_name(self):
        """
        This function prepares a string for the nodes which we need to pass in the select to get the hrefs after
        commit and used for filling up the existing objects with those.
        example string: {<obj>: ['vport', 'protocols'],  <obj>: 'deviceGroup|ethernet', <obj> : 'traffic'}
        """
        # print('1', self._SDM_NAME, self.parent._SDM_NAME)
        if self.parent.__class__.__name__ == "Ixnetwork":
            if len(self._children) == 0 or self._parent not in self._children:
                self._children[self.parent] = [self._SDM_NAME]
                self._rootNode = self.parent
                self._parent._rootNode = self.parent
            else:
                if (
                    len(
                        list(
                            filter(
                                lambda x: self._SDM_NAME in x, self._children.values()
                            )
                        )
                    )
                    == 0
                ):
                    self._children[self.parent].append(self._SDM_NAME)
                self._rootNode = self.parent
        else:
            # obj_considered = False
            # # print('1', self._SDM_NAME, id(self.parent))
            # for key, child_str in self._children.items():
            #     if self.parent._SDM_NAME in child_str and self._SDM_NAME not in child_str:
            #         self._children[key].append(self._SDM_NAME)
            #         obj_considered = True
            #         break
            #     elif self._SDM_NAME in child_str:
            #         # if (self.parent._SDM_NAME == child_str[0] and self.parent is not key) or \
            #         #         (self._SDM_NAME == child_str[0] and self is not key):
            #         #     obj_considered = False
            #         #     break
            #         # else:
            #         # if self.parent._SDM_NAME == child_str[0] and 'href' in self.parent._properties:
            #         #     self._children[self.parent] = [href]
            #         obj_considered = True
            #
            # # print('2', self._children.values())
            # if not obj_considered:
            #     self._children[self.parent] = [self._SDM_NAME]

            # new case where we store the root nod concept
            if self._rootNode is None:
                self._children[self.parent] = [self._SDM_NAME]
                self._rootNode = self.parent
                self._parent._rootNode = self.parent
            elif self._SDM_NAME not in self._children[self._rootNode]:
                if (
                    self._rootNode._SDM_NAME == "ixnetwork"
                    and self._parent._SDM_NAME not in self._children[self._rootNode]
                ):
                    self._children[self.parent] = [self._SDM_NAME]
                    self._rootNode = self.parent
                    self._parent._rootNode = self.parent
                else:
                    self._children[self._rootNode].append(self._SDM_NAME)
        # print('3', self._children.values())

    def _check_for_enum_values(self, enum_map, local_dict=None, attribute=None):
        """
        This function basically does a check for correct enum values for attributes and throws an exception
        """
        if len(enum_map) < 0:
            return
        if local_dict is not None:
            for key, value in local_dict.items():
                if key == "self" or value is None:
                    continue
                if enum_map.get(key, None) is not None and value not in enum_map[key]:
                    raise Exception(
                        "%s is not a valid value for attribute %s allowed values are %s"
                        % (value, str(key), str(enum_map[key]))
                    )
        if attribute is not None:
            if (
                enum_map.get(attribute[0], None) is not None
                and attribute[1] not in enum_map[attribute[0]]
            ):
                raise Exception(
                    "%s is not a valid value  for attribute %s allowed values are %s"
                    % (attribute[1], str(attribute[0]), str(enum_map[attribute[0]]))
                )

    def _raise_exception(self):
        """
        This function basically raises an exception for operations before commit
        """
        raise Exception(
            "You are not allowed to use this function before commit in config mode"
        )
