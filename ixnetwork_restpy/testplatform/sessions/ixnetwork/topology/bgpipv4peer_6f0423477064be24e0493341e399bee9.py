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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class BgpIpv4Peer(Base):
    """Bgp IPv4 Peer
    The BgpIpv4Peer class encapsulates a list of bgpIpv4Peer resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpIpv4Peer.find() method.
    The list can be managed by using the BgpIpv4Peer.add() and BgpIpv4Peer.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bgpIpv4Peer"
    _SDM_ATT_MAP = {
        "ActAsRestarted": "actAsRestarted",
        "Active": "active",
        "AdvertiseEndOfRib": "advertiseEndOfRib",
        "AdvertiseEvpnRoutesForOtherVtep": "advertiseEvpnRoutesForOtherVtep",
        "AdvertiseTunnelEncapsulationExtendedCommunity": "advertiseTunnelEncapsulationExtendedCommunity",
        "AllowIxiaSignatureSuffix": "allowIxiaSignatureSuffix",
        "AlwaysIncludeTunnelEncExtCommunity": "alwaysIncludeTunnelEncExtCommunity",
        "AsSetMode": "asSetMode",
        "Authentication": "authentication",
        "BgpFsmState": "bgpFsmState",
        "BgpId": "bgpId",
        "BgpLsAsSetMode": "bgpLsAsSetMode",
        "BgpLsEnableAsPathSegments": "bgpLsEnableAsPathSegments",
        "BgpLsEnableCluster": "bgpLsEnableCluster",
        "BgpLsEnableExtendedCommunity": "bgpLsEnableExtendedCommunity",
        "BgpLsNoOfASPathSegments": "bgpLsNoOfASPathSegments",
        "BgpLsNoOfClusters": "bgpLsNoOfClusters",
        "BgpLsNoOfCommunities": "bgpLsNoOfCommunities",
        "BgpLsOverridePeerAsSetMode": "bgpLsOverridePeerAsSetMode",
        "CapabilityExtendedMessage": "capabilityExtendedMessage",
        "CapabilityIpV4Mdt": "capabilityIpV4Mdt",
        "CapabilityIpV4Mpls": "capabilityIpV4Mpls",
        "CapabilityIpV4MplsVpn": "capabilityIpV4MplsVpn",
        "CapabilityIpV4Multicast": "capabilityIpV4Multicast",
        "CapabilityIpV4MulticastVpn": "capabilityIpV4MulticastVpn",
        "CapabilityIpV4Unicast": "capabilityIpV4Unicast",
        "CapabilityIpV6Mpls": "capabilityIpV6Mpls",
        "CapabilityIpV6MplsVpn": "capabilityIpV6MplsVpn",
        "CapabilityIpV6Multicast": "capabilityIpV6Multicast",
        "CapabilityIpV6MulticastVpn": "capabilityIpV6MulticastVpn",
        "CapabilityIpV6Unicast": "capabilityIpV6Unicast",
        "CapabilityIpv4MplsAddPath": "capabilityIpv4MplsAddPath",
        "CapabilityIpv4MplsVPNAddPath": "capabilityIpv4MplsVPNAddPath",
        "CapabilityIpv4UnicastAddPath": "capabilityIpv4UnicastAddPath",
        "CapabilityIpv6MplsAddPath": "capabilityIpv6MplsAddPath",
        "CapabilityIpv6MplsVPNAddPath": "capabilityIpv6MplsVPNAddPath",
        "CapabilityIpv6UnicastAddPath": "capabilityIpv6UnicastAddPath",
        "CapabilityLinkStateNonVpn": "capabilityLinkStateNonVpn",
        "CapabilityLinkStateVpn": "capabilityLinkStateVpn",
        "CapabilityRouteConstraint": "capabilityRouteConstraint",
        "CapabilityRouteRefresh": "capabilityRouteRefresh",
        "CapabilitySRTEPoliciesV4": "capabilitySRTEPoliciesV4",
        "CapabilitySRTEPoliciesV6": "capabilitySRTEPoliciesV6",
        "CapabilityVpls": "capabilityVpls",
        "Capabilityipv4UnicastFlowSpec": "capabilityipv4UnicastFlowSpec",
        "Capabilityipv6UnicastFlowSpec": "capabilityipv6UnicastFlowSpec",
        "ConfigureKeepaliveTimer": "configureKeepaliveTimer",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "CustomSidType": "customSidType",
        "DescriptiveName": "descriptiveName",
        "DiscardIxiaGeneratedRoutes": "discardIxiaGeneratedRoutes",
        "DowntimeInSec": "downtimeInSec",
        "DutIp": "dutIp",
        "Enable4ByteAs": "enable4ByteAs",
        "EnableBfdRegistration": "enableBfdRegistration",
        "EnableBgpId": "enableBgpId",
        "EnableBgpIdSameasRouterId": "enableBgpIdSameasRouterId",
        "EnableBgpLsCommunity": "enableBgpLsCommunity",
        "EnableEpeTraffic": "enableEpeTraffic",
        "EnableGracefulRestart": "enableGracefulRestart",
        "EnableLlgr": "enableLlgr",
        "Errors": "errors",
        "EthernetSegmentsCountV4": "ethernetSegmentsCountV4",
        "Evpn": "evpn",
        "FilterEvpn": "filterEvpn",
        "FilterIpV4Mpls": "filterIpV4Mpls",
        "FilterIpV4MplsVpn": "filterIpV4MplsVpn",
        "FilterIpV4Multicast": "filterIpV4Multicast",
        "FilterIpV4MulticastVpn": "filterIpV4MulticastVpn",
        "FilterIpV4Unicast": "filterIpV4Unicast",
        "FilterIpV6Mpls": "filterIpV6Mpls",
        "FilterIpV6MplsVpn": "filterIpV6MplsVpn",
        "FilterIpV6Multicast": "filterIpV6Multicast",
        "FilterIpV6MulticastVpn": "filterIpV6MulticastVpn",
        "FilterIpV6Unicast": "filterIpV6Unicast",
        "FilterIpv4MulticastBgpMplsVpn": "filterIpv4MulticastBgpMplsVpn",
        "FilterIpv4UnicastFlowSpec": "filterIpv4UnicastFlowSpec",
        "FilterIpv6MulticastBgpMplsVpn": "filterIpv6MulticastBgpMplsVpn",
        "FilterIpv6UnicastFlowSpec": "filterIpv6UnicastFlowSpec",
        "FilterLinkState": "filterLinkState",
        "FilterLinkStateVpn": "filterLinkStateVpn",
        "FilterSRTEPoliciesV4": "filterSRTEPoliciesV4",
        "FilterSRTEPoliciesV6": "filterSRTEPoliciesV6",
        "FilterVpls": "filterVpls",
        "Flap": "flap",
        "HoldTimer": "holdTimer",
        "IpVrfToIpVrfType": "ipVrfToIpVrfType",
        "Ipv4MplsAddPathMode": "ipv4MplsAddPathMode",
        "Ipv4MplsCapability": "ipv4MplsCapability",
        "Ipv4MplsVPNAddPathMode": "ipv4MplsVPNAddPathMode",
        "Ipv4MulticastBgpMplsVpn": "ipv4MulticastBgpMplsVpn",
        "Ipv4MultipleMplsLabelsCapability": "ipv4MultipleMplsLabelsCapability",
        "Ipv4UnicastAddPathMode": "ipv4UnicastAddPathMode",
        "Ipv6MplsAddPathMode": "ipv6MplsAddPathMode",
        "Ipv6MplsCapability": "ipv6MplsCapability",
        "Ipv6MplsVPNAddPathMode": "ipv6MplsVPNAddPathMode",
        "Ipv6MulticastBgpMplsVpn": "ipv6MulticastBgpMplsVpn",
        "Ipv6MultipleMplsLabelsCapability": "ipv6MultipleMplsLabelsCapability",
        "Ipv6UnicastAddPathMode": "ipv6UnicastAddPathMode",
        "IrbInterfaceLabel": "irbInterfaceLabel",
        "IrbIpv4Address": "irbIpv4Address",
        "IxiaSignatureSuffix": "ixiaSignatureSuffix",
        "KeepaliveTimer": "keepaliveTimer",
        "L3VPNEncapsulationType": "l3VPNEncapsulationType",
        "LocalAs2Bytes": "localAs2Bytes",
        "LocalAs4Bytes": "localAs4Bytes",
        "LocalIpv4Ver2": "localIpv4Ver2",
        "LocalRouterID": "localRouterID",
        "MaxBGPMsgLengthTx": "maxBGPMsgLengthTx",
        "Md5Key": "md5Key",
        "ModeOfBfdOperations": "modeOfBfdOperations",
        "MplsLabelsCountForIpv4MplsRoute": "mplsLabelsCountForIpv4MplsRoute",
        "MplsLabelsCountForIpv6MplsRoute": "mplsLabelsCountForIpv6MplsRoute",
        "Multiplier": "multiplier",
        "Name": "name",
        "NoOfEpePeers": "noOfEpePeers",
        "NoOfExtendedCommunities": "noOfExtendedCommunities",
        "NoOfUserDefinedAfiSafi": "noOfUserDefinedAfiSafi",
        "NumBgpLsId": "numBgpLsId",
        "NumBgpLsInstanceIdentifier": "numBgpLsInstanceIdentifier",
        "NumBgpUpdatesGeneratedPerIteration": "numBgpUpdatesGeneratedPerIteration",
        "NumberColorFlexAlgoMapping": "numberColorFlexAlgoMapping",
        "NumberFlowSpecRangeV4": "numberFlowSpecRangeV4",
        "NumberFlowSpecRangeV6": "numberFlowSpecRangeV6",
        "NumberSRTEPolicies": "numberSRTEPolicies",
        "OperationalModel": "operationalModel",
        "RestartTime": "restartTime",
        "RoutersMacOrIrbMacAddress": "routersMacOrIrbMacAddress",
        "SRGBRangeCount": "sRGBRangeCount",
        "SendIxiaSignatureWithRoutes": "sendIxiaSignatureWithRoutes",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StaleTime": "staleTime",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TcpWindowSizeInBytes": "tcpWindowSizeInBytes",
        "Ttl": "ttl",
        "Type": "type",
        "UdpPortEndValue": "udpPortEndValue",
        "UdpPortStartValue": "udpPortStartValue",
        "UpdateInterval": "updateInterval",
        "UptimeInSec": "uptimeInSec",
        "VplsEnableNextHop": "vplsEnableNextHop",
        "VplsNextHop": "vplsNextHop",
    }
    _SDM_ENUM_MAP = {
        "ipVrfToIpVrfType": [
            "interfaceLess",
            "interfacefullWithCorefacingIRB",
            "interfacefullWithUnnumberedCorefacingIRB",
        ],
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(BgpIpv4Peer, self).__init__(parent, list_op)

    @property
    def BgpCustomAfiSafiv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcustomafisafiv4_3755a44fa17f2a2c8666f79d7f4bbce7.BgpCustomAfiSafiv4): An instance of the BgpCustomAfiSafiv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcustomafisafiv4_3755a44fa17f2a2c8666f79d7f4bbce7 import (
            BgpCustomAfiSafiv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpCustomAfiSafiv4", None) is not None:
                return self._properties.get("BgpCustomAfiSafiv4")
        return BgpCustomAfiSafiv4(self)._select()

    @property
    def BgpEpePeerList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlist_8d99c24c6bc075dd9519d2ac06779a94.BgpEpePeerList): An instance of the BgpEpePeerList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlist_8d99c24c6bc075dd9519d2ac06779a94 import (
            BgpEpePeerList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEpePeerList", None) is not None:
                return self._properties.get("BgpEpePeerList")
        return BgpEpePeerList(self)._select()

    @property
    def BgpEthernetSegmentV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpethernetsegmentv4_2514045783c23a908611c72c13ab7e8f.BgpEthernetSegmentV4): An instance of the BgpEthernetSegmentV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpethernetsegmentv4_2514045783c23a908611c72c13ab7e8f import (
            BgpEthernetSegmentV4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEthernetSegmentV4", None) is not None:
                return self._properties.get("BgpEthernetSegmentV4")
        return BgpEthernetSegmentV4(self)._select()

    @property
    def BgpFlowSpecRangesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslist_850749b96bb629595bbddf006a29b1eb.BgpFlowSpecRangesList): An instance of the BgpFlowSpecRangesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslist_850749b96bb629595bbddf006a29b1eb import (
            BgpFlowSpecRangesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpFlowSpecRangesList", None) is not None:
                return self._properties.get("BgpFlowSpecRangesList")
        return BgpFlowSpecRangesList(self)._select()

    @property
    def BgpFlowSpecRangesListV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv4_0163de8cc99a19d1385a21d26b93a544.BgpFlowSpecRangesListV4): An instance of the BgpFlowSpecRangesListV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv4_0163de8cc99a19d1385a21d26b93a544 import (
            BgpFlowSpecRangesListV4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpFlowSpecRangesListV4", None) is not None:
                return self._properties.get("BgpFlowSpecRangesListV4")
        return BgpFlowSpecRangesListV4(self)._select()

    @property
    def BgpFlowSpecRangesListV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv6_c579a493ccdc64a6383fef9d60aac4cc.BgpFlowSpecRangesListV6): An instance of the BgpFlowSpecRangesListV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv6_c579a493ccdc64a6383fef9d60aac4cc import (
            BgpFlowSpecRangesListV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpFlowSpecRangesListV6", None) is not None:
                return self._properties.get("BgpFlowSpecRangesListV6")
        return BgpFlowSpecRangesListV6(self)._select()

    @property
    def BgpIPv4EvpnEvi(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnevi_05f1ea70759fa1436b3981f124b83276.BgpIPv4EvpnEvi): An instance of the BgpIPv4EvpnEvi class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnevi_05f1ea70759fa1436b3981f124b83276 import (
            BgpIPv4EvpnEvi,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIPv4EvpnEvi", None) is not None:
                return self._properties.get("BgpIPv4EvpnEvi")
        return BgpIPv4EvpnEvi(self)

    @property
    def BgpIPv4EvpnPbb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnpbb_f1db536c355bf8211909601b21790955.BgpIPv4EvpnPbb): An instance of the BgpIPv4EvpnPbb class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnpbb_f1db536c355bf8211909601b21790955 import (
            BgpIPv4EvpnPbb,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIPv4EvpnPbb", None) is not None:
                return self._properties.get("BgpIPv4EvpnPbb")
        return BgpIPv4EvpnPbb(self)

    @property
    def BgpIPv4EvpnVXLAN(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnvxlan_ac7a890f916ca5599eb4618d697c2f6e.BgpIPv4EvpnVXLAN): An instance of the BgpIPv4EvpnVXLAN class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnvxlan_ac7a890f916ca5599eb4618d697c2f6e import (
            BgpIPv4EvpnVXLAN,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIPv4EvpnVXLAN", None) is not None:
                return self._properties.get("BgpIPv4EvpnVXLAN")
        return BgpIPv4EvpnVXLAN(self)

    @property
    def BgpIPv4EvpnVXLANVpws(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnvxlanvpws_8885c446b89d80aaa511ee82c37e924f.BgpIPv4EvpnVXLANVpws): An instance of the BgpIPv4EvpnVXLANVpws class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnvxlanvpws_8885c446b89d80aaa511ee82c37e924f import (
            BgpIPv4EvpnVXLANVpws,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIPv4EvpnVXLANVpws", None) is not None:
                return self._properties.get("BgpIPv4EvpnVXLANVpws")
        return BgpIPv4EvpnVXLANVpws(self)

    @property
    def BgpIPv4EvpnVpws(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnvpws_e8af65dd80ab4466e956b1bd0656c202.BgpIPv4EvpnVpws): An instance of the BgpIPv4EvpnVpws class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4evpnvpws_e8af65dd80ab4466e956b1bd0656c202 import (
            BgpIPv4EvpnVpws,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIPv4EvpnVpws", None) is not None:
                return self._properties.get("BgpIPv4EvpnVpws")
        return BgpIPv4EvpnVpws(self)

    @property
    def BgpIpv4AdL2Vpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4adl2vpn_08c7fedfc475cb9798d64a65caa67e97.BgpIpv4AdL2Vpn): An instance of the BgpIpv4AdL2Vpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4adl2vpn_08c7fedfc475cb9798d64a65caa67e97 import (
            BgpIpv4AdL2Vpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv4AdL2Vpn", None) is not None:
                return self._properties.get("BgpIpv4AdL2Vpn")
        return BgpIpv4AdL2Vpn(self)

    @property
    def BgpIpv4L2Site(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4l2site_3fc887aa9816db034ba10b85d4b057ee.BgpIpv4L2Site): An instance of the BgpIpv4L2Site class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4l2site_3fc887aa9816db034ba10b85d4b057ee import (
            BgpIpv4L2Site,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv4L2Site", None) is not None:
                return self._properties.get("BgpIpv4L2Site")
        return BgpIpv4L2Site(self)

    @property
    def BgpIpv4MVrf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4mvrf_200ce763656bd00177bc416b83bf991a.BgpIpv4MVrf): An instance of the BgpIpv4MVrf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4mvrf_200ce763656bd00177bc416b83bf991a import (
            BgpIpv4MVrf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv4MVrf", None) is not None:
                return self._properties.get("BgpIpv4MVrf")
        return BgpIpv4MVrf(self)

    @property
    def BgpLsAsPathSegmentList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsaspathsegmentlist_fed4f671dbff6ccda8e8824fbe375856.BgpLsAsPathSegmentList): An instance of the BgpLsAsPathSegmentList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsaspathsegmentlist_fed4f671dbff6ccda8e8824fbe375856 import (
            BgpLsAsPathSegmentList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpLsAsPathSegmentList", None) is not None:
                return self._properties.get("BgpLsAsPathSegmentList")
        return BgpLsAsPathSegmentList(self)

    @property
    def BgpLsClusterIdList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsclusteridlist_7b4bcec76ea98c69afbc1dcb2556f669.BgpLsClusterIdList): An instance of the BgpLsClusterIdList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsclusteridlist_7b4bcec76ea98c69afbc1dcb2556f669 import (
            BgpLsClusterIdList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpLsClusterIdList", None) is not None:
                return self._properties.get("BgpLsClusterIdList")
        return BgpLsClusterIdList(self)

    @property
    def BgpLsCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplscommunitieslist_4de2ae5e4864bdf5a8d1e869bc852de2.BgpLsCommunitiesList): An instance of the BgpLsCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplscommunitieslist_4de2ae5e4864bdf5a8d1e869bc852de2 import (
            BgpLsCommunitiesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpLsCommunitiesList", None) is not None:
                return self._properties.get("BgpLsCommunitiesList")
        return BgpLsCommunitiesList(self)

    @property
    def BgpLsExtendedCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsextendedcommunitieslist_122b706e8dda6c5aa9ede89bef707eb5.BgpLsExtendedCommunitiesList): An instance of the BgpLsExtendedCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsextendedcommunitieslist_122b706e8dda6c5aa9ede89bef707eb5 import (
            BgpLsExtendedCommunitiesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpLsExtendedCommunitiesList", None) is not None:
                return self._properties.get("BgpLsExtendedCommunitiesList")
        return BgpLsExtendedCommunitiesList(self)

    @property
    def BgpSRGBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrgbrangesubobjectslist_6e28159e439bbeffe19ca2de4c7f7879.BgpSRGBRangeSubObjectsList): An instance of the BgpSRGBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrgbrangesubobjectslist_6e28159e439bbeffe19ca2de4c7f7879 import (
            BgpSRGBRangeSubObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpSRGBRangeSubObjectsList", None) is not None:
                return self._properties.get("BgpSRGBRangeSubObjectsList")
        return BgpSRGBRangeSubObjectsList(self)

    @property
    def BgpSRTEPoliciesListV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepolicieslistv4_f2d756189af5037098439a3ddb4c82c5.BgpSRTEPoliciesListV4): An instance of the BgpSRTEPoliciesListV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepolicieslistv4_f2d756189af5037098439a3ddb4c82c5 import (
            BgpSRTEPoliciesListV4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpSRTEPoliciesListV4", None) is not None:
                return self._properties.get("BgpSRTEPoliciesListV4")
        return BgpSRTEPoliciesListV4(self)._select()

    @property
    def BgpVrf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpvrf_0cb79569071cf4c1cb6a19d71168e407.BgpVrf): An instance of the BgpVrf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpvrf_0cb79569071cf4c1cb6a19d71168e407 import (
            BgpVrf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpVrf", None) is not None:
                return self._properties.get("BgpVrf")
        return BgpVrf(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import (
            Connector,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Connector", None) is not None:
                return self._properties.get("Connector")
        return Connector(self)

    @property
    def FlexAlgoColorMappingTemplate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flexalgocolormappingtemplate_8e0816b88fc7b32d81aaa2e2335895f1.FlexAlgoColorMappingTemplate): An instance of the FlexAlgoColorMappingTemplate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flexalgocolormappingtemplate_8e0816b88fc7b32d81aaa2e2335895f1 import (
            FlexAlgoColorMappingTemplate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlexAlgoColorMappingTemplate", None) is not None:
                return self._properties.get("FlexAlgoColorMappingTemplate")
        return FlexAlgoColorMappingTemplate(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_421be1db953efaf826fe146cf9700e26.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_421be1db953efaf826fe146cf9700e26 import (
            TlvProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TlvProfile", None) is not None:
                return self._properties.get("TlvProfile")
        return TlvProfile(self)

    @property
    def ActAsRestarted(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Act as restarted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActAsRestarted"])
        )

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AdvertiseEndOfRib(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise End-Of-RIB
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseEndOfRib"])
        )

    @property
    def AdvertiseEvpnRoutesForOtherVtep(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Advertise EVPN routes for other VTEPS
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertiseEvpnRoutesForOtherVtep"])

    @AdvertiseEvpnRoutesForOtherVtep.setter
    def AdvertiseEvpnRoutesForOtherVtep(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvertiseEvpnRoutesForOtherVtep"], value)

    @property
    def AdvertiseTunnelEncapsulationExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Tunnel Encapsulation Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AdvertiseTunnelEncapsulationExtendedCommunity"]
            ),
        )

    @property
    def AllowIxiaSignatureSuffix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is ixia signature suffix, routes with this suffix will be learned. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc c. Keep empty if routes with all ixia signature need to be discarded.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AllowIxiaSignatureSuffix"])
        )

    @property
    def AlwaysIncludeTunnelEncExtCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Always Include Tunnel Encapsulation Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AlwaysIncludeTunnelEncExtCommunity"]
            ),
        )

    @property
    def AsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AsSetMode"]))

    @property
    def Authentication(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Authentication"])
        )

    @property
    def BgpFsmState(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[active | connect | error | established | idle | none | openConfirm | openSent]): Logs additional information about the BGP Peer State
        """
        return self._get_attribute(self._SDM_ATT_MAP["BgpFsmState"])

    @property
    def BgpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BgpId"]))

    @property
    def BgpLsAsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpLsAsSetMode"])
        )

    @property
    def BgpLsEnableAsPathSegments(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AS Path Segments
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpLsEnableAsPathSegments"])
        )

    @property
    def BgpLsEnableCluster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Cluster
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpLsEnableCluster"])
        )

    @property
    def BgpLsEnableExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpLsEnableExtendedCommunity"])
        )

    @property
    def BgpLsNoOfASPathSegments(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number Of AS Path Segments Per Route Range
        """
        return self._get_attribute(self._SDM_ATT_MAP["BgpLsNoOfASPathSegments"])

    @BgpLsNoOfASPathSegments.setter
    def BgpLsNoOfASPathSegments(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BgpLsNoOfASPathSegments"], value)

    @property
    def BgpLsNoOfClusters(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Clusters
        """
        return self._get_attribute(self._SDM_ATT_MAP["BgpLsNoOfClusters"])

    @BgpLsNoOfClusters.setter
    def BgpLsNoOfClusters(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BgpLsNoOfClusters"], value)

    @property
    def BgpLsNoOfCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP["BgpLsNoOfCommunities"])

    @BgpLsNoOfCommunities.setter
    def BgpLsNoOfCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BgpLsNoOfCommunities"], value)

    @property
    def BgpLsOverridePeerAsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpLsOverridePeerAsSetMode"])
        )

    @property
    def CapabilityExtendedMessage(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Extended Message Capability (Capability code 6, length 0): If enabled, a BGP Peer is able to receive and handle BGP messages having a maximum size of 65535 bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityExtendedMessage"])
        )

    @property
    def CapabilityIpV4Mdt(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 BGP MDT: AFI = 1, SAFI = 66
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV4Mdt"])
        )

    @property
    def CapabilityIpV4Mpls(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 MPLS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV4Mpls"])
        )

    @property
    def CapabilityIpV4MplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 MPLS VPN Capability: AFI=1,SAFI=128
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV4MplsVpn"])
        )

    @property
    def CapabilityIpV4Multicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Multicast Capability: AFI=1,SAFI=2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV4Multicast"])
        )

    @property
    def CapabilityIpV4MulticastVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP MCAST-VPN: AFI = 1, SAFI = 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV4MulticastVpn"])
        )

    @property
    def CapabilityIpV4Unicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Unicast Capability: AFI=1,SAFI=1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV4Unicast"])
        )

    @property
    def CapabilityIpV6Mpls(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 MPLS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV6Mpls"])
        )

    @property
    def CapabilityIpV6MplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 MPLS VPN Capability: AFI=2,SAFI=128
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV6MplsVpn"])
        )

    @property
    def CapabilityIpV6Multicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Multicast Capability: AFI=2,SAFI=2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV6Multicast"])
        )

    @property
    def CapabilityIpV6MulticastVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP6 MCAST-VPN: AFI = 2, SAFI = 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV6MulticastVpn"])
        )

    @property
    def CapabilityIpV6Unicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Unicast Capability: AFI=2,SAFI=1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpV6Unicast"])
        )

    @property
    def CapabilityIpv4MplsAddPath(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 MPLS Add Path Capability
        """
        return self._get_attribute(self._SDM_ATT_MAP["CapabilityIpv4MplsAddPath"])

    @CapabilityIpv4MplsAddPath.setter
    def CapabilityIpv4MplsAddPath(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CapabilityIpv4MplsAddPath"], value)

    @property
    def CapabilityIpv4MplsVPNAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Capability check box for IPv4 MPLS VPN Add Path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpv4MplsVPNAddPath"])
        )

    @property
    def CapabilityIpv4UnicastAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Check box for IPv4 Unicast Add Path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpv4UnicastAddPath"])
        )

    @property
    def CapabilityIpv6MplsAddPath(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 MPLS Add Path Capability
        """
        return self._get_attribute(self._SDM_ATT_MAP["CapabilityIpv6MplsAddPath"])

    @CapabilityIpv6MplsAddPath.setter
    def CapabilityIpv6MplsAddPath(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CapabilityIpv6MplsAddPath"], value)

    @property
    def CapabilityIpv6MplsVPNAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Capability check box for IPv6 MPLS VPN Add Path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpv6MplsVPNAddPath"])
        )

    @property
    def CapabilityIpv6UnicastAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Check box for IPv6 Unicast Add Path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityIpv6UnicastAddPath"])
        )

    @property
    def CapabilityLinkStateNonVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link State Non-VPN Capability: AFI=16388,SAFI=71
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityLinkStateNonVpn"])
        )

    @property
    def CapabilityLinkStateVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to enable Link State VPN capability on the router.AFI=16388 and SAFI=72 values will be supported.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityLinkStateVpn"])
        )

    @property
    def CapabilityRouteConstraint(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Constraint Capability: AFI=1,SAFI=132
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityRouteConstraint"])
        )

    @property
    def CapabilityRouteRefresh(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Refresh
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityRouteRefresh"])
        )

    @property
    def CapabilitySRTEPoliciesV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 SR TE Policy Capability: AFI=1,SAFI=73
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitySRTEPoliciesV4"])
        )

    @property
    def CapabilitySRTEPoliciesV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 SR TE Policy Capability: AFI=2,SAFI=73
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitySRTEPoliciesV6"])
        )

    @property
    def CapabilityVpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VPLS Capability: AFI = 25, SAFI = 65
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilityVpls"])
        )

    @property
    def Capabilityipv4UnicastFlowSpec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Unicast Flow Spec Capability: AFI=1,SAFI=133
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Capabilityipv4UnicastFlowSpec"]),
        )

    @property
    def Capabilityipv6UnicastFlowSpec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Unicast Flow Spec Capability: AFI=2,SAFI=133
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Capabilityipv6UnicastFlowSpec"]),
        )

    @property
    def ConfigureKeepaliveTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Keepalive Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureKeepaliveTimer"])
        )

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def CustomSidType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): moved to port data in bgp/srv6 Custom SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CustomSidType"]))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DiscardIxiaGeneratedRoutes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard Ixia Generated Routes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DiscardIxiaGeneratedRoutes"])
        )

    @property
    def DowntimeInSec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Downtime in Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DowntimeInSec"]))

    @property
    def DutIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DUT IP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DutIp"]))

    @property
    def Enable4ByteAs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable 4-Byte AS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Enable4ByteAs"]))

    @property
    def EnableBfdRegistration(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BFD Registration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableBfdRegistration"])
        )

    @property
    def EnableBgpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BGP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBgpId"]))

    @property
    def EnableBgpIdSameasRouterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP ID Same as Router ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableBgpIdSameasRouterId"])
        )

    @property
    def EnableBgpLsCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableBgpLsCommunity"])
        )

    @property
    def EnableEpeTraffic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable EPE Traffic
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEpeTraffic"])

    @EnableEpeTraffic.setter
    def EnableEpeTraffic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEpeTraffic"], value)

    @property
    def EnableGracefulRestart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Graceful Restart
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableGracefulRestart"])
        )

    @property
    def EnableLlgr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable LLGR
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableLlgr"]))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def EthernetSegmentsCountV4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Ethernet Segments
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSegmentsCountV4"])

    @EthernetSegmentsCountV4.setter
    def EthernetSegmentsCountV4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetSegmentsCountV4"], value)

    @property
    def Evpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVPN Capability: AFI = 25, SAFI = 70
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Evpn"]))

    @property
    def FilterEvpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Check box for EVPN filter
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FilterEvpn"]))

    @property
    def FilterIpV4Mpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv4 MPLS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV4Mpls"])
        )

    @property
    def FilterIpV4MplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv4 MPLS VPN
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV4MplsVpn"])
        )

    @property
    def FilterIpV4Multicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv4 Multicast
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV4Multicast"])
        )

    @property
    def FilterIpV4MulticastVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv4 Multicast VPN
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV4MulticastVpn"])
        )

    @property
    def FilterIpV4Unicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv4 Unicast
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV4Unicast"])
        )

    @property
    def FilterIpV6Mpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv6 MPLS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV6Mpls"])
        )

    @property
    def FilterIpV6MplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv6 MPLS VPN
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV6MplsVpn"])
        )

    @property
    def FilterIpV6Multicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv6 Multicast
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV6Multicast"])
        )

    @property
    def FilterIpV6MulticastVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv6 Multicast VPN
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV6MulticastVpn"])
        )

    @property
    def FilterIpV6Unicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv6 Unicast
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpV6Unicast"])
        )

    @property
    def FilterIpv4MulticastBgpMplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Check box for IPv4 Multicast BGP/MPLS VPN filter
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FilterIpv4MulticastBgpMplsVpn"]),
        )

    @property
    def FilterIpv4UnicastFlowSpec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv4 Unicast Flow Spec
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpv4UnicastFlowSpec"])
        )

    @property
    def FilterIpv6MulticastBgpMplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Check box for IPv6 Multicast BGP/MPLS VPN filter
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FilterIpv6MulticastBgpMplsVpn"]),
        )

    @property
    def FilterIpv6UnicastFlowSpec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter IPv6 Unicast Flow Spec
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterIpv6UnicastFlowSpec"])
        )

    @property
    def FilterLinkState(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter Link State
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterLinkState"])
        )

    @property
    def FilterLinkStateVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to store incoming BGP LS VPN route info.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterLinkStateVpn"])
        )

    @property
    def FilterSRTEPoliciesV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IPv4 SR TE Policy Filter
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterSRTEPoliciesV4"])
        )

    @property
    def FilterSRTEPoliciesV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IPv6 SR TE Policy Filter
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterSRTEPoliciesV6"])
        )

    @property
    def FilterVpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter VPLS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FilterVpls"]))

    @property
    def Flap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flap
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Flap"]))

    @property
    def HoldTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hold Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HoldTimer"]))

    @property
    def IpVrfToIpVrfType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(interfaceLess | interfacefullWithCorefacingIRB | interfacefullWithUnnumberedCorefacingIRB): IP-VRF-to-IP-VRF Model Type
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpVrfToIpVrfType"])

    @IpVrfToIpVrfType.setter
    def IpVrfToIpVrfType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpVrfToIpVrfType"], value)

    @property
    def Ipv4MplsAddPathMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 MPLS Add Path Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4MplsAddPathMode"])
        )

    @property
    def Ipv4MplsCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 MPLS Capability: AFI=1, SAFI=4
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4MplsCapability"])

    @Ipv4MplsCapability.setter
    def Ipv4MplsCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4MplsCapability"], value)

    @property
    def Ipv4MplsVPNAddPathMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 MPLS VPN Add Path Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4MplsVPNAddPathMode"])
        )

    @property
    def Ipv4MulticastBgpMplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP Multicast for BGP/MPLS IP VPN (UMH): AFI = 1, SAFI = 129
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4MulticastBgpMplsVpn"])
        )

    @property
    def Ipv4MultipleMplsLabelsCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["Ipv4MultipleMplsLabelsCapability"]
        )

    @Ipv4MultipleMplsLabelsCapability.setter
    def Ipv4MultipleMplsLabelsCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["Ipv4MultipleMplsLabelsCapability"], value
        )

    @property
    def Ipv4UnicastAddPathMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Unicast Add Path Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4UnicastAddPathMode"])
        )

    @property
    def Ipv6MplsAddPathMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 MPLS Add Path Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6MplsAddPathMode"])
        )

    @property
    def Ipv6MplsCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 MPLS Capability: AFI=2, SAFI=4
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6MplsCapability"])

    @Ipv6MplsCapability.setter
    def Ipv6MplsCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6MplsCapability"], value)

    @property
    def Ipv6MplsVPNAddPathMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 MPLS VPN Add Path Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6MplsVPNAddPathMode"])
        )

    @property
    def Ipv6MulticastBgpMplsVpn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP6 Multicast for BGP/MPLS IP VPN (UMH): AFI = 2, SAFI = 129
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6MulticastBgpMplsVpn"])
        )

    @property
    def Ipv6MultipleMplsLabelsCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["Ipv6MultipleMplsLabelsCapability"]
        )

    @Ipv6MultipleMplsLabelsCapability.setter
    def Ipv6MultipleMplsLabelsCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["Ipv6MultipleMplsLabelsCapability"], value
        )

    @property
    def Ipv6UnicastAddPathMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Unicast Add Path Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6UnicastAddPathMode"])
        )

    @property
    def IrbInterfaceLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label to be used for Route Type 2 carrying IRB MAC and/or IRB IP in Route Type 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IrbInterfaceLabel"])
        )

    @property
    def IrbIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IRB IPv4 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IrbIpv4Address"])
        )

    @property
    def IxiaSignatureSuffix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is ixia signature suffix to be added with routes. Supported Values: 0 to 65535. Keep empty if suffix is not required.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IxiaSignatureSuffix"])
        )

    @property
    def KeepaliveTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Keepalive Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeepaliveTimer"])
        )

    @property
    def L3VPNEncapsulationType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN Traffic Encapsulation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3VPNEncapsulationType"])
        )

    @property
    def LocalAs2Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local AS# (2-Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocalAs2Bytes"]))

    @property
    def LocalAs4Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local AS# (4-Bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocalAs4Bytes"]))

    @property
    def LocalIpv4Ver2(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIpv4Ver2"])

    @property
    def LocalRouterID(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalRouterID"])

    @property
    def MaxBGPMsgLengthTx(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max BGP Message Length (in bytes): The maximum size of a BGP message that can be transmitted. The minimum value is 4096 and the maximum size can be configured up to 65535. 4096 is the default value. This is not applicable for OPEN and KEEPALIVE messages as their maximum size limit is 4096.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxBGPMsgLengthTx"])
        )

    @property
    def Md5Key(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MD5 Key
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Md5Key"]))

    @property
    def ModeOfBfdOperations(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mode of BFD Operations
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ModeOfBfdOperations"])
        )

    @property
    def MplsLabelsCountForIpv4MplsRoute(self):
        # type: () -> int
        """
        Returns
        -------
        - number: MPLS Labels Count For IPv4 MPLS Route
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabelsCountForIpv4MplsRoute"])

    @MplsLabelsCountForIpv4MplsRoute.setter
    def MplsLabelsCountForIpv4MplsRoute(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsLabelsCountForIpv4MplsRoute"], value)

    @property
    def MplsLabelsCountForIpv6MplsRoute(self):
        # type: () -> int
        """
        Returns
        -------
        - number: MPLS Labels Count For IPv6 MPLS Route
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabelsCountForIpv6MplsRoute"])

    @MplsLabelsCountForIpv6MplsRoute.setter
    def MplsLabelsCountForIpv6MplsRoute(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsLabelsCountForIpv6MplsRoute"], value)

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NoOfEpePeers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of EPE Peers
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfEpePeers"])

    @NoOfEpePeers.setter
    def NoOfEpePeers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfEpePeers"], value)

    @property
    def NoOfExtendedCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfExtendedCommunities"])

    @NoOfExtendedCommunities.setter
    def NoOfExtendedCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfExtendedCommunities"], value)

    @property
    def NoOfUserDefinedAfiSafi(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of User Defined AFI SAFI
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfUserDefinedAfiSafi"])

    @NoOfUserDefinedAfiSafi.setter
    def NoOfUserDefinedAfiSafi(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfUserDefinedAfiSafi"], value)

    @property
    def NumBgpLsId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP LS Instance ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NumBgpLsId"]))

    @property
    def NumBgpLsInstanceIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IGP Multi instance unique identifier. 0 is default single-instance IGP. (e.g. for OSPFv3 it is possible to separately run 4 instances of OSPFv3 with peer, one advertising v4 only, another v6 only and other 2 mcast v4 and v6 respectively) .
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NumBgpLsInstanceIdentifier"])
        )

    @property
    def NumBgpUpdatesGeneratedPerIteration(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Num BGP Updates Generated Per Iteration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NumBgpUpdatesGeneratedPerIteration"]
            ),
        )

    @property
    def NumberColorFlexAlgoMapping(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Color/Flex Algo Mapping Entries
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberColorFlexAlgoMapping"])

    @NumberColorFlexAlgoMapping.setter
    def NumberColorFlexAlgoMapping(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberColorFlexAlgoMapping"], value)

    @property
    def NumberFlowSpecRangeV4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of IPv4 Flow Spec Ranges
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberFlowSpecRangeV4"])

    @NumberFlowSpecRangeV4.setter
    def NumberFlowSpecRangeV4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberFlowSpecRangeV4"], value)

    @property
    def NumberFlowSpecRangeV6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of IPv6 Flow Spec Ranges
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberFlowSpecRangeV6"])

    @NumberFlowSpecRangeV6.setter
    def NumberFlowSpecRangeV6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberFlowSpecRangeV6"], value)

    @property
    def NumberSRTEPolicies(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of SR TE Policies
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberSRTEPolicies"])

    @NumberSRTEPolicies.setter
    def NumberSRTEPolicies(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberSRTEPolicies"], value)

    @property
    def OperationalModel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Operational Model
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OperationalModel"])
        )

    @property
    def RestartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Time
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RestartTime"]))

    @property
    def RoutersMacOrIrbMacAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router's MAC/IRB MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutersMacOrIrbMacAddress"])
        )

    @property
    def SRGBRangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SRGB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SRGBRangeCount"])

    @SRGBRangeCount.setter
    def SRGBRangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SRGBRangeCount"], value)

    @property
    def SendIxiaSignatureWithRoutes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send Ixia Signature With Routes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendIxiaSignatureWithRoutes"])
        )

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[aSRoutingLoopErrorRx | attributeFlagErrorRx | attributesLengthErrorRx | authenticationFailureErrorRx | badBGPIdentifierErrorRx | badMessageLengthErrorRx | badMessageTypeErrorRx | badPeerASErrorRx | bGPHeaderErrorRx | bGPHeaderErrorTx | bGPHoldTimerExpiredErrorRx | bGPOpenPacketErrorRx | bGPStateMachineErrorRx | bGPUpdatePacketErrorRx | ceaseErrorRx | ceaseNotificationErrorTx | connectionNotsynchronizedErrorRx | holdtimeExpiredErrorTx | invalidASPathErrorRx | invalidNetworkFieldErrorRx | invalidNextHopAttributeErrorRx | invalidOriginAttributeErrorRx | malformedAttributeListErrorRx | missingWellKnownAttributeErrorRx | none | openPacketErrTx | optionalAttributeErrorRx | stateMachineErrorTx | unacceptableHoldTimeErrorRx | unrecognizedWellKnownAttributeErrorRx | unspecifiedErrorRx | unspecifiedErrorTx | unspecifiedSubcodeErrorRx | unsupportedOptionalParameterErrorRx | unsupportedversionNumberErrorRx | updatePacketErrorTx]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionInfo"])

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StaleTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Stale Time/ LLGR Stale Time
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StaleTime"]))

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def TcpWindowSizeInBytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TCP Window Size (in bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpWindowSizeInBytes"])
        )

    @property
    def Ttl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ttl"]))

    @property
    def Type(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def UdpPortEndValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: UDP Port End Value
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpPortEndValue"])

    @UdpPortEndValue.setter
    def UdpPortEndValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpPortEndValue"], value)

    @property
    def UdpPortStartValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: UDP Port Start Value
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpPortStartValue"])

    @UdpPortStartValue.setter
    def UdpPortStartValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpPortStartValue"], value)

    @property
    def UpdateInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Update Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UpdateInterval"])
        )

    @property
    def UptimeInSec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Uptime in Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UptimeInSec"]))

    @property
    def VplsEnableNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VPLS Enable Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VplsEnableNextHop"])
        )

    @property
    def VplsNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VPLS Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VplsNextHop"]))

    def update(
        self,
        AdvertiseEvpnRoutesForOtherVtep=None,
        BgpLsNoOfASPathSegments=None,
        BgpLsNoOfClusters=None,
        BgpLsNoOfCommunities=None,
        CapabilityIpv4MplsAddPath=None,
        CapabilityIpv6MplsAddPath=None,
        ConnectedVia=None,
        EnableEpeTraffic=None,
        EthernetSegmentsCountV4=None,
        IpVrfToIpVrfType=None,
        Ipv4MplsCapability=None,
        Ipv4MultipleMplsLabelsCapability=None,
        Ipv6MplsCapability=None,
        Ipv6MultipleMplsLabelsCapability=None,
        MplsLabelsCountForIpv4MplsRoute=None,
        MplsLabelsCountForIpv6MplsRoute=None,
        Multiplier=None,
        Name=None,
        NoOfEpePeers=None,
        NoOfExtendedCommunities=None,
        NoOfUserDefinedAfiSafi=None,
        NumberColorFlexAlgoMapping=None,
        NumberFlowSpecRangeV4=None,
        NumberFlowSpecRangeV6=None,
        NumberSRTEPolicies=None,
        SRGBRangeCount=None,
        StackedLayers=None,
        UdpPortEndValue=None,
        UdpPortStartValue=None,
    ):
        # type: (bool, int, int, int, bool, bool, List[str], bool, int, str, bool, bool, bool, bool, int, int, int, str, int, int, int, int, int, int, int, int, List[str], int, int) -> BgpIpv4Peer
        """Updates bgpIpv4Peer resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AdvertiseEvpnRoutesForOtherVtep (bool): Advertise EVPN routes for other VTEPS
        - BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
        - BgpLsNoOfClusters (number): Number of Clusters
        - BgpLsNoOfCommunities (number): Number of Communities
        - CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
        - CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableEpeTraffic (bool): Enable EPE Traffic
        - EthernetSegmentsCountV4 (number): Number of Ethernet Segments
        - IpVrfToIpVrfType (str(interfaceLess | interfacefullWithCorefacingIRB | interfacefullWithUnnumberedCorefacingIRB)): IP-VRF-to-IP-VRF Model Type
        - Ipv4MplsCapability (bool): IPv4 MPLS Capability: AFI=1, SAFI=4
        - Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
        - Ipv6MplsCapability (bool): IPv6 MPLS Capability: AFI=2, SAFI=4
        - Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
        - MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
        - MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfEpePeers (number): Number of EPE Peers
        - NoOfExtendedCommunities (number): Number of Extended Communities
        - NoOfUserDefinedAfiSafi (number): Count of User Defined AFI SAFI
        - NumberColorFlexAlgoMapping (number): Number of Color/Flex Algo Mapping Entries
        - NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
        - NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
        - NumberSRTEPolicies (number): Count of SR TE Policies
        - SRGBRangeCount (number): SRGB Range Count
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - UdpPortEndValue (number): UDP Port End Value
        - UdpPortStartValue (number): UDP Port Start Value

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdvertiseEvpnRoutesForOtherVtep=None,
        BgpLsNoOfASPathSegments=None,
        BgpLsNoOfClusters=None,
        BgpLsNoOfCommunities=None,
        CapabilityIpv4MplsAddPath=None,
        CapabilityIpv6MplsAddPath=None,
        ConnectedVia=None,
        EnableEpeTraffic=None,
        EthernetSegmentsCountV4=None,
        IpVrfToIpVrfType=None,
        Ipv4MplsCapability=None,
        Ipv4MultipleMplsLabelsCapability=None,
        Ipv6MplsCapability=None,
        Ipv6MultipleMplsLabelsCapability=None,
        MplsLabelsCountForIpv4MplsRoute=None,
        MplsLabelsCountForIpv6MplsRoute=None,
        Multiplier=None,
        Name=None,
        NoOfEpePeers=None,
        NoOfExtendedCommunities=None,
        NoOfUserDefinedAfiSafi=None,
        NumberColorFlexAlgoMapping=None,
        NumberFlowSpecRangeV4=None,
        NumberFlowSpecRangeV6=None,
        NumberSRTEPolicies=None,
        SRGBRangeCount=None,
        StackedLayers=None,
        UdpPortEndValue=None,
        UdpPortStartValue=None,
    ):
        # type: (bool, int, int, int, bool, bool, List[str], bool, int, str, bool, bool, bool, bool, int, int, int, str, int, int, int, int, int, int, int, int, List[str], int, int) -> BgpIpv4Peer
        """Adds a new bgpIpv4Peer resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseEvpnRoutesForOtherVtep (bool): Advertise EVPN routes for other VTEPS
        - BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
        - BgpLsNoOfClusters (number): Number of Clusters
        - BgpLsNoOfCommunities (number): Number of Communities
        - CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
        - CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableEpeTraffic (bool): Enable EPE Traffic
        - EthernetSegmentsCountV4 (number): Number of Ethernet Segments
        - IpVrfToIpVrfType (str(interfaceLess | interfacefullWithCorefacingIRB | interfacefullWithUnnumberedCorefacingIRB)): IP-VRF-to-IP-VRF Model Type
        - Ipv4MplsCapability (bool): IPv4 MPLS Capability: AFI=1, SAFI=4
        - Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
        - Ipv6MplsCapability (bool): IPv6 MPLS Capability: AFI=2, SAFI=4
        - Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
        - MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
        - MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfEpePeers (number): Number of EPE Peers
        - NoOfExtendedCommunities (number): Number of Extended Communities
        - NoOfUserDefinedAfiSafi (number): Count of User Defined AFI SAFI
        - NumberColorFlexAlgoMapping (number): Number of Color/Flex Algo Mapping Entries
        - NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
        - NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
        - NumberSRTEPolicies (number): Count of SR TE Policies
        - SRGBRangeCount (number): SRGB Range Count
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - UdpPortEndValue (number): UDP Port End Value
        - UdpPortStartValue (number): UDP Port Start Value

        Returns
        -------
        - self: This instance with all currently retrieved bgpIpv4Peer resources using find and the newly added bgpIpv4Peer resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpIpv4Peer resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AdvertiseEvpnRoutesForOtherVtep=None,
        BgpFsmState=None,
        BgpLsNoOfASPathSegments=None,
        BgpLsNoOfClusters=None,
        BgpLsNoOfCommunities=None,
        CapabilityIpv4MplsAddPath=None,
        CapabilityIpv6MplsAddPath=None,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        EnableEpeTraffic=None,
        Errors=None,
        EthernetSegmentsCountV4=None,
        IpVrfToIpVrfType=None,
        Ipv4MplsCapability=None,
        Ipv4MultipleMplsLabelsCapability=None,
        Ipv6MplsCapability=None,
        Ipv6MultipleMplsLabelsCapability=None,
        LocalIpv4Ver2=None,
        LocalRouterID=None,
        MplsLabelsCountForIpv4MplsRoute=None,
        MplsLabelsCountForIpv6MplsRoute=None,
        Multiplier=None,
        Name=None,
        NoOfEpePeers=None,
        NoOfExtendedCommunities=None,
        NoOfUserDefinedAfiSafi=None,
        NumberColorFlexAlgoMapping=None,
        NumberFlowSpecRangeV4=None,
        NumberFlowSpecRangeV6=None,
        NumberSRTEPolicies=None,
        SRGBRangeCount=None,
        SessionInfo=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        UdpPortEndValue=None,
        UdpPortStartValue=None,
    ):
        """Finds and retrieves bgpIpv4Peer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpIpv4Peer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpIpv4Peer resources from the server.

        Args
        ----
        - AdvertiseEvpnRoutesForOtherVtep (bool): Advertise EVPN routes for other VTEPS
        - BgpFsmState (list(str[active | connect | error | established | idle | none | openConfirm | openSent])): Logs additional information about the BGP Peer State
        - BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
        - BgpLsNoOfClusters (number): Number of Clusters
        - BgpLsNoOfCommunities (number): Number of Communities
        - CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
        - CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableEpeTraffic (bool): Enable EPE Traffic
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - EthernetSegmentsCountV4 (number): Number of Ethernet Segments
        - IpVrfToIpVrfType (str(interfaceLess | interfacefullWithCorefacingIRB | interfacefullWithUnnumberedCorefacingIRB)): IP-VRF-to-IP-VRF Model Type
        - Ipv4MplsCapability (bool): IPv4 MPLS Capability: AFI=1, SAFI=4
        - Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
        - Ipv6MplsCapability (bool): IPv6 MPLS Capability: AFI=2, SAFI=4
        - Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
        - LocalIpv4Ver2 (list(str)): Local IP
        - LocalRouterID (list(str)): Router ID
        - MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
        - MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfEpePeers (number): Number of EPE Peers
        - NoOfExtendedCommunities (number): Number of Extended Communities
        - NoOfUserDefinedAfiSafi (number): Count of User Defined AFI SAFI
        - NumberColorFlexAlgoMapping (number): Number of Color/Flex Algo Mapping Entries
        - NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
        - NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
        - NumberSRTEPolicies (number): Count of SR TE Policies
        - SRGBRangeCount (number): SRGB Range Count
        - SessionInfo (list(str[aSRoutingLoopErrorRx | attributeFlagErrorRx | attributesLengthErrorRx | authenticationFailureErrorRx | badBGPIdentifierErrorRx | badMessageLengthErrorRx | badMessageTypeErrorRx | badPeerASErrorRx | bGPHeaderErrorRx | bGPHeaderErrorTx | bGPHoldTimerExpiredErrorRx | bGPOpenPacketErrorRx | bGPStateMachineErrorRx | bGPUpdatePacketErrorRx | ceaseErrorRx | ceaseNotificationErrorTx | connectionNotsynchronizedErrorRx | holdtimeExpiredErrorTx | invalidASPathErrorRx | invalidNetworkFieldErrorRx | invalidNextHopAttributeErrorRx | invalidOriginAttributeErrorRx | malformedAttributeListErrorRx | missingWellKnownAttributeErrorRx | none | openPacketErrTx | optionalAttributeErrorRx | stateMachineErrorTx | unacceptableHoldTimeErrorRx | unrecognizedWellKnownAttributeErrorRx | unspecifiedErrorRx | unspecifiedErrorTx | unspecifiedSubcodeErrorRx | unsupportedOptionalParameterErrorRx | unsupportedversionNumberErrorRx | updatePacketErrorTx])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - UdpPortEndValue (number): UDP Port End Value
        - UdpPortStartValue (number): UDP Port Start Value

        Returns
        -------
        - self: This instance with matching bgpIpv4Peer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpIpv4Peer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpIpv4Peer resources from the server available through an iterator or index

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def BgpIPv4FlowSpecLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the bgpIPv4FlowSpecLearnedInfo operation on the server.

        Get IPv4 FlowSpec Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        bgpIPv4FlowSpecLearnedInfo(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        bgpIPv4FlowSpecLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        bgpIPv4FlowSpecLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "bgpIPv4FlowSpecLearnedInfo", payload=payload, response_object=None
        )

    def BgpIPv6FlowSpecLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the bgpIPv6FlowSpecLearnedInfo operation on the server.

        Get IPv6 FlowSpec Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        bgpIPv6FlowSpecLearnedInfo(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        bgpIPv6FlowSpecLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        bgpIPv6FlowSpecLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "bgpIPv6FlowSpecLearnedInfo", payload=payload, response_object=None
        )

    def BreakTCPSession(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the breakTCPSession operation on the server.

        Break TCP Session

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        breakTCPSession(Notification_code=number, Notification_sub_code=number, async_operation=bool)
        ---------------------------------------------------------------------------------------------
        - Notification_code (number): This parameter requires a notification_code of type kInteger
        - Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        breakTCPSession(Notification_code=number, Notification_sub_code=number, SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------------------------------------------
        - Notification_code (number): This parameter requires a notification_code of type kInteger
        - Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        breakTCPSession(SessionIndices=string, Notification_code=number, Notification_sub_code=number, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a notification_code of type kInteger
        - Notification_code (number): This parameter requires a notification_sub_code of type kInteger
        - Notification_sub_code (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("breakTCPSession", payload=payload, response_object=None)

    def Breaktcpsession(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the breaktcpsession operation on the server.

        Break BGP Peer Range TCP Session.

        breaktcpsession(Arg2=list, Arg3=number, Arg4=number, async_operation=bool)list
        ------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Notification Code
        - Arg4 (number): Notification Sub Code
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("breaktcpsession", payload=payload, response_object=None)

    def ClearAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedInfo(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAllLearnedInfo", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAllLearnedInfoInClient", payload=payload, response_object=None
        )

    def GetADVPLSLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getADVPLSLearnedInfo operation on the server.

        Get ADVPLS Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getADVPLSLearnedInfo(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getADVPLSLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getADVPLSLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getADVPLSLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getADVPLSLearnedInfo", payload=payload, response_object=None
        )

    def GetAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getAllLearnedInfo operation on the server.

        Get All Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getAllLearnedInfo(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAllLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAllLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("getAllLearnedInfo", payload=payload, response_object=None)

    def GetbgpIpv4FlowSpecLearnedInfoLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getbgpIpv4FlowSpecLearnedInfoLearnedInfo operation on the server.

        getbgpIpv4FlowSpecLearnedInfoLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getbgpIpv4FlowSpecLearnedInfoLearnedInfo",
            payload=payload,
            response_object=None,
        )

    def GetbgpIpv6FlowSpecLearnedInfoLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getbgpIpv6FlowSpecLearnedInfoLearnedInfo operation on the server.

        getbgpIpv6FlowSpecLearnedInfoLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getbgpIpv6FlowSpecLearnedInfoLearnedInfo",
            payload=payload,
            response_object=None,
        )

    def GetbgpSrTeLearnedInfoLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getbgpSrTeLearnedInfoLearnedInfo operation on the server.

        getbgpSrTeLearnedInfoLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getbgpSrTeLearnedInfoLearnedInfo", payload=payload, response_object=None
        )

    def GetbgpTracerouteLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getbgpTracerouteLearnedInfo operation on the server.

        Get Traceroute Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getbgpTracerouteLearnedInfo(async_operation=bool)
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getbgpTracerouteLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getbgpTracerouteLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getbgpTracerouteLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getbgpTracerouteLearnedInfo", payload=payload, response_object=None
        )

    def GetEVPNLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getEVPNLearnedInfo operation on the server.

        Get EVPN Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getEVPNLearnedInfo(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getEVPNLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getEVPNLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getEVPNLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getEVPNLearnedInfo", payload=payload, response_object=None
        )

    def GetIPv4LearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv4LearnedInfo operation on the server.

        Get IPv4 Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv4LearnedInfo(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4LearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4LearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4LearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIPv4LearnedInfo", payload=payload, response_object=None
        )

    def GetIPv4MplsLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv4MplsLearnedInfo operation on the server.

        Fetches IPv4 MPLS routes learnt by this BGP peer.

        getIPv4MplsLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIPv4MplsLearnedInfo", payload=payload, response_object=None
        )

    def GetIpv4MvpnLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIpv4MvpnLearnedInfo operation on the server.

        Fetches MVPN MAC IP routes learnt by this BGP peer.

        getIpv4MvpnLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIpv4MvpnLearnedInfo", payload=payload, response_object=None
        )

    def GetIpv4UmhRoutesLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIpv4UmhRoutesLearnedInfo operation on the server.

        Fetches Umh Routes learned by this BGP peer.

        getIpv4UmhRoutesLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIpv4UmhRoutesLearnedInfo", payload=payload, response_object=None
        )

    def GetIPv4VpnLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv4VpnLearnedInfo operation on the server.

        Get IPv4 Vpn Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv4VpnLearnedInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4VpnLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4VpnLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4VpnLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIPv4VpnLearnedInfo", payload=payload, response_object=None
        )

    def GetIPv6LearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv6LearnedInfo operation on the server.

        Get IPv6 Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv6LearnedInfo(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6LearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6LearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6LearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIPv6LearnedInfo", payload=payload, response_object=None
        )

    def GetIPv6MplsLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv6MplsLearnedInfo operation on the server.

        Gets IPv6 Mpls routes learnt by this BGP peer.

        getIPv6MplsLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIPv6MplsLearnedInfo", payload=payload, response_object=None
        )

    def GetIpv6MvpnLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIpv6MvpnLearnedInfo operation on the server.

        Fetches MVPN MAC IP routes learnt by this BGP peer.

        getIpv6MvpnLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIpv6MvpnLearnedInfo", payload=payload, response_object=None
        )

    def GetIpv6UmhRoutesLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIpv6UmhRoutesLearnedInfo operation on the server.

        Fetches Umh Route learned by this BGP peer.

        getIpv6UmhRoutesLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIpv6UmhRoutesLearnedInfo", payload=payload, response_object=None
        )

    def GetIPv6VpnLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv6VpnLearnedInfo operation on the server.

        Get IPv6 Vpn Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv6VpnLearnedInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6VpnLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6VpnLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6VpnLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getIPv6VpnLearnedInfo", payload=payload, response_object=None
        )

    def GetLinkStateLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getLinkStateLearnedInfo operation on the server.

        Get Link State Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLinkStateLearnedInfo(async_operation=bool)
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLinkStateLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLinkStateLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLinkStateLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getLinkStateLearnedInfo", payload=payload, response_object=None
        )

    def GetLinkStateVPNLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getLinkStateVPNLearnedInfo operation on the server.

        Get Link State VPN Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLinkStateVPNLearnedInfo(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLinkStateVPNLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLinkStateVPNLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLinkStateVPNLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getLinkStateVPNLearnedInfo", payload=payload, response_object=None
        )

    def GetVPLSLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getVPLSLearnedInfo operation on the server.

        Get VPLS Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getVPLSLearnedInfo(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getVPLSLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getVPLSLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getVPLSLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getVPLSLearnedInfo", payload=payload, response_object=None
        )

    def GracefulRestart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the gracefulRestart operation on the server.

        Graceful restart Peers on selected Peer Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gracefulRestart(Restart_time=number, async_operation=bool)
        ----------------------------------------------------------
        - Restart_time (number): This parameter requires a restart_time of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        gracefulRestart(Restart_time=number, SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------
        - Restart_time (number): This parameter requires a restart_time of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        gracefulRestart(SessionIndices=string, Restart_time=number, async_operation=bool)
        ---------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a restart_time of type kInteger
        - Restart_time (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("gracefulRestart", payload=payload, response_object=None)

    def Gracefulrestart(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the gracefulrestart operation on the server.

        Graceful restart Peers on selected Peer Ranges.

        gracefulrestart(Arg2=list, Arg3=number, async_operation=bool)list
        -----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Arg3 (number): Restart After Time(in secs).
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("gracefulrestart", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("restartDown", payload=payload, response_object=None)

    def ResumeKeepAlive(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the resumeKeepAlive operation on the server.

        Resume sending KeepAlive

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeKeepAlive(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeKeepAlive(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeKeepAlive(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("resumeKeepAlive", payload=payload, response_object=None)

    def Resumekeepalive(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumekeepalive operation on the server.

        Start Sending Keep Alive Messages.

        resumekeepalive(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("resumekeepalive", payload=payload, response_object=None)

    def ResumeTCPSession(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the resumeTCPSession operation on the server.

        Resume TCP Session

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeTCPSession(Notification_code=number, Notification_sub_code=number, async_operation=bool)
        ----------------------------------------------------------------------------------------------
        - Notification_code (number): This parameter requires a notification_code of type kInteger
        - Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeTCPSession(Notification_code=number, Notification_sub_code=number, SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------------------------------------------
        - Notification_code (number): This parameter requires a notification_code of type kInteger
        - Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeTCPSession(SessionIndices=string, Notification_code=number, Notification_sub_code=number, async_operation=bool)
        ---------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a notification_code of type kInteger
        - Notification_code (number): This parameter requires a notification_sub_code of type kInteger
        - Notification_sub_code (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("resumeTCPSession", payload=payload, response_object=None)

    def Resumetcpsession(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumetcpsession operation on the server.

        Resume BGP Peer Range TCP Session.

        resumetcpsession(Arg2=list, Arg3=number, Arg4=number, async_operation=bool)list
        -------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Notification Code
        - Arg4 (number): Notification Sub Code
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("resumetcpsession", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def StopKeepAlive(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopKeepAlive operation on the server.

        Stop sending KeepAlive

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopKeepAlive(async_operation=bool)
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopKeepAlive(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopKeepAlive(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopKeepAlive", payload=payload, response_object=None)

    def Stopkeepalive(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopkeepalive operation on the server.

        Stop Sending Keep Alive Messages.

        stopkeepalive(Arg2=list, async_operation=bool)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopkeepalive", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        ActAsRestarted=None,
        Active=None,
        AdvertiseEndOfRib=None,
        AdvertiseTunnelEncapsulationExtendedCommunity=None,
        AllowIxiaSignatureSuffix=None,
        AlwaysIncludeTunnelEncExtCommunity=None,
        AsSetMode=None,
        Authentication=None,
        BgpId=None,
        BgpLsAsSetMode=None,
        BgpLsEnableAsPathSegments=None,
        BgpLsEnableCluster=None,
        BgpLsEnableExtendedCommunity=None,
        BgpLsOverridePeerAsSetMode=None,
        CapabilityExtendedMessage=None,
        CapabilityIpV4Mdt=None,
        CapabilityIpV4Mpls=None,
        CapabilityIpV4MplsVpn=None,
        CapabilityIpV4Multicast=None,
        CapabilityIpV4MulticastVpn=None,
        CapabilityIpV4Unicast=None,
        CapabilityIpV6Mpls=None,
        CapabilityIpV6MplsVpn=None,
        CapabilityIpV6Multicast=None,
        CapabilityIpV6MulticastVpn=None,
        CapabilityIpV6Unicast=None,
        CapabilityIpv4MplsVPNAddPath=None,
        CapabilityIpv4UnicastAddPath=None,
        CapabilityIpv6MplsVPNAddPath=None,
        CapabilityIpv6UnicastAddPath=None,
        CapabilityLinkStateNonVpn=None,
        CapabilityLinkStateVpn=None,
        CapabilityRouteConstraint=None,
        CapabilityRouteRefresh=None,
        CapabilitySRTEPoliciesV4=None,
        CapabilitySRTEPoliciesV6=None,
        CapabilityVpls=None,
        Capabilityipv4UnicastFlowSpec=None,
        Capabilityipv6UnicastFlowSpec=None,
        ConfigureKeepaliveTimer=None,
        CustomSidType=None,
        DiscardIxiaGeneratedRoutes=None,
        DowntimeInSec=None,
        DutIp=None,
        Enable4ByteAs=None,
        EnableBfdRegistration=None,
        EnableBgpId=None,
        EnableBgpIdSameasRouterId=None,
        EnableBgpLsCommunity=None,
        EnableGracefulRestart=None,
        EnableLlgr=None,
        Evpn=None,
        FilterEvpn=None,
        FilterIpV4Mpls=None,
        FilterIpV4MplsVpn=None,
        FilterIpV4Multicast=None,
        FilterIpV4MulticastVpn=None,
        FilterIpV4Unicast=None,
        FilterIpV6Mpls=None,
        FilterIpV6MplsVpn=None,
        FilterIpV6Multicast=None,
        FilterIpV6MulticastVpn=None,
        FilterIpV6Unicast=None,
        FilterIpv4MulticastBgpMplsVpn=None,
        FilterIpv4UnicastFlowSpec=None,
        FilterIpv6MulticastBgpMplsVpn=None,
        FilterIpv6UnicastFlowSpec=None,
        FilterLinkState=None,
        FilterLinkStateVpn=None,
        FilterSRTEPoliciesV4=None,
        FilterSRTEPoliciesV6=None,
        FilterVpls=None,
        Flap=None,
        HoldTimer=None,
        Ipv4MplsAddPathMode=None,
        Ipv4MplsVPNAddPathMode=None,
        Ipv4MulticastBgpMplsVpn=None,
        Ipv4UnicastAddPathMode=None,
        Ipv6MplsAddPathMode=None,
        Ipv6MplsVPNAddPathMode=None,
        Ipv6MulticastBgpMplsVpn=None,
        Ipv6UnicastAddPathMode=None,
        IrbInterfaceLabel=None,
        IrbIpv4Address=None,
        IxiaSignatureSuffix=None,
        KeepaliveTimer=None,
        L3VPNEncapsulationType=None,
        LocalAs2Bytes=None,
        LocalAs4Bytes=None,
        MaxBGPMsgLengthTx=None,
        Md5Key=None,
        ModeOfBfdOperations=None,
        NumBgpLsId=None,
        NumBgpLsInstanceIdentifier=None,
        NumBgpUpdatesGeneratedPerIteration=None,
        OperationalModel=None,
        RestartTime=None,
        RoutersMacOrIrbMacAddress=None,
        SendIxiaSignatureWithRoutes=None,
        StaleTime=None,
        TcpWindowSizeInBytes=None,
        Ttl=None,
        Type=None,
        UpdateInterval=None,
        UptimeInSec=None,
        VplsEnableNextHop=None,
        VplsNextHop=None,
    ):
        """Base class infrastructure that gets a list of bgpIpv4Peer device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActAsRestarted (str): optional regex of actAsRestarted
        - Active (str): optional regex of active
        - AdvertiseEndOfRib (str): optional regex of advertiseEndOfRib
        - AdvertiseTunnelEncapsulationExtendedCommunity (str): optional regex of advertiseTunnelEncapsulationExtendedCommunity
        - AllowIxiaSignatureSuffix (str): optional regex of allowIxiaSignatureSuffix
        - AlwaysIncludeTunnelEncExtCommunity (str): optional regex of alwaysIncludeTunnelEncExtCommunity
        - AsSetMode (str): optional regex of asSetMode
        - Authentication (str): optional regex of authentication
        - BgpId (str): optional regex of bgpId
        - BgpLsAsSetMode (str): optional regex of bgpLsAsSetMode
        - BgpLsEnableAsPathSegments (str): optional regex of bgpLsEnableAsPathSegments
        - BgpLsEnableCluster (str): optional regex of bgpLsEnableCluster
        - BgpLsEnableExtendedCommunity (str): optional regex of bgpLsEnableExtendedCommunity
        - BgpLsOverridePeerAsSetMode (str): optional regex of bgpLsOverridePeerAsSetMode
        - CapabilityExtendedMessage (str): optional regex of capabilityExtendedMessage
        - CapabilityIpV4Mdt (str): optional regex of capabilityIpV4Mdt
        - CapabilityIpV4Mpls (str): optional regex of capabilityIpV4Mpls
        - CapabilityIpV4MplsVpn (str): optional regex of capabilityIpV4MplsVpn
        - CapabilityIpV4Multicast (str): optional regex of capabilityIpV4Multicast
        - CapabilityIpV4MulticastVpn (str): optional regex of capabilityIpV4MulticastVpn
        - CapabilityIpV4Unicast (str): optional regex of capabilityIpV4Unicast
        - CapabilityIpV6Mpls (str): optional regex of capabilityIpV6Mpls
        - CapabilityIpV6MplsVpn (str): optional regex of capabilityIpV6MplsVpn
        - CapabilityIpV6Multicast (str): optional regex of capabilityIpV6Multicast
        - CapabilityIpV6MulticastVpn (str): optional regex of capabilityIpV6MulticastVpn
        - CapabilityIpV6Unicast (str): optional regex of capabilityIpV6Unicast
        - CapabilityIpv4MplsVPNAddPath (str): optional regex of capabilityIpv4MplsVPNAddPath
        - CapabilityIpv4UnicastAddPath (str): optional regex of capabilityIpv4UnicastAddPath
        - CapabilityIpv6MplsVPNAddPath (str): optional regex of capabilityIpv6MplsVPNAddPath
        - CapabilityIpv6UnicastAddPath (str): optional regex of capabilityIpv6UnicastAddPath
        - CapabilityLinkStateNonVpn (str): optional regex of capabilityLinkStateNonVpn
        - CapabilityLinkStateVpn (str): optional regex of capabilityLinkStateVpn
        - CapabilityRouteConstraint (str): optional regex of capabilityRouteConstraint
        - CapabilityRouteRefresh (str): optional regex of capabilityRouteRefresh
        - CapabilitySRTEPoliciesV4 (str): optional regex of capabilitySRTEPoliciesV4
        - CapabilitySRTEPoliciesV6 (str): optional regex of capabilitySRTEPoliciesV6
        - CapabilityVpls (str): optional regex of capabilityVpls
        - Capabilityipv4UnicastFlowSpec (str): optional regex of capabilityipv4UnicastFlowSpec
        - Capabilityipv6UnicastFlowSpec (str): optional regex of capabilityipv6UnicastFlowSpec
        - ConfigureKeepaliveTimer (str): optional regex of configureKeepaliveTimer
        - CustomSidType (str): optional regex of customSidType
        - DiscardIxiaGeneratedRoutes (str): optional regex of discardIxiaGeneratedRoutes
        - DowntimeInSec (str): optional regex of downtimeInSec
        - DutIp (str): optional regex of dutIp
        - Enable4ByteAs (str): optional regex of enable4ByteAs
        - EnableBfdRegistration (str): optional regex of enableBfdRegistration
        - EnableBgpId (str): optional regex of enableBgpId
        - EnableBgpIdSameasRouterId (str): optional regex of enableBgpIdSameasRouterId
        - EnableBgpLsCommunity (str): optional regex of enableBgpLsCommunity
        - EnableGracefulRestart (str): optional regex of enableGracefulRestart
        - EnableLlgr (str): optional regex of enableLlgr
        - Evpn (str): optional regex of evpn
        - FilterEvpn (str): optional regex of filterEvpn
        - FilterIpV4Mpls (str): optional regex of filterIpV4Mpls
        - FilterIpV4MplsVpn (str): optional regex of filterIpV4MplsVpn
        - FilterIpV4Multicast (str): optional regex of filterIpV4Multicast
        - FilterIpV4MulticastVpn (str): optional regex of filterIpV4MulticastVpn
        - FilterIpV4Unicast (str): optional regex of filterIpV4Unicast
        - FilterIpV6Mpls (str): optional regex of filterIpV6Mpls
        - FilterIpV6MplsVpn (str): optional regex of filterIpV6MplsVpn
        - FilterIpV6Multicast (str): optional regex of filterIpV6Multicast
        - FilterIpV6MulticastVpn (str): optional regex of filterIpV6MulticastVpn
        - FilterIpV6Unicast (str): optional regex of filterIpV6Unicast
        - FilterIpv4MulticastBgpMplsVpn (str): optional regex of filterIpv4MulticastBgpMplsVpn
        - FilterIpv4UnicastFlowSpec (str): optional regex of filterIpv4UnicastFlowSpec
        - FilterIpv6MulticastBgpMplsVpn (str): optional regex of filterIpv6MulticastBgpMplsVpn
        - FilterIpv6UnicastFlowSpec (str): optional regex of filterIpv6UnicastFlowSpec
        - FilterLinkState (str): optional regex of filterLinkState
        - FilterLinkStateVpn (str): optional regex of filterLinkStateVpn
        - FilterSRTEPoliciesV4 (str): optional regex of filterSRTEPoliciesV4
        - FilterSRTEPoliciesV6 (str): optional regex of filterSRTEPoliciesV6
        - FilterVpls (str): optional regex of filterVpls
        - Flap (str): optional regex of flap
        - HoldTimer (str): optional regex of holdTimer
        - Ipv4MplsAddPathMode (str): optional regex of ipv4MplsAddPathMode
        - Ipv4MplsVPNAddPathMode (str): optional regex of ipv4MplsVPNAddPathMode
        - Ipv4MulticastBgpMplsVpn (str): optional regex of ipv4MulticastBgpMplsVpn
        - Ipv4UnicastAddPathMode (str): optional regex of ipv4UnicastAddPathMode
        - Ipv6MplsAddPathMode (str): optional regex of ipv6MplsAddPathMode
        - Ipv6MplsVPNAddPathMode (str): optional regex of ipv6MplsVPNAddPathMode
        - Ipv6MulticastBgpMplsVpn (str): optional regex of ipv6MulticastBgpMplsVpn
        - Ipv6UnicastAddPathMode (str): optional regex of ipv6UnicastAddPathMode
        - IrbInterfaceLabel (str): optional regex of irbInterfaceLabel
        - IrbIpv4Address (str): optional regex of irbIpv4Address
        - IxiaSignatureSuffix (str): optional regex of ixiaSignatureSuffix
        - KeepaliveTimer (str): optional regex of keepaliveTimer
        - L3VPNEncapsulationType (str): optional regex of l3VPNEncapsulationType
        - LocalAs2Bytes (str): optional regex of localAs2Bytes
        - LocalAs4Bytes (str): optional regex of localAs4Bytes
        - MaxBGPMsgLengthTx (str): optional regex of maxBGPMsgLengthTx
        - Md5Key (str): optional regex of md5Key
        - ModeOfBfdOperations (str): optional regex of modeOfBfdOperations
        - NumBgpLsId (str): optional regex of numBgpLsId
        - NumBgpLsInstanceIdentifier (str): optional regex of numBgpLsInstanceIdentifier
        - NumBgpUpdatesGeneratedPerIteration (str): optional regex of numBgpUpdatesGeneratedPerIteration
        - OperationalModel (str): optional regex of operationalModel
        - RestartTime (str): optional regex of restartTime
        - RoutersMacOrIrbMacAddress (str): optional regex of routersMacOrIrbMacAddress
        - SendIxiaSignatureWithRoutes (str): optional regex of sendIxiaSignatureWithRoutes
        - StaleTime (str): optional regex of staleTime
        - TcpWindowSizeInBytes (str): optional regex of tcpWindowSizeInBytes
        - Ttl (str): optional regex of ttl
        - Type (str): optional regex of type
        - UpdateInterval (str): optional regex of updateInterval
        - UptimeInSec (str): optional regex of uptimeInSec
        - VplsEnableNextHop (str): optional regex of vplsEnableNextHop
        - VplsNextHop (str): optional regex of vplsNextHop

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
