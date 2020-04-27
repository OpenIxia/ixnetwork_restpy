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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class EndpointSet(Base):
    """This object helps to set the endpoint set of a traffic item.
    The EndpointSet class encapsulates a list of endpointSet resources that are managed by the user.
    A list of resources can be retrieved from the server using the EndpointSet.find() method.
    The list can be managed by using the EndpointSet.add() and EndpointSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'endpointSet'

    def __init__(self, parent):
        super(EndpointSet, self).__init__(parent)

    @property
    def AllowEmptyTopologySets(self):
        """
        Returns
        -------
        - bool: Enable this to allow the setting of sources and destinations without throwing an error even if the combination produces an empty topology set.
        """
        return self._get_attribute('allowEmptyTopologySets')
    @AllowEmptyTopologySets.setter
    def AllowEmptyTopologySets(self, value):
        self._set_attribute('allowEmptyTopologySets', value)

    @property
    def DestinationFilter(self):
        """
        Returns
        -------
        - str: The list of conditions used for filtering destinations endpoints.
        """
        return self._get_attribute('destinationFilter')
    @DestinationFilter.setter
    def DestinationFilter(self, value):
        self._set_attribute('destinationFilter', value)

    @property
    def Destinations(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*]): Indicates the number of destination endpoints configured.
        """
        return self._get_attribute('destinations')
    @Destinations.setter
    def Destinations(self, value):
        self._set_attribute('destinations', value)

    @property
    def DestinationsDescription(self):
        """
        Returns
        -------
        - str: Summary description of destination endpoints.
        """
        return self._get_attribute('destinationsDescription')

    @property
    def FullyMeshedEndpoints(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*]): 
        """
        return self._get_attribute('fullyMeshedEndpoints')
    @FullyMeshedEndpoints.setter
    def FullyMeshedEndpoints(self, value):
        self._set_attribute('fullyMeshedEndpoints', value)

    @property
    def FullyMeshedEndpointsDescription(self):
        """
        Returns
        -------
        - str: Summary description of fully meshed endpoints.
        """
        return self._get_attribute('fullyMeshedEndpointsDescription')

    @property
    def MulticastDestinations(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[igmp | mld | none],arg3:str,arg4:str,arg5:number)): A compact representation of many virtual multicast destinations. Each list item consists of 5 values where the first two, a bool value and enum value, can be defaulted to false and none. The next two values are a starting address and step address which can be either an ipv4, ipv6 or streamId and the last value is a count of addresses.
        """
        return self._get_attribute('multicastDestinations')
    @MulticastDestinations.setter
    def MulticastDestinations(self, value):
        self._set_attribute('multicastDestinations', value)

    @property
    def MulticastReceivers(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number)): A list of virtual multicast receivers. Each list item consists of a multicast receiver object reference, port index, host index and group or join/prune index depending on the type of object reference.
        """
        return self._get_attribute('multicastReceivers')
    @MulticastReceivers.setter
    def MulticastReceivers(self, value):
        self._set_attribute('multicastReceivers', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the endpoint set.
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NgpfFilters(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:list[number])): The list of next generation structures used to filter endpoints. The structure consists of a string tag and list of integer indexes.
        """
        return self._get_attribute('ngpfFilters')
    @NgpfFilters.setter
    def NgpfFilters(self, value):
        self._set_attribute('ngpfFilters', value)

    @property
    def ScalableDestinations(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number)): A list of scalable destination structures
        """
        return self._get_attribute('scalableDestinations')
    @ScalableDestinations.setter
    def ScalableDestinations(self, value):
        self._set_attribute('scalableDestinations', value)

    @property
    def ScalableSources(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number)): A list of scalable source structures.
        """
        return self._get_attribute('scalableSources')
    @ScalableSources.setter
    def ScalableSources(self, value):
        self._set_attribute('scalableSources', value)

    @property
    def SourceFilter(self):
        """
        Returns
        -------
        - str: The list of conditions used for filtering source endpoints.
        """
        return self._get_attribute('sourceFilter')
    @SourceFilter.setter
    def SourceFilter(self, value):
        self._set_attribute('sourceFilter', value)

    @property
    def Sources(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*]): Indicates the number of source endpoints configured.
        """
        return self._get_attribute('sources')
    @Sources.setter
    def Sources(self, value):
        self._set_attribute('sources', value)

    @property
    def SourcesDescription(self):
        """
        Returns
        -------
        - str: Summary description of source endpoints.
        """
        return self._get_attribute('sourcesDescription')

    @property
    def TrafficGroups(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../*]): Indicates the traffic groups selected in the source/destination endpoint set.
        """
        return self._get_attribute('trafficGroups')
    @TrafficGroups.setter
    def TrafficGroups(self, value):
        self._set_attribute('trafficGroups', value)

    def update(self, AllowEmptyTopologySets=None, DestinationFilter=None, Destinations=None, FullyMeshedEndpoints=None, MulticastDestinations=None, MulticastReceivers=None, Name=None, NgpfFilters=None, ScalableDestinations=None, ScalableSources=None, SourceFilter=None, Sources=None, TrafficGroups=None):
        """Updates endpointSet resource on the server.

        Args
        ----
        - AllowEmptyTopologySets (bool): Enable this to allow the setting of sources and destinations without throwing an error even if the combination produces an empty topology set.
        - DestinationFilter (str): The list of conditions used for filtering destinations endpoints.
        - Destinations (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): Indicates the number of destination endpoints configured.
        - FullyMeshedEndpoints (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): 
        - MulticastDestinations (list(dict(arg1:bool,arg2:str[igmp | mld | none],arg3:str,arg4:str,arg5:number))): A compact representation of many virtual multicast destinations. Each list item consists of 5 values where the first two, a bool value and enum value, can be defaulted to false and none. The next two values are a starting address and step address which can be either an ipv4, ipv6 or streamId and the last value is a count of addresses.
        - MulticastReceivers (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number))): A list of virtual multicast receivers. Each list item consists of a multicast receiver object reference, port index, host index and group or join/prune index depending on the type of object reference.
        - Name (str): The name of the endpoint set.
        - NgpfFilters (list(dict(arg1:str,arg2:list[number]))): The list of next generation structures used to filter endpoints. The structure consists of a string tag and list of integer indexes.
        - ScalableDestinations (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number))): A list of scalable destination structures
        - ScalableSources (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number))): A list of scalable source structures.
        - SourceFilter (str): The list of conditions used for filtering source endpoints.
        - Sources (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): Indicates the number of source endpoints configured.
        - TrafficGroups (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../*])): Indicates the traffic groups selected in the source/destination endpoint set.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AllowEmptyTopologySets=None, DestinationFilter=None, Destinations=None, FullyMeshedEndpoints=None, MulticastDestinations=None, MulticastReceivers=None, Name=None, NgpfFilters=None, ScalableDestinations=None, ScalableSources=None, SourceFilter=None, Sources=None, TrafficGroups=None):
        """Adds a new endpointSet resource on the server and adds it to the container.

        Args
        ----
        - AllowEmptyTopologySets (bool): Enable this to allow the setting of sources and destinations without throwing an error even if the combination produces an empty topology set.
        - DestinationFilter (str): The list of conditions used for filtering destinations endpoints.
        - Destinations (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): Indicates the number of destination endpoints configured.
        - FullyMeshedEndpoints (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): 
        - MulticastDestinations (list(dict(arg1:bool,arg2:str[igmp | mld | none],arg3:str,arg4:str,arg5:number))): A compact representation of many virtual multicast destinations. Each list item consists of 5 values where the first two, a bool value and enum value, can be defaulted to false and none. The next two values are a starting address and step address which can be either an ipv4, ipv6 or streamId and the last value is a count of addresses.
        - MulticastReceivers (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number))): A list of virtual multicast receivers. Each list item consists of a multicast receiver object reference, port index, host index and group or join/prune index depending on the type of object reference.
        - Name (str): The name of the endpoint set.
        - NgpfFilters (list(dict(arg1:str,arg2:list[number]))): The list of next generation structures used to filter endpoints. The structure consists of a string tag and list of integer indexes.
        - ScalableDestinations (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number))): A list of scalable destination structures
        - ScalableSources (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number))): A list of scalable source structures.
        - SourceFilter (str): The list of conditions used for filtering source endpoints.
        - Sources (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): Indicates the number of source endpoints configured.
        - TrafficGroups (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../*])): Indicates the traffic groups selected in the source/destination endpoint set.

        Returns
        -------
        - self: This instance with all currently retrieved endpointSet resources using find and the newly added endpointSet resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained endpointSet resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AllowEmptyTopologySets=None, DestinationFilter=None, Destinations=None, DestinationsDescription=None, FullyMeshedEndpoints=None, FullyMeshedEndpointsDescription=None, MulticastDestinations=None, MulticastReceivers=None, Name=None, NgpfFilters=None, ScalableDestinations=None, ScalableSources=None, SourceFilter=None, Sources=None, SourcesDescription=None, TrafficGroups=None):
        """Finds and retrieves endpointSet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve endpointSet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all endpointSet resources from the server.

        Args
        ----
        - AllowEmptyTopologySets (bool): Enable this to allow the setting of sources and destinations without throwing an error even if the combination produces an empty topology set.
        - DestinationFilter (str): The list of conditions used for filtering destinations endpoints.
        - Destinations (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): Indicates the number of destination endpoints configured.
        - DestinationsDescription (str): Summary description of destination endpoints.
        - FullyMeshedEndpoints (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): 
        - FullyMeshedEndpointsDescription (str): Summary description of fully meshed endpoints.
        - MulticastDestinations (list(dict(arg1:bool,arg2:str[igmp | mld | none],arg3:str,arg4:str,arg5:number))): A compact representation of many virtual multicast destinations. Each list item consists of 5 values where the first two, a bool value and enum value, can be defaulted to false and none. The next two values are a starting address and step address which can be either an ipv4, ipv6 or streamId and the last value is a count of addresses.
        - MulticastReceivers (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number))): A list of virtual multicast receivers. Each list item consists of a multicast receiver object reference, port index, host index and group or join/prune index depending on the type of object reference.
        - Name (str): The name of the endpoint set.
        - NgpfFilters (list(dict(arg1:str,arg2:list[number]))): The list of next generation structures used to filter endpoints. The structure consists of a string tag and list of integer indexes.
        - ScalableDestinations (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number))): A list of scalable destination structures
        - ScalableSources (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/topology/.../*],arg2:number,arg3:number,arg4:number,arg5:number))): A list of scalable source structures.
        - SourceFilter (str): The list of conditions used for filtering source endpoints.
        - Sources (list(str[None | /api/v1/sessions/1/ixnetwork/lag/.../* | /api/v1/sessions/1/ixnetwork/topology/.../* | /api/v1/sessions/1/ixnetwork/traffic/.../* | /api/v1/sessions/1/ixnetwork/vport/.../*])): Indicates the number of source endpoints configured.
        - SourcesDescription (str): Summary description of source endpoints.
        - TrafficGroups (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../*])): Indicates the traffic groups selected in the source/destination endpoint set.

        Returns
        -------
        - self: This instance with matching endpointSet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of endpointSet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the endpointSet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def FindMulticastReceiverGroupIndex(self, *args, **kwargs):
        """Executes the findMulticastReceiverGroupIndex operation on the server.

        This will lookup the multicast receiver group index from the multicast provider using the group id start/step/count which can then be used as the group index argument in the endpointSet multicastReceivers struct.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        findMulticastReceiverGroupIndex(Arg2=href, Arg3=string, Arg4=string, Arg5=number)number
        ---------------------------------------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): A valid object reference
        - Arg3 (str): The multicast group id start value
        - Arg4 (str): The multicast group id step value
        - Arg5 (number): The multicast group id count value
        - Returns number: The index of the multicast group id.

        findMulticastReceiverGroupIndex(Arg2=href, Arg3=string)number
        -------------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/topology)): A valid object reference
        - Arg3 (str): The multicast group id which must be an eight digit hex value separated by colons i.e., 00:00:01:01:00:01:01:00.
        - Returns number: The index of the multicast group id.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('findMulticastReceiverGroupIndex', payload=payload, response_object=None)
