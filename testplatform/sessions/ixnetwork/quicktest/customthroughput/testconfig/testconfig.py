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
	def Backoff(self):
		"""The percentage value to increase or decrease, when the load is adjusted to decrease frame loss.

		Returns:
			number
		"""
		return self._get_attribute('backoff')
	@Backoff.setter
	def Backoff(self, value):
		self._set_attribute('backoff', value)

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
		"""Signifies the two values of frame loss unit.

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
		"""Specifies the resolution of the iteration.

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
		"""The combined backoff value.

		Returns:
			number
		"""
		return self._get_attribute('comboBackoff')
	@ComboBackoff.setter
	def ComboBackoff(self, value):
		self._set_attribute('comboBackoff', value)

	@property
	def ComboFrameLossUnit(self):
		"""Signifies the loss unit for frames for test configuration.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('comboFrameLossUnit')
	@ComboFrameLossUnit.setter
	def ComboFrameLossUnit(self, value):
		self._set_attribute('comboFrameLossUnit', value)

	@property
	def ComboLoadUnit(self):
		"""Signifies the combo loud unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('comboLoadUnit')
	@ComboLoadUnit.setter
	def ComboLoadUnit(self, value):
		self._set_attribute('comboLoadUnit', value)

	@property
	def ComboResolution(self):
		"""Signifies the combination of resolution values.

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
	def CountFramesize(self):
		"""Counts the number of frame sizes.

		Returns:
			number
		"""
		return self._get_attribute('countFramesize')
	@CountFramesize.setter
	def CountFramesize(self, value):
		self._set_attribute('countFramesize', value)

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
	def CustomFramesize(self):
		"""Signifies the customized frame size.

		Returns:
			str
		"""
		return self._get_attribute('customFramesize')
	@CustomFramesize.setter
	def CustomFramesize(self, value):
		self._set_attribute('customFramesize', value)

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
		"""Specifies the amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DisableInheritedImix(self):
		"""If true, disables inherited imix data.

		Returns:
			str
		"""
		return self._get_attribute('disableInheritedImix')
	@DisableInheritedImix.setter
	def DisableInheritedImix(self, value):
		self._set_attribute('disableInheritedImix', value)

	@property
	def Duration(self):
		"""sec

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableBackoffIteration(self):
		"""If true, enables the test to run an extra iteration for calculating the Backoff Latency.

		Returns:
			bool
		"""
		return self._get_attribute('enableBackoffIteration')
	@EnableBackoffIteration.setter
	def EnableBackoffIteration(self, value):
		self._set_attribute('enableBackoffIteration', value)

	@property
	def EnableDataIntegrity(self):
		"""If true, enables data integrity test.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableExtraIterations(self):
		"""If enabled, it signifies extra iterations.

		Returns:
			bool
		"""
		return self._get_attribute('enableExtraIterations')
	@EnableExtraIterations.setter
	def EnableExtraIterations(self, value):
		self._set_attribute('enableExtraIterations', value)

	@property
	def EnableFastConvergence(self):
		"""If enabled, it signifies the fast convergence.

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
		"""If true, enables the test to run an extra iteration for calculating the Saturation Latency.

		Returns:
			bool
		"""
		return self._get_attribute('enableSaturationIteration')
	@EnableSaturationIteration.setter
	def EnableSaturationIteration(self, value):
		self._set_attribute('enableSaturationIteration', value)

	@property
	def EnableStopTestOnHighLoss(self):
		"""If true, enable this to stop the high frame loss.

		Returns:
			bool
		"""
		return self._get_attribute('enableStopTestOnHighLoss')
	@EnableStopTestOnHighLoss.setter
	def EnableStopTestOnHighLoss(self, value):
		self._set_attribute('enableStopTestOnHighLoss', value)

	@property
	def ExtraIterationOffsets(self):
		"""It signifies the extra iterations offsets value.

		Returns:
			str
		"""
		return self._get_attribute('extraIterationOffsets')
	@ExtraIterationOffsets.setter
	def ExtraIterationOffsets(self, value):
		self._set_attribute('extraIterationOffsets', value)

	@property
	def FastConvergenceDuration(self):
		"""It signifies the fast convergence duration value.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceDuration')
	@FastConvergenceDuration.setter
	def FastConvergenceDuration(self, value):
		self._set_attribute('fastConvergenceDuration', value)

	@property
	def FastConvergenceThreshold(self):
		"""It signifies the fast convergence threshold value.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceThreshold')
	@FastConvergenceThreshold.setter
	def FastConvergenceThreshold(self, value):
		self._set_attribute('fastConvergenceThreshold', value)

	@property
	def FixedLoadUnit(self):
		"""The fixed values for load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('fixedLoadUnit')
	@FixedLoadUnit.setter
	def FixedLoadUnit(self, value):
		self._set_attribute('fixedLoadUnit', value)

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
		"""Signifies the unit for frame loss for test configuration.

		Returns:
			str
		"""
		return self._get_attribute('frameLossUnit')
	@FrameLossUnit.setter
	def FrameLossUnit(self, value):
		self._set_attribute('frameLossUnit', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian.

		Returns:
			str(custom|customlist|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

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
		"""Signifies the frame size for test configuration.

		Returns:
			str
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeFixedValue(self):
		"""It signifies the frame size fixed value.

		Returns:
			number
		"""
		return self._get_attribute('framesizeFixedValue')
	@FramesizeFixedValue.setter
	def FramesizeFixedValue(self, value):
		self._set_attribute('framesizeFixedValue', value)

	@property
	def FramesizeImixList(self):
		"""Signifies the list of frame size imix value.

		Returns:
			str
		"""
		return self._get_attribute('framesizeImixList')
	@FramesizeImixList.setter
	def FramesizeImixList(self, value):
		self._set_attribute('framesizeImixList', value)

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
		"""If enabled, it generates the tracking option for aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def ImixAdd(self):
		"""Signifies the test configuration.

		Returns:
			str
		"""
		return self._get_attribute('imixAdd')
	@ImixAdd.setter
	def ImixAdd(self, value):
		self._set_attribute('imixAdd', value)

	@property
	def ImixData(self):
		"""Signifies the IMIX data for test configuration.

		Returns:
			str
		"""
		return self._get_attribute('imixData')
	@ImixData.setter
	def ImixData(self, value):
		self._set_attribute('imixData', value)

	@property
	def ImixDelete(self):
		"""Signifies the deleted data of IMIX.

		Returns:
			str
		"""
		return self._get_attribute('imixDelete')
	@ImixDelete.setter
	def ImixDelete(self, value):
		self._set_attribute('imixDelete', value)

	@property
	def ImixDistribution(self):
		"""Signifies the distribution list for imix values.

		Returns:
			str(bwpercentage|weight)
		"""
		return self._get_attribute('imixDistribution')
	@ImixDistribution.setter
	def ImixDistribution(self, value):
		self._set_attribute('imixDistribution', value)

	@property
	def ImixEnabled(self):
		"""If true, enables the imix value.

		Returns:
			bool
		"""
		return self._get_attribute('imixEnabled')
	@ImixEnabled.setter
	def ImixEnabled(self, value):
		self._set_attribute('imixEnabled', value)

	@property
	def ImixTemplates(self):
		"""Signifies the imix templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('imixTemplates')
	@ImixTemplates.setter
	def ImixTemplates(self, value):
		self._set_attribute('imixTemplates', value)

	@property
	def ImixTrafficType(self):
		"""Signifies the traffic type of test configuration.

		Returns:
			str
		"""
		return self._get_attribute('imixTrafficType')
	@ImixTrafficType.setter
	def ImixTrafficType(self, value):
		self._set_attribute('imixTrafficType', value)

	@property
	def IncrementLoadUnit(self):
		"""If true, increments the load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

	@property
	def InitialBinaryLoadRate(self):
		"""Signifies the initial binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def InitialComboLoadRate(self):
		"""The first combination load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialComboLoadRate')
	@InitialComboLoadRate.setter
	def InitialComboLoadRate(self, value):
		self._set_attribute('initialComboLoadRate', value)

	@property
	def InitialFramesize(self):
		"""Signifies the initial frame size.

		Returns:
			number
		"""
		return self._get_attribute('initialFramesize')
	@InitialFramesize.setter
	def InitialFramesize(self, value):
		self._set_attribute('initialFramesize', value)

	@property
	def InitialIncrementLoadRate(self):
		"""Signifies the initial incremented load rate.

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
	def LastFramesize(self):
		"""Signifies the last frame size.

		Returns:
			number
		"""
		return self._get_attribute('lastFramesize')
	@LastFramesize.setter
	def LastFramesize(self, value):
		self._set_attribute('lastFramesize', value)

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
		"""Enters the Load Rate List.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadRateValue(self):
		"""Signifies the load rate value.

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
			str(binary|combo|step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def LoadUnit(self):
		"""Signifies the load unit value.

		Returns:
			str
		"""
		return self._get_attribute('loadUnit')
	@LoadUnit.setter
	def LoadUnit(self, value):
		self._set_attribute('loadUnit', value)

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
		"""The maximum combination load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxComboLoadRate')
	@MaxComboLoadRate.setter
	def MaxComboLoadRate(self, value):
		self._set_attribute('maxComboLoadRate', value)

	@property
	def MaxFramesize(self):
		"""Signifies the maximum frame size.

		Returns:
			number
		"""
		return self._get_attribute('maxFramesize')
	@MaxFramesize.setter
	def MaxFramesize(self, value):
		self._set_attribute('maxFramesize', value)

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
		"""Signifies the maximum increment of load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementLoadRate')
	@MaxIncrementLoadRate.setter
	def MaxIncrementLoadRate(self, value):
		self._set_attribute('maxIncrementLoadRate', value)

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
	def MinFramesize(self):
		"""Signifies the minimum frame size.

		Returns:
			number
		"""
		return self._get_attribute('minFramesize')
	@MinFramesize.setter
	def MinFramesize(self, value):
		self._set_attribute('minFramesize', value)

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
		"""Signifies the number of trials.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PercentMaxRate(self):
		"""The maximum rate in percentage.

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
	def RateSelect(self):
		"""The selected rate.

		Returns:
			str(fpsRate|kbpsRate|percentMaxRate)
		"""
		return self._get_attribute('rateSelect')
	@RateSelect.setter
	def RateSelect(self, value):
		self._set_attribute('rateSelect', value)

	@property
	def ReportSequenceError(self):
		"""If true, the sequence error, if found, is reported.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""If true, reports the throughput rate unit.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Resolution(self):
		"""Specify the resolution of the iteration.

		Returns:
			number
		"""
		return self._get_attribute('resolution')
	@Resolution.setter
	def Resolution(self, value):
		self._set_attribute('resolution', value)

	@property
	def SaturationIteration(self):
		"""This enables the test to run an extra iteration for calculating the Saturation Latency.

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
		"""Signifies the combination of step load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepComboLoadRate')
	@StepComboLoadRate.setter
	def StepComboLoadRate(self, value):
		self._set_attribute('stepComboLoadRate', value)

	@property
	def StepFrameLossUnit(self):
		"""The step frame loss unit for upstream traffic.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('stepFrameLossUnit')
	@StepFrameLossUnit.setter
	def StepFrameLossUnit(self, value):
		self._set_attribute('stepFrameLossUnit', value)

	@property
	def StepFramesize(self):
		"""The step value for frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepFramesize')
	@StepFramesize.setter
	def StepFramesize(self, value):
		self._set_attribute('stepFramesize', value)

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
		"""Signifies the step value for incremented load rate.

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
	def UnchangedInitial(self):
		"""Signifies the initial value that is unchanged.

		Returns:
			str(False|True)
		"""
		return self._get_attribute('unchangedInitial')
	@UnchangedInitial.setter
	def UnchangedInitial(self, value):
		self._set_attribute('unchangedInitial', value)

	@property
	def UnchangedValueList(self):
		"""It signifies the unchanged value list.

		Returns:
			str
		"""
		return self._get_attribute('unchangedValueList')
	@UnchangedValueList.setter
	def UnchangedValueList(self, value):
		self._set_attribute('unchangedValueList', value)

	@property
	def UsePercentOffsets(self):
		"""It signifies the value of percent offsets when used.

		Returns:
			str
		"""
		return self._get_attribute('usePercentOffsets')
	@UsePercentOffsets.setter
	def UsePercentOffsets(self, value):
		self._set_attribute('usePercentOffsets', value)

	def update(self, Backoff=None, BackoffIteration=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountFramesize=None, CountRandomFrameSize=None, CountRandomLoadRate=None, CustomFramesize=None, CustomLoadUnit=None, DelayAfterTransmit=None, DisableInheritedImix=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FixedLoadUnit=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeFixedValue=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialFramesize=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, Ipv4rate=None, Ipv6rate=None, LastFramesize=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadRateValue=None, LoadType=None, LoadUnit=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxFramesize=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinFramesize=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomLoadRate=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, SaturationIteration=None, StaggeredStart=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepFramesize=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedInitial=None, UnchangedValueList=None, UsePercentOffsets=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			Backoff (number): The percentage value to increase or decrease, when the load is adjusted to decrease frame loss.
			BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
			BinaryBackoff (number): Specifies the percentage of binary backoff.
			BinaryFrameLossUnit (str(%|frames)): Signifies the two values of frame loss unit.
			BinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies the binary load unit.
			BinaryResolution (number): Specifies the resolution of the iteration.
			BinarySearchType (str(linear|perFlow|perPort|perTrafficItem)): The binary search type value.
			BinaryTolerance (number): The binary tolerance level.
			BurstSize (number): The number of packets to send in a burst.
			CalculateJitter (bool): If true, calculates jitter.
			CalculateLatency (bool): If true, calculates the latency.
			ComboBackoff (number): The combined backoff value.
			ComboFrameLossUnit (str(%|frames)): Signifies the loss unit for frames for test configuration.
			ComboLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies the combo loud unit.
			ComboResolution (number): Signifies the combination of resolution values.
			ComboTolerance (number): The combined tolerance level.
			CountFramesize (number): Counts the number of frame sizes.
			CountRandomFrameSize (number): If true, randomly counts the frame size.
			CountRandomLoadRate (number): The random count of the load rate.
			CustomFramesize (str): Signifies the customized frame size.
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the custom load unit.
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
			DisableInheritedImix (str): If true, disables inherited imix data.
			Duration (number): sec
			EnableBackoffIteration (bool): If true, enables the test to run an extra iteration for calculating the Backoff Latency.
			EnableDataIntegrity (bool): If true, enables data integrity test.
			EnableExtraIterations (bool): If enabled, it signifies extra iterations.
			EnableFastConvergence (bool): If enabled, it signifies the fast convergence.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the Saturation Latency.
			EnableStopTestOnHighLoss (bool): If true, enable this to stop the high frame loss.
			ExtraIterationOffsets (str): It signifies the extra iterations offsets value.
			FastConvergenceDuration (number): It signifies the fast convergence duration value.
			FastConvergenceThreshold (number): It signifies the fast convergence threshold value.
			FixedLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The fixed values for load unit.
			ForceRegenerate (bool): Initiates a forced regeneration.
			FrameLossUnit (str): Signifies the unit for frame loss for test configuration.
			FrameSizeMode (str(custom|customlist|increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			FramesPerBurstGap (number): The number of frames to be sent after each burst.
			Framesize (str): Signifies the frame size for test configuration.
			FramesizeFixedValue (number): It signifies the frame size fixed value.
			FramesizeImixList (str): Signifies the list of frame size imix value.
			FramesizeList (list(str)): The list of the available frame sizes.
			Gap (number): It signifies the gap value for the protocol.
			GenerateTrackingOptionAggregationFiles (bool): If enabled, it generates the tracking option for aggregation files.
			ImixAdd (str): Signifies the test configuration.
			ImixData (str): Signifies the IMIX data for test configuration.
			ImixDelete (str): Signifies the deleted data of IMIX.
			ImixDistribution (str(bwpercentage|weight)): Signifies the distribution list for imix values.
			ImixEnabled (bool): If true, enables the imix value.
			ImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Signifies the imix templates.
			ImixTrafficType (str): Signifies the traffic type of test configuration.
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): If true, increments the load unit.
			InitialBinaryLoadRate (number): Signifies the initial binary load rate.
			InitialComboLoadRate (number): The first combination load rate.
			InitialFramesize (number): Signifies the initial frame size.
			InitialIncrementLoadRate (number): Signifies the initial incremented load rate.
			InitialStepLoadRate (number): The initial step value of the load rate.
			Ipv4rate (number): The rate at which IPv4 traffic is sent.
			Ipv6rate (number): The rate at which IPv6 traffic is sent.
			LastFramesize (number): Signifies the last frame size.
			LatencyBins (str): Sets the latency bins statistics.
			LatencyBinsEnabled (bool): Enables the latency bins statistics.
			LatencyType (str(cutThrough|storeForward)): The type of latency.
			LoadRateList (str): Enters the Load Rate List.
			LoadRateValue (number): Signifies the load rate value.
			LoadType (str(binary|combo|step)): The type of the payload setting.
			LoadUnit (str): Signifies the load unit value.
			MaxBinaryLoadRate (number): Specifies the maximum rate of the binary algorithm.
			MaxComboLoadRate (number): The maximum combination load rate.
			MaxFramesize (number): Signifies the maximum frame size.
			MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
			MaxIncrementLoadRate (number): Signifies the maximum increment of load rate.
			MaxRandomFrameSize (number): The maximum random frame size to be sent.
			MaxRandomLoadRate (number): The maximum random value of the load rate.
			MaxStepLoadRate (number): The maximum step value of the load rate.
			MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
			MinComboLoadRate (number): The minimum combination load rate.
			MinFpsRate (number): The rate at which minimum frames are sent per second.
			MinFramesize (number): Signifies the minimum frame size.
			MinIncrementFrameSize (number): The minimum incremental value of the frame size.
			MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			MinRandomLoadRate (number): The minimum random value of the load rate.
			Numtrials (number): Signifies the number of trials.
			PercentMaxRate (number): The maximum rate in percentage.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			RandomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The random values of the load unit.
			RateSelect (str(fpsRate|kbpsRate|percentMaxRate)): The selected rate.
			ReportSequenceError (bool): If true, the sequence error, if found, is reported.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): If true, reports the throughput rate unit.
			Resolution (number): Specify the resolution of the iteration.
			SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation Latency.
			StaggeredStart (bool): If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
			StepComboLoadRate (number): Signifies the combination of step load rate.
			StepFrameLossUnit (str(%|frames)): The step frame loss unit for upstream traffic.
			StepFramesize (number): The step value for frame size.
			StepIncrementFrameSize (number): The incremental step value of the frame size.
			StepIncrementLoadRate (number): Signifies the step value for incremented load rate.
			StepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the step rate of the load unit.
			StepStepLoadRate (number): The incremental step value of load rate.
			StepTolerance (number): The step value of the tolerance level.
			StopTestOnHighLoss (number): If true, enables this to stop the test in case of high frame loss.
			Tolerance (number): The value set for the tolerance level.
			TrafficType (str(burstyLoading|constantLoading)): The test based on the traffic type.
			TxDelay (number): Signifies the transmission delay time.
			UnchangedInitial (str(False|True)): Signifies the initial value that is unchanged.
			UnchangedValueList (str): It signifies the unchanged value list.
			UsePercentOffsets (str): It signifies the value of percent offsets when used.

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
