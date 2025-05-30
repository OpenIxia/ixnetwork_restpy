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


class CMacProperties(Base):
    """BGP C-MAC Properties
    The CMacProperties class encapsulates a list of cMacProperties resources that are managed by the user.
    A list of resources can be retrieved from the server using the CMacProperties.find() method.
    The list can be managed by using the CMacProperties.add() and CMacProperties.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "cMacProperties"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ActiveTs": "activeTs",
        "AdvSrv6L2SidInIgp": "advSrv6L2SidInIgp",
        "AdvSrv6L3SidInIgp": "advSrv6L3SidInIgp",
        "AdvertiseIpv4Address": "advertiseIpv4Address",
        "AdvertiseIpv6Address": "advertiseIpv6Address",
        "AdvertiseSRv6L2SID": "advertiseSRv6L2SID",
        "AdvertiseSRv6L3SID": "advertiseSRv6L3SID",
        "AggregatorAs": "aggregatorAs",
        "AggregatorId": "aggregatorId",
        "AsSetMode": "asSetMode",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "ETreeLeafLabel": "eTreeLeafLabel",
        "EnableAggregatorId": "enableAggregatorId",
        "EnableAsPathSegments": "enableAsPathSegments",
        "EnableAtomicAggregate": "enableAtomicAggregate",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableETreeExtComm": "enableETreeExtComm",
        "EnableETreeLeafIndication": "enableETreeLeafIndication",
        "EnableExtendedCommunity": "enableExtendedCommunity",
        "EnableLocalPreference": "enableLocalPreference",
        "EnableMultiExitDiscriminator": "enableMultiExitDiscriminator",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginatorId": "enableOriginatorId",
        "EnableSecondLabel": "enableSecondLabel",
        "EnableStickyStaticFlag": "enableStickyStaticFlag",
        "EnableUserDefinedSequenceNumber": "enableUserDefinedSequenceNumber",
        "EviId": "eviId",
        "FirstLabelStart": "firstLabelStart",
        "IncSrv6L2SidStructSsTlv": "incSrv6L2SidStructSsTlv",
        "IncSrv6L3SidStructSsTlv": "incSrv6L3SidStructSsTlv",
        "IncludeDefaultGatewayExtendedCommunity": "includeDefaultGatewayExtendedCommunity",
        "Ipv4AddressPrefixLength": "ipv4AddressPrefixLength",
        "Ipv4NextHop": "ipv4NextHop",
        "Ipv6AddressPrefixLength": "ipv6AddressPrefixLength",
        "Ipv6NextHop": "ipv6NextHop",
        "L2SidArgumentLength": "l2SidArgumentLength",
        "L2SidEnableTransposition": "l2SidEnableTransposition",
        "L2SidFunctionLength": "l2SidFunctionLength",
        "L2SidLocBlockLength": "l2SidLocBlockLength",
        "L2SidLocNodeLength": "l2SidLocNodeLength",
        "L2SidTranpositionLength": "l2SidTranpositionLength",
        "L2SidTranpositionOffset": "l2SidTranpositionOffset",
        "L3SidArgumentLength": "l3SidArgumentLength",
        "L3SidEnableTransposition": "l3SidEnableTransposition",
        "L3SidFunctionLength": "l3SidFunctionLength",
        "L3SidLocBlockLength": "l3SidLocBlockLength",
        "L3SidLocNodeLength": "l3SidLocNodeLength",
        "L3SidTranpositionLength": "l3SidTranpositionLength",
        "L3SidTranpositionOffset": "l3SidTranpositionOffset",
        "LabelMode": "labelMode",
        "LabelStep": "labelStep",
        "LocalPreference": "localPreference",
        "Mac": "mac",
        "MultiExitDiscriminator": "multiExitDiscriminator",
        "Name": "name",
        "NoOfASPathSegmentsPerRouteRange": "noOfASPathSegmentsPerRouteRange",
        "NoOfClusters": "noOfClusters",
        "NoOfCommunities": "noOfCommunities",
        "NoOfExtendedCommunity": "noOfExtendedCommunity",
        "Origin": "origin",
        "OriginatorId": "originatorId",
        "OverridePeerAsSetMode": "overridePeerAsSetMode",
        "PeerAddress": "peerAddress",
        "SecondLabelStart": "secondLabelStart",
        "SendSRv6L3SIDOptionalInfo": "sendSRv6L3SIDOptionalInfo",
        "SendSRv6SIDOptionalInfo": "sendSRv6SIDOptionalInfo",
        "SequenceNumber": "sequenceNumber",
        "SetNextHop": "setNextHop",
        "SetNextHopIpType": "setNextHopIpType",
        "Srv6EndpointBehavior": "srv6EndpointBehavior",
        "Srv6L2SidFlags": "srv6L2SidFlags",
        "Srv6L2SidLoc": "srv6L2SidLoc",
        "Srv6L2SidLocLen": "srv6L2SidLocLen",
        "Srv6L2SidLocMetric": "srv6L2SidLocMetric",
        "Srv6L2SidReserved": "srv6L2SidReserved",
        "Srv6L2SidStep": "srv6L2SidStep",
        "Srv6L3EndpointBehavior": "srv6L3EndpointBehavior",
        "Srv6L3SIDOptionalInformation": "srv6L3SIDOptionalInformation",
        "Srv6L3SidFlags": "srv6L3SidFlags",
        "Srv6L3SidLoc": "srv6L3SidLoc",
        "Srv6L3SidLocLen": "srv6L3SidLocLen",
        "Srv6L3SidLocMetric": "srv6L3SidLocMetric",
        "Srv6L3SidReserved": "srv6L3SidReserved",
        "Srv6L3SidReserved1": "srv6L3SidReserved1",
        "Srv6L3SidReserved2": "srv6L3SidReserved2",
        "Srv6L3SidStep": "srv6L3SidStep",
        "Srv6SIDOptionalInformation": "srv6SIDOptionalInformation",
        "Srv6SidReserved1": "srv6SidReserved1",
        "Srv6SidReserved2": "srv6SidReserved2",
        "UseSameSequenceNumber": "useSameSequenceNumber",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CMacProperties, self).__init__(parent, list_op)

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
    def ActiveTs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Active TS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActiveTs"]))

    @property
    def AdvSrv6L2SidInIgp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 L2 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvSrv6L2SidInIgp"])
        )

    @property
    def AdvSrv6L3SidInIgp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 L3 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvSrv6L3SidInIgp"])
        )

    @property
    def AdvertiseIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv4 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseIpv4Address"])
        )

    @property
    def AdvertiseIpv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseIpv6Address"])
        )

    @property
    def AdvertiseSRv6L2SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSRv6L2SID"])
        )

    @property
    def AdvertiseSRv6L3SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable SRv6 L3 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSRv6L3SID"])
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
    def ETreeLeafLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Leaf Label value for E-Tree Extended Community. Default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ETreeLeafLabel"])
        )

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
    def EnableETreeExtComm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable to configure this MAC Range to act as EVPN E-Tree Leaf Site. This enables E-Tree Extended Community to be sent along with MAC Advertisement. Configuration parameters for this extended community are available only if this is enabled. By default this is false and acts as Root Site.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableETreeExtComm"])
        )

    @property
    def EnableETreeLeafIndication(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables Leaf Indication Bit of E-Tree Extended Community. By default this is true.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableETreeLeafIndication"])
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
    def EnableSecondLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Second Label (L3)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSecondLabel"])
        )

    @property
    def EnableStickyStaticFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Sticky/Static Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableStickyStaticFlag"])
        )

    @property
    def EnableUserDefinedSequenceNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable User Defined Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EnableUserDefinedSequenceNumber"]),
        )

    @property
    def EviId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVI ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EviId"]))

    @property
    def FirstLabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): First Label (L2) Start
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FirstLabelStart"])
        )

    @property
    def IncSrv6L2SidStructSsTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it includes the SRv6 SID Structure Sub-Sub TLV into EVPN L2 SID for Type 2 Route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncSrv6L2SidStructSsTlv"])
        )

    @property
    def IncSrv6L3SidStructSsTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it includes the SRv6 SID Structure Sub-Sub TLV into EVPN L3 SID for Type 2 Route.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncSrv6L3SidStructSsTlv"])
        )

    @property
    def IncludeDefaultGatewayExtendedCommunity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Default Gateway Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IncludeDefaultGatewayExtendedCommunity"]
            ),
        )

    @property
    def Ipv4AddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Address Prefix Length which is used to determine the intersubnetting between local and remote host
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4AddressPrefixLength"])
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
    def Ipv6AddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address Prefix Length which is used to determine the intersubnetting between local and remote host
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6AddressPrefixLength"])
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
    def L2SidArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Argument Length for L2 SID with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidArgumentLength"])
        )

    @property
    def L2SidEnableTransposition(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, transposition mechanism will be enabled and Srv6 SID will be transposed as per transposition configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidEnableTransposition"])
        )

    @property
    def L2SidFunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Function Length for L2 SID with Minimum value of 0 , Max value upto 128 bits and default value of 16.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidFunctionLength"])
        )

    @property
    def L2SidLocBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Block Length for L2 SID with Minimum value of 0 , Max value upto 128 bits and default value of 40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidLocBlockLength"])
        )

    @property
    def L2SidLocNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Node Length for L2 SID with Minimum value of 0 , Max value upto 128 bits and default value of 24.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidLocNodeLength"])
        )

    @property
    def L2SidTranpositionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition length for L2 SID with Minimum value of 0 , Max value upto 24 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidTranpositionLength"])
        )

    @property
    def L2SidTranpositionOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition offset for L2 SID with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SidTranpositionOffset"])
        )

    @property
    def L3SidArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Argument Length for L3 SID with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidArgumentLength"])
        )

    @property
    def L3SidEnableTransposition(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, transposition mechanism will be enabled and Srv6 SID will be transposed as per transposition configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidEnableTransposition"])
        )

    @property
    def L3SidFunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Function Length for L3 SID with Minimum value of 0 , Max value upto 128 bits and default value of 16.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidFunctionLength"])
        )

    @property
    def L3SidLocBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Block Length for L3 SID with Minimum value of 0 , Max value upto 128 bits and default value of 40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidLocBlockLength"])
        )

    @property
    def L3SidLocNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Locator Node Length for L3 SID with Minimum value of 0 , Max value upto 128 bits and default value of 24.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidLocNodeLength"])
        )

    @property
    def L3SidTranpositionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition length for L3 SID with Minimum value of 0 , Max value upto 24 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidTranpositionLength"])
        )

    @property
    def L3SidTranpositionOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the EVPN Transposition offset for L3 SID with Minimum value of 0 , Max value upto 128 bits and default value of 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L3SidTranpositionOffset"])
        )

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
    def Mac(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): MAC addresses of the devices
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mac"])

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
    def PeerAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PeerAddress"]))

    @property
    def SecondLabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Second Label (L3) Start
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SecondLabelStart"])
        )

    @property
    def SendSRv6L3SIDOptionalInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 L3 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendSRv6L3SIDOptionalInfo"])
        )

    @property
    def SendSRv6SIDOptionalInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 L2 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendSRv6SIDOptionalInfo"])
        )

    @property
    def SequenceNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceNumber"])
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6EndpointBehavior"])
        )

    @property
    def Srv6L2SidFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L2SidFlags"])
        )

    @property
    def Srv6L2SidLoc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6L2SidLoc"]))

    @property
    def Srv6L2SidLocLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L2SidLocLen"])
        )

    @property
    def Srv6L2SidLocMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L2SidLocMetric"])
        )

    @property
    def Srv6L2SidReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L2SidReserved"])
        )

    @property
    def Srv6L2SidStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Range SRv6 SID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6L2SidStep"]))

    @property
    def Srv6L3EndpointBehavior(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3EndpointBehavior"])
        )

    @property
    def Srv6L3SIDOptionalInformation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SIDOptionalInformation"])
        )

    @property
    def Srv6L3SidFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidFlags"])
        )

    @property
    def Srv6L3SidLoc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidLoc"]))

    @property
    def Srv6L3SidLocLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidLocLen"])
        )

    @property
    def Srv6L3SidLocMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidLocMetric"])
        )

    @property
    def Srv6L3SidReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidReserved"])
        )

    @property
    def Srv6L3SidReserved1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Reserved1 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidReserved1"])
        )

    @property
    def Srv6L3SidReserved2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidReserved2"])
        )

    @property
    def Srv6L3SidStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Range SRv6 SID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6L3SidStep"]))

    @property
    def Srv6SIDOptionalInformation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SIDOptionalInformation"])
        )

    @property
    def Srv6SidReserved1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Reserved1 Field for Service Information sub-TLV
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidReserved2"])
        )

    @property
    def UseSameSequenceNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Same Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseSameSequenceNumber"])
        )

    def update(
        self,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
    ):
        # type: (str, int, int, int, int) -> CMacProperties
        """Updates cMacProperties resource on the server.

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
        # type: (str, int, int, int, int) -> CMacProperties
        """Adds a new cMacProperties resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Returns
        -------
        - self: This instance with all currently retrieved cMacProperties resources using find and the newly added cMacProperties resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained cMacProperties resources in this instance from the server.

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
        Mac=None,
        Name=None,
        NoOfASPathSegmentsPerRouteRange=None,
        NoOfClusters=None,
        NoOfCommunities=None,
        NoOfExtendedCommunity=None,
    ):
        # type: (int, str, List[str], str, int, int, int, int) -> CMacProperties
        """Finds and retrieves cMacProperties resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cMacProperties resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cMacProperties resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Mac (list(str)): MAC addresses of the devices
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Returns
        -------
        - self: This instance with matching cMacProperties resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cMacProperties data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cMacProperties resources from the server available through an iterator or index

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

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
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

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def ReadvertiseCMac(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the readvertiseCMac operation on the server.

        Readvertise C-MAC

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseCMac(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseCMac(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseCMac(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseCMac(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("readvertiseCMac", payload=payload, response_object=None)

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
        ActiveTs=None,
        AdvSrv6L2SidInIgp=None,
        AdvSrv6L3SidInIgp=None,
        AdvertiseIpv4Address=None,
        AdvertiseIpv6Address=None,
        AdvertiseSRv6L2SID=None,
        AdvertiseSRv6L3SID=None,
        AggregatorAs=None,
        AggregatorId=None,
        AsSetMode=None,
        ETreeLeafLabel=None,
        EnableAggregatorId=None,
        EnableAsPathSegments=None,
        EnableAtomicAggregate=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableETreeExtComm=None,
        EnableETreeLeafIndication=None,
        EnableExtendedCommunity=None,
        EnableLocalPreference=None,
        EnableMultiExitDiscriminator=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableSecondLabel=None,
        EnableStickyStaticFlag=None,
        EnableUserDefinedSequenceNumber=None,
        EviId=None,
        FirstLabelStart=None,
        IncSrv6L2SidStructSsTlv=None,
        IncSrv6L3SidStructSsTlv=None,
        IncludeDefaultGatewayExtendedCommunity=None,
        Ipv4AddressPrefixLength=None,
        Ipv4NextHop=None,
        Ipv6AddressPrefixLength=None,
        Ipv6NextHop=None,
        L2SidArgumentLength=None,
        L2SidEnableTransposition=None,
        L2SidFunctionLength=None,
        L2SidLocBlockLength=None,
        L2SidLocNodeLength=None,
        L2SidTranpositionLength=None,
        L2SidTranpositionOffset=None,
        L3SidArgumentLength=None,
        L3SidEnableTransposition=None,
        L3SidFunctionLength=None,
        L3SidLocBlockLength=None,
        L3SidLocNodeLength=None,
        L3SidTranpositionLength=None,
        L3SidTranpositionOffset=None,
        LabelMode=None,
        LabelStep=None,
        LocalPreference=None,
        MultiExitDiscriminator=None,
        Origin=None,
        OriginatorId=None,
        OverridePeerAsSetMode=None,
        PeerAddress=None,
        SecondLabelStart=None,
        SendSRv6L3SIDOptionalInfo=None,
        SendSRv6SIDOptionalInfo=None,
        SequenceNumber=None,
        SetNextHop=None,
        SetNextHopIpType=None,
        Srv6EndpointBehavior=None,
        Srv6L2SidFlags=None,
        Srv6L2SidLoc=None,
        Srv6L2SidLocLen=None,
        Srv6L2SidLocMetric=None,
        Srv6L2SidReserved=None,
        Srv6L2SidStep=None,
        Srv6L3EndpointBehavior=None,
        Srv6L3SIDOptionalInformation=None,
        Srv6L3SidFlags=None,
        Srv6L3SidLoc=None,
        Srv6L3SidLocLen=None,
        Srv6L3SidLocMetric=None,
        Srv6L3SidReserved=None,
        Srv6L3SidReserved1=None,
        Srv6L3SidReserved2=None,
        Srv6L3SidStep=None,
        Srv6SIDOptionalInformation=None,
        Srv6SidReserved1=None,
        Srv6SidReserved2=None,
        UseSameSequenceNumber=None,
    ):
        """Base class infrastructure that gets a list of cMacProperties device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTs (str): optional regex of activeTs
        - AdvSrv6L2SidInIgp (str): optional regex of advSrv6L2SidInIgp
        - AdvSrv6L3SidInIgp (str): optional regex of advSrv6L3SidInIgp
        - AdvertiseIpv4Address (str): optional regex of advertiseIpv4Address
        - AdvertiseIpv6Address (str): optional regex of advertiseIpv6Address
        - AdvertiseSRv6L2SID (str): optional regex of advertiseSRv6L2SID
        - AdvertiseSRv6L3SID (str): optional regex of advertiseSRv6L3SID
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AsSetMode (str): optional regex of asSetMode
        - ETreeLeafLabel (str): optional regex of eTreeLeafLabel
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableETreeExtComm (str): optional regex of enableETreeExtComm
        - EnableETreeLeafIndication (str): optional regex of enableETreeLeafIndication
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableSecondLabel (str): optional regex of enableSecondLabel
        - EnableStickyStaticFlag (str): optional regex of enableStickyStaticFlag
        - EnableUserDefinedSequenceNumber (str): optional regex of enableUserDefinedSequenceNumber
        - EviId (str): optional regex of eviId
        - FirstLabelStart (str): optional regex of firstLabelStart
        - IncSrv6L2SidStructSsTlv (str): optional regex of incSrv6L2SidStructSsTlv
        - IncSrv6L3SidStructSsTlv (str): optional regex of incSrv6L3SidStructSsTlv
        - IncludeDefaultGatewayExtendedCommunity (str): optional regex of includeDefaultGatewayExtendedCommunity
        - Ipv4AddressPrefixLength (str): optional regex of ipv4AddressPrefixLength
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6AddressPrefixLength (str): optional regex of ipv6AddressPrefixLength
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - L2SidArgumentLength (str): optional regex of l2SidArgumentLength
        - L2SidEnableTransposition (str): optional regex of l2SidEnableTransposition
        - L2SidFunctionLength (str): optional regex of l2SidFunctionLength
        - L2SidLocBlockLength (str): optional regex of l2SidLocBlockLength
        - L2SidLocNodeLength (str): optional regex of l2SidLocNodeLength
        - L2SidTranpositionLength (str): optional regex of l2SidTranpositionLength
        - L2SidTranpositionOffset (str): optional regex of l2SidTranpositionOffset
        - L3SidArgumentLength (str): optional regex of l3SidArgumentLength
        - L3SidEnableTransposition (str): optional regex of l3SidEnableTransposition
        - L3SidFunctionLength (str): optional regex of l3SidFunctionLength
        - L3SidLocBlockLength (str): optional regex of l3SidLocBlockLength
        - L3SidLocNodeLength (str): optional regex of l3SidLocNodeLength
        - L3SidTranpositionLength (str): optional regex of l3SidTranpositionLength
        - L3SidTranpositionOffset (str): optional regex of l3SidTranpositionOffset
        - LabelMode (str): optional regex of labelMode
        - LabelStep (str): optional regex of labelStep
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - PeerAddress (str): optional regex of peerAddress
        - SecondLabelStart (str): optional regex of secondLabelStart
        - SendSRv6L3SIDOptionalInfo (str): optional regex of sendSRv6L3SIDOptionalInfo
        - SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
        - SequenceNumber (str): optional regex of sequenceNumber
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
        - Srv6L2SidFlags (str): optional regex of srv6L2SidFlags
        - Srv6L2SidLoc (str): optional regex of srv6L2SidLoc
        - Srv6L2SidLocLen (str): optional regex of srv6L2SidLocLen
        - Srv6L2SidLocMetric (str): optional regex of srv6L2SidLocMetric
        - Srv6L2SidReserved (str): optional regex of srv6L2SidReserved
        - Srv6L2SidStep (str): optional regex of srv6L2SidStep
        - Srv6L3EndpointBehavior (str): optional regex of srv6L3EndpointBehavior
        - Srv6L3SIDOptionalInformation (str): optional regex of srv6L3SIDOptionalInformation
        - Srv6L3SidFlags (str): optional regex of srv6L3SidFlags
        - Srv6L3SidLoc (str): optional regex of srv6L3SidLoc
        - Srv6L3SidLocLen (str): optional regex of srv6L3SidLocLen
        - Srv6L3SidLocMetric (str): optional regex of srv6L3SidLocMetric
        - Srv6L3SidReserved (str): optional regex of srv6L3SidReserved
        - Srv6L3SidReserved1 (str): optional regex of srv6L3SidReserved1
        - Srv6L3SidReserved2 (str): optional regex of srv6L3SidReserved2
        - Srv6L3SidStep (str): optional regex of srv6L3SidStep
        - Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
        - Srv6SidReserved1 (str): optional regex of srv6SidReserved1
        - Srv6SidReserved2 (str): optional regex of srv6SidReserved2
        - UseSameSequenceNumber (str): optional regex of useSameSequenceNumber

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
