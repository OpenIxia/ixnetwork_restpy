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


class NeighborRange(Base):
    """This object holds information about a BGP4 internal or external neighbor router.
    The NeighborRange class encapsulates a list of neighborRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the NeighborRange.find() method.
    The list can be managed by using the NeighborRange.add() and NeighborRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'neighborRange'
    _SDM_ATT_MAP = {
        'AsNumMode': 'asNumMode',
        'Authentication': 'authentication',
        'BfdModeOfOperation': 'bfdModeOfOperation',
        'BgpId': 'bgpId',
        'DutIpAddress': 'dutIpAddress',
        'Enable4ByteAsNum': 'enable4ByteAsNum',
        'EnableActAsRestarted': 'enableActAsRestarted',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableBgpId': 'enableBgpId',
        'EnableDiscardIxiaGeneratedRoutes': 'enableDiscardIxiaGeneratedRoutes',
        'EnableGracefulRestart': 'enableGracefulRestart',
        'EnableLinkFlap': 'enableLinkFlap',
        'EnableNextHop': 'enableNextHop',
        'EnableOptionalParameters': 'enableOptionalParameters',
        'EnableSendIxiaSignatureWithRoutes': 'enableSendIxiaSignatureWithRoutes',
        'EnableStaggeredStart': 'enableStaggeredStart',
        'Enabled': 'enabled',
        'Evpn': 'evpn',
        'EvpnNextHopCount': 'evpnNextHopCount',
        'HoldTimer': 'holdTimer',
        'InterfaceStartIndex': 'interfaceStartIndex',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'IpV4Mdt': 'ipV4Mdt',
        'IpV4Mpls': 'ipV4Mpls',
        'IpV4MplsVpn': 'ipV4MplsVpn',
        'IpV4Multicast': 'ipV4Multicast',
        'IpV4MulticastVpn': 'ipV4MulticastVpn',
        'IpV4Unicast': 'ipV4Unicast',
        'IpV6Mpls': 'ipV6Mpls',
        'IpV6MplsVpn': 'ipV6MplsVpn',
        'IpV6Multicast': 'ipV6Multicast',
        'IpV6MulticastVpn': 'ipV6MulticastVpn',
        'IpV6Unicast': 'ipV6Unicast',
        'IsAsbr': 'isAsbr',
        'IsInterfaceLearnedInfoAvailable': 'isInterfaceLearnedInfoAvailable',
        'IsLearnedInfoRefreshed': 'isLearnedInfoRefreshed',
        'LinkFlapDownTime': 'linkFlapDownTime',
        'LinkFlapUpTime': 'linkFlapUpTime',
        'LocalAsNumber': 'localAsNumber',
        'LocalIpAddress': 'localIpAddress',
        'Md5Key': 'md5Key',
        'NextHop': 'nextHop',
        'NumUpdatesPerIteration': 'numUpdatesPerIteration',
        'RangeCount': 'rangeCount',
        'RemoteAsNumber': 'remoteAsNumber',
        'RestartTime': 'restartTime',
        'StaggeredStartPeriod': 'staggeredStartPeriod',
        'StaleTime': 'staleTime',
        'TcpWindowSize': 'tcpWindowSize',
        'TrafficGroupId': 'trafficGroupId',
        'TtlValue': 'ttlValue',
        'Type': 'type',
        'UpdateInterval': 'updateInterval',
        'Vpls': 'vpls',
    }
    _SDM_ENUM_MAP = {
        'asNumMode': ['fixed', 'increment'],
        'authentication': ['null', 'md5'],
        'bfdModeOfOperation': ['multiHop', 'singleHop'],
        'type': ['internal', 'external'],
    }

    def __init__(self, parent, list_op=False):
        super(NeighborRange, self).__init__(parent, list_op)

    @property
    def Bgp4VpnBgpAdVplsRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp4vpnbgpadvplsrange_c396d4abd272d60c3ff5958f98263958.Bgp4VpnBgpAdVplsRange): An instance of the Bgp4VpnBgpAdVplsRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp4vpnbgpadvplsrange_c396d4abd272d60c3ff5958f98263958 import Bgp4VpnBgpAdVplsRange
        if self._properties.get('Bgp4VpnBgpAdVplsRange', None) is not None:
            return self._properties.get('Bgp4VpnBgpAdVplsRange')
        else:
            return Bgp4VpnBgpAdVplsRange(self)

    @property
    def EthernetSegments(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernetsegments_a0eef4099ef38ee0e07ecf7430536119.EthernetSegments): An instance of the EthernetSegments class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ethernetsegments_a0eef4099ef38ee0e07ecf7430536119 import EthernetSegments
        if self._properties.get('EthernetSegments', None) is not None:
            return self._properties.get('EthernetSegments')
        else:
            return EthernetSegments(self)

    @property
    def InterfaceLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacelearnedinfo_44709d044bd5612e19aaa934437e496a.InterfaceLearnedInfo): An instance of the InterfaceLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacelearnedinfo_44709d044bd5612e19aaa934437e496a import InterfaceLearnedInfo
        if self._properties.get('InterfaceLearnedInfo', None) is not None:
            return self._properties.get('InterfaceLearnedInfo')
        else:
            return InterfaceLearnedInfo(self)._select()

    @property
    def L2Site(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2site_261b4b7984b4a56f96a23ca529af873f.L2Site): An instance of the L2Site class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2site_261b4b7984b4a56f96a23ca529af873f import L2Site
        if self._properties.get('L2Site', None) is not None:
            return self._properties.get('L2Site')
        else:
            return L2Site(self)

    @property
    def L3Site(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l3site_1184c1264fe43eeeb88002bee9622490.L3Site): An instance of the L3Site class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l3site_1184c1264fe43eeeb88002bee9622490 import L3Site
        if self._properties.get('L3Site', None) is not None:
            return self._properties.get('L3Site')
        else:
            return L3Site(self)

    @property
    def LearnedFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_df26bdb55c5d9a2a87a7eb099776d203.LearnedFilter): An instance of the LearnedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_df26bdb55c5d9a2a87a7eb099776d203 import LearnedFilter
        if self._properties.get('LearnedFilter', None) is not None:
            return self._properties.get('LearnedFilter')
        else:
            return LearnedFilter(self)._select()

    @property
    def LearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_1802ba18af469548428332b926b4e374.LearnedInformation): An instance of the LearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_1802ba18af469548428332b926b4e374 import LearnedInformation
        if self._properties.get('LearnedInformation', None) is not None:
            return self._properties.get('LearnedInformation')
        else:
            return LearnedInformation(self)._select()

    @property
    def MplsRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsrouterange_d92b7c314e154932c6a571f5bccc9139.MplsRouteRange): An instance of the MplsRouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsrouterange_d92b7c314e154932c6a571f5bccc9139 import MplsRouteRange
        if self._properties.get('MplsRouteRange', None) is not None:
            return self._properties.get('MplsRouteRange')
        else:
            return MplsRouteRange(self)

    @property
    def OpaqueRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquerouterange_758cfa0f54d8a32ec8c2cdda163db9de.OpaqueRouteRange): An instance of the OpaqueRouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquerouterange_758cfa0f54d8a32ec8c2cdda163db9de import OpaqueRouteRange
        if self._properties.get('OpaqueRouteRange', None) is not None:
            return self._properties.get('OpaqueRouteRange')
        else:
            return OpaqueRouteRange(self)

    @property
    def RouteImportOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routeimportoptions_6dbeb38f5cd6a11bd94fb0d2945c0d1b.RouteImportOptions): An instance of the RouteImportOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routeimportoptions_6dbeb38f5cd6a11bd94fb0d2945c0d1b import RouteImportOptions
        if self._properties.get('RouteImportOptions', None) is not None:
            return self._properties.get('RouteImportOptions')
        else:
            return RouteImportOptions(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_0d3bbd0c1e734e0573f923091baa82c2.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_0d3bbd0c1e734e0573f923091baa82c2 import RouteRange
        if self._properties.get('RouteRange', None) is not None:
            return self._properties.get('RouteRange')
        else:
            return RouteRange(self)

    @property
    def UserDefinedAfiSafi(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userdefinedafisafi_963e12659eb9e18aba3316a600da5e38.UserDefinedAfiSafi): An instance of the UserDefinedAfiSafi class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userdefinedafisafi_963e12659eb9e18aba3316a600da5e38 import UserDefinedAfiSafi
        if self._properties.get('UserDefinedAfiSafi', None) is not None:
            return self._properties.get('UserDefinedAfiSafi')
        else:
            return UserDefinedAfiSafi(self)

    @property
    def AsNumMode(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str(fixed | increment): (External only) Indicates that each new session uses a different AS number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsNumMode'])
    @AsNumMode.setter
    def AsNumMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AsNumMode'], value)

    @property
    def Authentication(self):
        # type: () -> str
        """
        Returns
        -------
        - str(null | md5): Select the type of cryptographic authentication to be used for the BGP peers in this peer range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Authentication'])
    @Authentication.setter
    def Authentication(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Authentication'], value)

    @property
    def BfdModeOfOperation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(multiHop | singleHop): Indicates whether to use a single-hop or a multi-hop mode of operation for the BFD session being created with a BGP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdModeOfOperation'])
    @BfdModeOfOperation.setter
    def BfdModeOfOperation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['BfdModeOfOperation'], value)

    @property
    def BgpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The BGP ID used in OPEN messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BgpId'])
    @BgpId.setter
    def BgpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['BgpId'], value)

    @property
    def DutIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the DUT router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutIpAddress'])
    @DutIpAddress.setter
    def DutIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DutIpAddress'], value)

    @property
    def Enable4ByteAsNum(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the 4-byte Autonomous System (AS) number of the DUT/SUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enable4ByteAsNum'])
    @Enable4ByteAsNum.setter
    def Enable4ByteAsNum(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enable4ByteAsNum'], value)

    @property
    def EnableActAsRestarted(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls the operation of BGP Graceful Restart.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableActAsRestarted'])
    @EnableActAsRestarted.setter
    def EnableActAsRestarted(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableActAsRestarted'], value)

    @property
    def EnableBfdRegistration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the BFD registration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def EnableBgpId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The BGP ID used in OPEN messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBgpId'])
    @EnableBgpId.setter
    def EnableBgpId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableBgpId'], value)

    @property
    def EnableDiscardIxiaGeneratedRoutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the discard of Ixia generated routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDiscardIxiaGeneratedRoutes'])
    @EnableDiscardIxiaGeneratedRoutes.setter
    def EnableDiscardIxiaGeneratedRoutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableDiscardIxiaGeneratedRoutes'], value)

    @property
    def EnableGracefulRestart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls the operation of BGP Graceful Restart.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestart'])
    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableGracefulRestart'], value)

    @property
    def EnableLinkFlap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables link flap
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkFlap'])
    @EnableLinkFlap.setter
    def EnableLinkFlap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkFlap'], value)

    @property
    def EnableNextHop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Used for IPv4 traffic. Controls the use of the NEXT_HOP attribute. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNextHop'])
    @EnableNextHop.setter
    def EnableNextHop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableNextHop'], value)

    @property
    def EnableOptionalParameters(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls how an OPEN is conducted in the presence of optional parameters.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOptionalParameters'])
    @EnableOptionalParameters.setter
    def EnableOptionalParameters(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableOptionalParameters'], value)

    @property
    def EnableSendIxiaSignatureWithRoutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables sending of Ixia signature with routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendIxiaSignatureWithRoutes'])
    @EnableSendIxiaSignatureWithRoutes.setter
    def EnableSendIxiaSignatureWithRoutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableSendIxiaSignatureWithRoutes'], value)

    @property
    def EnableStaggeredStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls the staggering and period of initial start messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStaggeredStart'])
    @EnableStaggeredStart.setter
    def EnableStaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableStaggeredStart'], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables simulation of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Evpn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, then this BGP peer range supports BGP MPLS Based Ethernet VPN per draft-ietf-l2vpn-evpn-03. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Evpn'])
    @Evpn.setter
    def Evpn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Evpn'], value)

    @property
    def EvpnNextHopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It is used to replicate the traffic among the available Next Hops in Ingress Replication mode. Default value is 1. Minimum value is 1 and maximum value is 255.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnNextHopCount'])
    @EvpnNextHopCount.setter
    def EvpnNextHopCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EvpnNextHopCount'], value)

    @property
    def HoldTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The period of time between KEEP-ALIVE messages sent to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HoldTimer'])
    @HoldTimer.setter
    def HoldTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['HoldTimer'], value)

    @property
    def InterfaceStartIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this SM interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceStartIndex'])
    @InterfaceStartIndex.setter
    def InterfaceStartIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InterfaceStartIndex'], value)

    @property
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of interface to be selected for this BGP interface. One of:Protocol Interface, DHCP, PPP
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Interfaces(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def IpV4Mdt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of this Data MDT range on the simulated interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Mdt'])
    @IpV4Mdt.setter
    def IpV4Mdt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV4Mdt'], value)

    @property
    def IpV4Mpls(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv4 MPLS address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Mpls'])
    @IpV4Mpls.setter
    def IpV4Mpls(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV4Mpls'], value)

    @property
    def IpV4MplsVpn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv4 MPLS/VPN address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4MplsVpn'])
    @IpV4MplsVpn.setter
    def IpV4MplsVpn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV4MplsVpn'], value)

    @property
    def IpV4Multicast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv4 multicast address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Multicast'])
    @IpV4Multicast.setter
    def IpV4Multicast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV4Multicast'], value)

    @property
    def IpV4MulticastVpn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this BGP router/peer supports the IPv4 Multicast/VPN address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4MulticastVpn'])
    @IpV4MulticastVpn.setter
    def IpV4MulticastVpn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV4MulticastVpn'], value)

    @property
    def IpV4Unicast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv4 unicast address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV4Unicast'])
    @IpV4Unicast.setter
    def IpV4Unicast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV4Unicast'], value)

    @property
    def IpV6Mpls(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv6 MPLS address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6Mpls'])
    @IpV6Mpls.setter
    def IpV6Mpls(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV6Mpls'], value)

    @property
    def IpV6MplsVpn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv6 MPLS/VPN address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6MplsVpn'])
    @IpV6MplsVpn.setter
    def IpV6MplsVpn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV6MplsVpn'], value)

    @property
    def IpV6Multicast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv6 multicast address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6Multicast'])
    @IpV6Multicast.setter
    def IpV6Multicast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV6Multicast'], value)

    @property
    def IpV6MulticastVpn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this BGP router/peer supports the IPv6 Multicast/VPN address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6MulticastVpn'])
    @IpV6MulticastVpn.setter
    def IpV6MulticastVpn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV6MulticastVpn'], value)

    @property
    def IpV6Unicast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv6 unicast address family.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpV6Unicast'])
    @IpV6Unicast.setter
    def IpV6Unicast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpV6Unicast'], value)

    @property
    def IsAsbr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it is ASBR
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAsbr'])
    @IsAsbr.setter
    def IsAsbr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsAsbr'], value)

    @property
    def IsInterfaceLearnedInfoAvailable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, learned information is made avavilable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsInterfaceLearnedInfoAvailable'])

    @property
    def IsLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, learned information is refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedInfoRefreshed'])

    @property
    def LinkFlapDownTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the link flap down time
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkFlapDownTime'])
    @LinkFlapDownTime.setter
    def LinkFlapDownTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['LinkFlapDownTime'], value)

    @property
    def LinkFlapUpTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the link flap up time
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkFlapUpTime'])
    @LinkFlapUpTime.setter
    def LinkFlapUpTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['LinkFlapUpTime'], value)

    @property
    def LocalAsNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (External only) The first AS Num assigned to the simulated neighbor router. May be set for external neighbors on any port type, but only Linux-based ports may set this for internal neighbors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalAsNumber'])
    @LocalAsNumber.setter
    def LocalAsNumber(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LocalAsNumber'], value)

    @property
    def LocalIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IP address for the simulated neighbor routers and the number of routers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIpAddress'])
    @LocalIpAddress.setter
    def LocalIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LocalIpAddress'], value)

    @property
    def Md5Key(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Active only when MD5 is selected in the Authentication Type field.) (String) Enter a value to be used as a secret MD5 Key for authentication. The maximum length allowed is 255 characters.One MD5 key can be configured per BGP peer range. Sessions from all peers in this peer range will use this MD5 key if MD5 is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5Key'])
    @Md5Key.setter
    def Md5Key(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Md5Key'], value)

    @property
    def NextHop(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If enableNextHop is true, this is the IPv4 address used as the next hop. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])
    @NextHop.setter
    def NextHop(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NextHop'], value)

    @property
    def NumUpdatesPerIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages will be sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumUpdatesPerIteration'])
    @NumUpdatesPerIteration.setter
    def NumUpdatesPerIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumUpdatesPerIteration'], value)

    @property
    def RangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of routers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RangeCount'])
    @RangeCount.setter
    def RangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RangeCount'], value)

    @property
    def RemoteAsNumber(self):
        # type: () -> int
        """DEPRECATED 
        Returns
        -------
        - number: The remote Autonomous System number associated with the routers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteAsNumber'])
    @RemoteAsNumber.setter
    def RemoteAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RemoteAsNumber'], value)

    @property
    def RestartTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Controls the operation of BGP Graceful Restart.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RestartTime'])
    @RestartTime.setter
    def RestartTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RestartTime'], value)

    @property
    def StaggeredStartPeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Controls the staggering and period of initial start messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStartPeriod'])
    @StaggeredStartPeriod.setter
    def StaggeredStartPeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStartPeriod'], value)

    @property
    def StaleTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Controls the operation of BGP Graceful Restart.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaleTime'])
    @StaleTime.setter
    def StaleTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StaleTime'], value)

    @property
    def TcpWindowSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (External neighbor only) The TCP window used for communications from the neighbor. (default = 8,192)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpWindowSize'])
    @TcpWindowSize.setter
    def TcpWindowSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TcpWindowSize'], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def TtlValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The limited number of iterations that a unit of data can experience before the data is discarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TtlValue'])
    @TtlValue.setter
    def TtlValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TtlValue'], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(internal | external): Indicates that the neighbor is either an internal or external router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def UpdateInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The frequency with which UPDATE messages are sent to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateInterval'])
    @UpdateInterval.setter
    def UpdateInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpdateInterval'], value)

    @property
    def Vpls(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports BGP VPLS per the Kompella draft.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vpls'])
    @Vpls.setter
    def Vpls(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Vpls'], value)

    def update(self, AsNumMode=None, Authentication=None, BfdModeOfOperation=None, BgpId=None, DutIpAddress=None, Enable4ByteAsNum=None, EnableActAsRestarted=None, EnableBfdRegistration=None, EnableBgpId=None, EnableDiscardIxiaGeneratedRoutes=None, EnableGracefulRestart=None, EnableLinkFlap=None, EnableNextHop=None, EnableOptionalParameters=None, EnableSendIxiaSignatureWithRoutes=None, EnableStaggeredStart=None, Enabled=None, Evpn=None, EvpnNextHopCount=None, HoldTimer=None, InterfaceStartIndex=None, InterfaceType=None, Interfaces=None, IpV4Mdt=None, IpV4Mpls=None, IpV4MplsVpn=None, IpV4Multicast=None, IpV4MulticastVpn=None, IpV4Unicast=None, IpV6Mpls=None, IpV6MplsVpn=None, IpV6Multicast=None, IpV6MulticastVpn=None, IpV6Unicast=None, IsAsbr=None, LinkFlapDownTime=None, LinkFlapUpTime=None, LocalAsNumber=None, LocalIpAddress=None, Md5Key=None, NextHop=None, NumUpdatesPerIteration=None, RangeCount=None, RemoteAsNumber=None, RestartTime=None, StaggeredStartPeriod=None, StaleTime=None, TcpWindowSize=None, TrafficGroupId=None, TtlValue=None, Type=None, UpdateInterval=None, Vpls=None):
        # type: (str, str, str, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, str, str, str, int, int, int, int, int, int, int, str, int, str, int, bool) -> NeighborRange
        """Updates neighborRange resource on the server.

        Args
        ----
        - AsNumMode (str(fixed | increment)): (External only) Indicates that each new session uses a different AS number.
        - Authentication (str(null | md5)): Select the type of cryptographic authentication to be used for the BGP peers in this peer range.
        - BfdModeOfOperation (str(multiHop | singleHop)): Indicates whether to use a single-hop or a multi-hop mode of operation for the BFD session being created with a BGP peer.
        - BgpId (str): The BGP ID used in OPEN messages.
        - DutIpAddress (str): The IP address of the DUT router.
        - Enable4ByteAsNum (bool): Enables the 4-byte Autonomous System (AS) number of the DUT/SUT.
        - EnableActAsRestarted (bool): Controls the operation of BGP Graceful Restart.
        - EnableBfdRegistration (bool): Enables the BFD registration.
        - EnableBgpId (bool): The BGP ID used in OPEN messages.
        - EnableDiscardIxiaGeneratedRoutes (bool): If true, enables the discard of Ixia generated routes
        - EnableGracefulRestart (bool): Controls the operation of BGP Graceful Restart.
        - EnableLinkFlap (bool): If true, enables link flap
        - EnableNextHop (bool): Used for IPv4 traffic. Controls the use of the NEXT_HOP attribute. (default = disabled)
        - EnableOptionalParameters (bool): Controls how an OPEN is conducted in the presence of optional parameters.
        - EnableSendIxiaSignatureWithRoutes (bool): If true, enables sending of Ixia signature with routes
        - EnableStaggeredStart (bool): Controls the staggering and period of initial start messages.
        - Enabled (bool): Enables or disables simulation of the router.
        - Evpn (bool): If enabled, then this BGP peer range supports BGP MPLS Based Ethernet VPN per draft-ietf-l2vpn-evpn-03. Default value is false.
        - EvpnNextHopCount (number): It is used to replicate the traffic among the available Next Hops in Ingress Replication mode. Default value is 1. Minimum value is 1 and maximum value is 255.
        - HoldTimer (number): The period of time between KEEP-ALIVE messages sent to the DUT.
        - InterfaceStartIndex (number): The assigned protocol interface ID for this SM interface.
        - InterfaceType (str): The type of interface to be selected for this BGP interface. One of:Protocol Interface, DHCP, PPP
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - IpV4Mdt (bool): Enables the use of this Data MDT range on the simulated interface.
        - IpV4Mpls (bool): If enabled, this BGP router/peer supports the IPv4 MPLS address family.
        - IpV4MplsVpn (bool): If enabled, this BGP router/peer supports the IPv4 MPLS/VPN address family.
        - IpV4Multicast (bool): If enabled, this BGP router/peer supports the IPv4 multicast address family.
        - IpV4MulticastVpn (bool): If true, this BGP router/peer supports the IPv4 Multicast/VPN address family.
        - IpV4Unicast (bool): If enabled, this BGP router/peer supports the IPv4 unicast address family.
        - IpV6Mpls (bool): If enabled, this BGP router/peer supports the IPv6 MPLS address family.
        - IpV6MplsVpn (bool): If enabled, this BGP router/peer supports the IPv6 MPLS/VPN address family.
        - IpV6Multicast (bool): If enabled, this BGP router/peer supports the IPv6 multicast address family.
        - IpV6MulticastVpn (bool): If true, this BGP router/peer supports the IPv6 Multicast/VPN address family.
        - IpV6Unicast (bool): If enabled, this BGP router/peer supports the IPv6 unicast address family.
        - IsAsbr (bool): If true, it is ASBR
        - LinkFlapDownTime (number): Signifies the link flap down time
        - LinkFlapUpTime (number): Signifies the link flap up time
        - LocalAsNumber (str): (External only) The first AS Num assigned to the simulated neighbor router. May be set for external neighbors on any port type, but only Linux-based ports may set this for internal neighbors.
        - LocalIpAddress (str): The first IP address for the simulated neighbor routers and the number of routers.
        - Md5Key (str): (Active only when MD5 is selected in the Authentication Type field.) (String) Enter a value to be used as a secret MD5 Key for authentication. The maximum length allowed is 255 characters.One MD5 key can be configured per BGP peer range. Sessions from all peers in this peer range will use this MD5 key if MD5 is enabled.
        - NextHop (str): If enableNextHop is true, this is the IPv4 address used as the next hop. (default = 0.0.0.0)
        - NumUpdatesPerIteration (number): When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages will be sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance. (default = 1)
        - RangeCount (number): The number of routers.
        - RemoteAsNumber (number): The remote Autonomous System number associated with the routers.
        - RestartTime (number): Controls the operation of BGP Graceful Restart.
        - StaggeredStartPeriod (number): Controls the staggering and period of initial start messages.
        - StaleTime (number): Controls the operation of BGP Graceful Restart.
        - TcpWindowSize (number): (External neighbor only) The TCP window used for communications from the neighbor. (default = 8,192)
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TtlValue (number): The limited number of iterations that a unit of data can experience before the data is discarded.
        - Type (str(internal | external)): Indicates that the neighbor is either an internal or external router.
        - UpdateInterval (number): The frequency with which UPDATE messages are sent to the DUT.
        - Vpls (bool): If enabled, this BGP router/peer supports BGP VPLS per the Kompella draft.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AsNumMode=None, Authentication=None, BfdModeOfOperation=None, BgpId=None, DutIpAddress=None, Enable4ByteAsNum=None, EnableActAsRestarted=None, EnableBfdRegistration=None, EnableBgpId=None, EnableDiscardIxiaGeneratedRoutes=None, EnableGracefulRestart=None, EnableLinkFlap=None, EnableNextHop=None, EnableOptionalParameters=None, EnableSendIxiaSignatureWithRoutes=None, EnableStaggeredStart=None, Enabled=None, Evpn=None, EvpnNextHopCount=None, HoldTimer=None, InterfaceStartIndex=None, InterfaceType=None, Interfaces=None, IpV4Mdt=None, IpV4Mpls=None, IpV4MplsVpn=None, IpV4Multicast=None, IpV4MulticastVpn=None, IpV4Unicast=None, IpV6Mpls=None, IpV6MplsVpn=None, IpV6Multicast=None, IpV6MulticastVpn=None, IpV6Unicast=None, IsAsbr=None, LinkFlapDownTime=None, LinkFlapUpTime=None, LocalAsNumber=None, LocalIpAddress=None, Md5Key=None, NextHop=None, NumUpdatesPerIteration=None, RangeCount=None, RemoteAsNumber=None, RestartTime=None, StaggeredStartPeriod=None, StaleTime=None, TcpWindowSize=None, TrafficGroupId=None, TtlValue=None, Type=None, UpdateInterval=None, Vpls=None):
        # type: (str, str, str, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, str, str, str, int, int, int, int, int, int, int, str, int, str, int, bool) -> NeighborRange
        """Adds a new neighborRange resource on the server and adds it to the container.

        Args
        ----
        - AsNumMode (str(fixed | increment)): (External only) Indicates that each new session uses a different AS number.
        - Authentication (str(null | md5)): Select the type of cryptographic authentication to be used for the BGP peers in this peer range.
        - BfdModeOfOperation (str(multiHop | singleHop)): Indicates whether to use a single-hop or a multi-hop mode of operation for the BFD session being created with a BGP peer.
        - BgpId (str): The BGP ID used in OPEN messages.
        - DutIpAddress (str): The IP address of the DUT router.
        - Enable4ByteAsNum (bool): Enables the 4-byte Autonomous System (AS) number of the DUT/SUT.
        - EnableActAsRestarted (bool): Controls the operation of BGP Graceful Restart.
        - EnableBfdRegistration (bool): Enables the BFD registration.
        - EnableBgpId (bool): The BGP ID used in OPEN messages.
        - EnableDiscardIxiaGeneratedRoutes (bool): If true, enables the discard of Ixia generated routes
        - EnableGracefulRestart (bool): Controls the operation of BGP Graceful Restart.
        - EnableLinkFlap (bool): If true, enables link flap
        - EnableNextHop (bool): Used for IPv4 traffic. Controls the use of the NEXT_HOP attribute. (default = disabled)
        - EnableOptionalParameters (bool): Controls how an OPEN is conducted in the presence of optional parameters.
        - EnableSendIxiaSignatureWithRoutes (bool): If true, enables sending of Ixia signature with routes
        - EnableStaggeredStart (bool): Controls the staggering and period of initial start messages.
        - Enabled (bool): Enables or disables simulation of the router.
        - Evpn (bool): If enabled, then this BGP peer range supports BGP MPLS Based Ethernet VPN per draft-ietf-l2vpn-evpn-03. Default value is false.
        - EvpnNextHopCount (number): It is used to replicate the traffic among the available Next Hops in Ingress Replication mode. Default value is 1. Minimum value is 1 and maximum value is 255.
        - HoldTimer (number): The period of time between KEEP-ALIVE messages sent to the DUT.
        - InterfaceStartIndex (number): The assigned protocol interface ID for this SM interface.
        - InterfaceType (str): The type of interface to be selected for this BGP interface. One of:Protocol Interface, DHCP, PPP
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - IpV4Mdt (bool): Enables the use of this Data MDT range on the simulated interface.
        - IpV4Mpls (bool): If enabled, this BGP router/peer supports the IPv4 MPLS address family.
        - IpV4MplsVpn (bool): If enabled, this BGP router/peer supports the IPv4 MPLS/VPN address family.
        - IpV4Multicast (bool): If enabled, this BGP router/peer supports the IPv4 multicast address family.
        - IpV4MulticastVpn (bool): If true, this BGP router/peer supports the IPv4 Multicast/VPN address family.
        - IpV4Unicast (bool): If enabled, this BGP router/peer supports the IPv4 unicast address family.
        - IpV6Mpls (bool): If enabled, this BGP router/peer supports the IPv6 MPLS address family.
        - IpV6MplsVpn (bool): If enabled, this BGP router/peer supports the IPv6 MPLS/VPN address family.
        - IpV6Multicast (bool): If enabled, this BGP router/peer supports the IPv6 multicast address family.
        - IpV6MulticastVpn (bool): If true, this BGP router/peer supports the IPv6 Multicast/VPN address family.
        - IpV6Unicast (bool): If enabled, this BGP router/peer supports the IPv6 unicast address family.
        - IsAsbr (bool): If true, it is ASBR
        - LinkFlapDownTime (number): Signifies the link flap down time
        - LinkFlapUpTime (number): Signifies the link flap up time
        - LocalAsNumber (str): (External only) The first AS Num assigned to the simulated neighbor router. May be set for external neighbors on any port type, but only Linux-based ports may set this for internal neighbors.
        - LocalIpAddress (str): The first IP address for the simulated neighbor routers and the number of routers.
        - Md5Key (str): (Active only when MD5 is selected in the Authentication Type field.) (String) Enter a value to be used as a secret MD5 Key for authentication. The maximum length allowed is 255 characters.One MD5 key can be configured per BGP peer range. Sessions from all peers in this peer range will use this MD5 key if MD5 is enabled.
        - NextHop (str): If enableNextHop is true, this is the IPv4 address used as the next hop. (default = 0.0.0.0)
        - NumUpdatesPerIteration (number): When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages will be sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance. (default = 1)
        - RangeCount (number): The number of routers.
        - RemoteAsNumber (number): The remote Autonomous System number associated with the routers.
        - RestartTime (number): Controls the operation of BGP Graceful Restart.
        - StaggeredStartPeriod (number): Controls the staggering and period of initial start messages.
        - StaleTime (number): Controls the operation of BGP Graceful Restart.
        - TcpWindowSize (number): (External neighbor only) The TCP window used for communications from the neighbor. (default = 8,192)
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TtlValue (number): The limited number of iterations that a unit of data can experience before the data is discarded.
        - Type (str(internal | external)): Indicates that the neighbor is either an internal or external router.
        - UpdateInterval (number): The frequency with which UPDATE messages are sent to the DUT.
        - Vpls (bool): If enabled, this BGP router/peer supports BGP VPLS per the Kompella draft.

        Returns
        -------
        - self: This instance with all currently retrieved neighborRange resources using find and the newly added neighborRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained neighborRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AsNumMode=None, Authentication=None, BfdModeOfOperation=None, BgpId=None, DutIpAddress=None, Enable4ByteAsNum=None, EnableActAsRestarted=None, EnableBfdRegistration=None, EnableBgpId=None, EnableDiscardIxiaGeneratedRoutes=None, EnableGracefulRestart=None, EnableLinkFlap=None, EnableNextHop=None, EnableOptionalParameters=None, EnableSendIxiaSignatureWithRoutes=None, EnableStaggeredStart=None, Enabled=None, Evpn=None, EvpnNextHopCount=None, HoldTimer=None, InterfaceStartIndex=None, InterfaceType=None, Interfaces=None, IpV4Mdt=None, IpV4Mpls=None, IpV4MplsVpn=None, IpV4Multicast=None, IpV4MulticastVpn=None, IpV4Unicast=None, IpV6Mpls=None, IpV6MplsVpn=None, IpV6Multicast=None, IpV6MulticastVpn=None, IpV6Unicast=None, IsAsbr=None, IsInterfaceLearnedInfoAvailable=None, IsLearnedInfoRefreshed=None, LinkFlapDownTime=None, LinkFlapUpTime=None, LocalAsNumber=None, LocalIpAddress=None, Md5Key=None, NextHop=None, NumUpdatesPerIteration=None, RangeCount=None, RemoteAsNumber=None, RestartTime=None, StaggeredStartPeriod=None, StaleTime=None, TcpWindowSize=None, TrafficGroupId=None, TtlValue=None, Type=None, UpdateInterval=None, Vpls=None):
        # type: (str, str, str, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, str, str, str, int, int, int, int, int, int, int, str, int, str, int, bool) -> NeighborRange
        """Finds and retrieves neighborRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve neighborRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all neighborRange resources from the server.

        Args
        ----
        - AsNumMode (str(fixed | increment)): (External only) Indicates that each new session uses a different AS number.
        - Authentication (str(null | md5)): Select the type of cryptographic authentication to be used for the BGP peers in this peer range.
        - BfdModeOfOperation (str(multiHop | singleHop)): Indicates whether to use a single-hop or a multi-hop mode of operation for the BFD session being created with a BGP peer.
        - BgpId (str): The BGP ID used in OPEN messages.
        - DutIpAddress (str): The IP address of the DUT router.
        - Enable4ByteAsNum (bool): Enables the 4-byte Autonomous System (AS) number of the DUT/SUT.
        - EnableActAsRestarted (bool): Controls the operation of BGP Graceful Restart.
        - EnableBfdRegistration (bool): Enables the BFD registration.
        - EnableBgpId (bool): The BGP ID used in OPEN messages.
        - EnableDiscardIxiaGeneratedRoutes (bool): If true, enables the discard of Ixia generated routes
        - EnableGracefulRestart (bool): Controls the operation of BGP Graceful Restart.
        - EnableLinkFlap (bool): If true, enables link flap
        - EnableNextHop (bool): Used for IPv4 traffic. Controls the use of the NEXT_HOP attribute. (default = disabled)
        - EnableOptionalParameters (bool): Controls how an OPEN is conducted in the presence of optional parameters.
        - EnableSendIxiaSignatureWithRoutes (bool): If true, enables sending of Ixia signature with routes
        - EnableStaggeredStart (bool): Controls the staggering and period of initial start messages.
        - Enabled (bool): Enables or disables simulation of the router.
        - Evpn (bool): If enabled, then this BGP peer range supports BGP MPLS Based Ethernet VPN per draft-ietf-l2vpn-evpn-03. Default value is false.
        - EvpnNextHopCount (number): It is used to replicate the traffic among the available Next Hops in Ingress Replication mode. Default value is 1. Minimum value is 1 and maximum value is 255.
        - HoldTimer (number): The period of time between KEEP-ALIVE messages sent to the DUT.
        - InterfaceStartIndex (number): The assigned protocol interface ID for this SM interface.
        - InterfaceType (str): The type of interface to be selected for this BGP interface. One of:Protocol Interface, DHCP, PPP
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - IpV4Mdt (bool): Enables the use of this Data MDT range on the simulated interface.
        - IpV4Mpls (bool): If enabled, this BGP router/peer supports the IPv4 MPLS address family.
        - IpV4MplsVpn (bool): If enabled, this BGP router/peer supports the IPv4 MPLS/VPN address family.
        - IpV4Multicast (bool): If enabled, this BGP router/peer supports the IPv4 multicast address family.
        - IpV4MulticastVpn (bool): If true, this BGP router/peer supports the IPv4 Multicast/VPN address family.
        - IpV4Unicast (bool): If enabled, this BGP router/peer supports the IPv4 unicast address family.
        - IpV6Mpls (bool): If enabled, this BGP router/peer supports the IPv6 MPLS address family.
        - IpV6MplsVpn (bool): If enabled, this BGP router/peer supports the IPv6 MPLS/VPN address family.
        - IpV6Multicast (bool): If enabled, this BGP router/peer supports the IPv6 multicast address family.
        - IpV6MulticastVpn (bool): If true, this BGP router/peer supports the IPv6 Multicast/VPN address family.
        - IpV6Unicast (bool): If enabled, this BGP router/peer supports the IPv6 unicast address family.
        - IsAsbr (bool): If true, it is ASBR
        - IsInterfaceLearnedInfoAvailable (bool): If true, learned information is made avavilable.
        - IsLearnedInfoRefreshed (bool): If true, learned information is refreshed.
        - LinkFlapDownTime (number): Signifies the link flap down time
        - LinkFlapUpTime (number): Signifies the link flap up time
        - LocalAsNumber (str): (External only) The first AS Num assigned to the simulated neighbor router. May be set for external neighbors on any port type, but only Linux-based ports may set this for internal neighbors.
        - LocalIpAddress (str): The first IP address for the simulated neighbor routers and the number of routers.
        - Md5Key (str): (Active only when MD5 is selected in the Authentication Type field.) (String) Enter a value to be used as a secret MD5 Key for authentication. The maximum length allowed is 255 characters.One MD5 key can be configured per BGP peer range. Sessions from all peers in this peer range will use this MD5 key if MD5 is enabled.
        - NextHop (str): If enableNextHop is true, this is the IPv4 address used as the next hop. (default = 0.0.0.0)
        - NumUpdatesPerIteration (number): When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages will be sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance. (default = 1)
        - RangeCount (number): The number of routers.
        - RemoteAsNumber (number): The remote Autonomous System number associated with the routers.
        - RestartTime (number): Controls the operation of BGP Graceful Restart.
        - StaggeredStartPeriod (number): Controls the staggering and period of initial start messages.
        - StaleTime (number): Controls the operation of BGP Graceful Restart.
        - TcpWindowSize (number): (External neighbor only) The TCP window used for communications from the neighbor. (default = 8,192)
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TtlValue (number): The limited number of iterations that a unit of data can experience before the data is discarded.
        - Type (str(internal | external)): Indicates that the neighbor is either an internal or external router.
        - UpdateInterval (number): The frequency with which UPDATE messages are sent to the DUT.
        - Vpls (bool): If enabled, this BGP router/peer supports BGP VPLS per the Kompella draft.

        Returns
        -------
        - self: This instance with matching neighborRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of neighborRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the neighborRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        ?

        getInterfaceAccessorIfaceList(async_operation=bool)string
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)

    def GetInterfaceLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getInterfaceLearnedInfo operation on the server.

        This function allows to Get the interface learned information.

        getInterfaceLearnedInfo(async_operation=bool)string
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getInterfaceLearnedInfo', payload=payload, response_object=None)

    def RefreshLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInfo operation on the server.

        This function allows to refresh the BGP learned information from the DUT.

        refreshLearnedInfo(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
