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


class Interface(Base):
    """This object is a network interface.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def LearnedFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_db18f78f500a66194f6f483e02a33bca.LearnedFilter): An instance of the LearnedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_db18f78f500a66194f6f483e02a33bca import LearnedFilter
        return LearnedFilter(self)._select()

    @property
    def LearnedLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_3b654dfa2b2aa7c8e2aebce973df4cc3.LearnedLsa): An instance of the LearnedLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_3b654dfa2b2aa7c8e2aebce973df4cc3 import LearnedLsa
        return LearnedLsa(self)

    @property
    def AdvertiseNetworkRange(self):
        """
        Returns
        -------
        - bool: Enables the advertisement of the OSPF network range.
        """
        return self._get_attribute('advertiseNetworkRange')
    @AdvertiseNetworkRange.setter
    def AdvertiseNetworkRange(self, value):
        self._set_attribute('advertiseNetworkRange', value)

    @property
    def AreaId(self):
        """
        Returns
        -------
        - number: The OSPF area ID associated with the interface.
        """
        return self._get_attribute('areaId')
    @AreaId.setter
    def AreaId(self, value):
        self._set_attribute('areaId', value)

    @property
    def AuthenticationMethods(self):
        """
        Returns
        -------
        - str(null | password | md5): The type of authentication to be used on this link interface.
        """
        return self._get_attribute('authenticationMethods')
    @AuthenticationMethods.setter
    def AuthenticationMethods(self, value):
        self._set_attribute('authenticationMethods', value)

    @property
    def AuthenticationPassword(self):
        """
        Returns
        -------
        - str: Enter a clear-text 64-bit password. A password is configured at each end of the link. The password is inserted as is into the packet, and is compared upon receipt at the other end of the link. The received packet is dropped if the contained password does not match the configured password.
        """
        return self._get_attribute('authenticationPassword')
    @AuthenticationPassword.setter
    def AuthenticationPassword(self, value):
        self._set_attribute('authenticationPassword', value)

    @property
    def BBit(self):
        """
        Returns
        -------
        - bool: Indicates that this router is an Area Border Router (ABR).
        """
        return self._get_attribute('bBit')
    @BBit.setter
    def BBit(self, value):
        self._set_attribute('bBit', value)

    @property
    def ConnectedToDut(self):
        """
        Returns
        -------
        - bool: Indicates that this OSPF interface is directly connected to the DUT.
        """
        return self._get_attribute('connectedToDut')
    @ConnectedToDut.setter
    def ConnectedToDut(self, value):
        self._set_attribute('connectedToDut', value)

    @property
    def DeadInterval(self):
        """
        Returns
        -------
        - number: The number of seconds allowed before declaring a silent router as being down.
        """
        return self._get_attribute('deadInterval')
    @DeadInterval.setter
    def DeadInterval(self, value):
        self._set_attribute('deadInterval', value)

    @property
    def EBit(self):
        """
        Returns
        -------
        - bool: External bit. Specifies how AS-external-LSAs are flooded.
        """
        return self._get_attribute('eBit')
    @EBit.setter
    def EBit(self, value):
        self._set_attribute('eBit', value)

    @property
    def EnableAdvertiseRouterLsaLoopback(self):
        """
        Returns
        -------
        - bool: If true, advertises the router's LSA loopback address. (default = false)
        """
        return self._get_attribute('enableAdvertiseRouterLsaLoopback')
    @EnableAdvertiseRouterLsaLoopback.setter
    def EnableAdvertiseRouterLsaLoopback(self, value):
        self._set_attribute('enableAdvertiseRouterLsaLoopback', value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: Indicates if a BFD session is to be created to the OSPF peer IP address once the OSPF session is established. This allows OSPF to use BFD to maintain IPv4 connectivity the OSPF peer.
        """
        return self._get_attribute('enableBfdRegistration')
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute('enableBfdRegistration', value)

    @property
    def EnableFastHello(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableFastHello')
    @EnableFastHello.setter
    def EnableFastHello(self, value):
        self._set_attribute('enableFastHello', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the simulated interface.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def EntryColumn(self):
        """
        Returns
        -------
        - number: The column where the entry point router is located in the OSPFnetwork range grid.
        """
        return self._get_attribute('entryColumn')
    @EntryColumn.setter
    def EntryColumn(self, value):
        self._set_attribute('entryColumn', value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: The row where the entry point router is located in the OSPF network range grid.
        """
        return self._get_attribute('entryRow')
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute('entryRow', value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: The number of seconds between Hello packets sent from an Ixia router. The Ixia state machine sends Hello packets at this interval for all of the defined interfaces.
        """
        return self._get_attribute('helloInterval')
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute('helloInterval', value)

    @property
    def HelloMultiplier(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('helloMultiplier')
    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._set_attribute('helloMultiplier', value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this OSPF interface.
        """
        return self._get_attribute('interfaceIndex')
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute('interfaceIndex', value)

    @property
    def InterfaceIpAddress(self):
        """
        Returns
        -------
        - str: The IP address for this OSPF interface.
        """
        return self._get_attribute('interfaceIpAddress')
    @InterfaceIpAddress.setter
    def InterfaceIpAddress(self, value):
        self._set_attribute('interfaceIpAddress', value)

    @property
    def InterfaceIpMaskAddress(self):
        """
        Returns
        -------
        - str: The IP mask associated with the IP address for this interface. Only used if protocolInterfaceDescription is empty. (default = 255.255.255.0)
        """
        return self._get_attribute('interfaceIpMaskAddress')
    @InterfaceIpMaskAddress.setter
    def InterfaceIpMaskAddress(self, value):
        self._set_attribute('interfaceIpMaskAddress', value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str: The type of interface to be selected for this OSPF interface.
        """
        return self._get_attribute('interfaceType')
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute('interfaceType', value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute('interfaces')
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute('interfaces', value)

    @property
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, refreshes learned information automatically.
        """
        return self._get_attribute('isLearnedInfoRefreshed')

    @property
    def LinkTypes(self):
        """
        Returns
        -------
        - str(pointToPoint | transit | stub | virtual): Indicates the type of network link for the interface.
        """
        return self._get_attribute('linkTypes')
    @LinkTypes.setter
    def LinkTypes(self, value):
        self._set_attribute('linkTypes', value)

    @property
    def Md5AuthenticationKey(self):
        """
        Returns
        -------
        - str: If authenticationMethod is set to ospfInterfaceAuthenticationMD5, then this is MD5 key ID used for authentication. (default = 1)
        """
        return self._get_attribute('md5AuthenticationKey')
    @Md5AuthenticationKey.setter
    def Md5AuthenticationKey(self, value):
        self._set_attribute('md5AuthenticationKey', value)

    @property
    def Md5AuthenticationKeyId(self):
        """
        Returns
        -------
        - number: A value to be used as a key ID associated with the MD5 key.
        """
        return self._get_attribute('md5AuthenticationKeyId')
    @Md5AuthenticationKeyId.setter
    def Md5AuthenticationKeyId(self, value):
        self._set_attribute('md5AuthenticationKeyId', value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: A user-assigned routing metric associated with the interface.
        """
        return self._get_attribute('metric')
    @Metric.setter
    def Metric(self, value):
        self._set_attribute('metric', value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: The maximum transmission unit (MTU) that is allowed on this link.
        """
        return self._get_attribute('mtu')
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute('mtu', value)

    @property
    def NeighborIpAddress(self):
        """
        Returns
        -------
        - str: If the link type is a point to point network, this is the address of the other end of the link.
        """
        return self._get_attribute('neighborIpAddress')
    @NeighborIpAddress.setter
    def NeighborIpAddress(self, value):
        self._set_attribute('neighborIpAddress', value)

    @property
    def NeighborRouterId(self):
        """
        Returns
        -------
        - str: When the linkType option is set to ospfInterfaceLinkPointToPoint, then this option should be set to the ID of the router on the other end of the point-to-point connection. (default = 0.0.0.0)
        """
        return self._get_attribute('neighborRouterId')
    @NeighborRouterId.setter
    def NeighborRouterId(self, value):
        self._set_attribute('neighborRouterId', value)

    @property
    def NetworkRangeIp(self):
        """
        Returns
        -------
        - str: The IP address for the first OSPFv2 network to be advertised in the range.
        """
        return self._get_attribute('networkRangeIp')
    @NetworkRangeIp.setter
    def NetworkRangeIp(self, value):
        self._set_attribute('networkRangeIp', value)

    @property
    def NetworkRangeIpByMask(self):
        """
        Returns
        -------
        - bool: The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        """
        return self._get_attribute('networkRangeIpByMask')
    @NetworkRangeIpByMask.setter
    def NetworkRangeIpByMask(self, value):
        self._set_attribute('networkRangeIpByMask', value)

    @property
    def NetworkRangeIpIncrementBy(self):
        """
        Returns
        -------
        - str: The step size by which to automatically increment the IP addresses in the range.
        """
        return self._get_attribute('networkRangeIpIncrementBy')
    @NetworkRangeIpIncrementBy.setter
    def NetworkRangeIpIncrementBy(self, value):
        self._set_attribute('networkRangeIpIncrementBy', value)

    @property
    def NetworkRangeIpMask(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask used with the IP address of the first network, in creating a range of addresses.
        """
        return self._get_attribute('networkRangeIpMask')
    @NetworkRangeIpMask.setter
    def NetworkRangeIpMask(self, value):
        self._set_attribute('networkRangeIpMask', value)

    @property
    def NetworkRangeLinkType(self):
        """
        Returns
        -------
        - str(broadcast | pointToPoint): The attribute for the network range link type.
        """
        return self._get_attribute('networkRangeLinkType')
    @NetworkRangeLinkType.setter
    def NetworkRangeLinkType(self, value):
        self._set_attribute('networkRangeLinkType', value)

    @property
    def NetworkRangeRouterId(self):
        """
        Returns
        -------
        - str: The unique identifier for the network range router.
        """
        return self._get_attribute('networkRangeRouterId')
    @NetworkRangeRouterId.setter
    def NetworkRangeRouterId(self, value):
        self._set_attribute('networkRangeRouterId', value)

    @property
    def NetworkRangeRouterIdIncrementBy(self):
        """
        Returns
        -------
        - str: The step size by which to automatically increment the IP addresses in the range.
        """
        return self._get_attribute('networkRangeRouterIdIncrementBy')
    @NetworkRangeRouterIdIncrementBy.setter
    def NetworkRangeRouterIdIncrementBy(self, value):
        self._set_attribute('networkRangeRouterIdIncrementBy', value)

    @property
    def NetworkRangeTeEnable(self):
        """
        Returns
        -------
        - bool: Enables network range TEs.
        """
        return self._get_attribute('networkRangeTeEnable')
    @NetworkRangeTeEnable.setter
    def NetworkRangeTeEnable(self, value):
        self._set_attribute('networkRangeTeEnable', value)

    @property
    def NetworkRangeTeMaxBandwidth(self):
        """
        Returns
        -------
        - number: The maximum bandwidth for the network range TEs.
        """
        return self._get_attribute('networkRangeTeMaxBandwidth')
    @NetworkRangeTeMaxBandwidth.setter
    def NetworkRangeTeMaxBandwidth(self, value):
        self._set_attribute('networkRangeTeMaxBandwidth', value)

    @property
    def NetworkRangeTeMetric(self):
        """
        Returns
        -------
        - number: The metrics for network range TEs.
        """
        return self._get_attribute('networkRangeTeMetric')
    @NetworkRangeTeMetric.setter
    def NetworkRangeTeMetric(self, value):
        self._set_attribute('networkRangeTeMetric', value)

    @property
    def NetworkRangeTeResMaxBandwidth(self):
        """
        Returns
        -------
        - number: The maximum bandwidth for reserved network range TEs.
        """
        return self._get_attribute('networkRangeTeResMaxBandwidth')
    @NetworkRangeTeResMaxBandwidth.setter
    def NetworkRangeTeResMaxBandwidth(self, value):
        self._set_attribute('networkRangeTeResMaxBandwidth', value)

    @property
    def NetworkRangeTeUnreservedBwPriority(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number): The maximum bandwidth for unreserved network range TEs.
        """
        return self._get_attribute('networkRangeTeUnreservedBwPriority')
    @NetworkRangeTeUnreservedBwPriority.setter
    def NetworkRangeTeUnreservedBwPriority(self, value):
        self._set_attribute('networkRangeTeUnreservedBwPriority', value)

    @property
    def NetworkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast | pointToMultipoint): The type of network attached to the link.
        """
        return self._get_attribute('networkType')
    @NetworkType.setter
    def NetworkType(self, value):
        self._set_attribute('networkType', value)

    @property
    def NoOfCols(self):
        """
        Returns
        -------
        - number: The number of columns in a grid.
        """
        return self._get_attribute('noOfCols')
    @NoOfCols.setter
    def NoOfCols(self, value):
        self._set_attribute('noOfCols', value)

    @property
    def NoOfRows(self):
        """
        Returns
        -------
        - number: The number or rows in a grid.
        """
        return self._get_attribute('noOfRows')
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute('noOfRows', value)

    @property
    def Options(self):
        """
        Returns
        -------
        - number: Options related to the interface. Multiple options may be or'd together.
        """
        return self._get_attribute('options')
    @Options.setter
    def Options(self, value):
        self._set_attribute('options', value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: The priority of the interface, for use in election of the designated or backup master.
        """
        return self._get_attribute('priority')
    @Priority.setter
    def Priority(self, value):
        self._set_attribute('priority', value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The name of the defined interface entry from which IP address and mask are extracted for this interface.
        """
        return self._get_attribute('protocolInterface')
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute('protocolInterface', value)

    @property
    def ShowExternal(self):
        """
        Returns
        -------
        - bool: Enables the use of External routes on this interface.
        """
        return self._get_attribute('showExternal')
    @ShowExternal.setter
    def ShowExternal(self, value):
        self._set_attribute('showExternal', value)

    @property
    def ShowNssa(self):
        """
        Returns
        -------
        - bool: Enables the use of Not So Stubby Area routes on this interface.
        """
        return self._get_attribute('showNssa')
    @ShowNssa.setter
    def ShowNssa(self, value):
        self._set_attribute('showNssa', value)

    @property
    def TeAdminGroup(self):
        """
        Returns
        -------
        - str: Assignment of traffic engineering administrative group numbers to the interface.
        """
        return self._get_attribute('teAdminGroup')
    @TeAdminGroup.setter
    def TeAdminGroup(self, value):
        self._set_attribute('teAdminGroup', value)

    @property
    def TeEnable(self):
        """
        Returns
        -------
        - bool: Enables the generation of the Traffic Engineering opaque LSA with the remainder of the options in this class.
        """
        return self._get_attribute('teEnable')
    @TeEnable.setter
    def TeEnable(self, value):
        self._set_attribute('teEnable', value)

    @property
    def TeMaxBandwidth(self):
        """
        Returns
        -------
        - number: The maximum bandwidth that can possibly be used on this link in this direction.
        """
        return self._get_attribute('teMaxBandwidth')
    @TeMaxBandwidth.setter
    def TeMaxBandwidth(self, value):
        self._set_attribute('teMaxBandwidth', value)

    @property
    def TeMetricLevel(self):
        """
        Returns
        -------
        - number: The user-assigned link metric for traffic engineering.
        """
        return self._get_attribute('teMetricLevel')
    @TeMetricLevel.setter
    def TeMetricLevel(self, value):
        self._set_attribute('teMetricLevel', value)

    @property
    def TeResMaxBandwidth(self):
        """
        Returns
        -------
        - number: If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        """
        return self._get_attribute('teResMaxBandwidth')
    @TeResMaxBandwidth.setter
    def TeResMaxBandwidth(self, value):
        self._set_attribute('teResMaxBandwidth', value)

    @property
    def TeUnreservedBwPriority(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number): The amount of bandwidth not yet reserved at each of the eight priority levels.
        """
        return self._get_attribute('teUnreservedBwPriority')
    @TeUnreservedBwPriority.setter
    def TeUnreservedBwPriority(self, value):
        self._set_attribute('teUnreservedBwPriority', value)

    @property
    def ValidateReceivedMtuSize(self):
        """
        Returns
        -------
        - bool: If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.
        """
        return self._get_attribute('validateReceivedMtuSize')
    @ValidateReceivedMtuSize.setter
    def ValidateReceivedMtuSize(self, value):
        self._set_attribute('validateReceivedMtuSize', value)

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
        - TeMaxBandwidth (number): The maximum bandwidth that can possibly be used on this link in this direction.
        - TeMetricLevel (number): The user-assigned link metric for traffic engineering.
        - TeResMaxBandwidth (number): If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        - TeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): The amount of bandwidth not yet reserved at each of the eight priority levels.
        - ValidateReceivedMtuSize (bool): If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

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
        - TeMaxBandwidth (number): The maximum bandwidth that can possibly be used on this link in this direction.
        - TeMetricLevel (number): The user-assigned link metric for traffic engineering.
        - TeResMaxBandwidth (number): If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        - TeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): The amount of bandwidth not yet reserved at each of the eight priority levels.
        - ValidateReceivedMtuSize (bool): If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

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
        - TeMaxBandwidth (number): The maximum bandwidth that can possibly be used on this link in this direction.
        - TeMetricLevel (number): The user-assigned link metric for traffic engineering.
        - TeResMaxBandwidth (number): If enableTrafficEngineering is 1, then this indicates the maximum bandwidth, in bytes per second, that can be reserved on the link between this interface and its neighbors in the outbound direction. (default = 0.0)
        - TeUnreservedBwPriority (dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:number,arg8:number)): The amount of bandwidth not yet reserved at each of the eight priority levels.
        - ValidateReceivedMtuSize (bool): If enabled (the default setting), the MTU will be verified during the Database (DB) exchange. If disabled, the advertised MTU size is set to 0, and the received MTU size is ignored during the DB exchange. NOTE: This option is only available for OSPFv2 interfaces that are directly connected to the DUT.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

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
