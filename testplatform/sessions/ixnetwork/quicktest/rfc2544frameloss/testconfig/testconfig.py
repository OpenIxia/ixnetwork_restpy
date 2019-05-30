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
	def CalibrateLatency(self):
		"""If true, calibrates the latency.

		Returns:
			bool
		"""
		return self._get_attribute('calibrateLatency')
	@CalibrateLatency.setter
	def CalibrateLatency(self, value):
		self._set_attribute('calibrateLatency', value)

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
	def CountRandomIpRatio(self):
		"""Sets the count of the random ip ratio loop

		Returns:
			number
		"""
		return self._get_attribute('countRandomIpRatio')
	@CountRandomIpRatio.setter
	def CountRandomIpRatio(self, value):
		self._set_attribute('countRandomIpRatio', value)

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
		"""Specifies the amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DetailedResultsEnabled(self):
		"""If true, it enables the detailed results for the fully meshed case

		Returns:
			bool
		"""
		return self._get_attribute('detailedResultsEnabled')
	@DetailedResultsEnabled.setter
	def DetailedResultsEnabled(self, value):
		self._set_attribute('detailedResultsEnabled', value)

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
	def EnableOldStatsForReef(self):
		"""If true, enables old statistics for reef load module.

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def FloodedFramesEnabled(self):
		"""If true, it enables the flooded frames statistics

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
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian.

		Returns:
			str(custom|increment|random|unchanged)
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
		"""The frame size to be used.

		Returns:
			str
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeImixList(self):
		"""The list of the available lmix frame sizes.

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
		"""If true, enables the tracking option in aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def Grain(self):
		"""The granular value of the test parameter.

		Returns:
			str(coarse|fine)
		"""
		return self._get_attribute('grain')
	@Grain.setter
	def Grain(self, value):
		self._set_attribute('grain', value)

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
		"""Displays imix data.

		Returns:
			str
		"""
		return self._get_attribute('imixData')
	@ImixData.setter
	def ImixData(self, value):
		self._set_attribute('imixData', value)

	@property
	def ImixDelete(self):
		"""Deletes an imix data.

		Returns:
			str
		"""
		return self._get_attribute('imixDelete')
	@ImixDelete.setter
	def ImixDelete(self, value):
		self._set_attribute('imixDelete', value)

	@property
	def ImixDistribution(self):
		"""Shows the distribution of imix data.

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
	def IncrementLoadUnit(self):
		"""The unit increment for the load.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

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
	def IpRatioMode(self):
		"""Sets the ip ratio mode

		Returns:
			str(custom|fixed|increment|random)
		"""
		return self._get_attribute('ipRatioMode')
	@IpRatioMode.setter
	def IpRatioMode(self, value):
		self._set_attribute('ipRatioMode', value)

	@property
	def Ipv4RatioList(self):
		"""Sets the ipv4 ratio list

		Returns:
			str
		"""
		return self._get_attribute('ipv4RatioList')
	@Ipv4RatioList.setter
	def Ipv4RatioList(self, value):
		self._set_attribute('ipv4RatioList', value)

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
	def Ipv6RatioList(self):
		"""Sets the ipv6 ratio list

		Returns:
			str
		"""
		return self._get_attribute('ipv6RatioList')
	@Ipv6RatioList.setter
	def Ipv6RatioList(self, value):
		self._set_attribute('ipv6RatioList', value)

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
			str(cutThrough|forwardingDelay|mef|storeForward)
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
	def LoadType(self):
		"""The type of the payload setting.

		Returns:
			str(step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def LoadUnit(self):
		"""The load unit value.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('loadUnit')
	@LoadUnit.setter
	def LoadUnit(self, value):
		self._set_attribute('loadUnit', value)

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
	def MaxIncrementIpv4Ratio(self):
		"""Sets the maximum increment value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxIncrementIpv4Ratio')
	@MaxIncrementIpv4Ratio.setter
	def MaxIncrementIpv4Ratio(self, value):
		self._set_attribute('maxIncrementIpv4Ratio', value)

	@property
	def MaxIncrementIpv6Ratio(self):
		"""Sets the maximum increment value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxIncrementIpv6Ratio')
	@MaxIncrementIpv6Ratio.setter
	def MaxIncrementIpv6Ratio(self, value):
		self._set_attribute('maxIncrementIpv6Ratio', value)

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
	def MaxRandomIpv4Ratio(self):
		"""Sets the maximum radom value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxRandomIpv4Ratio')
	@MaxRandomIpv4Ratio.setter
	def MaxRandomIpv4Ratio(self, value):
		self._set_attribute('maxRandomIpv4Ratio', value)

	@property
	def MaxRandomIpv6Ratio(self):
		"""Sets the maximum random value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxRandomIpv6Ratio')
	@MaxRandomIpv6Ratio.setter
	def MaxRandomIpv6Ratio(self, value):
		self._set_attribute('maxRandomIpv6Ratio', value)

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
	def MinIncrementIpv4Ratio(self):
		"""Sets the minimum increment value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('minIncrementIpv4Ratio')
	@MinIncrementIpv4Ratio.setter
	def MinIncrementIpv4Ratio(self, value):
		self._set_attribute('minIncrementIpv4Ratio', value)

	@property
	def MinIncrementIpv6Ratio(self):
		"""Sets the minimum increment value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('minIncrementIpv6Ratio')
	@MinIncrementIpv6Ratio.setter
	def MinIncrementIpv6Ratio(self, value):
		self._set_attribute('minIncrementIpv6Ratio', value)

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
	def MinRandomIpv4Ratio(self):
		"""Sets the minimum random value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('minRandomIpv4Ratio')
	@MinRandomIpv4Ratio.setter
	def MinRandomIpv4Ratio(self, value):
		self._set_attribute('minRandomIpv4Ratio', value)

	@property
	def MinRandomIpv6Ratio(self):
		"""Sets the minimum random value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('minRandomIpv6Ratio')
	@MinRandomIpv6Ratio.setter
	def MinRandomIpv6Ratio(self, value):
		self._set_attribute('minRandomIpv6Ratio', value)

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
	def MinStepLoadRate(self):
		"""The minimum step value of load rate.

		Returns:
			number
		"""
		return self._get_attribute('minStepLoadRate')
	@MinStepLoadRate.setter
	def MinStepLoadRate(self, value):
		self._set_attribute('minStepLoadRate', value)

	@property
	def NumFrames(self):
		"""The number of frames sent.

		Returns:
			number
		"""
		return self._get_attribute('numFrames')
	@NumFrames.setter
	def NumFrames(self, value):
		self._set_attribute('numFrames', value)

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
		"""The maximum percentage rate.

		Returns:
			number
		"""
		return self._get_attribute('percentMaxRate')
	@PercentMaxRate.setter
	def PercentMaxRate(self, value):
		self._set_attribute('percentMaxRate', value)

	@property
	def PortDelayEnabled(self):
		"""Enables the port delay.

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
	def Rfc2544ImixDataQoS(self):
		"""If true, it uses the same frame data qos

		Returns:
			bool
		"""
		return self._get_attribute('rfc2544ImixDataQoS')
	@Rfc2544ImixDataQoS.setter
	def Rfc2544ImixDataQoS(self, value):
		self._set_attribute('rfc2544ImixDataQoS', value)

	@property
	def Rfc2889ordering(self):
		"""If true, indicates frame ordering by Rfc2889.

		Returns:
			str(noOrdering|peakLoading|unchanged|val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def Runmode(self):
		"""Specifies the number of frames that IxNetwork sends from each port in running mode.

		Returns:
			str(duration|noframes)
		"""
		return self._get_attribute('runmode')
	@Runmode.setter
	def Runmode(self, value):
		self._set_attribute('runmode', value)

	@property
	def SendFullyMeshed(self):
		"""Indicates the source group mapping type used for sending data.

		Returns:
			bool
		"""
		return self._get_attribute('sendFullyMeshed')
	@SendFullyMeshed.setter
	def SendFullyMeshed(self, value):
		self._set_attribute('sendFullyMeshed', value)

	@property
	def ShowDetailedBinaryResults(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('showDetailedBinaryResults')
	@ShowDetailedBinaryResults.setter
	def ShowDetailedBinaryResults(self, value):
		self._set_attribute('showDetailedBinaryResults', value)

	@property
	def StaggeredStart(self):
		"""Starts test with a stagger.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

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
	def StepIncrementIpv4Ratio(self):
		"""The step in which the ipv4 ratio loop is incremented

		Returns:
			str
		"""
		return self._get_attribute('stepIncrementIpv4Ratio')
	@StepIncrementIpv4Ratio.setter
	def StepIncrementIpv4Ratio(self, value):
		self._set_attribute('stepIncrementIpv4Ratio', value)

	@property
	def StepIncrementIpv6Ratio(self):
		"""The step in which the ipv6 ratio loop is incremented

		Returns:
			str
		"""
		return self._get_attribute('stepIncrementIpv6Ratio')
	@StepIncrementIpv6Ratio.setter
	def StepIncrementIpv6Ratio(self, value):
		self._set_attribute('stepIncrementIpv6Ratio', value)

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
	def StepLoadRateFormula(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('stepLoadRateFormula')
	@StepLoadRateFormula.setter
	def StepLoadRateFormula(self, value):
		self._set_attribute('stepLoadRateFormula', value)

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
	def StepTiLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('stepTiLoss')
	@StepTiLoss.setter
	def StepTiLoss(self, value):
		self._set_attribute('stepTiLoss', value)

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
		"""Specifies the amount of delay after every transmit.

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
	def UseTiLoss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('useTiLoss')
	@UseTiLoss.setter
	def UseTiLoss(self, value):
		self._set_attribute('useTiLoss', value)

	def update(self, BurstSize=None, CalculateJitter=None, CalculateLatency=None, CalibrateLatency=None, CountRandomFrameSize=None, CountRandomIpRatio=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, Grain=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, IpRatioMode=None, Ipv4RatioList=None, Ipv4rate=None, Ipv6RatioList=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxIncrementFrameSize=None, MaxIncrementIpv4Ratio=None, MaxIncrementIpv6Ratio=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomIpv4Ratio=None, MaxRandomIpv6Ratio=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinIncrementIpv4Ratio=None, MinIncrementIpv6Ratio=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomIpv4Ratio=None, MinRandomIpv6Ratio=None, MinRandomLoadRate=None, MinStepLoadRate=None, NumFrames=None, Numtrials=None, PeakLoadingReplicationCount=None, PerTrafficResults=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2544ImixDataQoS=None, Rfc2889ordering=None, Runmode=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, StaggeredStart=None, StepIncrementFrameSize=None, StepIncrementIpv4Ratio=None, StepIncrementIpv6Ratio=None, StepIncrementLoadRate=None, StepLoadRateFormula=None, StepLoadUnit=None, StepStepLoadRate=None, StepTiLoss=None, StepTolerance=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedValueList=None, UseTiLoss=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BurstSize (number): The number of packets to send in a burst.
			CalculateJitter (bool): If true, the jitter is calculated.
			CalculateLatency (bool): If true, calculates the latency.
			CalibrateLatency (bool): If true, calibrates the latency.
			CountRandomFrameSize (number): If true, randomly counts the frame size.
			CountRandomIpRatio (number): Sets the count of the random ip ratio loop
			CountRandomLoadRate (number): The random count of the load rate.
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the custom load unit.
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
			DetailedResultsEnabled (bool): If true, it enables the detailed results for the fully meshed case
			Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
			EnableDataIntegrity (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
			FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
			ForceRegenerate (bool): Initiates a forced regeneration.
			FrameSizeMode (str(custom|increment|random|unchanged)): This attribute is the frame size mode for the Quad Gaussian.
			FramesPerBurstGap (number): The number of frames to be sent after each burst.
			Framesize (str): The frame size to be used.
			FramesizeImixList (str): The list of the available lmix frame sizes.
			FramesizeList (list(str)): The list of the available frame sizes.
			Gap (number): The gap in transmission of frames.
			GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
			Grain (str(coarse|fine)): The granular value of the test parameter.
			ImixAdd (str): Adds an imix data.
			ImixData (str): Displays imix data.
			ImixDelete (str): Deletes an imix data.
			ImixDistribution (str(bwpercentage|weight)): Shows the distribution of imix data.
			ImixEnabled (bool): If True, Enables the imix value.
			ImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Specefies the imix templates.
			ImixTrafficType (str): Displays the imix traffic type.
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The unit increment for the load.
			InitialIncrementLoadRate (number): The initial incremental value of the load rate.
			InitialStepLoadRate (number): The initial step value of the load rate.
			IpRatioMode (str(custom|fixed|increment|random)): Sets the ip ratio mode
			Ipv4RatioList (str): Sets the ipv4 ratio list
			Ipv4rate (number): The rate at which IPv4 traffic is sent.
			Ipv6RatioList (str): Sets the ipv6 ratio list
			Ipv6rate (number): The rate at which IPv6 traffic is sent.
			LatencyBins (str): Sets the latency bins statistics.
			LatencyBinsEnabled (bool): Enables the latency bins statistics.
			LatencyType (str(cutThrough|forwardingDelay|mef|storeForward)): The type of latency.
			LoadRateList (str): Enters the Load Rate List.
			LoadType (str(step)): The type of the payload setting.
			LoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The load unit value.
			MapType (str): The mapping type.
			MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
			MaxIncrementIpv4Ratio (str): Sets the maximum increment value for the ipv4 ratio
			MaxIncrementIpv6Ratio (str): Sets the maximum increment value for the ipv6 ratio
			MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
			MaxRandomFrameSize (number): The maximum random frame size to be sent.
			MaxRandomIpv4Ratio (str): Sets the maximum radom value for the ipv4 ratio
			MaxRandomIpv6Ratio (str): Sets the maximum random value for the ipv6 ratio
			MaxRandomLoadRate (number): The maximum random value of the load rate.
			MaxStepLoadRate (number): The maximum step value of the load rate.
			MinFpsRate (number): The rate at which minimum frames are sent per second.
			MinIncrementFrameSize (number): The minimum incremental value of the frame size.
			MinIncrementIpv4Ratio (str): Sets the minimum increment value for the ipv4 ratio
			MinIncrementIpv6Ratio (str): Sets the minimum increment value for the ipv6 ratio
			MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			MinRandomIpv4Ratio (str): Sets the minimum random value for the ipv4 ratio
			MinRandomIpv6Ratio (str): Sets the minimum random value for the ipv6 ratio
			MinRandomLoadRate (number): The maximum random value of the load rate.
			MinStepLoadRate (number): The minimum step value of load rate.
			NumFrames (number): The number of frames sent.
			Numtrials (number): The integer value that states the number of trials permitted.
			PeakLoadingReplicationCount (number): NOT DEFINED
			PerTrafficResults (bool): 
			PercentMaxRate (number): The maximum percentage rate.
			PortDelayEnabled (bool): Enables the port delay.
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured
			PortDelayValue (number): Sets the port delay value.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			RandomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The random values of the load unit.
			RateSelect (str(fpsRate|kbpsRate|percentMaxRate)): The rate selected.
			ReportSequenceError (bool): Reports sequence errors in the test result.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The unit of rate for throughput.
			Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
			Rfc2544ImixDataQoS (bool): If true, it uses the same frame data qos
			Rfc2889ordering (str(noOrdering|peakLoading|unchanged|val2889Ordering)): If true, indicates frame ordering by Rfc2889.
			Runmode (str(duration|noframes)): Specifies the number of frames that IxNetwork sends from each port in running mode.
			SendFullyMeshed (bool): Indicates the source group mapping type used for sending data.
			ShowDetailedBinaryResults (bool): 
			StaggeredStart (bool): Starts test with a stagger.
			StepIncrementFrameSize (number): The incremental step value of the frame size.
			StepIncrementIpv4Ratio (str): The step in which the ipv4 ratio loop is incremented
			StepIncrementIpv6Ratio (str): The step in which the ipv6 ratio loop is incremented
			StepIncrementLoadRate (number): The step incremental value of the load rate.
			StepLoadRateFormula (str): 
			StepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the step rate of the load unit.
			StepStepLoadRate (number): The incremental step value of load rate.
			StepTiLoss (bool): NOT DEFINED
			StepTolerance (number): The step value of the tolerance level.
			SupportedTrafficTypes (str): The traffic types supported.
			Tolerance (number): The value set for the tolerance level.
			TrafficType (str(burstyLoading|constantLoading)): The test based on the traffic type.
			TxDelay (number): Specifies the amount of delay after every transmit.
			UnchangedValueList (str): The number of unchanged sessions.
			UseTiLoss (str): NOT DEFINED

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
