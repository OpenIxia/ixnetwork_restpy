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


class UmhSelectionRouteRange(Base):
    """This object represents a UMH selection route range in an L3 site
    The UmhSelectionRouteRange class encapsulates a list of umhSelectionRouteRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the UmhSelectionRouteRange.find() method.
    The list can be managed by using the UmhSelectionRouteRange.add() and UmhSelectionRouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "umhSelectionRouteRange"
    _SDM_ATT_MAP = {
        "AggregatorAsNumber": "aggregatorAsNumber",
        "AggregatorIdIncrementMode": "aggregatorIdIncrementMode",
        "AggregatorIpAddress": "aggregatorIpAddress",
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
        "EnableAsPath": "enableAsPath",
        "EnableAtomicAggregator": "enableAtomicAggregator",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableGenerateUniqueRoutes": "enableGenerateUniqueRoutes",
        "EnableLocalPref": "enableLocalPref",
        "EnableMed": "enableMed",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginator": "enableOriginator",
        "EnableUseTraditionalNlri": "enableUseTraditionalNlri",
        "Enabled": "enabled",
        "FirstRoute": "firstRoute",
        "IncludeSourceAsExtendedCommunityPresent": "includeSourceAsExtendedCommunityPresent",
        "IncludeVrfRouteImportExtendedCommunityPresent": "includeVrfRouteImportExtendedCommunityPresent",
        "IpType": "ipType",
        "LocalPref": "localPref",
        "MaskWidth": "maskWidth",
        "MaskWidthTo": "maskWidthTo",
        "Med": "med",
        "NextHopIpAddress": "nextHopIpAddress",
        "NextHopMode": "nextHopMode",
        "NextHopSetMode": "nextHopSetMode",
        "OriginProtocol": "originProtocol",
        "OriginatorId": "originatorId",
        "PackingFrom": "packingFrom",
        "PackingTo": "packingTo",
        "RouteCountPerVrfs": "routeCountPerVrfs",
        "RouteStepAcrossVrfs": "routeStepAcrossVrfs",
        "Step": "step",
    }
    _SDM_ENUM_MAP = {
        "aggregatorIdIncrementMode": ["fixed", "increment"],
        "distinguisherMode": ["global", "local"],
        "distinguisherType": ["as", "ip", "asNumber2"],
        "ipType": ["ipAny", "ipv4", "ipv6"],
        "nextHopMode": ["nextHopIncrement", "fixed", "incrementPerPrefix"],
        "nextHopSetMode": ["sameAsLocalIp", "setManually"],
        "originProtocol": ["igp", "egp", "incomplete"],
    }

    def __init__(self, parent, list_op=False):
        super(UmhSelectionRouteRange, self).__init__(parent, list_op)

    @property
    def AsSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_4988c478ce9b4241205f6811a359ffe8.AsSegment): An instance of the AsSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_4988c478ce9b4241205f6811a359ffe8 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_f3997bb962d2128c99954ba076f70beb.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_f3997bb962d2128c99954ba076f70beb import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_6aed3c83f2a302323de0f8dd850abdcc.Community): An instance of the Community class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_6aed3c83f2a302323de0f8dd850abdcc import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_1088c247b717ff4329d3c4e43ec9916b.ExtendedCommunity): An instance of the ExtendedCommunity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_1088c247b717ff4329d3c4e43ec9916b import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_0c191468e6dbc2508006af0395ecab15.Flapping): An instance of the Flapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_0c191468e6dbc2508006af0395ecab15 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_f8e4bd27d1a26b770c2211ad8e011438.LabelSpace): An instance of the LabelSpace class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_f8e4bd27d1a26b770c2211ad8e011438 import (
            LabelSpace,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LabelSpace", None) is not None:
                return self._properties.get("LabelSpace")
        return LabelSpace(self)._select()

    @property
    def AggregatorAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: AS number associated with Aggregator ID in Aggregator attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorAsNumber"])

    @AggregatorAsNumber.setter
    def AggregatorAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorAsNumber"], value)

    @property
    def AggregatorIdIncrementMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixed | increment): Increment mode of aggregator ID
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorIdIncrementMode"])

    @AggregatorIdIncrementMode.setter
    def AggregatorIdIncrementMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorIdIncrementMode"], value)

    @property
    def AggregatorIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IP address of the aggregator in Aggregator attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorIpAddress"])

    @AggregatorIpAddress.setter
    def AggregatorIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorIpAddress"], value)

    @property
    def DistinguisherAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Distinguisher AS number
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
        - number: Increment step of Distinguisher AS number across the routes in route range
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
        - number: Increment step of Distinguisher AS number across the VRFs in VRF range
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
        - number: Distinguisher assigned number
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
        - number: Increment step of distinguisher assigned number across routes in route range
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
        - number: Increment step of distinguisher assigned number across VRFs in VRF range
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
        - number: Number of times increment step will be used ( default = 1 )
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
        - number: Number of times increment step will be used per VRF
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
        - str: Distinguisher IP address
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
        - str: Increment step of distinguisher IP address across routes in route range
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
        - str: Increment step of distinguisher IP address across VRFs in VRF range
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
    def EnableAtomicAggregator(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAtomicAggregator"])

    @EnableAtomicAggregator.setter
    def EnableAtomicAggregator(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAtomicAggregator"], value)

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
    def EnableOriginator(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOriginator"])

    @EnableOriginator.setter
    def EnableOriginator(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOriginator"], value)

    @property
    def EnableUseTraditionalNlri(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableUseTraditionalNlri"])

    @EnableUseTraditionalNlri.setter
    def EnableUseTraditionalNlri(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableUseTraditionalNlri"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the UMH route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FirstRoute(self):
        # type: () -> str
        """
        Returns
        -------
        - str: First route in route range
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstRoute"])

    @FirstRoute.setter
    def FirstRoute(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstRoute"], value)

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
    def MaskWidth(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Mask width of route range
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaskWidth"])

    @MaskWidth.setter
    def MaskWidth(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaskWidth"], value)

    @property
    def MaskWidthTo(self):
        # type: () -> int
        """
        Returns
        -------
        - number: mask width of last route range
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaskWidthTo"])

    @MaskWidthTo.setter
    def MaskWidthTo(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaskWidthTo"], value)

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
        - str(nextHopIncrement | fixed | incrementPerPrefix): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
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
        - str(sameAsLocalIp | setManually): Indicates now to set the next hop IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopSetMode"])

    @NextHopSetMode.setter
    def NextHopSetMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopSetMode"], value)

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
    def PackingFrom(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Initial number of route packed in one BGP update
        """
        return self._get_attribute(self._SDM_ATT_MAP["PackingFrom"])

    @PackingFrom.setter
    def PackingFrom(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PackingFrom"], value)

    @property
    def PackingTo(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Final number of routes packed in one BGP update
        """
        return self._get_attribute(self._SDM_ATT_MAP["PackingTo"])

    @PackingTo.setter
    def PackingTo(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PackingTo"], value)

    @property
    def RouteCountPerVrfs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of route per VRF
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteCountPerVrfs"])

    @RouteCountPerVrfs.setter
    def RouteCountPerVrfs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteCountPerVrfs"], value)

    @property
    def RouteStepAcrossVrfs(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The route increment value across VRFs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteStepAcrossVrfs"])

    @RouteStepAcrossVrfs.setter
    def RouteStepAcrossVrfs(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteStepAcrossVrfs"], value)

    @property
    def Step(self):
        # type: () -> int
        """
        Returns
        -------
        - number: step
        """
        return self._get_attribute(self._SDM_ATT_MAP["Step"])

    @Step.setter
    def Step(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Step"], value)

    def update(
        self,
        AggregatorAsNumber=None,
        AggregatorIdIncrementMode=None,
        AggregatorIpAddress=None,
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
        EnableAsPath=None,
        EnableAtomicAggregator=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableGenerateUniqueRoutes=None,
        EnableLocalPref=None,
        EnableMed=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginator=None,
        EnableUseTraditionalNlri=None,
        Enabled=None,
        FirstRoute=None,
        IncludeSourceAsExtendedCommunityPresent=None,
        IncludeVrfRouteImportExtendedCommunityPresent=None,
        IpType=None,
        LocalPref=None,
        MaskWidth=None,
        MaskWidthTo=None,
        Med=None,
        NextHopIpAddress=None,
        NextHopMode=None,
        NextHopSetMode=None,
        OriginProtocol=None,
        OriginatorId=None,
        PackingFrom=None,
        PackingTo=None,
        RouteCountPerVrfs=None,
        RouteStepAcrossVrfs=None,
        Step=None,
    ):
        # type: (int, str, str, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, str, int, int, int, int, str, str, str, str, str, int, int, int, str, int) -> UmhSelectionRouteRange
        """Updates umhSelectionRouteRange resource on the server.

        Args
        ----
        - AggregatorAsNumber (number): AS number associated with Aggregator ID in Aggregator attribute
        - AggregatorIdIncrementMode (str(fixed | increment)): Increment mode of aggregator ID
        - AggregatorIpAddress (str): IP address of the aggregator in Aggregator attribute
        - DistinguisherAsNumber (number): Distinguisher AS number
        - DistinguisherAsNumberStep (number): Increment step of Distinguisher AS number across the routes in route range
        - DistinguisherAsNumberStepAcrossVrfs (number): Increment step of Distinguisher AS number across the VRFs in VRF range
        - DistinguisherAssignedNumber (number): Distinguisher assigned number
        - DistinguisherAssignedNumberStep (number): Increment step of distinguisher assigned number across routes in route range
        - DistinguisherAssignedNumberStepAcrossVrfs (number): Increment step of distinguisher assigned number across VRFs in VRF range
        - DistinguisherCount (number): Number of times increment step will be used ( default = 1 )
        - DistinguisherCountPerVrf (number): Number of times increment step will be used per VRF
        - DistinguisherIpAddress (str): Distinguisher IP address
        - DistinguisherIpAddressStep (str): Increment step of distinguisher IP address across routes in route range
        - DistinguisherIpAddressStepAcrossVrfs (str): Increment step of distinguisher IP address across VRFs in VRF range
        - DistinguisherMode (str(global | local)): Specifies which part of the route distinguisher you want to increment.
        - DistinguisherStep (number): The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        - DistinguisherType (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Enables the generation of AS Path related items.
        - EnableAtomicAggregator (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableGenerateUniqueRoutes (bool): When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginator (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - EnableUseTraditionalNlri (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): Enables the UMH route range.
        - FirstRoute (str): First route in route range
        - IncludeSourceAsExtendedCommunityPresent (bool): If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): Defines the route target extended community.
        - IpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextworkAddress.
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - MaskWidth (number): Mask width of route range
        - MaskWidthTo (number): mask width of last route range
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(nextHopIncrement | fixed | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(sameAsLocalIp | setManually)): Indicates now to set the next hop IP address.
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - PackingFrom (number): Initial number of route packed in one BGP update
        - PackingTo (number): Final number of routes packed in one BGP update
        - RouteCountPerVrfs (number): Number of route per VRF
        - RouteStepAcrossVrfs (str): The route increment value across VRFs.
        - Step (number): step

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AggregatorAsNumber=None,
        AggregatorIdIncrementMode=None,
        AggregatorIpAddress=None,
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
        EnableAsPath=None,
        EnableAtomicAggregator=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableGenerateUniqueRoutes=None,
        EnableLocalPref=None,
        EnableMed=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginator=None,
        EnableUseTraditionalNlri=None,
        Enabled=None,
        FirstRoute=None,
        IncludeSourceAsExtendedCommunityPresent=None,
        IncludeVrfRouteImportExtendedCommunityPresent=None,
        IpType=None,
        LocalPref=None,
        MaskWidth=None,
        MaskWidthTo=None,
        Med=None,
        NextHopIpAddress=None,
        NextHopMode=None,
        NextHopSetMode=None,
        OriginProtocol=None,
        OriginatorId=None,
        PackingFrom=None,
        PackingTo=None,
        RouteCountPerVrfs=None,
        RouteStepAcrossVrfs=None,
        Step=None,
    ):
        # type: (int, str, str, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, str, int, int, int, int, str, str, str, str, str, int, int, int, str, int) -> UmhSelectionRouteRange
        """Adds a new umhSelectionRouteRange resource on the server and adds it to the container.

        Args
        ----
        - AggregatorAsNumber (number): AS number associated with Aggregator ID in Aggregator attribute
        - AggregatorIdIncrementMode (str(fixed | increment)): Increment mode of aggregator ID
        - AggregatorIpAddress (str): IP address of the aggregator in Aggregator attribute
        - DistinguisherAsNumber (number): Distinguisher AS number
        - DistinguisherAsNumberStep (number): Increment step of Distinguisher AS number across the routes in route range
        - DistinguisherAsNumberStepAcrossVrfs (number): Increment step of Distinguisher AS number across the VRFs in VRF range
        - DistinguisherAssignedNumber (number): Distinguisher assigned number
        - DistinguisherAssignedNumberStep (number): Increment step of distinguisher assigned number across routes in route range
        - DistinguisherAssignedNumberStepAcrossVrfs (number): Increment step of distinguisher assigned number across VRFs in VRF range
        - DistinguisherCount (number): Number of times increment step will be used ( default = 1 )
        - DistinguisherCountPerVrf (number): Number of times increment step will be used per VRF
        - DistinguisherIpAddress (str): Distinguisher IP address
        - DistinguisherIpAddressStep (str): Increment step of distinguisher IP address across routes in route range
        - DistinguisherIpAddressStepAcrossVrfs (str): Increment step of distinguisher IP address across VRFs in VRF range
        - DistinguisherMode (str(global | local)): Specifies which part of the route distinguisher you want to increment.
        - DistinguisherStep (number): The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        - DistinguisherType (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Enables the generation of AS Path related items.
        - EnableAtomicAggregator (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableGenerateUniqueRoutes (bool): When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginator (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - EnableUseTraditionalNlri (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): Enables the UMH route range.
        - FirstRoute (str): First route in route range
        - IncludeSourceAsExtendedCommunityPresent (bool): If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): Defines the route target extended community.
        - IpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextworkAddress.
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - MaskWidth (number): Mask width of route range
        - MaskWidthTo (number): mask width of last route range
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(nextHopIncrement | fixed | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(sameAsLocalIp | setManually)): Indicates now to set the next hop IP address.
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - PackingFrom (number): Initial number of route packed in one BGP update
        - PackingTo (number): Final number of routes packed in one BGP update
        - RouteCountPerVrfs (number): Number of route per VRF
        - RouteStepAcrossVrfs (str): The route increment value across VRFs.
        - Step (number): step

        Returns
        -------
        - self: This instance with all currently retrieved umhSelectionRouteRange resources using find and the newly added umhSelectionRouteRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained umhSelectionRouteRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AggregatorAsNumber=None,
        AggregatorIdIncrementMode=None,
        AggregatorIpAddress=None,
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
        EnableAsPath=None,
        EnableAtomicAggregator=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableGenerateUniqueRoutes=None,
        EnableLocalPref=None,
        EnableMed=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginator=None,
        EnableUseTraditionalNlri=None,
        Enabled=None,
        FirstRoute=None,
        IncludeSourceAsExtendedCommunityPresent=None,
        IncludeVrfRouteImportExtendedCommunityPresent=None,
        IpType=None,
        LocalPref=None,
        MaskWidth=None,
        MaskWidthTo=None,
        Med=None,
        NextHopIpAddress=None,
        NextHopMode=None,
        NextHopSetMode=None,
        OriginProtocol=None,
        OriginatorId=None,
        PackingFrom=None,
        PackingTo=None,
        RouteCountPerVrfs=None,
        RouteStepAcrossVrfs=None,
        Step=None,
    ):
        # type: (int, str, str, int, int, int, int, int, int, int, int, str, str, str, str, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, str, int, int, int, int, str, str, str, str, str, int, int, int, str, int) -> UmhSelectionRouteRange
        """Finds and retrieves umhSelectionRouteRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve umhSelectionRouteRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all umhSelectionRouteRange resources from the server.

        Args
        ----
        - AggregatorAsNumber (number): AS number associated with Aggregator ID in Aggregator attribute
        - AggregatorIdIncrementMode (str(fixed | increment)): Increment mode of aggregator ID
        - AggregatorIpAddress (str): IP address of the aggregator in Aggregator attribute
        - DistinguisherAsNumber (number): Distinguisher AS number
        - DistinguisherAsNumberStep (number): Increment step of Distinguisher AS number across the routes in route range
        - DistinguisherAsNumberStepAcrossVrfs (number): Increment step of Distinguisher AS number across the VRFs in VRF range
        - DistinguisherAssignedNumber (number): Distinguisher assigned number
        - DistinguisherAssignedNumberStep (number): Increment step of distinguisher assigned number across routes in route range
        - DistinguisherAssignedNumberStepAcrossVrfs (number): Increment step of distinguisher assigned number across VRFs in VRF range
        - DistinguisherCount (number): Number of times increment step will be used ( default = 1 )
        - DistinguisherCountPerVrf (number): Number of times increment step will be used per VRF
        - DistinguisherIpAddress (str): Distinguisher IP address
        - DistinguisherIpAddressStep (str): Increment step of distinguisher IP address across routes in route range
        - DistinguisherIpAddressStepAcrossVrfs (str): Increment step of distinguisher IP address across VRFs in VRF range
        - DistinguisherMode (str(global | local)): Specifies which part of the route distinguisher you want to increment.
        - DistinguisherStep (number): The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        - DistinguisherType (str(as | ip | asNumber2)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Enables the generation of AS Path related items.
        - EnableAtomicAggregator (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableGenerateUniqueRoutes (bool): When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginator (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - EnableUseTraditionalNlri (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): Enables the UMH route range.
        - FirstRoute (str): First route in route range
        - IncludeSourceAsExtendedCommunityPresent (bool): If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        - IncludeVrfRouteImportExtendedCommunityPresent (bool): Defines the route target extended community.
        - IpType (str(ipAny | ipv4 | ipv6)): The type of IP address in nextworkAddress.
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - MaskWidth (number): Mask width of route range
        - MaskWidthTo (number): mask width of last route range
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(nextHopIncrement | fixed | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(sameAsLocalIp | setManually)): Indicates now to set the next hop IP address.
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - PackingFrom (number): Initial number of route packed in one BGP update
        - PackingTo (number): Final number of routes packed in one BGP update
        - RouteCountPerVrfs (number): Number of route per VRF
        - RouteStepAcrossVrfs (str): The route increment value across VRFs.
        - Step (number): step

        Returns
        -------
        - self: This instance with matching umhSelectionRouteRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of umhSelectionRouteRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the umhSelectionRouteRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
