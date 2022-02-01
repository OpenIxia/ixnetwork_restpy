# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class TestConfig(Base):
    """The test configuration parameters.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'AlgorithmType': 'algorithmType',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'ContinuePassFailed': 'continuePassFailed',
        'CurrentService': 'currentService',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'Duration': 'duration',
        'DurationLabel': 'durationLabel',
        'EnableBurstTest': 'enableBurstTest',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableLatencyPassFailLabel': 'enableLatencyPassFailLabel',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableStandardDeviationPassFailLabel': 'enableStandardDeviationPassFailLabel',
        'ForceRegenerate': 'forceRegenerate',
        'FrameDataDetailedResults': 'frameDataDetailedResults',
        'FrameLossFramesMode': 'frameLossFramesMode',
        'FrameSizeMode': 'frameSizeMode',
        'Gap': 'gap',
        'GenerateTrackingOptionAggregationFiles': 'generateTrackingOptionAggregationFiles',
        'IsColorAware': 'isColorAware',
        'IsServicePeformanceMode': 'isServicePeformanceMode',
        'IterationInitialRate': 'iterationInitialRate',
        'IterationStep': 'iterationStep',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LearnSnoopConfig': 'learnSnoopConfig',
        'NoOfFrames': 'noOfFrames',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'Rfc2889ordering': 'rfc2889ordering',
        'ServiceIterations': 'serviceIterations',
        'ServicesList': 'servicesList',
        'SkipDefaultPassFailEvaluation': 'skipDefaultPassFailEvaluation',
        'StaggeredStart': 'staggeredStart',
        'TestTrafficType': 'testTrafficType',
        'TransmitMode': 'transmitMode',
        'TxDelay': 'txDelay',
    }
    _SDM_ENUM_MAP = {
        'algorithmType': ['srvConfiguration', 'srvPerformance'],
        'frameSizeMode': ['custom', 'fixed', 'increment', 'random'],
        'latencyType': ['cutThrough', 'mef', 'storeForward'],
        'portDelayUnit': ['bytes', 'nanoseconds'],
        'reportTputRateUnit': ['gbps', 'gBps', 'kbps', 'kBps', 'mbps', 'mBps'],
        'rfc2889ordering': ['noOrdering', 'unchanged', 'val2889Ordering'],
        'transmitMode': ['noFrames', 'useDuration'],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def AlgorithmType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(srvConfiguration | srvPerformance): The type of algorithm used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AlgorithmType'])
    @AlgorithmType.setter
    def AlgorithmType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AlgorithmType'], value)

    @property
    def CalculateJitter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Calculates the interval between timestamps of PGID packet arrivals.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateJitter'])
    @CalculateJitter.setter
    def CalculateJitter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalculateJitter'], value)

    @property
    def CalculateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Calculates and reports latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def ContinuePassFailed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ContinuePassFailed'])
    @ContinuePassFailed.setter
    def ContinuePassFailed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ContinuePassFailed'], value)

    @property
    def CurrentService(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The service in use currently.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentService'])
    @CurrentService.setter
    def CurrentService(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CurrentService'], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The duration of the test in hours, which is used to calculate the number of frames to transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def DurationLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The label defining the traffic duration time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationLabel'])
    @DurationLabel.setter
    def DurationLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DurationLabel'], value)

    @property
    def EnableBurstTest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables burst test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBurstTest'])
    @EnableBurstTest.setter
    def EnableBurstTest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableBurstTest'], value)

    @property
    def EnableDataIntegrity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables data integrity test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'])
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'], value)

    @property
    def EnableLatencyPassFailLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The latency pass fail criteria is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLatencyPassFailLabel'])
    @EnableLatencyPassFailLabel.setter
    def EnableLatencyPassFailLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableLatencyPassFailLabel'], value)

    @property
    def EnableLayer1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'])
    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'], value)

    @property
    def EnableStandardDeviationPassFailLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Standard Deviation for the Pass/Fail criteria is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStandardDeviationPassFailLabel'])
    @EnableStandardDeviationPassFailLabel.setter
    def EnableStandardDeviationPassFailLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableStandardDeviationPassFailLabel'], value)

    @property
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

    @property
    def FrameDataDetailedResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameDataDetailedResults'])
    @FrameDataDetailedResults.setter
    def FrameDataDetailedResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['FrameDataDetailedResults'], value)

    @property
    def FrameLossFramesMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameLossFramesMode'])
    @FrameLossFramesMode.setter
    def FrameLossFramesMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FrameLossFramesMode'], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The gap in transmission of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def GenerateTrackingOptionAggregationFiles(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the tracking option in aggregation files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'])
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'], value)

    @property
    def IsColorAware(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it becomes aware of the color.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsColorAware'])
    @IsColorAware.setter
    def IsColorAware(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsColorAware'], value)

    @property
    def IsServicePeformanceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The service performance mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsServicePeformanceMode'])
    @IsServicePeformanceMode.setter
    def IsServicePeformanceMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsServicePeformanceMode'], value)

    @property
    def IterationInitialRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The initial rate of iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IterationInitialRate'])
    @IterationInitialRate.setter
    def IterationInitialRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['IterationInitialRate'], value)

    @property
    def IterationStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The iteration step.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IterationStep'])
    @IterationStep.setter
    def IterationStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['IterationStep'], value)

    @property
    def LatencyBins(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBins'])
    @LatencyBins.setter
    def LatencyBins(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatencyBins'], value)

    @property
    def LatencyBinsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the latency bins statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'])
    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'], value)

    @property
    def LatencyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | mef | storeForward): The type of latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LearnSnoopConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The learned snoop configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnSnoopConfig'])
    @LearnSnoopConfig.setter
    def LearnSnoopConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['LearnSnoopConfig'], value)

    @property
    def NoOfFrames(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The number of frames sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfFrames'])
    @NoOfFrames.setter
    def NoOfFrames(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfFrames'], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the Number of trials.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PortDelayEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayEnabled'])
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['PortDelayEnabled'], value)

    @property
    def PortDelayUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayUnit'])
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PortDelayUnit'], value)

    @property
    def PortDelayValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the port delay value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayValue'])
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PortDelayValue'], value)

    @property
    def ProtocolItem(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def ReportSequenceError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the sequence error, if found, is reported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportSequenceError'])
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ReportSequenceError'], value)

    @property
    def ReportTputRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The unit of rate for throughput.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'])
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'], value)

    @property
    def Rfc2889ordering(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2889ordering'])
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Rfc2889ordering'], value)

    @property
    def ServiceIterations(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Number of service iterations.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServiceIterations'])
    @ServiceIterations.setter
    def ServiceIterations(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ServiceIterations'], value)

    @property
    def ServicesList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of service.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServicesList'])
    @ServicesList.setter
    def ServicesList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ServicesList'], value)

    @property
    def SkipDefaultPassFailEvaluation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it skips the default pass fail evaluation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipDefaultPassFailEvaluation'])
    @SkipDefaultPassFailEvaluation.setter
    def SkipDefaultPassFailEvaluation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SkipDefaultPassFailEvaluation'], value)

    @property
    def StaggeredStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Staggered start of traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStart'])
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStart'], value)

    @property
    def TestTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives the test traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTrafficType'])
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TestTrafficType'], value)

    @property
    def TransmitMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noFrames | useDuration): The transmit mode for this traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitMode'])
    @TransmitMode.setter
    def TransmitMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TransmitMode'], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum delay between successive packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    def update(self, AlgorithmType=None, CalculateJitter=None, CalculateLatency=None, ContinuePassFailed=None, CurrentService=None, DelayAfterTransmit=None, Duration=None, DurationLabel=None, EnableBurstTest=None, EnableDataIntegrity=None, EnableLatencyPassFailLabel=None, EnableLayer1Rate=None, EnableStandardDeviationPassFailLabel=None, ForceRegenerate=None, FrameDataDetailedResults=None, FrameLossFramesMode=None, FrameSizeMode=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, IsColorAware=None, IsServicePeformanceMode=None, IterationInitialRate=None, IterationStep=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LearnSnoopConfig=None, NoOfFrames=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Rfc2889ordering=None, ServiceIterations=None, ServicesList=None, SkipDefaultPassFailEvaluation=None, StaggeredStart=None, TestTrafficType=None, TransmitMode=None, TxDelay=None):
        # type: (str, bool, bool, bool, str, int, int, str, bool, bool, str, bool, str, bool, bool, str, str, int, bool, bool, str, str, str, str, bool, str, bool, str, int, bool, str, int, List[str], bool, str, str, str, str, bool, bool, str, str, int) -> TestConfig
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
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AlgorithmType=None, CalculateJitter=None, CalculateLatency=None, ContinuePassFailed=None, CurrentService=None, DelayAfterTransmit=None, Duration=None, DurationLabel=None, EnableBurstTest=None, EnableDataIntegrity=None, EnableLatencyPassFailLabel=None, EnableLayer1Rate=None, EnableStandardDeviationPassFailLabel=None, ForceRegenerate=None, FrameDataDetailedResults=None, FrameLossFramesMode=None, FrameSizeMode=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, IsColorAware=None, IsServicePeformanceMode=None, IterationInitialRate=None, IterationStep=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LearnSnoopConfig=None, NoOfFrames=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Rfc2889ordering=None, ServiceIterations=None, ServicesList=None, SkipDefaultPassFailEvaluation=None, StaggeredStart=None, TestTrafficType=None, TransmitMode=None, TxDelay=None):
        # type: (str, bool, bool, bool, str, int, int, str, bool, bool, str, bool, str, bool, bool, str, str, int, bool, bool, str, str, str, str, bool, str, bool, str, int, bool, str, int, List[str], bool, str, str, str, str, bool, bool, str, str, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

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

        Returns
        -------
        - self: This instance with matching testConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
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
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('waitForTest', payload=payload, response_object=None)
