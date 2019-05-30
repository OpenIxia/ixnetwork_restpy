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
		"""The frame loss unit of measurement for the binary algorithm in binary.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('binaryFrameLossUnit')
	@BinaryFrameLossUnit.setter
	def BinaryFrameLossUnit(self, value):
		self._set_attribute('binaryFrameLossUnit', value)

	@property
	def BinaryLoadUnit(self):
		"""Signifies the binary load unit.

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
		"""The number of packets to send in a burst.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CalculateJitter(self):
		"""If true, the jitter is calculated.

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
		"""If true, randomly counts the frame size.

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
	def DelayAfterTransmit(self):
		"""Specifies the amount of delay after every transmit.

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
		"""If true, enables the checking of data integrity for the pass or fail of the trial.

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
			bool
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
	def EnableMinFrameSize(self):
		"""If true, enables minimum frame size.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableSaturationIteration(self):
		"""If true, enables the test to run an extra iteration for calculating the SaturationLatency.

		Returns:
			bool
		"""
		return self._get_attribute('enableSaturationIteration')
	@EnableSaturationIteration.setter
	def EnableSaturationIteration(self, value):
		self._set_attribute('enableSaturationIteration', value)

	@property
	def EnableStopTestOnHighLoss(self):
		"""If true, enables the test to stop in case of a high loss.

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
	def FrameLossUnit(self):
		"""Frame loss measurement unit.

		Returns:
			str
		"""
		return self._get_attribute('frameLossUnit')
	@FrameLossUnit.setter
	def FrameLossUnit(self, value):
		self._set_attribute('frameLossUnit', value)

	@property
	def FramesPerBurstGap(self):
		"""The number of frames to be sent after each burst.

		Returns:
			number
		"""
		return self._get_attribute('framesPerBurstGap')
	@FramesPerBurstGap.setter
	def FramesPerBurstGap(self, value):
		self._set_attribute('framesPerBurstGap', value)

	@property
	def Framesize(self):
		"""The frame size to be used.

		Returns:
			str
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeFixedValue(self):
		"""The fixed value of framesize.

		Returns:
			number
		"""
		return self._get_attribute('framesizeFixedValue')
	@FramesizeFixedValue.setter
	def FramesizeFixedValue(self, value):
		self._set_attribute('framesizeFixedValue', value)

	@property
	def FramesizeList(self):
		"""The list of the available frame sizes.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def Gap(self):
		"""The gap in transmission of frames.

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""If enabled, it generates the tracking option for aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def GroupDistributionType(self):
		"""Indicates the group distribution type.

		Returns:
			str(acrossHosts|acrossPorts)
		"""
		return self._get_attribute('groupDistributionType')
	@GroupDistributionType.setter
	def GroupDistributionType(self, value):
		self._set_attribute('groupDistributionType', value)

	@property
	def Igmpv3MessageType(self):
		"""It gives details about the IGMPv3 message type in the test configuration.

		Returns:
			str(exclude|include)
		"""
		return self._get_attribute('igmpv3MessageType')
	@Igmpv3MessageType.setter
	def Igmpv3MessageType(self, value):
		self._set_attribute('igmpv3MessageType', value)

	@property
	def Igmpv3SourceAddrList(self):
		"""It gives details about the IGMPv3 source address list in the test configuration.

		Returns:
			str
		"""
		return self._get_attribute('igmpv3SourceAddrList')
	@Igmpv3SourceAddrList.setter
	def Igmpv3SourceAddrList(self, value):
		self._set_attribute('igmpv3SourceAddrList', value)

	@property
	def InitialBinaryLoadRate(self):
		"""The initial binary value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def InitialComboLoadRate(self):
		"""The initial combination value of the load rate.

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
	def Ipv4rate(self):
		"""The rate at which IPv4 traffic is sent.

		Returns:
			number
		"""
		return self._get_attribute('ipv4rate')
	@Ipv4rate.setter
	def Ipv4rate(self, value):
		self._set_attribute('ipv4rate', value)

	@property
	def Ipv6rate(self):
		"""The rate at which IPv6 traffic is sent.

		Returns:
			number
		"""
		return self._get_attribute('ipv6rate')
	@Ipv6rate.setter
	def Ipv6rate(self, value):
		self._set_attribute('ipv6rate', value)

	@property
	def IsMulticastAutomaticFrameData(self):
		"""It signifies the automatic frame data for multicast.

		Returns:
			str
		"""
		return self._get_attribute('isMulticastAutomaticFrameData')
	@IsMulticastAutomaticFrameData.setter
	def IsMulticastAutomaticFrameData(self, value):
		self._set_attribute('isMulticastAutomaticFrameData', value)

	@property
	def IsMulticastTrafficIncluded(self):
		"""Indicates if the test has multicast traffic included or not.

		Returns:
			bool
		"""
		return self._get_attribute('isMulticastTrafficIncluded')
	@IsMulticastTrafficIncluded.setter
	def IsMulticastTrafficIncluded(self, value):
		self._set_attribute('isMulticastTrafficIncluded', value)

	@property
	def IsUnicastTrafficIncluded(self):
		"""Indicates if the test has unicast traffic included or not.

		Returns:
			bool
		"""
		return self._get_attribute('isUnicastTrafficIncluded')
	@IsUnicastTrafficIncluded.setter
	def IsUnicastTrafficIncluded(self, value):
		self._set_attribute('isUnicastTrafficIncluded', value)

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
	def JoinLeaveWaitTime(self):
		"""The wait time for the leave.

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveWaitTime')
	@JoinLeaveWaitTime.setter
	def JoinLeaveWaitTime(self, value):
		self._set_attribute('joinLeaveWaitTime', value)

	@property
	def LatencyBins(self):
		"""Sets the latency bins statistics.

		Returns:
			str
		"""
		return self._get_attribute('latencyBins')
	@LatencyBins.setter
	def LatencyBins(self, value):
		self._set_attribute('latencyBins', value)

	@property
	def LatencyBinsEnabled(self):
		"""Enables the latency bins statistics.

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
			str(cutThrough|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadRateList(self):
		"""It signifies the list of load rate.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadRateValue(self):
		"""The value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('loadRateValue')
	@LoadRateValue.setter
	def LoadRateValue(self, value):
		self._set_attribute('loadRateValue', value)

	@property
	def LoadType(self):
		"""The type of the payload setting.

		Returns:
			str(binary|quickSearch|step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MaxBinaryLoadRate(self):
		"""The upper bound of the iteration rates for each frame size during a binary search.

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
		"""The maximum incremental value of the frame size.

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
		"""Sets the maximum QuickSearch load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxQuickSearchLoadRate')
	@MaxQuickSearchLoadRate.setter
	def MaxQuickSearchLoadRate(self, value):
		self._set_attribute('maxQuickSearchLoadRate', value)

	@property
	def MaxRandomFrameSize(self):
		"""The maximum random frame size to be sent.

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
	def MinFpsRate(self):
		"""The rate at which minimum frames are sent per second.

		Returns:
			number
		"""
		return self._get_attribute('minFpsRate')
	@MinFpsRate.setter
	def MinFpsRate(self, value):
		self._set_attribute('minFpsRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""The minimum incremental value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinKbpsRate(self):
		"""The rate at which minimum frames are sent per kbps.

		Returns:
			number
		"""
		return self._get_attribute('minKbpsRate')
	@MinKbpsRate.setter
	def MinKbpsRate(self, value):
		self._set_attribute('minKbpsRate', value)

	@property
	def MinQuickSearchLoadRate(self):
		"""Signifies the minimum Quick Search load rate.

		Returns:
			number
		"""
		return self._get_attribute('minQuickSearchLoadRate')
	@MinQuickSearchLoadRate.setter
	def MinQuickSearchLoadRate(self, value):
		self._set_attribute('minQuickSearchLoadRate', value)

	@property
	def MinRandomFrameSize(self):
		"""The minimum random frame size to be sent.

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def MinRandomLoadRate(self):
		"""The minimum random value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('minRandomLoadRate')
	@MinRandomLoadRate.setter
	def MinRandomLoadRate(self, value):
		self._set_attribute('minRandomLoadRate', value)

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
	def PercentMaxRate(self):
		"""The rate in maximum percentage.

		Returns:
			number
		"""
		return self._get_attribute('percentMaxRate')
	@PercentMaxRate.setter
	def PercentMaxRate(self, value):
		self._set_attribute('percentMaxRate', value)

	@property
	def PortDelayEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('portDelayEnabled')
	@PortDelayEnabled.setter
	def PortDelayEnabled(self, value):
		self._set_attribute('portDelayEnabled', value)

	@property
	def PortDelayUnit(self):
		"""Sets the port delay unit in which it will be measured.

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value.

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

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
	def QuickSearchFrameLossUnit(self):
		"""Signifies the quick search frame loss unit.

		Returns:
			str(%)
		"""
		return self._get_attribute('quickSearchFrameLossUnit')
	@QuickSearchFrameLossUnit.setter
	def QuickSearchFrameLossUnit(self, value):
		self._set_attribute('quickSearchFrameLossUnit', value)

	@property
	def QuickSearchLoadUnit(self):
		"""Signifies the quick search load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('quickSearchLoadUnit')
	@QuickSearchLoadUnit.setter
	def QuickSearchLoadUnit(self, value):
		self._set_attribute('quickSearchLoadUnit', value)

	@property
	def QuickSearchResolution(self):
		"""Sets the quick search resolution.

		Returns:
			number
		"""
		return self._get_attribute('quickSearchResolution')
	@QuickSearchResolution.setter
	def QuickSearchResolution(self, value):
		self._set_attribute('quickSearchResolution', value)

	@property
	def QuickSearchSearchType(self):
		"""Signifies the quick search type.

		Returns:
			str(linear|perFlow|perPort|perTrafficItem)
		"""
		return self._get_attribute('quickSearchSearchType')
	@QuickSearchSearchType.setter
	def QuickSearchSearchType(self, value):
		self._set_attribute('quickSearchSearchType', value)

	@property
	def QuickSearchTolerance(self):
		"""Sets the quick search tolerance.

		Returns:
			number
		"""
		return self._get_attribute('quickSearchTolerance')
	@QuickSearchTolerance.setter
	def QuickSearchTolerance(self, value):
		self._set_attribute('quickSearchTolerance', value)

	@property
	def RateSelect(self):
		"""The rate selected.

		Returns:
			str(fpsRate|kbpsRate|percentMaxRate)
		"""
		return self._get_attribute('rateSelect')
	@RateSelect.setter
	def RateSelect(self, value):
		self._set_attribute('rateSelect', value)

	@property
	def ReportSequenceError(self):
		"""Reports sequence errors in the test result.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""The unit of rate for throughput.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Resolution(self):
		"""Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.

		Returns:
			number
		"""
		return self._get_attribute('resolution')
	@Resolution.setter
	def Resolution(self, value):
		self._set_attribute('resolution', value)

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
	def StaggeredStart(self):
		"""If true, transmit start is staggered; if false, transmit starts on all ports at the same time.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

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
		"""The step frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('stepFrameLossUnit')
	@StepFrameLossUnit.setter
	def StepFrameLossUnit(self, value):
		self._set_attribute('stepFrameLossUnit', value)

	@property
	def StepIncrementFrameSize(self):
		"""The incremental step value of the frame size.

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
		"""If true, enables this to stop the test in case of high frame loss.

		Returns:
			number
		"""
		return self._get_attribute('stopTestOnHighLoss')
	@StopTestOnHighLoss.setter
	def StopTestOnHighLoss(self, value):
		self._set_attribute('stopTestOnHighLoss', value)

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
	def Tolerance(self):
		"""The value set for the tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""The test based on the traffic type.

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""Signifies the transmission delay time.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UnchangedValueList(self):
		"""The number of unchanged sessions.

		Returns:
			str
		"""
		return self._get_attribute('unchangedValueList')
	@UnchangedValueList.setter
	def UnchangedValueList(self, value):
		self._set_attribute('unchangedValueList', value)

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

	def update(self, BackoffIteration=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboResolution=None, ComboTolerance=None, CountRandomFrameSize=None, CountRandomLoadRate=None, DelayAfterTransmit=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FrameLossUnit=None, FramesPerBurstGap=None, Framesize=None, FramesizeFixedValue=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, GroupDistributionType=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, Ipv4rate=None, Ipv6rate=None, IsMulticastAutomaticFrameData=None, IsMulticastTrafficIncluded=None, IsUnicastTrafficIncluded=None, JoinLeaveMultiplier=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadRateValue=None, LoadType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MinRandomLoadRate=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, SaturationIteration=None, StaggeredStart=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, TestTrafficType=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedValueList=None, UsePercentOffsets=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
			BinaryBackoff (number): Specifies the percentage of binary backoff.
			BinaryFrameLossUnit (str(%|frames)): The frame loss unit of measurement for the binary algorithm in binary.
			BinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies the binary load unit.
			BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
			BinarySearchType (str(linear|perFlow|perPort|perTrafficItem)): The binary search type value.
			BinaryTolerance (number): The binary tolerance level.
			BurstSize (number): The number of packets to send in a burst.
			CalculateJitter (bool): If true, the jitter is calculated.
			CalculateLatency (bool): If true, calculates the latency.
			ComboBackoff (number): The backoff combination of the test configuration.
			ComboResolution (number): The combined resolution value.
			ComboTolerance (number): The combined tolerance level.
			CountRandomFrameSize (number): If true, randomly counts the frame size.
			CountRandomLoadRate (number): The random count of the load rate.
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
			Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
			EnableBackoffIteration (bool): If true, enables back off iteration test.
			EnableDataIntegrity (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
			EnableExtraIterations (bool): If true, more iterations are performed.
			EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
			EnableStopTestOnHighLoss (bool): If true, enables the test to stop in case of a high loss.
			ExtraIterationOffsets (str): This enables the test to run an extra iteration.
			FastConvergenceDuration (number): This enables the test to perform iterations using the fast convergence duration configured.
			FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
			FrameLossUnit (str): Frame loss measurement unit.
			FramesPerBurstGap (number): The number of frames to be sent after each burst.
			Framesize (str): The frame size to be used.
			FramesizeFixedValue (number): The fixed value of framesize.
			FramesizeList (list(str)): The list of the available frame sizes.
			Gap (number): The gap in transmission of frames.
			GenerateTrackingOptionAggregationFiles (bool): If enabled, it generates the tracking option for aggregation files.
			GroupDistributionType (str(acrossHosts|acrossPorts)): Indicates the group distribution type.
			Igmpv3MessageType (str(exclude|include)): It gives details about the IGMPv3 message type in the test configuration.
			Igmpv3SourceAddrList (str): It gives details about the IGMPv3 source address list in the test configuration.
			InitialBinaryLoadRate (number): The initial binary value of the load rate.
			InitialComboLoadRate (number): The initial combination value of the load rate.
			InitialIncrementLoadRate (number): The initial incremental value of the load rate.
			InitialStepLoadRate (number): The initial step value of the load rate.
			Ipv4rate (number): The rate at which IPv4 traffic is sent.
			Ipv6rate (number): The rate at which IPv6 traffic is sent.
			IsMulticastAutomaticFrameData (str): It signifies the automatic frame data for multicast.
			IsMulticastTrafficIncluded (bool): Indicates if the test has multicast traffic included or not.
			IsUnicastTrafficIncluded (bool): Indicates if the test has unicast traffic included or not.
			JoinLeaveMultiplier (number): NOT DEFINED
			JoinLeaveWaitTime (number): The wait time for the leave.
			LatencyBins (str): Sets the latency bins statistics.
			LatencyBinsEnabled (bool): Enables the latency bins statistics.
			LatencyType (str(cutThrough|storeForward)): The type of latency.
			LoadRateList (str): It signifies the list of load rate.
			LoadRateValue (number): The value of the load rate.
			LoadType (str(binary|quickSearch|step)): The type of the payload setting.
			MaxBinaryLoadRate (number): The upper bound of the iteration rates for each frame size during a binary search.
			MaxComboLoadRate (number): The maximum value of the load rate Combo Load Type.
			MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
			MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
			MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate.
			MaxRandomFrameSize (number): The maximum random frame size to be sent.
			MaxRandomLoadRate (number): The maximum random value of the load rate.
			MaxStepLoadRate (number): The maximum step value of the load rate.
			MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
			MinComboLoadRate (number): The minimum combination load rate.
			MinFpsRate (number): The rate at which minimum frames are sent per second.
			MinIncrementFrameSize (number): The minimum incremental value of the frame size.
			MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
			MinQuickSearchLoadRate (number): Signifies the minimum Quick Search load rate.
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			MinRandomLoadRate (number): The minimum random value of the load rate.
			Numtrials (number): The integer value that states the number of trials permitted.
			PercentMaxRate (number): The rate in maximum percentage.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			QuickSearchFrameLossUnit (str(%)): Signifies the quick search frame loss unit.
			QuickSearchLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies the quick search load unit.
			QuickSearchResolution (number): Sets the quick search resolution.
			QuickSearchSearchType (str(linear|perFlow|perPort|perTrafficItem)): Signifies the quick search type.
			QuickSearchTolerance (number): Sets the quick search tolerance.
			RateSelect (str(fpsRate|kbpsRate|percentMaxRate)): The rate selected.
			ReportSequenceError (bool): Reports sequence errors in the test result.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The unit of rate for throughput.
			Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
			SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
			StaggeredStart (bool): If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
			StepComboLoadRate (number): The step value of combination load rate.
			StepFrameLossUnit (str(%|frames)): The step frame loss unit.
			StepIncrementFrameSize (number): The incremental step value of the frame size.
			StepIncrementLoadRate (number): The step incremental value of the load rate.
			StepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the step rate of the load unit.
			StepStepLoadRate (number): The incremental step value of load rate.
			StepTolerance (number): The step value of the tolerance level.
			StopTestOnHighLoss (number): If true, enables this to stop the test in case of high frame loss.
			TestTrafficType (str): It signifies the test traffic type value.
			Tolerance (number): The value set for the tolerance level.
			TrafficType (str(burstyLoading|constantLoading)): The test based on the traffic type.
			TxDelay (number): Signifies the transmission delay time.
			UnchangedValueList (str): The number of unchanged sessions.
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
