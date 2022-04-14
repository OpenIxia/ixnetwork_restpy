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


class VpnRouteRange(Base):
    """This object represents a route range present at a VPN site.
    The VpnRouteRange class encapsulates a list of vpnRouteRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the VpnRouteRange.find() method.
    The list can be managed by using the VpnRouteRange.add() and VpnRouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "vpnRouteRange"
    _SDM_ATT_MAP = {
        "AdvertiseNextHopAsV4": "advertiseNextHopAsV4",
        "AggregatorAsNum": "aggregatorAsNum",
        "AggregatorIpAddress": "aggregatorIpAddress",
        "Delay": "delay",
        "DistinguisherAsNumber": "distinguisherAsNumber",
        "DistinguisherAsNumberStep": "distinguisherAsNumberStep",
        "DistinguisherAsNumberStepAcrossVrfs": "distinguisherAsNumberStepAcrossVrfs",
        "DistinguisherAssignedNumber": "distinguisherAssignedNumber",
        "DistinguisherAssignedNumberStep": "distinguisherAssignedNumberStep",
        "DistinguisherAssignedNumberStepAcrossVrfs": "distinguisherAssignedNumberStepAcrossVrfs",
        "DistinguisherCount": "distinguisherCount",
        "DistinguisherCountPerVrf": "distinguisherCountPerVrf",
        "DistinguisherIpAddress": "distinguisherIpAddress",
        "DistinguisherIpAddressStep": "distinguisherIpAddressStep",
        "DistinguisherIpAddressStepAcrossVrfs": "distinguisherIpAddressStepAcrossVrfs",
        "DistinguisherMode": "distinguisherMode",
        "DistinguisherStep": "distinguisherStep",
        "DistinguisherType": "distinguisherType",
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
        "EnableTraditionalNlriUpdate": "enableTraditionalNlriUpdate",
        "Enabled": "enabled",
        "EndOfRib": "endOfRib",
        "FromPacking": "fromPacking",
        "FromPrefix": "fromPrefix",
        "IncludeSourceAsExtendedCommunityPresent": "includeSourceAsExtendedCommunityPresent",
        "IncludeVrfRouteImportExtendedCommunityPresent": "includeVrfRouteImportExtendedCommunityPresent",
        "IpType": "ipType",
        "IterationStep": "iterationStep",
        "LocalPref": "localPref",
        "Med": "med",
        "NetworkAddress": "networkAddress",
        "NextHopIpAddress": "nextHopIpAddress",
        "NextHopMode": "nextHopMode",
        "NextHopSetMode": "nextHopSetMode",
        "NumRoutes": "numRoutes",
        "OriginProtocol": "originProtocol",
        "OriginatorId": "originatorId",
        "RouteStepAcrossVRFs": "routeStepAcrossVRFs",
        "ThruPacking": "thruPacking",
        "ThruPrefix": "thruPrefix",
    }
    _SDM_ENUM_MAP = {
        "distinguisherMode": ["global", "local"],
        "distinguisherType": ["as", "ip", "asNumber2"],
        "ipType": ["ipAny", "ipv4", "ipv6"],
        "nextHopMode": ["fixed", "nextHopIncrement", "incrementPerPrefix"],
        "nextHopSetMode": ["setManually", "sameAsLocalIp"],
        "originProtocol": ["igp", "egp", "incomplete"],
    }

    def __init__(self, parent, list_op=False):
        super(VpnRouteRange, self).__init__(parent, list_op)

    @property
    def AsSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_4c94ceeed96557ff32fce7012dd22015.AsSegment): An instance of the AsSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_4c94ceeed96557ff32fce7012dd22015 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d2832402dfe62deffe3879c9fac5c4b9.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d2832402dfe62deffe3879c9fac5c4b9 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_e64a1ecd41511c1ec329aaecd199e41a.Community): An instance of the Community class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_e64a1ecd41511c1ec329aaecd199e41a import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_3f0e6925fdf4da36c7391d85a7b4b847.ExtendedCommunity): An instance of the ExtendedCommunity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_3f0e6925fdf4da36c7391d85a7b4b847 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_fcfccc97842ec02dad79c00c55fd6e0c.Flapping): An instance of the Flapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_fcfccc97842ec02dad79c00c55fd6e0c import (
            Flapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Flapping", None) is not None:
                return self._properties.get("Flapping")
        return Flapping(self)._select()

    @property
    def LabelSpace(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_85f09a1ad5ebf5a0273fd140a21079a2.LabelSpace): An instance of the LabelSpace class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_85f09a1ad5ebf5a0273fd140a21079a2 import (
            LabelSpace,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LabelSpace", None) is not None:
                return self._properties.get("LabelSpace")
        return LabelSpace(self)._select()

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
        - number: The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
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
        - str: The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorIpAddress"])

    @AggregatorIpAddress.setter
    def AggregatorIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorIpAddress"], value)

    @property
    def Delay(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Delay"])

    @Delay.setter
    def Delay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Delay"], value)

    @property
    def DistinguisherAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If distinguisherType is set to bgp4DistinguisherTypeAS, this is the 2-byte AS number in the administrator sub-field of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherAsNumber"])

    @DistinguisherAsNumber.setter
    def DistinguisherAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherAsNumber"], value)

    @property
    def DistinguisherAsNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for for the distinguisher AS number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherAsNumberStep"])

    @DistinguisherAsNumberStep.setter
    def DistinguisherAsNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherAsNumberStep"], value)

    @property
    def DistinguisherAsNumberStepAcrossVrfs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for per VRF distinguisher AS number within the VRF Range.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DistinguisherAsNumberStepAcrossVrfs"]
        )

    @DistinguisherAsNumberStepAcrossVrfs.setter
    def DistinguisherAsNumberStepAcrossVrfs(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DistinguisherAsNumberStepAcrossVrfs"], value
        )

    @property
    def DistinguisherAssignedNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned number of the VPN route distinguisher. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the route distinguisher. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherAssignedNumber"])

    @DistinguisherAssignedNumber.setter
    def DistinguisherAssignedNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherAssignedNumber"], value)

    @property
    def DistinguisherAssignedNumberStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for for the distinguisher assigned number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherAssignedNumberStep"])

    @DistinguisherAssignedNumberStep.setter
    def DistinguisherAssignedNumberStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherAssignedNumberStep"], value)

    @property
    def DistinguisherAssignedNumberStepAcrossVrfs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step for per VRF distinguisher assigned number within the VRF Range.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DistinguisherAssignedNumberStepAcrossVrfs"]
        )

    @DistinguisherAssignedNumberStepAcrossVrfs.setter
    def DistinguisherAssignedNumberStepAcrossVrfs(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DistinguisherAssignedNumberStepAcrossVrfs"], value
        )

    @property
    def DistinguisherCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of times that the increment step will be used. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherCount"])

    @DistinguisherCount.setter
    def DistinguisherCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherCount"], value)

    @property
    def DistinguisherCountPerVrf(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of times that the increment step is used per VRF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherCountPerVrf"])

    @DistinguisherCountPerVrf.setter
    def DistinguisherCountPerVrf(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherCountPerVrf"], value)

    @property
    def DistinguisherIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If distinguisherType is set to bgp4DistinguisherTypeIP, this is the 4-byte IP address in the administrator subfield of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherIpAddress"])

    @DistinguisherIpAddress.setter
    def DistinguisherIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherIpAddress"], value)

    @property
    def DistinguisherIpAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment step for for the distinguisher IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherIpAddressStep"])

    @DistinguisherIpAddressStep.setter
    def DistinguisherIpAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherIpAddressStep"], value)

    @property
    def DistinguisherIpAddressStepAcrossVrfs(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment step for per VRF distinguisher IP address within the VRF Range.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DistinguisherIpAddressStepAcrossVrfs"]
        )

    @DistinguisherIpAddressStepAcrossVrfs.setter
    def DistinguisherIpAddressStepAcrossVrfs(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DistinguisherIpAddressStepAcrossVrfs"], value
        )

    @property
    def DistinguisherMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(global | local): Specifies which part of the route distinguisher you want to increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherMode"])

    @DistinguisherMode.setter
    def DistinguisherMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherMode"], value)

    @property
    def DistinguisherStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherStep"])

    @DistinguisherStep.setter
    def DistinguisherStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherStep"], value)

    @property
    def DistinguisherType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(as | ip | asNumber2): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguisherType"])

    @DistinguisherType.setter
    def DistinguisherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguisherType"], value)

    @property
    def EnableAggregator(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
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
        - bool: If true, increments the Aggregator ID by interationStep.
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
        - bool: Enables the generation of AS Path related items.
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
        - bool: Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
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
        - bool: Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
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
        - bool: Enables the generation of a COMMUNITY attribute list. (default = false)
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
        - bool: When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
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
        - bool:
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
        - bool:
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
        - bool: Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
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
        - bool: Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
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
        - bool: Enables the generation of a NEXT HOP attribute. (default = true)
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
        - bool: Enables the generation of an ORIGIN attribute. (default = true)
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
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOriginatorId"])

    @EnableOriginatorId.setter
    def EnableOriginatorId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOriginatorId"], value)

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
        - bool: Enables the VPN route range.
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
        - number: The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
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
        - number: The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FromPrefix"])

    @FromPrefix.setter
    def FromPrefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FromPrefix"], value)

    @property
    def IncludeSourceAsExtendedCommunityPresent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IncludeSourceAsExtendedCommunityPresent"]
        )

    @IncludeSourceAsExtendedCommunityPresent.setter
    def IncludeSourceAsExtendedCommunityPresent(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["IncludeSourceAsExtendedCommunityPresent"], value
        )

    @property
    def IncludeVrfRouteImportExtendedCommunityPresent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Defines the route target extended community.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IncludeVrfRouteImportExtendedCommunityPresent"]
        )

    @IncludeVrfRouteImportExtendedCommunityPresent.setter
    def IncludeVrfRouteImportExtendedCommunityPresent(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["IncludeVrfRouteImportExtendedCommunityPresent"], value
        )

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): The type of IP address in nextworkAddress.
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
        - number: During prefix generation, the increment between prefixes. (default = 1)
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
        - number: The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
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
        - number: The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
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
        - str: The network address used for the generated prefixes. (default = 0.0.0.0)
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
        - str: The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopIpAddress"])

    @NextHopIpAddress.setter
    def NextHopIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopIpAddress"], value)

    @property
    def NextHopMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixed | nextHopIncrement | incrementPerPrefix): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
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
        - str: The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginatorId"])

    @OriginatorId.setter
    def OriginatorId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OriginatorId"], value)

    @property
    def RouteStepAcrossVRFs(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The route increment value across VRFs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteStepAcrossVRFs"])

    @RouteStepAcrossVRFs.setter
    def RouteStepAcrossVRFs(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteStepAcrossVRFs"], value)

    @property
    def ThruPacking(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. See the discussion under fromPacking above. (default = 0)
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
        Delay=None,
        DistinguisherAsNumber=None,
        DistinguisherAsNumberStep=None,
        DistinguisherAsNumberStepAcrossVrfs=None,
        DistinguisherAssignedNumber=None,
        DistinguisherAssignedNumberStep=None,
        DistinguisherAssignedNumberStepAcrossVrfs=None,
        DistinguisherCount=None,
        DistinguisherCountPerVrf=None,
        DistinguisherIpAddress=None,
        DistinguisherIpAddressStep=None,
        DistinguisherIpAddressStepAcrossVrfs=None,
        DistinguisherMode=None,
        DistinguisherStep=None,
        DistinguisherType=None,
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
        EnableTraditionalNlriUpdate=None,
        Enabled=None,
        EndOfRib=None,
        FromPacking=None,
        FromPrefix=None,
        IncludeSourceAsExtendedCommunityPresent=None,
        IncludeVrfRouteImportExtendedCommunityPresent=None,
        IpType=None,
        IterationStep=None,
        LocalPref=None,
        Med=None,
        NetworkAddress=None,
        NextHopIpAddress=None,
        NextHopMode=None,
        NextHopSetMode=None,
        NumRoutes=None,
        OriginProtocol=None,
        OriginatorId=None,
        RouteStepAcrossVRFs=None,
        ThruPacking=None,
        ThruPrefix=None,
    ):
        # type: (bool, int, str, int, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, bool, bool, str, int, int, int, str, str, str, str, int, str, str, str, int, int) -> VpnRouteRange
        """Updates vpnRouteRange resource on the server.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorIpAddress (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - Delay (number):
        - DistinguisherAsNumber (number): If distinguisherType is set to bgp4DistinguisherTypeAS, this is the 2-byte AS number in the administrator sub-field of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0)
        - DistinguisherAsNumberStep (number): The increment step for for the distinguisher AS number.
        - DistinguisherAsNumberStepAcrossVrfs (number): The increment step for per VRF distinguisher AS number within the VRF Range.
        - DistinguisherAssignedNumber (number): The assigned number of the VPN route distinguisher. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the route distinguisher. (default = 0)
        - DistinguisherAssignedNumberStep (number): The increment step for for the distinguisher assigned number.
        - DistinguisherAssignedNumberStepAcrossVrfs (number): The increment step for per VRF distinguisher assigned number within the VRF Range.
        - DistinguisherCount (number): The number of times that the increment step will be used. (default = 1)
        - DistinguisherCountPerVrf (number): The number of times that the increment step is used per VRF.
        - DistinguisherIpAddress (str): If distinguisherType is set to bgp4DistinguisherTypeIP, this is the 4-byte IP address in the administrator subfield of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0.0.0.0)
        - DistinguisherIpAddressStep (str): The increment step for for the distinguisher IP address.
        - DistinguisherIpAddressStepAcrossVrfs (str): The increment step for per VRF distinguisher IP address within the VRF Range.
        - DistinguisherMode (str(global | local)): Specifies which part of the route distinguisher you want to increment.
        - DistinguisherStep (number): The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        - DistinguisherType (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAggregatorIdIncrementMode (bool): If true, increments the Aggregator ID by interationStep.
        - EnableAsPath (bool): Enables the generation of AS Path related items.
        - EnableAtomicAttribute (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableGenerateUniqueRoutes (bool): When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        - EnableIncludeLoopback (bool):
        - EnableIncludeMulticast (bool):
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): Enables the VPN route range.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        - IncludeSourceAsExtendedCommunityPresent (bool): If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): Defines the route target extended community.
        - IpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextworkAddress.
        - IterationStep (number): During prefix generation, the increment between prefixes. (default = 1)
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NetworkAddress (str): The network address used for the generated prefixes. (default = 0.0.0.0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - RouteStepAcrossVRFs (str): The route increment value across VRFs.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. See the discussion under fromPacking above. (default = 0)
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
        Delay=None,
        DistinguisherAsNumber=None,
        DistinguisherAsNumberStep=None,
        DistinguisherAsNumberStepAcrossVrfs=None,
        DistinguisherAssignedNumber=None,
        DistinguisherAssignedNumberStep=None,
        DistinguisherAssignedNumberStepAcrossVrfs=None,
        DistinguisherCount=None,
        DistinguisherCountPerVrf=None,
        DistinguisherIpAddress=None,
        DistinguisherIpAddressStep=None,
        DistinguisherIpAddressStepAcrossVrfs=None,
        DistinguisherMode=None,
        DistinguisherStep=None,
        DistinguisherType=None,
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
        EnableTraditionalNlriUpdate=None,
        Enabled=None,
        EndOfRib=None,
        FromPacking=None,
        FromPrefix=None,
        IncludeSourceAsExtendedCommunityPresent=None,
        IncludeVrfRouteImportExtendedCommunityPresent=None,
        IpType=None,
        IterationStep=None,
        LocalPref=None,
        Med=None,
        NetworkAddress=None,
        NextHopIpAddress=None,
        NextHopMode=None,
        NextHopSetMode=None,
        NumRoutes=None,
        OriginProtocol=None,
        OriginatorId=None,
        RouteStepAcrossVRFs=None,
        ThruPacking=None,
        ThruPrefix=None,
    ):
        # type: (bool, int, str, int, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, bool, bool, str, int, int, int, str, str, str, str, int, str, str, str, int, int) -> VpnRouteRange
        """Adds a new vpnRouteRange resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorIpAddress (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - Delay (number):
        - DistinguisherAsNumber (number): If distinguisherType is set to bgp4DistinguisherTypeAS, this is the 2-byte AS number in the administrator sub-field of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0)
        - DistinguisherAsNumberStep (number): The increment step for for the distinguisher AS number.
        - DistinguisherAsNumberStepAcrossVrfs (number): The increment step for per VRF distinguisher AS number within the VRF Range.
        - DistinguisherAssignedNumber (number): The assigned number of the VPN route distinguisher. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the route distinguisher. (default = 0)
        - DistinguisherAssignedNumberStep (number): The increment step for for the distinguisher assigned number.
        - DistinguisherAssignedNumberStepAcrossVrfs (number): The increment step for per VRF distinguisher assigned number within the VRF Range.
        - DistinguisherCount (number): The number of times that the increment step will be used. (default = 1)
        - DistinguisherCountPerVrf (number): The number of times that the increment step is used per VRF.
        - DistinguisherIpAddress (str): If distinguisherType is set to bgp4DistinguisherTypeIP, this is the 4-byte IP address in the administrator subfield of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0.0.0.0)
        - DistinguisherIpAddressStep (str): The increment step for for the distinguisher IP address.
        - DistinguisherIpAddressStepAcrossVrfs (str): The increment step for per VRF distinguisher IP address within the VRF Range.
        - DistinguisherMode (str(global | local)): Specifies which part of the route distinguisher you want to increment.
        - DistinguisherStep (number): The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        - DistinguisherType (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAggregatorIdIncrementMode (bool): If true, increments the Aggregator ID by interationStep.
        - EnableAsPath (bool): Enables the generation of AS Path related items.
        - EnableAtomicAttribute (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableGenerateUniqueRoutes (bool): When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        - EnableIncludeLoopback (bool):
        - EnableIncludeMulticast (bool):
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): Enables the VPN route range.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        - IncludeSourceAsExtendedCommunityPresent (bool): If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): Defines the route target extended community.
        - IpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextworkAddress.
        - IterationStep (number): During prefix generation, the increment between prefixes. (default = 1)
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NetworkAddress (str): The network address used for the generated prefixes. (default = 0.0.0.0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - RouteStepAcrossVRFs (str): The route increment value across VRFs.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. See the discussion under fromPacking above. (default = 0)
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Returns
        -------
        - self: This instance with all currently retrieved vpnRouteRange resources using find and the newly added vpnRouteRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vpnRouteRange resources in this instance from the server.

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
        Delay=None,
        DistinguisherAsNumber=None,
        DistinguisherAsNumberStep=None,
        DistinguisherAsNumberStepAcrossVrfs=None,
        DistinguisherAssignedNumber=None,
        DistinguisherAssignedNumberStep=None,
        DistinguisherAssignedNumberStepAcrossVrfs=None,
        DistinguisherCount=None,
        DistinguisherCountPerVrf=None,
        DistinguisherIpAddress=None,
        DistinguisherIpAddressStep=None,
        DistinguisherIpAddressStepAcrossVrfs=None,
        DistinguisherMode=None,
        DistinguisherStep=None,
        DistinguisherType=None,
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
        EnableTraditionalNlriUpdate=None,
        Enabled=None,
        EndOfRib=None,
        FromPacking=None,
        FromPrefix=None,
        IncludeSourceAsExtendedCommunityPresent=None,
        IncludeVrfRouteImportExtendedCommunityPresent=None,
        IpType=None,
        IterationStep=None,
        LocalPref=None,
        Med=None,
        NetworkAddress=None,
        NextHopIpAddress=None,
        NextHopMode=None,
        NextHopSetMode=None,
        NumRoutes=None,
        OriginProtocol=None,
        OriginatorId=None,
        RouteStepAcrossVRFs=None,
        ThruPacking=None,
        ThruPrefix=None,
    ):
        # type: (bool, int, str, int, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, bool, bool, str, int, int, int, str, str, str, str, int, str, str, str, int, int) -> VpnRouteRange
        """Finds and retrieves vpnRouteRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vpnRouteRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vpnRouteRange resources from the server.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorIpAddress (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - Delay (number):
        - DistinguisherAsNumber (number): If distinguisherType is set to bgp4DistinguisherTypeAS, this is the 2-byte AS number in the administrator sub-field of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0)
        - DistinguisherAsNumberStep (number): The increment step for for the distinguisher AS number.
        - DistinguisherAsNumberStepAcrossVrfs (number): The increment step for per VRF distinguisher AS number within the VRF Range.
        - DistinguisherAssignedNumber (number): The assigned number of the VPN route distinguisher. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the route distinguisher. (default = 0)
        - DistinguisherAssignedNumberStep (number): The increment step for for the distinguisher assigned number.
        - DistinguisherAssignedNumberStepAcrossVrfs (number): The increment step for per VRF distinguisher assigned number within the VRF Range.
        - DistinguisherCount (number): The number of times that the increment step will be used. (default = 1)
        - DistinguisherCountPerVrf (number): The number of times that the increment step is used per VRF.
        - DistinguisherIpAddress (str): If distinguisherType is set to bgp4DistinguisherTypeIP, this is the 4-byte IP address in the administrator subfield of the value field of the VPN Route Distinguisher. It is the global part of the route distinguisher. (default = 0.0.0.0)
        - DistinguisherIpAddressStep (str): The increment step for for the distinguisher IP address.
        - DistinguisherIpAddressStepAcrossVrfs (str): The increment step for per VRF distinguisher IP address within the VRF Range.
        - DistinguisherMode (str(global | local)): Specifies which part of the route distinguisher you want to increment.
        - DistinguisherStep (number): The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        - DistinguisherType (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAggregatorIdIncrementMode (bool): If true, increments the Aggregator ID by interationStep.
        - EnableAsPath (bool): Enables the generation of AS Path related items.
        - EnableAtomicAttribute (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableGenerateUniqueRoutes (bool): When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        - EnableIncludeLoopback (bool):
        - EnableIncludeMulticast (bool):
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): Enables the VPN route range.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        - IncludeSourceAsExtendedCommunityPresent (bool): If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): Defines the route target extended community.
        - IpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextworkAddress.
        - IterationStep (number): During prefix generation, the increment between prefixes. (default = 1)
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NetworkAddress (str): The network address used for the generated prefixes. (default = 0.0.0.0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - RouteStepAcrossVRFs (str): The route increment value across VRFs.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. See the discussion under fromPacking above. (default = 0)
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Returns
        -------
        - self: This instance with matching vpnRouteRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vpnRouteRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vpnRouteRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
