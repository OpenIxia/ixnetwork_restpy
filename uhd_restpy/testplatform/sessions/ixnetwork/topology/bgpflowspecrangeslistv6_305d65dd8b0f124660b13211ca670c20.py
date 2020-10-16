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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class BgpFlowSpecRangesListV6(Base):
    """BGP Flow Spec Ranges
    The BgpFlowSpecRangesListV6 class encapsulates a required bgpFlowSpecRangesListV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpFlowSpecRangesListV6'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AggregatorAs': 'aggregatorAs',
        'AggregatorId': 'aggregatorId',
        'AsNumber2Bytes': 'asNumber2Bytes',
        'AsNumber4Bytes': 'asNumber4Bytes',
        'AsSetMode': 'asSetMode',
        'AssignedNumber2Bytes': 'assignedNumber2Bytes',
        'AssignedNumber4Bytes': 'assignedNumber4Bytes',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestPortMatch': 'destPortMatch',
        'DestPrefixLengthV6': 'destPrefixLengthV6',
        'DestPrefixOffset': 'destPrefixOffset',
        'DestPrefixV6': 'destPrefixV6',
        'DscpMatch': 'dscpMatch',
        'EnableAggregatorId': 'enableAggregatorId',
        'EnableAsPathSegments': 'enableAsPathSegments',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableDestPrefixV6': 'enableDestPrefixV6',
        'EnableExtendedCommunity': 'enableExtendedCommunity',
        'EnableLargeCommunities': 'enableLargeCommunities',
        'EnableLocalPreference': 'enableLocalPreference',
        'EnableMultiExitDiscriminator': 'enableMultiExitDiscriminator',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginatorId': 'enableOriginatorId',
        'EnableRedirect': 'enableRedirect',
        'EnableReirectIPv6': 'enableReirectIPv6',
        'EnableSourcePrefixV6': 'enableSourcePrefixV6',
        'EnableTrafficAction': 'enableTrafficAction',
        'EnableTrafficMarketing': 'enableTrafficMarketing',
        'EnableTrafficMarking': 'enableTrafficMarking',
        'EnableTrafficRate': 'enableTrafficRate',
        'FlowLabel': 'flowLabel',
        'FlowSpecName': 'flowSpecName',
        'FragmentMatchV6': 'fragmentMatchV6',
        'IcmpCodeMatch': 'icmpCodeMatch',
        'IcmpTypeMatch': 'icmpTypeMatch',
        'Ip': 'ip',
        'IpPacketLenMatch': 'ipPacketLenMatch',
        'IpV4': 'ipV4',
        'Ipv4NextHop': 'ipv4NextHop',
        'Ipv6NextHop': 'ipv6NextHop',
        'LocalPreference': 'localPreference',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Name': 'name',
        'NextHeader': 'nextHeader',
        'NoOfASPathSegmentsPerRouteRange': 'noOfASPathSegmentsPerRouteRange',
        'NoOfClusters': 'noOfClusters',
        'NoOfCommunities': 'noOfCommunities',
        'NoOfExtendedCommunity': 'noOfExtendedCommunity',
        'NoOfLargeCommunities': 'noOfLargeCommunities',
        'NumberOfFlows': 'numberOfFlows',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'OverridePeerAsSetMode': 'overridePeerAsSetMode',
        'PortMatch': 'portMatch',
        'RedirectCBit': 'redirectCBit',
        'RedirectExtCommunityType': 'redirectExtCommunityType',
        'RedirectIPv6': 'redirectIPv6',
        'Redirectnexthop': 'redirectnexthop',
        'SetNextHop': 'setNextHop',
        'SetNextHopIpType': 'setNextHopIpType',
        'SourcePortMatch': 'sourcePortMatch',
        'SourcePrefixLengthV6': 'sourcePrefixLengthV6',
        'SourcePrefixV6': 'sourcePrefixV6',
        'SrcPrefixOffset': 'srcPrefixOffset',
        'TcpFlagsMatch': 'tcpFlagsMatch',
        'TerminalAction': 'terminalAction',
        'TrafficActionSample': 'trafficActionSample',
        'TrafficDscp': 'trafficDscp',
        'TrafficRate': 'trafficRate',
    }

    def __init__(self, parent):
        super(BgpFlowSpecRangesListV6, self).__init__(parent)

    @property
    def BgpAsPathSegmentList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist_4d209c5ac36c18374125f19531d4795f.BgpAsPathSegmentList): An instance of the BgpAsPathSegmentList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist_4d209c5ac36c18374125f19531d4795f import BgpAsPathSegmentList
        return BgpAsPathSegmentList(self)

    @property
    def BgpClusterIdList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist_82b17094a31a96f755045be572017577.BgpClusterIdList): An instance of the BgpClusterIdList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist_82b17094a31a96f755045be572017577 import BgpClusterIdList
        return BgpClusterIdList(self)

    @property
    def BgpCommunitiesList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist_2963fcaf235bccb665be655ea86cee0f.BgpCommunitiesList): An instance of the BgpCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist_2963fcaf235bccb665be655ea86cee0f import BgpCommunitiesList
        return BgpCommunitiesList(self)

    @property
    def BgpExtendedCommunitiesList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist_bac41900b4999f09d65f045cf8104248.BgpExtendedCommunitiesList): An instance of the BgpExtendedCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist_bac41900b4999f09d65f045cf8104248 import BgpExtendedCommunitiesList
        return BgpExtendedCommunitiesList(self)

    @property
    def BgpLargeCommunitiesList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgplargecommunitieslist_4e8b7e63fdd826da6c354669eb5e3ed0.BgpLargeCommunitiesList): An instance of the BgpLargeCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgplargecommunitieslist_4e8b7e63fdd826da6c354669eb5e3ed0 import BgpLargeCommunitiesList
        return BgpLargeCommunitiesList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AggregatorAs(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Aggregator AS
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorAs']))

    @property
    def AggregatorId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Aggregator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorId']))

    @property
    def AsNumber2Bytes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS 2-Bytes
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumber2Bytes']))

    @property
    def AsNumber4Bytes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS 4-Bytes
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumber4Bytes']))

    @property
    def AsSetMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSetMode']))

    @property
    def AssignedNumber2Bytes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Assigned Number(2 Octets)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumber2Bytes']))

    @property
    def AssignedNumber4Bytes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Assigned Number(4 Octets)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumber4Bytes']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DestPortMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestPortMatch']))

    @property
    def DestPrefixLengthV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination Prefix Length (bits) - Controlled by Enable Destination Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestPrefixLengthV6']))

    @property
    def DestPrefixOffset(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination Prefix Offset (bits) - Controlled by Enable Destination Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestPrefixOffset']))

    @property
    def DestPrefixV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination Prefix - Controlled by Enable Destination Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestPrefixV6']))

    @property
    def DscpMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 10, 10-20, <10, 10&20, 10|20-30&!25|>=50 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DscpMatch']))

    @property
    def EnableAggregatorId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Aggregator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAggregatorId']))

    @property
    def EnableAsPathSegments(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable AS Path Segments
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAsPathSegments']))

    @property
    def EnableAtomicAggregate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Atomic Aggregate
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate']))

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Cluster
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCluster']))

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCommunity']))

    @property
    def EnableDestPrefixV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Click to Enable Destination Prefix and Prefix Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDestPrefixV6']))

    @property
    def EnableExtendedCommunity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExtendedCommunity']))

    @property
    def EnableLargeCommunities(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Large Communities Attribute
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLargeCommunities']))

    @property
    def EnableLocalPreference(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Local Preference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLocalPreference']))

    @property
    def EnableMultiExitDiscriminator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Multi Exit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMultiExitDiscriminator']))

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNextHop']))

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOrigin']))

    @property
    def EnableOriginatorId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Originator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOriginatorId']))

    @property
    def EnableRedirect(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Redirect
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRedirect']))

    @property
    def EnableReirectIPv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Redirect-IPv6
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableReirectIPv6']))

    @property
    def EnableSourcePrefixV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Click to Enable Source Prefix and Prefix Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSourcePrefixV6']))

    @property
    def EnableTrafficAction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Traffic Action
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTrafficAction']))

    @property
    def EnableTrafficMarketing(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Traffic Marketing
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTrafficMarketing']))

    @property
    def EnableTrafficMarking(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Traffic Marking
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTrafficMarking']))

    @property
    def EnableTrafficRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Traffic Rate
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTrafficRate']))

    @property
    def FlowLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlowLabel']))

    @property
    def FlowSpecName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Flow Spec Name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlowSpecName']))

    @property
    def FragmentMatchV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Flags: lf,ff,isf join different matchcriteria using | or & join flags using | (bitwise or) Eg. (lf), (lf|ff|isf), (not)(lf|isf), (not|match)(ff)|(isf|lf) Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FragmentMatchV6']))

    @property
    def IcmpCodeMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-220&!210|>=230 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IcmpCodeMatch']))

    @property
    def IcmpTypeMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-220&!210|>=230 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IcmpTypeMatch']))

    @property
    def Ip(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ip']))

    @property
    def IpPacketLenMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpPacketLenMatch']))

    @property
    def IpV4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpV4']))

    @property
    def Ipv4NextHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NextHop']))

    @property
    def Ipv6NextHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NextHop']))

    @property
    def LocalPreference(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Preference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalPreference']))

    @property
    def MultiExitDiscriminator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Multi Exit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MultiExitDiscriminator']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NextHeader(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-220&!210|>=230 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHeader']))

    @property
    def NoOfASPathSegmentsPerRouteRange(self):
        """
        Returns
        -------
        - number: Number Of AS Path Segments Per Route Range
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfASPathSegmentsPerRouteRange'])
    @NoOfASPathSegmentsPerRouteRange.setter
    def NoOfASPathSegmentsPerRouteRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfASPathSegmentsPerRouteRange'], value)

    @property
    def NoOfClusters(self):
        """
        Returns
        -------
        - number: Number of Clusters
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfClusters'])
    @NoOfClusters.setter
    def NoOfClusters(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfClusters'], value)

    @property
    def NoOfCommunities(self):
        """
        Returns
        -------
        - number: Number of Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCommunities'])
    @NoOfCommunities.setter
    def NoOfCommunities(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfCommunities'], value)

    @property
    def NoOfExtendedCommunity(self):
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfExtendedCommunity'])
    @NoOfExtendedCommunity.setter
    def NoOfExtendedCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfExtendedCommunity'], value)

    @property
    def NoOfLargeCommunities(self):
        """
        Returns
        -------
        - number: Number of Large Communities (Should be in the range 1-32)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfLargeCommunities'])
    @NoOfLargeCommunities.setter
    def NoOfLargeCommunities(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfLargeCommunities'], value)

    @property
    def NumberOfFlows(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of Flows in a Flow Range
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfFlows']))

    @property
    def Origin(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Origin']))

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Originator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OriginatorId']))

    @property
    def OverridePeerAsSetMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverridePeerAsSetMode']))

    @property
    def PortMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc Keep Empty If Not Requried This Field Matches Source OR Destination TCP/UDP Ports
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortMatch']))

    @property
    def RedirectCBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): C Bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedirectCBit']))

    @property
    def RedirectExtCommunityType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Extended Community Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedirectExtCommunityType']))

    @property
    def RedirectIPv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Redirect-IPv6
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedirectIPv6']))

    @property
    def Redirectnexthop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Redirectnexthop']))

    @property
    def SetNextHop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Set Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNextHop']))

    @property
    def SetNextHopIpType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNextHopIpType']))

    @property
    def SourcePortMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 >value (!, >, <, >=, <= supported) join using | or & Eg. 100, 100-200, <100, 100&200, 100|200-300&!250|>=500 etc Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourcePortMatch']))

    @property
    def SourcePrefixLengthV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source Prefix Length (bits) - Controlled by Enable Source Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourcePrefixLengthV6']))

    @property
    def SourcePrefixV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source Prefix - Controlled by Enable Source Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourcePrefixV6']))

    @property
    def SrcPrefixOffset(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source Prefix Offset (bits) - Controlled by Enable Source Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcPrefixOffset']))

    @property
    def TcpFlagsMatch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Flags: ns,cwr,ece,urg,ack,psh,rst,syn,fin join different matchcriteria using | or & join flags using | (bitwise or) Eg. (cwr), (ece|urg|psh|syn), (not)(cwr|syn), (not|match)(ece|psh)|(psh|rst)&(not)(ns) Keep Empty If Not Requried
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TcpFlagsMatch']))

    @property
    def TerminalAction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Terminal Action
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TerminalAction']))

    @property
    def TrafficActionSample(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Sample
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TrafficActionSample']))

    @property
    def TrafficDscp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): DSCP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TrafficDscp']))

    @property
    def TrafficRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Traffic Rate (Bytes/s)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TrafficRate']))

    def update(self, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NoOfLargeCommunities=None):
        """Updates bgpFlowSpecRangesListV6 resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, AggregatorAs=None, AggregatorId=None, AsNumber2Bytes=None, AsNumber4Bytes=None, AsSetMode=None, AssignedNumber2Bytes=None, AssignedNumber4Bytes=None, DestPortMatch=None, DestPrefixLengthV6=None, DestPrefixOffset=None, DestPrefixV6=None, DscpMatch=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableDestPrefixV6=None, EnableExtendedCommunity=None, EnableLargeCommunities=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRedirect=None, EnableReirectIPv6=None, EnableSourcePrefixV6=None, EnableTrafficAction=None, EnableTrafficMarketing=None, EnableTrafficMarking=None, EnableTrafficRate=None, FlowLabel=None, FlowSpecName=None, FragmentMatchV6=None, IcmpCodeMatch=None, IcmpTypeMatch=None, Ip=None, IpPacketLenMatch=None, IpV4=None, Ipv4NextHop=None, Ipv6NextHop=None, LocalPreference=None, MultiExitDiscriminator=None, NextHeader=None, NumberOfFlows=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PortMatch=None, RedirectCBit=None, RedirectExtCommunityType=None, RedirectIPv6=None, Redirectnexthop=None, SetNextHop=None, SetNextHopIpType=None, SourcePortMatch=None, SourcePrefixLengthV6=None, SourcePrefixV6=None, SrcPrefixOffset=None, TcpFlagsMatch=None, TerminalAction=None, TrafficActionSample=None, TrafficDscp=None, TrafficRate=None):
        """Base class infrastructure that gets a list of bgpFlowSpecRangesListV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AsNumber2Bytes (str): optional regex of asNumber2Bytes
        - AsNumber4Bytes (str): optional regex of asNumber4Bytes
        - AsSetMode (str): optional regex of asSetMode
        - AssignedNumber2Bytes (str): optional regex of assignedNumber2Bytes
        - AssignedNumber4Bytes (str): optional regex of assignedNumber4Bytes
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
        - EnableReirectIPv6 (str): optional regex of enableReirectIPv6
        - EnableSourcePrefixV6 (str): optional regex of enableSourcePrefixV6
        - EnableTrafficAction (str): optional regex of enableTrafficAction
        - EnableTrafficMarketing (str): optional regex of enableTrafficMarketing
        - EnableTrafficMarking (str): optional regex of enableTrafficMarking
        - EnableTrafficRate (str): optional regex of enableTrafficRate
        - FlowLabel (str): optional regex of flowLabel
        - FlowSpecName (str): optional regex of flowSpecName
        - FragmentMatchV6 (str): optional regex of fragmentMatchV6
        - IcmpCodeMatch (str): optional regex of icmpCodeMatch
        - IcmpTypeMatch (str): optional regex of icmpTypeMatch
        - Ip (str): optional regex of ip
        - IpPacketLenMatch (str): optional regex of ipPacketLenMatch
        - IpV4 (str): optional regex of ipV4
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - NextHeader (str): optional regex of nextHeader
        - NumberOfFlows (str): optional regex of numberOfFlows
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - PortMatch (str): optional regex of portMatch
        - RedirectCBit (str): optional regex of redirectCBit
        - RedirectExtCommunityType (str): optional regex of redirectExtCommunityType
        - RedirectIPv6 (str): optional regex of redirectIPv6
        - Redirectnexthop (str): optional regex of redirectnexthop
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - SourcePortMatch (str): optional regex of sourcePortMatch
        - SourcePrefixLengthV6 (str): optional regex of sourcePrefixLengthV6
        - SourcePrefixV6 (str): optional regex of sourcePrefixV6
        - SrcPrefixOffset (str): optional regex of srcPrefixOffset
        - TcpFlagsMatch (str): optional regex of tcpFlagsMatch
        - TerminalAction (str): optional regex of terminalAction
        - TrafficActionSample (str): optional regex of trafficActionSample
        - TrafficDscp (str): optional regex of trafficDscp
        - TrafficRate (str): optional regex of trafficRate

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
