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


class RouteRange(Base):
    """Configures a route item, with attributes, to be associated with BGP neighbors.
    The RouteRange class encapsulates a list of routeRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the RouteRange.find() method.
    The list can be managed by using the RouteRange.add() and RouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "routeRange"
    _SDM_ATT_MAP = {
        "AdvertiseNextHopAsV4": "advertiseNextHopAsV4",
        "AggregatorAsNum": "aggregatorAsNum",
        "AggregatorIpAddress": "aggregatorIpAddress",
        "AsPathSetMode": "asPathSetMode",
        "EnableAggregator": "enableAggregator",
        "EnableAggregatorIdIncrementMode": "enableAggregatorIdIncrementMode",
        "EnableAsPath": "enableAsPath",
        "EnableAtomicAttribute": "enableAtomicAttribute",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableGenerateUniqueRoutes": "enableGenerateUniqueRoutes",
        "EnableIncludeLoopback": "enableIncludeLoopback",
        "EnableIncludeMulticast": "enableIncludeMulticast",
        "EnableLocalPref": "enableLocalPref",
        "EnableMed": "enableMed",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginatorId": "enableOriginatorId",
        "EnableProperSafi": "enableProperSafi",
        "EnableTraditionalNlriUpdate": "enableTraditionalNlriUpdate",
        "Enabled": "enabled",
        "EndOfRib": "endOfRib",
        "FromPacking": "fromPacking",
        "FromPrefix": "fromPrefix",
        "IpType": "ipType",
        "IterationStep": "iterationStep",
        "LocalPref": "localPref",
        "Med": "med",
        "NetworkAddress": "networkAddress",
        "NextHopIpAddress": "nextHopIpAddress",
        "NextHopIpType": "nextHopIpType",
        "NextHopMode": "nextHopMode",
        "NextHopSetMode": "nextHopSetMode",
        "NumRoutes": "numRoutes",
        "OriginProtocol": "originProtocol",
        "OriginatorId": "originatorId",
        "ThruPacking": "thruPacking",
        "ThruPrefix": "thruPrefix",
    }
    _SDM_ENUM_MAP = {
        "asPathSetMode": [
            "noInclude",
            "includeAsSeq",
            "includeAsSet",
            "includeAsSeqConf",
            "includeAsSetConf",
            "prependAs",
        ],
        "ipType": ["ipAny", "ipv4", "ipv6"],
        "nextHopIpType": ["ipAny", "ipv4", "ipv6"],
        "nextHopMode": ["fixed", "nextHopIncrement", "incrementPerPrefix"],
        "nextHopSetMode": ["setManually", "sameAsLocalIp"],
        "originProtocol": ["igp", "egp", "incomplete"],
    }

    def __init__(self, parent, list_op=False):
        super(RouteRange, self).__init__(parent, list_op)

    @property
    def AsSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_25ab3214c0c84c6c786d9e2b3d4cdf0e.AsSegment): An instance of the AsSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_25ab3214c0c84c6c786d9e2b3d4cdf0e import (
            AsSegment,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AsSegment", None) is not None:
                return self._properties.get("AsSegment")
        return AsSegment(self)._select()

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_68bd2583b0e1823a0ae210f6a0c8d70c.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_68bd2583b0e1823a0ae210f6a0c8d70c import (
            Cluster,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Cluster", None) is not None:
                return self._properties.get("Cluster")
        return Cluster(self)._select()

    @property
    def Community(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_95636df7171c99766f0e15bfbccad02d.Community): An instance of the Community class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_95636df7171c99766f0e15bfbccad02d import (
            Community,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Community", None) is not None:
                return self._properties.get("Community")
        return Community(self)._select()

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_1dea3b4b2127a9e11303811fee71411b.ExtendedCommunity): An instance of the ExtendedCommunity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_1dea3b4b2127a9e11303811fee71411b import (
            ExtendedCommunity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ExtendedCommunity", None) is not None:
                return self._properties.get("ExtendedCommunity")
        return ExtendedCommunity(self)._select()

    @property
    def Flapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_7cd710597ec8a94d40bed7d06822e7f9.Flapping): An instance of the Flapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_7cd710597ec8a94d40bed7d06822e7f9 import (
            Flapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Flapping", None) is not None:
                return self._properties.get("Flapping")
        return Flapping(self)._select()

    @property
    def AdvertiseNextHopAsV4(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertiseNextHopAsV4"])

    @AdvertiseNextHopAsV4.setter
    def AdvertiseNextHopAsV4(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvertiseNextHopAsV4"], value)

    @property
    def AggregatorAsNum(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the AS associated with the aggregator router ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorAsNum"])

    @AggregatorAsNum.setter
    def AggregatorAsNum(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorAsNum"], value)

    @property
    def AggregatorIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address for the aggregator.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorIpAddress"])

    @AggregatorIpAddress.setter
    def AggregatorIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorIpAddress"], value)

    @property
    def AsPathSetMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs): The mode to set the AsPath.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsPathSetMode"])

    @AsPathSetMode.setter
    def AsPathSetMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsPathSetMode"], value)

    @property
    def EnableAggregator(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAggregator"])

    @EnableAggregator.setter
    def EnableAggregator(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAggregator"], value)

    @property
    def EnableAggregatorIdIncrementMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The mode for the router ID of the router that aggregated two or more routes into one. Choose one of the following options: (1) Fixed-the same Aggregator ID will be used each time. (2) Increment-the Aggregator ID will increment by 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAggregatorIdIncrementMode"])

    @EnableAggregatorIdIncrementMode.setter
    def EnableAggregatorIdIncrementMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAggregatorIdIncrementMode"], value)

    @property
    def EnableAsPath(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that AS-PATH attributes are to be generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAsPath"])

    @EnableAsPath.setter
    def EnableAsPath(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAsPath"], value)

    @property
    def EnableAtomicAttribute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the attribute bit that indicates the router has aggregated two or more prefixes together into one.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAtomicAttribute"])

    @EnableAtomicAttribute.setter
    def EnableAtomicAttribute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAtomicAttribute"], value)

    @property
    def EnableCluster(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Generates a list of BGP clusters that a particular route has passed through.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCluster"])

    @EnableCluster.setter
    def EnableCluster(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCluster"], value)

    @property
    def EnableCommunity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that a community attribute should be added to the BGP entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCommunity"])

    @EnableCommunity.setter
    def EnableCommunity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCommunity"], value)

    @property
    def EnableGenerateUniqueRoutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generate unique routes option. Without this option enabled, every neighbor in the range will generate exactly the same set of routes, starting from the first route.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGenerateUniqueRoutes"])

    @EnableGenerateUniqueRoutes.setter
    def EnableGenerateUniqueRoutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGenerateUniqueRoutes"], value)

    @property
    def EnableIncludeLoopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Includes loopback addresses (for example, 127.0.0.0 for IPv4) in the list of VPN route ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludeLoopback"])

    @EnableIncludeLoopback.setter
    def EnableIncludeLoopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludeLoopback"], value)

    @property
    def EnableIncludeMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Includes multicast addresses (for example, 224.0.0.0 for IPv4) in the list of VPN route ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludeMulticast"])

    @EnableIncludeMulticast.setter
    def EnableIncludeMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludeMulticast"], value)

    @property
    def EnableLocalPref(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: inserts a LOCAL PREF attribute with the indicated value. (INTERNAL BGP only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLocalPref"])

    @EnableLocalPref.setter
    def EnableLocalPref(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLocalPref"], value)

    @property
    def EnableMed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Inserts a multi-exit discriminator (MED) attribute with the indicated value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMed"])

    @EnableMed.setter
    def EnableMed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMed"], value)

    @property
    def EnableNextHop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Next Hop. Inserts a Next Hop attribute that indicates the next router to send packets to, in order to get to the indicated prefixes/network addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableNextHop"])

    @EnableNextHop.setter
    def EnableNextHop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableNextHop"], value)

    @property
    def EnableOrigin(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the origin of the route will be indicated in the Origin field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOrigin"])

    @EnableOrigin.setter
    def EnableOrigin(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOrigin"], value)

    @property
    def EnableOriginatorId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOriginatorId"])

    @EnableOriginatorId.setter
    def EnableOriginatorId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOriginatorId"], value)

    @property
    def EnableProperSafi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (Not available for MPLS Route Ranges.) If enabled, the Multiprotocol BGP extensions are included with the SAFI set to 2 to indicate Network Layer Reachability Information for Multicast forwarding.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableProperSafi"])

    @EnableProperSafi.setter
    def EnableProperSafi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableProperSafi"], value)

    @property
    def EnableTraditionalNlriUpdate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTraditionalNlriUpdate"])

    @EnableTraditionalNlriUpdate.setter
    def EnableTraditionalNlriUpdate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTraditionalNlriUpdate"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the route range is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def EndOfRib(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables end of rib
        """
        return self._get_attribute(self._SDM_ATT_MAP["EndOfRib"])

    @EndOfRib.setter
    def EndOfRib(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EndOfRib"], value)

    @property
    def FromPacking(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FromPacking"])

    @FromPacking.setter
    def FromPacking(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FromPacking"], value)

    @property
    def FromPrefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first prefix length to generate based on the networkAddress and numRoutes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FromPrefix"])

    @FromPrefix.setter
    def FromPrefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FromPrefix"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): The version of the Internet Protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def IterationStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The step value to use for incrementing the network mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IterationStep"])

    @IterationStep.setter
    def IterationStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IterationStep"], value)

    @property
    def LocalPref(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Inserts a local pref attribute with the indicated value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPref"])

    @LocalPref.setter
    def LocalPref(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalPref"], value)

    @property
    def Med(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A multi-exit discriminator (MED) attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Med"])

    @Med.setter
    def Med(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Med"], value)

    @property
    def NetworkAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The network address used for the generated prefixes, in either IPv4 or IPv6 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkAddress"])

    @NetworkAddress.setter
    def NetworkAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworkAddress"], value)

    @property
    def NextHopIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The network (Layer 3) address of the router that is the next hop on the path to the destination.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopIpAddress"])

    @NextHopIpAddress.setter
    def NextHopIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopIpAddress"], value)

    @property
    def NextHopIpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): The type of IP address in nextHopIpAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopIpType"])

    @NextHopIpType.setter
    def NextHopIpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopIpType"], value)

    @property
    def NextHopMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixed | nextHopIncrement | incrementPerPrefix): Generates the NEXT HOP attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopMode"])

    @NextHopMode.setter
    def NextHopMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopMode"], value)

    @property
    def NextHopSetMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(setManually | sameAsLocalIp): Indicates now to set the next hop IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopSetMode"])

    @NextHopSetMode.setter
    def NextHopSetMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopSetMode"], value)

    @property
    def NumRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of prefixes (routes) to generate for this routeItem. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRoutes"])

    @NumRoutes.setter
    def NumRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRoutes"], value)

    @property
    def OriginProtocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str(igp | egp | incomplete): An indication of where the route entry originated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginProtocol"])

    @OriginProtocol.setter
    def OriginProtocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OriginProtocol"], value)

    @property
    def OriginatorId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The ID for the router that originated the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginatorId"])

    @OriginatorId.setter
    def OriginatorId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OriginatorId"], value)

    @property
    def ThruPacking(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ThruPacking"])

    @ThruPacking.setter
    def ThruPacking(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ThruPacking"], value)

    @property
    def ThruPrefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The last prefix length to generate based on the networkAddress and numRanges. (default = 24)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ThruPrefix"])

    @ThruPrefix.setter
    def ThruPrefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ThruPrefix"], value)

    def update(
        self,
        AdvertiseNextHopAsV4=None,
        AggregatorAsNum=None,
        AggregatorIpAddress=None,
        AsPathSetMode=None,
        EnableAggregator=None,
        EnableAggregatorIdIncrementMode=None,
        EnableAsPath=None,
        EnableAtomicAttribute=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableGenerateUniqueRoutes=None,
        EnableIncludeLoopback=None,
        EnableIncludeMulticast=None,
        EnableLocalPref=None,
        EnableMed=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableProperSafi=None,
        EnableTraditionalNlriUpdate=None,
        Enabled=None,
        EndOfRib=None,
        FromPacking=None,
        FromPrefix=None,
        IpType=None,
        IterationStep=None,
        LocalPref=None,
        Med=None,
        NetworkAddress=None,
        NextHopIpAddress=None,
        NextHopIpType=None,
        NextHopMode=None,
        NextHopSetMode=None,
        NumRoutes=None,
        OriginProtocol=None,
        OriginatorId=None,
        ThruPacking=None,
        ThruPrefix=None,
    ):
        # type: (bool, int, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, int, int, int, str, str, str, str, str, int, str, str, int, int) -> RouteRange
        """Updates routeRange resource on the server.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): Sets the AS associated with the aggregator router ID.
        - AggregatorIpAddress (str): The IP address for the aggregator.
        - AsPathSetMode (str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs)): The mode to set the AsPath.
        - EnableAggregator (bool): If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        - EnableAggregatorIdIncrementMode (bool): The mode for the router ID of the router that aggregated two or more routes into one. Choose one of the following options: (1) Fixed-the same Aggregator ID will be used each time. (2) Increment-the Aggregator ID will increment by 1.
        - EnableAsPath (bool): Indicates that AS-PATH attributes are to be generated.
        - EnableAtomicAttribute (bool): Sets the attribute bit that indicates the router has aggregated two or more prefixes together into one.
        - EnableCluster (bool): Generates a list of BGP clusters that a particular route has passed through.
        - EnableCommunity (bool): Indicates that a community attribute should be added to the BGP entry.
        - EnableGenerateUniqueRoutes (bool): Enables the generate unique routes option. Without this option enabled, every neighbor in the range will generate exactly the same set of routes, starting from the first route.
        - EnableIncludeLoopback (bool): Includes loopback addresses (for example, 127.0.0.0 for IPv4) in the list of VPN route ranges.
        - EnableIncludeMulticast (bool): Includes multicast addresses (for example, 224.0.0.0 for IPv4) in the list of VPN route ranges.
        - EnableLocalPref (bool): inserts a LOCAL PREF attribute with the indicated value. (INTERNAL BGP only)
        - EnableMed (bool): Inserts a multi-exit discriminator (MED) attribute with the indicated value.
        - EnableNextHop (bool): Enables Next Hop. Inserts a Next Hop attribute that indicates the next router to send packets to, in order to get to the indicated prefixes/network addresses.
        - EnableOrigin (bool): If enabled, the origin of the route will be indicated in the Origin field.
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        - EnableProperSafi (bool): (Not available for MPLS Route Ranges.) If enabled, the Multiprotocol BGP extensions are included with the SAFI set to 2 to indicate Network Layer Reachability Information for Multicast forwarding.
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): If true, the route range is enabled.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRoutes.
        - IpType (str(ipAny | ipv4 | ipv6)): The version of the Internet Protocol.
        - IterationStep (number): The step value to use for incrementing the network mask.
        - LocalPref (number): Inserts a local pref attribute with the indicated value.
        - Med (number): A multi-exit discriminator (MED) attribute.
        - NetworkAddress (str): The network address used for the generated prefixes, in either IPv4 or IPv6 format.
        - NextHopIpAddress (str): The network (Layer 3) address of the router that is the next hop on the path to the destination.
        - NextHopIpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextHopIpAddress.
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Generates the NEXT HOP attribute.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The ID for the router that originated the route.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdvertiseNextHopAsV4=None,
        AggregatorAsNum=None,
        AggregatorIpAddress=None,
        AsPathSetMode=None,
        EnableAggregator=None,
        EnableAggregatorIdIncrementMode=None,
        EnableAsPath=None,
        EnableAtomicAttribute=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableGenerateUniqueRoutes=None,
        EnableIncludeLoopback=None,
        EnableIncludeMulticast=None,
        EnableLocalPref=None,
        EnableMed=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableProperSafi=None,
        EnableTraditionalNlriUpdate=None,
        Enabled=None,
        EndOfRib=None,
        FromPacking=None,
        FromPrefix=None,
        IpType=None,
        IterationStep=None,
        LocalPref=None,
        Med=None,
        NetworkAddress=None,
        NextHopIpAddress=None,
        NextHopIpType=None,
        NextHopMode=None,
        NextHopSetMode=None,
        NumRoutes=None,
        OriginProtocol=None,
        OriginatorId=None,
        ThruPacking=None,
        ThruPrefix=None,
    ):
        # type: (bool, int, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, int, int, int, str, str, str, str, str, int, str, str, int, int) -> RouteRange
        """Adds a new routeRange resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): Sets the AS associated with the aggregator router ID.
        - AggregatorIpAddress (str): The IP address for the aggregator.
        - AsPathSetMode (str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs)): The mode to set the AsPath.
        - EnableAggregator (bool): If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        - EnableAggregatorIdIncrementMode (bool): The mode for the router ID of the router that aggregated two or more routes into one. Choose one of the following options: (1) Fixed-the same Aggregator ID will be used each time. (2) Increment-the Aggregator ID will increment by 1.
        - EnableAsPath (bool): Indicates that AS-PATH attributes are to be generated.
        - EnableAtomicAttribute (bool): Sets the attribute bit that indicates the router has aggregated two or more prefixes together into one.
        - EnableCluster (bool): Generates a list of BGP clusters that a particular route has passed through.
        - EnableCommunity (bool): Indicates that a community attribute should be added to the BGP entry.
        - EnableGenerateUniqueRoutes (bool): Enables the generate unique routes option. Without this option enabled, every neighbor in the range will generate exactly the same set of routes, starting from the first route.
        - EnableIncludeLoopback (bool): Includes loopback addresses (for example, 127.0.0.0 for IPv4) in the list of VPN route ranges.
        - EnableIncludeMulticast (bool): Includes multicast addresses (for example, 224.0.0.0 for IPv4) in the list of VPN route ranges.
        - EnableLocalPref (bool): inserts a LOCAL PREF attribute with the indicated value. (INTERNAL BGP only)
        - EnableMed (bool): Inserts a multi-exit discriminator (MED) attribute with the indicated value.
        - EnableNextHop (bool): Enables Next Hop. Inserts a Next Hop attribute that indicates the next router to send packets to, in order to get to the indicated prefixes/network addresses.
        - EnableOrigin (bool): If enabled, the origin of the route will be indicated in the Origin field.
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        - EnableProperSafi (bool): (Not available for MPLS Route Ranges.) If enabled, the Multiprotocol BGP extensions are included with the SAFI set to 2 to indicate Network Layer Reachability Information for Multicast forwarding.
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): If true, the route range is enabled.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRoutes.
        - IpType (str(ipAny | ipv4 | ipv6)): The version of the Internet Protocol.
        - IterationStep (number): The step value to use for incrementing the network mask.
        - LocalPref (number): Inserts a local pref attribute with the indicated value.
        - Med (number): A multi-exit discriminator (MED) attribute.
        - NetworkAddress (str): The network address used for the generated prefixes, in either IPv4 or IPv6 format.
        - NextHopIpAddress (str): The network (Layer 3) address of the router that is the next hop on the path to the destination.
        - NextHopIpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextHopIpAddress.
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Generates the NEXT HOP attribute.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The ID for the router that originated the route.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Returns
        -------
        - self: This instance with all currently retrieved routeRange resources using find and the newly added routeRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained routeRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AdvertiseNextHopAsV4=None,
        AggregatorAsNum=None,
        AggregatorIpAddress=None,
        AsPathSetMode=None,
        EnableAggregator=None,
        EnableAggregatorIdIncrementMode=None,
        EnableAsPath=None,
        EnableAtomicAttribute=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableGenerateUniqueRoutes=None,
        EnableIncludeLoopback=None,
        EnableIncludeMulticast=None,
        EnableLocalPref=None,
        EnableMed=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginatorId=None,
        EnableProperSafi=None,
        EnableTraditionalNlriUpdate=None,
        Enabled=None,
        EndOfRib=None,
        FromPacking=None,
        FromPrefix=None,
        IpType=None,
        IterationStep=None,
        LocalPref=None,
        Med=None,
        NetworkAddress=None,
        NextHopIpAddress=None,
        NextHopIpType=None,
        NextHopMode=None,
        NextHopSetMode=None,
        NumRoutes=None,
        OriginProtocol=None,
        OriginatorId=None,
        ThruPacking=None,
        ThruPrefix=None,
    ):
        # type: (bool, int, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, str, int, int, int, str, str, str, str, str, int, str, str, int, int) -> RouteRange
        """Finds and retrieves routeRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeRange resources from the server.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): Sets the AS associated with the aggregator router ID.
        - AggregatorIpAddress (str): The IP address for the aggregator.
        - AsPathSetMode (str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs)): The mode to set the AsPath.
        - EnableAggregator (bool): If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        - EnableAggregatorIdIncrementMode (bool): The mode for the router ID of the router that aggregated two or more routes into one. Choose one of the following options: (1) Fixed-the same Aggregator ID will be used each time. (2) Increment-the Aggregator ID will increment by 1.
        - EnableAsPath (bool): Indicates that AS-PATH attributes are to be generated.
        - EnableAtomicAttribute (bool): Sets the attribute bit that indicates the router has aggregated two or more prefixes together into one.
        - EnableCluster (bool): Generates a list of BGP clusters that a particular route has passed through.
        - EnableCommunity (bool): Indicates that a community attribute should be added to the BGP entry.
        - EnableGenerateUniqueRoutes (bool): Enables the generate unique routes option. Without this option enabled, every neighbor in the range will generate exactly the same set of routes, starting from the first route.
        - EnableIncludeLoopback (bool): Includes loopback addresses (for example, 127.0.0.0 for IPv4) in the list of VPN route ranges.
        - EnableIncludeMulticast (bool): Includes multicast addresses (for example, 224.0.0.0 for IPv4) in the list of VPN route ranges.
        - EnableLocalPref (bool): inserts a LOCAL PREF attribute with the indicated value. (INTERNAL BGP only)
        - EnableMed (bool): Inserts a multi-exit discriminator (MED) attribute with the indicated value.
        - EnableNextHop (bool): Enables Next Hop. Inserts a Next Hop attribute that indicates the next router to send packets to, in order to get to the indicated prefixes/network addresses.
        - EnableOrigin (bool): If enabled, the origin of the route will be indicated in the Origin field.
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        - EnableProperSafi (bool): (Not available for MPLS Route Ranges.) If enabled, the Multiprotocol BGP extensions are included with the SAFI set to 2 to indicate Network Layer Reachability Information for Multicast forwarding.
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): If true, the route range is enabled.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRoutes.
        - IpType (str(ipAny | ipv4 | ipv6)): The version of the Internet Protocol.
        - IterationStep (number): The step value to use for incrementing the network mask.
        - LocalPref (number): Inserts a local pref attribute with the indicated value.
        - Med (number): A multi-exit discriminator (MED) attribute.
        - NetworkAddress (str): The network address used for the generated prefixes, in either IPv4 or IPv6 format.
        - NextHopIpAddress (str): The network (Layer 3) address of the router that is the next hop on the path to the destination.
        - NextHopIpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextHopIpAddress.
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Generates the NEXT HOP attribute.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The ID for the router that originated the route.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Returns
        -------
        - self: This instance with matching routeRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of routeRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the routeRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ReAdvertiseRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the reAdvertiseRoutes operation on the server.

        NOT DEFINED

        reAdvertiseRoutes(async_operation=bool)string
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

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
        return self._execute("reAdvertiseRoutes", payload=payload, response_object=None)
