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


class BgpEthernetSegmentV4(Base):
    """BGP V4 Ethernet Segment Configuration
    The BgpEthernetSegmentV4 class encapsulates a required bgpEthernetSegmentV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpEthernetSegmentV4'
    _SDM_ATT_MAP = {
        'AdvertiseAliasingBeforeAdPerEsRoute': 'AdvertiseAliasingBeforeAdPerEsRoute',
        'AdvertiseInclusiveMulticastRoute': 'AdvertiseInclusiveMulticastRoute',
        'AliasingRouteGranularity': 'AliasingRouteGranularity',
        'Active': 'active',
        'AdvertiseAliasingAutomatically': 'advertiseAliasingAutomatically',
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
        'IrbIPv4Address': 'irbIPv4Address',
        'IrbInterfaceLabel': 'irbInterfaceLabel',
        'LocalPreference': 'localPreference',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Name': 'name',
        'NoOfASPathSegmentsPerRouteRange': 'noOfASPathSegmentsPerRouteRange',
        'NoOfClusters': 'noOfClusters',
        'NoOfCommunities': 'noOfCommunities',
        'NoOfExtendedCommunity': 'noOfExtendedCommunity',
        'NoOfbMacMappedIpsV4': 'noOfbMacMappedIpsV4',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'OverridePeerAsSetMode': 'overridePeerAsSetMode',
        'RouterMacAddress': 'routerMacAddress',
        'SetNextHop': 'setNextHop',
        'SetNextHopIpType': 'setNextHopIpType',
        'SupportFastConvergence': 'supportFastConvergence',
        'SupportMultihomedEsAutoDiscovery': 'supportMultihomedEsAutoDiscovery',
        'UseControlWord': 'useControlWord',
        'UseSameSequenceNumber': 'useSameSequenceNumber',
        'VtepIpv4Address': 'vtepIpv4Address',
    }

    def __init__(self, parent):
        super(BgpEthernetSegmentV4, self).__init__(parent)

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
    def Bgpv4BMacMappedIpList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpv4bmacmappediplist_9ea54e6390e4283600c8840153ae453b.Bgpv4BMacMappedIpList): An instance of the Bgpv4BMacMappedIpList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpv4bmacmappediplist_9ea54e6390e4283600c8840153ae453b import Bgpv4BMacMappedIpList
        return Bgpv4BMacMappedIpList(self)._select()

    @property
    def AdvertiseAliasingBeforeAdPerEsRoute(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Aliasing Before A-D/ES Route
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseAliasingBeforeAdPerEsRoute']))

    @property
    def AdvertiseInclusiveMulticastRoute(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Support Inclusive Multicast Ethernet Tag Route (RT Type 3)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseInclusiveMulticastRoute']))

    @property
    def AliasingRouteGranularity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Aliasing Route Granularity
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AliasingRouteGranularity']))

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
    def AdvertiseAliasingAutomatically(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Aliasing Automatically
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseAliasingAutomatically']))

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
    def AsSetMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsSetMode']))

    @property
    def AutoConfigureEsImport(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Auto Configure ES-Import
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoConfigureEsImport']))

    @property
    def BMacPrefix(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-MAC Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BMacPrefix']))

    @property
    def BMacPrefixLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-MAC Prefix Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BMacPrefixLength']))

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
    def DfElectionTimer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): DF Election Timer(s)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DfElectionTimer']))

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
    def EnableExtendedCommunity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExtendedCommunity']))

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
    def EnableSingleActive(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Single-Active
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSingleActive']))

    @property
    def EnableStickyStaticFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable B-MAC Sticky/Static Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableStickyStaticFlag']))

    @property
    def EsImport(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): ES Import
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsImport']))

    @property
    def EsiLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): ESI Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsiLabel']))

    @property
    def EsiType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): ESI Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsiType']))

    @property
    def EsiValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): ESI Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EsiValue']))

    @property
    def EvisCount(self):
        """
        Returns
        -------
        - number: Number of EVIs
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvisCount'])
    @EvisCount.setter
    def EvisCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvisCount'], value)

    @property
    def IncludeMacMobilityExtendedCommunity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include MAC Mobility Extended Community
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMacMobilityExtendedCommunity']))

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
    def IrbIPv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IRB IP Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IrbIPv4Address']))

    @property
    def IrbInterfaceLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Label to be used for Route Type 2 carrying IRB MAC and/or IRB IP in Route Type 2
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IrbInterfaceLabel']))

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
    def NoOfbMacMappedIpsV4(self):
        """
        Returns
        -------
        - number: Number of B-MAC Mapped IPs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfbMacMappedIpsV4'])
    @NoOfbMacMappedIpsV4.setter
    def NoOfbMacMappedIpsV4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfbMacMappedIpsV4'], value)

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
    def RouterMacAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Router's MAC Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterMacAddress']))

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
    def SupportFastConvergence(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Support Fast Convergence
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportFastConvergence']))

    @property
    def SupportMultihomedEsAutoDiscovery(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Support Multi-homed ES Auto Discovery
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportMultihomedEsAutoDiscovery']))

    @property
    def UseControlWord(self):
        """
        Returns
        -------
        - bool: Use Control Word
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseControlWord'])
    @UseControlWord.setter
    def UseControlWord(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseControlWord'], value)

    @property
    def UseSameSequenceNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use B-MAC Same Sequence Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseSameSequenceNumber']))

    @property
    def VtepIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VTEP IP Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VtepIpv4Address']))

    def update(self, EvisCount=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NoOfbMacMappedIpsV4=None, UseControlWord=None):
        """Updates bgpEthernetSegmentV4 resource on the server.

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
        - NoOfbMacMappedIpsV4 (number): Number of B-MAC Mapped IPs
        - UseControlWord (bool): Use Control Word

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, AdvertiseAliasingBeforeAdPerEsRoute=None, AdvertiseInclusiveMulticastRoute=None, AliasingRouteGranularity=None, Active=None, AdvertiseAliasingAutomatically=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigureEsImport=None, BMacPrefix=None, BMacPrefixLength=None, DfElectionTimer=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableSingleActive=None, EnableStickyStaticFlag=None, EsImport=None, EsiLabel=None, EsiType=None, EsiValue=None, IncludeMacMobilityExtendedCommunity=None, Ipv4NextHop=None, Ipv6NextHop=None, IrbIPv4Address=None, IrbInterfaceLabel=None, LocalPreference=None, MultiExitDiscriminator=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, RouterMacAddress=None, SetNextHop=None, SetNextHopIpType=None, SupportFastConvergence=None, SupportMultihomedEsAutoDiscovery=None, UseSameSequenceNumber=None, VtepIpv4Address=None):
        """Base class infrastructure that gets a list of bgpEthernetSegmentV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AdvertiseAliasingBeforeAdPerEsRoute (str): optional regex of AdvertiseAliasingBeforeAdPerEsRoute
        - AdvertiseInclusiveMulticastRoute (str): optional regex of AdvertiseInclusiveMulticastRoute
        - AliasingRouteGranularity (str): optional regex of AliasingRouteGranularity
        - Active (str): optional regex of active
        - AdvertiseAliasingAutomatically (str): optional regex of advertiseAliasingAutomatically
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
        - IrbIPv4Address (str): optional regex of irbIPv4Address
        - IrbInterfaceLabel (str): optional regex of irbInterfaceLabel
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - RouterMacAddress (str): optional regex of routerMacAddress
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - SupportFastConvergence (str): optional regex of supportFastConvergence
        - SupportMultihomedEsAutoDiscovery (str): optional regex of supportMultihomedEsAutoDiscovery
        - UseSameSequenceNumber (str): optional regex of useSameSequenceNumber
        - VtepIpv4Address (str): optional regex of vtepIpv4Address

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def AdvertiseAdPerEsRoute(self, *args, **kwargs):
        """Executes the advertiseAdPerEsRoute operation on the server.

        Advertise AD per ES Route.

        advertiseAdPerEsRoute(Arg2=list)list
        ------------------------------------
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
        return self._execute('advertiseAdPerEsRoute', payload=payload, response_object=None)

    def FlushRemoteCMACForwardingTable(self, *args, **kwargs):
        """Executes the flushRemoteCMACForwardingTable operation on the server.

        Flush Remote CMAC Forwarding Table

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        flushRemoteCMACForwardingTable(SessionIndices=list)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        flushRemoteCMACForwardingTable(SessionIndices=string)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        flushRemoteCMACForwardingTable(Arg2=list)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        """Executes the withdrawAdPerEsRoute operation on the server.

        Withdraw AD per ES Route.

        withdrawAdPerEsRoute(Arg2=list)list
        -----------------------------------
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
        return self._execute('withdrawAdPerEsRoute', payload=payload, response_object=None)
