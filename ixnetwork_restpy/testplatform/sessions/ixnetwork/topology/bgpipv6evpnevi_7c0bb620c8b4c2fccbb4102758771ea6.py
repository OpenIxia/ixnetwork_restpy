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


class BgpIPv6EvpnEvi(Base):
    """BGP IPv6 Peer EVPN EVI Configuration
    The BgpIPv6EvpnEvi class encapsulates a list of bgpIPv6EvpnEvi resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpIPv6EvpnEvi.find() method.
    The list can be managed by using the BgpIPv6EvpnEvi.add() and BgpIPv6EvpnEvi.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bgpIPv6EvpnEvi"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AdRouteLabel": "adRouteLabel",
        "AdvSrv6SidInIgp": "advSrv6SidInIgp",
        "AdvSrv6SidInIgpPMSI": "advSrv6SidInIgpPMSI",
        "AdvertiseL3vniSeparately": "advertiseL3vniSeparately",
        "AdvertiseSRv6SID": "advertiseSRv6SID",
        "AdvertiseSRv6SIDPMSI": "advertiseSRv6SIDPMSI",
        "AggregatorAs": "aggregatorAs",
        "AggregatorId": "aggregatorId",
        "AsSetMode": "asSetMode",
        "AutoConfigOriginatingRouterIp": "autoConfigOriginatingRouterIp",
        "AutoConfigPMSITunnelId": "autoConfigPMSITunnelId",
        "AutoConfigureRdIpAddress": "autoConfigureRdIpAddress",
        "BMacFirstLabel": "bMacFirstLabel",
        "BMacSecondLabel": "bMacSecondLabel",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableAggregatorId": "enableAggregatorId",
        "EnableAsPathSegments": "enableAsPathSegments",
        "EnableAtomicAggregate": "enableAtomicAggregate",
        "EnableBMacSecondLabel": "enableBMacSecondLabel",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableExtendedCommunity": "enableExtendedCommunity",
        "EnableL3TargetOnlyForRouteType5": "enableL3TargetOnlyForRouteType5",
        "EnableL3vniTargetList": "enableL3vniTargetList",
        "EnableLocalPreference": "enableLocalPreference",
        "EnableMultiExitDiscriminator": "enableMultiExitDiscriminator",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginatorId": "enableOriginatorId",
        "Errors": "errors",
        "EsiType": "esiType",
        "EsiValue": "esiValue",
        "EvpnArgumentLength": "evpnArgumentLength",
        "EvpnEnableTransposition": "evpnEnableTransposition",
        "EvpnFunctionLength": "evpnFunctionLength",
        "EvpnIncSrv6SidStructSsTlv": "evpnIncSrv6SidStructSsTlv",
        "EvpnLocBlockLength": "evpnLocBlockLength",
        "EvpnLocNodeLength": "evpnLocNodeLength",
        "EvpnTranpositionLength": "evpnTranpositionLength",
        "EvpnTranpositionOffset": "evpnTranpositionOffset",
        "IgmpProxySupport": "igmpProxySupport",
        "ImportRtListSameAsExportRtList": "importRtListSameAsExportRtList",
        "IncludeMcastFlagsExtComm": "includeMcastFlagsExtComm",
        "IncludePmsiTunnelAttribute": "includePmsiTunnelAttribute",
        "Ipv4NextHop": "ipv4NextHop",
        "Ipv6NextHop": "ipv6NextHop",
        "L3vniImportRtListSameAsL3vniExportRtList": "l3vniImportRtListSameAsL3vniExportRtList",
        "LocalPreference": "localPreference",
        "MldProxySupport": "mldProxySupport",
        "MultiExitDiscriminator": "multiExitDiscriminator",
        "MulticastTunnelType": "multicastTunnelType",
        "Multiplier": "multiplier",
        "Name": "name",
        "NoOfASPathSegmentsPerRouteRange": "noOfASPathSegmentsPerRouteRange",
        "NoOfClusters": "noOfClusters",
        "NoOfCommunities": "noOfCommunities",
        "NoOfExtendedCommunity": "noOfExtendedCommunity",
        "NumBroadcastDomainV6": "numBroadcastDomainV6",
        "NumRtInExportRouteTargetList": "numRtInExportRouteTargetList",
        "NumRtInImportRouteTargetList": "numRtInImportRouteTargetList",
        "NumRtInL3vniExportRouteTargetList": "numRtInL3vniExportRouteTargetList",
        "NumRtInL3vniImportRouteTargetList": "numRtInL3vniImportRouteTargetList",
        "Origin": "origin",
        "OriginatingRouterIpv4": "originatingRouterIpv4",
        "OriginatingRouterIpv6": "originatingRouterIpv6",
        "OriginatorId": "originatorId",
        "OverridePeerAsSetMode": "overridePeerAsSetMode",
        "PmsiArgumentLength": "pmsiArgumentLength",
        "PmsiEnableTransposition": "pmsiEnableTransposition",
        "PmsiFunctionLength": "pmsiFunctionLength",
        "PmsiIncSrv6SidStructSsTlv": "pmsiIncSrv6SidStructSsTlv",
        "PmsiLocBlockLength": "pmsiLocBlockLength",
        "PmsiLocNodeLength": "pmsiLocNodeLength",
        "PmsiTranpositionLength": "pmsiTranpositionLength",
        "PmsiTranpositionOffset": "pmsiTranpositionOffset",
        "PmsiTunnelIDv4": "pmsiTunnelIDv4",
        "PmsiTunnelIDv6": "pmsiTunnelIDv6",
        "RdASNumber": "rdASNumber",
        "RdEvi": "rdEvi",
        "RdIpAddress": "rdIpAddress",
        "RdType": "rdType",
        "SendSRv6SIDOptionalInfo": "sendSRv6SIDOptionalInfo",
        "SendSRv6SIDOptionalInfoPMSI": "sendSRv6SIDOptionalInfoPMSI",
        "SessionStatus": "sessionStatus",
        "SetNextHop": "setNextHop",
        "SetNextHopIpType": "setNextHopIpType",
        "Srv6EndpointBehavior": "srv6EndpointBehavior",
        "Srv6EndpointBehaviorPMSI": "srv6EndpointBehaviorPMSI",
        "Srv6SIDOptionalInformation": "srv6SIDOptionalInformation",
        "Srv6SIDOptionalInformationPMSI": "srv6SIDOptionalInformationPMSI",
        "Srv6SidFlags": "srv6SidFlags",
        "Srv6SidFlagsPMSI": "srv6SidFlagsPMSI",
        "Srv6SidLoc": "srv6SidLoc",
        "Srv6SidLocLen": "srv6SidLocLen",
        "Srv6SidLocLenPMSI": "srv6SidLocLenPMSI",
        "Srv6SidLocMetric": "srv6SidLocMetric",
        "Srv6SidLocMetricPMSI": "srv6SidLocMetricPMSI",
        "Srv6SidLocPMSI": "srv6SidLocPMSI",
        "Srv6SidReserved": "srv6SidReserved",
        "Srv6SidReserved1": "srv6SidReserved1",
        "Srv6SidReserved1PMSI": "srv6SidReserved1PMSI",
        "Srv6SidReserved2": "srv6SidReserved2",
        "Srv6SidReserved2PMSI": "srv6SidReserved2PMSI",
        "Srv6SidReservedPMSI": "srv6SidReservedPMSI",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "UpstreamDownstreamAssignedMplsLabel": "upstreamDownstreamAssignedMplsLabel",
        "UseIpv4MappedIpv6Address": "useIpv4MappedIpv6Address",
        "UseUpstreamDownstreamAssignedMplsLabel": "useUpstreamDownstreamAssignedMplsLabel",
    }
    _SDM_ENUM_MAP = {
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
        super(BgpIPv6EvpnEvi, self).__init__(parent, list_op)

    @property
    def BgpAsPathSegmentList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist_4d209c5ac36c18374125f19531d4795f.BgpAsPathSegmentList): An instance of the BgpAsPathSegmentList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist_4d209c5ac36c18374125f19531d4795f import (
            BgpAsPathSegmentList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpAsPathSegmentList", None) is not None:
                return self._properties.get("BgpAsPathSegmentList")
        return BgpAsPathSegmentList(self)

    @property
    def BgpClusterIdList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist_82b17094a31a96f755045be572017577.BgpClusterIdList): An instance of the BgpClusterIdList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist_82b17094a31a96f755045be572017577 import (
            BgpClusterIdList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpClusterIdList", None) is not None:
                return self._properties.get("BgpClusterIdList")
        return BgpClusterIdList(self)

    @property
    def BgpCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist_e5bf1a4a4a05d2687d59e9c2a92fa768.BgpCommunitiesList): An instance of the BgpCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist_e5bf1a4a4a05d2687d59e9c2a92fa768 import (
            BgpCommunitiesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpCommunitiesList", None) is not None:
                return self._properties.get("BgpCommunitiesList")
        return BgpCommunitiesList(self)

    @property
    def BgpExportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist_ce93ce056c01eaf7643c31a7fd67768c.BgpExportRouteTargetList): An instance of the BgpExportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist_ce93ce056c01eaf7643c31a7fd67768c import (
            BgpExportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpExportRouteTargetList", None) is not None:
                return self._properties.get("BgpExportRouteTargetList")
        return BgpExportRouteTargetList(self)

    @property
    def BgpExtendedCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist_8226f9a3ca5552e5a51e89a45cfc1b7e.BgpExtendedCommunitiesList): An instance of the BgpExtendedCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist_8226f9a3ca5552e5a51e89a45cfc1b7e import (
            BgpExtendedCommunitiesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpExtendedCommunitiesList", None) is not None:
                return self._properties.get("BgpExtendedCommunitiesList")
        return BgpExtendedCommunitiesList(self)

    @property
    def BgpImportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist_99470595cc13238e15b19c07b8af6021.BgpImportRouteTargetList): An instance of the BgpImportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist_99470595cc13238e15b19c07b8af6021 import (
            BgpImportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpImportRouteTargetList", None) is not None:
                return self._properties.get("BgpImportRouteTargetList")
        return BgpImportRouteTargetList(self)

    @property
    def BgpL3VNIExportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vniexportroutetargetlist_0ceb637a2c3fee9e0d0bdf68e75d9054.BgpL3VNIExportRouteTargetList): An instance of the BgpL3VNIExportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vniexportroutetargetlist_0ceb637a2c3fee9e0d0bdf68e75d9054 import (
            BgpL3VNIExportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpL3VNIExportRouteTargetList", None) is not None:
                return self._properties.get("BgpL3VNIExportRouteTargetList")
        return BgpL3VNIExportRouteTargetList(self)

    @property
    def BgpL3VNIImportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vniimportroutetargetlist_f9fc41787790538b1714fae483245f7d.BgpL3VNIImportRouteTargetList): An instance of the BgpL3VNIImportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vniimportroutetargetlist_f9fc41787790538b1714fae483245f7d import (
            BgpL3VNIImportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpL3VNIImportRouteTargetList", None) is not None:
                return self._properties.get("BgpL3VNIImportRouteTargetList")
        return BgpL3VNIImportRouteTargetList(self)

    @property
    def BroadcastDomainV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.broadcastdomainv6_f52f2d23ece3114c2b2d1e550e07fc42.BroadcastDomainV6): An instance of the BroadcastDomainV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.broadcastdomainv6_f52f2d23ece3114c2b2d1e550e07fc42 import (
            BroadcastDomainV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BroadcastDomainV6", None) is not None:
                return self._properties.get("BroadcastDomainV6")
        return BroadcastDomainV6(self)._select()

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
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import (
            Tag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Tag", None) is not None:
                return self._properties.get("Tag")
        return Tag(self)

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
    def AdRouteLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AD Route Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdRouteLabel"]))

    @property
    def AdvSrv6SidInIgp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvSrv6SidInIgp"])
        )

    @property
    def AdvSrv6SidInIgpPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvSrv6SidInIgpPMSI"])
        )

    @property
    def AdvertiseL3vniSeparately(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise L3 Route Separately
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseL3vniSeparately"])
        )

    @property
    def AdvertiseSRv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSRv6SID"])
        )

    @property
    def AdvertiseSRv6SIDPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSRv6SIDPMSI"])
        )

    @property
    def AggregatorAs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator AS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AggregatorAs"]))

    @property
    def AggregatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AggregatorId"]))

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
    def AutoConfigOriginatingRouterIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to true, this field enables option to configure Originating router IP address automatically from BGP Router's local IP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AutoConfigOriginatingRouterIp"]),
        )

    @property
    def AutoConfigPMSITunnelId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Configure PMSI Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoConfigPMSITunnelId"])
        )

    @property
    def AutoConfigureRdIpAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto-Configure RD IP Addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoConfigureRdIpAddress"])
        )

    @property
    def BMacFirstLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B MAC First Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BMacFirstLabel"])
        )

    @property
    def BMacSecondLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B MAC Second Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BMacSecondLabel"])
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
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EnableAggregatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableAggregatorId"])
        )

    @property
    def EnableAsPathSegments(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AS Path Segments
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableAsPathSegments"])
        )

    @property
    def EnableAtomicAggregate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Atomic Aggregate
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableAtomicAggregate"])
        )

    @property
    def EnableBMacSecondLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable B MAC Second Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableBMacSecondLabel"])
        )

    @property
    def EnableCluster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Cluster
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableCluster"]))

    @property
    def EnableCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableCommunity"])
        )

    @property
    def EnableExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableExtendedCommunity"])
        )

    @property
    def EnableL3TargetOnlyForRouteType5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable L3 Target only for Route Type 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EnableL3TargetOnlyForRouteType5"]),
        )

    @property
    def EnableL3vniTargetList(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable L3 Target List
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableL3vniTargetList"])
        )

    @property
    def EnableLocalPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableLocalPreference"])
        )

    @property
    def EnableMultiExitDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableMultiExitDiscriminator"])
        )

    @property
    def EnableNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableNextHop"]))

    @property
    def EnableOrigin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableOrigin"]))

    @property
    def EnableOriginatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableOriginatorId"])
        )

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def EsiType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ESI Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EsiType"]))

    @property
    def EsiValue(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): ESI Value
        """
        return self._get_attribute(self._SDM_ATT_MAP["EsiValue"])

    @property
    def EvpnArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Argument Length for EVI with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnArgumentLength"])
        )

    @property
    def EvpnEnableTransposition(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, transposition mechanism will be enabled and Srv6 SID will be transposed as per transposition configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnEnableTransposition"])
        )

    @property
    def EvpnFunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Function Length for EVI with Minimum value of 0 , Max value upto 128 bits and default value of 16.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnFunctionLength"])
        )

    @property
    def EvpnIncSrv6SidStructSsTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it includes the SRv6 SID Structure Sub-Sub TLV into EVPN EVI for Type 1 Route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnIncSrv6SidStructSsTlv"])
        )

    @property
    def EvpnLocBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Block Length for EVI with Minimum value of 0 , Max value upto 128 bits and default value of 40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnLocBlockLength"])
        )

    @property
    def EvpnLocNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Node Length for EVI with Minimum value of 0 , Max value upto 128 bits and default value of 24.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnLocNodeLength"])
        )

    @property
    def EvpnTranpositionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition length for EVI with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnTranpositionLength"])
        )

    @property
    def EvpnTranpositionOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition offset for EVI with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvpnTranpositionOffset"])
        )

    @property
    def IgmpProxySupport(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables 'I' bit in Multicast Flags Extended Community that is carried with IMET route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IgmpProxySupport"])
        )

    @property
    def ImportRtListSameAsExportRtList(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Import RT List Same As Export RT List
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImportRtListSameAsExportRtList"])

    @ImportRtListSameAsExportRtList.setter
    def ImportRtListSameAsExportRtList(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImportRtListSameAsExportRtList"], value)

    @property
    def IncludeMcastFlagsExtComm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables Multicast Flags Extended Community that is carried with IMET route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMcastFlagsExtComm"])
        )

    @property
    def IncludePmsiTunnelAttribute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include PMSI Tunnel Attribute
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludePmsiTunnelAttribute"])
        )

    @property
    def Ipv4NextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4NextHop"]))

    @property
    def Ipv6NextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6NextHop"]))

    @property
    def L3vniImportRtListSameAsL3vniExportRtList(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L3 Import RT List Same As L3 Export RT List
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["L3vniImportRtListSameAsL3vniExportRtList"]
        )

    @L3vniImportRtListSameAsL3vniExportRtList.setter
    def L3vniImportRtListSameAsL3vniExportRtList(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["L3vniImportRtListSameAsL3vniExportRtList"], value
        )

    @property
    def LocalPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalPreference"])
        )

    @property
    def MldProxySupport(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables 'M' bit in Multicast Flags Extended Community that is carried with IMET route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MldProxySupport"])
        )

    @property
    def MultiExitDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MultiExitDiscriminator"])
        )

    @property
    def MulticastTunnelType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Tunnel Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastTunnelType"])
        )

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
    def NoOfASPathSegmentsPerRouteRange(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number Of AS Path Segments Per Route Range
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfASPathSegmentsPerRouteRange"])

    @NoOfASPathSegmentsPerRouteRange.setter
    def NoOfASPathSegmentsPerRouteRange(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfASPathSegmentsPerRouteRange"], value)

    @property
    def NoOfClusters(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Clusters
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfClusters"])

    @NoOfClusters.setter
    def NoOfClusters(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfClusters"], value)

    @property
    def NoOfCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfCommunities"])

    @NoOfCommunities.setter
    def NoOfCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfCommunities"], value)

    @property
    def NoOfExtendedCommunity(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfExtendedCommunity"])

    @NoOfExtendedCommunity.setter
    def NoOfExtendedCommunity(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfExtendedCommunity"], value)

    @property
    def NumBroadcastDomainV6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of broadcast domain to be configured under EVI
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumBroadcastDomainV6"])

    @NumBroadcastDomainV6.setter
    def NumBroadcastDomainV6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumBroadcastDomainV6"], value)

    @property
    def NumRtInExportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in Export Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRtInExportRouteTargetList"])

    @NumRtInExportRouteTargetList.setter
    def NumRtInExportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRtInExportRouteTargetList"], value)

    @property
    def NumRtInImportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in Import Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRtInImportRouteTargetList"])

    @NumRtInImportRouteTargetList.setter
    def NumRtInImportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRtInImportRouteTargetList"], value)

    @property
    def NumRtInL3vniExportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in L3 Export Route Target List(multiplier)
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumRtInL3vniExportRouteTargetList"]
        )

    @NumRtInL3vniExportRouteTargetList.setter
    def NumRtInL3vniExportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumRtInL3vniExportRouteTargetList"], value
        )

    @property
    def NumRtInL3vniImportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in L3 Import Route Target List(multiplier)
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumRtInL3vniImportRouteTargetList"]
        )

    @NumRtInL3vniImportRouteTargetList.setter
    def NumRtInL3vniImportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumRtInL3vniImportRouteTargetList"], value
        )

    @property
    def Origin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Origin"]))

    @property
    def OriginatingRouterIpv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures Originating Router IP address in IPv4 Address format
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OriginatingRouterIpv4"])
        )

    @property
    def OriginatingRouterIpv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures Originating Router IP address in IPv6 Address format
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OriginatingRouterIpv6"])
        )

    @property
    def OriginatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OriginatorId"]))

    @property
    def OverridePeerAsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OverridePeerAsSetMode"])
        )

    @property
    def PmsiArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Argument Length for PMSI with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiArgumentLength"])
        )

    @property
    def PmsiEnableTransposition(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, transposition mechanism will be enabled and Srv6 SID will be transposed as per transposition configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiEnableTransposition"])
        )

    @property
    def PmsiFunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Function Length for PMSI with Minimum value of 0 , Max value upto 128 bits and default value of 16.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiFunctionLength"])
        )

    @property
    def PmsiIncSrv6SidStructSsTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it includes the SRv6 SID Structure Sub-Sub TLV into EVPN PMSI for Type 3 Route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiIncSrv6SidStructSsTlv"])
        )

    @property
    def PmsiLocBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Block Length for PMSI with Minimum value of 0 , Max value upto 128 bits and default value of 40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiLocBlockLength"])
        )

    @property
    def PmsiLocNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Node Length for PMSI with Minimum value of 0 , Max value upto 128 bits and default value of 24.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiLocNodeLength"])
        )

    @property
    def PmsiTranpositionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition length for PMSI with Minimum value of 0 , Max value upto 24 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiTranpositionLength"])
        )

    @property
    def PmsiTranpositionOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition offset for PMSI with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiTranpositionOffset"])
        )

    @property
    def PmsiTunnelIDv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PMSI Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiTunnelIDv4"])
        )

    @property
    def PmsiTunnelIDv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PMSI Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PmsiTunnelIDv6"])
        )

    @property
    def RdASNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVPN Route Distinguisher AS Number (2-byte or 4-Byte)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RdASNumber"]))

    @property
    def RdEvi(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVPN Route Distinguisher Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RdEvi"]))

    @property
    def RdIpAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RD IP Addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RdIpAddress"]))

    @property
    def RdType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVPN RR Distinguisher Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RdType"]))

    @property
    def SendSRv6SIDOptionalInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendSRv6SIDOptionalInfo"])
        )

    @property
    def SendSRv6SIDOptionalInfoPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendSRv6SIDOptionalInfoPMSI"])
        )

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
    def SetNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SetNextHop"]))

    @property
    def SetNextHopIpType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SetNextHopIpType"])
        )

    @property
    def Srv6EndpointBehavior(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6EndpointBehavior"])
        )

    @property
    def Srv6EndpointBehaviorPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6EndpointBehaviorPMSI"])
        )

    @property
    def Srv6SIDOptionalInformation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SIDOptionalInformation"])
        )

    @property
    def Srv6SIDOptionalInformationPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Srv6SIDOptionalInformationPMSI"]),
        )

    @property
    def Srv6SidFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidFlags"]))

    @property
    def Srv6SidFlagsPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidFlagsPMSI"])
        )

    @property
    def Srv6SidLoc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLoc"]))

    @property
    def Srv6SidLocLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLocLen"]))

    @property
    def Srv6SidLocLenPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLocLenPMSI"])
        )

    @property
    def Srv6SidLocMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLocMetric"])
        )

    @property
    def Srv6SidLocMetricPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLocMetricPMSI"])
        )

    @property
    def Srv6SidLocPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLocPMSI"])
        )

    @property
    def Srv6SidReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved"])
        )

    @property
    def Srv6SidReserved1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved1 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved1"])
        )

    @property
    def Srv6SidReserved1PMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved1 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved1PMSI"])
        )

    @property
    def Srv6SidReserved2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved2"])
        )

    @property
    def Srv6SidReserved2PMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved2PMSI"])
        )

    @property
    def Srv6SidReservedPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReservedPMSI"])
        )

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
    def UpstreamDownstreamAssignedMplsLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream/Downstream Assigned MPLS Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UpstreamDownstreamAssignedMplsLabel"]
            ),
        )

    @property
    def UseIpv4MappedIpv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use IPv4 Mapped IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseIpv4MappedIpv6Address"])
        )

    @property
    def UseUpstreamDownstreamAssignedMplsLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Upstream/Downstream Assigned MPLS Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UseUpstreamDownstreamAssignedMplsLabel"]
            ),
        )

    def update(
        self,
        ConnectedVia=None,
        ImportRtListSameAsExportRtList=None,
        L3vniImportRtListSameAsL3vniExportRtList=None,
        Multiplier=None,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
        NumBroadcastDomainV6=None,
        NumRtInExportRouteTargetList=None,
        NumRtInImportRouteTargetList=None,
        NumRtInL3vniExportRouteTargetList=None,
        NumRtInL3vniImportRouteTargetList=None,
        StackedLayers=None,
    ):
        # type: (List[str], bool, bool, int, str, int, int, int, int, int, int, int, int, int, List[str]) -> BgpIPv6EvpnEvi
        """Updates bgpIPv6EvpnEvi resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
        - NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        ImportRtListSameAsExportRtList=None,
        L3vniImportRtListSameAsL3vniExportRtList=None,
        Multiplier=None,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
        NumBroadcastDomainV6=None,
        NumRtInExportRouteTargetList=None,
        NumRtInImportRouteTargetList=None,
        NumRtInL3vniExportRouteTargetList=None,
        NumRtInL3vniImportRouteTargetList=None,
        StackedLayers=None,
    ):
        # type: (List[str], bool, bool, int, str, int, int, int, int, int, int, int, int, int, List[str]) -> BgpIPv6EvpnEvi
        """Adds a new bgpIPv6EvpnEvi resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
        - NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved bgpIPv6EvpnEvi resources using find and the newly added bgpIPv6EvpnEvi resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpIPv6EvpnEvi resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        Errors=None,
        EsiValue=None,
        ImportRtListSameAsExportRtList=None,
        L3vniImportRtListSameAsL3vniExportRtList=None,
        Multiplier=None,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
        NumBroadcastDomainV6=None,
        NumRtInExportRouteTargetList=None,
        NumRtInImportRouteTargetList=None,
        NumRtInL3vniExportRouteTargetList=None,
        NumRtInL3vniImportRouteTargetList=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves bgpIPv6EvpnEvi resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpIPv6EvpnEvi resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpIPv6EvpnEvi resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - EsiValue (list(str)): ESI Value
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
        - NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching bgpIPv6EvpnEvi resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpIPv6EvpnEvi data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpIPv6EvpnEvi resources from the server available through an iterator or index

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

    def AdvertiseAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the advertiseAliasing operation on the server.

        Advertise Aliasing Per EVI.

        advertiseAliasing(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute("advertiseAliasing", payload=payload, response_object=None)

    def AdvertiseAliasingPerEvi(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the advertiseAliasingPerEvi operation on the server.

        Advertise Aliasing Per EVI

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        advertiseAliasingPerEvi(async_operation=bool)
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        advertiseAliasingPerEvi(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        advertiseAliasingPerEvi(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------
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
            "advertiseAliasingPerEvi", payload=payload, response_object=None
        )

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

    def WithdrawAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the withdrawAliasing operation on the server.

        Withdraw Aliasing Per EVI.

        withdrawAliasing(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute("withdrawAliasing", payload=payload, response_object=None)

    def WithdrawAliasingPerEvi(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the withdrawAliasingPerEvi operation on the server.

        Withdraw Aliasing Per EVI

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        withdrawAliasingPerEvi(async_operation=bool)
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawAliasingPerEvi(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawAliasingPerEvi(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------
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
            "withdrawAliasingPerEvi", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AdRouteLabel=None,
        AdvSrv6SidInIgp=None,
        AdvSrv6SidInIgpPMSI=None,
        AdvertiseL3vniSeparately=None,
        AdvertiseSRv6SID=None,
        AdvertiseSRv6SIDPMSI=None,
        AggregatorAs=None,
        AggregatorId=None,
        AsSetMode=None,
        AutoConfigOriginatingRouterIp=None,
        AutoConfigPMSITunnelId=None,
        AutoConfigureRdIpAddress=None,
        BMacFirstLabel=None,
        BMacSecondLabel=None,
        EnableAggregatorId=None,
        EnableAsPathSegments=None,
        EnableAtomicAggregate=None,
        EnableBMacSecondLabel=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableExtendedCommunity=None,
        EnableL3TargetOnlyForRouteType5=None,
        EnableL3vniTargetList=None,
        EnableLocalPreference=None,
        EnableMultiExitDiscriminator=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EsiType=None,
        EvpnArgumentLength=None,
        EvpnEnableTransposition=None,
        EvpnFunctionLength=None,
        EvpnIncSrv6SidStructSsTlv=None,
        EvpnLocBlockLength=None,
        EvpnLocNodeLength=None,
        EvpnTranpositionLength=None,
        EvpnTranpositionOffset=None,
        IgmpProxySupport=None,
        IncludeMcastFlagsExtComm=None,
        IncludePmsiTunnelAttribute=None,
        Ipv4NextHop=None,
        Ipv6NextHop=None,
        LocalPreference=None,
        MldProxySupport=None,
        MultiExitDiscriminator=None,
        MulticastTunnelType=None,
        Origin=None,
        OriginatingRouterIpv4=None,
        OriginatingRouterIpv6=None,
        OriginatorId=None,
        OverridePeerAsSetMode=None,
        PmsiArgumentLength=None,
        PmsiEnableTransposition=None,
        PmsiFunctionLength=None,
        PmsiIncSrv6SidStructSsTlv=None,
        PmsiLocBlockLength=None,
        PmsiLocNodeLength=None,
        PmsiTranpositionLength=None,
        PmsiTranpositionOffset=None,
        PmsiTunnelIDv4=None,
        PmsiTunnelIDv6=None,
        RdASNumber=None,
        RdEvi=None,
        RdIpAddress=None,
        RdType=None,
        SendSRv6SIDOptionalInfo=None,
        SendSRv6SIDOptionalInfoPMSI=None,
        SetNextHop=None,
        SetNextHopIpType=None,
        Srv6EndpointBehavior=None,
        Srv6EndpointBehaviorPMSI=None,
        Srv6SIDOptionalInformation=None,
        Srv6SIDOptionalInformationPMSI=None,
        Srv6SidFlags=None,
        Srv6SidFlagsPMSI=None,
        Srv6SidLoc=None,
        Srv6SidLocLen=None,
        Srv6SidLocLenPMSI=None,
        Srv6SidLocMetric=None,
        Srv6SidLocMetricPMSI=None,
        Srv6SidLocPMSI=None,
        Srv6SidReserved=None,
        Srv6SidReserved1=None,
        Srv6SidReserved1PMSI=None,
        Srv6SidReserved2=None,
        Srv6SidReserved2PMSI=None,
        Srv6SidReservedPMSI=None,
        UpstreamDownstreamAssignedMplsLabel=None,
        UseIpv4MappedIpv6Address=None,
        UseUpstreamDownstreamAssignedMplsLabel=None,
    ):
        """Base class infrastructure that gets a list of bgpIPv6EvpnEvi device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdRouteLabel (str): optional regex of adRouteLabel
        - AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
        - AdvSrv6SidInIgpPMSI (str): optional regex of advSrv6SidInIgpPMSI
        - AdvertiseL3vniSeparately (str): optional regex of advertiseL3vniSeparately
        - AdvertiseSRv6SID (str): optional regex of advertiseSRv6SID
        - AdvertiseSRv6SIDPMSI (str): optional regex of advertiseSRv6SIDPMSI
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AsSetMode (str): optional regex of asSetMode
        - AutoConfigOriginatingRouterIp (str): optional regex of autoConfigOriginatingRouterIp
        - AutoConfigPMSITunnelId (str): optional regex of autoConfigPMSITunnelId
        - AutoConfigureRdIpAddress (str): optional regex of autoConfigureRdIpAddress
        - BMacFirstLabel (str): optional regex of bMacFirstLabel
        - BMacSecondLabel (str): optional regex of bMacSecondLabel
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableBMacSecondLabel (str): optional regex of enableBMacSecondLabel
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableL3TargetOnlyForRouteType5 (str): optional regex of enableL3TargetOnlyForRouteType5
        - EnableL3vniTargetList (str): optional regex of enableL3vniTargetList
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EsiType (str): optional regex of esiType
        - EvpnArgumentLength (str): optional regex of evpnArgumentLength
        - EvpnEnableTransposition (str): optional regex of evpnEnableTransposition
        - EvpnFunctionLength (str): optional regex of evpnFunctionLength
        - EvpnIncSrv6SidStructSsTlv (str): optional regex of evpnIncSrv6SidStructSsTlv
        - EvpnLocBlockLength (str): optional regex of evpnLocBlockLength
        - EvpnLocNodeLength (str): optional regex of evpnLocNodeLength
        - EvpnTranpositionLength (str): optional regex of evpnTranpositionLength
        - EvpnTranpositionOffset (str): optional regex of evpnTranpositionOffset
        - IgmpProxySupport (str): optional regex of igmpProxySupport
        - IncludeMcastFlagsExtComm (str): optional regex of includeMcastFlagsExtComm
        - IncludePmsiTunnelAttribute (str): optional regex of includePmsiTunnelAttribute
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LocalPreference (str): optional regex of localPreference
        - MldProxySupport (str): optional regex of mldProxySupport
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - MulticastTunnelType (str): optional regex of multicastTunnelType
        - Origin (str): optional regex of origin
        - OriginatingRouterIpv4 (str): optional regex of originatingRouterIpv4
        - OriginatingRouterIpv6 (str): optional regex of originatingRouterIpv6
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - PmsiArgumentLength (str): optional regex of pmsiArgumentLength
        - PmsiEnableTransposition (str): optional regex of pmsiEnableTransposition
        - PmsiFunctionLength (str): optional regex of pmsiFunctionLength
        - PmsiIncSrv6SidStructSsTlv (str): optional regex of pmsiIncSrv6SidStructSsTlv
        - PmsiLocBlockLength (str): optional regex of pmsiLocBlockLength
        - PmsiLocNodeLength (str): optional regex of pmsiLocNodeLength
        - PmsiTranpositionLength (str): optional regex of pmsiTranpositionLength
        - PmsiTranpositionOffset (str): optional regex of pmsiTranpositionOffset
        - PmsiTunnelIDv4 (str): optional regex of pmsiTunnelIDv4
        - PmsiTunnelIDv6 (str): optional regex of pmsiTunnelIDv6
        - RdASNumber (str): optional regex of rdASNumber
        - RdEvi (str): optional regex of rdEvi
        - RdIpAddress (str): optional regex of rdIpAddress
        - RdType (str): optional regex of rdType
        - SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
        - SendSRv6SIDOptionalInfoPMSI (str): optional regex of sendSRv6SIDOptionalInfoPMSI
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
        - Srv6EndpointBehaviorPMSI (str): optional regex of srv6EndpointBehaviorPMSI
        - Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
        - Srv6SIDOptionalInformationPMSI (str): optional regex of srv6SIDOptionalInformationPMSI
        - Srv6SidFlags (str): optional regex of srv6SidFlags
        - Srv6SidFlagsPMSI (str): optional regex of srv6SidFlagsPMSI
        - Srv6SidLoc (str): optional regex of srv6SidLoc
        - Srv6SidLocLen (str): optional regex of srv6SidLocLen
        - Srv6SidLocLenPMSI (str): optional regex of srv6SidLocLenPMSI
        - Srv6SidLocMetric (str): optional regex of srv6SidLocMetric
        - Srv6SidLocMetricPMSI (str): optional regex of srv6SidLocMetricPMSI
        - Srv6SidLocPMSI (str): optional regex of srv6SidLocPMSI
        - Srv6SidReserved (str): optional regex of srv6SidReserved
        - Srv6SidReserved1 (str): optional regex of srv6SidReserved1
        - Srv6SidReserved1PMSI (str): optional regex of srv6SidReserved1PMSI
        - Srv6SidReserved2 (str): optional regex of srv6SidReserved2
        - Srv6SidReserved2PMSI (str): optional regex of srv6SidReserved2PMSI
        - Srv6SidReservedPMSI (str): optional regex of srv6SidReservedPMSI
        - UpstreamDownstreamAssignedMplsLabel (str): optional regex of upstreamDownstreamAssignedMplsLabel
        - UseIpv4MappedIpv6Address (str): optional regex of useIpv4MappedIpv6Address
        - UseUpstreamDownstreamAssignedMplsLabel (str): optional regex of useUpstreamDownstreamAssignedMplsLabel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
