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
	def BinaryBackoff(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binaryBackoff')
	@BinaryBackoff.setter
	def BinaryBackoff(self, value):
		self._set_attribute('binaryBackoff', value)

	@property
	def BinaryFrameLossUnit(self):
		"""NOT DEFINED

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('binaryFrameLossUnit')
	@BinaryFrameLossUnit.setter
	def BinaryFrameLossUnit(self, value):
		self._set_attribute('binaryFrameLossUnit', value)

	@property
	def BinaryResolution(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def BinaryTolerance(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binaryTolerance')
	@BinaryTolerance.setter
	def BinaryTolerance(self, value):
		self._set_attribute('binaryTolerance', value)

	@property
	def Binary_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_delay_enableAccLoss')
	@Binary_delay_enableAccLoss.setter
	def Binary_delay_enableAccLoss(self, value):
		self._set_attribute('binary_delay_enableAccLoss', value)

	@property
	def Binary_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('binary_delay_modeAccLoss')
	@Binary_delay_modeAccLoss.setter
	def Binary_delay_modeAccLoss(self, value):
		self._set_attribute('binary_delay_modeAccLoss', value)

	@property
	def Binary_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('binary_delay_scaleAccLoss')
	@Binary_delay_scaleAccLoss.setter
	def Binary_delay_scaleAccLoss(self, value):
		self._set_attribute('binary_delay_scaleAccLoss', value)

	@property
	def Binary_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_delay_thresholdAccLoss')
	@Binary_delay_thresholdAccLoss.setter
	def Binary_delay_thresholdAccLoss(self, value):
		self._set_attribute('binary_delay_thresholdAccLoss', value)

	@property
	def Binary_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_flooded_enableAccLoss')
	@Binary_flooded_enableAccLoss.setter
	def Binary_flooded_enableAccLoss(self, value):
		self._set_attribute('binary_flooded_enableAccLoss', value)

	@property
	def Binary_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_flooded_thresholdAccLoss')
	@Binary_flooded_thresholdAccLoss.setter
	def Binary_flooded_thresholdAccLoss(self, value):
		self._set_attribute('binary_flooded_thresholdAccLoss', value)

	@property
	def Binary_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_integrity_enableAccLoss')
	@Binary_integrity_enableAccLoss.setter
	def Binary_integrity_enableAccLoss(self, value):
		self._set_attribute('binary_integrity_enableAccLoss', value)

	@property
	def Binary_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_integrity_thresholdAccLoss')
	@Binary_integrity_thresholdAccLoss.setter
	def Binary_integrity_thresholdAccLoss(self, value):
		self._set_attribute('binary_integrity_thresholdAccLoss', value)

	@property
	def Binary_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_latency_enableAccLoss')
	@Binary_latency_enableAccLoss.setter
	def Binary_latency_enableAccLoss(self, value):
		self._set_attribute('binary_latency_enableAccLoss', value)

	@property
	def Binary_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('binary_latency_modeAccLoss')
	@Binary_latency_modeAccLoss.setter
	def Binary_latency_modeAccLoss(self, value):
		self._set_attribute('binary_latency_modeAccLoss', value)

	@property
	def Binary_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('binary_latency_scaleAccLoss')
	@Binary_latency_scaleAccLoss.setter
	def Binary_latency_scaleAccLoss(self, value):
		self._set_attribute('binary_latency_scaleAccLoss', value)

	@property
	def Binary_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_latency_thresholdAccLoss')
	@Binary_latency_thresholdAccLoss.setter
	def Binary_latency_thresholdAccLoss(self, value):
		self._set_attribute('binary_latency_thresholdAccLoss', value)

	@property
	def Binary_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_seq_enableAccLoss')
	@Binary_seq_enableAccLoss.setter
	def Binary_seq_enableAccLoss(self, value):
		self._set_attribute('binary_seq_enableAccLoss', value)

	@property
	def Binary_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('binary_seq_modeAccLoss')
	@Binary_seq_modeAccLoss.setter
	def Binary_seq_modeAccLoss(self, value):
		self._set_attribute('binary_seq_modeAccLoss', value)

	@property
	def Binary_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_seq_thresholdAccLoss')
	@Binary_seq_thresholdAccLoss.setter
	def Binary_seq_thresholdAccLoss(self, value):
		self._set_attribute('binary_seq_thresholdAccLoss', value)

	@property
	def BurstSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CalculateJitter(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('calculateJitter')
	@CalculateJitter.setter
	def CalculateJitter(self, value):
		self._set_attribute('calculateJitter', value)

	@property
	def CalculateLatency(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def CalibrateLatency(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('calibrateLatency')
	@CalibrateLatency.setter
	def CalibrateLatency(self, value):
		self._set_attribute('calibrateLatency', value)

	@property
	def CountRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def CountRandomIpRatio(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('countRandomIpRatio')
	@CountRandomIpRatio.setter
	def CountRandomIpRatio(self, value):
		self._set_attribute('countRandomIpRatio', value)

	@property
	def CountRandomLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('countRandomLoadRate')
	@CountRandomLoadRate.setter
	def CountRandomLoadRate(self, value):
		self._set_attribute('countRandomLoadRate', value)

	@property
	def CustomLoadUnit(self):
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def DelayAfterTransmit(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DetailedResultsEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('detailedResultsEnabled')
	@DetailedResultsEnabled.setter
	def DetailedResultsEnabled(self, value):
		self._set_attribute('detailedResultsEnabled', value)

	@property
	def Duration(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableDataIntegrity(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

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
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableOldStatsForReef(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def FloodedFramesEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('floodedFramesEnabled')
	@FloodedFramesEnabled.setter
	def FloodedFramesEnabled(self, value):
		self._set_attribute('floodedFramesEnabled', value)

	@property
	def ForceRegenerate(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameLossUnit(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('frameLossUnit')
	@FrameLossUnit.setter
	def FrameLossUnit(self, value):
		self._set_attribute('frameLossUnit', value)

	@property
	def FrameSizeMode(self):
		"""NOT DEFINED

		Returns:
			str(custom|increment|random|unchanged)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesPerBurstGap(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('framesPerBurstGap')
	@FramesPerBurstGap.setter
	def FramesPerBurstGap(self, value):
		self._set_attribute('framesPerBurstGap', value)

	@property
	def Framesize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeImixList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('framesizeImixList')
	@FramesizeImixList.setter
	def FramesizeImixList(self, value):
		self._set_attribute('framesizeImixList', value)

	@property
	def FramesizeList(self):
		"""NOT DEFINED

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def Gap(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def ImixAdd(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('imixAdd')
	@ImixAdd.setter
	def ImixAdd(self, value):
		self._set_attribute('imixAdd', value)

	@property
	def ImixData(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('imixData')
	@ImixData.setter
	def ImixData(self, value):
		self._set_attribute('imixData', value)

	@property
	def ImixDelete(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('imixDelete')
	@ImixDelete.setter
	def ImixDelete(self, value):
		self._set_attribute('imixDelete', value)

	@property
	def ImixDistribution(self):
		"""NOT DEFINED

		Returns:
			str(bwpercentage|weight)
		"""
		return self._get_attribute('imixDistribution')
	@ImixDistribution.setter
	def ImixDistribution(self, value):
		self._set_attribute('imixDistribution', value)

	@property
	def ImixEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('imixEnabled')
	@ImixEnabled.setter
	def ImixEnabled(self, value):
		self._set_attribute('imixEnabled', value)

	@property
	def ImixTemplates(self):
		"""NOT DEFINED

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('imixTemplates')
	@ImixTemplates.setter
	def ImixTemplates(self, value):
		self._set_attribute('imixTemplates', value)

	@property
	def ImixTrafficType(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('imixTrafficType')
	@ImixTrafficType.setter
	def ImixTrafficType(self, value):
		self._set_attribute('imixTrafficType', value)

	@property
	def IncrementLoadUnit(self):
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

	@property
	def InitialIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('initialIncrementLoadRate')
	@InitialIncrementLoadRate.setter
	def InitialIncrementLoadRate(self, value):
		self._set_attribute('initialIncrementLoadRate', value)

	@property
	def IpRatioMode(self):
		"""NOT DEFINED

		Returns:
			str(custom|fixed|increment|random)
		"""
		return self._get_attribute('ipRatioMode')
	@IpRatioMode.setter
	def IpRatioMode(self, value):
		self._set_attribute('ipRatioMode', value)

	@property
	def Ipv4RatioList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('ipv4RatioList')
	@Ipv4RatioList.setter
	def Ipv4RatioList(self, value):
		self._set_attribute('ipv4RatioList', value)

	@property
	def Ipv4rate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('ipv4rate')
	@Ipv4rate.setter
	def Ipv4rate(self, value):
		self._set_attribute('ipv4rate', value)

	@property
	def Ipv6RatioList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('ipv6RatioList')
	@Ipv6RatioList.setter
	def Ipv6RatioList(self, value):
		self._set_attribute('ipv6RatioList', value)

	@property
	def Ipv6rate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('ipv6rate')
	@Ipv6rate.setter
	def Ipv6rate(self, value):
		self._set_attribute('ipv6rate', value)

	@property
	def LatencyBins(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('latencyBins')
	@LatencyBins.setter
	def LatencyBins(self, value):
		self._set_attribute('latencyBins', value)

	@property
	def LatencyBinsEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('latencyBinsEnabled')
	@LatencyBinsEnabled.setter
	def LatencyBinsEnabled(self, value):
		self._set_attribute('latencyBinsEnabled', value)

	@property
	def LatencyType(self):
		"""NOT DEFINED

		Returns:
			str(cutThrough|forwardingDelay|mef|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('loadRate')
	@LoadRate.setter
	def LoadRate(self, value):
		self._set_attribute('loadRate', value)

	@property
	def LoadRateList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadType(self):
		"""NOT DEFINED

		Returns:
			str(binary)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def LoadUnit(self):
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('loadUnit')
	@LoadUnit.setter
	def LoadUnit(self, value):
		self._set_attribute('loadUnit', value)

	@property
	def MapType(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxIncrementIpv4Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('maxIncrementIpv4Ratio')
	@MaxIncrementIpv4Ratio.setter
	def MaxIncrementIpv4Ratio(self, value):
		self._set_attribute('maxIncrementIpv4Ratio', value)

	@property
	def MaxIncrementIpv6Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('maxIncrementIpv6Ratio')
	@MaxIncrementIpv6Ratio.setter
	def MaxIncrementIpv6Ratio(self, value):
		self._set_attribute('maxIncrementIpv6Ratio', value)

	@property
	def MaxIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementLoadRate')
	@MaxIncrementLoadRate.setter
	def MaxIncrementLoadRate(self, value):
		self._set_attribute('maxIncrementLoadRate', value)

	@property
	def MaxRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MaxRandomIpv4Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('maxRandomIpv4Ratio')
	@MaxRandomIpv4Ratio.setter
	def MaxRandomIpv4Ratio(self, value):
		self._set_attribute('maxRandomIpv4Ratio', value)

	@property
	def MaxRandomIpv6Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('maxRandomIpv6Ratio')
	@MaxRandomIpv6Ratio.setter
	def MaxRandomIpv6Ratio(self, value):
		self._set_attribute('maxRandomIpv6Ratio', value)

	@property
	def MaxRandomLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxRandomLoadRate')
	@MaxRandomLoadRate.setter
	def MaxRandomLoadRate(self, value):
		self._set_attribute('maxRandomLoadRate', value)

	@property
	def MinFpsRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minFpsRate')
	@MinFpsRate.setter
	def MinFpsRate(self, value):
		self._set_attribute('minFpsRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinIncrementIpv4Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('minIncrementIpv4Ratio')
	@MinIncrementIpv4Ratio.setter
	def MinIncrementIpv4Ratio(self, value):
		self._set_attribute('minIncrementIpv4Ratio', value)

	@property
	def MinIncrementIpv6Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('minIncrementIpv6Ratio')
	@MinIncrementIpv6Ratio.setter
	def MinIncrementIpv6Ratio(self, value):
		self._set_attribute('minIncrementIpv6Ratio', value)

	@property
	def MinKbpsRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minKbpsRate')
	@MinKbpsRate.setter
	def MinKbpsRate(self, value):
		self._set_attribute('minKbpsRate', value)

	@property
	def MinRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def MinRandomIpv4Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('minRandomIpv4Ratio')
	@MinRandomIpv4Ratio.setter
	def MinRandomIpv4Ratio(self, value):
		self._set_attribute('minRandomIpv4Ratio', value)

	@property
	def MinRandomIpv6Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('minRandomIpv6Ratio')
	@MinRandomIpv6Ratio.setter
	def MinRandomIpv6Ratio(self, value):
		self._set_attribute('minRandomIpv6Ratio', value)

	@property
	def MinRandomLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minRandomLoadRate')
	@MinRandomLoadRate.setter
	def MinRandomLoadRate(self, value):
		self._set_attribute('minRandomLoadRate', value)

	@property
	def NumFrames(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numFrames')
	@NumFrames.setter
	def NumFrames(self, value):
		self._set_attribute('numFrames', value)

	@property
	def NumFramesFromula(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('numFramesFromula')
	@NumFramesFromula.setter
	def NumFramesFromula(self, value):
		self._set_attribute('numFramesFromula', value)

	@property
	def Numtrials(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PeakLoadingReplicationCount(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('peakLoadingReplicationCount')
	@PeakLoadingReplicationCount.setter
	def PeakLoadingReplicationCount(self, value):
		self._set_attribute('peakLoadingReplicationCount', value)

	@property
	def PerTrafficResults(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('perTrafficResults')
	@PerTrafficResults.setter
	def PerTrafficResults(self, value):
		self._set_attribute('perTrafficResults', value)

	@property
	def PercentMaxRate(self):
		"""NOT DEFINED

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
		"""NOT DEFINED

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""NOT DEFINED

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
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('randomLoadUnit')
	@RandomLoadUnit.setter
	def RandomLoadUnit(self, value):
		self._set_attribute('randomLoadUnit', value)

	@property
	def RateSelect(self):
		"""NOT DEFINED

		Returns:
			str(fpsRate|kbpsRate|percentMaxRate)
		"""
		return self._get_attribute('rateSelect')
	@RateSelect.setter
	def RateSelect(self, value):
		self._set_attribute('rateSelect', value)

	@property
	def ReportSequenceError(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""NOT DEFINED

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Resolution(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('resolution')
	@Resolution.setter
	def Resolution(self, value):
		self._set_attribute('resolution', value)

	@property
	def Rfc2544ImixDataQoS(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('rfc2544ImixDataQoS')
	@Rfc2544ImixDataQoS.setter
	def Rfc2544ImixDataQoS(self, value):
		self._set_attribute('rfc2544ImixDataQoS', value)

	@property
	def Rfc2889ordering(self):
		"""NOT DEFINED

		Returns:
			str(noOrdering|peakLoading|unchanged|val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def SendFullyMeshed(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('sendFullyMeshed')
	@SendFullyMeshed.setter
	def SendFullyMeshed(self, value):
		self._set_attribute('sendFullyMeshed', value)

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
	def StaggeredStart(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def StepIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def StepIncrementIpv4Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('stepIncrementIpv4Ratio')
	@StepIncrementIpv4Ratio.setter
	def StepIncrementIpv4Ratio(self, value):
		self._set_attribute('stepIncrementIpv4Ratio', value)

	@property
	def StepIncrementIpv6Ratio(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('stepIncrementIpv6Ratio')
	@StepIncrementIpv6Ratio.setter
	def StepIncrementIpv6Ratio(self, value):
		self._set_attribute('stepIncrementIpv6Ratio', value)

	@property
	def StepIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementLoadRate')
	@StepIncrementLoadRate.setter
	def StepIncrementLoadRate(self, value):
		self._set_attribute('stepIncrementLoadRate', value)

	@property
	def SupportedTrafficTypes(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def Tolerance(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""NOT DEFINED

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	def update(self, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryResolution=None, BinaryTolerance=None, Binary_delay_enableAccLoss=None, Binary_delay_modeAccLoss=None, Binary_delay_scaleAccLoss=None, Binary_delay_thresholdAccLoss=None, Binary_flooded_enableAccLoss=None, Binary_flooded_thresholdAccLoss=None, Binary_integrity_enableAccLoss=None, Binary_integrity_thresholdAccLoss=None, Binary_latency_enableAccLoss=None, Binary_latency_modeAccLoss=None, Binary_latency_scaleAccLoss=None, Binary_latency_thresholdAccLoss=None, Binary_seq_enableAccLoss=None, Binary_seq_modeAccLoss=None, Binary_seq_thresholdAccLoss=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, CalibrateLatency=None, CountRandomFrameSize=None, CountRandomIpRatio=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialIncrementLoadRate=None, IpRatioMode=None, Ipv4RatioList=None, Ipv4rate=None, Ipv6RatioList=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRate=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxIncrementFrameSize=None, MaxIncrementIpv4Ratio=None, MaxIncrementIpv6Ratio=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomIpv4Ratio=None, MaxRandomIpv6Ratio=None, MaxRandomLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinIncrementIpv4Ratio=None, MinIncrementIpv6Ratio=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomIpv4Ratio=None, MinRandomIpv6Ratio=None, MinRandomLoadRate=None, NumFrames=None, NumFramesFromula=None, Numtrials=None, PeakLoadingReplicationCount=None, PerTrafficResults=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2544ImixDataQoS=None, Rfc2889ordering=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, StaggeredStart=None, StepIncrementFrameSize=None, StepIncrementIpv4Ratio=None, StepIncrementIpv6Ratio=None, StepIncrementLoadRate=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BinaryBackoff (number): NOT DEFINED
			BinaryFrameLossUnit (str(%|frames)): NOT DEFINED
			BinaryResolution (number): NOT DEFINED
			BinaryTolerance (number): NOT DEFINED
			Binary_delay_enableAccLoss (bool): NOT DEFINED
			Binary_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Binary_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Binary_delay_thresholdAccLoss (number): NOT DEFINED
			Binary_flooded_enableAccLoss (bool): NOT DEFINED
			Binary_flooded_thresholdAccLoss (number): NOT DEFINED
			Binary_integrity_enableAccLoss (bool): NOT DEFINED
			Binary_integrity_thresholdAccLoss (number): NOT DEFINED
			Binary_latency_enableAccLoss (bool): NOT DEFINED
			Binary_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Binary_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Binary_latency_thresholdAccLoss (number): NOT DEFINED
			Binary_seq_enableAccLoss (bool): NOT DEFINED
			Binary_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Binary_seq_thresholdAccLoss (number): NOT DEFINED
			BurstSize (number): NOT DEFINED
			CalculateJitter (bool): NOT DEFINED
			CalculateLatency (bool): NOT DEFINED
			CalibrateLatency (bool): NOT DEFINED
			CountRandomFrameSize (number): NOT DEFINED
			CountRandomIpRatio (number): NOT DEFINED
			CountRandomLoadRate (number): NOT DEFINED
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			DelayAfterTransmit (number): NOT DEFINED
			DetailedResultsEnabled (bool): NOT DEFINED
			Duration (number): NOT DEFINED
			EnableDataIntegrity (bool): NOT DEFINED
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): NOT DEFINED
			EnableOldStatsForReef (bool): NOT DEFINED
			FloodedFramesEnabled (bool): NOT DEFINED
			ForceRegenerate (bool): NOT DEFINED
			FrameLossUnit (str): NOT DEFINED
			FrameSizeMode (str(custom|increment|random|unchanged)): NOT DEFINED
			FramesPerBurstGap (number): NOT DEFINED
			Framesize (str): NOT DEFINED
			FramesizeImixList (str): NOT DEFINED
			FramesizeList (list(str)): NOT DEFINED
			Gap (number): NOT DEFINED
			GenerateTrackingOptionAggregationFiles (bool): NOT DEFINED
			ImixAdd (str): NOT DEFINED
			ImixData (str): NOT DEFINED
			ImixDelete (str): NOT DEFINED
			ImixDistribution (str(bwpercentage|weight)): NOT DEFINED
			ImixEnabled (bool): NOT DEFINED
			ImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): NOT DEFINED
			ImixTrafficType (str): NOT DEFINED
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			InitialIncrementLoadRate (number): NOT DEFINED
			IpRatioMode (str(custom|fixed|increment|random)): NOT DEFINED
			Ipv4RatioList (str): NOT DEFINED
			Ipv4rate (number): NOT DEFINED
			Ipv6RatioList (str): NOT DEFINED
			Ipv6rate (number): NOT DEFINED
			LatencyBins (str): NOT DEFINED
			LatencyBinsEnabled (bool): NOT DEFINED
			LatencyType (str(cutThrough|forwardingDelay|mef|storeForward)): NOT DEFINED
			LoadRate (number): NOT DEFINED
			LoadRateList (str): NOT DEFINED
			LoadType (str(binary)): NOT DEFINED
			LoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			MapType (str): NOT DEFINED
			MaxIncrementFrameSize (number): NOT DEFINED
			MaxIncrementIpv4Ratio (str): NOT DEFINED
			MaxIncrementIpv6Ratio (str): NOT DEFINED
			MaxIncrementLoadRate (number): NOT DEFINED
			MaxRandomFrameSize (number): NOT DEFINED
			MaxRandomIpv4Ratio (str): NOT DEFINED
			MaxRandomIpv6Ratio (str): NOT DEFINED
			MaxRandomLoadRate (number): NOT DEFINED
			MinFpsRate (number): NOT DEFINED
			MinIncrementFrameSize (number): NOT DEFINED
			MinIncrementIpv4Ratio (str): NOT DEFINED
			MinIncrementIpv6Ratio (str): NOT DEFINED
			MinKbpsRate (number): NOT DEFINED
			MinRandomFrameSize (number): NOT DEFINED
			MinRandomIpv4Ratio (str): NOT DEFINED
			MinRandomIpv6Ratio (str): NOT DEFINED
			MinRandomLoadRate (number): NOT DEFINED
			NumFrames (number): NOT DEFINED
			NumFramesFromula (str): 
			Numtrials (number): NOT DEFINED
			PeakLoadingReplicationCount (number): NOT DEFINED
			PerTrafficResults (bool): 
			PercentMaxRate (number): NOT DEFINED
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): NOT DEFINED
			PortDelayValue (number): NOT DEFINED
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			RandomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			RateSelect (str(fpsRate|kbpsRate|percentMaxRate)): NOT DEFINED
			ReportSequenceError (bool): NOT DEFINED
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): NOT DEFINED
			Resolution (number): NOT DEFINED
			Rfc2544ImixDataQoS (bool): NOT DEFINED
			Rfc2889ordering (str(noOrdering|peakLoading|unchanged|val2889Ordering)): NOT DEFINED
			SendFullyMeshed (bool): NOT DEFINED
			ShowDetailedBinaryResults (bool): NOT DEFINED
			StaggeredStart (bool): NOT DEFINED
			StepIncrementFrameSize (number): NOT DEFINED
			StepIncrementIpv4Ratio (str): NOT DEFINED
			StepIncrementIpv6Ratio (str): NOT DEFINED
			StepIncrementLoadRate (number): NOT DEFINED
			SupportedTrafficTypes (str): NOT DEFINED
			Tolerance (number): NOT DEFINED
			TrafficType (str(burstyLoading|constantLoading)): NOT DEFINED
			TxDelay (number): NOT DEFINED

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
