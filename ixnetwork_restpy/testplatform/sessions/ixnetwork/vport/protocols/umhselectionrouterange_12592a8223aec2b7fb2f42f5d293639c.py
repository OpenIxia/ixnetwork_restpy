# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class UmhSelectionRouteRange(Base):
    """This object represents a UMH selection route range in an L3 site
    The UmhSelectionRouteRange class encapsulates a list of umhSelectionRouteRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the UmhSelectionRouteRange.find() method.
    The list can be managed by using the UmhSelectionRouteRange.add() and UmhSelectionRouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'umhSelectionRouteRange'

    def __init__(self, parent):
        super(UmhSelectionRouteRange, self).__init__(parent)

    @property
    def AsSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_858cf5f120c1b651f6a00efc244302d4.AsSegment): An instance of the AsSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_858cf5f120c1b651f6a00efc244302d4 import AsSegment
        return AsSegment(self)._select()

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_3ad02ef938563f0387e6e97ed7b6fbe5.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_3ad02ef938563f0387e6e97ed7b6fbe5 import Cluster
        return Cluster(self)._select()

    @property
    def Community(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_75d9a4400c04da25b439dd0f8418efff.Community): An instance of the Community class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_75d9a4400c04da25b439dd0f8418efff import Community
        return Community(self)._select()

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_bc9de205aa97de06a487bf33693d9e47.ExtendedCommunity): An instance of the ExtendedCommunity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_bc9de205aa97de06a487bf33693d9e47 import ExtendedCommunity
        return ExtendedCommunity(self)._select()

    @property
    def Flapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_c0790b3410d661259abaede6bfe2d0c8.Flapping): An instance of the Flapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_c0790b3410d661259abaede6bfe2d0c8 import Flapping
        return Flapping(self)._select()

    @property
    def LabelSpace(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_1dd82452dbbdd3a23ae7a6a05357fd0d.LabelSpace): An instance of the LabelSpace class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_1dd82452dbbdd3a23ae7a6a05357fd0d import LabelSpace
        return LabelSpace(self)._select()

    @property
    def AggregatorAsNumber(self):
        """
        Returns
        -------
        - number: AS number associated with Aggregator ID in Aggregator attribute
        """
        return self._get_attribute('aggregatorAsNumber')
    @AggregatorAsNumber.setter
    def AggregatorAsNumber(self, value):
        self._set_attribute('aggregatorAsNumber', value)

    @property
    def AggregatorIdIncrementMode(self):
        """
        Returns
        -------
        - str(fixed | increment): Increment mode of aggregator ID
        """
        return self._get_attribute('aggregatorIdIncrementMode')
    @AggregatorIdIncrementMode.setter
    def AggregatorIdIncrementMode(self, value):
        self._set_attribute('aggregatorIdIncrementMode', value)

    @property
    def AggregatorIpAddress(self):
        """
        Returns
        -------
        - str: IP address of the aggregator in Aggregator attribute
        """
        return self._get_attribute('aggregatorIpAddress')
    @AggregatorIpAddress.setter
    def AggregatorIpAddress(self, value):
        self._set_attribute('aggregatorIpAddress', value)

    @property
    def DistinguisherAsNumber(self):
        """
        Returns
        -------
        - number: Distinguisher AS number
        """
        return self._get_attribute('distinguisherAsNumber')
    @DistinguisherAsNumber.setter
    def DistinguisherAsNumber(self, value):
        self._set_attribute('distinguisherAsNumber', value)

    @property
    def DistinguisherAsNumberStep(self):
        """
        Returns
        -------
        - number: Increment step of Distinguisher AS number across the routes in route range
        """
        return self._get_attribute('distinguisherAsNumberStep')
    @DistinguisherAsNumberStep.setter
    def DistinguisherAsNumberStep(self, value):
        self._set_attribute('distinguisherAsNumberStep', value)

    @property
    def DistinguisherAsNumberStepAcrossVrfs(self):
        """
        Returns
        -------
        - number: Increment step of Distinguisher AS number across the VRFs in VRF range
        """
        return self._get_attribute('distinguisherAsNumberStepAcrossVrfs')
    @DistinguisherAsNumberStepAcrossVrfs.setter
    def DistinguisherAsNumberStepAcrossVrfs(self, value):
        self._set_attribute('distinguisherAsNumberStepAcrossVrfs', value)

    @property
    def DistinguisherAssignedNumber(self):
        """
        Returns
        -------
        - number: Distinguisher assigned number
        """
        return self._get_attribute('distinguisherAssignedNumber')
    @DistinguisherAssignedNumber.setter
    def DistinguisherAssignedNumber(self, value):
        self._set_attribute('distinguisherAssignedNumber', value)

    @property
    def DistinguisherAssignedNumberStep(self):
        """
        Returns
        -------
        - number: Increment step of distinguisher assigned number across routes in route range
        """
        return self._get_attribute('distinguisherAssignedNumberStep')
    @DistinguisherAssignedNumberStep.setter
    def DistinguisherAssignedNumberStep(self, value):
        self._set_attribute('distinguisherAssignedNumberStep', value)

    @property
    def DistinguisherAssignedNumberStepAcrossVrfs(self):
        """
        Returns
        -------
        - number: Increment step of distinguisher assigned number across VRFs in VRF range
        """
        return self._get_attribute('distinguisherAssignedNumberStepAcrossVrfs')
    @DistinguisherAssignedNumberStepAcrossVrfs.setter
    def DistinguisherAssignedNumberStepAcrossVrfs(self, value):
        self._set_attribute('distinguisherAssignedNumberStepAcrossVrfs', value)

    @property
    def DistinguisherCount(self):
        """
        Returns
        -------
        - number: Number of times increment step will be used ( default = 1 )
        """
        return self._get_attribute('distinguisherCount')
    @DistinguisherCount.setter
    def DistinguisherCount(self, value):
        self._set_attribute('distinguisherCount', value)

    @property
    def DistinguisherCountPerVrf(self):
        """
        Returns
        -------
        - number: Number of times increment step will be used per VRF
        """
        return self._get_attribute('distinguisherCountPerVrf')
    @DistinguisherCountPerVrf.setter
    def DistinguisherCountPerVrf(self, value):
        self._set_attribute('distinguisherCountPerVrf', value)

    @property
    def DistinguisherIpAddress(self):
        """
        Returns
        -------
        - str: Distinguisher IP address
        """
        return self._get_attribute('distinguisherIpAddress')
    @DistinguisherIpAddress.setter
    def DistinguisherIpAddress(self, value):
        self._set_attribute('distinguisherIpAddress', value)

    @property
    def DistinguisherIpAddressStep(self):
        """
        Returns
        -------
        - str: Increment step of distinguisher IP address across routes in route range
        """
        return self._get_attribute('distinguisherIpAddressStep')
    @DistinguisherIpAddressStep.setter
    def DistinguisherIpAddressStep(self, value):
        self._set_attribute('distinguisherIpAddressStep', value)

    @property
    def DistinguisherIpAddressStepAcrossVrfs(self):
        """
        Returns
        -------
        - str: Increment step of distinguisher IP address across VRFs in VRF range
        """
        return self._get_attribute('distinguisherIpAddressStepAcrossVrfs')
    @DistinguisherIpAddressStepAcrossVrfs.setter
    def DistinguisherIpAddressStepAcrossVrfs(self, value):
        self._set_attribute('distinguisherIpAddressStepAcrossVrfs', value)

    @property
    def DistinguisherMode(self):
        """
        Returns
        -------
        - str(global | local): Specifies which part of the route distinguisher you want to increment.
        """
        return self._get_attribute('distinguisherMode')
    @DistinguisherMode.setter
    def DistinguisherMode(self, value):
        self._set_attribute('distinguisherMode', value)

    @property
    def DistinguisherStep(self):
        """
        Returns
        -------
        - number: The size of the increment step to be used with the part of the route distinguisher which will be incremented. (default = 1)
        """
        return self._get_attribute('distinguisherStep')
    @DistinguisherStep.setter
    def DistinguisherStep(self, value):
        self._set_attribute('distinguisherStep', value)

    @property
    def DistinguisherType(self):
        """
        Returns
        -------
        - str(as | ip | asNumber2): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        """
        return self._get_attribute('distinguisherType')
    @DistinguisherType.setter
    def DistinguisherType(self, value):
        self._set_attribute('distinguisherType', value)

    @property
    def EnableAggregator(self):
        """
        Returns
        -------
        - bool: Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        """
        return self._get_attribute('enableAggregator')
    @EnableAggregator.setter
    def EnableAggregator(self, value):
        self._set_attribute('enableAggregator', value)

    @property
    def EnableAsPath(self):
        """
        Returns
        -------
        - bool: Enables the generation of AS Path related items.
        """
        return self._get_attribute('enableAsPath')
    @EnableAsPath.setter
    def EnableAsPath(self, value):
        self._set_attribute('enableAsPath', value)

    @property
    def EnableAtomicAggregator(self):
        """
        Returns
        -------
        - bool: Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        """
        return self._get_attribute('enableAtomicAggregator')
    @EnableAtomicAggregator.setter
    def EnableAtomicAggregator(self, value):
        self._set_attribute('enableAtomicAggregator', value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        """
        return self._get_attribute('enableCluster')
    @EnableCluster.setter
    def EnableCluster(self, value):
        self._set_attribute('enableCluster', value)

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - bool: Enables the generation of a COMMUNITY attribute list. (default = false)
        """
        return self._get_attribute('enableCommunity')
    @EnableCommunity.setter
    def EnableCommunity(self, value):
        self._set_attribute('enableCommunity', value)

    @property
    def EnableGenerateUniqueRoutes(self):
        """
        Returns
        -------
        - bool: When set to 1, each router generates a different IP address range. When not enabled, each router will advertise the route range as is.
        """
        return self._get_attribute('enableGenerateUniqueRoutes')
    @EnableGenerateUniqueRoutes.setter
    def EnableGenerateUniqueRoutes(self, value):
        self._set_attribute('enableGenerateUniqueRoutes', value)

    @property
    def EnableLocalPref(self):
        """
        Returns
        -------
        - bool: Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        """
        return self._get_attribute('enableLocalPref')
    @EnableLocalPref.setter
    def EnableLocalPref(self, value):
        self._set_attribute('enableLocalPref', value)

    @property
    def EnableMed(self):
        """
        Returns
        -------
        - bool: Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        """
        return self._get_attribute('enableMed')
    @EnableMed.setter
    def EnableMed(self, value):
        self._set_attribute('enableMed', value)

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - bool: Enables the generation of a NEXT HOP attribute. (default = true)
        """
        return self._get_attribute('enableNextHop')
    @EnableNextHop.setter
    def EnableNextHop(self, value):
        self._set_attribute('enableNextHop', value)

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGIN attribute. (default = true)
        """
        return self._get_attribute('enableOrigin')
    @EnableOrigin.setter
    def EnableOrigin(self, value):
        self._set_attribute('enableOrigin', value)

    @property
    def EnableOriginator(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        """
        return self._get_attribute('enableOriginator')
    @EnableOriginator.setter
    def EnableOriginator(self, value):
        self._set_attribute('enableOriginator', value)

    @property
    def EnableUseTraditionalNlri(self):
        """
        Returns
        -------
        - bool: If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        """
        return self._get_attribute('enableUseTraditionalNlri')
    @EnableUseTraditionalNlri.setter
    def EnableUseTraditionalNlri(self, value):
        self._set_attribute('enableUseTraditionalNlri', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the UMH route range.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FirstRoute(self):
        """
        Returns
        -------
        - str: First route in route range
        """
        return self._get_attribute('firstRoute')
    @FirstRoute.setter
    def FirstRoute(self, value):
        self._set_attribute('firstRoute', value)

    @property
    def IncludeSourceAsExtendedCommunityPresent(self):
        """
        Returns
        -------
        - bool: If for a given MVPN BGP is used for exchanging C-multicast routes, or if segmented
        """
        return self._get_attribute('includeSourceAsExtendedCommunityPresent')
    @IncludeSourceAsExtendedCommunityPresent.setter
    def IncludeSourceAsExtendedCommunityPresent(self, value):
        self._set_attribute('includeSourceAsExtendedCommunityPresent', value)

    @property
    def IncludeVrfRouteImportExtendedCommunityPresent(self):
        """
        Returns
        -------
        - bool: Defines the route target extended community.
        """
        return self._get_attribute('includeVrfRouteImportExtendedCommunityPresent')
    @IncludeVrfRouteImportExtendedCommunityPresent.setter
    def IncludeVrfRouteImportExtendedCommunityPresent(self, value):
        self._set_attribute('includeVrfRouteImportExtendedCommunityPresent', value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): The type of IP address in nextworkAddress.
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def LocalPref(self):
        """
        Returns
        -------
        - number: The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        """
        return self._get_attribute('localPref')
    @LocalPref.setter
    def LocalPref(self, value):
        self._set_attribute('localPref', value)

    @property
    def MaskWidth(self):
        """
        Returns
        -------
        - number: Mask width of route range
        """
        return self._get_attribute('maskWidth')
    @MaskWidth.setter
    def MaskWidth(self, value):
        self._set_attribute('maskWidth', value)

    @property
    def MaskWidthTo(self):
        """
        Returns
        -------
        - number: mask width of last route range
        """
        return self._get_attribute('maskWidthTo')
    @MaskWidthTo.setter
    def MaskWidthTo(self, value):
        self._set_attribute('maskWidthTo', value)

    @property
    def Med(self):
        """
        Returns
        -------
        - number: The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        """
        return self._get_attribute('med')
    @Med.setter
    def Med(self, value):
        self._set_attribute('med', value)

    @property
    def NextHopIpAddress(self):
        """
        Returns
        -------
        - str: The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        """
        return self._get_attribute('nextHopIpAddress')
    @NextHopIpAddress.setter
    def NextHopIpAddress(self, value):
        self._set_attribute('nextHopIpAddress', value)

    @property
    def NextHopMode(self):
        """
        Returns
        -------
        - str(nextHopIncrement | fixed | incrementPerPrefix): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        """
        return self._get_attribute('nextHopMode')
    @NextHopMode.setter
    def NextHopMode(self, value):
        self._set_attribute('nextHopMode', value)

    @property
    def NextHopSetMode(self):
        """
        Returns
        -------
        - str(sameAsLocalIp | setManually): Indicates now to set the next hop IP address.
        """
        return self._get_attribute('nextHopSetMode')
    @NextHopSetMode.setter
    def NextHopSetMode(self, value):
        self._set_attribute('nextHopSetMode', value)

    @property
    def OriginProtocol(self):
        """
        Returns
        -------
        - str(igp | egp | incomplete): An indication of where the route entry originated.
        """
        return self._get_attribute('originProtocol')
    @OriginProtocol.setter
    def OriginProtocol(self, value):
        self._set_attribute('originProtocol', value)

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - str: The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        """
        return self._get_attribute('originatorId')
    @OriginatorId.setter
    def OriginatorId(self, value):
        self._set_attribute('originatorId', value)

    @property
    def PackingFrom(self):
        """
        Returns
        -------
        - number: Initial number of route packed in one BGP update
        """
        return self._get_attribute('packingFrom')
    @PackingFrom.setter
    def PackingFrom(self, value):
        self._set_attribute('packingFrom', value)

    @property
    def PackingTo(self):
        """
        Returns
        -------
        - number: Final number of routes packed in one BGP update
        """
        return self._get_attribute('packingTo')
    @PackingTo.setter
    def PackingTo(self, value):
        self._set_attribute('packingTo', value)

    @property
    def RouteCountPerVrfs(self):
        """
        Returns
        -------
        - number: Number of route per VRF
        """
        return self._get_attribute('routeCountPerVrfs')
    @RouteCountPerVrfs.setter
    def RouteCountPerVrfs(self, value):
        self._set_attribute('routeCountPerVrfs', value)

    @property
    def RouteStepAcrossVrfs(self):
        """
        Returns
        -------
        - str: The route increment value across VRFs.
        """
        return self._get_attribute('routeStepAcrossVrfs')
    @RouteStepAcrossVrfs.setter
    def RouteStepAcrossVrfs(self, value):
        self._set_attribute('routeStepAcrossVrfs', value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: step
        """
        return self._get_attribute('step')
    @Step.setter
    def Step(self, value):
        self._set_attribute('step', value)

    def update(self, AggregatorAsNumber=None, AggregatorIdIncrementMode=None, AggregatorIpAddress=None, DistinguisherAsNumber=None, DistinguisherAsNumberStep=None, DistinguisherAsNumberStepAcrossVrfs=None, DistinguisherAssignedNumber=None, DistinguisherAssignedNumberStep=None, DistinguisherAssignedNumberStepAcrossVrfs=None, DistinguisherCount=None, DistinguisherCountPerVrf=None, DistinguisherIpAddress=None, DistinguisherIpAddressStep=None, DistinguisherIpAddressStepAcrossVrfs=None, DistinguisherMode=None, DistinguisherStep=None, DistinguisherType=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregator=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, EnableUseTraditionalNlri=None, Enabled=None, FirstRoute=None, IncludeSourceAsExtendedCommunityPresent=None, IncludeVrfRouteImportExtendedCommunityPresent=None, IpType=None, LocalPref=None, MaskWidth=None, MaskWidthTo=None, Med=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, OriginProtocol=None, OriginatorId=None, PackingFrom=None, PackingTo=None, RouteCountPerVrfs=None, RouteStepAcrossVrfs=None, Step=None):
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
        return self._update(locals())

    def add(self, AggregatorAsNumber=None, AggregatorIdIncrementMode=None, AggregatorIpAddress=None, DistinguisherAsNumber=None, DistinguisherAsNumberStep=None, DistinguisherAsNumberStepAcrossVrfs=None, DistinguisherAssignedNumber=None, DistinguisherAssignedNumberStep=None, DistinguisherAssignedNumberStepAcrossVrfs=None, DistinguisherCount=None, DistinguisherCountPerVrf=None, DistinguisherIpAddress=None, DistinguisherIpAddressStep=None, DistinguisherIpAddressStepAcrossVrfs=None, DistinguisherMode=None, DistinguisherStep=None, DistinguisherType=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregator=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, EnableUseTraditionalNlri=None, Enabled=None, FirstRoute=None, IncludeSourceAsExtendedCommunityPresent=None, IncludeVrfRouteImportExtendedCommunityPresent=None, IpType=None, LocalPref=None, MaskWidth=None, MaskWidthTo=None, Med=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, OriginProtocol=None, OriginatorId=None, PackingFrom=None, PackingTo=None, RouteCountPerVrfs=None, RouteStepAcrossVrfs=None, Step=None):
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
        return self._create(locals())

    def remove(self):
        """Deletes all the contained umhSelectionRouteRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AggregatorAsNumber=None, AggregatorIdIncrementMode=None, AggregatorIpAddress=None, DistinguisherAsNumber=None, DistinguisherAsNumberStep=None, DistinguisherAsNumberStepAcrossVrfs=None, DistinguisherAssignedNumber=None, DistinguisherAssignedNumberStep=None, DistinguisherAssignedNumberStepAcrossVrfs=None, DistinguisherCount=None, DistinguisherCountPerVrf=None, DistinguisherIpAddress=None, DistinguisherIpAddressStep=None, DistinguisherIpAddressStepAcrossVrfs=None, DistinguisherMode=None, DistinguisherStep=None, DistinguisherType=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregator=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, EnableUseTraditionalNlri=None, Enabled=None, FirstRoute=None, IncludeSourceAsExtendedCommunityPresent=None, IncludeVrfRouteImportExtendedCommunityPresent=None, IpType=None, LocalPref=None, MaskWidth=None, MaskWidthTo=None, Med=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, OriginProtocol=None, OriginatorId=None, PackingFrom=None, PackingTo=None, RouteCountPerVrfs=None, RouteStepAcrossVrfs=None, Step=None):
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
        return self._select(locals())

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
