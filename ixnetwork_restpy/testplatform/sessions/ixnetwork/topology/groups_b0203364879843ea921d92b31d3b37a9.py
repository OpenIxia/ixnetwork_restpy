# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files
from typing import List, Any, Union


class Groups(Base):
    """Openflow Groups Configuration
    The Groups class encapsulates a list of groups resources that are managed by the system.
    A list of resources can be retrieved from the server using the Groups.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'groups'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ChannelName': 'channelName',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'GroupAdvertise': 'groupAdvertise',
        'GroupDescription': 'groupDescription',
        'GroupId': 'groupId',
        'GroupType': 'groupType',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberOfBuckets': 'numberOfBuckets',
        'OfChannel': 'ofChannel',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Groups, self).__init__(parent, list_op)

    @property
    def Buckets(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.buckets_bd4257b6720604ee2ee57801dd96774d.Buckets): An instance of the Buckets class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.buckets_bd4257b6720604ee2ee57801dd96774d import Buckets
        if self._properties.get('Buckets', None) is not None:
            return self._properties.get('Buckets')
        else:
            return Buckets(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ChannelName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Parent Channel Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChannelName'])

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def GroupAdvertise(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, group is advertised when the OpenFlow channel comes up.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAdvertise']))

    @property
    def GroupDescription(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A description of the group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupDescription']))

    @property
    def GroupId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 32-bit integer uniquely identifying the group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupId']))

    @property
    def GroupType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the type of group to determine the group semantics.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupType']))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NumberOfBuckets(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the number of Buckets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBuckets'])
    @NumberOfBuckets.setter
    def NumberOfBuckets(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfBuckets'], value)

    @property
    def OfChannel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The OF Channel to which the group belongs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OfChannel']))

    def update(self, Multiplier=None, Name=None, NumberOfBuckets=None):
        # type: (int, str, int) -> Groups
        """Updates groups resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBuckets (number): Specify the number of Buckets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Multiplier=None, Name=None, NumberOfBuckets=None):
        # type: (int, str, int) -> Groups
        """Adds a new groups resource on the json, only valid with config assistant

        Args
        ----
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBuckets (number): Specify the number of Buckets.

        Returns
        -------
        - self: This instance with all currently retrieved groups resources using find and the newly added groups resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ChannelName=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, NumberOfBuckets=None):
        # type: (str, int, str, int, str, int) -> Groups
        """Finds and retrieves groups resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groups resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groups resources from the server.

        Args
        ----
        - ChannelName (str): Parent Channel Name
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBuckets (number): Specify the number of Buckets.

        Returns
        -------
        - self: This instance with matching groups resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groups data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groups resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SendAllGroupAdd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendAllGroupAdd operation on the server.

        Sends a Group Add on all groups.

        sendAllGroupAdd(async_operation=bool)list
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendAllGroupAdd', payload=payload, response_object=None)

    def SendAllGroupRemove(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendAllGroupRemove operation on the server.

        Sends a Group Remove on all groups.

        sendAllGroupRemove(async_operation=bool)list
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendAllGroupRemove', payload=payload, response_object=None)

    def SendGroupAdd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendGroupAdd operation on the server.

        Sends a Group Add on selected Group.

        sendGroupAdd(Arg2=list, async_operation=bool)list
        -------------------------------------------------
        - Arg2 (list(number)): List of indices into the group range grid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendGroupAdd', payload=payload, response_object=None)

    def SendGroupRemove(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendGroupRemove operation on the server.

        Sends a Group Remove on selected Group.

        sendGroupRemove(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the group range grid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendGroupRemove', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, GroupAdvertise=None, GroupDescription=None, GroupId=None, GroupType=None, OfChannel=None):
        """Base class infrastructure that gets a list of groups device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - GroupAdvertise (str): optional regex of groupAdvertise
        - GroupDescription (str): optional regex of groupDescription
        - GroupId (str): optional regex of groupId
        - GroupType (str): optional regex of groupType
        - OfChannel (str): optional regex of ofChannel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
