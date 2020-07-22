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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TestConfig(Base):
    """Signifies the test configurations.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'Backoff': 'backoff',
        'BackoffIteration': 'backoffIteration',
        'BinaryBackoff': 'binaryBackoff',
        'BinaryFrameLossUnit': 'binaryFrameLossUnit',
        'BinaryLoadUnit': 'binaryLoadUnit',
        'BinaryResolution': 'binaryResolution',
        'BinarySearchType': 'binarySearchType',
        'BinaryTolerance': 'binaryTolerance',
        'BurstSize': 'burstSize',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'ComboBackoff': 'comboBackoff',
        'ComboFrameLossUnit': 'comboFrameLossUnit',
        'ComboLoadUnit': 'comboLoadUnit',
        'ComboResolution': 'comboResolution',
        'ComboTolerance': 'comboTolerance',
        'CountFramesize': 'countFramesize',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CountRandomLoadRate': 'countRandomLoadRate',
        'CustomFramesize': 'customFramesize',
        'CustomLoadUnit': 'customLoadUnit',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DisableInheritedImix': 'disableInheritedImix',
        'Duration': 'duration',
        'EnableBackoffIteration': 'enableBackoffIteration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableExtraIterations': 'enableExtraIterations',
        'EnableFastConvergence': 'enableFastConvergence',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableSaturationIteration': 'enableSaturationIteration',
        'EnableStopTestOnHighLoss': 'enableStopTestOnHighLoss',
        'ExtraIterationOffsets': 'extraIterationOffsets',
        'FastConvergenceDuration': 'fastConvergenceDuration',
        'FastConvergenceThreshold': 'fastConvergenceThreshold',
        'FixedLoadUnit': 'fixedLoadUnit',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameSizeMode': 'frameSizeMode',
        'FramesPerBurstGap': 'framesPerBurstGap',
        'Framesize': 'framesize',
        'FramesizeFixedValue': 'framesizeFixedValue',
        'FramesizeImixList': 'framesizeImixList',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'GenerateTrackingOptionAggregationFiles': 'generateTrackingOptionAggregationFiles',
        'ImixAdd': 'imixAdd',
        'ImixData': 'imixData',
        'ImixDelete': 'imixDelete',
        'ImixDistribution': 'imixDistribution',
        'ImixEnabled': 'imixEnabled',
        'ImixTemplates': 'imixTemplates',
        'ImixTrafficType': 'imixTrafficType',
        'IncrementLoadUnit': 'incrementLoadUnit',
        'InitialBinaryLoadRate': 'initialBinaryLoadRate',
        'InitialComboLoadRate': 'initialComboLoadRate',
        'InitialFramesize': 'initialFramesize',
        'InitialIncrementLoadRate': 'initialIncrementLoadRate',
        'InitialStepLoadRate': 'initialStepLoadRate',
        'Ipv4rate': 'ipv4rate',
        'Ipv6rate': 'ipv6rate',
        'LastFramesize': 'lastFramesize',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LoadRateList': 'loadRateList',
        'LoadRateValue': 'loadRateValue',
        'LoadType': 'loadType',
        'LoadUnit': 'loadUnit',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxComboLoadRate': 'maxComboLoadRate',
        'MaxFramesize': 'maxFramesize',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxIncrementLoadRate': 'maxIncrementLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxRandomLoadRate': 'maxRandomLoadRate',
        'MaxStepLoadRate': 'maxStepLoadRate',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinComboLoadRate': 'minComboLoadRate',
        'MinFpsRate': 'minFpsRate',
        'MinFramesize': 'minFramesize',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinKbpsRate': 'minKbpsRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MinRandomLoadRate': 'minRandomLoadRate',
        'Numtrials': 'numtrials',
        'PercentMaxRate': 'percentMaxRate',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'RandomLoadUnit': 'randomLoadUnit',
        'RateSelect': 'rateSelect',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'Resolution': 'resolution',
        'SaturationIteration': 'saturationIteration',
        'StaggeredStart': 'staggeredStart',
        'StepComboLoadRate': 'stepComboLoadRate',
        'StepFrameLossUnit': 'stepFrameLossUnit',
        'StepFramesize': 'stepFramesize',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepIncrementLoadRate': 'stepIncrementLoadRate',
        'StepLoadUnit': 'stepLoadUnit',
        'StepStepLoadRate': 'stepStepLoadRate',
        'StepTolerance': 'stepTolerance',
        'StopTestOnHighLoss': 'stopTestOnHighLoss',
        'Tolerance': 'tolerance',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
        'UnchangedInitial': 'unchangedInitial',
        'UnchangedValueList': 'unchangedValueList',
        'UsePercentOffsets': 'usePercentOffsets',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def Backoff(self):
        """
        Returns
        -------
        - number: The percentage value to increase or decrease, when the load is adjusted to decrease frame loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Backoff'])
    @Backoff.setter
    def Backoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Backoff'], value)

    @property
    def BackoffIteration(self):
        """
        Returns
        -------
        - number: This enables the test to run an extra iteration for calculating the Backoff Latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackoffIteration'])
    @BackoffIteration.setter
    def BackoffIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackoffIteration'], value)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: Specifies the percentage of binary backoff.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryBackoff'])
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryBackoff'], value)

    @property
    def BinaryFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): Signifies the two values of frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryFrameLossUnit'])
    @BinaryFrameLossUnit.setter
    def BinaryFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryFrameLossUnit'], value)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the binary load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'])
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'], value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: Specifies the resolution of the iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolution'])
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolution'], value)

    @property
    def BinarySearchType(self):
        """
        Returns
        -------
        - str(linear | perFlow | perPort | perTrafficItem): The binary search type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinarySearchType'])
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinarySearchType'], value)

    @property
    def BinaryTolerance(self):
        """
        Returns
        -------
        - number: The binary tolerance level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryTolerance'])
    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryTolerance'], value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: The number of packets to send in a burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def CalculateJitter(self):
        """
        Returns
        -------
        - bool: If true, calculates jitter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateJitter'])
    @CalculateJitter.setter
    def CalculateJitter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateJitter'], value)

    @property
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: If true, calculates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def ComboBackoff(self):
        """
        Returns
        -------
        - number: The combined backoff value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboBackoff'])
    @ComboBackoff.setter
    def ComboBackoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboBackoff'], value)

    @property
    def ComboFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): Signifies the loss unit for frames for test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboFrameLossUnit'])
    @ComboFrameLossUnit.setter
    def ComboFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboFrameLossUnit'], value)

    @property
    def ComboLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the combo loud unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboLoadUnit'])
    @ComboLoadUnit.setter
    def ComboLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboLoadUnit'], value)

    @property
    def ComboResolution(self):
        """
        Returns
        -------
        - number: Signifies the combination of resolution values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboResolution'])
    @ComboResolution.setter
    def ComboResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboResolution'], value)

    @property
    def ComboTolerance(self):
        """
        Returns
        -------
        - number: The combined tolerance level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboTolerance'])
    @ComboTolerance.setter
    def ComboTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboTolerance'], value)

    @property
    def CountFramesize(self):
        """
        Returns
        -------
        - number: Counts the number of frame sizes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountFramesize'])
    @CountFramesize.setter
    def CountFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountFramesize'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: If true, randomly counts the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def CountRandomLoadRate(self):
        """
        Returns
        -------
        - number: The random count of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomLoadRate'])
    @CountRandomLoadRate.setter
    def CountRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomLoadRate'], value)

    @property
    def CustomFramesize(self):
        """
        Returns
        -------
        - str: Signifies the customized frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomFramesize'])
    @CustomFramesize.setter
    def CustomFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomFramesize'], value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the custom load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def DisableInheritedImix(self):
        """
        Returns
        -------
        - str: If true, disables inherited imix data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableInheritedImix'])
    @DisableInheritedImix.setter
    def DisableInheritedImix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableInheritedImix'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: sec
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableBackoffIteration(self):
        """
        Returns
        -------
        - bool: If true, enables the test to run an extra iteration for calculating the Backoff Latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBackoffIteration'])
    @EnableBackoffIteration.setter
    def EnableBackoffIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBackoffIteration'], value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: If true, enables data integrity test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'])
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'], value)

    @property
    def EnableExtraIterations(self):
        """
        Returns
        -------
        - bool: If enabled, it signifies extra iterations.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraIterations'])
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraIterations'], value)

    @property
    def EnableFastConvergence(self):
        """
        Returns
        -------
        - bool: If enabled, it signifies the fast convergence.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastConvergence'])
    @EnableFastConvergence.setter
    def EnableFastConvergence(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastConvergence'], value)

    @property
    def EnableLayer1Rate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'])
    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableSaturationIteration(self):
        """
        Returns
        -------
        - bool: If true, enables the test to run an extra iteration for calculating the Saturation Latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSaturationIteration'])
    @EnableSaturationIteration.setter
    def EnableSaturationIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSaturationIteration'], value)

    @property
    def EnableStopTestOnHighLoss(self):
        """
        Returns
        -------
        - bool: If true, enable this to stop the high frame loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStopTestOnHighLoss'])
    @EnableStopTestOnHighLoss.setter
    def EnableStopTestOnHighLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStopTestOnHighLoss'], value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: It signifies the extra iterations offsets value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraIterationOffsets'])
    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraIterationOffsets'], value)

    @property
    def FastConvergenceDuration(self):
        """
        Returns
        -------
        - number: It signifies the fast convergence duration value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceDuration'])
    @FastConvergenceDuration.setter
    def FastConvergenceDuration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceDuration'], value)

    @property
    def FastConvergenceThreshold(self):
        """
        Returns
        -------
        - number: It signifies the fast convergence threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'])
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'], value)

    @property
    def FixedLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The fixed values for load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedLoadUnit'])
    @FixedLoadUnit.setter
    def FixedLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedLoadUnit'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

    @property
    def FrameLossUnit(self):
        """
        Returns
        -------
        - str: Signifies the unit for frame loss for test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameLossUnit'])
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameLossUnit'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def FramesPerBurstGap(self):
        """
        Returns
        -------
        - number: The number of frames to be sent after each burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'])
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'], value)

    @property
    def Framesize(self):
        """
        Returns
        -------
        - str: Signifies the frame size for test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Framesize'])
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Framesize'], value)

    @property
    def FramesizeFixedValue(self):
        """
        Returns
        -------
        - number: It signifies the frame size fixed value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeFixedValue'])
    @FramesizeFixedValue.setter
    def FramesizeFixedValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesizeFixedValue'], value)

    @property
    def FramesizeImixList(self):
        """
        Returns
        -------
        - str: Signifies the list of frame size imix value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeImixList'])
    @FramesizeImixList.setter
    def FramesizeImixList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesizeImixList'], value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): The list of the available frame sizes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeList'])
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesizeList'], value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: It signifies the gap value for the protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def GenerateTrackingOptionAggregationFiles(self):
        """
        Returns
        -------
        - bool: If enabled, it generates the tracking option for aggregation files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'])
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'], value)

    @property
    def ImixAdd(self):
        """
        Returns
        -------
        - str: Signifies the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixAdd'])
    @ImixAdd.setter
    def ImixAdd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixAdd'], value)

    @property
    def ImixData(self):
        """
        Returns
        -------
        - str: Signifies the IMIX data for test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixData'])
    @ImixData.setter
    def ImixData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixData'], value)

    @property
    def ImixDelete(self):
        """
        Returns
        -------
        - str: Signifies the deleted data of IMIX.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixDelete'])
    @ImixDelete.setter
    def ImixDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixDelete'], value)

    @property
    def ImixDistribution(self):
        """
        Returns
        -------
        - str(bwpercentage | weight): Signifies the distribution list for imix values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixDistribution'])
    @ImixDistribution.setter
    def ImixDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixDistribution'], value)

    @property
    def ImixEnabled(self):
        """
        Returns
        -------
        - bool: If true, enables the imix value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixEnabled'])
    @ImixEnabled.setter
    def ImixEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixEnabled'], value)

    @property
    def ImixTemplates(self):
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies the imix templates.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixTemplates'])
    @ImixTemplates.setter
    def ImixTemplates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixTemplates'], value)

    @property
    def ImixTrafficType(self):
        """
        Returns
        -------
        - str: Signifies the traffic type of test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixTrafficType'])
    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixTrafficType'], value)

    @property
    def IncrementLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): If true, increments the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementLoadUnit'])
    @IncrementLoadUnit.setter
    def IncrementLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementLoadUnit'], value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'])
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'], value)

    @property
    def InitialComboLoadRate(self):
        """
        Returns
        -------
        - number: The first combination load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialComboLoadRate'])
    @InitialComboLoadRate.setter
    def InitialComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialComboLoadRate'], value)

    @property
    def InitialFramesize(self):
        """
        Returns
        -------
        - number: Signifies the initial frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialFramesize'])
    @InitialFramesize.setter
    def InitialFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialFramesize'], value)

    @property
    def InitialIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the initial incremented load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialIncrementLoadRate'])
    @InitialIncrementLoadRate.setter
    def InitialIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialIncrementLoadRate'], value)

    @property
    def InitialStepLoadRate(self):
        """
        Returns
        -------
        - number: The initial step value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialStepLoadRate'])
    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialStepLoadRate'], value)

    @property
    def Ipv4rate(self):
        """
        Returns
        -------
        - number: The rate at which IPv4 traffic is sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4rate'])
    @Ipv4rate.setter
    def Ipv4rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4rate'], value)

    @property
    def Ipv6rate(self):
        """
        Returns
        -------
        - number: The rate at which IPv6 traffic is sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6rate'])
    @Ipv6rate.setter
    def Ipv6rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6rate'], value)

    @property
    def LastFramesize(self):
        """
        Returns
        -------
        - number: Signifies the last frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastFramesize'])
    @LastFramesize.setter
    def LastFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LastFramesize'], value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBins'])
    @LatencyBins.setter
    def LatencyBins(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyBins'], value)

    @property
    def LatencyBinsEnabled(self):
        """
        Returns
        -------
        - bool: Enables the latency bins statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'])
    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'], value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | storeForward): The type of latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadRateList(self):
        """
        Returns
        -------
        - str: Enters the Load Rate List.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateList'])
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateList'], value)

    @property
    def LoadRateValue(self):
        """
        Returns
        -------
        - number: Signifies the load rate value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateValue'])
    @LoadRateValue.setter
    def LoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateValue'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | combo | step): The type of the payload setting.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def LoadUnit(self):
        """
        Returns
        -------
        - str: Signifies the load unit value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadUnit'])
    @LoadUnit.setter
    def LoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadUnit'], value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Specifies the maximum rate of the binary algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'])
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'], value)

    @property
    def MaxComboLoadRate(self):
        """
        Returns
        -------
        - number: The maximum combination load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxComboLoadRate'])
    @MaxComboLoadRate.setter
    def MaxComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxComboLoadRate'], value)

    @property
    def MaxFramesize(self):
        """
        Returns
        -------
        - number: Signifies the maximum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxFramesize'])
    @MaxFramesize.setter
    def MaxFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxFramesize'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The maximum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum increment of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementLoadRate'])
    @MaxIncrementLoadRate.setter
    def MaxIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementLoadRate'], value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxRandomLoadRate(self):
        """
        Returns
        -------
        - number: The maximum random value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomLoadRate'])
    @MaxRandomLoadRate.setter
    def MaxRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomLoadRate'], value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: The maximum step value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxStepLoadRate'])
    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxStepLoadRate'], value)

    @property
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Specifies the minimum rate of the binary algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'])
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'], value)

    @property
    def MinComboLoadRate(self):
        """
        Returns
        -------
        - number: The minimum combination load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinComboLoadRate'])
    @MinComboLoadRate.setter
    def MinComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinComboLoadRate'], value)

    @property
    def MinFpsRate(self):
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinFpsRate'])
    @MinFpsRate.setter
    def MinFpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinFpsRate'], value)

    @property
    def MinFramesize(self):
        """
        Returns
        -------
        - number: Signifies the minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinFramesize'])
    @MinFramesize.setter
    def MinFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinFramesize'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinKbpsRate(self):
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinKbpsRate'])
    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinKbpsRate'], value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def MinRandomLoadRate(self):
        """
        Returns
        -------
        - number: The minimum random value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'])
    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Signifies the number of trials.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PercentMaxRate(self):
        """
        Returns
        -------
        - number: The maximum rate in percentage.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMaxRate'])
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentMaxRate'], value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayEnabled'])
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayEnabled'], value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayUnit'])
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayUnit'], value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayValue'])
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayValue'], value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def RandomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The random values of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomLoadUnit'])
    @RandomLoadUnit.setter
    def RandomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomLoadUnit'], value)

    @property
    def RateSelect(self):
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): The selected rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateSelect'])
    @RateSelect.setter
    def RateSelect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RateSelect'], value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: If true, the sequence error, if found, is reported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportSequenceError'])
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportSequenceError'], value)

    @property
    def ReportTputRateUnit(self):
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): If true, reports the throughput rate unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'])
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'], value)

    @property
    def Resolution(self):
        """
        Returns
        -------
        - number: Specify the resolution of the iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Resolution'])
    @Resolution.setter
    def Resolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Resolution'], value)

    @property
    def SaturationIteration(self):
        """
        Returns
        -------
        - number: This enables the test to run an extra iteration for calculating the Saturation Latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SaturationIteration'])
    @SaturationIteration.setter
    def SaturationIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SaturationIteration'], value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStart'])
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStart'], value)

    @property
    def StepComboLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the combination of step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepComboLoadRate'])
    @StepComboLoadRate.setter
    def StepComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepComboLoadRate'], value)

    @property
    def StepFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The step frame loss unit for upstream traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepFrameLossUnit'])
    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepFrameLossUnit'], value)

    @property
    def StepFramesize(self):
        """
        Returns
        -------
        - number: The step value for frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepFramesize'])
    @StepFramesize.setter
    def StepFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepFramesize'], value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The incremental step value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def StepIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the step value for incremented load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementLoadRate'])
    @StepIncrementLoadRate.setter
    def StepIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementLoadRate'], value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepLoadUnit'])
    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepLoadUnit'], value)

    @property
    def StepStepLoadRate(self):
        """
        Returns
        -------
        - number: The incremental step value of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepStepLoadRate'])
    @StepStepLoadRate.setter
    def StepStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepStepLoadRate'], value)

    @property
    def StepTolerance(self):
        """
        Returns
        -------
        - number: The step value of the tolerance level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepTolerance'])
    @StepTolerance.setter
    def StepTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepTolerance'], value)

    @property
    def StopTestOnHighLoss(self):
        """
        Returns
        -------
        - number: If true, enables this to stop the test in case of high frame loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StopTestOnHighLoss'])
    @StopTestOnHighLoss.setter
    def StopTestOnHighLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StopTestOnHighLoss'], value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: The value set for the tolerance level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tolerance'])
    @Tolerance.setter
    def Tolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tolerance'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): The test based on the traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: Signifies the transmission delay time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    @property
    def UnchangedInitial(self):
        """
        Returns
        -------
        - str(False | True): Signifies the initial value that is unchanged.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnchangedInitial'])
    @UnchangedInitial.setter
    def UnchangedInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnchangedInitial'], value)

    @property
    def UnchangedValueList(self):
        """
        Returns
        -------
        - str: It signifies the unchanged value list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnchangedValueList'])
    @UnchangedValueList.setter
    def UnchangedValueList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnchangedValueList'], value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - str: It signifies the value of percent offsets when used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, Backoff=None, BackoffIteration=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountFramesize=None, CountRandomFrameSize=None, CountRandomLoadRate=None, CustomFramesize=None, CustomLoadUnit=None, DelayAfterTransmit=None, DisableInheritedImix=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FixedLoadUnit=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeFixedValue=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialFramesize=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, Ipv4rate=None, Ipv6rate=None, LastFramesize=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadRateValue=None, LoadType=None, LoadUnit=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxFramesize=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinFramesize=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomLoadRate=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, SaturationIteration=None, StaggeredStart=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepFramesize=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedInitial=None, UnchangedValueList=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - Backoff (number): The percentage value to increase or decrease, when the load is adjusted to decrease frame loss.
        - BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
        - BinaryBackoff (number): Specifies the percentage of binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): Signifies the two values of frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the binary load unit.
        - BinaryResolution (number): Specifies the resolution of the iteration.
        - BinarySearchType (str(linear | perFlow | perPort | perTrafficItem)): The binary search type value.
        - BinaryTolerance (number): The binary tolerance level.
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - ComboBackoff (number): The combined backoff value.
        - ComboFrameLossUnit (str(% | frames)): Signifies the loss unit for frames for test configuration.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the combo loud unit.
        - ComboResolution (number): Signifies the combination of resolution values.
        - ComboTolerance (number): The combined tolerance level.
        - CountFramesize (number): Counts the number of frame sizes.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - CountRandomLoadRate (number): The random count of the load rate.
        - CustomFramesize (str): Signifies the customized frame size.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - DisableInheritedImix (str): If true, disables inherited imix data.
        - Duration (number): sec
        - EnableBackoffIteration (bool): If true, enables the test to run an extra iteration for calculating the Backoff Latency.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableExtraIterations (bool): If enabled, it signifies extra iterations.
        - EnableFastConvergence (bool): If enabled, it signifies the fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the Saturation Latency.
        - EnableStopTestOnHighLoss (bool): If true, enable this to stop the high frame loss.
        - ExtraIterationOffsets (str): It signifies the extra iterations offsets value.
        - FastConvergenceDuration (number): It signifies the fast convergence duration value.
        - FastConvergenceThreshold (number): It signifies the fast convergence threshold value.
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The fixed values for load unit.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameLossUnit (str): Signifies the unit for frame loss for test configuration.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesPerBurstGap (number): The number of frames to be sent after each burst.
        - Framesize (str): Signifies the frame size for test configuration.
        - FramesizeFixedValue (number): It signifies the frame size fixed value.
        - FramesizeImixList (str): Signifies the list of frame size imix value.
        - FramesizeList (list(str)): The list of the available frame sizes.
        - Gap (number): It signifies the gap value for the protocol.
        - GenerateTrackingOptionAggregationFiles (bool): If enabled, it generates the tracking option for aggregation files.
        - ImixAdd (str): Signifies the test configuration.
        - ImixData (str): Signifies the IMIX data for test configuration.
        - ImixDelete (str): Signifies the deleted data of IMIX.
        - ImixDistribution (str(bwpercentage | weight)): Signifies the distribution list for imix values.
        - ImixEnabled (bool): If true, enables the imix value.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies the imix templates.
        - ImixTrafficType (str): Signifies the traffic type of test configuration.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): If true, increments the load unit.
        - InitialBinaryLoadRate (number): Signifies the initial binary load rate.
        - InitialComboLoadRate (number): The first combination load rate.
        - InitialFramesize (number): Signifies the initial frame size.
        - InitialIncrementLoadRate (number): Signifies the initial incremented load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LastFramesize (number): Signifies the last frame size.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): The type of latency.
        - LoadRateList (str): Enters the Load Rate List.
        - LoadRateValue (number): Signifies the load rate value.
        - LoadType (str(binary | combo | step)): The type of the payload setting.
        - LoadUnit (str): Signifies the load unit value.
        - MaxBinaryLoadRate (number): Specifies the maximum rate of the binary algorithm.
        - MaxComboLoadRate (number): The maximum combination load rate.
        - MaxFramesize (number): Signifies the maximum frame size.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxIncrementLoadRate (number): Signifies the maximum increment of load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRandomLoadRate (number): The maximum random value of the load rate.
        - MaxStepLoadRate (number): The maximum step value of the load rate.
        - MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
        - MinComboLoadRate (number): The minimum combination load rate.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinFramesize (number): Signifies the minimum frame size.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MinRandomLoadRate (number): The minimum random value of the load rate.
        - Numtrials (number): Signifies the number of trials.
        - PercentMaxRate (number): The maximum rate in percentage.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): The selected rate.
        - ReportSequenceError (bool): If true, the sequence error, if found, is reported.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): If true, reports the throughput rate unit.
        - Resolution (number): Specify the resolution of the iteration.
        - SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation Latency.
        - StaggeredStart (bool): If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
        - StepComboLoadRate (number): Signifies the combination of step load rate.
        - StepFrameLossUnit (str(% | frames)): The step frame loss unit for upstream traffic.
        - StepFramesize (number): The step value for frame size.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepIncrementLoadRate (number): Signifies the step value for incremented load rate.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTolerance (number): The step value of the tolerance level.
        - StopTestOnHighLoss (number): If true, enables this to stop the test in case of high frame loss.
        - Tolerance (number): The value set for the tolerance level.
        - TrafficType (str(burstyLoading | constantLoading)): The test based on the traffic type.
        - TxDelay (number): Signifies the transmission delay time.
        - UnchangedInitial (str(False | True)): Signifies the initial value that is unchanged.
        - UnchangedValueList (str): It signifies the unchanged value list.
        - UsePercentOffsets (str): It signifies the value of percent offsets when used.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
