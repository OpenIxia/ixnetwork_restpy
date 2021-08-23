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


class BgpEthernetSegmentV6(Base):
    """BGP V6 Ethernet Segment Configuration
    The BgpEthernetSegmentV6 class encapsulates a required bgpEthernetSegmentV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpEthernetSegmentV6'
    _SDM_ATT_MAP = {
        'AdvertiseAliasingBeforeAdPerEsRoute': 'AdvertiseAliasingBeforeAdPerEsRoute',
        'AdvertiseInclusiveMulticastRoute': 'AdvertiseInclusiveMulticastRoute',
        'AliasingRouteGranularity': 'AliasingRouteGranularity',
        'Active': 'active',
        'AdvertiseAliasingAutomatically': 'advertiseAliasingAutomatically',
        'AdvertiseSRv6ESIFilteringSID': 'advertiseSRv6ESIFilteringSID',
        'AggregatorAs': 'aggregatorAs',
        'AggregatorId': 'aggregatorId',
        'AsSetMode': 'asSetMode',
        'AutoConfigureEsImport': 'autoConfigureEsImport',
        'BMacPrefix': 'bMacPrefix',
        'BMacPrefixLength': 'bMacPrefixLength',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DfElectionTimer': 'dfElectionTimer',
        'EnableAggregatorId': 'enableAggregatorId',
        'EnableAsPathSegments': 'enableAsPathSegments',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableExtendedCommunity': 'enableExtendedCommunity',
        'EnableLocalPreference': 'enableLocalPreference',
        'EnableMultiExitDiscriminator': 'enableMultiExitDiscriminator',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginatorId': 'enableOriginatorId',
        'EnableSingleActive': 'enableSingleActive',
        'EnableStickyStaticFlag': 'enableStickyStaticFlag',
        'EsImport': 'esImport',
        'EsiLabel': 'esiLabel',
        'EsiType': 'esiType',
        'EsiValue': 'esiValue',
        'EvisCount': 'evisCount',
        'IncludeMacMobilityExtendedCommunity': 'includeMacMobilityExtendedCommunity',
        'Ipv4NextHop': 'ipv4NextHop',
        'Ipv6NextHop': 'ipv6NextHop',
        'IrbIPv6Address': 'irbIPv6Address',
        'IrbInterfaceLabel': 'irbInterfaceLabel',
        'LocalPreference': 'localPreference',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Name': 'name',
        'NoOfASPathSegmentsPerRouteRange': 'noOfASPathSegmentsPerRouteRange',
        'NoOfClusters': 'noOfClusters',
        'NoOfCommunities': 'noOfCommunities',
        'NoOfExtendedCommunity': 'noOfExtendedCommunity',
        'NoOfbMacMappedIpsV6': 'noOfbMacMappedIpsV6',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'OverridePeerAsSetMode': 'overridePeerAsSetMode',
        'RouterMacAddress': 'routerMacAddress',
        'SetNextHop': 'setNextHop',
        'SetNextHopIpType': 'setNextHopIpType',
        'Srv6Sid': 'srv6Sid',
        'SupportFastConvergence': 'supportFastConvergence',
        'SupportMultihomedEsAutoDiscovery': 'supportMultihomedEsAutoDiscovery',
        'UseControlWord': 'useControlWord',
        'UseSameSequenceNumber': 'useSameSequenceNumber',
        'VTEPIP6Address': 'vTEPIP6Address',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(BgpEthernetSegmentV6, self).__init__(parent, list_op)

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
    def Bgpv6BMacMappedIpList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6bmacmappediplist_817eaa9cef28501f557db118314de575.Bgpv6BMacMappedIpList): An instance of the Bgpv6BMacMappedIpList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6bmacmappediplist_817eaa9cef28501f557db118314de575 import Bgpv6BMacMappedIpList
        if self._properties.get('Bgpv6BMacMappedIpList', None) is not None:
            return self._properties.get('Bgpv6BMacMappedIpList')
        else:
            return Bgpv6BMacMappedIpList(self)._select()

    @property
    def AdvertiseAliasingBeforeAdPerEsRoute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Aliasing Before A-D/ES Route
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseAliasingBeforeAdPerEsRoute']))

    @property
    def AdvertiseInclusiveMulticastRoute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Inclusive Multicast Ethernet Tag Route (RT Type 3)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseInclusiveMulticastRoute']))

    @property
    def AliasingRouteGranularity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aliasing Route Granularity
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AliasingRouteGranularity']))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvertiseAliasingAutomatically(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Aliasing Automatically
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseAliasingAutomatically']))

    @property
    def AdvertiseSRv6ESIFilteringSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 ESI Filtering SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseSRv6ESIFilteringSID']))

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
    def AutoConfigureEsImport(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Configure ES-Import
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoConfigureEsImport']))

    @property
    def BMacPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-MAC Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BMacPrefix']))

    @property
    def BMacPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-MAC Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BMacPrefixLength']))

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
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DfElectionTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DF Election Timer(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DfElectionTimer']))

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AS Path Segments
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
    def EnableSingleActive(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Single-Active
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSingleActive']))

    @property
    def EnableStickyStaticFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable B-MAC Sticky/Static Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableStickyStaticFlag']))

    @property
    def EsImport(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ES Import
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsImport']))

    @property
    def EsiLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ESI Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsiLabel']))

    @property
    def EsiType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ESI Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsiType']))

    @property
    def EsiValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ESI Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsiValue']))

    @property
    def EvisCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of EVIs
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvisCount'])
    @EvisCount.setter
    def EvisCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EvisCount'], value)

    @property
    def IncludeMacMobilityExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include MAC Mobility Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMacMobilityExtendedCommunity']))

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
    def IrbIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IRB IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IrbIPv6Address']))

    @property
    def IrbInterfaceLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label to be used for Route Type 2 carrying IRB MAC and/or IRB IP in Route Type 2
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IrbInterfaceLabel']))

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
    def NoOfASPathSegmentsPerRouteRange(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number Of AS Path Segments Per Route Range
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
    def NoOfExtendedCommunity(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfExtendedCommunity'])
    @NoOfExtendedCommunity.setter
    def NoOfExtendedCommunity(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfExtendedCommunity'], value)

    @property
    def NoOfbMacMappedIpsV6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of B-MAC Mapped IPs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfbMacMappedIpsV6'])
    @NoOfbMacMappedIpsV6.setter
    def NoOfbMacMappedIpsV6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfbMacMappedIpsV6'], value)

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
    def RouterMacAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router's MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterMacAddress']))

    @property
    def SetNextHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNextHop']))

    @property
    def SetNextHopIpType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNextHopIpType']))

    @property
    def Srv6Sid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6Sid']))

    @property
    def SupportFastConvergence(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Fast Convergence
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportFastConvergence']))

    @property
    def SupportMultihomedEsAutoDiscovery(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Multi-homed ES Auto Discovery
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportMultihomedEsAutoDiscovery']))

    @property
    def UseControlWord(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use Control Word
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseControlWord'])
    @UseControlWord.setter
    def UseControlWord(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UseControlWord'], value)

    @property
    def UseSameSequenceNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use B-MAC Same Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseSameSequenceNumber']))

    @property
    def VTEPIP6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VTEP IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VTEPIP6Address']))

    def update(self, EvisCount=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NoOfbMacMappedIpsV6=None, UseControlWord=None):
        # type: (int, str, int, int, int, int, int, bool) -> BgpEthernetSegmentV6
        """Updates bgpEthernetSegmentV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EvisCount (number): Number of EVIs
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities
        - NoOfbMacMappedIpsV6 (number): Number of B-MAC Mapped IPs
        - UseControlWord (bool): Use Control Word

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def AdvertiseAdPerEsRoute(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the advertiseAdPerEsRoute operation on the server.

        Advertise AD per ES Route.

        advertiseAdPerEsRoute(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
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
        return self._execute('advertiseAdPerEsRoute', payload=payload, response_object=None)

    def FlushRemoteCMACForwardingTable(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the flushRemoteCMACForwardingTable operation on the server.

        Flush Remote CMAC Forwarding Table

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        flushRemoteCMACForwardingTable(async_operation=bool)
        ----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        flushRemoteCMACForwardingTable(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        flushRemoteCMACForwardingTable(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        flushRemoteCMACForwardingTable(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('flushRemoteCMACForwardingTable', payload=payload, response_object=None)

    def WithdrawAdPerEsRoute(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the withdrawAdPerEsRoute operation on the server.

        Withdraw AD per ES Route.

        withdrawAdPerEsRoute(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
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
        return self._execute('withdrawAdPerEsRoute', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, AdvertiseAliasingBeforeAdPerEsRoute=None, AdvertiseInclusiveMulticastRoute=None, AliasingRouteGranularity=None, Active=None, AdvertiseAliasingAutomatically=None, AdvertiseSRv6ESIFilteringSID=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigureEsImport=None, BMacPrefix=None, BMacPrefixLength=None, DfElectionTimer=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableSingleActive=None, EnableStickyStaticFlag=None, EsImport=None, EsiLabel=None, EsiType=None, EsiValue=None, IncludeMacMobilityExtendedCommunity=None, Ipv4NextHop=None, Ipv6NextHop=None, IrbIPv6Address=None, IrbInterfaceLabel=None, LocalPreference=None, MultiExitDiscriminator=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, RouterMacAddress=None, SetNextHop=None, SetNextHopIpType=None, Srv6Sid=None, SupportFastConvergence=None, SupportMultihomedEsAutoDiscovery=None, UseSameSequenceNumber=None, VTEPIP6Address=None):
        """Base class infrastructure that gets a list of bgpEthernetSegmentV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AdvertiseAliasingBeforeAdPerEsRoute (str): optional regex of AdvertiseAliasingBeforeAdPerEsRoute
        - AdvertiseInclusiveMulticastRoute (str): optional regex of AdvertiseInclusiveMulticastRoute
        - AliasingRouteGranularity (str): optional regex of AliasingRouteGranularity
        - Active (str): optional regex of active
        - AdvertiseAliasingAutomatically (str): optional regex of advertiseAliasingAutomatically
        - AdvertiseSRv6ESIFilteringSID (str): optional regex of advertiseSRv6ESIFilteringSID
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AsSetMode (str): optional regex of asSetMode
        - AutoConfigureEsImport (str): optional regex of autoConfigureEsImport
        - BMacPrefix (str): optional regex of bMacPrefix
        - BMacPrefixLength (str): optional regex of bMacPrefixLength
        - DfElectionTimer (str): optional regex of dfElectionTimer
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableSingleActive (str): optional regex of enableSingleActive
        - EnableStickyStaticFlag (str): optional regex of enableStickyStaticFlag
        - EsImport (str): optional regex of esImport
        - EsiLabel (str): optional regex of esiLabel
        - EsiType (str): optional regex of esiType
        - EsiValue (str): optional regex of esiValue
        - IncludeMacMobilityExtendedCommunity (str): optional regex of includeMacMobilityExtendedCommunity
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - IrbIPv6Address (str): optional regex of irbIPv6Address
        - IrbInterfaceLabel (str): optional regex of irbInterfaceLabel
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - RouterMacAddress (str): optional regex of routerMacAddress
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - Srv6Sid (str): optional regex of srv6Sid
        - SupportFastConvergence (str): optional regex of supportFastConvergence
        - SupportMultihomedEsAutoDiscovery (str): optional regex of supportMultihomedEsAutoDiscovery
        - UseSameSequenceNumber (str): optional regex of useSameSequenceNumber
        - VTEPIP6Address (str): optional regex of vTEPIP6Address

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
