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


class TestConfig(Base):
    """The test configuration parameters.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def AlgorithmType(self):
        """
        Returns
        -------
        - str(srvConfiguration | srvPerformance): The type of algorithm used.
        """
        return self._get_attribute('algorithmType')
    @AlgorithmType.setter
    def AlgorithmType(self, value):
        self._set_attribute('algorithmType', value)

    @property
    def CalculateJitter(self):
        """
        Returns
        -------
        - bool: Calculates the interval between timestamps of PGID packet arrivals.
        """
        return self._get_attribute('calculateJitter')
    @CalculateJitter.setter
    def CalculateJitter(self, value):
        self._set_attribute('calculateJitter', value)

    @property
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: Calculates and reports latency.
        """
        return self._get_attribute('calculateLatency')
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute('calculateLatency', value)

    @property
    def ContinuePassFailed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('continuePassFailed')
    @ContinuePassFailed.setter
    def ContinuePassFailed(self, value):
        self._set_attribute('continuePassFailed', value)

    @property
    def CurrentService(self):
        """
        Returns
        -------
        - str: The service in use currently.
        """
        return self._get_attribute('currentService')
    @CurrentService.setter
    def CurrentService(self, value):
        self._set_attribute('currentService', value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute('delayAfterTransmit')
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute('delayAfterTransmit', value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The duration of the test in hours, which is used to calculate the number of frames to transmit.
        """
        return self._get_attribute('duration')
    @Duration.setter
    def Duration(self, value):
        self._set_attribute('duration', value)

    @property
    def DurationLabel(self):
        """
        Returns
        -------
        - str: The label defining the traffic duration time.
        """
        return self._get_attribute('durationLabel')
    @DurationLabel.setter
    def DurationLabel(self, value):
        self._set_attribute('durationLabel', value)

    @property
    def EnableBurstTest(self):
        """
        Returns
        -------
        - bool: If true, enables burst test.
        """
        return self._get_attribute('enableBurstTest')
    @EnableBurstTest.setter
    def EnableBurstTest(self, value):
        self._set_attribute('enableBurstTest', value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: If true, enables data integrity test.
        """
        return self._get_attribute('enableDataIntegrity')
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        self._set_attribute('enableDataIntegrity', value)

    @property
    def EnableLatencyPassFailLabel(self):
        """
        Returns
        -------
        - str: The latency pass fail criteria is set.
        """
        return self._get_attribute('enableLatencyPassFailLabel')
    @EnableLatencyPassFailLabel.setter
    def EnableLatencyPassFailLabel(self, value):
        self._set_attribute('enableLatencyPassFailLabel', value)

    @property
    def EnableLayer1Rate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableLayer1Rate')
    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        self._set_attribute('enableLayer1Rate', value)

    @property
    def EnableStandardDeviationPassFailLabel(self):
        """
        Returns
        -------
        - str: Standard Deviation for the Pass/Fail criteria is set.
        """
        return self._get_attribute('enableStandardDeviationPassFailLabel')
    @EnableStandardDeviationPassFailLabel.setter
    def EnableStandardDeviationPassFailLabel(self, value):
        self._set_attribute('enableStandardDeviationPassFailLabel', value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute('forceRegenerate')
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute('forceRegenerate', value)

    @property
    def FrameDataDetailedResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('frameDataDetailedResults')
    @FrameDataDetailedResults.setter
    def FrameDataDetailedResults(self, value):
        self._set_attribute('frameDataDetailedResults', value)

    @property
    def FrameLossFramesMode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('frameLossFramesMode')
    @FrameLossFramesMode.setter
    def FrameLossFramesMode(self, value):
        self._set_attribute('frameLossFramesMode', value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute('frameSizeMode')
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute('frameSizeMode', value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: The gap in transmission of frames.
        """
        return self._get_attribute('gap')
    @Gap.setter
    def Gap(self, value):
        self._set_attribute('gap', value)

    @property
    def GenerateTrackingOptionAggregationFiles(self):
        """
        Returns
        -------
        - bool: If true, enables the tracking option in aggregation files.
        """
        return self._get_attribute('generateTrackingOptionAggregationFiles')
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        self._set_attribute('generateTrackingOptionAggregationFiles', value)

    @property
    def IsColorAware(self):
        """
        Returns
        -------
        - bool: If true, it becomes aware of the color.
        """
        return self._get_attribute('isColorAware')
    @IsColorAware.setter
    def IsColorAware(self, value):
        self._set_attribute('isColorAware', value)

    @property
    def IsServicePeformanceMode(self):
        """
        Returns
        -------
        - str: The service performance mode.
        """
        return self._get_attribute('isServicePeformanceMode')
    @IsServicePeformanceMode.setter
    def IsServicePeformanceMode(self, value):
        self._set_attribute('isServicePeformanceMode', value)

    @property
    def IterationInitialRate(self):
        """
        Returns
        -------
        - str: The initial rate of iteration.
        """
        return self._get_attribute('iterationInitialRate')
    @IterationInitialRate.setter
    def IterationInitialRate(self, value):
        self._set_attribute('iterationInitialRate', value)

    @property
    def IterationStep(self):
        """
        Returns
        -------
        - str: The iteration step.
        """
        return self._get_attribute('iterationStep')
    @IterationStep.setter
    def IterationStep(self, value):
        self._set_attribute('iterationStep', value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics.
        """
        return self._get_attribute('latencyBins')
    @LatencyBins.setter
    def LatencyBins(self, value):
        self._set_attribute('latencyBins', value)

    @property
    def LatencyBinsEnabled(self):
        """
        Returns
        -------
        - bool: Enables the latency bins statistics.
        """
        return self._get_attribute('latencyBinsEnabled')
    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        self._set_attribute('latencyBinsEnabled', value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | mef | storeForward): The type of latency.
        """
        return self._get_attribute('latencyType')
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute('latencyType', value)

    @property
    def LearnSnoopConfig(self):
        """
        Returns
        -------
        - bool: The learned snoop configuration.
        """
        return self._get_attribute('learnSnoopConfig')
    @LearnSnoopConfig.setter
    def LearnSnoopConfig(self, value):
        self._set_attribute('learnSnoopConfig', value)

    @property
    def NoOfFrames(self):
        """
        Returns
        -------
        - str: The number of frames sent.
        """
        return self._get_attribute('noOfFrames')
    @NoOfFrames.setter
    def NoOfFrames(self, value):
        self._set_attribute('noOfFrames', value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: This signifies the Number of trials.
        """
        return self._get_attribute('numtrials')
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute('numtrials', value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('portDelayEnabled')
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute('portDelayEnabled', value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute('portDelayUnit')
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute('portDelayUnit', value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value.
        """
        return self._get_attribute('portDelayValue')
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute('portDelayValue', value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute('protocolItem')
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute('protocolItem', value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: If true, the sequence error, if found, is reported.
        """
        return self._get_attribute('reportSequenceError')
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        self._set_attribute('reportSequenceError', value)

    @property
    def ReportTputRateUnit(self):
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The unit of rate for throughput.
        """
        return self._get_attribute('reportTputRateUnit')
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute('reportTputRateUnit', value)

    @property
    def Rfc2889ordering(self):
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): NOT DEFINED
        """
        return self._get_attribute('rfc2889ordering')
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        self._set_attribute('rfc2889ordering', value)

    @property
    def ServiceIterations(self):
        """
        Returns
        -------
        - str: Number of service iterations.
        """
        return self._get_attribute('serviceIterations')
    @ServiceIterations.setter
    def ServiceIterations(self, value):
        self._set_attribute('serviceIterations', value)

    @property
    def ServicesList(self):
        """
        Returns
        -------
        - str: The list of service.
        """
        return self._get_attribute('servicesList')
    @ServicesList.setter
    def ServicesList(self, value):
        self._set_attribute('servicesList', value)

    @property
    def SkipDefaultPassFailEvaluation(self):
        """
        Returns
        -------
        - bool: If true, it skips the default pass fail evaluation.
        """
        return self._get_attribute('skipDefaultPassFailEvaluation')
    @SkipDefaultPassFailEvaluation.setter
    def SkipDefaultPassFailEvaluation(self, value):
        self._set_attribute('skipDefaultPassFailEvaluation', value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: Staggered start of traffic.
        """
        return self._get_attribute('staggeredStart')
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute('staggeredStart', value)

    @property
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: It gives the test traffic type.
        """
        return self._get_attribute('testTrafficType')
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute('testTrafficType', value)

    @property
    def TransmitMode(self):
        """
        Returns
        -------
        - str(noFrames | useDuration): The transmit mode for this traffic item.
        """
        return self._get_attribute('transmitMode')
    @TransmitMode.setter
    def TransmitMode(self, value):
        self._set_attribute('transmitMode', value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: The minimum delay between successive packets.
        """
        return self._get_attribute('txDelay')
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute('txDelay', value)

    def update(self, AlgorithmType=None, CalculateJitter=None, CalculateLatency=None, ContinuePassFailed=None, CurrentService=None, DelayAfterTransmit=None, Duration=None, DurationLabel=None, EnableBurstTest=None, EnableDataIntegrity=None, EnableLatencyPassFailLabel=None, EnableLayer1Rate=None, EnableStandardDeviationPassFailLabel=None, ForceRegenerate=None, FrameDataDetailedResults=None, FrameLossFramesMode=None, FrameSizeMode=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, IsColorAware=None, IsServicePeformanceMode=None, IterationInitialRate=None, IterationStep=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LearnSnoopConfig=None, NoOfFrames=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Rfc2889ordering=None, ServiceIterations=None, ServicesList=None, SkipDefaultPassFailEvaluation=None, StaggeredStart=None, TestTrafficType=None, TransmitMode=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - AlgorithmType (str(srvConfiguration | srvPerformance)): The type of algorithm used.
        - CalculateJitter (bool): Calculates the interval between timestamps of PGID packet arrivals.
        - CalculateLatency (bool): Calculates and reports latency.
        - ContinuePassFailed (bool): NOT DEFINED
        - CurrentService (str): The service in use currently.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - DurationLabel (str): The label defining the traffic duration time.
        - EnableBurstTest (bool): If true, enables burst test.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableLatencyPassFailLabel (str): The latency pass fail criteria is set.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableStandardDeviationPassFailLabel (str): Standard Deviation for the Pass/Fail criteria is set.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameDataDetailedResults (bool): NOT DEFINED
        - FrameLossFramesMode (str): NOT DEFINED
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsServicePeformanceMode (str): The service performance mode.
        - IterationInitialRate (str): The initial rate of iteration.
        - IterationStep (str): The iteration step.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | mef | storeForward)): The type of latency.
        - LearnSnoopConfig (bool): The learned snoop configuration.
        - NoOfFrames (str): The number of frames sent.
        - Numtrials (number): This signifies the Number of trials.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ReportSequenceError (bool): If true, the sequence error, if found, is reported.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): NOT DEFINED
        - ServiceIterations (str): Number of service iterations.
        - ServicesList (str): The list of service.
        - SkipDefaultPassFailEvaluation (bool): If true, it skips the default pass fail evaluation.
        - StaggeredStart (bool): Staggered start of traffic.
        - TestTrafficType (str): It gives the test traffic type.
        - TransmitMode (str(noFrames | useDuration)): The transmit mode for this traffic item.
        - TxDelay (number): The minimum delay between successive packets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
