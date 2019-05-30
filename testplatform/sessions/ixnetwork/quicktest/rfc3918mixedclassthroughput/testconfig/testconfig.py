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


class TestConfig(Base):
	"""The TestConfig class encapsulates a required testConfig node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TestConfig property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'testConfig'

	def __init__(self, parent):
		super(TestConfig, self).__init__(parent)

	@property
	def ApplyMode(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('applyMode')
	@ApplyMode.setter
	def ApplyMode(self, value):
		self._set_attribute('applyMode', value)

	@property
	def AssignGroupType(self):
		"""Assigns the group type.

		Returns:
			str(accumulated|distributed)
		"""
		return self._get_attribute('assignGroupType')
	@AssignGroupType.setter
	def AssignGroupType(self, value):
		self._set_attribute('assignGroupType', value)

	@property
	def BackoffIteration(self):
		"""This enables the test to run an extra iteration for calculating the Backoff Latency.

		Returns:
			number
		"""
		return self._get_attribute('backoffIteration')
	@BackoffIteration.setter
	def BackoffIteration(self, value):
		self._set_attribute('backoffIteration', value)

	@property
	def BidirectionalOptionEnabled(self):
		"""If true, enables bidirectional option.

		Returns:
			bool
		"""
		return self._get_attribute('bidirectionalOptionEnabled')
	@BidirectionalOptionEnabled.setter
	def BidirectionalOptionEnabled(self, value):
		self._set_attribute('bidirectionalOptionEnabled', value)

	@property
	def BinaryBackoff(self):
		"""Specifies the percentage of binary backoff.

		Returns:
			number
		"""
		return self._get_attribute('binaryBackoff')
	@BinaryBackoff.setter
	def BinaryBackoff(self, value):
		self._set_attribute('binaryBackoff', value)

	@property
	def BinaryFrameLossUnit(self):
		"""The binary frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('binaryFrameLossUnit')
	@BinaryFrameLossUnit.setter
	def BinaryFrameLossUnit(self, value):
		self._set_attribute('binaryFrameLossUnit', value)

	@property
	def BinaryLoadUnit(self):
		"""The binary load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('binaryLoadUnit')
	@BinaryLoadUnit.setter
	def BinaryLoadUnit(self, value):
		self._set_attribute('binaryLoadUnit', value)

	@property
	def BinaryResolution(self):
		"""Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def BinarySearchType(self):
		"""The binary search type value.

		Returns:
			str(linear|perFlow|perPort|perTrafficItem)
		"""
		return self._get_attribute('binarySearchType')
	@BinarySearchType.setter
	def BinarySearchType(self, value):
		self._set_attribute('binarySearchType', value)

	@property
	def BinaryTolerance(self):
		"""The binary tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('binaryTolerance')
	@BinaryTolerance.setter
	def BinaryTolerance(self, value):
		self._set_attribute('binaryTolerance', value)

	@property
	def BurstSize(self):
		"""The number of packets that are sent in a burst.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CalculateJitter(self):
		"""If true, calculates jitter.

		Returns:
			bool
		"""
		return self._get_attribute('calculateJitter')
	@CalculateJitter.setter
	def CalculateJitter(self, value):
		self._set_attribute('calculateJitter', value)

	@property
	def CalculateLatency(self):
		"""If true, calculates the latency.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def ComboBackoff(self):
		"""The backoff combination of the test configuration.

		Returns:
			number
		"""
		return self._get_attribute('comboBackoff')
	@ComboBackoff.setter
	def ComboBackoff(self, value):
		self._set_attribute('comboBackoff', value)

	@property
	def ComboFrameLossUnit(self):
		"""The frame loss unit for traffic in binary.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('comboFrameLossUnit')
	@ComboFrameLossUnit.setter
	def ComboFrameLossUnit(self, value):
		self._set_attribute('comboFrameLossUnit', value)

	@property
	def ComboLoadUnit(self):
		"""The combination of load units. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('comboLoadUnit')
	@ComboLoadUnit.setter
	def ComboLoadUnit(self, value):
		self._set_attribute('comboLoadUnit', value)

	@property
	def ComboResolution(self):
		"""The combined resolution value.

		Returns:
			number
		"""
		return self._get_attribute('comboResolution')
	@ComboResolution.setter
	def ComboResolution(self, value):
		self._set_attribute('comboResolution', value)

	@property
	def ComboTolerance(self):
		"""The combined tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('comboTolerance')
	@ComboTolerance.setter
	def ComboTolerance(self, value):
		self._set_attribute('comboTolerance', value)

	@property
	def CountRandomFrameSize(self):
		"""If true, frame sizes are counted at random.

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def CountRandomLoadRate(self):
		"""The random count of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('countRandomLoadRate')
	@CountRandomLoadRate.setter
	def CountRandomLoadRate(self, value):
		self._set_attribute('countRandomLoadRate', value)

	@property
	def CustomLoadUnit(self):
		"""Specifies the custom load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def DelayAfterTransmit(self):
		"""The amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def Duration(self):
		"""The duration of the test in hours, which is used to calculate the number of frames to transmit.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableBackoffIteration(self):
		"""If true, enables back off iteration test.

		Returns:
			bool
		"""
		return self._get_attribute('enableBackoffIteration')
	@EnableBackoffIteration.setter
	def EnableBackoffIteration(self, value):
		self._set_attribute('enableBackoffIteration', value)

	@property
	def EnableDataIntegrity(self):
		"""enableDataIntegrity

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableExtraIterations(self):
		"""If true, more iterations are performed.

		Returns:
			str
		"""
		return self._get_attribute('enableExtraIterations')
	@EnableExtraIterations.setter
	def EnableExtraIterations(self, value):
		self._set_attribute('enableExtraIterations', value)

	@property
	def EnableFastConvergence(self):
		"""If true, the test perform iterations using the fast convergence duration configured.

		Returns:
			bool
		"""
		return self._get_attribute('enableFastConvergence')
	@EnableFastConvergence.setter
	def EnableFastConvergence(self, value):
		self._set_attribute('enableFastConvergence', value)

	@property
	def EnableLayer1Rate(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableLayer1Rate')
	@EnableLayer1Rate.setter
	def EnableLayer1Rate(self, value):
		self._set_attribute('enableLayer1Rate', value)

	@property
	def EnableLayer2(self):
		"""If true, enables Layer2 protocols.

		Returns:
			bool
		"""
		return self._get_attribute('enableLayer2')
	@EnableLayer2.setter
	def EnableLayer2(self, value):
		self._set_attribute('enableLayer2', value)

	@property
	def EnableLeaveGroup(self):
		"""If true, the leave group is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableLeaveGroup')
	@EnableLeaveGroup.setter
	def EnableLeaveGroup(self, value):
		self._set_attribute('enableLeaveGroup', value)

	@property
	def EnableMinFrameSize(self):
		"""If enabled, it shows the minimum frame size.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableMulticastQuerier(self):
		"""Enable Multicast Querier Settings

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticastQuerier')
	@EnableMulticastQuerier.setter
	def EnableMulticastQuerier(self, value):
		self._set_attribute('enableMulticastQuerier', value)

	@property
	def EnableOldStatsForReef(self):
		"""Enable old statistics for reef.

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def EnableSaturationIteration(self):
		"""If true, SaturationIteration in enabled .

		Returns:
			bool
		"""
		return self._get_attribute('enableSaturationIteration')
	@EnableSaturationIteration.setter
	def EnableSaturationIteration(self, value):
		self._set_attribute('enableSaturationIteration', value)

	@property
	def EnableStopTestOnHighLoss(self):
		"""The test stops in case of a high loss.

		Returns:
			bool
		"""
		return self._get_attribute('enableStopTestOnHighLoss')
	@EnableStopTestOnHighLoss.setter
	def EnableStopTestOnHighLoss(self, value):
		self._set_attribute('enableStopTestOnHighLoss', value)

	@property
	def ExtraIterationOffsets(self):
		"""This enables the test to run an extra iteration.

		Returns:
			str
		"""
		return self._get_attribute('extraIterationOffsets')
	@ExtraIterationOffsets.setter
	def ExtraIterationOffsets(self, value):
		self._set_attribute('extraIterationOffsets', value)

	@property
	def FastConvergence(self):
		"""If true, enables fast convergence.

		Returns:
			str
		"""
		return self._get_attribute('fastConvergence')
	@FastConvergence.setter
	def FastConvergence(self, value):
		self._set_attribute('fastConvergence', value)

	@property
	def FastConvergenceDuration(self):
		"""This enables the test to perform iterations using the fast convergence duration configured.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceDuration')
	@FastConvergenceDuration.setter
	def FastConvergenceDuration(self, value):
		self._set_attribute('fastConvergenceDuration', value)

	@property
	def FastConvergenceThreshold(self):
		"""This enables the test to perform iterations using the fast convergence threshold configured.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceThreshold')
	@FastConvergenceThreshold.setter
	def FastConvergenceThreshold(self, value):
		self._set_attribute('fastConvergenceThreshold', value)

	@property
	def FirstMulticastDestMACAddress(self):
		"""The first multicast destination MAC address.

		Returns:
			str
		"""
		return self._get_attribute('firstMulticastDestMACAddress')
	@FirstMulticastDestMACAddress.setter
	def FirstMulticastDestMACAddress(self, value):
		self._set_attribute('firstMulticastDestMACAddress', value)

	@property
	def FloodedFramesEnabled(self):
		"""Show Flooded Frames

		Returns:
			bool
		"""
		return self._get_attribute('floodedFramesEnabled')
	@FloodedFramesEnabled.setter
	def FloodedFramesEnabled(self, value):
		self._set_attribute('floodedFramesEnabled', value)

	@property
	def ForceRegenerate(self):
		"""Initiates a forced regeneration.

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameLossUnit(self):
		"""The frame loss unit.

		Returns:
			str
		"""
		return self._get_attribute('frameLossUnit')
	@FrameLossUnit.setter
	def FrameLossUnit(self, value):
		self._set_attribute('frameLossUnit', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.

		Returns:
			str(custom|customlist|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesizeImixList(self):
		"""The list of frame size to be used

		Returns:
			str
		"""
		return self._get_attribute('framesizeImixList')
	@FramesizeImixList.setter
	def FramesizeImixList(self, value):
		self._set_attribute('framesizeImixList', value)

	@property
	def FramesizeList(self):
		"""The list of frame sizes.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def Gap(self):
		"""It signifies the gap value for the protocol.

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""If true, enables the tracking option in aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def GroupCapacityGreaterThan(self):
		"""The integer that distinguishes the group capacity that could be greater than the specified integer.

		Returns:
			number
		"""
		return self._get_attribute('groupCapacityGreaterThan')
	@GroupCapacityGreaterThan.setter
	def GroupCapacityGreaterThan(self, value):
		self._set_attribute('groupCapacityGreaterThan', value)

	@property
	def GroupDistributionType(self):
		"""The group distribution type.

		Returns:
			str(acrossHosts|acrossPorts)
		"""
		return self._get_attribute('groupDistributionType')
	@GroupDistributionType.setter
	def GroupDistributionType(self, value):
		self._set_attribute('groupDistributionType', value)

	@property
	def IgmpV1Timeout(self):
		"""The IGMPv1 timeout value.

		Returns:
			number
		"""
		return self._get_attribute('igmpV1Timeout')
	@IgmpV1Timeout.setter
	def IgmpV1Timeout(self, value):
		self._set_attribute('igmpV1Timeout', value)

	@property
	def IgmpVersion(self):
		"""The igmp version .

		Returns:
			number
		"""
		return self._get_attribute('igmpVersion')
	@IgmpVersion.setter
	def IgmpVersion(self, value):
		self._set_attribute('igmpVersion', value)

	@property
	def Igmpv3MessageType(self):
		"""It gives details about the igmpv3 message type in the test configuration

		Returns:
			str(exclude|include)
		"""
		return self._get_attribute('igmpv3MessageType')
	@Igmpv3MessageType.setter
	def Igmpv3MessageType(self, value):
		self._set_attribute('igmpv3MessageType', value)

	@property
	def Igmpv3SourceAddrList(self):
		"""It gives details about the igmpv3 source address list in the test configuration

		Returns:
			str
		"""
		return self._get_attribute('igmpv3SourceAddrList')
	@Igmpv3SourceAddrList.setter
	def Igmpv3SourceAddrList(self, value):
		self._set_attribute('igmpv3SourceAddrList', value)

	@property
	def ImixAdd(self):
		"""Adds an imix data.

		Returns:
			str
		"""
		return self._get_attribute('imixAdd')
	@ImixAdd.setter
	def ImixAdd(self, value):
		self._set_attribute('imixAdd', value)

	@property
	def ImixData(self):
		"""Displays the imix Data.

		Returns:
			str
		"""
		return self._get_attribute('imixData')
	@ImixData.setter
	def ImixData(self, value):
		self._set_attribute('imixData', value)

	@property
	def ImixDataQoS(self):
		"""Enables Imix Data QoS

		Returns:
			bool
		"""
		return self._get_attribute('imixDataQoS')
	@ImixDataQoS.setter
	def ImixDataQoS(self, value):
		self._set_attribute('imixDataQoS', value)

	@property
	def ImixDelete(self):
		"""Deletes the imix data.

		Returns:
			str
		"""
		return self._get_attribute('imixDelete')
	@ImixDelete.setter
	def ImixDelete(self, value):
		self._set_attribute('imixDelete', value)

	@property
	def ImixDistribution(self):
		"""Specifies the imix distribution unit.

		Returns:
			str(bwpercentage|weight)
		"""
		return self._get_attribute('imixDistribution')
	@ImixDistribution.setter
	def ImixDistribution(self, value):
		self._set_attribute('imixDistribution', value)

	@property
	def ImixEnabled(self):
		"""If True, Enables the imix value.

		Returns:
			bool
		"""
		return self._get_attribute('imixEnabled')
	@ImixEnabled.setter
	def ImixEnabled(self, value):
		self._set_attribute('imixEnabled', value)

	@property
	def ImixTemplates(self):
		"""Specefies the imix templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('imixTemplates')
	@ImixTemplates.setter
	def ImixTemplates(self, value):
		self._set_attribute('imixTemplates', value)

	@property
	def ImixTrafficType(self):
		"""Displays the imix traffic type.

		Returns:
			str
		"""
		return self._get_attribute('imixTrafficType')
	@ImixTrafficType.setter
	def ImixTrafficType(self, value):
		self._set_attribute('imixTrafficType', value)

	@property
	def IncMulticastDestMACAddress(self):
		"""The incrementing multicast destination MAC address.

		Returns:
			str
		"""
		return self._get_attribute('incMulticastDestMACAddress')
	@IncMulticastDestMACAddress.setter
	def IncMulticastDestMACAddress(self, value):
		self._set_attribute('incMulticastDestMACAddress', value)

	@property
	def IncPortMACAddress(self):
		"""The incrementing MAC address of the port.

		Returns:
			str
		"""
		return self._get_attribute('incPortMACAddress')
	@IncPortMACAddress.setter
	def IncPortMACAddress(self, value):
		self._set_attribute('incPortMACAddress', value)

	@property
	def IncrAddresses(self):
		"""The incremental address.

		Returns:
			number
		"""
		return self._get_attribute('incrAddresses')
	@IncrAddresses.setter
	def IncrAddresses(self, value):
		self._set_attribute('incrAddresses', value)

	@property
	def IncrStep(self):
		"""The option to increment step value.

		Returns:
			number
		"""
		return self._get_attribute('incrStep')
	@IncrStep.setter
	def IncrStep(self, value):
		self._set_attribute('incrStep', value)

	@property
	def IncrementLoadRate(self):
		"""The incremental value of load rate.

		Returns:
			str
		"""
		return self._get_attribute('incrementLoadRate')
	@IncrementLoadRate.setter
	def IncrementLoadRate(self, value):
		self._set_attribute('incrementLoadRate', value)

	@property
	def IncrementLoadUnit(self):
		"""The incremental value of the load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

	@property
	def InitialBinaryLoadRate(self):
		"""Specifies the initial rate of the binary algorithm.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def InitialComboLoadRate(self):
		"""The initial combination value of the load rate .

		Returns:
			number
		"""
		return self._get_attribute('initialComboLoadRate')
	@InitialComboLoadRate.setter
	def InitialComboLoadRate(self, value):
		self._set_attribute('initialComboLoadRate', value)

	@property
	def InitialIncrementLoadRate(self):
		"""The initial incremental value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialIncrementLoadRate')
	@InitialIncrementLoadRate.setter
	def InitialIncrementLoadRate(self, value):
		self._set_attribute('initialIncrementLoadRate', value)

	@property
	def InitialStepLoadRate(self):
		"""The initial step value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialStepLoadRate')
	@InitialStepLoadRate.setter
	def InitialStepLoadRate(self, value):
		self._set_attribute('initialStepLoadRate', value)

	@property
	def Ipv4Address(self):
		"""The allocated IPv4 address for this interface.

		Returns:
			str
		"""
		return self._get_attribute('ipv4Address')
	@Ipv4Address.setter
	def Ipv4Address(self, value):
		self._set_attribute('ipv4Address', value)

	@property
	def Ipv6Address(self):
		"""The allocated IPv6address for this interface.

		Returns:
			str
		"""
		return self._get_attribute('ipv6Address')
	@Ipv6Address.setter
	def Ipv6Address(self, value):
		self._set_attribute('ipv6Address', value)

	@property
	def IsIPv6(self):
		"""The allocated IPv6address for this interface.

		Returns:
			str
		"""
		return self._get_attribute('isIPv6')
	@IsIPv6.setter
	def IsIPv6(self, value):
		self._set_attribute('isIPv6', value)

	@property
	def IsMulticastAutomaticFrameData(self):
		"""The multicast automatic frame data.

		Returns:
			str
		"""
		return self._get_attribute('isMulticastAutomaticFrameData')
	@IsMulticastAutomaticFrameData.setter
	def IsMulticastAutomaticFrameData(self, value):
		self._set_attribute('isMulticastAutomaticFrameData', value)

	@property
	def IsNewMode(self):
		"""Is New Mode

		Returns:
			bool
		"""
		return self._get_attribute('isNewMode')
	@IsNewMode.setter
	def IsNewMode(self, value):
		self._set_attribute('isNewMode', value)

	@property
	def JoinLeaveMultiplier(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveMultiplier')
	@JoinLeaveMultiplier.setter
	def JoinLeaveMultiplier(self, value):
		self._set_attribute('joinLeaveMultiplier', value)

	@property
	def JoinLeaveRate(self):
		"""The join leave rate.

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveRate')
	@JoinLeaveRate.setter
	def JoinLeaveRate(self, value):
		self._set_attribute('joinLeaveRate', value)

	@property
	def JoinLeaveWaitTime(self):
		"""The wait time for join delay.

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveWaitTime')
	@JoinLeaveWaitTime.setter
	def JoinLeaveWaitTime(self, value):
		self._set_attribute('joinLeaveWaitTime', value)

	@property
	def LatencyBins(self):
		"""Sets the latency bins statistics

		Returns:
			str
		"""
		return self._get_attribute('latencyBins')
	@LatencyBins.setter
	def LatencyBins(self, value):
		self._set_attribute('latencyBins', value)

	@property
	def LatencyBinsEnabled(self):
		"""Enables the latency bins statistics

		Returns:
			bool
		"""
		return self._get_attribute('latencyBinsEnabled')
	@LatencyBinsEnabled.setter
	def LatencyBinsEnabled(self, value):
		self._set_attribute('latencyBinsEnabled', value)

	@property
	def LatencyType(self):
		"""The type of latency.

		Returns:
			str(cutThrough|forwardingDelay|mef|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LearnRateMac(self):
		"""Rates learning frames to MAC address.

		Returns:
			str
		"""
		return self._get_attribute('learnRateMac')
	@LearnRateMac.setter
	def LearnRateMac(self, value):
		self._set_attribute('learnRateMac', value)

	@property
	def LearnSendMac(self):
		"""Sends learning frames to MAC address.

		Returns:
			str
		"""
		return self._get_attribute('learnSendMac')
	@LearnSendMac.setter
	def LearnSendMac(self, value):
		self._set_attribute('learnSendMac', value)

	@property
	def LearnSendMacEnabled(self):
		"""Send Mac learning

		Returns:
			str
		"""
		return self._get_attribute('learnSendMacEnabled')
	@LearnSendMacEnabled.setter
	def LearnSendMacEnabled(self, value):
		self._set_attribute('learnSendMacEnabled', value)

	@property
	def LoadInitialRate(self):
		"""The initial rate of the load.

		Returns:
			number
		"""
		return self._get_attribute('loadInitialRate')
	@LoadInitialRate.setter
	def LoadInitialRate(self, value):
		self._set_attribute('loadInitialRate', value)

	@property
	def LoadRateList(self):
		"""Enters the Load Rate List.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadType(self):
		"""The type of the payload setting.

		Returns:
			str(binary|combo|custom|increment|quickSearch|random|step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""The mapping type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxBinaryLoadRate(self):
		"""Specifies the maximum rate of the binary algorithm.

		Returns:
			number
		"""
		return self._get_attribute('maxBinaryLoadRate')
	@MaxBinaryLoadRate.setter
	def MaxBinaryLoadRate(self, value):
		self._set_attribute('maxBinaryLoadRate', value)

	@property
	def MaxComboLoadRate(self):
		"""The maximum value of the load rate Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('maxComboLoadRate')
	@MaxComboLoadRate.setter
	def MaxComboLoadRate(self, value):
		self._set_attribute('maxComboLoadRate', value)

	@property
	def MaxIncrementFrameSize(self):
		"""The integer that states the maximum amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxIncrementLoadRate(self):
		"""The maximum incremental value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementLoadRate')
	@MaxIncrementLoadRate.setter
	def MaxIncrementLoadRate(self, value):
		self._set_attribute('maxIncrementLoadRate', value)

	@property
	def MaxQuickSearchLoadRate(self):
		"""Sets the maximum QuickSearch load rate

		Returns:
			number
		"""
		return self._get_attribute('maxQuickSearchLoadRate')
	@MaxQuickSearchLoadRate.setter
	def MaxQuickSearchLoadRate(self, value):
		self._set_attribute('maxQuickSearchLoadRate', value)

	@property
	def MaxRandomFrameSize(self):
		"""The integer that states the maximum random amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MaxRandomLoadRate(self):
		"""The maximum random value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomLoadRate')
	@MaxRandomLoadRate.setter
	def MaxRandomLoadRate(self, value):
		self._set_attribute('maxRandomLoadRate', value)

	@property
	def MaxStepLoadRate(self):
		"""The maximum step value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxStepLoadRate')
	@MaxStepLoadRate.setter
	def MaxStepLoadRate(self, value):
		self._set_attribute('maxStepLoadRate', value)

	@property
	def MinBinaryLoadRate(self):
		"""Specifies the minimum rate of the binary algorithm.

		Returns:
			number
		"""
		return self._get_attribute('minBinaryLoadRate')
	@MinBinaryLoadRate.setter
	def MinBinaryLoadRate(self, value):
		self._set_attribute('minBinaryLoadRate', value)

	@property
	def MinComboLoadRate(self):
		"""The minimum combination load rate.

		Returns:
			number
		"""
		return self._get_attribute('minComboLoadRate')
	@MinComboLoadRate.setter
	def MinComboLoadRate(self, value):
		self._set_attribute('minComboLoadRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""The integer that states the minimum amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinQuickSearchLoadRate(self):
		"""Sets the minum Quick Search load rate

		Returns:
			number
		"""
		return self._get_attribute('minQuickSearchLoadRate')
	@MinQuickSearchLoadRate.setter
	def MinQuickSearchLoadRate(self, value):
		self._set_attribute('minQuickSearchLoadRate', value)

	@property
	def MinRandomFrameSize(self):
		"""The integer that states the minimum random amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def MinRandomLoadRate(self):
		"""The maximum random value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('minRandomLoadRate')
	@MinRandomLoadRate.setter
	def MinRandomLoadRate(self, value):
		self._set_attribute('minRandomLoadRate', value)

	@property
	def MixedClassMulticast(self):
		"""The mixed multicast class.

		Returns:
			str
		"""
		return self._get_attribute('mixedClassMulticast')
	@MixedClassMulticast.setter
	def MixedClassMulticast(self, value):
		self._set_attribute('mixedClassMulticast', value)

	@property
	def MldVersion(self):
		"""The version of the MLD messages.

		Returns:
			number
		"""
		return self._get_attribute('mldVersion')
	@MldVersion.setter
	def MldVersion(self, value):
		self._set_attribute('mldVersion', value)

	@property
	def NumAddresses(self):
		"""The integer value for the number of addresses.

		Returns:
			number
		"""
		return self._get_attribute('numAddresses')
	@NumAddresses.setter
	def NumAddresses(self, value):
		self._set_attribute('numAddresses', value)

	@property
	def NumIterations(self):
		"""The integer value for the number of iterations.

		Returns:
			number
		"""
		return self._get_attribute('numIterations')
	@NumIterations.setter
	def NumIterations(self, value):
		self._set_attribute('numIterations', value)

	@property
	def Numtrials(self):
		"""The integer value that states the number of trials permitted.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PercentMulticastFrames(self):
		"""The percentage of multicast frames.

		Returns:
			number
		"""
		return self._get_attribute('percentMulticastFrames')
	@PercentMulticastFrames.setter
	def PercentMulticastFrames(self, value):
		self._set_attribute('percentMulticastFrames', value)

	@property
	def PercentUnicastFrames(self):
		"""The percentage of unicast frames.

		Returns:
			number
		"""
		return self._get_attribute('percentUnicastFrames')
	@PercentUnicastFrames.setter
	def PercentUnicastFrames(self, value):
		self._set_attribute('percentUnicastFrames', value)

	@property
	def PortDelayEnabled(self):
		"""Enable Delay Between Ports

		Returns:
			bool
		"""
		return self._get_attribute('portDelayEnabled')
	@PortDelayEnabled.setter
	def PortDelayEnabled(self, value):
		self._set_attribute('portDelayEnabled', value)

	@property
	def PortDelayUnit(self):
		"""Sets the port delay unit in which it will be measured

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

	@property
	def PortMACAddress(self):
		"""The MAC address of the port.

		Returns:
			str
		"""
		return self._get_attribute('portMACAddress')
	@PortMACAddress.setter
	def PortMACAddress(self, value):
		self._set_attribute('portMACAddress', value)

	@property
	def ProtocolItem(self):
		"""Protocol Items

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])
		"""
		return self._get_attribute('protocolItem')
	@ProtocolItem.setter
	def ProtocolItem(self, value):
		self._set_attribute('protocolItem', value)

	@property
	def QuickBackoffIteration(self):
		"""Sets the quicksearch backoff iteration

		Returns:
			number
		"""
		return self._get_attribute('quickBackoffIteration')
	@QuickBackoffIteration.setter
	def QuickBackoffIteration(self, value):
		self._set_attribute('quickBackoffIteration', value)

	@property
	def QuickEnableBackoffIteration(self):
		"""Enables the quick search backoff iteration

		Returns:
			bool
		"""
		return self._get_attribute('quickEnableBackoffIteration')
	@QuickEnableBackoffIteration.setter
	def QuickEnableBackoffIteration(self, value):
		self._set_attribute('quickEnableBackoffIteration', value)

	@property
	def QuickEnableSaturationIteration(self):
		"""Enables the Quick Search saturation iteration

		Returns:
			bool
		"""
		return self._get_attribute('quickEnableSaturationIteration')
	@QuickEnableSaturationIteration.setter
	def QuickEnableSaturationIteration(self, value):
		self._set_attribute('quickEnableSaturationIteration', value)

	@property
	def QuickSaturationIteration(self):
		"""Sets the quick search saturation iteration

		Returns:
			number
		"""
		return self._get_attribute('quickSaturationIteration')
	@QuickSaturationIteration.setter
	def QuickSaturationIteration(self, value):
		self._set_attribute('quickSaturationIteration', value)

	@property
	def QuickSearchFrameLossUnit(self):
		"""Sets the quick search frame loss unit

		Returns:
			str(%)
		"""
		return self._get_attribute('quickSearchFrameLossUnit')
	@QuickSearchFrameLossUnit.setter
	def QuickSearchFrameLossUnit(self, value):
		self._set_attribute('quickSearchFrameLossUnit', value)

	@property
	def QuickSearchLoadUnit(self):
		"""Sets the quick search load unit

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('quickSearchLoadUnit')
	@QuickSearchLoadUnit.setter
	def QuickSearchLoadUnit(self, value):
		self._set_attribute('quickSearchLoadUnit', value)

	@property
	def QuickSearchResolution(self):
		"""Sets the quick search resolution

		Returns:
			number
		"""
		return self._get_attribute('quickSearchResolution')
	@QuickSearchResolution.setter
	def QuickSearchResolution(self, value):
		self._set_attribute('quickSearchResolution', value)

	@property
	def QuickSearchSearchType(self):
		"""Sets the quick search type

		Returns:
			str(linear|perFlow|perPort|perTrafficItem)
		"""
		return self._get_attribute('quickSearchSearchType')
	@QuickSearchSearchType.setter
	def QuickSearchSearchType(self, value):
		self._set_attribute('quickSearchSearchType', value)

	@property
	def QuickSearchTolerance(self):
		"""Sets the quick search tolerance

		Returns:
			number
		"""
		return self._get_attribute('quickSearchTolerance')
	@QuickSearchTolerance.setter
	def QuickSearchTolerance(self, value):
		self._set_attribute('quickSearchTolerance', value)

	@property
	def RandomLoadUnit(self):
		"""The random values of the load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('randomLoadUnit')
	@RandomLoadUnit.setter
	def RandomLoadUnit(self, value):
		self._set_attribute('randomLoadUnit', value)

	@property
	def ReportSequenceError(self):
		"""If enabled, it reports sequence error.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""The throughput rate unit.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def RouterAlert(self):
		"""The router alert selected from the Hop-by-hop Options.

		Returns:
			bool
		"""
		return self._get_attribute('routerAlert')
	@RouterAlert.setter
	def RouterAlert(self, value):
		self._set_attribute('routerAlert', value)

	@property
	def SaturationIteration(self):
		"""This enables the test to run an extra iteration for calculating the Saturation latency.

		Returns:
			number
		"""
		return self._get_attribute('saturationIteration')
	@SaturationIteration.setter
	def SaturationIteration(self, value):
		self._set_attribute('saturationIteration', value)

	@property
	def ShowDetailedBinaryResults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('showDetailedBinaryResults')
	@ShowDetailedBinaryResults.setter
	def ShowDetailedBinaryResults(self, value):
		self._set_attribute('showDetailedBinaryResults', value)

	@property
	def StepComboLoadRate(self):
		"""The step value of combination load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepComboLoadRate')
	@StepComboLoadRate.setter
	def StepComboLoadRate(self, value):
		self._set_attribute('stepComboLoadRate', value)

	@property
	def StepFrameLossUnit(self):
		"""The frame loss unit for traffic.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('stepFrameLossUnit')
	@StepFrameLossUnit.setter
	def StepFrameLossUnit(self, value):
		self._set_attribute('stepFrameLossUnit', value)

	@property
	def StepIncrementFrameSize(self):
		"""The step to increment the frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def StepIncrementLoadRate(self):
		"""The step incremental value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementLoadRate')
	@StepIncrementLoadRate.setter
	def StepIncrementLoadRate(self, value):
		self._set_attribute('stepIncrementLoadRate', value)

	@property
	def StepLoadUnit(self):
		"""Specifies the step rate of the load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('stepLoadUnit')
	@StepLoadUnit.setter
	def StepLoadUnit(self, value):
		self._set_attribute('stepLoadUnit', value)

	@property
	def StepStepLoadRate(self):
		"""The incremental step value of load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepStepLoadRate')
	@StepStepLoadRate.setter
	def StepStepLoadRate(self, value):
		self._set_attribute('stepStepLoadRate', value)

	@property
	def StepTolerance(self):
		"""The step value of the tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('stepTolerance')
	@StepTolerance.setter
	def StepTolerance(self, value):
		self._set_attribute('stepTolerance', value)

	@property
	def StopTestOnHighLoss(self):
		"""It stops test on high loss.

		Returns:
			number
		"""
		return self._get_attribute('stopTestOnHighLoss')
	@StopTestOnHighLoss.setter
	def StopTestOnHighLoss(self, value):
		self._set_attribute('stopTestOnHighLoss', value)

	@property
	def SupportedTrafficTypes(self):
		"""The traffic types supported.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def TestTrafficType(self):
		"""It signifies the test traffic type value.

		Returns:
			str
		"""
		return self._get_attribute('testTrafficType')
	@TestTrafficType.setter
	def TestTrafficType(self, value):
		self._set_attribute('testTrafficType', value)

	@property
	def TrafficDistribution(self):
		"""Sets the traffic distribution type

		Returns:
			str(mixed|multicast|unicast)
		"""
		return self._get_attribute('trafficDistribution')
	@TrafficDistribution.setter
	def TrafficDistribution(self, value):
		self._set_attribute('trafficDistribution', value)

	@property
	def TxDelay(self):
		"""the delay recorded in the transmit port.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UnchangedInitial(self):
		"""The first value of an unchanged parameter.

		Returns:
			str(False|True)
		"""
		return self._get_attribute('unchangedInitial')
	@UnchangedInitial.setter
	def UnchangedInitial(self, value):
		self._set_attribute('unchangedInitial', value)

	@property
	def UsePercentOffsets(self):
		"""If true, sets the offset value in percentage.

		Returns:
			str
		"""
		return self._get_attribute('usePercentOffsets')
	@UsePercentOffsets.setter
	def UsePercentOffsets(self, value):
		self._set_attribute('usePercentOffsets', value)

	def update(self, ApplyMode=None, AssignGroupType=None, BackoffIteration=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountRandomFrameSize=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableLayer2=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergence=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FirstMulticastDestMACAddress=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, ImixAdd=None, ImixData=None, ImixDataQoS=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncMulticastDestMACAddress=None, IncPortMACAddress=None, IncrAddresses=None, IncrStep=None, IncrementLoadRate=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, IsNewMode=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LearnRateMac=None, LearnSendMac=None, LearnSendMacEnabled=None, LoadInitialRate=None, LoadRateList=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinIncrementFrameSize=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MinRandomLoadRate=None, MixedClassMulticast=None, MldVersion=None, NumAddresses=None, NumIterations=None, Numtrials=None, PercentMulticastFrames=None, PercentUnicastFrames=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortMACAddress=None, ProtocolItem=None, QuickBackoffIteration=None, QuickEnableBackoffIteration=None, QuickEnableSaturationIteration=None, QuickSaturationIteration=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, RandomLoadUnit=None, ReportSequenceError=None, ReportTputRateUnit=None, RouterAlert=None, SaturationIteration=None, ShowDetailedBinaryResults=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, SupportedTrafficTypes=None, TestTrafficType=None, TrafficDistribution=None, TxDelay=None, UnchangedInitial=None, UsePercentOffsets=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			ApplyMode (str): NOT DEFINED
			AssignGroupType (str(accumulated|distributed)): Assigns the group type.
			BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
			BidirectionalOptionEnabled (bool): If true, enables bidirectional option.
			BinaryBackoff (number): Specifies the percentage of binary backoff.
			BinaryFrameLossUnit (str(%|frames)): The binary frame loss unit.
			BinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The binary load unit.
			BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
			BinarySearchType (str(linear|perFlow|perPort|perTrafficItem)): The binary search type value.
			BinaryTolerance (number): The binary tolerance level.
			BurstSize (number): The number of packets that are sent in a burst.
			CalculateJitter (bool): If true, calculates jitter.
			CalculateLatency (bool): If true, calculates the latency.
			ComboBackoff (number): The backoff combination of the test configuration.
			ComboFrameLossUnit (str(%|frames)): The frame loss unit for traffic in binary.
			ComboLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The combination of load units. Possible values include:
			ComboResolution (number): The combined resolution value.
			ComboTolerance (number): The combined tolerance level.
			CountRandomFrameSize (number): If true, frame sizes are counted at random.
			CountRandomLoadRate (number): The random count of the load rate.
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the custom load unit.
			DelayAfterTransmit (number): The amount of delay after every transmit.
			Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
			EnableBackoffIteration (bool): If true, enables back off iteration test.
			EnableDataIntegrity (bool): enableDataIntegrity
			EnableExtraIterations (str): If true, more iterations are performed.
			EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableLayer2 (bool): If true, enables Layer2 protocols.
			EnableLeaveGroup (bool): If true, the leave group is enabled.
			EnableMinFrameSize (bool): If enabled, it shows the minimum frame size.
			EnableMulticastQuerier (bool): Enable Multicast Querier Settings
			EnableOldStatsForReef (bool): Enable old statistics for reef.
			EnableSaturationIteration (bool): If true, SaturationIteration in enabled .
			EnableStopTestOnHighLoss (bool): The test stops in case of a high loss.
			ExtraIterationOffsets (str): This enables the test to run an extra iteration.
			FastConvergence (str): If true, enables fast convergence.
			FastConvergenceDuration (number): This enables the test to perform iterations using the fast convergence duration configured.
			FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
			FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
			FloodedFramesEnabled (bool): Show Flooded Frames
			ForceRegenerate (bool): Initiates a forced regeneration.
			FrameLossUnit (str): The frame loss unit.
			FrameSizeMode (str(custom|customlist|increment|random)): This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.
			FramesizeImixList (str): The list of frame size to be used
			FramesizeList (list(str)): The list of frame sizes.
			Gap (number): It signifies the gap value for the protocol.
			GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
			GroupCapacityGreaterThan (number): The integer that distinguishes the group capacity that could be greater than the specified integer.
			GroupDistributionType (str(acrossHosts|acrossPorts)): The group distribution type.
			IgmpV1Timeout (number): The IGMPv1 timeout value.
			IgmpVersion (number): The igmp version .
			Igmpv3MessageType (str(exclude|include)): It gives details about the igmpv3 message type in the test configuration
			Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
			ImixAdd (str): Adds an imix data.
			ImixData (str): Displays the imix Data.
			ImixDataQoS (bool): Enables Imix Data QoS
			ImixDelete (str): Deletes the imix data.
			ImixDistribution (str(bwpercentage|weight)): Specifies the imix distribution unit.
			ImixEnabled (bool): If True, Enables the imix value.
			ImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Specefies the imix templates.
			ImixTrafficType (str): Displays the imix traffic type.
			IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
			IncPortMACAddress (str): The incrementing MAC address of the port.
			IncrAddresses (number): The incremental address.
			IncrStep (number): The option to increment step value.
			IncrementLoadRate (str): The incremental value of load rate.
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The incremental value of the load unit.
			InitialBinaryLoadRate (number): Specifies the initial rate of the binary algorithm.
			InitialComboLoadRate (number): The initial combination value of the load rate .
			InitialIncrementLoadRate (number): The initial incremental value of the load rate.
			InitialStepLoadRate (number): The initial step value of the load rate.
			Ipv4Address (str): The allocated IPv4 address for this interface.
			Ipv6Address (str): The allocated IPv6address for this interface.
			IsIPv6 (str): The allocated IPv6address for this interface.
			IsMulticastAutomaticFrameData (str): The multicast automatic frame data.
			IsNewMode (bool): Is New Mode
			JoinLeaveMultiplier (number): NOT DEFINED
			JoinLeaveRate (number): The join leave rate.
			JoinLeaveWaitTime (number): The wait time for join delay.
			LatencyBins (str): Sets the latency bins statistics
			LatencyBinsEnabled (bool): Enables the latency bins statistics
			LatencyType (str(cutThrough|forwardingDelay|mef|storeForward)): The type of latency.
			LearnRateMac (str): Rates learning frames to MAC address.
			LearnSendMac (str): Sends learning frames to MAC address.
			LearnSendMacEnabled (str): Send Mac learning
			LoadInitialRate (number): The initial rate of the load.
			LoadRateList (str): Enters the Load Rate List.
			LoadType (str(binary|combo|custom|increment|quickSearch|random|step)): The type of the payload setting.
			MapType (str): The mapping type.
			MaxBinaryLoadRate (number): Specifies the maximum rate of the binary algorithm.
			MaxComboLoadRate (number): The maximum value of the load rate Combo Load Type.
			MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
			MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
			MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
			MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
			MaxRandomLoadRate (number): The maximum random value of the load rate.
			MaxStepLoadRate (number): The maximum step value of the load rate.
			MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
			MinComboLoadRate (number): The minimum combination load rate.
			MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
			MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
			MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
			MinRandomLoadRate (number): The maximum random value of the load rate.
			MixedClassMulticast (str): The mixed multicast class.
			MldVersion (number): The version of the MLD messages.
			NumAddresses (number): The integer value for the number of addresses.
			NumIterations (number): The integer value for the number of iterations.
			Numtrials (number): The integer value that states the number of trials permitted.
			PercentMulticastFrames (number): The percentage of multicast frames.
			PercentUnicastFrames (number): The percentage of unicast frames.
			PortDelayEnabled (bool): Enable Delay Between Ports
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured
			PortDelayValue (number): Sets the port delay value
			PortMACAddress (str): The MAC address of the port.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			QuickBackoffIteration (number): Sets the quicksearch backoff iteration
			QuickEnableBackoffIteration (bool): Enables the quick search backoff iteration
			QuickEnableSaturationIteration (bool): Enables the Quick Search saturation iteration
			QuickSaturationIteration (number): Sets the quick search saturation iteration
			QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
			QuickSearchLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Sets the quick search load unit
			QuickSearchResolution (number): Sets the quick search resolution
			QuickSearchSearchType (str(linear|perFlow|perPort|perTrafficItem)): Sets the quick search type
			QuickSearchTolerance (number): Sets the quick search tolerance
			RandomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The random values of the load unit.
			ReportSequenceError (bool): If enabled, it reports sequence error.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The throughput rate unit.
			RouterAlert (bool): The router alert selected from the Hop-by-hop Options.
			SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
			ShowDetailedBinaryResults (bool): NOT DEFINED
			StepComboLoadRate (number): The step value of combination load rate.
			StepFrameLossUnit (str(%|frames)): The frame loss unit for traffic.
			StepIncrementFrameSize (number): The step to increment the frame size.
			StepIncrementLoadRate (number): The step incremental value of the load rate.
			StepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the step rate of the load unit.
			StepStepLoadRate (number): The incremental step value of load rate.
			StepTolerance (number): The step value of the tolerance level.
			StopTestOnHighLoss (number): It stops test on high loss.
			SupportedTrafficTypes (str): The traffic types supported.
			TestTrafficType (str): It signifies the test traffic type value.
			TrafficDistribution (str(mixed|multicast|unicast)): Sets the traffic distribution type
			TxDelay (number): the delay recorded in the transmit port.
			UnchangedInitial (str(False|True)): The first value of an unchanged parameter.
			UsePercentOffsets (str): If true, sets the offset value in percentage.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Apply(self):
		"""Executes the apply operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('apply', payload=payload, response_object=None)

	def ApplyAsync(self):
		"""Executes the applyAsync operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsync', payload=payload, response_object=None)

	def ApplyAsyncResult(self):
		"""Executes the applyAsyncResult operation on the server.

			Returns:
				bool: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsyncResult', payload=payload, response_object=None)

	def ApplyITWizardConfiguration(self):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		Generate a PDF report for the last succesfull test run.

			Returns:
				str: This method is asynchronous and has no return value.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('generateReport', payload=payload, response_object=None)

	def Run(self, *args, **kwargs):
		"""Executes the run operation on the server.

		Starts the specified Quick Test and waits for its execution to finish.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		run()list

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		run(InputParameters:string)list
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('run', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Starts the specified Quick Test.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(InputParameters:string)
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)

	def WaitForTest(self):
		"""Executes the waitForTest operation on the server.

		Waits for the execution of the specified Quick Test to be completed.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('waitForTest', payload=payload, response_object=None)
