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


class Interface(Base):
    """This object is a network interface.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'AdvertiseNetworkRange': 'advertiseNetworkRange',
        'AreaId': 'areaId',
        'AuthenticationMethods': 'authenticationMethods',
        'AuthenticationPassword': 'authenticationPassword',
        'BBit': 'bBit',
        'ConnectedToDut': 'connectedToDut',
        'DeadInterval': 'deadInterval',
        'EBit': 'eBit',
        'EnableAdvertiseRouterLsaLoopback': 'enableAdvertiseRouterLsaLoopback',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableFastHello': 'enableFastHello',
        'Enabled': 'enabled',
        'EntryColumn': 'entryColumn',
        'EntryRow': 'entryRow',
        'HelloInterval': 'helloInterval',
        'HelloMultiplier': 'helloMultiplier',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceIpAddress': 'interfaceIpAddress',
        'InterfaceIpMaskAddress': 'interfaceIpMaskAddress',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'IsLearnedInfoRefreshed': 'isLearnedInfoRefreshed',
        'LinkTypes': 'linkTypes',
        'Md5AuthenticationKey': 'md5AuthenticationKey',
        'Md5AuthenticationKeyId': 'md5AuthenticationKeyId',
        'Metric': 'metric',
        'Mtu': 'mtu',
        'NeighborIpAddress': 'neighborIpAddress',
        'NeighborRouterId': 'neighborRouterId',
        'NetworkRangeIp': 'networkRangeIp',
        'NetworkRangeIpByMask': 'networkRangeIpByMask',
        'NetworkRangeIpIncrementBy': 'networkRangeIpIncrementBy',
        'NetworkRangeIpMask': 'networkRangeIpMask',
        'NetworkRangeLinkType': 'networkRangeLinkType',
        'NetworkRangeRouterId': 'networkRangeRouterId',
        'NetworkRangeRouterIdIncrementBy': 'networkRangeRouterIdIncrementBy',
        'NetworkRangeTeEnable': 'networkRangeTeEnable',
        'NetworkRangeTeMaxBandwidth': 'networkRangeTeMaxBandwidth',
        'NetworkRangeTeMetric': 'networkRangeTeMetric',
        'NetworkRangeTeResMaxBandwidth': 'networkRangeTeResMaxBandwidth',
        'NetworkRangeTeUnreservedBwPriority': 'networkRangeTeUnreservedBwPriority',
        'NetworkType': 'networkType',
        'NoOfCols': 'noOfCols',
        'NoOfRows': 'noOfRows',
        'Options': 'options',
        'Priority': 'priority',
        'ProtocolInterface': 'protocolInterface',
        'ShowExternal': 'showExternal',
        'ShowNssa': 'showNssa',
        'TeAdminGroup': 'teAdminGroup',
        'TeEnable': 'teEnable',
        'TeMaxBandwidth': 'teMaxBandwidth',
        'TeMetricLevel': 'teMetricLevel',
        'TeResMaxBandwidth': 'teResMaxBandwidth',
        'TeUnreservedBwPriority': 'teUnreservedBwPriority',
        'ValidateReceivedMtuSize': 'validateReceivedMtuSize',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def LearnedFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_eefb8bda61928c41bfe3478f93e66c1f.LearnedFilter): An instance of the LearnedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_eefb8bda61928c41bfe3478f93e66c1f import LearnedFilter
        return LearnedFilter(self)._select()

    @property
    def LearnedLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_f8981275ed1dafbf0040b50e74f8ef42.LearnedLsa): An instance of the LearnedLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_f8981275ed1dafbf0040b50e74f8ef42 import LearnedLsa
        return LearnedLsa(self)

    @property
    def AdvertiseNetworkRange(self):
        """
        Returns
        -------
        - bool: Enables the advertisement of the OSPF network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseNetworkRange'])
    @AdvertiseNetworkRange.setter
    def AdvertiseNetworkRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseNetworkRange'], value)

    @property
    def AreaId(self):
        """
        Returns
        -------
        - number: The OSPF area ID associated with the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AreaId'])
    @AreaId.setter
    def AreaId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AreaId'], value)

    @property
    def AuthenticationMethods(self):
        """
        Returns
        -------
        - str(null | password | md5): The type of authentication to be used on this link interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthenticationMethods'])
    @AuthenticationMethods.setter
    def AuthenticationMethods(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthenticationMethods'], value)

    @property
    def AuthenticationPassword(self):
        """
        Returns
        -------
        - str: Enter a clear-text 64-bit password. A password is configured at each end of the link. The password is inserted as is into the packet, and is compared upon receipt at the other end of the link. The received packet is dropped if the contained password does not match the configured password.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthenticationPassword'])
    @AuthenticationPassword.setter
    def AuthenticationPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthenticationPassword'], value)

    @property
    def BBit(self):
        """
        Returns
        -------
        - bool: Indicates that this router is an Area Border Router (ABR).
        """
        return self._get_attribute(self._SDM_ATT_MAP['BBit'])
    @BBit.setter
    def BBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BBit'], value)

    @property
    def ConnectedToDut(self):
        """
        Returns
        -------
        - bool: Indicates that this OSPF interface is directly connected to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedToDut'])
    @ConnectedToDut.setter
    def ConnectedToDut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedToDut'], value)

    @property
    def DeadInterval(self):
        """
        Returns
        -------
        - number: The number of seconds allowed before declaring a silent router as being down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeadInterval'])
    @DeadInterval.setter
    def DeadInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeadInterval'], value)

    @property
    def EBit(self):
        """
        Returns
        -------
        - bool: External bit. Specifies how AS-external-LSAs are flooded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EBit'])
    @EBit.setter
    def EBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EBit'], value)

    @property
    def EnableAdvertiseRouterLsaLoopback(self):
        """
        Returns
        -------
        - bool: If true, advertises the router's LSA loopback address. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdvertiseRouterLsaLoopback'])
    @EnableAdvertiseRouterLsaLoopback.setter
    def EnableAdvertiseRouterLsaLoopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdvertiseRouterLsaLoopback'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: Indicates if a BFD session is to be created to the OSPF peer IP address once the OSPF session is established. This allows OSPF to use BFD to maintain IPv4 connectivity the OSPF peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def EnableFastHello(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastHello'])
    @EnableFastHello.setter
    def EnableFastHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastHello'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the simulated interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EntryColumn(self):
        """
        Returns
        -------
        - number: The column where the entry point router is located in the OSPFnetwork range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryColumn'])
    @EntryColumn.setter
    def EntryColumn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryColumn'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: The row where the entry point router is located in the OSPF network range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: The number of seconds between Hello packets sent from an Ixia router. The Ixia state machine sends Hello packets at this interval for all of the defined interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def HelloMultiplier(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloMultiplier'])
    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloMultiplier'], value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this OSPF interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIndex'])
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIndex'], value)

    @property
    def InterfaceIpAddress(self):
        """
        Returns
        -------
        - str: The IP address for this OSPF interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIpAddress'])
    @InterfaceIpAddress.setter
    def InterfaceIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIpAddress'], value)

    @property
    def InterfaceIpMaskAddress(self):
        """
        Returns
        -------
        - str: The IP mask associated with the IP address for this interface. Only used if protocolInterfaceDescription is empty. (default = 255.255.255.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIpMaskAddress'])
    @InterfaceIpMaskAddress.setter
    def InterfaceIpMaskAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIpMaskAddress'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str: The type of interface to be selected for this OSPF interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, refreshes learned information automatically.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedInfoRefreshed'])

    @property
    def LinkTypes(self):
        """
        Returns
        -------
        - str(pointToPoint | transit | stub | virtual): Indicates the type of network link for the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkTypes'])
    @LinkTypes.setter
    def LinkTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkTypes'], value)

    @property
    def Md5AuthenticationKey(self):
        """
        Returns
        -------
        - str: If authenticationMethod is set to ospfInterfaceAuthenticationMD5, then this is MD5 key ID used for authentication. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5AuthenticationKey'])
    @Md5AuthenticationKey.setter
    def Md5AuthenticationKey(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Md5AuthenticationKey'], value)

    @property
    def Md5AuthenticationKeyId(self):
        """
        Returns
        -------
        - number: A value to be used as a key ID associated with the MD5 key.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5AuthenticationKeyId'])
    @Md5AuthenticationKeyId.setter
    def Md5AuthenticationKeyId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Md5AuthenticationKeyId'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: A user-assigned routing metric associated with the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: The maximum transmission unit (MTU) that is allowed on this link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def NeighborIpAddress(self):
        """
        Returns
        -------
        - str: If the link type is a point to point network, this is the address of the other end of the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborIpAddress'])
    @NeighborIpAddress.setter
    def NeighborIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NeighborIpAddress'], value)

    @property
    def NeighborRouterId(self):
        """
        Returns
        -------
        - str: When the linkType option is set to ospfInterfaceLinkPointToPoint, then this option should be set to the ID of the router on the other end of the point-to-point connection. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborRouterId'])
    @NeighborRouterId.setter
    def NeighborRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NeighborRouterId'], value)

    @property
    def NetworkRangeIp(self):
        """
        Returns
        -------
        - str: The IP address for the first OSPFv2 network to be advertised in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIp'])
    @NetworkRangeIp.setter
    def NetworkRangeIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIp'], value)

    @property
    def NetworkRangeIpByMask(self):
        """
        Returns
        -------
        - bool: The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpByMask'])
    @NetworkRangeIpByMask.setter
    def NetworkRangeIpByMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIpByMask'], value)

    @property
    def NetworkRangeIpIncrementBy(self):
        """
        Returns
        -------
        - str: The step size by which to automatically increment the IP addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpIncrementBy'])
    @NetworkRangeIpIncrementBy.setter
    def NetworkRangeIpIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIpIncrementBy'], value)

    @property
    def NetworkRangeIpMask(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpMask'])
    @NetworkRangeIpMask.setter
    def NetworkRangeIpMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeIpMask'], value)

    @property
    def NetworkRangeLinkType(self):
        """
        Returns
        -------
        - str(broadcast | pointToPoint): The attribute for the network range link type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeLinkType'])
    @NetworkRangeLinkType.setter
    def NetworkRangeLinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeLinkType'], value)

    @property
    def NetworkRangeRouterId(self):
        """
        Returns
        -------
        - str: The unique identifier for the network range router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeRouterId'])
    @NetworkRangeRouterId.setter
    def NetworkRangeRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeRouterId'], value)

    @property
    def NetworkRangeRouterIdIncrementBy(self):
        """
        Returns
        -------
        - str: The step size by which to automatically increment the IP addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeRouterIdIncrementBy'])
    @NetworkRangeRouterIdIncrementBy.setter
    def NetworkRangeRouterIdIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeRouterIdIncrementBy'], value)

    @property
    def NetworkRangeTeEnable(self):
        """
        Returns
        -------
        - bool: Enables network range TEs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeEnable'])
    @NetworkRangeTeEnable.setter
    def NetworkRangeTeEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeEnable'], value)

    @property
    def NetworkRangeTeMaxBandwidth(self):
        """
        Returns
        -------
        - number: The maximum bandwidth for the network range TEs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeMaxBandwidth'])
    @NetworkRangeTeMaxBandwidth.setter
    def NetworkRangeTeMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeMaxBandwidth'], value)

    @property
    def NetworkRangeTeMetric(self):
        """
        Returns
        -------
        - number: The metrics for network range TEs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeMetric'])
    @NetworkRangeTeMetric.setter
    def NetworkRangeTeMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeMetric'], value)

    @property
    def NetworkRangeTeResMaxBandwidth(self):
        """
        Returns
        -------
        - number: The maximum bandwidth for reserved network range TEs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeResMaxBandwidth'])
    @NetworkRangeTeResMaxBandwidth.setter
    def NetworkRangeTeResMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeResMaxBandwidth'], value)

    @property
    def NetworkRangeTeUnreservedBwPriority(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number): The maximum bandwidth for unreserved network range TEs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkRangeTeUnreservedBwPriority'])
    @NetworkRangeTeUnreservedBwPriority.setter
    def NetworkRangeTeUnreservedBwPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkRangeTeUnreservedBwPriority'], value)

    @property
    def NetworkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast | pointToMultipoint): The type of network attached to the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkType'])
    @NetworkType.setter
    def NetworkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkType'], value)

    @property
    def NoOfCols(self):
        """
        Returns
        -------
        - number: The number of columns in a grid.
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
        - number: The number or rows in a grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRows'])
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRows'], value)

    @property
    def Options(self):
        """
        Returns
        -------
        - number: Options related to the interface. Multiple options may be or'd together.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Options'])
    @Options.setter
    def Options(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Options'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: The priority of the interface, for use in election of the designated or backup master.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The name of the defined interface entry from which IP address and mask are extracted for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def ShowExternal(self):
        """
        Returns
        -------
        - bool: Enables the use of External routes on this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowExternal'])
    @ShowExternal.setter
    def ShowExternal(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowExternal'], value)

    @property
    def ShowNssa(self):
        """
        Returns
        -------
        - bool: Enables the use of Not So Stubby Area routes on this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowNssa'])
    @ShowNssa.setter
    def ShowNssa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowNssa'], value)

    @property
    def TeAdminGroup(self):
        """
        Returns
        -------
        - str: Assignment of traffic engineering administrative group numbers to the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeAdminGroup'])
    @TeAdminGroup.setter
    def TeAdminGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeAdminGroup'], value)

    @property
    def TeEnable(self):
        """
        Returns
        -------
        - bool: Enables the generation of the Traffic Engineering opaque LSA with the remainder of the options in this class.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeEnable'])
    @TeEnable.setter
    def TeEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeEnable'], value)

    @property
    def TeMaxBandwidth(self):
        """
        Returns
        -------
        - str: The maximum bandwidth that can possibly be used on this link in this direction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMaxBandwidth'])
    @TeMaxBandwidth.setter
    def TeMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMaxBandwidth'], value)

    @property
    def TeMetricLevel(self):
        """
        Returns
        -------
        - number: The user-assigned link metric for traffic engineering.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMetricLevel'])
    @TeMetricLevel.setter
    def TeMetricLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMetricLevel'], value)

    @property
    def TeResMaxBandwidth(self):
        """
        Returns
        -------
        - str: If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeResMaxBandwidth'])
    @TeResMaxBandwidth.setter
    def TeResMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeResMaxBandwidth'], value)

    @property
    def TeUnreservedBwPriority(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str): The amount of bandwidth not yet reserved at each of the eight priority levels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeUnreservedBwPriority'])
    @TeUnreservedBwPriority.setter
    def TeUnreservedBwPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeUnreservedBwPriority'], value)

    @property
    def ValidateReceivedMtuSize(self):
        """
        Returns
        -------
        - bool: If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValidateReceivedMtuSize'])
    @ValidateReceivedMtuSize.setter
    def ValidateReceivedMtuSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ValidateReceivedMtuSize'], value)

    def update(self, AdvertiseNetworkRange=None, AreaId=None, AuthenticationMethods=None, AuthenticationPassword=None, BBit=None, ConnectedToDut=None, DeadInterval=None, EBit=None, EnableAdvertiseRouterLsaLoopback=None, EnableBfdRegistration=None, EnableFastHello=None, Enabled=None, EntryColumn=None, EntryRow=None, HelloInterval=None, HelloMultiplier=None, InterfaceIndex=None, InterfaceIpAddress=None, InterfaceIpMaskAddress=None, InterfaceType=None, Interfaces=None, LinkTypes=None, Md5AuthenticationKey=None, Md5AuthenticationKeyId=None, Metric=None, Mtu=None, NeighborIpAddress=None, NeighborRouterId=None, NetworkRangeIp=None, NetworkRangeIpByMask=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRouterId=None, NetworkRangeRouterIdIncrementBy=None, NetworkRangeTeEnable=None, NetworkRangeTeMaxBandwidth=None, NetworkRangeTeMetric=None, NetworkRangeTeResMaxBandwidth=None, NetworkRangeTeUnreservedBwPriority=None, NetworkType=None, NoOfCols=None, NoOfRows=None, Options=None, Priority=None, ProtocolInterface=None, ShowExternal=None, ShowNssa=None, TeAdminGroup=None, TeEnable=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None, ValidateReceivedMtuSize=None):
        """Updates interface resource on the server.

        Args
        ----
        - AdvertiseNetworkRange (bool): Enables the advertisement of the OSPF network range.
        - AreaId (number): The OSPF area ID associated with the interface.
        - AuthenticationMethods (str(null | password | md5)): The type of authentication to be used on this link interface.
        - AuthenticationPassword (str): Enter a clear-text 64-bit password. A password is configured at each end of the link. The password is inserted as is into the packet, and is compared upon receipt at the other end of the link. The received packet is dropped if the contained password does not match the configured password.
        - BBit (bool): Indicates that this router is an Area Border Router (ABR).
        - ConnectedToDut (bool): Indicates that this OSPF interface is directly connected to the DUT.
        - DeadInterval (number): The number of seconds allowed before declaring a silent router as being down.
        - EBit (bool): External bit. Specifies how AS-external-LSAs are flooded.
        - EnableAdvertiseRouterLsaLoopback (bool): If true, advertises the router's LSA loopback address. (default = false)
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the OSPF peer IP address once the OSPF session is established. This allows OSPF to use BFD to maintain IPv4 connectivity the OSPF peer.
        - EnableFastHello (bool): NOT DEFINED
        - Enabled (bool): Enables the use of the simulated interface.
        - EntryColumn (number): The column where the entry point router is located in the OSPFnetwork range grid.
        - EntryRow (number): The row where the entry point router is located in the OSPF network range grid.
        - HelloInterval (number): The number of seconds between Hello packets sent from an Ixia router. The Ixia state machine sends Hello packets at this interval for all of the defined interfaces.
        - HelloMultiplier (number): NOT DEFINED
        - InterfaceIndex (number): The assigned protocol interface ID for this OSPF interface.
        - InterfaceIpAddress (str): The IP address for this OSPF interface.
        - InterfaceIpMaskAddress (str): The IP mask associated with the IP address for this interface. Only used if protocolInterfaceDescription is empty. (default = 255.255.255.0)
        - InterfaceType (str): The type of interface to be selected for this OSPF interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - LinkTypes (str(pointToPoint | transit | stub | virtual)): Indicates the type of network link for the interface.
        - Md5AuthenticationKey (str): If authenticationMethod is set to ospfInterfaceAuthenticationMD5, then this is MD5 key ID used for authentication. (default = 1)
        - Md5AuthenticationKeyId (number): A value to be used as a key ID associated with the MD5 key.
        - Metric (number): A user-assigned routing metric associated with the interface.
        - Mtu (number): The maximum transmission unit (MTU) that is allowed on this link.
        - NeighborIpAddress (str): If the link type is a point to point network, this is the address of the other end of the link.
        - NeighborRouterId (str): When the linkType option is set to ospfInterfaceLinkPointToPoint, then this option should be set to the ID of the router on the other end of the point-to-point connection. (default = 0.0.0.0)
        - NetworkRangeIp (str): The IP address for the first OSPFv2 network to be advertised in the range.
        - NetworkRangeIpByMask (bool): The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        - NetworkRangeIpIncrementBy (str): The step size by which to automatically increment the IP addresses in the range.
        - NetworkRangeIpMask (number): The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        - NetworkRangeLinkType (str(broadcast | pointToPoint)): The attribute for the network range link type.
        - NetworkRangeRouterId (str): The unique identifier for the network range router.
        - NetworkRangeRouterIdIncrementBy (str): The step size by which to automatically increment the IP addresses in the range.
        - NetworkRangeTeEnable (bool): Enables network range TEs.
        - NetworkRangeTeMaxBandwidth (number): The maximum bandwidth for the network range TEs.
        - NetworkRangeTeMetric (number): The metrics for network range TEs.
        - NetworkRangeTeResMaxBandwidth (number): The maximum bandwidth for reserved network range TEs.
        - NetworkRangeTeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): The maximum bandwidth for unreserved network range TEs.
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): The type of network attached to the link.
        - NoOfCols (number): The number of columns in a grid.
        - NoOfRows (number): The number or rows in a grid.
        - Options (number): Options related to the interface. Multiple options may be or'd together.
        - Priority (number): The priority of the interface, for use in election of the designated or backup master.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of the defined interface entry from which IP address and mask are extracted for this interface.
        - ShowExternal (bool): Enables the use of External routes on this interface.
        - ShowNssa (bool): Enables the use of Not So Stubby Area routes on this interface.
        - TeAdminGroup (str): Assignment of traffic engineering administrative group numbers to the interface.
        - TeEnable (bool): Enables the generation of the Traffic Engineering opaque LSA with the remainder of the options in this class.
        - TeMaxBandwidth (str): The maximum bandwidth that can possibly be used on this link in this direction.
        - TeMetricLevel (number): The user-assigned link metric for traffic engineering.
        - TeResMaxBandwidth (str): If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        - TeUnreservedBwPriority (dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str)): The amount of bandwidth not yet reserved at each of the eight priority levels.
        - ValidateReceivedMtuSize (bool): If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertiseNetworkRange=None, AreaId=None, AuthenticationMethods=None, AuthenticationPassword=None, BBit=None, ConnectedToDut=None, DeadInterval=None, EBit=None, EnableAdvertiseRouterLsaLoopback=None, EnableBfdRegistration=None, EnableFastHello=None, Enabled=None, EntryColumn=None, EntryRow=None, HelloInterval=None, HelloMultiplier=None, InterfaceIndex=None, InterfaceIpAddress=None, InterfaceIpMaskAddress=None, InterfaceType=None, Interfaces=None, LinkTypes=None, Md5AuthenticationKey=None, Md5AuthenticationKeyId=None, Metric=None, Mtu=None, NeighborIpAddress=None, NeighborRouterId=None, NetworkRangeIp=None, NetworkRangeIpByMask=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRouterId=None, NetworkRangeRouterIdIncrementBy=None, NetworkRangeTeEnable=None, NetworkRangeTeMaxBandwidth=None, NetworkRangeTeMetric=None, NetworkRangeTeResMaxBandwidth=None, NetworkRangeTeUnreservedBwPriority=None, NetworkType=None, NoOfCols=None, NoOfRows=None, Options=None, Priority=None, ProtocolInterface=None, ShowExternal=None, ShowNssa=None, TeAdminGroup=None, TeEnable=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None, ValidateReceivedMtuSize=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseNetworkRange (bool): Enables the advertisement of the OSPF network range.
        - AreaId (number): The OSPF area ID associated with the interface.
        - AuthenticationMethods (str(null | password | md5)): The type of authentication to be used on this link interface.
        - AuthenticationPassword (str): Enter a clear-text 64-bit password. A password is configured at each end of the link. The password is inserted as is into the packet, and is compared upon receipt at the other end of the link. The received packet is dropped if the contained password does not match the configured password.
        - BBit (bool): Indicates that this router is an Area Border Router (ABR).
        - ConnectedToDut (bool): Indicates that this OSPF interface is directly connected to the DUT.
        - DeadInterval (number): The number of seconds allowed before declaring a silent router as being down.
        - EBit (bool): External bit. Specifies how AS-external-LSAs are flooded.
        - EnableAdvertiseRouterLsaLoopback (bool): If true, advertises the router's LSA loopback address. (default = false)
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the OSPF peer IP address once the OSPF session is established. This allows OSPF to use BFD to maintain IPv4 connectivity the OSPF peer.
        - EnableFastHello (bool): NOT DEFINED
        - Enabled (bool): Enables the use of the simulated interface.
        - EntryColumn (number): The column where the entry point router is located in the OSPFnetwork range grid.
        - EntryRow (number): The row where the entry point router is located in the OSPF network range grid.
        - HelloInterval (number): The number of seconds between Hello packets sent from an Ixia router. The Ixia state machine sends Hello packets at this interval for all of the defined interfaces.
        - HelloMultiplier (number): NOT DEFINED
        - InterfaceIndex (number): The assigned protocol interface ID for this OSPF interface.
        - InterfaceIpAddress (str): The IP address for this OSPF interface.
        - InterfaceIpMaskAddress (str): The IP mask associated with the IP address for this interface. Only used if protocolInterfaceDescription is empty. (default = 255.255.255.0)
        - InterfaceType (str): The type of interface to be selected for this OSPF interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - LinkTypes (str(pointToPoint | transit | stub | virtual)): Indicates the type of network link for the interface.
        - Md5AuthenticationKey (str): If authenticationMethod is set to ospfInterfaceAuthenticationMD5, then this is MD5 key ID used for authentication. (default = 1)
        - Md5AuthenticationKeyId (number): A value to be used as a key ID associated with the MD5 key.
        - Metric (number): A user-assigned routing metric associated with the interface.
        - Mtu (number): The maximum transmission unit (MTU) that is allowed on this link.
        - NeighborIpAddress (str): If the link type is a point to point network, this is the address of the other end of the link.
        - NeighborRouterId (str): When the linkType option is set to ospfInterfaceLinkPointToPoint, then this option should be set to the ID of the router on the other end of the point-to-point connection. (default = 0.0.0.0)
        - NetworkRangeIp (str): The IP address for the first OSPFv2 network to be advertised in the range.
        - NetworkRangeIpByMask (bool): The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        - NetworkRangeIpIncrementBy (str): The step size by which to automatically increment the IP addresses in the range.
        - NetworkRangeIpMask (number): The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        - NetworkRangeLinkType (str(broadcast | pointToPoint)): The attribute for the network range link type.
        - NetworkRangeRouterId (str): The unique identifier for the network range router.
        - NetworkRangeRouterIdIncrementBy (str): The step size by which to automatically increment the IP addresses in the range.
        - NetworkRangeTeEnable (bool): Enables network range TEs.
        - NetworkRangeTeMaxBandwidth (number): The maximum bandwidth for the network range TEs.
        - NetworkRangeTeMetric (number): The metrics for network range TEs.
        - NetworkRangeTeResMaxBandwidth (number): The maximum bandwidth for reserved network range TEs.
        - NetworkRangeTeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): The maximum bandwidth for unreserved network range TEs.
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): The type of network attached to the link.
        - NoOfCols (number): The number of columns in a grid.
        - NoOfRows (number): The number or rows in a grid.
        - Options (number): Options related to the interface. Multiple options may be or'd together.
        - Priority (number): The priority of the interface, for use in election of the designated or backup master.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of the defined interface entry from which IP address and mask are extracted for this interface.
        - ShowExternal (bool): Enables the use of External routes on this interface.
        - ShowNssa (bool): Enables the use of Not So Stubby Area routes on this interface.
        - TeAdminGroup (str): Assignment of traffic engineering administrative group numbers to the interface.
        - TeEnable (bool): Enables the generation of the Traffic Engineering opaque LSA with the remainder of the options in this class.
        - TeMaxBandwidth (str): The maximum bandwidth that can possibly be used on this link in this direction.
        - TeMetricLevel (number): The user-assigned link metric for traffic engineering.
        - TeResMaxBandwidth (str): If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        - TeUnreservedBwPriority (dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str)): The amount of bandwidth not yet reserved at each of the eight priority levels.
        - ValidateReceivedMtuSize (bool): If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertiseNetworkRange=None, AreaId=None, AuthenticationMethods=None, AuthenticationPassword=None, BBit=None, ConnectedToDut=None, DeadInterval=None, EBit=None, EnableAdvertiseRouterLsaLoopback=None, EnableBfdRegistration=None, EnableFastHello=None, Enabled=None, EntryColumn=None, EntryRow=None, HelloInterval=None, HelloMultiplier=None, InterfaceIndex=None, InterfaceIpAddress=None, InterfaceIpMaskAddress=None, InterfaceType=None, Interfaces=None, IsLearnedInfoRefreshed=None, LinkTypes=None, Md5AuthenticationKey=None, Md5AuthenticationKeyId=None, Metric=None, Mtu=None, NeighborIpAddress=None, NeighborRouterId=None, NetworkRangeIp=None, NetworkRangeIpByMask=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRouterId=None, NetworkRangeRouterIdIncrementBy=None, NetworkRangeTeEnable=None, NetworkRangeTeMaxBandwidth=None, NetworkRangeTeMetric=None, NetworkRangeTeResMaxBandwidth=None, NetworkRangeTeUnreservedBwPriority=None, NetworkType=None, NoOfCols=None, NoOfRows=None, Options=None, Priority=None, ProtocolInterface=None, ShowExternal=None, ShowNssa=None, TeAdminGroup=None, TeEnable=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None, ValidateReceivedMtuSize=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AdvertiseNetworkRange (bool): Enables the advertisement of the OSPF network range.
        - AreaId (number): The OSPF area ID associated with the interface.
        - AuthenticationMethods (str(null | password | md5)): The type of authentication to be used on this link interface.
        - AuthenticationPassword (str): Enter a clear-text 64-bit password. A password is configured at each end of the link. The password is inserted as is into the packet, and is compared upon receipt at the other end of the link. The received packet is dropped if the contained password does not match the configured password.
        - BBit (bool): Indicates that this router is an Area Border Router (ABR).
        - ConnectedToDut (bool): Indicates that this OSPF interface is directly connected to the DUT.
        - DeadInterval (number): The number of seconds allowed before declaring a silent router as being down.
        - EBit (bool): External bit. Specifies how AS-external-LSAs are flooded.
        - EnableAdvertiseRouterLsaLoopback (bool): If true, advertises the router's LSA loopback address. (default = false)
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the OSPF peer IP address once the OSPF session is established. This allows OSPF to use BFD to maintain IPv4 connectivity the OSPF peer.
        - EnableFastHello (bool): NOT DEFINED
        - Enabled (bool): Enables the use of the simulated interface.
        - EntryColumn (number): The column where the entry point router is located in the OSPFnetwork range grid.
        - EntryRow (number): The row where the entry point router is located in the OSPF network range grid.
        - HelloInterval (number): The number of seconds between Hello packets sent from an Ixia router. The Ixia state machine sends Hello packets at this interval for all of the defined interfaces.
        - HelloMultiplier (number): NOT DEFINED
        - InterfaceIndex (number): The assigned protocol interface ID for this OSPF interface.
        - InterfaceIpAddress (str): The IP address for this OSPF interface.
        - InterfaceIpMaskAddress (str): The IP mask associated with the IP address for this interface. Only used if protocolInterfaceDescription is empty. (default = 255.255.255.0)
        - InterfaceType (str): The type of interface to be selected for this OSPF interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - IsLearnedInfoRefreshed (bool): If true, refreshes learned information automatically.
        - LinkTypes (str(pointToPoint | transit | stub | virtual)): Indicates the type of network link for the interface.
        - Md5AuthenticationKey (str): If authenticationMethod is set to ospfInterfaceAuthenticationMD5, then this is MD5 key ID used for authentication. (default = 1)
        - Md5AuthenticationKeyId (number): A value to be used as a key ID associated with the MD5 key.
        - Metric (number): A user-assigned routing metric associated with the interface.
        - Mtu (number): The maximum transmission unit (MTU) that is allowed on this link.
        - NeighborIpAddress (str): If the link type is a point to point network, this is the address of the other end of the link.
        - NeighborRouterId (str): When the linkType option is set to ospfInterfaceLinkPointToPoint, then this option should be set to the ID of the router on the other end of the point-to-point connection. (default = 0.0.0.0)
        - NetworkRangeIp (str): The IP address for the first OSPFv2 network to be advertised in the range.
        - NetworkRangeIpByMask (bool): The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        - NetworkRangeIpIncrementBy (str): The step size by which to automatically increment the IP addresses in the range.
        - NetworkRangeIpMask (number): The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        - NetworkRangeLinkType (str(broadcast | pointToPoint)): The attribute for the network range link type.
        - NetworkRangeRouterId (str): The unique identifier for the network range router.
        - NetworkRangeRouterIdIncrementBy (str): The step size by which to automatically increment the IP addresses in the range.
        - NetworkRangeTeEnable (bool): Enables network range TEs.
        - NetworkRangeTeMaxBandwidth (number): The maximum bandwidth for the network range TEs.
        - NetworkRangeTeMetric (number): The metrics for network range TEs.
        - NetworkRangeTeResMaxBandwidth (number): The maximum bandwidth for reserved network range TEs.
        - NetworkRangeTeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): The maximum bandwidth for unreserved network range TEs.
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): The type of network attached to the link.
        - NoOfCols (number): The number of columns in a grid.
        - NoOfRows (number): The number or rows in a grid.
        - Options (number): Options related to the interface. Multiple options may be or'd together.
        - Priority (number): The priority of the interface, for use in election of the designated or backup master.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of the defined interface entry from which IP address and mask are extracted for this interface.
        - ShowExternal (bool): Enables the use of External routes on this interface.
        - ShowNssa (bool): Enables the use of Not So Stubby Area routes on this interface.
        - TeAdminGroup (str): Assignment of traffic engineering administrative group numbers to the interface.
        - TeEnable (bool): Enables the generation of the Traffic Engineering opaque LSA with the remainder of the options in this class.
        - TeMaxBandwidth (str): The maximum bandwidth that can possibly be used on this link in this direction.
        - TeMetricLevel (number): The user-assigned link metric for traffic engineering.
        - TeResMaxBandwidth (str): If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        - TeUnreservedBwPriority (dict(arg1:str,arg2:str,arg3:str,arg4:str,arg5:str,arg6:str,arg7:str,arg8:str)): The amount of bandwidth not yet reserved at each of the eight priority levels.
        - ValidateReceivedMtuSize (bool): If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Fetches interfaces accessor Iface list.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        A list of objects on which this exec can be used. This exec requires an object reference as an argument.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
