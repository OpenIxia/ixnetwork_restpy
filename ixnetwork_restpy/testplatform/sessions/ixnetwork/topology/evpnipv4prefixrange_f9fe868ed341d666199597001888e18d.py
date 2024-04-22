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


class EvpnIPv4PrefixRange(Base):
    """BGP EVPN IPv4 Prefix Range
    The EvpnIPv4PrefixRange class encapsulates a list of evpnIPv4PrefixRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the EvpnIPv4PrefixRange.find() method.
    The list can be managed by using the EvpnIPv4PrefixRange.add() and EvpnIPv4PrefixRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "evpnIPv4PrefixRange"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AdvSrv6SidInIgp": "advSrv6SidInIgp",
        "AdvertiseSRv6SID": "advertiseSRv6SID",
        "AggregatorAs": "aggregatorAs",
        "AggregatorId": "aggregatorId",
        "ArgumentLength": "argumentLength",
        "AsSetMode": "asSetMode",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableAggregatorId": "enableAggregatorId",
        "EnableAsPathSegments": "enableAsPathSegments",
        "EnableAtomicAggregate": "enableAtomicAggregate",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableExtendedCommunity": "enableExtendedCommunity",
        "EnableLocalPreference": "enableLocalPreference",
        "EnableMultiExitDiscriminator": "enableMultiExitDiscriminator",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginatorId": "enableOriginatorId",
        "EnableTransposition": "enableTransposition",
        "FunctionLength": "functionLength",
        "IncSrv6SidStructSsTlv": "incSrv6SidStructSsTlv",
        "Ipv4Address": "ipv4Address",
        "Ipv4NextHop": "ipv4NextHop",
        "Ipv6NextHop": "ipv6NextHop",
        "LabelMode": "labelMode",
        "LabelStart": "labelStart",
        "LabelStep": "labelStep",
        "LocBlockLength": "locBlockLength",
        "LocNodeLength": "locNodeLength",
        "LocalPreference": "localPreference",
        "MultiExitDiscriminator": "multiExitDiscriminator",
        "Name": "name",
        "NoOfASPathSegmentsPerRouteRange": "noOfASPathSegmentsPerRouteRange",
        "NoOfClusters": "noOfClusters",
        "NoOfCommunities": "noOfCommunities",
        "NoOfExtendedCommunity": "noOfExtendedCommunity",
        "Origin": "origin",
        "OriginatorId": "originatorId",
        "OverridePeerAsSetMode": "overridePeerAsSetMode",
        "SendSRv6SIDOptionalInfo": "sendSRv6SIDOptionalInfo",
        "SetNextHop": "setNextHop",
        "SetNextHopIpType": "setNextHopIpType",
        "Srv6EndpointBehavior": "srv6EndpointBehavior",
        "Srv6SIDOptionalInformation": "srv6SIDOptionalInformation",
        "Srv6SidFlags": "srv6SidFlags",
        "Srv6SidLoc": "srv6SidLoc",
        "Srv6SidLocLen": "srv6SidLocLen",
        "Srv6SidLocMetric": "srv6SidLocMetric",
        "Srv6SidReserved": "srv6SidReserved",
        "Srv6SidReserved1": "srv6SidReserved1",
        "Srv6SidReserved2": "srv6SidReserved2",
        "Srv6SidStep": "srv6SidStep",
        "TranspositionLength": "transpositionLength",
        "TranspositionOffset": "transpositionOffset",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EvpnIPv4PrefixRange, self).__init__(parent, list_op)

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
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_ecb45bfaef4008cb27346c98c45748b2.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_ecb45bfaef4008cb27346c98c45748b2 import (
            CMacProperties,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CMacProperties", None) is not None:
                return self._properties.get("CMacProperties")
        return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_f9fe868ed341d666199597001888e18d.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_f9fe868ed341d666199597001888e18d import (
            EvpnIPv4PrefixRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnIPv4PrefixRange", None) is not None:
                return self._properties.get("EvpnIPv4PrefixRange")
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_907e82e321deae422b0ee1ed0f82f2f3.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_907e82e321deae422b0ee1ed0f82f2f3 import (
            EvpnIPv6PrefixRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnIPv6PrefixRange", None) is not None:
                return self._properties.get("EvpnIPv6PrefixRange")
        return EvpnIPv6PrefixRange(self)

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
    def ArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Argument Length for IPV4/IPV6 Prefix Range with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ArgumentLength"])
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
    def EnableTransposition(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, transposition mechanism will be enabled and Srv6 SID will be transposed as per transposition configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableTransposition"])
        )

    @property
    def FunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Function Length for IPV4/IPV6 Prefix Range with Minimum value of 0 , Max value upto 128 bits and default value of 16.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FunctionLength"])
        )

    @property
    def IncSrv6SidStructSsTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it includes the SRv6 SID Structure Sub-Sub TLV into EVPN IPV4/IPV6 Prefix Range for Type 5 Route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncSrv6SidStructSsTlv"])
        )

    @property
    def Ipv4Address(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): IPv4 Address
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Address"])

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
    def LabelMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LabelMode"]))

    @property
    def LabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Start
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LabelStart"]))

    @property
    def LabelStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LabelStep"]))

    @property
    def LocBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Block Length for IPV4/IPV6 Prefix Range with Minimum value of 0 , Max value upto 128 bits and default value of 40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocBlockLength"])
        )

    @property
    def LocNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Node Length for IPV4/IPV6 Prefix Range with Minimum value of 0 , Max value upto 128 bits and default value of 24.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocNodeLength"]))

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
    def Srv6SidStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Range SRv6 SID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidStep"]))

    @property
    def TranspositionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition length for IPV4/IPV6 Prefix Range with Minimum value of 0 , Max value upto 24 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TranspositionLength"])
        )

    @property
    def TranspositionOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition offset for IPV4/IPV6 Prefix Range with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TranspositionOffset"])
        )

    def update(
        self,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
    ):
        # type: (str, int, int, int, int) -> EvpnIPv4PrefixRange
        """Updates evpnIPv4PrefixRange resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
    ):
        # type: (str, int, int, int, int) -> EvpnIPv4PrefixRange
        """Adds a new evpnIPv4PrefixRange resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Returns
        -------
        - self: This instance with all currently retrieved evpnIPv4PrefixRange resources using find and the newly added evpnIPv4PrefixRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained evpnIPv4PrefixRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Ipv4Address=None,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
    ):
        # type: (int, str, List[str], str, int, int, int, int) -> EvpnIPv4PrefixRange
        """Finds and retrieves evpnIPv4PrefixRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve evpnIPv4PrefixRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all evpnIPv4PrefixRange resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Ipv4Address (list(str)): IPv4 Address
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Returns
        -------
        - self: This instance with matching evpnIPv4PrefixRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of evpnIPv4PrefixRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the evpnIPv4PrefixRange resources from the server available through an iterator or index

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

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AdvSrv6SidInIgp=None,
        AdvertiseSRv6SID=None,
        AggregatorAs=None,
        AggregatorId=None,
        ArgumentLength=None,
        AsSetMode=None,
        EnableAggregatorId=None,
        EnableAsPathSegments=None,
        EnableAtomicAggregate=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableExtendedCommunity=None,
        EnableLocalPreference=None,
        EnableMultiExitDiscriminator=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableTransposition=None,
        FunctionLength=None,
        IncSrv6SidStructSsTlv=None,
        Ipv4NextHop=None,
        Ipv6NextHop=None,
        LabelMode=None,
        LabelStart=None,
        LabelStep=None,
        LocBlockLength=None,
        LocNodeLength=None,
        LocalPreference=None,
        MultiExitDiscriminator=None,
        Origin=None,
        OriginatorId=None,
        OverridePeerAsSetMode=None,
        SendSRv6SIDOptionalInfo=None,
        SetNextHop=None,
        SetNextHopIpType=None,
        Srv6EndpointBehavior=None,
        Srv6SIDOptionalInformation=None,
        Srv6SidFlags=None,
        Srv6SidLoc=None,
        Srv6SidLocLen=None,
        Srv6SidLocMetric=None,
        Srv6SidReserved=None,
        Srv6SidReserved1=None,
        Srv6SidReserved2=None,
        Srv6SidStep=None,
        TranspositionLength=None,
        TranspositionOffset=None,
    ):
        """Base class infrastructure that gets a list of evpnIPv4PrefixRange device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
        - AdvertiseSRv6SID (str): optional regex of advertiseSRv6SID
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - ArgumentLength (str): optional regex of argumentLength
        - AsSetMode (str): optional regex of asSetMode
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
        - EnableTransposition (str): optional regex of enableTransposition
        - FunctionLength (str): optional regex of functionLength
        - IncSrv6SidStructSsTlv (str): optional regex of incSrv6SidStructSsTlv
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LabelMode (str): optional regex of labelMode
        - LabelStart (str): optional regex of labelStart
        - LabelStep (str): optional regex of labelStep
        - LocBlockLength (str): optional regex of locBlockLength
        - LocNodeLength (str): optional regex of locNodeLength
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
        - Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
        - Srv6SidFlags (str): optional regex of srv6SidFlags
        - Srv6SidLoc (str): optional regex of srv6SidLoc
        - Srv6SidLocLen (str): optional regex of srv6SidLocLen
        - Srv6SidLocMetric (str): optional regex of srv6SidLocMetric
        - Srv6SidReserved (str): optional regex of srv6SidReserved
        - Srv6SidReserved1 (str): optional regex of srv6SidReserved1
        - Srv6SidReserved2 (str): optional regex of srv6SidReserved2
        - Srv6SidStep (str): optional regex of srv6SidStep
        - TranspositionLength (str): optional regex of transpositionLength
        - TranspositionOffset (str): optional regex of transpositionOffset

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
