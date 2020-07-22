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


class BgpV6L3VpnRouteProperty(Base):
    """BGP+ L3-VPN Route Range Properties
    The BgpV6L3VpnRouteProperty class encapsulates a list of bgpV6L3VpnRouteProperty resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpV6L3VpnRouteProperty.find() method.
    The list can be managed by using the BgpV6L3VpnRouteProperty.add() and BgpV6L3VpnRouteProperty.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpV6L3VpnRouteProperty'
    _SDM_ATT_MAP = {
        'OverridePeerAsSetMode': 'OverridePeerAsSetMode',
        'Active': 'active',
        'AdvSrv6SidInIgp': 'advSrv6SidInIgp',
        'AdvertiseNexthopAsV4': 'advertiseNexthopAsV4',
        'AggregatorAs': 'aggregatorAs',
        'AggregatorId': 'aggregatorId',
        'AggregatorIdMode': 'aggregatorIdMode',
        'ArgumentLength': 'argumentLength',
        'AsNumSuffixRange': 'asNumSuffixRange',
        'AsPathASString': 'asPathASString',
        'AsPathPerRoute': 'asPathPerRoute',
        'AsRandomSeed': 'asRandomSeed',
        'AsSegDist': 'asSegDist',
        'AsSetMode': 'asSetMode',
        'Count': 'count',
        'Delay': 'delay',
        'DescriptiveName': 'descriptiveName',
        'DistinguisherAsNumber': 'distinguisherAsNumber',
        'DistinguisherAssignedNumber': 'distinguisherAssignedNumber',
        'DistinguisherIpAddress': 'distinguisherIpAddress',
        'DistinguisherType': 'distinguisherType',
        'Downtime': 'downtime',
        'EnableAggregatorId': 'enableAggregatorId',
        'EnableAsPathSegments': 'enableAsPathSegments',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableExtendedCommunity': 'enableExtendedCommunity',
        'EnableFlapping': 'enableFlapping',
        'EnableIpv6Receiver': 'enableIpv6Receiver',
        'EnableIpv6Sender': 'enableIpv6Sender',
        'EnableLLNextHop': 'enableLLNextHop',
        'EnableLargeCommunities': 'enableLargeCommunities',
        'EnableLocalPreference': 'enableLocalPreference',
        'EnableMultiExitDiscriminator': 'enableMultiExitDiscriminator',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginatorId': 'enableOriginatorId',
        'EnableRandomAsPath': 'enableRandomAsPath',
        'EnableSrv6Sid': 'enableSrv6Sid',
        'EnableTransposition': 'enableTransposition',
        'EnableWeight': 'enableWeight',
        'FlapFromRouteIndex': 'flapFromRouteIndex',
        'FlapToRouteIndex': 'flapToRouteIndex',
        'FunctionLength': 'functionLength',
        'IncSrv6SidStructSsTlv': 'incSrv6SidStructSsTlv',
        'IncludeRdInNextHopLength': 'includeRdInNextHopLength',
        'IncludeSourceAsExtComm': 'includeSourceAsExtComm',
        'IncludeVrfRouteImportExtComm': 'includeVrfRouteImportExtComm',
        'Ipv4NextHop': 'ipv4NextHop',
        'Ipv6NextHop': 'ipv6NextHop',
        'LabelEnd': 'labelEnd',
        'LabelMode': 'labelMode',
        'LabelSpaceId': 'labelSpaceId',
        'LabelStart': 'labelStart',
        'LabelStep': 'labelStep',
        'LocBlockLength': 'locBlockLength',
        'LocNodeLength': 'locNodeLength',
        'LocalPreference': 'localPreference',
        'MaxASNumPerSegment': 'maxASNumPerSegment',
        'MaxNoOfASPathSegmentsPerRouteRange': 'maxNoOfASPathSegmentsPerRouteRange',
        'MinASNumPerSegment': 'minASNumPerSegment',
        'MinNoOfASPathSegmentsPerRouteRange': 'minNoOfASPathSegmentsPerRouteRange',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Name': 'name',
        'NextHopIPType': 'nextHopIPType',
        'NextHopIncrementMode': 'nextHopIncrementMode',
        'NextHopType': 'nextHopType',
        'NoOfASPathSegmentsPerRouteRange': 'noOfASPathSegmentsPerRouteRange',
        'NoOfClusters': 'noOfClusters',
        'NoOfCommunities': 'noOfCommunities',
        'NoOfExternalCommunities': 'noOfExternalCommunities',
        'NoOfLargeCommunities': 'noOfLargeCommunities',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'PackingFrom': 'packingFrom',
        'PackingTo': 'packingTo',
        'PartialFlap': 'partialFlap',
        'SendSRv6SIDOptionalInfo': 'sendSRv6SIDOptionalInfo',
        'Srv6EndpointBehavior': 'srv6EndpointBehavior',
        'Srv6SIDOptionalInformation': 'srv6SIDOptionalInformation',
        'Srv6SidFlags': 'srv6SidFlags',
        'Srv6SidFuncAllocType': 'srv6SidFuncAllocType',
        'Srv6SidLoc': 'srv6SidLoc',
        'Srv6SidLocLen': 'srv6SidLocLen',
        'Srv6SidLocMetric': 'srv6SidLocMetric',
        'Srv6SidReserved': 'srv6SidReserved',
        'Srv6SidReserved1': 'srv6SidReserved1',
        'Srv6SidReserved2': 'srv6SidReserved2',
        'Srv6SidStep': 'srv6SidStep',
        'TranspositionAlignment': 'transpositionAlignment',
        'TranspositionLength': 'transpositionLength',
        'TranspositionMode': 'transpositionMode',
        'TranspositionOffset': 'transpositionOffset',
        'Uptime': 'uptime',
        'UseAsIpv6UmhRoutes': 'useAsIpv6UmhRoutes',
        'UseAsUmhRoutes': 'useAsUmhRoutes',
        'UseTraditionalNlri': 'useTraditionalNlri',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(BgpV6L3VpnRouteProperty, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist_4d209c5ac36c18374125f19531d4795f import BgpAsPathSegmentList
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist_82b17094a31a96f755045be572017577 import BgpClusterIdList
        return BgpClusterIdList(self)

    @property
    def BgpCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist_2963fcaf235bccb665be655ea86cee0f.BgpCommunitiesList): An instance of the BgpCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist_2963fcaf235bccb665be655ea86cee0f import BgpCommunitiesList
        return BgpCommunitiesList(self)

    @property
    def BgpExtendedCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist_bac41900b4999f09d65f045cf8104248.BgpExtendedCommunitiesList): An instance of the BgpExtendedCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist_bac41900b4999f09d65f045cf8104248 import BgpExtendedCommunitiesList
        return BgpExtendedCommunitiesList(self)

    @property
    def BgpNonVPNRRLargeCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist_11861be5207f57b1a32d83eeb1d62224.BgpNonVPNRRLargeCommunitiesList): An instance of the BgpNonVPNRRLargeCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist_11861be5207f57b1a32d83eeb1d62224 import BgpNonVPNRRLargeCommunitiesList
        return BgpNonVPNRRLargeCommunitiesList(self)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        return EvpnIPv6PrefixRange(self)

    @property
    def OverridePeerAsSetMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverridePeerAsSetMode']))

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvSrv6SidInIgp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID Locator in IGP (ISIS)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvSrv6SidInIgp']))

    @property
    def AdvertiseNexthopAsV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Nexthop as V4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseNexthopAsV4']))

    @property
    def AggregatorAs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator AS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorAs']))

    @property
    def AggregatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorId']))

    @property
    def AggregatorIdMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator ID Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorIdMode']))

    @property
    def ArgumentLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Argument Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLength']))

    @property
    def AsNumSuffixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumSuffixRange']))

    @property
    def AsPathASString(self):
        """
        Returns
        -------
        - list(str): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPathASString'])

    @property
    def AsPathPerRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsPathPerRoute']))

    @property
    def AsRandomSeed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsRandomSeed']))

    @property
    def AsSegDist(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSegDist']))

    @property
    def AsSetMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSetMode']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def Delay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay in Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Delay']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DistinguisherAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher AS Number (2-byte or 4-Byte)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherAsNumber']))

    @property
    def DistinguisherAssignedNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumber']))

    @property
    def DistinguisherIpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherIpAddress']))

    @property
    def DistinguisherType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherType']))

    @property
    def Downtime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Downtime In Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Downtime']))

    @property
    def EnableAggregatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAggregatorId']))

    @property
    def EnableAsPathSegments(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Non-Random AS Path Segments
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAsPathSegments']))

    @property
    def EnableAtomicAggregate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Atomic Aggregate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate']))

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Cluster
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCluster']))

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCommunity']))

    @property
    def EnableExtendedCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExtendedCommunity']))

    @property
    def EnableFlapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Flapping
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFlapping']))

    @property
    def EnableIpv6Receiver(self):
        """
        Returns
        -------
        - bool: Enable IPv6 Receiver
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv6Receiver'])
    @EnableIpv6Receiver.setter
    def EnableIpv6Receiver(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv6Receiver'], value)

    @property
    def EnableIpv6Sender(self):
        """
        Returns
        -------
        - bool: Enable IPv6 Sender
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv6Sender'])
    @EnableIpv6Sender.setter
    def EnableIpv6Sender(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv6Sender'], value)

    @property
    def EnableLLNextHop(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Link-local address in Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLLNextHop']))

    @property
    def EnableLargeCommunities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Large Communities Attribute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLargeCommunities']))

    @property
    def EnableLocalPreference(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLocalPreference']))

    @property
    def EnableMultiExitDiscriminator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMultiExitDiscriminator']))

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNextHop']))

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOrigin']))

    @property
    def EnableOriginatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOriginatorId']))

    @property
    def EnableRandomAsPath(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables generation/advertisement of Random AS Path Segments.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRandomAsPath']))

    @property
    def EnableSrv6Sid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable SRv6 SID With VPN Route
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSrv6Sid']))

    @property
    def EnableTransposition(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Transposition
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTransposition']))

    @property
    def EnableWeight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableWeight']))

    @property
    def FlapFromRouteIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flap From Route Index
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapFromRouteIndex']))

    @property
    def FlapToRouteIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flap To Route Index
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapToRouteIndex']))

    @property
    def FunctionLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Function Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLength']))

    @property
    def IncSrv6SidStructSsTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include SRv6 SID Structure Sub-Sub TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncSrv6SidStructSsTlv']))

    @property
    def IncludeRdInNextHopLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If RD is included in NH Len then NH Len is NH size + RD size else NH len is NH size.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeRdInNextHopLength']))

    @property
    def IncludeSourceAsExtComm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Source AS ExtComm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSourceAsExtComm']))

    @property
    def IncludeVrfRouteImportExtComm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include VRF Route Import ExtComm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeVrfRouteImportExtComm']))

    @property
    def Ipv4NextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NextHop']))

    @property
    def Ipv6NextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NextHop']))

    @property
    def LabelEnd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label End
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelEnd']))

    @property
    def LabelMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelMode']))

    @property
    def LabelSpaceId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Space ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelSpaceId']))

    @property
    def LabelStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStart']))

    @property
    def LabelStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStep']))

    @property
    def LocBlockLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Block Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocBlockLength']))

    @property
    def LocNodeLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Node Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocNodeLength']))

    @property
    def LocalPreference(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalPreference']))

    @property
    def MaxASNumPerSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Number Of AS Numbers generated per Segment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxASNumPerSegment']))

    @property
    def MaxNoOfASPathSegmentsPerRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Number Of AS Path Segments Per Route Range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxNoOfASPathSegmentsPerRouteRange']))

    @property
    def MinASNumPerSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Number Of AS Numbers generated per Segments.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinASNumPerSegment']))

    @property
    def MinNoOfASPathSegmentsPerRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Number Of AS Path Segments Per Route Range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinNoOfASPathSegmentsPerRouteRange']))

    @property
    def MultiExitDiscriminator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue
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
    def NextHopIPType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopIPType']))

    @property
    def NextHopIncrementMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Hop Increment Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopIncrementMode']))

    @property
    def NextHopType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopType']))

    @property
    def NoOfASPathSegmentsPerRouteRange(self):
        """
        Returns
        -------
        - number: Number Of non-random or manually configured AS Path Segments Per Route Range
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
    def NoOfExternalCommunities(self):
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfExternalCommunities'])
    @NoOfExternalCommunities.setter
    def NoOfExternalCommunities(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfExternalCommunities'], value)

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
    def Origin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Origin']))

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OriginatorId']))

    @property
    def PackingFrom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packing From
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PackingFrom']))

    @property
    def PackingTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packing To
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PackingTo']))

    @property
    def PartialFlap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Partial Flap
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PartialFlap']))

    @property
    def SendSRv6SIDOptionalInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendSRv6SIDOptionalInfo']))

    @property
    def Srv6EndpointBehavior(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6EndpointBehavior']))

    @property
    def Srv6SIDOptionalInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SIDOptionalInformation']))

    @property
    def Srv6SidFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Flags field Value for all route in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidFlags']))

    @property
    def Srv6SidFuncAllocType(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Func Allocation Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidFuncAllocType']))

    @property
    def Srv6SidLoc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLoc']))

    @property
    def Srv6SidLocLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Length to be advertised in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocLen']))

    @property
    def Srv6SidLocMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Metric for advertisement in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocMetric']))

    @property
    def Srv6SidReserved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved']))

    @property
    def Srv6SidReserved1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved1 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved1']))

    @property
    def Srv6SidReserved2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidReserved2']))

    @property
    def Srv6SidStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Range SRv6 SID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidStep']))

    @property
    def TranspositionAlignment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transposition Alignment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TranspositionAlignment']))

    @property
    def TranspositionLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transposition Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TranspositionLength']))

    @property
    def TranspositionMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transposition Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TranspositionMode']))

    @property
    def TranspositionOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transposition Offset
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TranspositionOffset']))

    @property
    def Uptime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Uptime In Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Uptime']))

    @property
    def UseAsIpv6UmhRoutes(self):
        """
        Returns
        -------
        - bool: Use As IPv6 UMH Routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseAsIpv6UmhRoutes'])
    @UseAsIpv6UmhRoutes.setter
    def UseAsIpv6UmhRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseAsIpv6UmhRoutes'], value)

    @property
    def UseAsUmhRoutes(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use As UMH Routes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseAsUmhRoutes']))

    @property
    def UseTraditionalNlri(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Traditional NLRI
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseTraditionalNlri']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, EnableIpv6Receiver=None, EnableIpv6Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv6UmhRoutes=None):
        """Updates bgpV6L3VpnRouteProperty resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableIpv6Receiver (bool): Enable IPv6 Receiver
        - EnableIpv6Sender (bool): Enable IPv6 Sender
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableIpv6Receiver=None, EnableIpv6Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv6UmhRoutes=None):
        """Adds a new bgpV6L3VpnRouteProperty resource on the server and adds it to the container.

        Args
        ----
        - EnableIpv6Receiver (bool): Enable IPv6 Receiver
        - EnableIpv6Sender (bool): Enable IPv6 Sender
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

        Returns
        -------
        - self: This instance with all currently retrieved bgpV6L3VpnRouteProperty resources using find and the newly added bgpV6L3VpnRouteProperty resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpV6L3VpnRouteProperty resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AsPathASString=None, Count=None, DescriptiveName=None, EnableIpv6Receiver=None, EnableIpv6Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv6UmhRoutes=None):
        """Finds and retrieves bgpV6L3VpnRouteProperty resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpV6L3VpnRouteProperty resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpV6L3VpnRouteProperty resources from the server.

        Args
        ----
        - AsPathASString (list(str)): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EnableIpv6Receiver (bool): Enable IPv6 Receiver
        - EnableIpv6Sender (bool): Enable IPv6 Sender
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

        Returns
        -------
        - self: This instance with matching bgpV6L3VpnRouteProperty resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpV6L3VpnRouteProperty data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpV6L3VpnRouteProperty resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, OverridePeerAsSetMode=None, Active=None, AdvSrv6SidInIgp=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, ArgumentLength=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Delay=None, DistinguisherAsNumber=None, DistinguisherAssignedNumber=None, DistinguisherIpAddress=None, DistinguisherType=None, Downtime=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLLNextHop=None, EnableLargeCommunities=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSrv6Sid=None, EnableTransposition=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, FunctionLength=None, IncSrv6SidStructSsTlv=None, IncludeRdInNextHopLength=None, IncludeSourceAsExtComm=None, IncludeVrfRouteImportExtComm=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelMode=None, LabelSpaceId=None, LabelStart=None, LabelStep=None, LocBlockLength=None, LocNodeLength=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, SendSRv6SIDOptionalInfo=None, Srv6EndpointBehavior=None, Srv6SIDOptionalInformation=None, Srv6SidFlags=None, Srv6SidFuncAllocType=None, Srv6SidLoc=None, Srv6SidLocLen=None, Srv6SidLocMetric=None, Srv6SidReserved=None, Srv6SidReserved1=None, Srv6SidReserved2=None, Srv6SidStep=None, TranspositionAlignment=None, TranspositionLength=None, TranspositionMode=None, TranspositionOffset=None, Uptime=None, UseAsUmhRoutes=None, UseTraditionalNlri=None, Weight=None):
        """Base class infrastructure that gets a list of bgpV6L3VpnRouteProperty device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - OverridePeerAsSetMode (str): optional regex of OverridePeerAsSetMode
        - Active (str): optional regex of active
        - AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
        - AdvertiseNexthopAsV4 (str): optional regex of advertiseNexthopAsV4
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AggregatorIdMode (str): optional regex of aggregatorIdMode
        - ArgumentLength (str): optional regex of argumentLength
        - AsNumSuffixRange (str): optional regex of asNumSuffixRange
        - AsPathPerRoute (str): optional regex of asPathPerRoute
        - AsRandomSeed (str): optional regex of asRandomSeed
        - AsSegDist (str): optional regex of asSegDist
        - AsSetMode (str): optional regex of asSetMode
        - Delay (str): optional regex of delay
        - DistinguisherAsNumber (str): optional regex of distinguisherAsNumber
        - DistinguisherAssignedNumber (str): optional regex of distinguisherAssignedNumber
        - DistinguisherIpAddress (str): optional regex of distinguisherIpAddress
        - DistinguisherType (str): optional regex of distinguisherType
        - Downtime (str): optional regex of downtime
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableFlapping (str): optional regex of enableFlapping
        - EnableLLNextHop (str): optional regex of enableLLNextHop
        - EnableLargeCommunities (str): optional regex of enableLargeCommunities
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableRandomAsPath (str): optional regex of enableRandomAsPath
        - EnableSrv6Sid (str): optional regex of enableSrv6Sid
        - EnableTransposition (str): optional regex of enableTransposition
        - EnableWeight (str): optional regex of enableWeight
        - FlapFromRouteIndex (str): optional regex of flapFromRouteIndex
        - FlapToRouteIndex (str): optional regex of flapToRouteIndex
        - FunctionLength (str): optional regex of functionLength
        - IncSrv6SidStructSsTlv (str): optional regex of incSrv6SidStructSsTlv
        - IncludeRdInNextHopLength (str): optional regex of includeRdInNextHopLength
        - IncludeSourceAsExtComm (str): optional regex of includeSourceAsExtComm
        - IncludeVrfRouteImportExtComm (str): optional regex of includeVrfRouteImportExtComm
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LabelEnd (str): optional regex of labelEnd
        - LabelMode (str): optional regex of labelMode
        - LabelSpaceId (str): optional regex of labelSpaceId
        - LabelStart (str): optional regex of labelStart
        - LabelStep (str): optional regex of labelStep
        - LocBlockLength (str): optional regex of locBlockLength
        - LocNodeLength (str): optional regex of locNodeLength
        - LocalPreference (str): optional regex of localPreference
        - MaxASNumPerSegment (str): optional regex of maxASNumPerSegment
        - MaxNoOfASPathSegmentsPerRouteRange (str): optional regex of maxNoOfASPathSegmentsPerRouteRange
        - MinASNumPerSegment (str): optional regex of minASNumPerSegment
        - MinNoOfASPathSegmentsPerRouteRange (str): optional regex of minNoOfASPathSegmentsPerRouteRange
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - NextHopIPType (str): optional regex of nextHopIPType
        - NextHopIncrementMode (str): optional regex of nextHopIncrementMode
        - NextHopType (str): optional regex of nextHopType
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - PackingFrom (str): optional regex of packingFrom
        - PackingTo (str): optional regex of packingTo
        - PartialFlap (str): optional regex of partialFlap
        - SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
        - Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
        - Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
        - Srv6SidFlags (str): optional regex of srv6SidFlags
        - Srv6SidFuncAllocType (str): optional regex of srv6SidFuncAllocType
        - Srv6SidLoc (str): optional regex of srv6SidLoc
        - Srv6SidLocLen (str): optional regex of srv6SidLocLen
        - Srv6SidLocMetric (str): optional regex of srv6SidLocMetric
        - Srv6SidReserved (str): optional regex of srv6SidReserved
        - Srv6SidReserved1 (str): optional regex of srv6SidReserved1
        - Srv6SidReserved2 (str): optional regex of srv6SidReserved2
        - Srv6SidStep (str): optional regex of srv6SidStep
        - TranspositionAlignment (str): optional regex of transpositionAlignment
        - TranspositionLength (str): optional regex of transpositionLength
        - TranspositionMode (str): optional regex of transpositionMode
        - TranspositionOffset (str): optional regex of transpositionOffset
        - Uptime (str): optional regex of uptime
        - UseAsUmhRoutes (str): optional regex of useAsUmhRoutes
        - UseTraditionalNlri (str): optional regex of useTraditionalNlri
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def AgeOutRoutes(self, *args, **kwargs):
        """Executes the ageOutRoutes operation on the server.

        Age out percentage of BGP Routes in a Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ageOutRoutes(Percentage=number)
        -------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger

        ageOutRoutes(Percentage=number, SessionIndices=list)
        ----------------------------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        ageOutRoutes(SessionIndices=string, Percentage=number)
        ------------------------------------------------------
        - SessionIndices (str): This parameter requires a percentage of type kInteger
        - Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ageOutRoutes', payload=payload, response_object=None)

    def Ageoutroutes(self, *args, **kwargs):
        """Executes the ageoutroutes operation on the server.

        Completely/Partially age out routes contained in this route range.

        ageoutroutes(Arg2=list, Arg3=number)list
        ----------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Arg3 (number): What percentage of routes to age out. 100% means all routes.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ageoutroutes', payload=payload, response_object=None)

    def EnableIpv4Receiver(self, *args, **kwargs):
        """Executes the enableIpv4Receiver operation on the server.

        Activate or Deactivate Ipv4 Multicast Receiver Site

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableIpv4Receiver(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        enableIpv4Receiver(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableIpv4Receiver', payload=payload, response_object=None)

    def EnableIpv4Sender(self, *args, **kwargs):
        """Executes the enableIpv4Sender operation on the server.

        Activate or Deactivate Ipv4 Multicast Sender Site

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableIpv4Sender(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        enableIpv4Sender(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableIpv4Sender', payload=payload, response_object=None)

    def EnableIpv6Receiver(self, *args, **kwargs):
        """Executes the enableIpv6Receiver operation on the server.

        Activate or Deactivate Ipv6 Multicast Receiver Site

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableIpv6Receiver(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        enableIpv6Receiver(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableIpv6Receiver', payload=payload, response_object=None)

    def EnableIpv6Sender(self, *args, **kwargs):
        """Executes the enableIpv6Sender operation on the server.

        Activate or Deactivate Ipv6 Multicast Sender Site

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableIpv6Sender(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        enableIpv6Sender(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableIpv6Sender', payload=payload, response_object=None)

    def ReadvertiseRoutes(self, *args, **kwargs):
        """Executes the readvertiseRoutes operation on the server.

        Re-advertise Aged out BGP Routes in a Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseRoutes(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        readvertiseRoutes(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('readvertiseRoutes', payload=payload, response_object=None)

    def Readvertiseroutes(self, *args, **kwargs):
        """Executes the readvertiseroutes operation on the server.

        Readvertise only the aged-out routes contained in this route range.

        readvertiseroutes(Arg2=list)list
        --------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('readvertiseroutes', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

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
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def UseAsIpv4UmhRoutes(self, *args, **kwargs):
        """Executes the useAsIpv4UmhRoutes operation on the server.

        Activate Deactivate Ipv4 UMH Route Selection

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        useAsIpv4UmhRoutes(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        useAsIpv4UmhRoutes(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('useAsIpv4UmhRoutes', payload=payload, response_object=None)

    def UseAsIpv6UmhRoutes(self, *args, **kwargs):
        """Executes the useAsIpv6UmhRoutes operation on the server.

        Activate Deactivate Ipv6 UMH Route Selection

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        useAsIpv6UmhRoutes(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        useAsIpv6UmhRoutes(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('useAsIpv6UmhRoutes', payload=payload, response_object=None)
