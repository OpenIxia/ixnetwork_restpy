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
	def AggregateByDirection(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('aggregateByDirection')
	@AggregateByDirection.setter
	def AggregateByDirection(self, value):
		self._set_attribute('aggregateByDirection', value)

	@property
	def AggregateByFlowgroup(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('aggregateByFlowgroup')
	@AggregateByFlowgroup.setter
	def AggregateByFlowgroup(self, value):
		self._set_attribute('aggregateByFlowgroup', value)

	@property
	def AggregateByPort(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('aggregateByPort')
	@AggregateByPort.setter
	def AggregateByPort(self, value):
		self._set_attribute('aggregateByPort', value)

	@property
	def BackoffIteration(self):
		"""Signifies the back of iteration.

		Returns:
			number
		"""
		return self._get_attribute('backoffIteration')
	@BackoffIteration.setter
	def BackoffIteration(self, value):
		self._set_attribute('backoffIteration', value)

	@property
	def BinaryAcceptableFrameLossLabel(self):
		"""Signifies the binary value of acceptable frame loss label

		Returns:
			str
		"""
		return self._get_attribute('binaryAcceptableFrameLossLabel')
	@BinaryAcceptableFrameLossLabel.setter
	def BinaryAcceptableFrameLossLabel(self, value):
		self._set_attribute('binaryAcceptableFrameLossLabel', value)

	@property
	def BinaryBackoffLabel(self):
		"""Signifies the binary backoff label

		Returns:
			str
		"""
		return self._get_attribute('binaryBackoffLabel')
	@BinaryBackoffLabel.setter
	def BinaryBackoffLabel(self, value):
		self._set_attribute('binaryBackoffLabel', value)

	@property
	def BinaryInitialRateLabel(self):
		"""Signifies initial rate label

		Returns:
			str
		"""
		return self._get_attribute('binaryInitialRateLabel')
	@BinaryInitialRateLabel.setter
	def BinaryInitialRateLabel(self, value):
		self._set_attribute('binaryInitialRateLabel', value)

	@property
	def BinaryLoadUnitLabel(self):
		"""Signifies the binary load unit label

		Returns:
			str
		"""
		return self._get_attribute('binaryLoadUnitLabel')
	@BinaryLoadUnitLabel.setter
	def BinaryLoadUnitLabel(self, value):
		self._set_attribute('binaryLoadUnitLabel', value)

	@property
	def BinaryMaxRateLabel(self):
		"""Signifies the binary maximum rate label

		Returns:
			str
		"""
		return self._get_attribute('binaryMaxRateLabel')
	@BinaryMaxRateLabel.setter
	def BinaryMaxRateLabel(self, value):
		self._set_attribute('binaryMaxRateLabel', value)

	@property
	def BinaryMinRateLabel(self):
		"""Signifies the binary minimum rte label

		Returns:
			str
		"""
		return self._get_attribute('binaryMinRateLabel')
	@BinaryMinRateLabel.setter
	def BinaryMinRateLabel(self, value):
		self._set_attribute('binaryMinRateLabel', value)

	@property
	def BinaryResolutionLabel(self):
		"""Signifies the binary resolution label

		Returns:
			str
		"""
		return self._get_attribute('binaryResolutionLabel')
	@BinaryResolutionLabel.setter
	def BinaryResolutionLabel(self, value):
		self._set_attribute('binaryResolutionLabel', value)

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
		"""If true, calculates latency.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def DelayAfterTransmit(self):
		"""Signifies the delay time after transmit of the packet.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DownstreamBinaryBackoff(self):
		"""Signifies the downstream binary backoff

		Returns:
			number
		"""
		return self._get_attribute('downstreamBinaryBackoff')
	@DownstreamBinaryBackoff.setter
	def DownstreamBinaryBackoff(self, value):
		self._set_attribute('downstreamBinaryBackoff', value)

	@property
	def DownstreamBinaryFrameLossUnit(self):
		"""Signifies the downstream binary frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('downstreamBinaryFrameLossUnit')
	@DownstreamBinaryFrameLossUnit.setter
	def DownstreamBinaryFrameLossUnit(self, value):
		self._set_attribute('downstreamBinaryFrameLossUnit', value)

	@property
	def DownstreamBinaryLoadUnit(self):
		"""Signifies downstream binary load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('downstreamBinaryLoadUnit')
	@DownstreamBinaryLoadUnit.setter
	def DownstreamBinaryLoadUnit(self, value):
		self._set_attribute('downstreamBinaryLoadUnit', value)

	@property
	def DownstreamBinaryResolution(self):
		"""Signifies the downstream binary resolution.

		Returns:
			number
		"""
		return self._get_attribute('downstreamBinaryResolution')
	@DownstreamBinaryResolution.setter
	def DownstreamBinaryResolution(self, value):
		self._set_attribute('downstreamBinaryResolution', value)

	@property
	def DownstreamBinarySearchType(self):
		"""This signifies the downstream binary search type.

		Returns:
			str
		"""
		return self._get_attribute('downstreamBinarySearchType')
	@DownstreamBinarySearchType.setter
	def DownstreamBinarySearchType(self, value):
		self._set_attribute('downstreamBinarySearchType', value)

	@property
	def DownstreamBinaryTolerance(self):
		"""Signifies the downstream binary tolerance.

		Returns:
			number
		"""
		return self._get_attribute('downstreamBinaryTolerance')
	@DownstreamBinaryTolerance.setter
	def DownstreamBinaryTolerance(self, value):
		self._set_attribute('downstreamBinaryTolerance', value)

	@property
	def DownstreamImixAdd(self):
		"""Adds downstream IMIX

		Returns:
			str
		"""
		return self._get_attribute('downstreamImixAdd')
	@DownstreamImixAdd.setter
	def DownstreamImixAdd(self, value):
		self._set_attribute('downstreamImixAdd', value)

	@property
	def DownstreamImixData(self):
		"""Signifies the downstream IMIX data

		Returns:
			str
		"""
		return self._get_attribute('downstreamImixData')
	@DownstreamImixData.setter
	def DownstreamImixData(self, value):
		self._set_attribute('downstreamImixData', value)

	@property
	def DownstreamImixDataQoS(self):
		"""If true, enables the quality of service for downstream IMIX

		Returns:
			bool
		"""
		return self._get_attribute('downstreamImixDataQoS')
	@DownstreamImixDataQoS.setter
	def DownstreamImixDataQoS(self, value):
		self._set_attribute('downstreamImixDataQoS', value)

	@property
	def DownstreamImixDelete(self):
		"""Deletes downstream IMIX

		Returns:
			str
		"""
		return self._get_attribute('downstreamImixDelete')
	@DownstreamImixDelete.setter
	def DownstreamImixDelete(self, value):
		self._set_attribute('downstreamImixDelete', value)

	@property
	def DownstreamImixDistribution(self):
		"""signifies the downstream imix distribution.

		Returns:
			str(bwpercentage|weight)
		"""
		return self._get_attribute('downstreamImixDistribution')
	@DownstreamImixDistribution.setter
	def DownstreamImixDistribution(self, value):
		self._set_attribute('downstreamImixDistribution', value)

	@property
	def DownstreamImixEnabled(self):
		"""If true, enables downstream IMIX

		Returns:
			bool
		"""
		return self._get_attribute('downstreamImixEnabled')
	@DownstreamImixEnabled.setter
	def DownstreamImixEnabled(self, value):
		self._set_attribute('downstreamImixEnabled', value)

	@property
	def DownstreamImixTemplates(self):
		"""Signifies downstream IMIX templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('downstreamImixTemplates')
	@DownstreamImixTemplates.setter
	def DownstreamImixTemplates(self, value):
		self._set_attribute('downstreamImixTemplates', value)

	@property
	def DownstreamInitialBinaryLoadRate(self):
		"""This signifies downstream initial binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('downstreamInitialBinaryLoadRate')
	@DownstreamInitialBinaryLoadRate.setter
	def DownstreamInitialBinaryLoadRate(self, value):
		self._set_attribute('downstreamInitialBinaryLoadRate', value)

	@property
	def DownstreamInitialStepLoadRate(self):
		"""This signifies downstream initial step load rate.

		Returns:
			number
		"""
		return self._get_attribute('downstreamInitialStepLoadRate')
	@DownstreamInitialStepLoadRate.setter
	def DownstreamInitialStepLoadRate(self, value):
		self._set_attribute('downstreamInitialStepLoadRate', value)

	@property
	def DownstreamLoadType(self):
		"""Signifies downstream load type.

		Returns:
			str
		"""
		return self._get_attribute('downstreamLoadType')
	@DownstreamLoadType.setter
	def DownstreamLoadType(self, value):
		self._set_attribute('downstreamLoadType', value)

	@property
	def DownstreamMaxBinaryLoadRate(self):
		"""Signifies maximum downstream binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('downstreamMaxBinaryLoadRate')
	@DownstreamMaxBinaryLoadRate.setter
	def DownstreamMaxBinaryLoadRate(self, value):
		self._set_attribute('downstreamMaxBinaryLoadRate', value)

	@property
	def DownstreamMaxStepLoadRate(self):
		"""Signifies downstream maximum step load rate.

		Returns:
			number
		"""
		return self._get_attribute('downstreamMaxStepLoadRate')
	@DownstreamMaxStepLoadRate.setter
	def DownstreamMaxStepLoadRate(self, value):
		self._set_attribute('downstreamMaxStepLoadRate', value)

	@property
	def DownstreamMinBinaryLoadRate(self):
		"""Signifies minimum downstream binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('downstreamMinBinaryLoadRate')
	@DownstreamMinBinaryLoadRate.setter
	def DownstreamMinBinaryLoadRate(self, value):
		self._set_attribute('downstreamMinBinaryLoadRate', value)

	@property
	def DownstreamStepFrameLossUnit(self):
		"""Signifies downstream step frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('downstreamStepFrameLossUnit')
	@DownstreamStepFrameLossUnit.setter
	def DownstreamStepFrameLossUnit(self, value):
		self._set_attribute('downstreamStepFrameLossUnit', value)

	@property
	def DownstreamStepLoadUnit(self):
		"""Signifies downstream step load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('downstreamStepLoadUnit')
	@DownstreamStepLoadUnit.setter
	def DownstreamStepLoadUnit(self, value):
		self._set_attribute('downstreamStepLoadUnit', value)

	@property
	def DownstreamStepStepLoadRate(self):
		"""This signifies downstream step load rate.

		Returns:
			str
		"""
		return self._get_attribute('downstreamStepStepLoadRate')
	@DownstreamStepStepLoadRate.setter
	def DownstreamStepStepLoadRate(self, value):
		self._set_attribute('downstreamStepStepLoadRate', value)

	@property
	def DownstreamStepTolerance(self):
		"""Signifies downstream step tolerance.

		Returns:
			number
		"""
		return self._get_attribute('downstreamStepTolerance')
	@DownstreamStepTolerance.setter
	def DownstreamStepTolerance(self, value):
		self._set_attribute('downstreamStepTolerance', value)

	@property
	def DownstreamStopTestOnHighLoss(self):
		"""This stops the downstream test on high loss.

		Returns:
			number
		"""
		return self._get_attribute('downstreamStopTestOnHighLoss')
	@DownstreamStopTestOnHighLoss.setter
	def DownstreamStopTestOnHighLoss(self, value):
		self._set_attribute('downstreamStopTestOnHighLoss', value)

	@property
	def Duration(self):
		"""Signifies the duration.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableBackoffIteration(self):
		"""If true, enables backoff iteration.

		Returns:
			bool
		"""
		return self._get_attribute('enableBackoffIteration')
	@EnableBackoffIteration.setter
	def EnableBackoffIteration(self, value):
		self._set_attribute('enableBackoffIteration', value)

	@property
	def EnableDataIntegrity(self):
		"""If true, enables data integrity.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableFastConvergence(self):
		"""If true, enables fast convergence.

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
		"""If true, enables stop test on high loss option.

		Returns:
			bool
		"""
		return self._get_attribute('enableStopTestOnHighLoss')
	@EnableStopTestOnHighLoss.setter
	def EnableStopTestOnHighLoss(self, value):
		self._set_attribute('enableStopTestOnHighLoss', value)

	@property
	def FastConvergenceDuration(self):
		"""Signifies fast convergence duration.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceDuration')
	@FastConvergenceDuration.setter
	def FastConvergenceDuration(self, value):
		self._set_attribute('fastConvergenceDuration', value)

	@property
	def FastConvergenceThreshold(self):
		"""Signifies the threshold for fast convergence.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceThreshold')
	@FastConvergenceThreshold.setter
	def FastConvergenceThreshold(self, value):
		self._set_attribute('fastConvergenceThreshold', value)

	@property
	def ForceRegenerate(self):
		"""If true, enables force regenerate.

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FramesPerBurstGap(self):
		"""Signifies the frames sent per burst gap

		Returns:
			number
		"""
		return self._get_attribute('framesPerBurstGap')
	@FramesPerBurstGap.setter
	def FramesPerBurstGap(self, value):
		self._set_attribute('framesPerBurstGap', value)

	@property
	def Gap(self):
		"""Signifies the burst gap

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""If true, generates tracking option of aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def ImixTrafficType(self):
		"""Signifies the type of IMIX traffic.

		Returns:
			str
		"""
		return self._get_attribute('imixTrafficType')
	@ImixTrafficType.setter
	def ImixTrafficType(self, value):
		self._set_attribute('imixTrafficType', value)

	@property
	def IterationParameters(self):
		"""This signifies the Iteration Parameters.

		Returns:
			str
		"""
		return self._get_attribute('iterationParameters')
	@IterationParameters.setter
	def IterationParameters(self, value):
		self._set_attribute('iterationParameters', value)

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
		"""Signifies the latency type.

		Returns:
			str(cutThrough|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadType(self):
		"""Signifies the load type.

		Returns:
			str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""Signifies the map type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def Numtrials(self):
		"""Signifies the numeric trials.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

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
	def ReportSequenceError(self):
		"""If true, reports sequence error.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""Reports throughput rate unit.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def SaturationIteration(self):
		"""Signifies saturation iteration.

		Returns:
			number
		"""
		return self._get_attribute('saturationIteration')
	@SaturationIteration.setter
	def SaturationIteration(self, value):
		self._set_attribute('saturationIteration', value)

	@property
	def StaggeredStart(self):
		"""If true, staggers start.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def StepAcceptableFrameLossLabel(self):
		"""Signifies step acceptable frame loss label

		Returns:
			str
		"""
		return self._get_attribute('stepAcceptableFrameLossLabel')
	@StepAcceptableFrameLossLabel.setter
	def StepAcceptableFrameLossLabel(self, value):
		self._set_attribute('stepAcceptableFrameLossLabel', value)

	@property
	def StepEndRateLabel(self):
		"""Signifies step end rate label

		Returns:
			str
		"""
		return self._get_attribute('stepEndRateLabel')
	@StepEndRateLabel.setter
	def StepEndRateLabel(self, value):
		self._set_attribute('stepEndRateLabel', value)

	@property
	def StepInitialRateLabel(self):
		"""Signifies step initial rate label

		Returns:
			str
		"""
		return self._get_attribute('stepInitialRateLabel')
	@StepInitialRateLabel.setter
	def StepInitialRateLabel(self, value):
		self._set_attribute('stepInitialRateLabel', value)

	@property
	def StepLoadUnitLabel(self):
		"""Signifies the step load unit label

		Returns:
			str
		"""
		return self._get_attribute('stepLoadUnitLabel')
	@StepLoadUnitLabel.setter
	def StepLoadUnitLabel(self, value):
		self._set_attribute('stepLoadUnitLabel', value)

	@property
	def StepStepRateLabel(self):
		"""Signifies the step rate label

		Returns:
			str
		"""
		return self._get_attribute('stepStepRateLabel')
	@StepStepRateLabel.setter
	def StepStepRateLabel(self, value):
		self._set_attribute('stepStepRateLabel', value)

	@property
	def SupportedTrafficTypes(self):
		"""Signifies the traffic types supported.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def TestType(self):
		"""Signifies th test type.

		Returns:
			str(downstreamOnly|upstreamDownstream|upstreamOnly)
		"""
		return self._get_attribute('testType')
	@TestType.setter
	def TestType(self, value):
		self._set_attribute('testType', value)

	@property
	def TestTypeTemp(self):
		"""Signifies the temporary test type.

		Returns:
			str(downstreamOnly|upstreamDownstream|upstreamOnly)
		"""
		return self._get_attribute('testTypeTemp')
	@TestTypeTemp.setter
	def TestTypeTemp(self, value):
		self._set_attribute('testTypeTemp', value)

	@property
	def TestTypeTemp2(self):
		"""Signifies the second temporary test type.

		Returns:
			str(downstreamOnly|upstreamDownstream|upstreamOnly)
		"""
		return self._get_attribute('testTypeTemp2')
	@TestTypeTemp2.setter
	def TestTypeTemp2(self, value):
		self._set_attribute('testTypeTemp2', value)

	@property
	def Tolerance(self):
		"""Signifies the tolerance.

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""Signifies the traffic type.

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""Signifies the delay time during the transmission of data

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UpstreamBinaryBackoff(self):
		"""Signifies upstream binary backoff

		Returns:
			number
		"""
		return self._get_attribute('upstreamBinaryBackoff')
	@UpstreamBinaryBackoff.setter
	def UpstreamBinaryBackoff(self, value):
		self._set_attribute('upstreamBinaryBackoff', value)

	@property
	def UpstreamBinaryFrameLossUnit(self):
		"""Signifies the upstream binary frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('upstreamBinaryFrameLossUnit')
	@UpstreamBinaryFrameLossUnit.setter
	def UpstreamBinaryFrameLossUnit(self, value):
		self._set_attribute('upstreamBinaryFrameLossUnit', value)

	@property
	def UpstreamBinaryLoadUnit(self):
		"""This signifies the upstream binary load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('upstreamBinaryLoadUnit')
	@UpstreamBinaryLoadUnit.setter
	def UpstreamBinaryLoadUnit(self, value):
		self._set_attribute('upstreamBinaryLoadUnit', value)

	@property
	def UpstreamBinaryResolution(self):
		"""Signifies upstream binary resolution.

		Returns:
			number
		"""
		return self._get_attribute('upstreamBinaryResolution')
	@UpstreamBinaryResolution.setter
	def UpstreamBinaryResolution(self, value):
		self._set_attribute('upstreamBinaryResolution', value)

	@property
	def UpstreamBinarySearchType(self):
		"""Signifies the upstream binary search type.

		Returns:
			str
		"""
		return self._get_attribute('upstreamBinarySearchType')
	@UpstreamBinarySearchType.setter
	def UpstreamBinarySearchType(self, value):
		self._set_attribute('upstreamBinarySearchType', value)

	@property
	def UpstreamBinaryTolerance(self):
		"""Signifies the upstream binary tolerance.

		Returns:
			number
		"""
		return self._get_attribute('upstreamBinaryTolerance')
	@UpstreamBinaryTolerance.setter
	def UpstreamBinaryTolerance(self, value):
		self._set_attribute('upstreamBinaryTolerance', value)

	@property
	def UpstreamEnableExtraIterations(self):
		"""If true, enables extra iterations upstream.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableExtraIterations')
	@UpstreamEnableExtraIterations.setter
	def UpstreamEnableExtraIterations(self, value):
		self._set_attribute('upstreamEnableExtraIterations', value)

	@property
	def UpstreamExtraIterationOffsets(self):
		"""Signifies extra iteration offsets upstream.

		Returns:
			str
		"""
		return self._get_attribute('upstreamExtraIterationOffsets')
	@UpstreamExtraIterationOffsets.setter
	def UpstreamExtraIterationOffsets(self, value):
		self._set_attribute('upstreamExtraIterationOffsets', value)

	@property
	def UpstreamImixAdd(self):
		"""Adds upstream IMIX

		Returns:
			str
		"""
		return self._get_attribute('upstreamImixAdd')
	@UpstreamImixAdd.setter
	def UpstreamImixAdd(self, value):
		self._set_attribute('upstreamImixAdd', value)

	@property
	def UpstreamImixData(self):
		"""Signifies upstream IMIX data

		Returns:
			str
		"""
		return self._get_attribute('upstreamImixData')
	@UpstreamImixData.setter
	def UpstreamImixData(self, value):
		self._set_attribute('upstreamImixData', value)

	@property
	def UpstreamImixDataQoS(self):
		"""If true, enables quality of service for upstream IMIX data

		Returns:
			bool
		"""
		return self._get_attribute('upstreamImixDataQoS')
	@UpstreamImixDataQoS.setter
	def UpstreamImixDataQoS(self, value):
		self._set_attribute('upstreamImixDataQoS', value)

	@property
	def UpstreamImixDelete(self):
		"""Deletes upstream IMIX data

		Returns:
			str
		"""
		return self._get_attribute('upstreamImixDelete')
	@UpstreamImixDelete.setter
	def UpstreamImixDelete(self, value):
		self._set_attribute('upstreamImixDelete', value)

	@property
	def UpstreamImixDistribution(self):
		"""Distributes upstream IMIX

		Returns:
			str(bwpercentage|weight)
		"""
		return self._get_attribute('upstreamImixDistribution')
	@UpstreamImixDistribution.setter
	def UpstreamImixDistribution(self, value):
		self._set_attribute('upstreamImixDistribution', value)

	@property
	def UpstreamImixEnabled(self):
		"""If true, enables upstream IMIX

		Returns:
			bool
		"""
		return self._get_attribute('upstreamImixEnabled')
	@UpstreamImixEnabled.setter
	def UpstreamImixEnabled(self, value):
		self._set_attribute('upstreamImixEnabled', value)

	@property
	def UpstreamImixTemplates(self):
		"""Signifies upstream IMIX templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('upstreamImixTemplates')
	@UpstreamImixTemplates.setter
	def UpstreamImixTemplates(self, value):
		self._set_attribute('upstreamImixTemplates', value)

	@property
	def UpstreamInitialBinaryLoadRate(self):
		"""Signifies the uptream initial binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('upstreamInitialBinaryLoadRate')
	@UpstreamInitialBinaryLoadRate.setter
	def UpstreamInitialBinaryLoadRate(self, value):
		self._set_attribute('upstreamInitialBinaryLoadRate', value)

	@property
	def UpstreamInitialStepLoadRate(self):
		"""This signifies upstream initial step load rate.

		Returns:
			number
		"""
		return self._get_attribute('upstreamInitialStepLoadRate')
	@UpstreamInitialStepLoadRate.setter
	def UpstreamInitialStepLoadRate(self, value):
		self._set_attribute('upstreamInitialStepLoadRate', value)

	@property
	def UpstreamLoadType(self):
		"""Signifies upstream load type.

		Returns:
			str(binary)
		"""
		return self._get_attribute('upstreamLoadType')
	@UpstreamLoadType.setter
	def UpstreamLoadType(self, value):
		self._set_attribute('upstreamLoadType', value)

	@property
	def UpstreamMaxBinaryLoadRate(self):
		"""Signifies upstream maximum binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('upstreamMaxBinaryLoadRate')
	@UpstreamMaxBinaryLoadRate.setter
	def UpstreamMaxBinaryLoadRate(self, value):
		self._set_attribute('upstreamMaxBinaryLoadRate', value)

	@property
	def UpstreamMaxStepLoadRate(self):
		"""Signifies upstream maximum step load rate.

		Returns:
			number
		"""
		return self._get_attribute('upstreamMaxStepLoadRate')
	@UpstreamMaxStepLoadRate.setter
	def UpstreamMaxStepLoadRate(self, value):
		self._set_attribute('upstreamMaxStepLoadRate', value)

	@property
	def UpstreamMinBinaryLoadRate(self):
		"""Signifies the upstream binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('upstreamMinBinaryLoadRate')
	@UpstreamMinBinaryLoadRate.setter
	def UpstreamMinBinaryLoadRate(self, value):
		self._set_attribute('upstreamMinBinaryLoadRate', value)

	@property
	def UpstreamStepFrameLossUnit(self):
		"""Signifies the upstream step frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('upstreamStepFrameLossUnit')
	@UpstreamStepFrameLossUnit.setter
	def UpstreamStepFrameLossUnit(self, value):
		self._set_attribute('upstreamStepFrameLossUnit', value)

	@property
	def UpstreamStepLoadUnit(self):
		"""Signifies upstream step load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('upstreamStepLoadUnit')
	@UpstreamStepLoadUnit.setter
	def UpstreamStepLoadUnit(self, value):
		self._set_attribute('upstreamStepLoadUnit', value)

	@property
	def UpstreamStepStepLoadRate(self):
		"""Signifies the upstream step load rate.

		Returns:
			str
		"""
		return self._get_attribute('upstreamStepStepLoadRate')
	@UpstreamStepStepLoadRate.setter
	def UpstreamStepStepLoadRate(self, value):
		self._set_attribute('upstreamStepStepLoadRate', value)

	@property
	def UpstreamStepTolerance(self):
		"""Signifies upstream step tolerance value.

		Returns:
			number
		"""
		return self._get_attribute('upstreamStepTolerance')
	@UpstreamStepTolerance.setter
	def UpstreamStepTolerance(self, value):
		self._set_attribute('upstreamStepTolerance', value)

	@property
	def UpstreamStopTestOnHighLoss(self):
		"""Signifies upstream stop test on high loss.

		Returns:
			number
		"""
		return self._get_attribute('upstreamStopTestOnHighLoss')
	@UpstreamStopTestOnHighLoss.setter
	def UpstreamStopTestOnHighLoss(self, value):
		self._set_attribute('upstreamStopTestOnHighLoss', value)

	@property
	def UpstreamUsePercentOffsets(self):
		"""Signifies upstream use percent offsets.

		Returns:
			str
		"""
		return self._get_attribute('upstreamUsePercentOffsets')
	@UpstreamUsePercentOffsets.setter
	def UpstreamUsePercentOffsets(self, value):
		self._set_attribute('upstreamUsePercentOffsets', value)

	def update(self, AggregateByDirection=None, AggregateByFlowgroup=None, AggregateByPort=None, BackoffIteration=None, BinaryAcceptableFrameLossLabel=None, BinaryBackoffLabel=None, BinaryInitialRateLabel=None, BinaryLoadUnitLabel=None, BinaryMaxRateLabel=None, BinaryMinRateLabel=None, BinaryResolutionLabel=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, DelayAfterTransmit=None, DownstreamBinaryBackoff=None, DownstreamBinaryFrameLossUnit=None, DownstreamBinaryLoadUnit=None, DownstreamBinaryResolution=None, DownstreamBinarySearchType=None, DownstreamBinaryTolerance=None, DownstreamImixAdd=None, DownstreamImixData=None, DownstreamImixDataQoS=None, DownstreamImixDelete=None, DownstreamImixDistribution=None, DownstreamImixEnabled=None, DownstreamImixTemplates=None, DownstreamInitialBinaryLoadRate=None, DownstreamInitialStepLoadRate=None, DownstreamLoadType=None, DownstreamMaxBinaryLoadRate=None, DownstreamMaxStepLoadRate=None, DownstreamMinBinaryLoadRate=None, DownstreamStepFrameLossUnit=None, DownstreamStepLoadUnit=None, DownstreamStepStepLoadRate=None, DownstreamStepTolerance=None, DownstreamStopTestOnHighLoss=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, ForceRegenerate=None, FramesPerBurstGap=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixTrafficType=None, IterationParameters=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadType=None, MapType=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, SaturationIteration=None, StaggeredStart=None, StepAcceptableFrameLossLabel=None, StepEndRateLabel=None, StepInitialRateLabel=None, StepLoadUnitLabel=None, StepStepRateLabel=None, SupportedTrafficTypes=None, TestType=None, TestTypeTemp=None, TestTypeTemp2=None, Tolerance=None, TrafficType=None, TxDelay=None, UpstreamBinaryBackoff=None, UpstreamBinaryFrameLossUnit=None, UpstreamBinaryLoadUnit=None, UpstreamBinaryResolution=None, UpstreamBinarySearchType=None, UpstreamBinaryTolerance=None, UpstreamEnableExtraIterations=None, UpstreamExtraIterationOffsets=None, UpstreamImixAdd=None, UpstreamImixData=None, UpstreamImixDataQoS=None, UpstreamImixDelete=None, UpstreamImixDistribution=None, UpstreamImixEnabled=None, UpstreamImixTemplates=None, UpstreamInitialBinaryLoadRate=None, UpstreamInitialStepLoadRate=None, UpstreamLoadType=None, UpstreamMaxBinaryLoadRate=None, UpstreamMaxStepLoadRate=None, UpstreamMinBinaryLoadRate=None, UpstreamStepFrameLossUnit=None, UpstreamStepLoadUnit=None, UpstreamStepStepLoadRate=None, UpstreamStepTolerance=None, UpstreamStopTestOnHighLoss=None, UpstreamUsePercentOffsets=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			AggregateByDirection (bool): NOT DEFINED
			AggregateByFlowgroup (bool): NOT DEFINED
			AggregateByPort (bool): NOT DEFINED
			BackoffIteration (number): Signifies the back of iteration.
			BinaryAcceptableFrameLossLabel (str): Signifies the binary value of acceptable frame loss label
			BinaryBackoffLabel (str): Signifies the binary backoff label
			BinaryInitialRateLabel (str): Signifies initial rate label
			BinaryLoadUnitLabel (str): Signifies the binary load unit label
			BinaryMaxRateLabel (str): Signifies the binary maximum rate label
			BinaryMinRateLabel (str): Signifies the binary minimum rte label
			BinaryResolutionLabel (str): Signifies the binary resolution label
			BurstSize (number): The number of packets to send in a burst.
			CalculateJitter (bool): If true, calculates jitter.
			CalculateLatency (bool): If true, calculates latency.
			DelayAfterTransmit (number): Signifies the delay time after transmit of the packet.
			DownstreamBinaryBackoff (number): Signifies the downstream binary backoff
			DownstreamBinaryFrameLossUnit (str(%|frames)): Signifies the downstream binary frame loss unit.
			DownstreamBinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies downstream binary load unit.
			DownstreamBinaryResolution (number): Signifies the downstream binary resolution.
			DownstreamBinarySearchType (str): This signifies the downstream binary search type.
			DownstreamBinaryTolerance (number): Signifies the downstream binary tolerance.
			DownstreamImixAdd (str): Adds downstream IMIX
			DownstreamImixData (str): Signifies the downstream IMIX data
			DownstreamImixDataQoS (bool): If true, enables the quality of service for downstream IMIX
			DownstreamImixDelete (str): Deletes downstream IMIX
			DownstreamImixDistribution (str(bwpercentage|weight)): signifies the downstream imix distribution.
			DownstreamImixEnabled (bool): If true, enables downstream IMIX
			DownstreamImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Signifies downstream IMIX templates.
			DownstreamInitialBinaryLoadRate (number): This signifies downstream initial binary load rate.
			DownstreamInitialStepLoadRate (number): This signifies downstream initial step load rate.
			DownstreamLoadType (str): Signifies downstream load type.
			DownstreamMaxBinaryLoadRate (number): Signifies maximum downstream binary load rate.
			DownstreamMaxStepLoadRate (number): Signifies downstream maximum step load rate.
			DownstreamMinBinaryLoadRate (number): Signifies minimum downstream binary load rate.
			DownstreamStepFrameLossUnit (str(%|frames)): Signifies downstream step frame loss unit.
			DownstreamStepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies downstream step load unit.
			DownstreamStepStepLoadRate (str): This signifies downstream step load rate.
			DownstreamStepTolerance (number): Signifies downstream step tolerance.
			DownstreamStopTestOnHighLoss (number): This stops the downstream test on high loss.
			Duration (number): Signifies the duration.
			EnableBackoffIteration (bool): If true, enables backoff iteration.
			EnableDataIntegrity (bool): If true, enables data integrity.
			EnableFastConvergence (bool): If true, enables fast convergence.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
			EnableStopTestOnHighLoss (bool): If true, enables stop test on high loss option.
			FastConvergenceDuration (number): Signifies fast convergence duration.
			FastConvergenceThreshold (number): Signifies the threshold for fast convergence.
			ForceRegenerate (bool): If true, enables force regenerate.
			FramesPerBurstGap (number): Signifies the frames sent per burst gap
			Gap (number): Signifies the burst gap
			GenerateTrackingOptionAggregationFiles (bool): If true, generates tracking option of aggregation files.
			ImixTrafficType (str): Signifies the type of IMIX traffic.
			IterationParameters (str): This signifies the Iteration Parameters.
			LatencyBins (str): Sets the latency bins statistics.
			LatencyBinsEnabled (bool): Enables the latency bins statistics.
			LatencyType (str(cutThrough|storeForward)): Signifies the latency type.
			LoadType (str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)): Signifies the load type.
			MapType (str): Signifies the map type.
			Numtrials (number): Signifies the numeric trials.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			ReportSequenceError (bool): If true, reports sequence error.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): Reports throughput rate unit.
			SaturationIteration (number): Signifies saturation iteration.
			StaggeredStart (bool): If true, staggers start.
			StepAcceptableFrameLossLabel (str): Signifies step acceptable frame loss label
			StepEndRateLabel (str): Signifies step end rate label
			StepInitialRateLabel (str): Signifies step initial rate label
			StepLoadUnitLabel (str): Signifies the step load unit label
			StepStepRateLabel (str): Signifies the step rate label
			SupportedTrafficTypes (str): Signifies the traffic types supported.
			TestType (str(downstreamOnly|upstreamDownstream|upstreamOnly)): Signifies th test type.
			TestTypeTemp (str(downstreamOnly|upstreamDownstream|upstreamOnly)): Signifies the temporary test type.
			TestTypeTemp2 (str(downstreamOnly|upstreamDownstream|upstreamOnly)): Signifies the second temporary test type.
			Tolerance (number): Signifies the tolerance.
			TrafficType (str(burstyLoading|constantLoading)): Signifies the traffic type.
			TxDelay (number): Signifies the delay time during the transmission of data
			UpstreamBinaryBackoff (number): Signifies upstream binary backoff
			UpstreamBinaryFrameLossUnit (str(%|frames)): Signifies the upstream binary frame loss unit.
			UpstreamBinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): This signifies the upstream binary load unit.
			UpstreamBinaryResolution (number): Signifies upstream binary resolution.
			UpstreamBinarySearchType (str): Signifies the upstream binary search type.
			UpstreamBinaryTolerance (number): Signifies the upstream binary tolerance.
			UpstreamEnableExtraIterations (bool): If true, enables extra iterations upstream.
			UpstreamExtraIterationOffsets (str): Signifies extra iteration offsets upstream.
			UpstreamImixAdd (str): Adds upstream IMIX
			UpstreamImixData (str): Signifies upstream IMIX data
			UpstreamImixDataQoS (bool): If true, enables quality of service for upstream IMIX data
			UpstreamImixDelete (str): Deletes upstream IMIX data
			UpstreamImixDistribution (str(bwpercentage|weight)): Distributes upstream IMIX
			UpstreamImixEnabled (bool): If true, enables upstream IMIX
			UpstreamImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Signifies upstream IMIX templates.
			UpstreamInitialBinaryLoadRate (number): Signifies the uptream initial binary load rate.
			UpstreamInitialStepLoadRate (number): This signifies upstream initial step load rate.
			UpstreamLoadType (str(binary)): Signifies upstream load type.
			UpstreamMaxBinaryLoadRate (number): Signifies upstream maximum binary load rate.
			UpstreamMaxStepLoadRate (number): Signifies upstream maximum step load rate.
			UpstreamMinBinaryLoadRate (number): Signifies the upstream binary load rate.
			UpstreamStepFrameLossUnit (str(%|frames)): Signifies the upstream step frame loss unit.
			UpstreamStepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies upstream step load unit.
			UpstreamStepStepLoadRate (str): Signifies the upstream step load rate.
			UpstreamStepTolerance (number): Signifies upstream step tolerance value.
			UpstreamStopTestOnHighLoss (number): Signifies upstream stop test on high loss.
			UpstreamUsePercentOffsets (str): Signifies upstream use percent offsets.

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
