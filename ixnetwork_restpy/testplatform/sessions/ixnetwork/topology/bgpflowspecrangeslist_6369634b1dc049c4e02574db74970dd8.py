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


class BgpFlowSpecRangesList(Base):
    """Flow Spec
    The BgpFlowSpecRangesList class encapsulates a required bgpFlowSpecRangesList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpFlowSpecRangesList"
    _SDM_ATT_MAP = {
        "ActivateSRv6Policy": "activateSRv6Policy",
        "Active": "active",
        "AggregatorAs": "aggregatorAs",
        "AggregatorId": "aggregatorId",
        "ArgumentLengthFlowspec": "argumentLengthFlowspec",
        "AsNumber2Bytes": "asNumber2Bytes",
        "AsNumber4Bytes": "asNumber4Bytes",
        "AsSetMode": "asSetMode",
        "AssignedNumber2Bytes": "assignedNumber2Bytes",
        "AssignedNumber4Bytes": "assignedNumber4Bytes",
        "ColorCOBitsFlowspec": "colorCOBitsFlowspec",
        "ColorReservedBitsFlowspec": "colorReservedBitsFlowspec",
        "ColorValueFlowspec": "colorValueFlowspec",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DestPortMatch": "destPortMatch",
        "DestPrefixLengthV6": "destPrefixLengthV6",
        "DestPrefixOffset": "destPrefixOffset",
        "DestPrefixV6": "destPrefixV6",
        "DscpMatch": "dscpMatch",
        "EnableAggregatorId": "enableAggregatorId",
        "EnableAsPathSegments": "enableAsPathSegments",
        "EnableAtomicAggregate": "enableAtomicAggregate",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableDestPrefixV6": "enableDestPrefixV6",
        "EnableExtendedCommunity": "enableExtendedCommunity",
        "EnableLargeCommunities": "enableLargeCommunities",
        "EnableLocalPreference": "enableLocalPreference",
        "EnableMultiExitDiscriminator": "enableMultiExitDiscriminator",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginatorId": "enableOriginatorId",
        "EnableRedirect": "enableRedirect",
        "EnableRedirectIPv6NHop": "enableRedirectIPv6NHop",
        "EnableReirectIPv6": "enableReirectIPv6",
        "EnableSourcePrefixV6": "enableSourcePrefixV6",
        "EnableSrv6SidFlowspec": "enableSrv6SidFlowspec",
        "EnableTrafficAction": "enableTrafficAction",
        "EnableTrafficMarketing": "enableTrafficMarketing",
        "EnableTrafficMarking": "enableTrafficMarking",
        "EnableTrafficRate": "enableTrafficRate",
        "EnableTrafficRatePacket": "enableTrafficRatePacket",
        "FlowLabel": "flowLabel",
        "FlowSpecName": "flowSpecName",
        "FragmentMatchV6": "fragmentMatchV6",
        "FunctionLengthFlowspec": "functionLengthFlowspec",
        "IcmpCodeMatch": "icmpCodeMatch",
        "IcmpTypeMatch": "icmpTypeMatch",
        "IncSrv6SidStructSsTlvFlowspec": "incSrv6SidStructSsTlvFlowspec",
        "Ip": "ip",
        "IpPacketLenMatch": "ipPacketLenMatch",
        "IpV4": "ipV4",
        "Ipv4NextHop": "ipv4NextHop",
        "Ipv6NextHop": "ipv6NextHop",
        "LocBlockLengthFlowspec": "locBlockLengthFlowspec",
        "LocNodeLengthFlowspec": "locNodeLengthFlowspec",
        "LocalPreference": "localPreference",
        "MultiExitDiscriminator": "multiExitDiscriminator",
        "Name": "name",
        "NextHeader": "nextHeader",
        "NoOfASPathSegmentsPerRouteRange": "noOfASPathSegmentsPerRouteRange",
        "NoOfClusters": "noOfClusters",
        "NoOfCommunities": "noOfCommunities",
        "NoOfExtendedCommunity": "noOfExtendedCommunity",
        "NoOfLargeCommunities": "noOfLargeCommunities",
        "NumberOfFlows": "numberOfFlows",
        "Origin": "origin",
        "OriginatorId": "originatorId",
        "OverridePeerAsSetMode": "overridePeerAsSetMode",
        "PortMatch": "portMatch",
        "RedirectCBit": "redirectCBit",
        "RedirectCBitIPv6NHop": "redirectCBitIPv6NHop",
        "RedirectExtCommunityType": "redirectExtCommunityType",
        "RedirectIPv6": "redirectIPv6",
        "RedirectIPv6NHop": "redirectIPv6NHop",
        "Redirectnexthop": "redirectnexthop",
        "SetNextHop": "setNextHop",
        "SetNextHopIpType": "setNextHopIpType",
        "SourcePortMatch": "sourcePortMatch",
        "SourcePrefixLengthV6": "sourcePrefixLengthV6",
        "SourcePrefixV6": "sourcePrefixV6",
        "SrcPrefixOffset": "srcPrefixOffset",
        "Srv6EndpointBehaviorFlowspec": "srv6EndpointBehaviorFlowspec",
        "Srv6SidFlagsFlowspec": "srv6SidFlagsFlowspec",
        "Srv6SidFuncAllocTypeFlowspec": "srv6SidFuncAllocTypeFlowspec",
        "Srv6SidLocFlowspec": "srv6SidLocFlowspec",
        "Srv6SidReserved": "srv6SidReserved",
        "Srv6SidReserved1Flowspec": "srv6SidReserved1Flowspec",
        "Srv6SidReserved2Flowspec": "srv6SidReserved2Flowspec",
        "TcpFlagsMatch": "tcpFlagsMatch",
        "TerminalAction": "terminalAction",
        "TrafficActionSample": "trafficActionSample",
        "TrafficDscp": "trafficDscp",
        "TrafficRate": "trafficRate",
        "TrafficRatePacket": "trafficRatePacket",
        "TranspositionLengthFlowspec": "transpositionLengthFlowspec",
        "TranspositionOffsetFlowspec": "transpositionOffsetFlowspec",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpFlowSpecRangesList, self).__init__(parent, list_op)

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
    def BgpLargeCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplargecommunitieslist_703a2720b8aadfe51fc367a215cd291e.BgpLargeCommunitiesList): An instance of the BgpLargeCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplargecommunitieslist_703a2720b8aadfe51fc367a215cd291e import (
            BgpLargeCommunitiesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpLargeCommunitiesList", None) is not None:
                return self._properties.get("BgpLargeCommunitiesList")
        return BgpLargeCommunitiesList(self)

    @property
    def ActivateSRv6Policy(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to True, then the current SRv6 Policy is sent for the Flow Specification. Default value is set to False.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActivateSRv6Policy"])
        )

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
    def ArgumentLengthFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Argument length for SRv6 SID for the current Flow Specification. Default value is set to 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ArgumentLengthFlowspec"])
        )

    @property
    def AsNumber2Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS 2-Bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsNumber2Bytes"])
        )

    @property
    def AsNumber4Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS 4-Bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsNumber4Bytes"])
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
    def AssignedNumber2Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Assigned Number(2 Octets)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignedNumber2Bytes"])
        )

    @property
    def AssignedNumber4Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Assigned Number(4 Octets)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignedNumber4Bytes"])
        )

    @property
    def ColorCOBitsFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CO bits for the Color Extended Community attribute for the SRv6 Policy for current Flow Specification. Default value is set to 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ColorCOBitsFlowspec"])
        )

    @property
    def ColorReservedBitsFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Reserved Bits for the Color Extended Communtiy attribute for the SRv6 Policy for current Flow Specification. Default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ColorReservedBitsFlowspec"])
        )

    @property
    def ColorValueFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Value for the Color Extended Communtiy attribute for the SRv6 Policy for current Flow Specification. Default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ColorValueFlowspec"])
        )

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
    def DestPortMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is Destination Port Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestPortMatch"]))

    @property
    def DestPrefixLengthV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination Prefix Length (bits) - Controlled by Enable Destination Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestPrefixLengthV6"])
        )

    @property
    def DestPrefixOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination Prefix Offset (bits) - Controlled by Enable Destination Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestPrefixOffset"])
        )

    @property
    def DestPrefixV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination Prefix - Controlled by Enable Destination Prefix (Pattern is calculated based on length and offset)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestPrefixV6"]))

    @property
    def DscpMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is DSCP Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 10, 10-20, <10, 10&20, 10|20-30&!25|>=50 etc c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DscpMatch"]))

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
    def EnableDestPrefixV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Click to Enable Destination Prefix and Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableDestPrefixV6"])
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
    def EnableLargeCommunities(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Large Communities Attribute
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableLargeCommunities"])
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
    def EnableRedirect(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Redirect
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableRedirect"])
        )

    @property
    def EnableRedirectIPv6NHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Redirect To IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableRedirectIPv6NHop"])
        )

    @property
    def EnableReirectIPv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable RT Redirect-IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableReirectIPv6"])
        )

    @property
    def EnableSourcePrefixV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Click to Enable Source Prefix and Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSourcePrefixV6"])
        )

    @property
    def EnableSrv6SidFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to True, then you can put SRv6 SID value and related informations for the current Flow Specification. Default value is False.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSrv6SidFlowspec"])
        )

    @property
    def EnableTrafficAction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Traffic Action
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableTrafficAction"])
        )

    @property
    def EnableTrafficMarketing(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Traffic Marketing
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableTrafficMarketing"])
        )

    @property
    def EnableTrafficMarking(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Traffic Marking
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableTrafficMarking"])
        )

    @property
    def EnableTrafficRate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to True, the Traffic Rate Packets Column gets enabled. You can configure the Rate of Traffic in packets per second. Default value is False.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableTrafficRate"])
        )

    @property
    def EnableTrafficRatePacket(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to True, the Traffic Rate Bytes Column gets enabled. You can configure the Rate of Traffic in bytes per second. Default value is False.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableTrafficRatePacket"])
        )

    @property
    def FlowLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is Flow Label Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlowLabel"]))

    @property
    def FlowSpecName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flow Spec Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlowSpecName"]))

    @property
    def FragmentMatchV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is fragment match in Flowspec Match Components. Supported Flags: lf,ff,isf join different matchcriteria using | or & join flags using | (bitwise or) Eg. (lf), (lf|ff|isf), (not)(lf|isf), (not|match)(ff)|(isf|lf) Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FragmentMatchV6"])
        )

    @property
    def FunctionLengthFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Function Length of SRv6 SID for the current Flow Specification. Default value is set to 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FunctionLengthFlowspec"])
        )

    @property
    def IcmpCodeMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is ICMP Code Match in Flowspec Match Components. This field takes the string of ICMP Code matching criteria for a flow specification.Supported Formats:a. valueb. value1-value2>value (!, >, <, >=, <= supported)join using | or &Eg. 100, 100-200, <100, 100&200, 100|200-220&!210|>=230 etc.c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IcmpCodeMatch"]))

    @property
    def IcmpTypeMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is ICMP Type Match in Flowspec Match Components. This field takes the string of ICMP Type matching criteria for a flow specification.Supported Formats:a. valueb. value1-value2>value (!, >, <, >=, <= supported)join using | or &Eg. 100, 100-200, <100, 100&200, 100|200-220&!210|>=230 etcc. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IcmpTypeMatch"]))

    @property
    def IncSrv6SidStructSsTlvFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to True, then the SRv6 Sid Structure Sub-Sub-TLV is sent in packet for the current Flow Specification. Default value is False.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IncSrv6SidStructSsTlvFlowspec"]),
        )

    @property
    def Ip(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ip"]))

    @property
    def IpPacketLenMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is IP Packet Length Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpPacketLenMatch"])
        )

    @property
    def IpV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IpV4"]))

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
    def LocBlockLengthFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Block length for SRv6 SID for the current Flow Specification. Default value is set to 40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocBlockLengthFlowspec"])
        )

    @property
    def LocNodeLengthFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Node length for SRv6 SID for the current Flow Specification. Default value is set to 24.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocNodeLengthFlowspec"])
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
    def NextHeader(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is Upper Layer Protocol Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-220&!210|>=230 etc c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NextHeader"]))

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
    def NoOfLargeCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Large Communities (Should be in the range 1-32)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfLargeCommunities"])

    @NoOfLargeCommunities.setter
    def NoOfLargeCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfLargeCommunities"], value)

    @property
    def NumberOfFlows(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Flows in a Flow Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NumberOfFlows"]))

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
    def PortMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is Port Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc c. Keep Empty If Not Requried This Field Matches Source OR Destination TCP/UDP Ports
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortMatch"]))

    @property
    def RedirectCBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RedirectCBit"]))

    @property
    def RedirectCBitIPv6NHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C Bit(IPv6 Next Hop)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RedirectCBitIPv6NHop"])
        )

    @property
    def RedirectExtCommunityType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Extended Community Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RedirectExtCommunityType"])
        )

    @property
    def RedirectIPv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RT Redirect-IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RedirectIPv6"]))

    @property
    def RedirectIPv6NHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redirect To IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RedirectIPv6NHop"])
        )

    @property
    def Redirectnexthop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Redirectnexthop"])
        )

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
    def SourcePortMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is Source Port Match in Flowspec Match Components. Supported Formats: a. value b. value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc c. Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourcePortMatch"])
        )

    @property
    def SourcePrefixLengthV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Prefix Length (bits) - Controlled by Enable Source Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourcePrefixLengthV6"])
        )

    @property
    def SourcePrefixV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Prefix - Controlled by Enable Source Prefix (Pattern is calculated based on length and offset)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourcePrefixV6"])
        )

    @property
    def SrcPrefixOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Prefix Offset (bits) - Controlled by Enable Source Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcPrefixOffset"])
        )

    @property
    def Srv6EndpointBehaviorFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is SRv6 Endpoint Behaviour for the current Flow Specifcation. Default value is set to 0xFFFF.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6EndpointBehaviorFlowspec"])
        )

    @property
    def Srv6SidFlagsFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to specify Sid Flags in SRv6 Service Information SubTLV. Default value is set to 0x00.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidFlagsFlowspec"])
        )

    @property
    def Srv6SidFuncAllocTypeFlowspec(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Func Allocation Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidFuncAllocTypeFlowspec"])
        )

    @property
    def Srv6SidLocFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID. It consists of Locator, Func and Args.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidLocFlowspec"])
        )

    @property
    def Srv6SidReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to specify Reserved value in SRv6 L3 Service TLV. Default value is set to 0x00.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved"])
        )

    @property
    def Srv6SidReserved1Flowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to specify Reserved1 field value in SRv6 Service Information SubTLV. Default value is set to 0x00.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved1Flowspec"])
        )

    @property
    def Srv6SidReserved2Flowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to specify Reserved2 field value in SRv6 Service Information SubTLV. Default value is set to 0x00.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved2Flowspec"])
        )

    @property
    def TcpFlagsMatch(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is TCP Flags Match in Flowspec Match Components. Supported Flags: ns,cwr,ece,urg,ack,psh,rst,syn,fin join different matchcriteria using | or & join flags using | (bitwise or) Eg. (cwr), (ece|urg|psh|syn), (not)(cwr|syn), (not|match)(ece|psh)|(psh|rst)&(not)(ns) Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TcpFlagsMatch"]))

    @property
    def TerminalAction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Terminal Action
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TerminalAction"])
        )

    @property
    def TrafficActionSample(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sample
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrafficActionSample"])
        )

    @property
    def TrafficDscp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSCP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TrafficDscp"]))

    @property
    def TrafficRate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Traffic Rate (Bytes/s)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TrafficRate"]))

    @property
    def TrafficRatePacket(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Traffic Rate (Packets/s)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrafficRatePacket"])
        )

    @property
    def TranspositionLengthFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transposition length for SRv6 SID for the current Flow Specification. Default value is set to 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TranspositionLengthFlowspec"])
        )

    @property
    def TranspositionOffsetFlowspec(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transposition offset for SRv6 SID for the current Flow Specification. Default value is set to 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TranspositionOffsetFlowspec"])
        )

    def update(
        self,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
        NoOfLargeCommunities=None,
    ):
        # type: (str, int, int, int, int, int) -> BgpFlowSpecRangesList
        """Updates bgpFlowSpecRangesList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)

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
        NoOfLargeCommunities=None,
    ):
        # type: (int, str, str, int, int, int, int, int) -> BgpFlowSpecRangesList
        """Finds and retrieves bgpFlowSpecRangesList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpFlowSpecRangesList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpFlowSpecRangesList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)

        Returns
        -------
        - self: This instance with matching bgpFlowSpecRangesList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpFlowSpecRangesList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpFlowSpecRangesList resources from the server available through an iterator or index

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
        ActivateSRv6Policy=None,
        Active=None,
        AggregatorAs=None,
        AggregatorId=None,
        ArgumentLengthFlowspec=None,
        AsNumber2Bytes=None,
        AsNumber4Bytes=None,
        AsSetMode=None,
        AssignedNumber2Bytes=None,
        AssignedNumber4Bytes=None,
        ColorCOBitsFlowspec=None,
        ColorReservedBitsFlowspec=None,
        ColorValueFlowspec=None,
        DestPortMatch=None,
        DestPrefixLengthV6=None,
        DestPrefixOffset=None,
        DestPrefixV6=None,
        DscpMatch=None,
        EnableAggregatorId=None,
        EnableAsPathSegments=None,
        EnableAtomicAggregate=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableDestPrefixV6=None,
        EnableExtendedCommunity=None,
        EnableLargeCommunities=None,
        EnableLocalPreference=None,
        EnableMultiExitDiscriminator=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableRedirect=None,
        EnableRedirectIPv6NHop=None,
        EnableReirectIPv6=None,
        EnableSourcePrefixV6=None,
        EnableSrv6SidFlowspec=None,
        EnableTrafficAction=None,
        EnableTrafficMarketing=None,
        EnableTrafficMarking=None,
        EnableTrafficRate=None,
        EnableTrafficRatePacket=None,
        FlowLabel=None,
        FlowSpecName=None,
        FragmentMatchV6=None,
        FunctionLengthFlowspec=None,
        IcmpCodeMatch=None,
        IcmpTypeMatch=None,
        IncSrv6SidStructSsTlvFlowspec=None,
        Ip=None,
        IpPacketLenMatch=None,
        IpV4=None,
        Ipv4NextHop=None,
        Ipv6NextHop=None,
        LocBlockLengthFlowspec=None,
        LocNodeLengthFlowspec=None,
        LocalPreference=None,
        MultiExitDiscriminator=None,
        NextHeader=None,
        NumberOfFlows=None,
        Origin=None,
        OriginatorId=None,
        OverridePeerAsSetMode=None,
        PortMatch=None,
        RedirectCBit=None,
        RedirectCBitIPv6NHop=None,
        RedirectExtCommunityType=None,
        RedirectIPv6=None,
        RedirectIPv6NHop=None,
        Redirectnexthop=None,
        SetNextHop=None,
        SetNextHopIpType=None,
        SourcePortMatch=None,
        SourcePrefixLengthV6=None,
        SourcePrefixV6=None,
        SrcPrefixOffset=None,
        Srv6EndpointBehaviorFlowspec=None,
        Srv6SidFlagsFlowspec=None,
        Srv6SidFuncAllocTypeFlowspec=None,
        Srv6SidLocFlowspec=None,
        Srv6SidReserved=None,
        Srv6SidReserved1Flowspec=None,
        Srv6SidReserved2Flowspec=None,
        TcpFlagsMatch=None,
        TerminalAction=None,
        TrafficActionSample=None,
        TrafficDscp=None,
        TrafficRate=None,
        TrafficRatePacket=None,
        TranspositionLengthFlowspec=None,
        TranspositionOffsetFlowspec=None,
    ):
        """Base class infrastructure that gets a list of bgpFlowSpecRangesList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActivateSRv6Policy (str): optional regex of activateSRv6Policy
        - Active (str): optional regex of active
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - ArgumentLengthFlowspec (str): optional regex of argumentLengthFlowspec
        - AsNumber2Bytes (str): optional regex of asNumber2Bytes
        - AsNumber4Bytes (str): optional regex of asNumber4Bytes
        - AsSetMode (str): optional regex of asSetMode
        - AssignedNumber2Bytes (str): optional regex of assignedNumber2Bytes
        - AssignedNumber4Bytes (str): optional regex of assignedNumber4Bytes
        - ColorCOBitsFlowspec (str): optional regex of colorCOBitsFlowspec
        - ColorReservedBitsFlowspec (str): optional regex of colorReservedBitsFlowspec
        - ColorValueFlowspec (str): optional regex of colorValueFlowspec
        - DestPortMatch (str): optional regex of destPortMatch
        - DestPrefixLengthV6 (str): optional regex of destPrefixLengthV6
        - DestPrefixOffset (str): optional regex of destPrefixOffset
        - DestPrefixV6 (str): optional regex of destPrefixV6
        - DscpMatch (str): optional regex of dscpMatch
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableDestPrefixV6 (str): optional regex of enableDestPrefixV6
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableLargeCommunities (str): optional regex of enableLargeCommunities
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableRedirect (str): optional regex of enableRedirect
        - EnableRedirectIPv6NHop (str): optional regex of enableRedirectIPv6NHop
        - EnableReirectIPv6 (str): optional regex of enableReirectIPv6
        - EnableSourcePrefixV6 (str): optional regex of enableSourcePrefixV6
        - EnableSrv6SidFlowspec (str): optional regex of enableSrv6SidFlowspec
        - EnableTrafficAction (str): optional regex of enableTrafficAction
        - EnableTrafficMarketing (str): optional regex of enableTrafficMarketing
        - EnableTrafficMarking (str): optional regex of enableTrafficMarking
        - EnableTrafficRate (str): optional regex of enableTrafficRate
        - EnableTrafficRatePacket (str): optional regex of enableTrafficRatePacket
        - FlowLabel (str): optional regex of flowLabel
        - FlowSpecName (str): optional regex of flowSpecName
        - FragmentMatchV6 (str): optional regex of fragmentMatchV6
        - FunctionLengthFlowspec (str): optional regex of functionLengthFlowspec
        - IcmpCodeMatch (str): optional regex of icmpCodeMatch
        - IcmpTypeMatch (str): optional regex of icmpTypeMatch
        - IncSrv6SidStructSsTlvFlowspec (str): optional regex of incSrv6SidStructSsTlvFlowspec
        - Ip (str): optional regex of ip
        - IpPacketLenMatch (str): optional regex of ipPacketLenMatch
        - IpV4 (str): optional regex of ipV4
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LocBlockLengthFlowspec (str): optional regex of locBlockLengthFlowspec
        - LocNodeLengthFlowspec (str): optional regex of locNodeLengthFlowspec
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - NextHeader (str): optional regex of nextHeader
        - NumberOfFlows (str): optional regex of numberOfFlows
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - PortMatch (str): optional regex of portMatch
        - RedirectCBit (str): optional regex of redirectCBit
        - RedirectCBitIPv6NHop (str): optional regex of redirectCBitIPv6NHop
        - RedirectExtCommunityType (str): optional regex of redirectExtCommunityType
        - RedirectIPv6 (str): optional regex of redirectIPv6
        - RedirectIPv6NHop (str): optional regex of redirectIPv6NHop
        - Redirectnexthop (str): optional regex of redirectnexthop
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - SourcePortMatch (str): optional regex of sourcePortMatch
        - SourcePrefixLengthV6 (str): optional regex of sourcePrefixLengthV6
        - SourcePrefixV6 (str): optional regex of sourcePrefixV6
        - SrcPrefixOffset (str): optional regex of srcPrefixOffset
        - Srv6EndpointBehaviorFlowspec (str): optional regex of srv6EndpointBehaviorFlowspec
        - Srv6SidFlagsFlowspec (str): optional regex of srv6SidFlagsFlowspec
        - Srv6SidFuncAllocTypeFlowspec (str): optional regex of srv6SidFuncAllocTypeFlowspec
        - Srv6SidLocFlowspec (str): optional regex of srv6SidLocFlowspec
        - Srv6SidReserved (str): optional regex of srv6SidReserved
        - Srv6SidReserved1Flowspec (str): optional regex of srv6SidReserved1Flowspec
        - Srv6SidReserved2Flowspec (str): optional regex of srv6SidReserved2Flowspec
        - TcpFlagsMatch (str): optional regex of tcpFlagsMatch
        - TerminalAction (str): optional regex of terminalAction
        - TrafficActionSample (str): optional regex of trafficActionSample
        - TrafficDscp (str): optional regex of trafficDscp
        - TrafficRate (str): optional regex of trafficRate
        - TrafficRatePacket (str): optional regex of trafficRatePacket
        - TranspositionLengthFlowspec (str): optional regex of transpositionLengthFlowspec
        - TranspositionOffsetFlowspec (str): optional regex of transpositionOffsetFlowspec

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
