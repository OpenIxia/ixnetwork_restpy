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
from typing import List, Any, Union


class BgpV6IPRouteProperty(Base):
    """BGP+ Non-VPN IPv4/v6 Route Range Properties
    The BgpV6IPRouteProperty class encapsulates a list of bgpV6IPRouteProperty resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpV6IPRouteProperty.find() method.
    The list can be managed by using the BgpV6IPRouteProperty.add() and BgpV6IPRouteProperty.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpV6IPRouteProperty'
    _SDM_ATT_MAP = {
        'OverridePeerAsSetMode': 'OverridePeerAsSetMode',
        'Active': 'active',
        'AddPathId': 'addPathId',
        'AdvertiseAsBGPLSPrefix': 'advertiseAsBGPLSPrefix',
        'AdvertiseAsBgp3107': 'advertiseAsBgp3107',
        'AdvertiseAsBgp3107Sr': 'advertiseAsBgp3107Sr',
        'AdvertiseAsRfc8277': 'advertiseAsRfc8277',
        'AdvertiseAsRfc8277SR': 'advertiseAsRfc8277SR',
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
        'Downtime': 'downtime',
        'EnableAddPath': 'enableAddPath',
        'EnableAggregatorId': 'enableAggregatorId',
        'EnableAigp': 'enableAigp',
        'EnableAsPathSegments': 'enableAsPathSegments',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableExtendedCommunity': 'enableExtendedCommunity',
        'EnableFlapping': 'enableFlapping',
        'EnableLLNextHop': 'enableLLNextHop',
        'EnableLargeCommunities': 'enableLargeCommunities',
        'EnableLocalPreference': 'enableLocalPreference',
        'EnableMultiExitDiscriminator': 'enableMultiExitDiscriminator',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginatorId': 'enableOriginatorId',
        'EnableRandomAsPath': 'enableRandomAsPath',
        'EnableSRGB': 'enableSRGB',
        'EnableWeight': 'enableWeight',
        'FlapFromRouteIndex': 'flapFromRouteIndex',
        'FlapToRouteIndex': 'flapToRouteIndex',
        'IncrementMode': 'incrementMode',
        'Ipv4NextHop': 'ipv4NextHop',
        'Ipv6NextHop': 'ipv6NextHop',
        'LabelEnd': 'labelEnd',
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
        'NoOfLabels': 'noOfLabels',
        'NoOfLargeCommunities': 'noOfLargeCommunities',
        'NoOfSegmentIds': 'noOfSegmentIds',
        'NoOfTlvs': 'noOfTlvs',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'PackingFrom': 'packingFrom',
        'PackingTo': 'packingTo',
        'PartialFlap': 'partialFlap',
        'RouteOrigin': 'routeOrigin',
        'SegmentId': 'segmentId',
        'SendMulticastWithProperSAFI': 'sendMulticastWithProperSAFI',
        'SkipMulticast': 'skipMulticast',
        'SpecialLabel': 'specialLabel',
        'Uptime': 'uptime',
        'UseTraditionalNlri': 'useTraditionalNlri',
        'Weight': 'weight',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(BgpV6IPRouteProperty, self).__init__(parent, list_op)

    @property
    def Bgp8277SRSegmentIdList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgp8277srsegmentidlist_0718aa70c2b1ee20aec9def96e59fdcc.Bgp8277SRSegmentIdList): An instance of the Bgp8277SRSegmentIdList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgp8277srsegmentidlist_0718aa70c2b1ee20aec9def96e59fdcc import Bgp8277SRSegmentIdList
        if self._properties.get('Bgp8277SRSegmentIdList', None) is not None:
            return self._properties.get('Bgp8277SRSegmentIdList')
        else:
            return Bgp8277SRSegmentIdList(self)

    @property
    def Rfc8277LabelStack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.rfc8277labelstack_c6a926d8802154f2012482423beab167.Rfc8277LabelStack): An instance of the Rfc8277LabelStack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.rfc8277labelstack_c6a926d8802154f2012482423beab167 import Rfc8277LabelStack
        if self._properties.get('Rfc8277LabelStack', None) is not None:
            return self._properties.get('Rfc8277LabelStack')
        else:
            return Rfc8277LabelStack(self)

    @property
    def BgpAigpList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpaigplist_b76a0c0926b383c03300a5c9015e1c36.BgpAigpList): An instance of the BgpAigpList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpaigplist_b76a0c0926b383c03300a5c9015e1c36 import BgpAigpList
        if self._properties.get('BgpAigpList', None) is not None:
            return self._properties.get('BgpAigpList')
        else:
            return BgpAigpList(self)

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
        if self._properties.get('BgpAsPathSegmentList', None) is not None:
            return self._properties.get('BgpAsPathSegmentList')
        else:
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
        if self._properties.get('BgpClusterIdList', None) is not None:
            return self._properties.get('BgpClusterIdList')
        else:
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
        if self._properties.get('BgpCommunitiesList', None) is not None:
            return self._properties.get('BgpCommunitiesList')
        else:
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
        if self._properties.get('BgpExtendedCommunitiesList', None) is not None:
            return self._properties.get('BgpExtendedCommunitiesList')
        else:
            return BgpExtendedCommunitiesList(self)

    @property
    def BgpNonVPNRRLargeCommunitiesList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist_11861be5207f57b1a32d83eeb1d62224.BgpNonVPNRRLargeCommunitiesList): An instance of the BgpNonVPNRRLargeCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist_11861be5207f57b1a32d83eeb1d62224 import BgpNonVPNRRLargeCommunitiesList
        if self._properties.get('BgpNonVPNRRLargeCommunitiesList', None) is not None:
            return self._properties.get('BgpNonVPNRRLargeCommunitiesList')
        else:
            return BgpNonVPNRRLargeCommunitiesList(self)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        if self._properties.get('CMacProperties', None) is not None:
            return self._properties.get('CMacProperties')
        else:
            return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        if self._properties.get('EvpnIPv4PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv4PrefixRange')
        else:
            return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        if self._properties.get('EvpnIPv6PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv6PrefixRange')
        else:
            return EvpnIPv6PrefixRange(self)

    @property
    def GenerateIpv6RoutesParams(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.generateipv6routesparams_6a6e5a59a1ed54f9f9343ab3545821c1.GenerateIpv6RoutesParams): An instance of the GenerateIpv6RoutesParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.generateipv6routesparams_6a6e5a59a1ed54f9f9343ab3545821c1 import GenerateIpv6RoutesParams
        if self._properties.get('GenerateIpv6RoutesParams', None) is not None:
            return self._properties.get('GenerateIpv6RoutesParams')
        else:
            return GenerateIpv6RoutesParams(self)._select()

    @property
    def GenerateRoutesParams(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.generateroutesparams_117e1ed7232c32aa1932f4f8d5499699.GenerateRoutesParams): An instance of the GenerateRoutesParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.generateroutesparams_117e1ed7232c32aa1932f4f8d5499699 import GenerateRoutesParams
        if self._properties.get('GenerateRoutesParams', None) is not None:
            return self._properties.get('GenerateRoutesParams')
        else:
            return GenerateRoutesParams(self)._select()

    @property
    def ImportBgpRoutesParams(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.importbgproutesparams_4d60eb735df5bf7c597595458b68aa31.ImportBgpRoutesParams): An instance of the ImportBgpRoutesParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.importbgproutesparams_4d60eb735df5bf7c597595458b68aa31 import ImportBgpRoutesParams
        if self._properties.get('ImportBgpRoutesParams', None) is not None:
            return self._properties.get('ImportBgpRoutesParams')
        else:
            return ImportBgpRoutesParams(self)._select()

    @property
    def OverridePeerAsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverridePeerAsSetMode']))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AddPathId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BGP ADD Path Id
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AddPathId']))

    @property
    def AdvertiseAsBGPLSPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise as BGP-LS Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseAsBGPLSPrefix']))

    @property
    def AdvertiseAsBgp3107(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Will cause this route to be sent as BGP 3107 MPLS SAFI route
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseAsBgp3107'])
    @AdvertiseAsBgp3107.setter
    def AdvertiseAsBgp3107(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseAsBgp3107'], value)

    @property
    def AdvertiseAsBgp3107Sr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseAsBgp3107Sr'])
    @AdvertiseAsBgp3107Sr.setter
    def AdvertiseAsBgp3107Sr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseAsBgp3107Sr'], value)

    @property
    def AdvertiseAsRfc8277(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Will cause this route to be sent as RFC 8277 MPLS SAFI route
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseAsRfc8277'])
    @AdvertiseAsRfc8277.setter
    def AdvertiseAsRfc8277(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseAsRfc8277'], value)

    @property
    def AdvertiseAsRfc8277SR(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Will cause this route to be sent as RFC 8277 MPLS SAFI route
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseAsRfc8277SR'])
    @AdvertiseAsRfc8277SR.setter
    def AdvertiseAsRfc8277SR(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseAsRfc8277SR'], value)

    @property
    def AdvertiseNexthopAsV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Nexthop as V4
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseNexthopAsV4']))

    @property
    def AggregatorAs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Aggregator AS
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorAs']))

    @property
    def AggregatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Aggregator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorId']))

    @property
    def AggregatorIdMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Aggregator ID Mode
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AggregatorIdMode']))

    @property
    def AsNumSuffixRange(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
        """
        from uhd_restpy.multivalue import Multivalue
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
        - obj(uhd_restpy.multivalue.Multivalue): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsPathPerRoute']))

    @property
    def AsRandomSeed(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsRandomSeed']))

    @property
    def AsSegDist(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSegDist']))

    @property
    def AsSetMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from uhd_restpy.multivalue import Multivalue
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
        - obj(uhd_restpy.multivalue.Multivalue): Delay in Seconds
        """
        from uhd_restpy.multivalue import Multivalue
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
    def Downtime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Downtime In Seconds
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Downtime']))

    @property
    def EnableAddPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Path ID when ADD Path Capability is enabled in BGP Peer
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAddPath']))

    @property
    def EnableAggregatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Aggregator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAggregatorId']))

    @property
    def EnableAigp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable AIGP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAigp']))

    @property
    def EnableAsPathSegments(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Non-Random AS Path Segments
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAsPathSegments']))

    @property
    def EnableAtomicAggregate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Atomic Aggregate
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate']))

    @property
    def EnableCluster(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Cluster
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCluster']))

    @property
    def EnableCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCommunity']))

    @property
    def EnableExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExtendedCommunity']))

    @property
    def EnableFlapping(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Flapping
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFlapping']))

    @property
    def EnableLLNextHop(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Link-local address in Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLLNextHop']))

    @property
    def EnableLargeCommunities(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Large Communities Attribute
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLargeCommunities']))

    @property
    def EnableLocalPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Local Preference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLocalPreference']))

    @property
    def EnableMultiExitDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Multi Exit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMultiExitDiscriminator']))

    @property
    def EnableNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNextHop']))

    @property
    def EnableOrigin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOrigin']))

    @property
    def EnableOriginatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Originator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOriginatorId']))

    @property
    def EnableRandomAsPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables generation/advertisement of Random AS Path Segments.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRandomAsPath']))

    @property
    def EnableSRGB(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable SRGB TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSRGB']))

    @property
    def EnableWeight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableWeight']))

    @property
    def FlapFromRouteIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Flap From Route Index
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapFromRouteIndex']))

    @property
    def FlapToRouteIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Flap To Route Index
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapToRouteIndex']))

    @property
    def IncrementMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Either Fixed or Increment
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncrementMode']))

    @property
    def Ipv4NextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NextHop']))

    @property
    def Ipv6NextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NextHop']))

    @property
    def LabelEnd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Range Label End
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelEnd']))

    @property
    def LabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Range Label Start
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStart']))

    @property
    def LabelStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Range Label Step
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStep']))

    @property
    def LocalPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Preference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalPreference']))

    @property
    def MaxASNumPerSegment(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Number Of AS Numbers generated per Segment
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxASNumPerSegment']))

    @property
    def MaxNoOfASPathSegmentsPerRouteRange(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Number Of AS Path Segments Per Route Range.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxNoOfASPathSegmentsPerRouteRange']))

    @property
    def MinASNumPerSegment(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Minimum Number Of AS Numbers generated per Segments.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinASNumPerSegment']))

    @property
    def MinNoOfASPathSegmentsPerRouteRange(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Minimum Number Of AS Path Segments Per Route Range.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinNoOfASPathSegmentsPerRouteRange']))

    @property
    def MultiExitDiscriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Multi Exit
        """
        from uhd_restpy.multivalue import Multivalue
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
        - obj(uhd_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopIPType']))

    @property
    def NextHopIncrementMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Next Hop Increment Mode
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopIncrementMode']))

    @property
    def NextHopType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Set Next Hop
        """
        from uhd_restpy.multivalue import Multivalue
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
    def NoOfLabels(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Labels
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfLabels'])
    @NoOfLabels.setter
    def NoOfLabels(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfLabels'], value)

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
    def NoOfSegmentIds(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Segment Ids
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSegmentIds'])
    @NoOfSegmentIds.setter
    def NoOfSegmentIds(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfSegmentIds'], value)

    @property
    def NoOfTlvs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of TLVs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfTlvs'])
    @NoOfTlvs.setter
    def NoOfTlvs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfTlvs'], value)

    @property
    def Origin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Origin']))

    @property
    def OriginatorId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Originator ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OriginatorId']))

    @property
    def PackingFrom(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Packing From
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PackingFrom']))

    @property
    def PackingTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Packing To
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PackingTo']))

    @property
    def PartialFlap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Partial Flap
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PartialFlap']))

    @property
    def RouteOrigin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteOrigin']))

    @property
    def SegmentId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SID or Segment ID, converts to label value by adding offset into SRGB Start Label Value.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SegmentId']))

    @property
    def SendMulticastWithProperSAFI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Send Routes with SAFI as Multicast (2)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendMulticastWithProperSAFI']))

    @property
    def SkipMulticast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Skip the Multicast routes for this route range
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SkipMulticast']))

    @property
    def SpecialLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If we are emulating Egress then Label field may not hold Label value calculated based on SRGB and Offset but Implicit IPv4 NULL or Explicit NULL
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SpecialLabel']))

    @property
    def Uptime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Uptime In Seconds
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Uptime']))

    @property
    def UseTraditionalNlri(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use Traditional NLRI
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseTraditionalNlri']))

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, AdvertiseAsRfc8277SR=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfLargeCommunities=None, NoOfSegmentIds=None, NoOfTlvs=None):
        # type: (bool, bool, bool, bool, str, int, int, int, int, int, int, int, int) -> BgpV6IPRouteProperty
        """Updates bgpV6IPRouteProperty resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
        - AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
        - AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
        - AdvertiseAsRfc8277SR (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLabels (number): Number of Labels
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - NoOfSegmentIds (number): Number of Segment Ids
        - NoOfTlvs (number): Number of TLVs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, AdvertiseAsRfc8277SR=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfLargeCommunities=None, NoOfSegmentIds=None, NoOfTlvs=None):
        # type: (bool, bool, bool, bool, str, int, int, int, int, int, int, int, int) -> BgpV6IPRouteProperty
        """Adds a new bgpV6IPRouteProperty resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
        - AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
        - AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
        - AdvertiseAsRfc8277SR (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLabels (number): Number of Labels
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - NoOfSegmentIds (number): Number of Segment Ids
        - NoOfTlvs (number): Number of TLVs

        Returns
        -------
        - self: This instance with all currently retrieved bgpV6IPRouteProperty resources using find and the newly added bgpV6IPRouteProperty resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpV6IPRouteProperty resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, AdvertiseAsRfc8277SR=None, AsPathASString=None, Count=None, DescriptiveName=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfLargeCommunities=None, NoOfSegmentIds=None, NoOfTlvs=None):
        # type: (bool, bool, bool, bool, List[str], int, str, str, int, int, int, int, int, int, int, int) -> BgpV6IPRouteProperty
        """Finds and retrieves bgpV6IPRouteProperty resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpV6IPRouteProperty resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpV6IPRouteProperty resources from the server.

        Args
        ----
        - AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
        - AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
        - AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
        - AdvertiseAsRfc8277SR (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
        - AsPathASString (list(str)): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExternalCommunities (number): Number of Extended Communities
        - NoOfLabels (number): Number of Labels
        - NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
        - NoOfSegmentIds (number): Number of Segment Ids
        - NoOfTlvs (number): Number of TLVs

        Returns
        -------
        - self: This instance with matching bgpV6IPRouteProperty resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpV6IPRouteProperty data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpV6IPRouteProperty resources from the server available through an iterator or index

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

    def GenerateIpv6Routes(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the generateIpv6Routes operation on the server.

        Generate Primary and Duplicate Routes with advanced prefix length distribution options.

        DEPRECATED generateIpv6Routes(Arg2=number, Arg3=number, Arg4=number, Arg5=string, Arg6=string, Arg7=enum, Arg8=enum, Arg9=href, Arg10=number, Arg11=number, Arg12=bool, Arg13=bool, Arg14=string, Arg15=string, Arg16=string, async_operation=bool)list
        -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (number): Number of Primary Routes per Device.
        - Arg3 (number): Percentage to Duplicate Primary Routes per Device.
        - Arg4 (number): Number of Routes per Route Range.
        - Arg5 (str): Network Address Start Value.
        - Arg6 (str): Network Address Step Value.
        - Arg7 (str(fixed | random | even | exponential | internet | custom)): Prefix Length Distribution Type.
        - Arg8 (str(perTopology | perDevice | perPort)): Prefix Length Distribution Scope.
        - Arg9 (obj(uhd_restpy.files.Files)): Source file having custom distribution information.
        - Arg10 (number): Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
        - Arg11 (number): Prefix Length End Value. Applicable only for Even and Exponential distribution type.
        - Arg12 (bool): Do not include Loopback Address in the generated Address Range
        - Arg13 (bool): Do not include Multicast Address in the generated Address Range
        - Arg14 (str): Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: aa:0:1:b: - bb:0:2:c:, aa00: - bb00:1
        - Arg15 (str): AS Path Suffix for Primary Routes
        - Arg16 (str): AS Path Suffix for Duplicate Routes
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateIpv6Routes', payload=payload, response_object=None)

    def GenerateRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the generateRoutes operation on the server.

        Generate Primary and Duplicate Routes with advanced prefix length distribution options.

        DEPRECATED generateRoutes(Arg2=enum, Arg3=number, Arg4=number, Arg5=number, Arg6=number, Arg7=string, Arg8=string, Arg9=bool, Arg10=bool, Arg11=enum, Arg12=enum, Arg13=href, Arg14=enum, Arg15=number, Arg16=number, Arg17=string, Arg18=bool, Arg19=bool, Arg20=bool, Arg21=string, Arg22=string, async_operation=bool)list
        -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (str(none)): The replication type of the routes.
        - Arg3 (number): The number of routes you want to generate. Only available, when Route Replication is selected as Per Device.
        - Arg4 (number): Number of Primary Routes per Device.
        - Arg5 (number): Number of Routes per Route Range.
        - Arg6 (number): Percentage to Duplicate Primary Routes per Device.
        - Arg7 (str): Network Address Start Value.
        - Arg8 (str): Network Address Step Value.
        - Arg9 (bool): Include the default route address, 0.0.0.0, in the generated Address Range.
        - Arg10 (bool): DO not include Class E Addresses (240.0.0.0 - 255.255.255.254) in the generated Address Range.
        - Arg11 (str(fixed | random | even | exponential | internet | custom)): Prefix Length Distribution Type.
        - Arg12 (str(perTopology | perDevice | perPort)): Prefix Length Distribution Scope.
        - Arg13 (obj(uhd_restpy.files.Files)): Source file having custom distribution information.
        - Arg14 (str(internetMix | customMix)): The prefix lengths are assigned to the routes in accordance with Internet Prefix Profile.
        - Arg15 (number): Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
        - Arg16 (number): Prefix Length End Value. Applicable only for Even and Exponential distribution type.
        - Arg17 (str): Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: 192.0.0.0 - 192.255.255.255, 201.0.0.0. - 201.255.255.255
        - Arg18 (bool): Do not include Loopback Address in the generated Address Range
        - Arg19 (bool): Do not include Multicast Address in the generated Address Range
        - Arg20 (bool): If selected, Random AS Path is turned on for the route range. Only available, when Route Replication is selected as Per Device.
        - Arg21 (str): AS Path Suffix for Primary Routes
        - Arg22 (str): AS Path Suffix for Duplicate Routes
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateRoutes', payload=payload, response_object=None)

    def ImportBgpRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the importBgpRoutes operation on the server.

        Import IPv4 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        importBgpRoutes(Arg2=enum, Arg3=bool, Arg4=enum, Arg5=enum, Arg6=href, async_operation=bool)list
        ------------------------------------------------------------------------------------------------
        - Arg2 (str(roundRobin | replicate)): Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.
        - Arg3 (bool): Import only the best routes (provided route file has this information).
        - Arg4 (str(overwriteTestersAddress | preserveFromFile)): Option for setting Next Hop modification type.
        - Arg5 (str(csv | juniper | cisco)): Import routes file type. Route import may fail in file type is not matching with the file being imported.
        - Arg6 (obj(uhd_restpy.files.Files)): Select source file having route information.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each asynchronous action invocation.

        DEPRECATED importBgpRoutes(Arg2=enum, Arg3=bool, Arg4=enum, Arg5=enum, Arg6=href, Arg7=number, async_operation=bool)list
        ------------------------------------------------------------------------------------------------------------------------
        - Arg2 (str(roundRobin | replicate)): Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.
        - Arg3 (bool): Import only the best routes (provided route file has this information).
        - Arg4 (str(overwriteTestersAddress | preserveFromFile)): Option for setting Next Hop modification type.
        - Arg5 (str(csv | juniper | cisco)): Import routes file type. Route import may fail in file type is not matching with the file being imported.
        - Arg6 (obj(uhd_restpy.files.Files)): Select source file having route information.
        - Arg7 (number): Specify maximum routes(per port) that you want to import. Based on Card Memory, the Max Route Limit Per Port are: - 4GB or more => 2.0 million 2GB => 1.6 million 1GB => 0.8 million Less than 1GB => 0.5 million
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each asynchronous action invocation.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('importBgpRoutes', payload=payload, response_object=None)

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

    def get_device_ids(self, PortNames=None, OverridePeerAsSetMode=None, Active=None, AddPathId=None, AdvertiseAsBGPLSPrefix=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Delay=None, Downtime=None, EnableAddPath=None, EnableAggregatorId=None, EnableAigp=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLLNextHop=None, EnableLargeCommunities=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSRGB=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncrementMode=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, RouteOrigin=None, SegmentId=None, SendMulticastWithProperSAFI=None, SkipMulticast=None, SpecialLabel=None, Uptime=None, UseTraditionalNlri=None, Weight=None):
        """Base class infrastructure that gets a list of bgpV6IPRouteProperty device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - OverridePeerAsSetMode (str): optional regex of OverridePeerAsSetMode
        - Active (str): optional regex of active
        - AddPathId (str): optional regex of addPathId
        - AdvertiseAsBGPLSPrefix (str): optional regex of advertiseAsBGPLSPrefix
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
        - Downtime (str): optional regex of downtime
        - EnableAddPath (str): optional regex of enableAddPath
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAigp (str): optional regex of enableAigp
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
        - EnableSRGB (str): optional regex of enableSRGB
        - EnableWeight (str): optional regex of enableWeight
        - FlapFromRouteIndex (str): optional regex of flapFromRouteIndex
        - FlapToRouteIndex (str): optional regex of flapToRouteIndex
        - IncrementMode (str): optional regex of incrementMode
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LabelEnd (str): optional regex of labelEnd
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
        - RouteOrigin (str): optional regex of routeOrigin
        - SegmentId (str): optional regex of segmentId
        - SendMulticastWithProperSAFI (str): optional regex of sendMulticastWithProperSAFI
        - SkipMulticast (str): optional regex of skipMulticast
        - SpecialLabel (str): optional regex of specialLabel
        - Uptime (str): optional regex of uptime
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
