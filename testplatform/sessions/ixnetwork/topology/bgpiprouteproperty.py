# Copyright 1997 - 2018 by IXIA Keysight
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


class BgpIPRouteProperty(Base):
	"""The BgpIPRouteProperty class encapsulates a user managed bgpIPRouteProperty node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the BgpIPRouteProperty property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'bgpIPRouteProperty'

	def __init__(self, parent):
		super(BgpIPRouteProperty, self).__init__(parent)

	@property
	def Rfc8277LabelStack(self):
		"""An instance of the Rfc8277LabelStack class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rfc8277labelstack.Rfc8277LabelStack)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rfc8277labelstack import Rfc8277LabelStack
		return Rfc8277LabelStack(self)

	@property
	def BgpAigpList(self):
		"""An instance of the BgpAigpList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaigplist.BgpAigpList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaigplist import BgpAigpList
		return BgpAigpList(self)

	@property
	def BgpAsPathSegmentList(self):
		"""An instance of the BgpAsPathSegmentList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist.BgpAsPathSegmentList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist import BgpAsPathSegmentList
		return BgpAsPathSegmentList(self)

	@property
	def BgpClusterIdList(self):
		"""An instance of the BgpClusterIdList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist.BgpClusterIdList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist import BgpClusterIdList
		return BgpClusterIdList(self)

	@property
	def BgpCommunitiesList(self):
		"""An instance of the BgpCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist.BgpCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist import BgpCommunitiesList
		return BgpCommunitiesList(self)

	@property
	def BgpExtendedCommunitiesList(self):
		"""An instance of the BgpExtendedCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist.BgpExtendedCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist import BgpExtendedCommunitiesList
		return BgpExtendedCommunitiesList(self)

	@property
	def BgpNonVPNRRLargeCommunitiesList(self):
		"""An instance of the BgpNonVPNRRLargeCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist.BgpNonVPNRRLargeCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist import BgpNonVPNRRLargeCommunitiesList
		return BgpNonVPNRRLargeCommunitiesList(self)

	@property
	def CMacProperties(self):
		"""An instance of the CMacProperties class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties.CMacProperties)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties import CMacProperties
		return CMacProperties(self)

	@property
	def EvpnIPv4PrefixRange(self):
		"""An instance of the EvpnIPv4PrefixRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange.EvpnIPv4PrefixRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange import EvpnIPv4PrefixRange
		return EvpnIPv4PrefixRange(self)

	@property
	def EvpnIPv6PrefixRange(self):
		"""An instance of the EvpnIPv6PrefixRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange.EvpnIPv6PrefixRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange import EvpnIPv6PrefixRange
		return EvpnIPv6PrefixRange(self)

	@property
	def GenerateIpv6RoutesParams(self):
		"""An instance of the GenerateIpv6RoutesParams class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.generateipv6routesparams.GenerateIpv6RoutesParams)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.generateipv6routesparams import GenerateIpv6RoutesParams
		return GenerateIpv6RoutesParams(self)._select()

	@property
	def GenerateRoutesParams(self):
		"""An instance of the GenerateRoutesParams class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.generateroutesparams.GenerateRoutesParams)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.generateroutesparams import GenerateRoutesParams
		return GenerateRoutesParams(self)._select()

	@property
	def ImportBgpRoutesParams(self):
		"""An instance of the ImportBgpRoutesParams class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.importbgproutesparams.ImportBgpRoutesParams)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.importbgproutesparams import ImportBgpRoutesParams
		return ImportBgpRoutesParams(self)._select()

	@property
	def OverridePeerAsSetMode(self):
		"""Override Peer AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('OverridePeerAsSetMode')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AddPathId(self):
		"""BGP ADD Path Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('addPathId')

	@property
	def AdvertiseAsBGPLSPrefix(self):
		"""Advertise as BGP-LS Prefix

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseAsBGPLSPrefix')

	@property
	def AdvertiseAsBgp3107(self):
		"""Will cause this route to be sent as BGP 3107 MPLS SAFI route

		Returns:
			bool
		"""
		return self._get_attribute('advertiseAsBgp3107')
	@AdvertiseAsBgp3107.setter
	def AdvertiseAsBgp3107(self, value):
		self._set_attribute('advertiseAsBgp3107', value)

	@property
	def AdvertiseAsBgp3107Sr(self):
		"""Will cause this route to be sent as BGP 3107 SR MPLS SAFI route

		Returns:
			bool
		"""
		return self._get_attribute('advertiseAsBgp3107Sr')
	@AdvertiseAsBgp3107Sr.setter
	def AdvertiseAsBgp3107Sr(self, value):
		self._set_attribute('advertiseAsBgp3107Sr', value)

	@property
	def AdvertiseAsRfc8277(self):
		"""Will cause this route to be sent as RFC 8277 MPLS SAFI route

		Returns:
			bool
		"""
		return self._get_attribute('advertiseAsRfc8277')
	@AdvertiseAsRfc8277.setter
	def AdvertiseAsRfc8277(self, value):
		self._set_attribute('advertiseAsRfc8277', value)

	@property
	def AdvertiseNexthopAsV4(self):
		"""Advertise Nexthop as V4

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseNexthopAsV4')

	@property
	def AggregatorAs(self):
		"""Aggregator AS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorAs')

	@property
	def AggregatorId(self):
		"""Aggregator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorId')

	@property
	def AggregatorIdMode(self):
		"""Aggregator ID Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorIdMode')

	@property
	def AsNumSuffixRange(self):
		"""Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asNumSuffixRange')

	@property
	def AsPathASString(self):
		"""Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.

		Returns:
			list(str)
		"""
		return self._get_attribute('asPathASString')

	@property
	def AsPathPerRoute(self):
		"""When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asPathPerRoute')

	@property
	def AsRandomSeed(self):
		"""Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asRandomSeed')

	@property
	def AsSegDist(self):
		"""Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSegDist')

	@property
	def AsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSetMode')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def Delay(self):
		"""Delay

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('delay')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def Downtime(self):
		"""Downtime In Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('downtime')

	@property
	def EnableAddPath(self):
		"""Enable Path ID when ADD Path Capability is enabled in BGP Peer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAddPath')

	@property
	def EnableAggregatorId(self):
		"""Enable Aggregator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAggregatorId')

	@property
	def EnableAigp(self):
		"""Enable AIGP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAigp')

	@property
	def EnableAsPathSegments(self):
		"""Enable Non-Random AS Path Segments

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAsPathSegments')

	@property
	def EnableAtomicAggregate(self):
		"""Enable Atomic Aggregate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAtomicAggregate')

	@property
	def EnableCluster(self):
		"""Enable Cluster

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCluster')

	@property
	def EnableCommunity(self):
		"""Enable Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCommunity')

	@property
	def EnableExtendedCommunity(self):
		"""Enable Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableExtendedCommunity')

	@property
	def EnableFlapping(self):
		"""Enable Flapping

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableFlapping')

	@property
	def EnableLargeCommunities(self):
		"""Enable Large Communities Attribute

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLargeCommunities')

	@property
	def EnableLocalPreference(self):
		"""Enable Local Preference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLocalPreference')

	@property
	def EnableMultiExitDiscriminator(self):
		"""Enable Multi Exit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableMultiExitDiscriminator')

	@property
	def EnableNextHop(self):
		"""Enable Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableNextHop')

	@property
	def EnableOrigin(self):
		"""Enable Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOrigin')

	@property
	def EnableOriginatorId(self):
		"""Enable Originator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOriginatorId')

	@property
	def EnableRandomAsPath(self):
		"""Enables generation/advertisement of Random AS Path Segments.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableRandomAsPath')

	@property
	def EnableSRGB(self):
		"""Enable SRGB TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableSRGB')

	@property
	def EnableWeight(self):
		"""Enable Weight

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableWeight')

	@property
	def FlapFromRouteIndex(self):
		"""Flap From Route Index

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flapFromRouteIndex')

	@property
	def FlapToRouteIndex(self):
		"""Flap To Route Index

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flapToRouteIndex')

	@property
	def IncrementMode(self):
		"""Either Fixed or Increment

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('incrementMode')

	@property
	def Ipv4NextHop(self):
		"""IPv4 Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4NextHop')

	@property
	def Ipv6NextHop(self):
		"""IPv6 Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6NextHop')

	@property
	def LabelEnd(self):
		"""Route Range Label End

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelEnd')

	@property
	def LabelStart(self):
		"""Route Range Label Start

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelStart')

	@property
	def LabelStep(self):
		"""Route Range Label Step

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelStep')

	@property
	def LocalPreference(self):
		"""Local Preference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localPreference')

	@property
	def MaxASNumPerSegment(self):
		"""Maximum Number Of AS Numbers generated per Segment

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxASNumPerSegment')

	@property
	def MaxNoOfASPathSegmentsPerRouteRange(self):
		"""Maximum Number Of AS Path Segments Per Route Range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxNoOfASPathSegmentsPerRouteRange')

	@property
	def MinASNumPerSegment(self):
		"""Minimum Number Of AS Numbers generated per Segments.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minASNumPerSegment')

	@property
	def MinNoOfASPathSegmentsPerRouteRange(self):
		"""Minimum Number Of AS Path Segments Per Route Range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minNoOfASPathSegmentsPerRouteRange')

	@property
	def MultiExitDiscriminator(self):
		"""Multi Exit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multiExitDiscriminator')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NextHopIPType(self):
		"""Set Next Hop IP Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nextHopIPType')

	@property
	def NextHopIncrementMode(self):
		"""Next Hop Increment Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nextHopIncrementMode')

	@property
	def NextHopType(self):
		"""Set Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nextHopType')

	@property
	def NoOfASPathSegmentsPerRouteRange(self):
		"""Number Of non-random or manually configured AS Path Segments Per Route Range

		Returns:
			number
		"""
		return self._get_attribute('noOfASPathSegmentsPerRouteRange')
	@NoOfASPathSegmentsPerRouteRange.setter
	def NoOfASPathSegmentsPerRouteRange(self, value):
		self._set_attribute('noOfASPathSegmentsPerRouteRange', value)

	@property
	def NoOfClusters(self):
		"""Number of Clusters

		Returns:
			number
		"""
		return self._get_attribute('noOfClusters')
	@NoOfClusters.setter
	def NoOfClusters(self, value):
		self._set_attribute('noOfClusters', value)

	@property
	def NoOfCommunities(self):
		"""Number of Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfCommunities')
	@NoOfCommunities.setter
	def NoOfCommunities(self, value):
		self._set_attribute('noOfCommunities', value)

	@property
	def NoOfExternalCommunities(self):
		"""Number of Extended Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfExternalCommunities')
	@NoOfExternalCommunities.setter
	def NoOfExternalCommunities(self, value):
		self._set_attribute('noOfExternalCommunities', value)

	@property
	def NoOfLabels(self):
		"""Number of Labels

		Returns:
			number
		"""
		return self._get_attribute('noOfLabels')
	@NoOfLabels.setter
	def NoOfLabels(self, value):
		self._set_attribute('noOfLabels', value)

	@property
	def NoOfLargeCommunities(self):
		"""Number of Large Communities (Should be in the range 1-32)

		Returns:
			number
		"""
		return self._get_attribute('noOfLargeCommunities')
	@NoOfLargeCommunities.setter
	def NoOfLargeCommunities(self, value):
		self._set_attribute('noOfLargeCommunities', value)

	@property
	def NoOfTlvs(self):
		"""Number of TLVs

		Returns:
			number
		"""
		return self._get_attribute('noOfTlvs')
	@NoOfTlvs.setter
	def NoOfTlvs(self, value):
		self._set_attribute('noOfTlvs', value)

	@property
	def Origin(self):
		"""Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('origin')

	@property
	def OriginatorId(self):
		"""Originator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('originatorId')

	@property
	def PackingFrom(self):
		"""Packing From

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('packingFrom')

	@property
	def PackingTo(self):
		"""Packing To

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('packingTo')

	@property
	def PartialFlap(self):
		"""Partial Flap

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('partialFlap')

	@property
	def RouteOrigin(self):
		"""Route Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routeOrigin')

	@property
	def SegmentId(self):
		"""SID or Segment ID, converts to label value by adding offset into SRGB Start Label Value.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('segmentId')

	@property
	def SendMulticastWithProperSAFI(self):
		"""Send Routes with SAFI as Multicast (2)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendMulticastWithProperSAFI')

	@property
	def SkipMulticast(self):
		"""Skip the Multicast routes for this route range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('skipMulticast')

	@property
	def SpecialLabel(self):
		"""If we are emulating Egress then Label field may not hold Label value calculated based on SRGB and Offset but Implicit IPv4 NULL or Explicit NULL

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('specialLabel')

	@property
	def Uptime(self):
		"""Uptime In Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('uptime')

	@property
	def UseTraditionalNlri(self):
		"""Use Traditional NLRI

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useTraditionalNlri')

	@property
	def Weight(self):
		"""Weight

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('weight')

	def update(self, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfLargeCommunities=None, NoOfTlvs=None):
		"""Updates a child instance of bgpIPRouteProperty on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
			NoOfTlvs (number): Number of TLVs

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfLargeCommunities=None, NoOfTlvs=None):
		"""Adds a new bgpIPRouteProperty node on the server and retrieves it in this instance.

		Args:
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
			NoOfTlvs (number): Number of TLVs

		Returns:
			self: This instance with all currently retrieved bgpIPRouteProperty data using find and the newly added bgpIPRouteProperty data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the bgpIPRouteProperty data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, AsPathASString=None, Count=None, DescriptiveName=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfLargeCommunities=None, NoOfTlvs=None):
		"""Finds and retrieves bgpIPRouteProperty data from the server.

		All named parameters support regex and can be used to selectively retrieve bgpIPRouteProperty data from the server.
		By default the find method takes no parameters and will retrieve all bgpIPRouteProperty data from the server.

		Args:
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			AsPathASString (list(str)): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
			NoOfTlvs (number): Number of TLVs

		Returns:
			self: This instance with matching bgpIPRouteProperty data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bgpIPRouteProperty data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bgpIPRouteProperty data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, OverridePeerAsSetMode=None, Active=None, AddPathId=None, AdvertiseAsBGPLSPrefix=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Delay=None, Downtime=None, EnableAddPath=None, EnableAggregatorId=None, EnableAigp=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLargeCommunities=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSRGB=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncrementMode=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, RouteOrigin=None, SegmentId=None, SendMulticastWithProperSAFI=None, SkipMulticast=None, SpecialLabel=None, Uptime=None, UseTraditionalNlri=None, Weight=None):
		"""Base class infrastructure that gets a list of bgpIPRouteProperty device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			OverridePeerAsSetMode (str): optional regex of OverridePeerAsSetMode
			Active (str): optional regex of active
			AddPathId (str): optional regex of addPathId
			AdvertiseAsBGPLSPrefix (str): optional regex of advertiseAsBGPLSPrefix
			AdvertiseNexthopAsV4 (str): optional regex of advertiseNexthopAsV4
			AggregatorAs (str): optional regex of aggregatorAs
			AggregatorId (str): optional regex of aggregatorId
			AggregatorIdMode (str): optional regex of aggregatorIdMode
			AsNumSuffixRange (str): optional regex of asNumSuffixRange
			AsPathPerRoute (str): optional regex of asPathPerRoute
			AsRandomSeed (str): optional regex of asRandomSeed
			AsSegDist (str): optional regex of asSegDist
			AsSetMode (str): optional regex of asSetMode
			Delay (str): optional regex of delay
			Downtime (str): optional regex of downtime
			EnableAddPath (str): optional regex of enableAddPath
			EnableAggregatorId (str): optional regex of enableAggregatorId
			EnableAigp (str): optional regex of enableAigp
			EnableAsPathSegments (str): optional regex of enableAsPathSegments
			EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
			EnableCluster (str): optional regex of enableCluster
			EnableCommunity (str): optional regex of enableCommunity
			EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
			EnableFlapping (str): optional regex of enableFlapping
			EnableLargeCommunities (str): optional regex of enableLargeCommunities
			EnableLocalPreference (str): optional regex of enableLocalPreference
			EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
			EnableNextHop (str): optional regex of enableNextHop
			EnableOrigin (str): optional regex of enableOrigin
			EnableOriginatorId (str): optional regex of enableOriginatorId
			EnableRandomAsPath (str): optional regex of enableRandomAsPath
			EnableSRGB (str): optional regex of enableSRGB
			EnableWeight (str): optional regex of enableWeight
			FlapFromRouteIndex (str): optional regex of flapFromRouteIndex
			FlapToRouteIndex (str): optional regex of flapToRouteIndex
			IncrementMode (str): optional regex of incrementMode
			Ipv4NextHop (str): optional regex of ipv4NextHop
			Ipv6NextHop (str): optional regex of ipv6NextHop
			LabelEnd (str): optional regex of labelEnd
			LabelStart (str): optional regex of labelStart
			LabelStep (str): optional regex of labelStep
			LocalPreference (str): optional regex of localPreference
			MaxASNumPerSegment (str): optional regex of maxASNumPerSegment
			MaxNoOfASPathSegmentsPerRouteRange (str): optional regex of maxNoOfASPathSegmentsPerRouteRange
			MinASNumPerSegment (str): optional regex of minASNumPerSegment
			MinNoOfASPathSegmentsPerRouteRange (str): optional regex of minNoOfASPathSegmentsPerRouteRange
			MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
			NextHopIPType (str): optional regex of nextHopIPType
			NextHopIncrementMode (str): optional regex of nextHopIncrementMode
			NextHopType (str): optional regex of nextHopType
			Origin (str): optional regex of origin
			OriginatorId (str): optional regex of originatorId
			PackingFrom (str): optional regex of packingFrom
			PackingTo (str): optional regex of packingTo
			PartialFlap (str): optional regex of partialFlap
			RouteOrigin (str): optional regex of routeOrigin
			SegmentId (str): optional regex of segmentId
			SendMulticastWithProperSAFI (str): optional regex of sendMulticastWithProperSAFI
			SkipMulticast (str): optional regex of skipMulticast
			SpecialLabel (str): optional regex of specialLabel
			Uptime (str): optional regex of uptime
			UseTraditionalNlri (str): optional regex of useTraditionalNlri
			Weight (str): optional regex of weight

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def AgeOutRoutes(self, *args, **kwargs):
		"""Executes the ageOutRoutes operation on the server.

		Age out percentage of BGP Routes in a Route Range

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ageOutRoutes(Percentage:number)
			Args:
				args[0] is Percentage (number): This parameter requires a percentage of type kInteger

		ageOutRoutes(Percentage:number, SessionIndices:list)
			Args:
				args[0] is Percentage (number): This parameter requires a percentage of type kInteger
				args[1] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		ageOutRoutes(SessionIndices:string, Percentage:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a percentage of type kInteger
				args[1] is Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ageOutRoutes', payload=payload, response_object=None)

	def Ageoutroutes(self, *args, **kwargs):
		"""Executes the ageoutroutes operation on the server.

		Completely/Partially age out routes contained in this route range.

		ageoutroutes(Arg2:list, Arg3:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
				args[1] is Arg3 (number): What percentage of routes to age out. 100% means all routes.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ageoutroutes', payload=payload, response_object=None)

	def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		fetchAndUpdateConfigFromCloud(Mode:string)
			Args:
				args[0] is Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

	def GenerateIpv6Routes(self, *args, **kwargs):
		"""Executes the generateIpv6Routes operation on the server.

		Generate Primary and Duplicate Routes with advanced prefix length distribution options.

		generateIpv6Routes(Arg2:number, Arg3:number, Arg4:number, Arg5:string, Arg6:string, Arg7:enum, Arg8:enum, Arg9:href, Arg10:number, Arg11:number, Arg12:bool, Arg13:bool, Arg14:string, Arg15:string, Arg16:string)list
			Args:
				args[0] is Arg2 (number): Number of Primary Routes per Device.
				args[1] is Arg3 (number): Percentage to Duplicate Primary Routes per Device.
				args[2] is Arg4 (number): Number of Routes per Route Range.
				args[3] is Arg5 (str): Network Address Start Value.
				args[4] is Arg6 (str): Network Address Step Value.
				args[5] is Arg7 (str(custom|even|exponential|fixed|internet|random)): Prefix Length Distribution Type.
				args[6] is Arg8 (str(perDevice|perPort|perTopology)): Prefix Length Distribution Scope.
				args[7] is Arg9 (obj(ixnetwork_restpy.files.Files)): Source file having custom distribution information.
				args[8] is Arg10 (number): Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
				args[9] is Arg11 (number): Prefix Length End Value. Applicable only for Even and Exponential distribution type.
				args[10] is Arg12 (bool): Do not include Loopback Address in the generated Address Range
				args[11] is Arg13 (bool): Do not include Multicast Address in the generated Address Range
				args[12] is Arg14 (str): Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: aa:0:1:b: - bb:0:2:c:, aa00: - bb00:1
				args[13] is Arg15 (str): AS Path Suffix for Primary Routes
				args[14] is Arg16 (str): AS Path Suffix for Duplicate Routes

			Returns:
				list(str): ID to associate each async action invocation.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('generateIpv6Routes', payload=payload, response_object=None)

	def GenerateRoutes(self, *args, **kwargs):
		"""Executes the generateRoutes operation on the server.

		Generate Primary and Duplicate Routes with advanced prefix length distribution options.

		generateRoutes(Arg2:number, Arg3:number, Arg4:number, Arg5:string, Arg6:string, Arg7:enum, Arg8:enum, Arg9:href, Arg10:number, Arg11:number, Arg12:bool, Arg13:bool, Arg14:string, Arg15:string, Arg16:string)list
			Args:
				args[0] is Arg2 (number): Number of Primary Routes per Device.
				args[1] is Arg3 (number): Percentage to Duplicate Primary Routes per Device.
				args[2] is Arg4 (number): Number of Routes per Route Range.
				args[3] is Arg5 (str): Network Address Start Value.
				args[4] is Arg6 (str): Network Address Step Value.
				args[5] is Arg7 (str(custom|even|exponential|fixed|internet|random)): Prefix Length Distribution Type.
				args[6] is Arg8 (str(perDevice|perPort|perTopology)): Prefix Length Distribution Scope.
				args[7] is Arg9 (obj(ixnetwork_restpy.files.Files)): Source file having custom distribution information.
				args[8] is Arg10 (number): Prefix Length Start Value. Applicable only for Fixed, Even and Exponential distribution type.
				args[9] is Arg11 (number): Prefix Length End Value. Applicable only for Even and Exponential distribution type.
				args[10] is Arg12 (bool): Do not include Loopback Address in the generated Address Range
				args[11] is Arg13 (bool): Do not include Multicast Address in the generated Address Range
				args[12] is Arg14 (str): Address Ranges that will be skipped. You can provide multiple ranges separated by ','. Example: 192.0.0.0 - 192.255.255.255
				args[13] is Arg15 (str): AS Path Suffix for Primary Routes
				args[14] is Arg16 (str): AS Path Suffix for Duplicate Routes

			Returns:
				list(str): ID to associate each async action invocation.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('generateRoutes', payload=payload, response_object=None)

	def ImportBgpRoutes(self, *args, **kwargs):
		"""Executes the importBgpRoutes operation on the server.

		Import IPv4 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

		importBgpRoutes(Arg2:enum, Arg3:bool, Arg4:enum, Arg5:enum, Arg6:href)list
			Args:
				args[0] is Arg2 (str(replicate|roundRobin)): Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.
				args[1] is Arg3 (bool): Import only the best routes (provided route file has this information).
				args[2] is Arg4 (str(overwriteTestersAddress|preserveFromFile)): Option for setting Next Hop modification type.
				args[3] is Arg5 (str(cisco|csv|juniper)): Import routes file type. Route import may fail in file type is not matching with the file being imported.
				args[4] is Arg6 (obj(ixnetwork_restpy.files.Files)): Select source file having route information.

			Returns:
				list(str): ID to associate each asynchronous action invocation.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('importBgpRoutes', payload=payload, response_object=None)

	def ReadvertiseRoutes(self, *args, **kwargs):
		"""Executes the readvertiseRoutes operation on the server.

		Re-advertise Aged out OSPF Routes in a Route Range

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		readvertiseRoutes()

		readvertiseRoutes(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		readvertiseRoutes(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('readvertiseRoutes', payload=payload, response_object=None)

	def Readvertiseroutes(self, *args, **kwargs):
		"""Executes the readvertiseroutes operation on the server.

		Readvertise only the aged-out routes contained in this route range.

		readvertiseroutes(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('readvertiseroutes', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start BGP Route Range

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Stop BGP Route Range

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)
