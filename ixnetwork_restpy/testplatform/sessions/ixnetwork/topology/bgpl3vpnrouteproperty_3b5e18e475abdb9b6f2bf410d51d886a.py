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


class BgpL3VpnRouteProperty(Base):
    """BGP L3-VPN Route Range Properties
    The BgpL3VpnRouteProperty class encapsulates a list of bgpL3VpnRouteProperty resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpL3VpnRouteProperty.find() method.
    The list can be managed by using the BgpL3VpnRouteProperty.add() and BgpL3VpnRouteProperty.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpL3VpnRouteProperty'
    _SDM_ATT_MAP = {
        'OverridePeerAsSetMode': 'OverridePeerAsSetMode',
        'Active': 'active',
        'AddPathId': 'addPathId',
        'AdvertiseNexthopAsV4': 'advertiseNexthopAsV4',
        'AggregatorAs': 'aggregatorAs',
        'AggregatorId': 'aggregatorId',
        'AggregatorIdMode': 'aggregatorIdMode',
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
        'EnableAddPath': 'enableAddPath',
        'EnableAggregatorId': 'enableAggregatorId',
        'EnableAsPathSegments': 'enableAsPathSegments',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableExtendedCommunity': 'enableExtendedCommunity',
        'EnableFlapping': 'enableFlapping',
        'EnableIpv4Receiver': 'enableIpv4Receiver',
        'EnableIpv4Sender': 'enableIpv4Sender',
        'EnableLargeCommunities': 'enableLargeCommunities',
        'EnableLocalPreference': 'enableLocalPreference',
        'EnableMultiExitDiscriminator': 'enableMultiExitDiscriminator',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginatorId': 'enableOriginatorId',
        'EnableRandomAsPath': 'enableRandomAsPath',
        'EnableWeight': 'enableWeight',
        'FlapFromRouteIndex': 'flapFromRouteIndex',
        'FlapToRouteIndex': 'flapToRouteIndex',
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
        'Uptime': 'uptime',
        'UseAsIpv4UmhRoutes': 'useAsIpv4UmhRoutes',
        'UseAsUmhRoutes': 'useAsUmhRoutes',
        'UseTraditionalNlri': 'useTraditionalNlri',
        'Weight': 'weight',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(BgpL3VpnRouteProperty, self).__init__(parent, list_op)

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
        if self._properties.get('BgpAsPathSegmentList', None) is not None:
            return self._properties.get('BgpAsPathSegmentList')
        else:
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
        if self._properties.get('BgpClusterIdList', None) is not None:
            return self._properties.get('BgpClusterIdList')
        else:
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
        if self._properties.get('BgpCommunitiesList', None) is not None:
            return self._properties.get('BgpCommunitiesList')
        else:
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
        if self._properties.get('BgpExtendedCommunitiesList', None) is not None:
            return self._properties.get('BgpExtendedCommunitiesList')
        else:
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
        if self._properties.get('BgpNonVPNRRLargeCommunitiesList', None) is not None:
            return self._properties.get('BgpNonVPNRRLargeCommunitiesList')
        else:
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
        if self._properties.get('CMacProperties', None) is not None:
            return self._properties.get('CMacProperties')
        else:
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
        if self._properties.get('EvpnIPv4PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv4PrefixRange')
        else:
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
        if self._properties.get('EvpnIPv6PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv6PrefixRange')
        else:
            return EvpnIPv6PrefixRange(self)

    @property
    def OverridePeerAsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverridePeerAsSetMode']))

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
    def AddPathId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP ADD Path Id for L3VPN Routes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AddPathId']))

    @property
    def AdvertiseNexthopAsV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Nexthop as V4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseNexthopAsV4']))

    @property
    def AggregatorAs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator AS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorAs']))

    @property
    def AggregatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorId']))

    @property
    def AggregatorIdMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator ID Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorIdMode']))

    @property
    def AsNumSuffixRange(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumSuffixRange']))

    @property
    def AsPathASString(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPathASString'])

    @property
    def AsPathPerRoute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsPathPerRoute']))

    @property
    def AsRandomSeed(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsRandomSeed']))

    @property
    def AsSegDist(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSegDist']))

    @property
    def AsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSetMode']))

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
    def Delay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay in Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Delay']))

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
    def DistinguisherAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher AS Number (2-byte or 4-Byte)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherAsNumber']))

    @property
    def DistinguisherAssignedNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherAssignedNumber']))

    @property
    def DistinguisherIpAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherIpAddress']))

    @property
    def DistinguisherType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Distinguisher Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DistinguisherType']))

    @property
    def Downtime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Downtime In Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Downtime']))

    @property
    def EnableAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Path ID when MPLS-VPN ADD Path Capability is enabled in BGP Peer and Add-Path Mode is Send or Both
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAddPath']))

    @property
    def EnableAggregatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAggregatorId']))

    @property
    def EnableAsPathSegments(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Non-Random AS Path Segments
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAsPathSegments']))

    @property
    def EnableAtomicAggregate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Atomic Aggregate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate']))

    @property
    def EnableCluster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Cluster
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCluster']))

    @property
    def EnableCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCommunity']))

    @property
    def EnableExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExtendedCommunity']))

    @property
    def EnableFlapping(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Flapping
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFlapping']))

    @property
    def EnableIpv4Receiver(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable IPv4 Receiver
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv4Receiver'])
    @EnableIpv4Receiver.setter
    def EnableIpv4Receiver(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv4Receiver'], value)

    @property
    def EnableIpv4Sender(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable IPv4 Sender
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv4Sender'])
    @EnableIpv4Sender.setter
    def EnableIpv4Sender(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv4Sender'], value)

    @property
    def EnableLargeCommunities(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Large Communities Attribute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLargeCommunities']))

    @property
    def EnableLocalPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLocalPreference']))

    @property
    def EnableMultiExitDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMultiExitDiscriminator']))

    @property
    def EnableNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNextHop']))

    @property
    def EnableOrigin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOrigin']))

    @property
    def EnableOriginatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOriginatorId']))

    @property
    def EnableRandomAsPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables generation/advertisement of Random AS Path Segments.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRandomAsPath']))

    @property
    def EnableWeight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableWeight']))

    @property
    def FlapFromRouteIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flap From Route Index
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapFromRouteIndex']))

    @property
    def FlapToRouteIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flap To Route Index
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapToRouteIndex']))

    @property
    def IncludeRdInNextHopLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If RD is included in NH Len then NH Len is NH size + RD size else NH len is NH size.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeRdInNextHopLength']))

    @property
    def IncludeSourceAsExtComm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Source AS ExtComm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSourceAsExtComm']))

    @property
    def IncludeVrfRouteImportExtComm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include VRF Route Import ExtComm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeVrfRouteImportExtComm']))

    @property
    def Ipv4NextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NextHop']))

    @property
    def Ipv6NextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NextHop']))

    @property
    def LabelEnd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label End
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelEnd']))

    @property
    def LabelMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelMode']))

    @property
    def LabelSpaceId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Space ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelSpaceId']))

    @property
    def LabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStart']))

    @property
    def LabelStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN RR Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStep']))

    @property
    def LocalPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalPreference']))

    @property
    def MaxASNumPerSegment(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Number Of AS Numbers generated per Segment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxASNumPerSegment']))

    @property
    def MaxNoOfASPathSegmentsPerRouteRange(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Number Of AS Path Segments Per Route Range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxNoOfASPathSegmentsPerRouteRange']))

    @property
    def MinASNumPerSegment(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Number Of AS Numbers generated per Segments.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinASNumPerSegment']))

    @property
    def MinNoOfASPathSegmentsPerRouteRange(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Number Of AS Path Segments Per Route Range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinNoOfASPathSegmentsPerRouteRange']))

    @property
    def MultiExitDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MultiExitDiscriminator']))

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
    def NextHopIPType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopIPType']))

    @property
    def NextHopIncrementMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Hop Increment Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopIncrementMode']))

    @property
    def NextHopType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopType']))

    @property
    def NoOfASPathSegmentsPerRouteRange(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number Of non-random or manually configured AS Path Segments Per Route Range
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfASPathSegmentsPerRouteRange'])
    @NoOfASPathSegmentsPerRouteRange.setter
    def NoOfASPathSegmentsPerRouteRange(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfASPathSegmentsPerRouteRange'], value)

    @property
    def NoOfClusters(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Clusters
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfClusters'])
    @NoOfClusters.setter
    def NoOfClusters(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfClusters'], value)

    @property
    def NoOfCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCommunities'])
    @NoOfCommunities.setter
    def NoOfCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfCommunities'], value)

    @property
    def NoOfExternalCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfExternalCommunities'])
    @NoOfExternalCommunities.setter
    def NoOfExternalCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfExternalCommunities'], value)

    @property
    def NoOfLargeCommunities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Large Communities (Should be in the range 1-32)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfLargeCommunities'])
    @NoOfLargeCommunities.setter
    def NoOfLargeCommunities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfLargeCommunities'], value)

    @property
    def Origin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Origin']))

    @property
    def OriginatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OriginatorId']))

    @property
    def PackingFrom(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packing From
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PackingFrom']))

    @property
    def PackingTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packing To
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PackingTo']))

    @property
    def PartialFlap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Partial Flap
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PartialFlap']))

    @property
    def Uptime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Uptime In Seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Uptime']))

    @property
    def UseAsIpv4UmhRoutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use As IPv4 UMH Routes
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseAsIpv4UmhRoutes'])
    @UseAsIpv4UmhRoutes.setter
    def UseAsIpv4UmhRoutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UseAsIpv4UmhRoutes'], value)

    @property
    def UseAsUmhRoutes(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use As UMH Routes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseAsUmhRoutes']))

    @property
    def UseTraditionalNlri(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Traditional NLRI
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseTraditionalNlri']))

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, EnableIpv4Receiver=None, EnableIpv4Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv4UmhRoutes=None):
        # type: (bool, bool, str, int, int, int, int, int, bool) -> BgpL3VpnRouteProperty
        """Updates bgpL3VpnRouteProperty resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableIpv4Receiver (bool): Enable IPv4 Receiver
        - EnableIpv4Sender (bool): Enable IPv4 Sender
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - UseAsIpv4UmhRoutes (bool): Use As IPv4 UMH Routes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableIpv4Receiver=None, EnableIpv4Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv4UmhRoutes=None):
        # type: (bool, bool, str, int, int, int, int, int, bool) -> BgpL3VpnRouteProperty
        """Adds a new bgpL3VpnRouteProperty resource on the server and adds it to the container.

        Args
        ----
        - EnableIpv4Receiver (bool): Enable IPv4 Receiver
        - EnableIpv4Sender (bool): Enable IPv4 Sender
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - UseAsIpv4UmhRoutes (bool): Use As IPv4 UMH Routes

        Returns
        -------
        - self: This instance with all currently retrieved bgpL3VpnRouteProperty resources using find and the newly added bgpL3VpnRouteProperty resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpL3VpnRouteProperty resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AsPathASString=None, Count=None, DescriptiveName=None, EnableIpv4Receiver=None, EnableIpv4Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv4UmhRoutes=None):
        # type: (List[str], int, str, bool, bool, str, int, int, int, int, int, bool) -> BgpL3VpnRouteProperty
        """Finds and retrieves bgpL3VpnRouteProperty resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpL3VpnRouteProperty resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpL3VpnRouteProperty resources from the server.

        Args
        ----
        - AsPathASString (list(str)): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableIpv4Receiver (bool): Enable IPv4 Receiver
        - EnableIpv4Sender (bool): Enable IPv4 Sender
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - UseAsIpv4UmhRoutes (bool): Use As IPv4 UMH Routes

        Returns
        -------
        - self: This instance with matching bgpL3VpnRouteProperty resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpL3VpnRouteProperty data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpL3VpnRouteProperty resources from the server available through an iterator or index

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

        abort(async_operation=bool)
        ---------------------------
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

    def AgeOutRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ageOutRoutes operation on the server.

        Age out percentage of BGP Routes in a Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ageOutRoutes(Percentage=number, async_operation=bool)
        -----------------------------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ageOutRoutes(Percentage=number, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ageOutRoutes(SessionIndices=string, Percentage=number, async_operation=bool)
        ----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a percentage of type kInteger
        - Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the ageoutroutes operation on the server.

        Completely/Partially age out routes contained in this route range.

        ageoutroutes(Arg2=list, Arg3=number, async_operation=bool)list
        --------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Arg3 (number): What percentage of routes to age out. 100% means all routes.
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
        return self._execute('ageoutroutes', payload=payload, response_object=None)

    def EnableIpv4Receiver(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the enableIpv4Receiver operation on the server.

        Activate or Deactivate Ipv4 Multicast Receiver Site

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableIpv4Receiver(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        enableIpv4Receiver(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        enableIpv4Receiver(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
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
        return self._execute('enableIpv4Receiver', payload=payload, response_object=None)

    def EnableIpv4Sender(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the enableIpv4Sender operation on the server.

        Activate or Deactivate Ipv4 Multicast Sender Site

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableIpv4Sender(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        enableIpv4Sender(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        enableIpv4Sender(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------
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
        return self._execute('enableIpv4Sender', payload=payload, response_object=None)

    def ReadvertiseRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the readvertiseRoutes operation on the server.

        Re-advertise Aged out BGP Routes in a Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseRoutes(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseRoutes(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseRoutes(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
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
        return self._execute('readvertiseRoutes', payload=payload, response_object=None)

    def Readvertiseroutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the readvertiseroutes operation on the server.

        Readvertise only the aged-out routes contained in this route range.

        readvertiseroutes(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute('readvertiseroutes', payload=payload, response_object=None)

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

    def UseAsIpv4UmhRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the useAsIpv4UmhRoutes operation on the server.

        Activate Deactivate Ipv4 UMH Route Selection

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        useAsIpv4UmhRoutes(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        useAsIpv4UmhRoutes(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        useAsIpv4UmhRoutes(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
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
        return self._execute('useAsIpv4UmhRoutes', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, OverridePeerAsSetMode=None, Active=None, AddPathId=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Delay=None, DistinguisherAsNumber=None, DistinguisherAssignedNumber=None, DistinguisherIpAddress=None, DistinguisherType=None, Downtime=None, EnableAddPath=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLargeCommunities=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncludeRdInNextHopLength=None, IncludeSourceAsExtComm=None, IncludeVrfRouteImportExtComm=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelMode=None, LabelSpaceId=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, Uptime=None, UseAsUmhRoutes=None, UseTraditionalNlri=None, Weight=None):
        """Base class infrastructure that gets a list of bgpL3VpnRouteProperty device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - OverridePeerAsSetMode (str): optional regex of OverridePeerAsSetMode
        - Active (str): optional regex of active
        - AddPathId (str): optional regex of addPathId
        - AdvertiseNexthopAsV4 (str): optional regex of advertiseNexthopAsV4
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AggregatorIdMode (str): optional regex of aggregatorIdMode
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
        - EnableAddPath (str): optional regex of enableAddPath
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableFlapping (str): optional regex of enableFlapping
        - EnableLargeCommunities (str): optional regex of enableLargeCommunities
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableRandomAsPath (str): optional regex of enableRandomAsPath
        - EnableWeight (str): optional regex of enableWeight
        - FlapFromRouteIndex (str): optional regex of flapFromRouteIndex
        - FlapToRouteIndex (str): optional regex of flapToRouteIndex
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
