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


class UpGroupInfo(Base):
    """UP Group level Configuration
    The UpGroupInfo class encapsulates a list of upGroupInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the UpGroupInfo.find() method.
    The list can be managed by using the UpGroupInfo.add() and UpGroupInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'upGroupInfo'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BasAccessType': 'basAccessType',
        'BurstInterval': 'burstInterval',
        'Capabilities': 'capabilities',
        'CardsPerSlot': 'cardsPerSlot',
        'ConfigureAccessType': 'configureAccessType',
        'ConfigureBrasSubInterface': 'configureBrasSubInterface',
        'ConfigureCuspChannel': 'configureCuspChannel',
        'ConfigureVlan': 'configureVlan',
        'ConfigureVxlanChannel': 'configureVxlanChannel',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'CpVxlanIPv4Address': 'cpVxlanIPv4Address',
        'CpVxlanIPv6Address': 'cpVxlanIPv6Address',
        'CvlanPerSubint': 'cvlanPerSubint',
        'DeadTimer': 'deadTimer',
        'DescriptiveName': 'descriptiveName',
        'EnableBurstUpdates': 'enableBurstUpdates',
        'Errors': 'errors',
        'EstablishmentTimer': 'establishmentTimer',
        'HelloVendorID': 'helloVendorID',
        'IPv4Address': 'iPv4Address',
        'IPv6Address': 'iPv6Address',
        'InterfaceType': 'interfaceType',
        'KeepaliveTimer': 'keepaliveTimer',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NetconfCpIPv4Address': 'netconfCpIPv4Address',
        'NumberOfDhcpUsers': 'numberOfDhcpUsers',
        'NumberOfIPv4AddressPools': 'numberOfIPv4AddressPools',
        'NumberOfL2tpUsers': 'numberOfL2tpUsers',
        'NumberOfPppoeUsers': 'numberOfPppoeUsers',
        'NumberOfStaticUsers': 'numberOfStaticUsers',
        'NumberofSlots': 'numberofSlots',
        'PacketsPerBurst': 'packetsPerBurst',
        'PeVid': 'peVid',
        'PeVlanPriority': 'peVlanPriority',
        'PortsPerCard': 'portsPerCard',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StartCardNumber': 'startCardNumber',
        'StartCvlanId': 'startCvlanId',
        'StartPortNumber': 'startPortNumber',
        'StartSlotNumber': 'startSlotNumber',
        'StartSubIntNumber': 'startSubIntNumber',
        'StartSvlanId': 'startSvlanId',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SubVersion': 'subVersion',
        'SubintPerPort': 'subintPerPort',
        'SvlanPerSubint': 'svlanPerSubint',
        'Upcapabilities': 'upcapabilities',
        'VendorID': 'vendorID',
        'Version': 'version',
        'Vni': 'vni',
        'VxlanIPv4Address': 'vxlanIPv4Address',
        'VxlanIPv6Address': 'vxlanIPv6Address',
    }
    _SDM_ENUM_MAP = {
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(UpGroupInfo, self).__init__(parent, list_op)

    @property
    def CuspCPIPv4AddressPoolList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpipv4addresspoollist_455d9f6528efb822a61db2ff9130065f.CuspCPIPv4AddressPoolList): An instance of the CuspCPIPv4AddressPoolList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpipv4addresspoollist_455d9f6528efb822a61db2ff9130065f import CuspCPIPv4AddressPoolList
        if self._properties.get('CuspCPIPv4AddressPoolList', None) is not None:
            return self._properties.get('CuspCPIPv4AddressPoolList')
        else:
            return CuspCPIPv4AddressPoolList(self)._select()

    @property
    def DhcpUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpuserslist_e5e3c66a65cccc690b826096fb798f1c.DhcpUsersList): An instance of the DhcpUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpuserslist_e5e3c66a65cccc690b826096fb798f1c import DhcpUsersList
        if self._properties.get('DhcpUsersList', None) is not None:
            return self._properties.get('DhcpUsersList')
        else:
            return DhcpUsersList(self)._select()

    @property
    def L2tpUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l2tpuserslist_ba900382a58f148e1eb5e9560d26bd76.L2tpUsersList): An instance of the L2tpUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l2tpuserslist_ba900382a58f148e1eb5e9560d26bd76 import L2tpUsersList
        if self._properties.get('L2tpUsersList', None) is not None:
            return self._properties.get('L2tpUsersList')
        else:
            return L2tpUsersList(self)._select()

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        if self._properties.get('LearnedInfo', None) is not None:
            return self._properties.get('LearnedInfo')
        else:
            return LearnedInfo(self)

    @property
    def PppoEUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoeuserslist_5c8b22bccea414256df02bdb69e3a5aa.PppoEUsersList): An instance of the PppoEUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoeuserslist_5c8b22bccea414256df02bdb69e3a5aa import PppoEUsersList
        if self._properties.get('PppoEUsersList', None) is not None:
            return self._properties.get('PppoEUsersList')
        else:
            return PppoEUsersList(self)._select()

    @property
    def StaticUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticuserslist_6e510ac3a5bcd21e2ded020484d06cc2.StaticUsersList): An instance of the StaticUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticuserslist_6e510ac3a5bcd21e2ded020484d06cc2 import StaticUsersList
        if self._properties.get('StaticUsersList', None) is not None:
            return self._properties.get('StaticUsersList')
        else:
            return StaticUsersList(self)._select()

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
    def BasAccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BAS Access Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BasAccessType']))

    @property
    def BurstInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst Interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BurstInterval']))

    @property
    def Capabilities(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CpWaitUserObjectAck.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Capabilities']))

    @property
    def CardsPerSlot(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of cards per slot.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CardsPerSlot']))

    @property
    def ConfigureAccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure BRAS Function.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureAccessType']))

    @property
    def ConfigureBrasSubInterface(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure BRAS Sub-Interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureBrasSubInterface']))

    @property
    def ConfigureCuspChannel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure CUSP channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureCuspChannel']))

    @property
    def ConfigureVlan(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure VLAN under Sub-Interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureVlan']))

    @property
    def ConfigureVxlanChannel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure VXLAN channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureVxlanChannel']))

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

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
    def CpVxlanIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the CP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CpVxlanIPv4Address']))

    @property
    def CpVxlanIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the CP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CpVxlanIPv6Address']))

    @property
    def CvlanPerSubint(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CVLAN count per sub-interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CvlanPerSubint']))

    @property
    def DeadTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Dead Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DeadTimer']))

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
    def EnableBurstUpdates(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable sending burst of update packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBurstUpdates']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def EstablishmentTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Establishment Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EstablishmentTimer']))

    @property
    def HelloVendorID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Vendor ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloVendorID']))

    @property
    def IPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv4Address']))

    @property
    def IPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UP IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv6Address']))

    @property
    def InterfaceType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of the interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterfaceType']))

    @property
    def KeepaliveTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Keepalive Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeepaliveTimer']))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
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
    def NetconfCpIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetconfCpIPv4Address']))

    @property
    def NumberOfDhcpUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of DHCP Subscriber Groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfDhcpUsers'])
    @NumberOfDhcpUsers.setter
    def NumberOfDhcpUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfDhcpUsers'], value)

    @property
    def NumberOfIPv4AddressPools(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of IPv4 Address Pools
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfIPv4AddressPools'])
    @NumberOfIPv4AddressPools.setter
    def NumberOfIPv4AddressPools(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfIPv4AddressPools'], value)

    @property
    def NumberOfL2tpUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of L2TP Subscriber Groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfL2tpUsers'])
    @NumberOfL2tpUsers.setter
    def NumberOfL2tpUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfL2tpUsers'], value)

    @property
    def NumberOfPppoeUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of PPPoE Subscriber Groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfPppoeUsers'])
    @NumberOfPppoeUsers.setter
    def NumberOfPppoeUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfPppoeUsers'], value)

    @property
    def NumberOfStaticUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Static Subscribers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfStaticUsers'])
    @NumberOfStaticUsers.setter
    def NumberOfStaticUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfStaticUsers'], value)

    @property
    def NumberofSlots(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of solts.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberofSlots']))

    @property
    def PacketsPerBurst(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packets Per Burst.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PacketsPerBurst']))

    @property
    def PeVid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PE VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeVid']))

    @property
    def PeVlanPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PE VLAN Priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeVlanPriority']))

    @property
    def PortsPerCard(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of ports per card.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortsPerCard']))

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StartCardNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Starting number of the card.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartCardNumber']))

    @property
    def StartCvlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Starting ID of CVLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartCvlanId']))

    @property
    def StartPortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Starting number of the port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartPortNumber']))

    @property
    def StartSlotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Startig number of the slot.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSlotNumber']))

    @property
    def StartSubIntNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub-Interface Number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSubIntNumber']))

    @property
    def StartSvlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Starting ID of SVLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSvlanId']))

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def SubVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub Version
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubVersion']))

    @property
    def SubintPerPort(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Sub-Interfaces per port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubintPerPort']))

    @property
    def SvlanPerSubint(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SVLAN count per sub-interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SvlanPerSubint']))

    @property
    def Upcapabilities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Up Capabilities
        """
        return self._get_attribute(self._SDM_ATT_MAP['Upcapabilities'])
    @Upcapabilities.setter
    def Upcapabilities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Upcapabilities'], value)

    @property
    def VendorID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Vendor ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VendorID']))

    @property
    def Version(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CUSP Protocol Version
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Vni(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VXLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vni']))

    @property
    def VxlanIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VxlanIPv4Address']))

    @property
    def VxlanIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VxlanIPv6Address']))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfDhcpUsers=None, NumberOfIPv4AddressPools=None, NumberOfL2tpUsers=None, NumberOfPppoeUsers=None, NumberOfStaticUsers=None, StackedLayers=None, Upcapabilities=None):
        # type: (List[str], int, str, int, int, int, int, int, List[str], int) -> UpGroupInfo
        """Updates upGroupInfo resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfDhcpUsers (number): Number of DHCP Subscriber Groups.
        - NumberOfIPv4AddressPools (number): Number of IPv4 Address Pools
        - NumberOfL2tpUsers (number): Number of L2TP Subscriber Groups.
        - NumberOfPppoeUsers (number): Number of PPPoE Subscriber Groups.
        - NumberOfStaticUsers (number): Number of Static Subscribers.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - Upcapabilities (number): Up Capabilities

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfDhcpUsers=None, NumberOfIPv4AddressPools=None, NumberOfL2tpUsers=None, NumberOfPppoeUsers=None, NumberOfStaticUsers=None, StackedLayers=None, Upcapabilities=None):
        # type: (List[str], int, str, int, int, int, int, int, List[str], int) -> UpGroupInfo
        """Adds a new upGroupInfo resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfDhcpUsers (number): Number of DHCP Subscriber Groups.
        - NumberOfIPv4AddressPools (number): Number of IPv4 Address Pools
        - NumberOfL2tpUsers (number): Number of L2TP Subscriber Groups.
        - NumberOfPppoeUsers (number): Number of PPPoE Subscriber Groups.
        - NumberOfStaticUsers (number): Number of Static Subscribers.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - Upcapabilities (number): Up Capabilities

        Returns
        -------
        - self: This instance with all currently retrieved upGroupInfo resources using find and the newly added upGroupInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained upGroupInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, NumberOfDhcpUsers=None, NumberOfIPv4AddressPools=None, NumberOfL2tpUsers=None, NumberOfPppoeUsers=None, NumberOfStaticUsers=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, Upcapabilities=None):
        """Finds and retrieves upGroupInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve upGroupInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all upGroupInfo resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfDhcpUsers (number): Number of DHCP Subscriber Groups.
        - NumberOfIPv4AddressPools (number): Number of IPv4 Address Pools
        - NumberOfL2tpUsers (number): Number of L2TP Subscriber Groups.
        - NumberOfPppoeUsers (number): Number of PPPoE Subscriber Groups.
        - NumberOfStaticUsers (number): Number of Static Subscribers.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - Upcapabilities (number): Up Capabilities

        Returns
        -------
        - self: This instance with matching upGroupInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of upGroupInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the upGroupInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def ClearAllLearnedInfoInClient(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllLearnedInfoInClient operation on the server.

        Clears ALL routes from GUI grid for the selected BGP Peers.

        clearAllLearnedInfoInClient(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute('clearAllLearnedInfoInClient', payload=payload, response_object=None)

    def GetAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getAllLearnedInfo operation on the server.

        Fetches Subscriber Learned Info.

        getAllLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute('getAllLearnedInfo', payload=payload, response_object=None)

    def GetDHCPLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getDHCPLearnedInfo operation on the server.

        Fetches Subscriber Learned Info.

        getDHCPLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute('getDHCPLearnedInfo', payload=payload, response_object=None)

    def GetL2TPLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getL2TPLearnedInfo operation on the server.

        Fetches Subscriber Learned Info.

        getL2TPLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute('getL2TPLearnedInfo', payload=payload, response_object=None)

    def GetPPPLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPPPLearnedInfo operation on the server.

        Fetches Subscriber Learned Info.

        getPPPLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute('getPPPLearnedInfo', payload=payload, response_object=None)

    def GetUPResourceInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getUPResourceInfo operation on the server.

        Fetches IPv4 routes learnt by this BGP peer.

        getUPResourceInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute('getUPResourceInfo', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def SendUpdateDeleteBursts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendUpdateDeleteBursts operation on the server.

        Trigger to send burts of update request packets.

        sendUpdateDeleteBursts(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
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
        return self._execute('sendUpdateDeleteBursts', payload=payload, response_object=None)

    def SendUpdateRequestBursts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendUpdateRequestBursts operation on the server.

        Trigger to send burts of update request packets.

        sendUpdateRequestBursts(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
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
        return self._execute('sendUpdateRequestBursts', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, BasAccessType=None, BurstInterval=None, Capabilities=None, CardsPerSlot=None, ConfigureAccessType=None, ConfigureBrasSubInterface=None, ConfigureCuspChannel=None, ConfigureVlan=None, ConfigureVxlanChannel=None, CpVxlanIPv4Address=None, CpVxlanIPv6Address=None, CvlanPerSubint=None, DeadTimer=None, EnableBurstUpdates=None, EstablishmentTimer=None, HelloVendorID=None, IPv4Address=None, IPv6Address=None, InterfaceType=None, KeepaliveTimer=None, NetconfCpIPv4Address=None, NumberofSlots=None, PacketsPerBurst=None, PeVid=None, PeVlanPriority=None, PortsPerCard=None, StartCardNumber=None, StartCvlanId=None, StartPortNumber=None, StartSlotNumber=None, StartSubIntNumber=None, StartSvlanId=None, SubVersion=None, SubintPerPort=None, SvlanPerSubint=None, VendorID=None, Version=None, Vni=None, VxlanIPv4Address=None, VxlanIPv6Address=None):
        """Base class infrastructure that gets a list of upGroupInfo device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BasAccessType (str): optional regex of basAccessType
        - BurstInterval (str): optional regex of burstInterval
        - Capabilities (str): optional regex of capabilities
        - CardsPerSlot (str): optional regex of cardsPerSlot
        - ConfigureAccessType (str): optional regex of configureAccessType
        - ConfigureBrasSubInterface (str): optional regex of configureBrasSubInterface
        - ConfigureCuspChannel (str): optional regex of configureCuspChannel
        - ConfigureVlan (str): optional regex of configureVlan
        - ConfigureVxlanChannel (str): optional regex of configureVxlanChannel
        - CpVxlanIPv4Address (str): optional regex of cpVxlanIPv4Address
        - CpVxlanIPv6Address (str): optional regex of cpVxlanIPv6Address
        - CvlanPerSubint (str): optional regex of cvlanPerSubint
        - DeadTimer (str): optional regex of deadTimer
        - EnableBurstUpdates (str): optional regex of enableBurstUpdates
        - EstablishmentTimer (str): optional regex of establishmentTimer
        - HelloVendorID (str): optional regex of helloVendorID
        - IPv4Address (str): optional regex of iPv4Address
        - IPv6Address (str): optional regex of iPv6Address
        - InterfaceType (str): optional regex of interfaceType
        - KeepaliveTimer (str): optional regex of keepaliveTimer
        - NetconfCpIPv4Address (str): optional regex of netconfCpIPv4Address
        - NumberofSlots (str): optional regex of numberofSlots
        - PacketsPerBurst (str): optional regex of packetsPerBurst
        - PeVid (str): optional regex of peVid
        - PeVlanPriority (str): optional regex of peVlanPriority
        - PortsPerCard (str): optional regex of portsPerCard
        - StartCardNumber (str): optional regex of startCardNumber
        - StartCvlanId (str): optional regex of startCvlanId
        - StartPortNumber (str): optional regex of startPortNumber
        - StartSlotNumber (str): optional regex of startSlotNumber
        - StartSubIntNumber (str): optional regex of startSubIntNumber
        - StartSvlanId (str): optional regex of startSvlanId
        - SubVersion (str): optional regex of subVersion
        - SubintPerPort (str): optional regex of subintPerPort
        - SvlanPerSubint (str): optional regex of svlanPerSubint
        - VendorID (str): optional regex of vendorID
        - Version (str): optional regex of version
        - Vni (str): optional regex of vni
        - VxlanIPv4Address (str): optional regex of vxlanIPv4Address
        - VxlanIPv6Address (str): optional regex of vxlanIPv6Address

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
