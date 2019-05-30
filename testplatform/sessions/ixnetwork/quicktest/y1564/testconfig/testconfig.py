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
	def AlgorithmType(self):
		"""The type of algorithm used.

		Returns:
			str(srvConfiguration|srvPerformance)
		"""
		return self._get_attribute('algorithmType')
	@AlgorithmType.setter
	def AlgorithmType(self, value):
		self._set_attribute('algorithmType', value)

	@property
	def CalculateJitter(self):
		"""Calculates the interval between timestamps of PGID packet arrivals.

		Returns:
			bool
		"""
		return self._get_attribute('calculateJitter')
	@CalculateJitter.setter
	def CalculateJitter(self, value):
		self._set_attribute('calculateJitter', value)

	@property
	def CalculateLatency(self):
		"""Calculates and reports latency.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def ContinuePassFailed(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('continuePassFailed')
	@ContinuePassFailed.setter
	def ContinuePassFailed(self, value):
		self._set_attribute('continuePassFailed', value)

	@property
	def CurrentService(self):
		"""The service in use currently.

		Returns:
			str
		"""
		return self._get_attribute('currentService')
	@CurrentService.setter
	def CurrentService(self, value):
		self._set_attribute('currentService', value)

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
	def DurationLabel(self):
		"""The label defining the traffic duration time.

		Returns:
			str
		"""
		return self._get_attribute('durationLabel')
	@DurationLabel.setter
	def DurationLabel(self, value):
		self._set_attribute('durationLabel', value)

	@property
	def EnableBurstTest(self):
		"""If true, enables burst test.

		Returns:
			bool
		"""
		return self._get_attribute('enableBurstTest')
	@EnableBurstTest.setter
	def EnableBurstTest(self, value):
		self._set_attribute('enableBurstTest', value)

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
	def EnableLatencyPassFailLabel(self):
		"""The latency pass fail criteria is set.

		Returns:
			str
		"""
		return self._get_attribute('enableLatencyPassFailLabel')
	@EnableLatencyPassFailLabel.setter
	def EnableLatencyPassFailLabel(self, value):
		self._set_attribute('enableLatencyPassFailLabel', value)

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
	def EnableStandardDeviationPassFailLabel(self):
		"""Standard Deviation for the Pass/Fail criteria is set.

		Returns:
			str
		"""
		return self._get_attribute('enableStandardDeviationPassFailLabel')
	@EnableStandardDeviationPassFailLabel.setter
	def EnableStandardDeviationPassFailLabel(self, value):
		self._set_attribute('enableStandardDeviationPassFailLabel', value)

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
	def FrameDataDetailedResults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('frameDataDetailedResults')
	@FrameDataDetailedResults.setter
	def FrameDataDetailedResults(self, value):
		self._set_attribute('frameDataDetailedResults', value)

	@property
	def FrameLossFramesMode(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('frameLossFramesMode')
	@FrameLossFramesMode.setter
	def FrameLossFramesMode(self, value):
		self._set_attribute('frameLossFramesMode', value)

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
	def IsColorAware(self):
		"""If true, it becomes aware of the color.

		Returns:
			bool
		"""
		return self._get_attribute('isColorAware')
	@IsColorAware.setter
	def IsColorAware(self, value):
		self._set_attribute('isColorAware', value)

	@property
	def IsServicePeformanceMode(self):
		"""The service performance mode.

		Returns:
			str
		"""
		return self._get_attribute('isServicePeformanceMode')
	@IsServicePeformanceMode.setter
	def IsServicePeformanceMode(self, value):
		self._set_attribute('isServicePeformanceMode', value)

	@property
	def IterationInitialRate(self):
		"""The initial rate of iteration.

		Returns:
			str
		"""
		return self._get_attribute('iterationInitialRate')
	@IterationInitialRate.setter
	def IterationInitialRate(self, value):
		self._set_attribute('iterationInitialRate', value)

	@property
	def IterationStep(self):
		"""The iteration step.

		Returns:
			str
		"""
		return self._get_attribute('iterationStep')
	@IterationStep.setter
	def IterationStep(self, value):
		self._set_attribute('iterationStep', value)

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
			str(cutThrough|mef|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LearnSnoopConfig(self):
		"""The learned snoop configuration.

		Returns:
			bool
		"""
		return self._get_attribute('learnSnoopConfig')
	@LearnSnoopConfig.setter
	def LearnSnoopConfig(self, value):
		self._set_attribute('learnSnoopConfig', value)

	@property
	def NoOfFrames(self):
		"""The number of frames sent.

		Returns:
			str
		"""
		return self._get_attribute('noOfFrames')
	@NoOfFrames.setter
	def NoOfFrames(self, value):
		self._set_attribute('noOfFrames', value)

	@property
	def Numtrials(self):
		"""This signifies the Number of trials.

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
		"""The unit of rate for throughput.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Rfc2889ordering(self):
		"""NOT DEFINED

		Returns:
			str(noOrdering|unchanged|val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def ServiceIterations(self):
		"""Number of service iterations.

		Returns:
			str
		"""
		return self._get_attribute('serviceIterations')
	@ServiceIterations.setter
	def ServiceIterations(self, value):
		self._set_attribute('serviceIterations', value)

	@property
	def ServicesList(self):
		"""The list of service.

		Returns:
			str
		"""
		return self._get_attribute('servicesList')
	@ServicesList.setter
	def ServicesList(self, value):
		self._set_attribute('servicesList', value)

	@property
	def SkipDefaultPassFailEvaluation(self):
		"""If true, it skips the default pass fail evaluation.

		Returns:
			bool
		"""
		return self._get_attribute('skipDefaultPassFailEvaluation')
	@SkipDefaultPassFailEvaluation.setter
	def SkipDefaultPassFailEvaluation(self, value):
		self._set_attribute('skipDefaultPassFailEvaluation', value)

	@property
	def StaggeredStart(self):
		"""Staggered start of traffic.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def TestTrafficType(self):
		"""It gives the test traffic type.

		Returns:
			str
		"""
		return self._get_attribute('testTrafficType')
	@TestTrafficType.setter
	def TestTrafficType(self, value):
		self._set_attribute('testTrafficType', value)

	@property
	def TransmitMode(self):
		"""The transmit mode for this traffic item.

		Returns:
			str(noFrames|useDuration)
		"""
		return self._get_attribute('transmitMode')
	@TransmitMode.setter
	def TransmitMode(self, value):
		self._set_attribute('transmitMode', value)

	@property
	def TxDelay(self):
		"""The minimum delay between successive packets.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	def update(self, AlgorithmType=None, CalculateJitter=None, CalculateLatency=None, ContinuePassFailed=None, CurrentService=None, DelayAfterTransmit=None, Duration=None, DurationLabel=None, EnableBurstTest=None, EnableDataIntegrity=None, EnableLatencyPassFailLabel=None, EnableLayer1Rate=None, EnableStandardDeviationPassFailLabel=None, ForceRegenerate=None, FrameDataDetailedResults=None, FrameLossFramesMode=None, FrameSizeMode=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, IsColorAware=None, IsServicePeformanceMode=None, IterationInitialRate=None, IterationStep=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LearnSnoopConfig=None, NoOfFrames=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Rfc2889ordering=None, ServiceIterations=None, ServicesList=None, SkipDefaultPassFailEvaluation=None, StaggeredStart=None, TestTrafficType=None, TransmitMode=None, TxDelay=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			AlgorithmType (str(srvConfiguration|srvPerformance)): The type of algorithm used.
			CalculateJitter (bool): Calculates the interval between timestamps of PGID packet arrivals.
			CalculateLatency (bool): Calculates and reports latency.
			ContinuePassFailed (bool): NOT DEFINED
			CurrentService (str): The service in use currently.
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
			Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
			DurationLabel (str): The label defining the traffic duration time.
			EnableBurstTest (bool): If true, enables burst test.
			EnableDataIntegrity (bool): If true, enables data integrity test.
			EnableLatencyPassFailLabel (str): The latency pass fail criteria is set.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableStandardDeviationPassFailLabel (str): Standard Deviation for the Pass/Fail criteria is set.
			ForceRegenerate (bool): Initiates a forced regeneration.
			FrameDataDetailedResults (bool): NOT DEFINED
			FrameLossFramesMode (str): NOT DEFINED
			FrameSizeMode (str(custom|customlist|increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			Gap (number): The gap in transmission of frames.
			GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
			IsColorAware (bool): If true, it becomes aware of the color.
			IsServicePeformanceMode (str): The service performance mode.
			IterationInitialRate (str): The initial rate of iteration.
			IterationStep (str): The iteration step.
			LatencyBins (str): Sets the latency bins statistics.
			LatencyBinsEnabled (bool): Enables the latency bins statistics.
			LatencyType (str(cutThrough|mef|storeForward)): The type of latency.
			LearnSnoopConfig (bool): The learned snoop configuration.
			NoOfFrames (str): The number of frames sent.
			Numtrials (number): This signifies the Number of trials.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			ReportSequenceError (bool): If true, the sequence error, if found, is reported.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The unit of rate for throughput.
			Rfc2889ordering (str(noOrdering|unchanged|val2889Ordering)): NOT DEFINED
			ServiceIterations (str): Number of service iterations.
			ServicesList (str): The list of service.
			SkipDefaultPassFailEvaluation (bool): If true, it skips the default pass fail evaluation.
			StaggeredStart (bool): Staggered start of traffic.
			TestTrafficType (str): It gives the test traffic type.
			TransmitMode (str(noFrames|useDuration)): The transmit mode for this traffic item.
			TxDelay (number): The minimum delay between successive packets.

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
