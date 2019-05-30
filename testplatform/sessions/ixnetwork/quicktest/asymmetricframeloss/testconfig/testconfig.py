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
		"""If true, calibrates the latency.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

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
	def DownstreamGrain(self):
		"""The type downstream grain.

		Returns:
			str(coarse|fine)
		"""
		return self._get_attribute('downstreamGrain')
	@DownstreamGrain.setter
	def DownstreamGrain(self, value):
		self._set_attribute('downstreamGrain', value)

	@property
	def DownstreamImixAdd(self):
		"""Adds the IMIX for downstream.

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
		"""Signifies the quality of service for downstream IMIX data

		Returns:
			bool
		"""
		return self._get_attribute('downstreamImixDataQoS')
	@DownstreamImixDataQoS.setter
	def DownstreamImixDataQoS(self, value):
		self._set_attribute('downstreamImixDataQoS', value)

	@property
	def DownstreamImixDelete(self):
		"""Deletes the downstream IMIX value

		Returns:
			str
		"""
		return self._get_attribute('downstreamImixDelete')
	@DownstreamImixDelete.setter
	def DownstreamImixDelete(self, value):
		self._set_attribute('downstreamImixDelete', value)

	@property
	def DownstreamImixDistribution(self):
		"""It gives details about the down stream Imix distribution.

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
		"""Signifies the downstream IMIX templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('downstreamImixTemplates')
	@DownstreamImixTemplates.setter
	def DownstreamImixTemplates(self, value):
		self._set_attribute('downstreamImixTemplates', value)

	@property
	def DownstreamInitialStepLoadRate(self):
		"""Signifies downstream initial step load rate

		Returns:
			number
		"""
		return self._get_attribute('downstreamInitialStepLoadRate')
	@DownstreamInitialStepLoadRate.setter
	def DownstreamInitialStepLoadRate(self, value):
		self._set_attribute('downstreamInitialStepLoadRate', value)

	@property
	def DownstreamLoadType(self):
		"""Signifies downstream load type

		Returns:
			str(step)
		"""
		return self._get_attribute('downstreamLoadType')
	@DownstreamLoadType.setter
	def DownstreamLoadType(self, value):
		self._set_attribute('downstreamLoadType', value)

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
		"""Signifies downstream step load rate

		Returns:
			str
		"""
		return self._get_attribute('downstreamStepStepLoadRate')
	@DownstreamStepStepLoadRate.setter
	def DownstreamStepStepLoadRate(self, value):
		self._set_attribute('downstreamStepStepLoadRate', value)

	@property
	def DownstreamStepTolerance(self):
		"""Signifies downstream step tolerance

		Returns:
			number
		"""
		return self._get_attribute('downstreamStepTolerance')
	@DownstreamStepTolerance.setter
	def DownstreamStepTolerance(self, value):
		self._set_attribute('downstreamStepTolerance', value)

	@property
	def Duration(self):
		"""The duration of the test in hours, minutes, or seconds, which is used to calculate.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableDataIntegrity(self):
		"""Allows to do a data integrity check.

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
		"""If true, allows to set minimum frame size.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

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
	def FramesPerBurstGap(self):
		"""Specifies the per burst gap.

		Returns:
			number
		"""
		return self._get_attribute('framesPerBurstGap')
	@FramesPerBurstGap.setter
	def FramesPerBurstGap(self, value):
		self._set_attribute('framesPerBurstGap', value)

	@property
	def Gap(self):
		"""The inter burst gap.

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""Generates tracking option on aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def GranularityLabel(self):
		"""Signifies the granulity label

		Returns:
			str
		"""
		return self._get_attribute('granularityLabel')
	@GranularityLabel.setter
	def GranularityLabel(self, value):
		self._set_attribute('granularityLabel', value)

	@property
	def ImixTrafficType(self):
		"""Signifies the traffic type for IMIX

		Returns:
			str
		"""
		return self._get_attribute('imixTrafficType')
	@ImixTrafficType.setter
	def ImixTrafficType(self, value):
		self._set_attribute('imixTrafficType', value)

	@property
	def InitialRateLabel(self):
		"""Signifies the initial rate label

		Returns:
			str
		"""
		return self._get_attribute('initialRateLabel')
	@InitialRateLabel.setter
	def InitialRateLabel(self, value):
		self._set_attribute('initialRateLabel', value)

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
		"""The latency type, either Cut Through or Store and Forward.

		Returns:
			str(cutThrough|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadType(self):
		"""The latency type, either Cut Through or Store and Forward.

		Returns:
			str(step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def LoadUnitLabel(self):
		"""Signifies the load unit label

		Returns:
			str
		"""
		return self._get_attribute('loadUnitLabel')
	@LoadUnitLabel.setter
	def LoadUnitLabel(self, value):
		self._set_attribute('loadUnitLabel', value)

	@property
	def MapType(self):
		"""The map type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def NumFrames(self):
		"""Number of frames.

		Returns:
			number
		"""
		return self._get_attribute('numFrames')
	@NumFrames.setter
	def NumFrames(self, value):
		self._set_attribute('numFrames', value)

	@property
	def Numtrials(self):
		"""Number of trials.

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
		"""Sets the port delay value

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
		"""Specifies to include the types of sequence errors in the results, such as Small.

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
	def Runmode(self):
		"""The running mode.

		Returns:
			str(duration|noframes)
		"""
		return self._get_attribute('runmode')
	@Runmode.setter
	def Runmode(self, value):
		self._set_attribute('runmode', value)

	@property
	def StaggeredStart(self):
		"""Enable a staggered start to traffic transmit.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def SupportedTrafficTypes(self):
		"""The supported traffic types.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def TestType(self):
		"""Signifies the test type

		Returns:
			str(downstreamOnly|upstreamDownstream|upstreamOnly)
		"""
		return self._get_attribute('testType')
	@TestType.setter
	def TestType(self, value):
		self._set_attribute('testType', value)

	@property
	def TestTypeTemp(self):
		"""Signifies the temporary test type

		Returns:
			str(downstreamOnly|upstreamDownstream|upstreamOnly)
		"""
		return self._get_attribute('testTypeTemp')
	@TestTypeTemp.setter
	def TestTypeTemp(self, value):
		self._set_attribute('testTypeTemp', value)

	@property
	def TestTypeTemp2(self):
		"""Signifies the second termorary version of test type

		Returns:
			str(downstreamOnly|upstreamDownstream|upstreamOnly)
		"""
		return self._get_attribute('testTypeTemp2')
	@TestTypeTemp2.setter
	def TestTypeTemp2(self, value):
		self._set_attribute('testTypeTemp2', value)

	@property
	def TrafficType(self):
		"""The type of traffic to be transmitted.

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""The delay in transmission.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UpstreamGrain(self):
		"""The upstream traffic grain type.

		Returns:
			str(coarse|fine)
		"""
		return self._get_attribute('upstreamGrain')
	@UpstreamGrain.setter
	def UpstreamGrain(self, value):
		self._set_attribute('upstreamGrain', value)

	@property
	def UpstreamImixAdd(self):
		"""Adds IMIX upstream.

		Returns:
			str
		"""
		return self._get_attribute('upstreamImixAdd')
	@UpstreamImixAdd.setter
	def UpstreamImixAdd(self, value):
		self._set_attribute('upstreamImixAdd', value)

	@property
	def UpstreamImixData(self):
		"""Signifies the data of upstream IMIX

		Returns:
			str
		"""
		return self._get_attribute('upstreamImixData')
	@UpstreamImixData.setter
	def UpstreamImixData(self, value):
		self._set_attribute('upstreamImixData', value)

	@property
	def UpstreamImixDataQoS(self):
		"""Signifies the quality of service for upstream IMIX data

		Returns:
			bool
		"""
		return self._get_attribute('upstreamImixDataQoS')
	@UpstreamImixDataQoS.setter
	def UpstreamImixDataQoS(self, value):
		self._set_attribute('upstreamImixDataQoS', value)

	@property
	def UpstreamImixDelete(self):
		"""Deletes upstream IMIX

		Returns:
			str
		"""
		return self._get_attribute('upstreamImixDelete')
	@UpstreamImixDelete.setter
	def UpstreamImixDelete(self, value):
		self._set_attribute('upstreamImixDelete', value)

	@property
	def UpstreamImixDistribution(self):
		"""Signifies the distribution of upstream IMIX

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
		"""Signifies the upstream IMIX templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('upstreamImixTemplates')
	@UpstreamImixTemplates.setter
	def UpstreamImixTemplates(self, value):
		self._set_attribute('upstreamImixTemplates', value)

	@property
	def UpstreamInitialStepLoadRate(self):
		"""Signifies upstream initial step load rate

		Returns:
			number
		"""
		return self._get_attribute('upstreamInitialStepLoadRate')
	@UpstreamInitialStepLoadRate.setter
	def UpstreamInitialStepLoadRate(self, value):
		self._set_attribute('upstreamInitialStepLoadRate', value)

	@property
	def UpstreamLoadType(self):
		"""Signifies upstream load type

		Returns:
			str(step)
		"""
		return self._get_attribute('upstreamLoadType')
	@UpstreamLoadType.setter
	def UpstreamLoadType(self, value):
		self._set_attribute('upstreamLoadType', value)

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
		"""Signifies the upstream step load rate

		Returns:
			str
		"""
		return self._get_attribute('upstreamStepStepLoadRate')
	@UpstreamStepStepLoadRate.setter
	def UpstreamStepStepLoadRate(self, value):
		self._set_attribute('upstreamStepStepLoadRate', value)

	@property
	def UpstreamStepTolerance(self):
		"""Signifies upstream step tolerance value

		Returns:
			number
		"""
		return self._get_attribute('upstreamStepTolerance')
	@UpstreamStepTolerance.setter
	def UpstreamStepTolerance(self, value):
		self._set_attribute('upstreamStepTolerance', value)

	def update(self, BurstSize=None, CalculateJitter=None, CalculateLatency=None, DelayAfterTransmit=None, DownstreamGrain=None, DownstreamImixAdd=None, DownstreamImixData=None, DownstreamImixDataQoS=None, DownstreamImixDelete=None, DownstreamImixDistribution=None, DownstreamImixEnabled=None, DownstreamImixTemplates=None, DownstreamInitialStepLoadRate=None, DownstreamLoadType=None, DownstreamStepLoadUnit=None, DownstreamStepStepLoadRate=None, DownstreamStepTolerance=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableMinFrameSize=None, ForceRegenerate=None, FramesPerBurstGap=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, GranularityLabel=None, ImixTrafficType=None, InitialRateLabel=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadType=None, LoadUnitLabel=None, MapType=None, NumFrames=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Runmode=None, StaggeredStart=None, SupportedTrafficTypes=None, TestType=None, TestTypeTemp=None, TestTypeTemp2=None, TrafficType=None, TxDelay=None, UpstreamGrain=None, UpstreamImixAdd=None, UpstreamImixData=None, UpstreamImixDataQoS=None, UpstreamImixDelete=None, UpstreamImixDistribution=None, UpstreamImixEnabled=None, UpstreamImixTemplates=None, UpstreamInitialStepLoadRate=None, UpstreamLoadType=None, UpstreamStepLoadUnit=None, UpstreamStepStepLoadRate=None, UpstreamStepTolerance=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BurstSize (number): The number of packets to send in a burst.
			CalculateJitter (bool): If true, calculates jitter.
			CalculateLatency (bool): If true, calibrates the latency.
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
			DownstreamGrain (str(coarse|fine)): The type downstream grain.
			DownstreamImixAdd (str): Adds the IMIX for downstream.
			DownstreamImixData (str): Signifies the downstream IMIX data
			DownstreamImixDataQoS (bool): Signifies the quality of service for downstream IMIX data
			DownstreamImixDelete (str): Deletes the downstream IMIX value
			DownstreamImixDistribution (str(bwpercentage|weight)): It gives details about the down stream Imix distribution.
			DownstreamImixEnabled (bool): If true, enables downstream IMIX
			DownstreamImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Signifies the downstream IMIX templates.
			DownstreamInitialStepLoadRate (number): Signifies downstream initial step load rate
			DownstreamLoadType (str(step)): Signifies downstream load type
			DownstreamStepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies downstream step load unit.
			DownstreamStepStepLoadRate (str): Signifies downstream step load rate
			DownstreamStepTolerance (number): Signifies downstream step tolerance
			Duration (number): The duration of the test in hours, minutes, or seconds, which is used to calculate.
			EnableDataIntegrity (bool): Allows to do a data integrity check.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): If true, allows to set minimum frame size.
			ForceRegenerate (bool): Initiates a forced regeneration.
			FramesPerBurstGap (number): Specifies the per burst gap.
			Gap (number): The inter burst gap.
			GenerateTrackingOptionAggregationFiles (bool): Generates tracking option on aggregation files.
			GranularityLabel (str): Signifies the granulity label
			ImixTrafficType (str): Signifies the traffic type for IMIX
			InitialRateLabel (str): Signifies the initial rate label
			LatencyBins (str): Sets the latency bins statistics.
			LatencyBinsEnabled (bool): Enables the latency bins statistics.
			LatencyType (str(cutThrough|storeForward)): The latency type, either Cut Through or Store and Forward.
			LoadType (str(step)): The latency type, either Cut Through or Store and Forward.
			LoadUnitLabel (str): Signifies the load unit label
			MapType (str): The map type.
			NumFrames (number): Number of frames.
			Numtrials (number): Number of trials.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			ReportSequenceError (bool): Specifies to include the types of sequence errors in the results, such as Small.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The throughput rate unit.
			Runmode (str(duration|noframes)): The running mode.
			StaggeredStart (bool): Enable a staggered start to traffic transmit.
			SupportedTrafficTypes (str): The supported traffic types.
			TestType (str(downstreamOnly|upstreamDownstream|upstreamOnly)): Signifies the test type
			TestTypeTemp (str(downstreamOnly|upstreamDownstream|upstreamOnly)): Signifies the temporary test type
			TestTypeTemp2 (str(downstreamOnly|upstreamDownstream|upstreamOnly)): Signifies the second termorary version of test type
			TrafficType (str(burstyLoading|constantLoading)): The type of traffic to be transmitted.
			TxDelay (number): The delay in transmission.
			UpstreamGrain (str(coarse|fine)): The upstream traffic grain type.
			UpstreamImixAdd (str): Adds IMIX upstream.
			UpstreamImixData (str): Signifies the data of upstream IMIX
			UpstreamImixDataQoS (bool): Signifies the quality of service for upstream IMIX data
			UpstreamImixDelete (str): Deletes upstream IMIX
			UpstreamImixDistribution (str(bwpercentage|weight)): Signifies the distribution of upstream IMIX
			UpstreamImixEnabled (bool): If true, enables upstream IMIX
			UpstreamImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Signifies the upstream IMIX templates.
			UpstreamInitialStepLoadRate (number): Signifies upstream initial step load rate
			UpstreamLoadType (str(step)): Signifies upstream load type
			UpstreamStepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Signifies upstream step load unit.
			UpstreamStepStepLoadRate (str): Signifies the upstream step load rate
			UpstreamStepTolerance (number): Signifies upstream step tolerance value

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
