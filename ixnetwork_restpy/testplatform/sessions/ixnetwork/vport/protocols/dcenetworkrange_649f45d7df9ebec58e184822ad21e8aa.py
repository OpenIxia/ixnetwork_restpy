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


class DceNetworkRange(Base):
    """Sets the Network Range for a particular DCE ISIS router.
    The DceNetworkRange class encapsulates a list of dceNetworkRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceNetworkRange.find() method.
    The list can be managed by using the DceNetworkRange.add() and DceNetworkRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceNetworkRange'
    _SDM_ATT_MAP = {
        'AdvertiseNetworkRange': 'advertiseNetworkRange',
        'BroadcastRootPriorityStep': 'broadcastRootPriorityStep',
        'CapabilityRouterId': 'capabilityRouterId',
        'EnableHostName': 'enableHostName',
        'EnableMultiTopology': 'enableMultiTopology',
        'EntryCol': 'entryCol',
        'EntryRow': 'entryRow',
        'HostNamePrefix': 'hostNamePrefix',
        'InterfaceMetric': 'interfaceMetric',
        'LinkType': 'linkType',
        'NoOfCols': 'noOfCols',
        'NoOfRows': 'noOfRows',
        'NumberOfMultiDestinationTrees': 'numberOfMultiDestinationTrees',
        'StartBroadcastRootPriority': 'startBroadcastRootPriority',
        'StartSwitchId': 'startSwitchId',
        'StartSystemId': 'startSystemId',
        'SwitchIdPriority': 'switchIdPriority',
        'SwitchIdStep': 'switchIdStep',
        'SystemIdIncrementBy': 'systemIdIncrementBy',
    }

    def __init__(self, parent):
        super(DceNetworkRange, self).__init__(parent)

    @property
    def DceNodeIpv4Groups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodeipv4groups_6b38a306d1902845b0170d6a9e9b016c.DceNodeIpv4Groups): An instance of the DceNodeIpv4Groups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodeipv4groups_6b38a306d1902845b0170d6a9e9b016c import DceNodeIpv4Groups
        return DceNodeIpv4Groups(self)

    @property
    def DceNodeIpv6Groups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodeipv6groups_d39b93291c370eeac7c5ff151e5839b7.DceNodeIpv6Groups): An instance of the DceNodeIpv6Groups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodeipv6groups_d39b93291c370eeac7c5ff151e5839b7 import DceNodeIpv6Groups
        return DceNodeIpv6Groups(self)

    @property
    def DceNodeMacGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodemacgroups_34e1724b78ebdaead9952262e204cb39.DceNodeMacGroups): An instance of the DceNodeMacGroups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodemacgroups_34e1724b78ebdaead9952262e204cb39 import DceNodeMacGroups
        return DceNodeMacGroups(self)

    @property
    def DceNodeTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodetopologyrange_a60b1fb5614d89a53ce60d4c9c2448a8.DceNodeTopologyRange): An instance of the DceNodeTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodetopologyrange_a60b1fb5614d89a53ce60d4c9c2448a8 import DceNodeTopologyRange
        return DceNodeTopologyRange(self)

    @property
    def DceOutsideLinks(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dceoutsidelinks_448ca86781afc72591d4b730ba434c0d.DceOutsideLinks): An instance of the DceOutsideLinks class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dceoutsidelinks_448ca86781afc72591d4b730ba434c0d import DceOutsideLinks
        return DceOutsideLinks(self)

    @property
    def TrillNodeMacRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillnodemacranges_bf9812019b5a6f083e449b4094986684.TrillNodeMacRanges): An instance of the TrillNodeMacRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillnodemacranges_bf9812019b5a6f083e449b4094986684 import TrillNodeMacRanges
        return TrillNodeMacRanges(self)

    @property
    def AdvertiseNetworkRange(self):
        """
        Returns
        -------
        - bool: If true, this DCE ISIS Network Range is advertised.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseNetworkRange'])
    @AdvertiseNetworkRange.setter
    def AdvertiseNetworkRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseNetworkRange'], value)

    @property
    def BroadcastRootPriorityStep(self):
        """DEPRECATED 
        Returns
        -------
        - number: The increment step of the Broadcast Root Priority of this emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BroadcastRootPriorityStep'])
    @BroadcastRootPriorityStep.setter
    def BroadcastRootPriorityStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BroadcastRootPriorityStep'], value)

    @property
    def CapabilityRouterId(self):
        """
        Returns
        -------
        - str: The IP address format of Capability Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CapabilityRouterId'])
    @CapabilityRouterId.setter
    def CapabilityRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CapabilityRouterId'], value)

    @property
    def EnableHostName(self):
        """
        Returns
        -------
        - bool: If true, the given dynamic host name is transmitted in all the packets sent from this router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHostName'])
    @EnableHostName.setter
    def EnableHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHostName'], value)

    @property
    def EnableMultiTopology(self):
        """
        Returns
        -------
        - bool: Enables more than one topology (distribution tree) corresponding to the given R bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMultiTopology'])
    @EnableMultiTopology.setter
    def EnableMultiTopology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMultiTopology'], value)

    @property
    def EntryCol(self):
        """
        Returns
        -------
        - number: The value in this field is used in combination with entry row to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryCol'])
    @EntryCol.setter
    def EntryCol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryCol'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: The value in this field is used in combination with entry column to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

    @property
    def HostNamePrefix(self):
        """
        Returns
        -------
        - str: Allows to add a prefix to the generated host name of this router. When host name prefix is provided, the generated host name is appended by -1 for the first router and subsequently increased by 1 for each router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostNamePrefix'])
    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostNamePrefix'], value)

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - number: The metric cost associated with this emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric'])
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceMetric'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast): For DCE ISIS emulation type, the type of network link is set to Point-Point and made read-only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])

    @property
    def NoOfCols(self):
        """
        Returns
        -------
        - number: The value in this field is used in combination with number of rows to create a matrix (grid) for a network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCols'])
    @NoOfCols.setter
    def NoOfCols(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfCols'], value)

    @property
    def NoOfRows(self):
        """
        Returns
        -------
        - number: The value in this field is used in combination with number of columns to create a matrix (grid) for a network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRows'])
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRows'], value)

    @property
    def NumberOfMultiDestinationTrees(self):
        """DEPRECATED 
        Returns
        -------
        - number: The number of Multi-Destination Trees for the DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfMultiDestinationTrees'])
    @NumberOfMultiDestinationTrees.setter
    def NumberOfMultiDestinationTrees(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfMultiDestinationTrees'], value)

    @property
    def StartBroadcastRootPriority(self):
        """DEPRECATED 
        Returns
        -------
        - number: The starting value of the Broadcast Root Priority of this DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartBroadcastRootPriority'])
    @StartBroadcastRootPriority.setter
    def StartBroadcastRootPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartBroadcastRootPriority'], value)

    @property
    def StartSwitchId(self):
        """DEPRECATED 
        Returns
        -------
        - number: The Switch ID of this emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSwitchId'])
    @StartSwitchId.setter
    def StartSwitchId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSwitchId'], value)

    @property
    def StartSystemId(self):
        """
        Returns
        -------
        - str: The System ID assigned to the starting DCE ISIS router in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSystemId'])
    @StartSystemId.setter
    def StartSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSystemId'], value)

    @property
    def SwitchIdPriority(self):
        """DEPRECATED 
        Returns
        -------
        - number: The Switch ID priority of this DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchIdPriority'])
    @SwitchIdPriority.setter
    def SwitchIdPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchIdPriority'], value)

    @property
    def SwitchIdStep(self):
        """DEPRECATED 
        Returns
        -------
        - number: The increment value by which the Switch ID of the DCE ISIS router increases.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchIdStep'])
    @SwitchIdStep.setter
    def SwitchIdStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchIdStep'], value)

    @property
    def SystemIdIncrementBy(self):
        """
        Returns
        -------
        - str: The incremented System ID used when more than one router is emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemIdIncrementBy'])
    @SystemIdIncrementBy.setter
    def SystemIdIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SystemIdIncrementBy'], value)

    def update(self, AdvertiseNetworkRange=None, BroadcastRootPriorityStep=None, CapabilityRouterId=None, EnableHostName=None, EnableMultiTopology=None, EntryCol=None, EntryRow=None, HostNamePrefix=None, InterfaceMetric=None, NoOfCols=None, NoOfRows=None, NumberOfMultiDestinationTrees=None, StartBroadcastRootPriority=None, StartSwitchId=None, StartSystemId=None, SwitchIdPriority=None, SwitchIdStep=None, SystemIdIncrementBy=None):
        """Updates dceNetworkRange resource on the server.

        Args
        ----
        - AdvertiseNetworkRange (bool): If true, this DCE ISIS Network Range is advertised.
        - BroadcastRootPriorityStep (number): The increment step of the Broadcast Root Priority of this emulated DCE ISIS router.
        - CapabilityRouterId (str): The IP address format of Capability Router.
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - EnableMultiTopology (bool): Enables more than one topology (distribution tree) corresponding to the given R bridge.
        - EntryCol (number): The value in this field is used in combination with entry row to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        - EntryRow (number): The value in this field is used in combination with entry column to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        - HostNamePrefix (str): Allows to add a prefix to the generated host name of this router. When host name prefix is provided, the generated host name is appended by -1 for the first router and subsequently increased by 1 for each router.
        - InterfaceMetric (number): The metric cost associated with this emulated DCE ISIS router.
        - NoOfCols (number): The value in this field is used in combination with number of rows to create a matrix (grid) for a network range.
        - NoOfRows (number): The value in this field is used in combination with number of columns to create a matrix (grid) for a network range.
        - NumberOfMultiDestinationTrees (number): The number of Multi-Destination Trees for the DCE ISIS router.
        - StartBroadcastRootPriority (number): The starting value of the Broadcast Root Priority of this DCE ISIS router.
        - StartSwitchId (number): The Switch ID of this emulated DCE ISIS router.
        - StartSystemId (str): The System ID assigned to the starting DCE ISIS router in this network range.
        - SwitchIdPriority (number): The Switch ID priority of this DCE ISIS router.
        - SwitchIdStep (number): The increment value by which the Switch ID of the DCE ISIS router increases.
        - SystemIdIncrementBy (str): The incremented System ID used when more than one router is emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertiseNetworkRange=None, BroadcastRootPriorityStep=None, CapabilityRouterId=None, EnableHostName=None, EnableMultiTopology=None, EntryCol=None, EntryRow=None, HostNamePrefix=None, InterfaceMetric=None, NoOfCols=None, NoOfRows=None, NumberOfMultiDestinationTrees=None, StartBroadcastRootPriority=None, StartSwitchId=None, StartSystemId=None, SwitchIdPriority=None, SwitchIdStep=None, SystemIdIncrementBy=None):
        """Adds a new dceNetworkRange resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseNetworkRange (bool): If true, this DCE ISIS Network Range is advertised.
        - BroadcastRootPriorityStep (number): The increment step of the Broadcast Root Priority of this emulated DCE ISIS router.
        - CapabilityRouterId (str): The IP address format of Capability Router.
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - EnableMultiTopology (bool): Enables more than one topology (distribution tree) corresponding to the given R bridge.
        - EntryCol (number): The value in this field is used in combination with entry row to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        - EntryRow (number): The value in this field is used in combination with entry column to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        - HostNamePrefix (str): Allows to add a prefix to the generated host name of this router. When host name prefix is provided, the generated host name is appended by -1 for the first router and subsequently increased by 1 for each router.
        - InterfaceMetric (number): The metric cost associated with this emulated DCE ISIS router.
        - NoOfCols (number): The value in this field is used in combination with number of rows to create a matrix (grid) for a network range.
        - NoOfRows (number): The value in this field is used in combination with number of columns to create a matrix (grid) for a network range.
        - NumberOfMultiDestinationTrees (number): The number of Multi-Destination Trees for the DCE ISIS router.
        - StartBroadcastRootPriority (number): The starting value of the Broadcast Root Priority of this DCE ISIS router.
        - StartSwitchId (number): The Switch ID of this emulated DCE ISIS router.
        - StartSystemId (str): The System ID assigned to the starting DCE ISIS router in this network range.
        - SwitchIdPriority (number): The Switch ID priority of this DCE ISIS router.
        - SwitchIdStep (number): The increment value by which the Switch ID of the DCE ISIS router increases.
        - SystemIdIncrementBy (str): The incremented System ID used when more than one router is emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.

        Returns
        -------
        - self: This instance with all currently retrieved dceNetworkRange resources using find and the newly added dceNetworkRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceNetworkRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertiseNetworkRange=None, BroadcastRootPriorityStep=None, CapabilityRouterId=None, EnableHostName=None, EnableMultiTopology=None, EntryCol=None, EntryRow=None, HostNamePrefix=None, InterfaceMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, NumberOfMultiDestinationTrees=None, StartBroadcastRootPriority=None, StartSwitchId=None, StartSystemId=None, SwitchIdPriority=None, SwitchIdStep=None, SystemIdIncrementBy=None):
        """Finds and retrieves dceNetworkRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceNetworkRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceNetworkRange resources from the server.

        Args
        ----
        - AdvertiseNetworkRange (bool): If true, this DCE ISIS Network Range is advertised.
        - BroadcastRootPriorityStep (number): The increment step of the Broadcast Root Priority of this emulated DCE ISIS router.
        - CapabilityRouterId (str): The IP address format of Capability Router.
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - EnableMultiTopology (bool): Enables more than one topology (distribution tree) corresponding to the given R bridge.
        - EntryCol (number): The value in this field is used in combination with entry row to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        - EntryRow (number): The value in this field is used in combination with entry column to specify which 'virtual' router in the Network Range is connected to the current ISIS L2/L3 Router.
        - HostNamePrefix (str): Allows to add a prefix to the generated host name of this router. When host name prefix is provided, the generated host name is appended by -1 for the first router and subsequently increased by 1 for each router.
        - InterfaceMetric (number): The metric cost associated with this emulated DCE ISIS router.
        - LinkType (str(pointToPoint | broadcast)): For DCE ISIS emulation type, the type of network link is set to Point-Point and made read-only.
        - NoOfCols (number): The value in this field is used in combination with number of rows to create a matrix (grid) for a network range.
        - NoOfRows (number): The value in this field is used in combination with number of columns to create a matrix (grid) for a network range.
        - NumberOfMultiDestinationTrees (number): The number of Multi-Destination Trees for the DCE ISIS router.
        - StartBroadcastRootPriority (number): The starting value of the Broadcast Root Priority of this DCE ISIS router.
        - StartSwitchId (number): The Switch ID of this emulated DCE ISIS router.
        - StartSystemId (str): The System ID assigned to the starting DCE ISIS router in this network range.
        - SwitchIdPriority (number): The Switch ID priority of this DCE ISIS router.
        - SwitchIdStep (number): The increment value by which the Switch ID of the DCE ISIS router increases.
        - SystemIdIncrementBy (str): The incremented System ID used when more than one router is emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.

        Returns
        -------
        - self: This instance with matching dceNetworkRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceNetworkRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceNetworkRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
