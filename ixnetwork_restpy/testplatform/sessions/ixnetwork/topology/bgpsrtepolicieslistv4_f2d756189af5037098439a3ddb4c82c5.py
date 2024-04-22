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


class BgpSRTEPoliciesListV4(Base):
    """
    The BgpSRTEPoliciesListV4 class encapsulates a required bgpSRTEPoliciesListV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpSRTEPoliciesListV4"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AddPathId": "addPathId",
        "AggregatorAs": "aggregatorAs",
        "AggregatorId": "aggregatorId",
        "AsSetMode": "asSetMode",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Distinguisher": "distinguisher",
        "EnableAddPath": "enableAddPath",
        "EnableAggregatorId": "enableAggregatorId",
        "EnableAsPathSegments": "enableAsPathSegments",
        "EnableAtomicAggregate": "enableAtomicAggregate",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableExtendedCommunity": "enableExtendedCommunity",
        "EnableLinkLocal": "enableLinkLocal",
        "EnableLocalPreference": "enableLocalPreference",
        "EnableMultiExitDiscriminator": "enableMultiExitDiscriminator",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginatorId": "enableOriginatorId",
        "EnableSendWithdraw": "enableSendWithdraw",
        "EndPointV4": "endPointV4",
        "EndPointV6": "endPointV6",
        "Ipv4NextHop": "ipv4NextHop",
        "Ipv6LinkLocalNextHop": "ipv6LinkLocalNextHop",
        "Ipv6NextHop": "ipv6NextHop",
        "LocalPreference": "localPreference",
        "MultiExitDiscriminator": "multiExitDiscriminator",
        "Name": "name",
        "NoOfASPathSegmentsPerRouteRange": "noOfASPathSegmentsPerRouteRange",
        "NoOfClusters": "noOfClusters",
        "NoOfCommunities": "noOfCommunities",
        "NoOfExtendedCommunity": "noOfExtendedCommunity",
        "NumberOfTunnelsV4": "numberOfTunnelsV4",
        "Origin": "origin",
        "OriginatorId": "originatorId",
        "OverridePeerAsSetMode": "overridePeerAsSetMode",
        "PolicyColor": "policyColor",
        "PolicyType": "policyType",
        "SetNextHop": "setNextHop",
        "SetNextHopIpType": "setNextHopIpType",
        "SrtepolicyName": "srtepolicyName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpSRTEPoliciesListV4, self).__init__(parent, list_op)

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
    def BgpSRTEPoliciesTunnelEncapsulationListV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciestunnelencapsulationlistv4_9031e764336dd61c6ed0b672cca24aab.BgpSRTEPoliciesTunnelEncapsulationListV4): An instance of the BgpSRTEPoliciesTunnelEncapsulationListV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciestunnelencapsulationlistv4_9031e764336dd61c6ed0b672cca24aab import (
            BgpSRTEPoliciesTunnelEncapsulationListV4,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("BgpSRTEPoliciesTunnelEncapsulationListV4", None)
                is not None
            ):
                return self._properties.get("BgpSRTEPoliciesTunnelEncapsulationListV4")
        return BgpSRTEPoliciesTunnelEncapsulationListV4(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AddPathId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP ADD Path Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AddPathId"]))

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
    def Distinguisher(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Distinguisher
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Distinguisher"]))

    @property
    def EnableAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Path ID when ADD Path Capability is enabled in BGP Peer
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableAddPath"]))

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
    def EnableLinkLocal(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled pick Link Local IPv6 from interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableLinkLocal"])
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
    def EnableSendWithdraw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Send Withdraw
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSendWithdraw"])
        )

    @property
    def EndPointV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 End Point
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndPointV4"]))

    @property
    def EndPointV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 End Point
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndPointV6"]))

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
    def Ipv6LinkLocalNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When next hop type is Global+ Link Local use this Link Local IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6LinkLocalNextHop"])
        )

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
    def NumberOfTunnelsV4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of Tunnel TLVs Per Policy
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfTunnelsV4"])

    @NumberOfTunnelsV4.setter
    def NumberOfTunnelsV4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfTunnelsV4"], value)

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
    def PolicyColor(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy Color
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PolicyColor"]))

    @property
    def PolicyType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PolicyType"]))

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
    def SrtepolicyName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy Name For Reference
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrtepolicyName"])
        )

    def update(
        self,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
        NumberOfTunnelsV4=None,
    ):
        # type: (str, int, int, int, int, int) -> BgpSRTEPoliciesListV4
        """Updates bgpSRTEPoliciesListV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NumberOfTunnelsV4 (number): Count of Tunnel TLVs Per Policy

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
        NumberOfTunnelsV4=None,
    ):
        # type: (int, str, str, int, int, int, int, int) -> BgpSRTEPoliciesListV4
        """Finds and retrieves bgpSRTEPoliciesListV4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpSRTEPoliciesListV4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpSRTEPoliciesListV4 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NumberOfTunnelsV4 (number): Count of Tunnel TLVs Per Policy

        Returns
        -------
        - self: This instance with matching bgpSRTEPoliciesListV4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpSRTEPoliciesListV4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpSRTEPoliciesListV4 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AddPathId=None,
        AggregatorAs=None,
        AggregatorId=None,
        AsSetMode=None,
        Distinguisher=None,
        EnableAddPath=None,
        EnableAggregatorId=None,
        EnableAsPathSegments=None,
        EnableAtomicAggregate=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableExtendedCommunity=None,
        EnableLinkLocal=None,
        EnableLocalPreference=None,
        EnableMultiExitDiscriminator=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableSendWithdraw=None,
        EndPointV4=None,
        EndPointV6=None,
        Ipv4NextHop=None,
        Ipv6LinkLocalNextHop=None,
        Ipv6NextHop=None,
        LocalPreference=None,
        MultiExitDiscriminator=None,
        Origin=None,
        OriginatorId=None,
        OverridePeerAsSetMode=None,
        PolicyColor=None,
        PolicyType=None,
        SetNextHop=None,
        SetNextHopIpType=None,
        SrtepolicyName=None,
    ):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesListV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AddPathId (str): optional regex of addPathId
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AsSetMode (str): optional regex of asSetMode
        - Distinguisher (str): optional regex of distinguisher
        - EnableAddPath (str): optional regex of enableAddPath
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableLinkLocal (str): optional regex of enableLinkLocal
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableSendWithdraw (str): optional regex of enableSendWithdraw
        - EndPointV4 (str): optional regex of endPointV4
        - EndPointV6 (str): optional regex of endPointV6
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6LinkLocalNextHop (str): optional regex of ipv6LinkLocalNextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - PolicyColor (str): optional regex of policyColor
        - PolicyType (str): optional regex of policyType
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - SrtepolicyName (str): optional regex of srtepolicyName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
