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
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
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
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CountRandomLoadRate': 'countRandomLoadRate',
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
        'FixedFramesize': 'fixedFramesize',
        'FixedLoadUnit': 'fixedLoadUnit',
        'FixedRate': 'fixedRate',
        'ForceContinuosTraffic': 'forceContinuosTraffic',
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
        'InitialIncrementLoadRate': 'initialIncrementLoadRate',
        'InitialStepLoadRate': 'initialStepLoadRate',
        'Ipv4rate': 'ipv4rate',
        'Ipv6rate': 'ipv6rate',
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
        'MaxRate': 'maxRate',
        'MaxStepLoadRate': 'maxStepLoadRate',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinComboLoadRate': 'minComboLoadRate',
        'MinFpsRate': 'minFpsRate',
        'MinFramesize': 'minFramesize',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinKbpsRate': 'minKbpsRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MinRandomLoadRate': 'minRandomLoadRate',
        'MinRate': 'minRate',
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
        'Runmode': 'runmode',
        'SaturationIteration': 'saturationIteration',
        'StaggeredStart': 'staggeredStart',
        'StepComboLoadRate': 'stepComboLoadRate',
        'StepFrameLossUnit': 'stepFrameLossUnit',
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
    def BackoffIteration(self):
        """
        Returns
        -------
        - number: The backoff of the test configuration.
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
        - number: The binary search interval through which the next iteration's rate is obtained.
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
        - str(% | frames): Signifies the binary frame loss unit.
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
        - number: The binary resolution of the test configuration.
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
        - str(linear | perFlow | perPort | perTrafficItem): Signifies the binary search type.
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
        - number: The tolerance that a binary field can accept.
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
        - number: The backoff combination of the test configuration.
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
        - str(% | frames): Signifies the combo frame loss unit.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the combo load unit.
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
        - number: Specify the combination resolution of the iteration.
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
        - number: The tolerance combination of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboTolerance'])
    @ComboTolerance.setter
    def ComboTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboTolerance'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: Signifies the count of random frame size.
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
        - number: Signifies the count of random load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomLoadRate'])
    @CountRandomLoadRate.setter
    def CountRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomLoadRate'], value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the custom load unit.
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
        - number: Signifies the delay time after transmit.
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
        - str: Disabled inherited imix.
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
        - number: The duration of the test in hours, which is used to calculate the number of frames to transmit.
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
        - bool: If true, enables backoff of iteration.
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
        - bool: If true, enables data integrity.
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
        - bool: If true, enables extra iterations.
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
        - bool: If true, enables fast convergence.
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
        - bool: If true, enables the test to run an extra iteration for calculating the SaturationLatency.
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
        - bool: If true, stops the test in case of a high loss.
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
        - str: Signifies the extra iterations offsets.
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
        - number: Signifies the duration time between fast convergences.
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
        - number: Signifies the threshold of fast convergence.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'])
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'], value)

    @property
    def FixedFramesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedFramesize'])
    @FixedFramesize.setter
    def FixedFramesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedFramesize'], value)

    @property
    def FixedLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the fixed load unit values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedLoadUnit'])
    @FixedLoadUnit.setter
    def FixedLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedLoadUnit'], value)

    @property
    def FixedRate(self):
        """
        Returns
        -------
        - number: Signifies the fixed rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedRate'])
    @FixedRate.setter
    def FixedRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedRate'], value)

    @property
    def ForceContinuosTraffic(self):
        """
        Returns
        -------
        - bool: Forces continuous traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceContinuosTraffic'])
    @ForceContinuosTraffic.setter
    def ForceContinuosTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceContinuosTraffic'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: If true, forces regeneration.
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
        - str: Signifies the frame loss unit.
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
        - str(custom | increment | random): Signifies the frame size mode.
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
        - number: Signifies the frames per burst gap.
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
        - str: Signifies the framesize.
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
        - number: Signifies the fixed value of frame size.
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
        - str: Signifies the IMIX list of frame size.
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
        - list(str): Lists the frame size.
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
        - number: The gap in transmission of frames.
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
        - bool: If true, enables the tracking option in aggregation files.
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
        - str: Signifies the IMIX address.
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
        - str: Signifies the IMIX data.
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
        - str(bwpercentage | weight): Signifies the distribution list of IMIX.
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
        - bool: If true, enables IMIX.
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
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies the IMIX templates.
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
        - str: Signifies the traffic type of IMIX.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the incremented load unit.
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
        - number: Signifies the initial combo load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialComboLoadRate'])
    @InitialComboLoadRate.setter
    def InitialComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialComboLoadRate'], value)

    @property
    def InitialIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the initial increment of load rate.
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
        - number: Signifies the initial step load rate value.
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
        - str: Enter the Load Rate List.
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
        - number: The value of the load rate.
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
        - str(fixed | random | unchanged): Type of load.
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
        - str: Signifies the load unit.
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
        - number: Signifies the maximum binary load rate.
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
        - number: Signifies the maximum combo load rate.
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
        - number: Bytes
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
        - number: Signifies the maximum increment of frame size.
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
        - number: Signifies the maximum random frame size.
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
        - number: Signifies the maximum random load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomLoadRate'])
    @MaxRandomLoadRate.setter
    def MaxRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomLoadRate'], value)

    @property
    def MaxRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRate'])
    @MaxRate.setter
    def MaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRate'], value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum step load rate.
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
        - number: Signifies the minimum binary load rate.
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
        - number: Signifies the minimum combo load rate.
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
        - number: Signifies the Minimum fps rate.
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
        - number: Bytes
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
        - number: Signifies the minimum increment frame size.
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
        - number: Signifies the minimum kbps rate.
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
        - number: Signifies the minimum random frame size.
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
        - number: Signifies the minimum random load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'])
    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'], value)

    @property
    def MinRate(self):
        """
        Returns
        -------
        - number: Signifies the minimum rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRate'])
    @MinRate.setter
    def MinRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRate'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Defines how many times each frame size will be tested.
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
        - number: The maximum rate percentage.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the random load unit value.
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
        - str(fpsRate | kbpsRate | percentMaxRate): Signifies the rate selected.
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
        - bool: If true, reports sequence error.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): Reports the throughput rate unit.
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
    def Runmode(self):
        """
        Returns
        -------
        - str(duration | noframes): Specifies the number of frames that IxNetwork sends from each port in running mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Runmode'])
    @Runmode.setter
    def Runmode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Runmode'], value)

    @property
    def SaturationIteration(self):
        """
        Returns
        -------
        - number: The of iteration for saturation.
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
        - bool: If true, staggers the start of the test.
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
        - number: The combination step value of load rate.
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
        - str(% | frames): Signifies the step frame loss unit value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepFrameLossUnit'])
    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepFrameLossUnit'], value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: Increments the step frame size.
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
        - number: Signifies the incremented step load rate value.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the step load unit value.
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
        - number: Signifies the step value of the load rate.
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
        - number: It the stops the test on high loss.
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
        - str(burstyLoading | constantLoading): Signifies the type of traffic.
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
        - str: Signifies the unchanged value list.
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
        - str: Signifies the use of percent offsets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, BackoffIteration=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountRandomFrameSize=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, DisableInheritedImix=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FixedFramesize=None, FixedLoadUnit=None, FixedRate=None, ForceContinuosTraffic=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeFixedValue=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, Ipv4rate=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadRateValue=None, LoadType=None, LoadUnit=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxFramesize=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomLoadRate=None, MaxRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinFramesize=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomLoadRate=None, MinRate=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Runmode=None, SaturationIteration=None, StaggeredStart=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedInitial=None, UnchangedValueList=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BackoffIteration (number): The backoff of the test configuration.
        - BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
        - BinaryFrameLossUnit (str(% | frames)): Signifies the binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the binary load unit.
        - BinaryResolution (number): The binary resolution of the test configuration.
        - BinarySearchType (str(linear | perFlow | perPort | perTrafficItem)): Signifies the binary search type.
        - BinaryTolerance (number): The tolerance that a binary field can accept.
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - ComboBackoff (number): The backoff combination of the test configuration.
        - ComboFrameLossUnit (str(% | frames)): Signifies the combo frame loss unit.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the combo load unit.
        - ComboResolution (number): Specify the combination resolution of the iteration.
        - ComboTolerance (number): The tolerance combination of the test configuration.
        - CountRandomFrameSize (number): Signifies the count of random frame size.
        - CountRandomLoadRate (number): Signifies the count of random load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the custom load unit.
        - DelayAfterTransmit (number): Signifies the delay time after transmit.
        - DisableInheritedImix (str): Disabled inherited imix.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableBackoffIteration (bool): If true, enables backoff of iteration.
        - EnableDataIntegrity (bool): If true, enables data integrity.
        - EnableExtraIterations (bool): If true, enables extra iterations.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
        - EnableStopTestOnHighLoss (bool): If true, stops the test in case of a high loss.
        - ExtraIterationOffsets (str): Signifies the extra iterations offsets.
        - FastConvergenceDuration (number): Signifies the duration time between fast convergences.
        - FastConvergenceThreshold (number): Signifies the threshold of fast convergence.
        - FixedFramesize (number): Bytes
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the fixed load unit values.
        - FixedRate (number): Signifies the fixed rate.
        - ForceContinuosTraffic (bool): Forces continuous traffic.
        - ForceRegenerate (bool): If true, forces regeneration.
        - FrameLossUnit (str): Signifies the frame loss unit.
        - FrameSizeMode (str(custom | increment | random)): Signifies the frame size mode.
        - FramesPerBurstGap (number): Signifies the frames per burst gap.
        - Framesize (str): Signifies the framesize.
        - FramesizeFixedValue (number): Signifies the fixed value of frame size.
        - FramesizeImixList (str): Signifies the IMIX list of frame size.
        - FramesizeList (list(str)): Lists the frame size.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - ImixAdd (str): Signifies the IMIX address.
        - ImixData (str): Signifies the IMIX data.
        - ImixDelete (str): Signifies the deleted data of IMIX.
        - ImixDistribution (str(bwpercentage | weight)): Signifies the distribution list of IMIX.
        - ImixEnabled (bool): If true, enables IMIX.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies the IMIX templates.
        - ImixTrafficType (str): Signifies the traffic type of IMIX.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the incremented load unit.
        - InitialBinaryLoadRate (number): Signifies the initial binary load rate.
        - InitialComboLoadRate (number): Signifies the initial combo load rate.
        - InitialIncrementLoadRate (number): Signifies the initial increment of load rate.
        - InitialStepLoadRate (number): Signifies the initial step load rate value.
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): The type of latency.
        - LoadRateList (str): Enter the Load Rate List.
        - LoadRateValue (number): The value of the load rate.
        - LoadType (str(fixed | random | unchanged)): Type of load.
        - LoadUnit (str): Signifies the load unit.
        - MaxBinaryLoadRate (number): Signifies the maximum binary load rate.
        - MaxComboLoadRate (number): Signifies the maximum combo load rate.
        - MaxFramesize (number): Bytes
        - MaxIncrementFrameSize (number): Signifies the maximum increment of frame size.
        - MaxIncrementLoadRate (number): Signifies the maximum increment of load rate.
        - MaxRandomFrameSize (number): Signifies the maximum random frame size.
        - MaxRandomLoadRate (number): Signifies the maximum random load rate.
        - MaxRate (number): Signifies the maximum rate.
        - MaxStepLoadRate (number): Signifies the maximum step load rate.
        - MinBinaryLoadRate (number): Signifies the minimum binary load rate.
        - MinComboLoadRate (number): Signifies the minimum combo load rate.
        - MinFpsRate (number): Signifies the Minimum fps rate.
        - MinFramesize (number): Bytes
        - MinIncrementFrameSize (number): Signifies the minimum increment frame size.
        - MinKbpsRate (number): Signifies the minimum kbps rate.
        - MinRandomFrameSize (number): Signifies the minimum random frame size.
        - MinRandomLoadRate (number): Signifies the minimum random load rate.
        - MinRate (number): Signifies the minimum rate.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PercentMaxRate (number): The maximum rate percentage.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the random load unit value.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): Signifies the rate selected.
        - ReportSequenceError (bool): If true, reports sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Reports the throughput rate unit.
        - Resolution (number): Specify the resolution of the iteration.
        - Runmode (str(duration | noframes)): Specifies the number of frames that IxNetwork sends from each port in running mode.
        - SaturationIteration (number): The of iteration for saturation.
        - StaggeredStart (bool): If true, staggers the start of the test.
        - StepComboLoadRate (number): The combination step value of load rate.
        - StepFrameLossUnit (str(% | frames)): Signifies the step frame loss unit value.
        - StepIncrementFrameSize (number): Increments the step frame size.
        - StepIncrementLoadRate (number): Signifies the incremented step load rate value.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the step load unit value.
        - StepStepLoadRate (number): Signifies the step value of the load rate.
        - StepTolerance (number): The step value of the tolerance level.
        - StopTestOnHighLoss (number): It the stops the test on high loss.
        - Tolerance (number): The value set for the tolerance level.
        - TrafficType (str(burstyLoading | constantLoading)): Signifies the type of traffic.
        - TxDelay (number): Signifies the transmission delay time.
        - UnchangedInitial (str(False | True)): Signifies the initial value that is unchanged.
        - UnchangedValueList (str): Signifies the unchanged value list.
        - UsePercentOffsets (str): Signifies the use of percent offsets.

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
