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
    """The IxNetwork Test Configuration feature provides the ability to run predefined
tests and allows the user to set some global test parameters for the individual test
types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: The percentage to be applied to the search interval through which the next iterations rate is obtained.
        """
        return self._get_attribute('binaryBackoff')
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        self._set_attribute('binaryBackoff', value)

    @property
    def BinaryFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The binary frame loss unit.
        """
        return self._get_attribute('binaryFrameLossUnit')
    @BinaryFrameLossUnit.setter
    def BinaryFrameLossUnit(self, value):
        self._set_attribute('binaryFrameLossUnit', value)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The binary load unit.
        """
        return self._get_attribute('binaryLoadUnit')
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute('binaryLoadUnit', value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: The resolution of the iteration during a binary search.
        """
        return self._get_attribute('binaryResolution')
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute('binaryResolution', value)

    @property
    def BinarySearchType(self):
        """
        Returns
        -------
        - str(linear | perFlow | perPort): The binary search type.
        """
        return self._get_attribute('binarySearchType')
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute('binarySearchType', value)

    @property
    def BinaryTolerance(self):
        """
        Returns
        -------
        - number: The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.
        """
        return self._get_attribute('binaryTolerance')
    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        self._set_attribute('binaryTolerance', value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: It signifies the burst size of the protocol.
        """
        return self._get_attribute('burstSize')
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute('burstSize', value)

    @property
    def CalculateJitter(self):
        """
        Returns
        -------
        - bool: If true, enables jitter calculation.
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
        - bool: If true, enables latency calculation.
        """
        return self._get_attribute('calculateLatency')
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute('calculateLatency', value)

    @property
    def ComboBackoff(self):
        """
        Returns
        -------
        - number: The percentage to be applied to the search interval through which the next iterations rate is obtained, for Combo Load Type.
        """
        return self._get_attribute('comboBackoff')
    @ComboBackoff.setter
    def ComboBackoff(self, value):
        self._set_attribute('comboBackoff', value)

    @property
    def ComboFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The combo frame loss unit.
        """
        return self._get_attribute('comboFrameLossUnit')
    @ComboFrameLossUnit.setter
    def ComboFrameLossUnit(self, value):
        self._set_attribute('comboFrameLossUnit', value)

    @property
    def ComboLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The combo Load Unit.
        """
        return self._get_attribute('comboLoadUnit')
    @ComboLoadUnit.setter
    def ComboLoadUnit(self, value):
        self._set_attribute('comboLoadUnit', value)

    @property
    def ComboResolution(self):
        """
        Returns
        -------
        - number: The resolution of the iteration for Combo Load Type.
        """
        return self._get_attribute('comboResolution')
    @ComboResolution.setter
    def ComboResolution(self, value):
        self._set_attribute('comboResolution', value)

    @property
    def ComboTolerance(self):
        """
        Returns
        -------
        - number: The value of the tolerance level for Combo Load Type.
        """
        return self._get_attribute('comboTolerance')
    @ComboTolerance.setter
    def ComboTolerance(self, value):
        self._set_attribute('comboTolerance', value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: If true, randomly counts the frame size.
        """
        return self._get_attribute('countRandomFrameSize')
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute('countRandomFrameSize', value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The custom load unit.
        """
        return self._get_attribute('customLoadUnit')
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute('customLoadUnit', value)

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
    def DetailedResultsEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('detailedResultsEnabled')
    @DetailedResultsEnabled.setter
    def DetailedResultsEnabled(self, value):
        self._set_attribute('detailedResultsEnabled', value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The duration of the test in hours, which is used to calculate the number of framesto transmit.
        """
        return self._get_attribute('duration')
    @Duration.setter
    def Duration(self, value):
        self._set_attribute('duration', value)

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
    def EnableExtraIterations(self):
        """
        Returns
        -------
        - bool: If true, enables the tracking option in aggregation files.
        """
        return self._get_attribute('enableExtraIterations')
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute('enableExtraIterations', value)

    @property
    def EnableFastConvergence(self):
        """
        Returns
        -------
        - bool: If true, enables fast convergence.
        """
        return self._get_attribute('enableFastConvergence')
    @EnableFastConvergence.setter
    def EnableFastConvergence(self, value):
        self._set_attribute('enableFastConvergence', value)

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
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute('enableMinFrameSize')
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute('enableMinFrameSize', value)

    @property
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: Enables old statistics for reef.
        """
        return self._get_attribute('enableOldStatsForReef')
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute('enableOldStatsForReef', value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: Sets extra iteration offset values.
        """
        return self._get_attribute('extraIterationOffsets')
    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        self._set_attribute('extraIterationOffsets', value)

    @property
    def FastConvergenceDuration(self):
        """
        Returns
        -------
        - number: sec
        """
        return self._get_attribute('fastConvergenceDuration')
    @FastConvergenceDuration.setter
    def FastConvergenceDuration(self, value):
        self._set_attribute('fastConvergenceDuration', value)

    @property
    def FastConvergenceThreshold(self):
        """
        Returns
        -------
        - number: If true, enables fast convergence threshold value.
        """
        return self._get_attribute('fastConvergenceThreshold')
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute('fastConvergenceThreshold', value)

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
    def FrameLossUnit(self):
        """
        Returns
        -------
        - str: The frame loss unit.
        """
        return self._get_attribute('frameLossUnit')
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        self._set_attribute('frameLossUnit', value)

    @property
    def FrameOrderingByRfc2889(self):
        """
        Returns
        -------
        - bool: If true, indicates frame ordering by Rfc2889.
        """
        return self._get_attribute('frameOrderingByRfc2889')
    @FrameOrderingByRfc2889.setter
    def FrameOrderingByRfc2889(self, value):
        self._set_attribute('frameOrderingByRfc2889', value)

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
    def FramesPerBurstGap(self):
        """
        Returns
        -------
        - number: It signifies the frames per burst gap.
        """
        return self._get_attribute('framesPerBurstGap')
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        self._set_attribute('framesPerBurstGap', value)

    @property
    def Framesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute('framesize')
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute('framesize', value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): List containing the frame sizes used in the test.
        """
        return self._get_attribute('framesizeList')
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute('framesizeList', value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: Inter-frame gap.
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
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The load rate used in the first iteration for each frame size during a binary search.
        """
        return self._get_attribute('initialBinaryLoadRate')
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute('initialBinaryLoadRate', value)

    @property
    def InitialComboLoadRate(self):
        """
        Returns
        -------
        - number: The initial value of the load rate for Combo Load Type.
        """
        return self._get_attribute('initialComboLoadRate')
    @InitialComboLoadRate.setter
    def InitialComboLoadRate(self, value):
        self._set_attribute('initialComboLoadRate', value)

    @property
    def InitialStepLoadRate(self):
        """
        Returns
        -------
        - number: The initial value of the load rate for Step Load Type.
        """
        return self._get_attribute('initialStepLoadRate')
    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        self._set_attribute('initialStepLoadRate', value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics
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
        - bool: Enables the latency bins statistics
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
        - str(cutThrough | storeForward): The type of latency.
        """
        return self._get_attribute('latencyType')
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute('latencyType', value)

    @property
    def LoadRateList(self):
        """
        Returns
        -------
        - str: The list of Load Rate.
        """
        return self._get_attribute('loadRateList')
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute('loadRateList', value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | combo | custom | quickSearch | step | unchanged): The type of load.
        """
        return self._get_attribute('loadType')
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute('loadType', value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: The POS traffic map type.
        """
        return self._get_attribute('mapType')
    @MapType.setter
    def MapType(self, value):
        self._set_attribute('mapType', value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The lower bound of the iteration rates for each frame size during a binary search.
        """
        return self._get_attribute('maxBinaryLoadRate')
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute('maxBinaryLoadRate', value)

    @property
    def MaxComboLoadRate(self):
        """
        Returns
        -------
        - number: The maximum value of the load rate Combo Load Type.
        """
        return self._get_attribute('maxComboLoadRate')
    @MaxComboLoadRate.setter
    def MaxComboLoadRate(self, value):
        self._set_attribute('maxComboLoadRate', value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The maximum incremental value of the frame size.
        """
        return self._get_attribute('maxIncrementFrameSize')
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute('maxIncrementFrameSize', value)

    @property
    def MaxQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: Sets the maximum QuickSearch load rate
        """
        return self._get_attribute('maxQuickSearchLoadRate')
    @MaxQuickSearchLoadRate.setter
    def MaxQuickSearchLoadRate(self, value):
        self._set_attribute('maxQuickSearchLoadRate', value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute('maxRandomFrameSize')
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute('maxRandomFrameSize', value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: The maximum value of the load rate Step Load Type.
        """
        return self._get_attribute('maxStepLoadRate')
    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        self._set_attribute('maxStepLoadRate', value)

    @property
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The lower bound of the iteration rates for each frame size during a binary search.
        """
        return self._get_attribute('minBinaryLoadRate')
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute('minBinaryLoadRate', value)

    @property
    def MinComboLoadRate(self):
        """
        Returns
        -------
        - number: The minimum value of the load rate Combo Load Type.
        """
        return self._get_attribute('minComboLoadRate')
    @MinComboLoadRate.setter
    def MinComboLoadRate(self, value):
        self._set_attribute('minComboLoadRate', value)

    @property
    def MinFpsRate(self):
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per second.
        """
        return self._get_attribute('minFpsRate')
    @MinFpsRate.setter
    def MinFpsRate(self, value):
        self._set_attribute('minFpsRate', value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum incremental value of the frame size.
        """
        return self._get_attribute('minIncrementFrameSize')
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute('minIncrementFrameSize', value)

    @property
    def MinKbpsRate(self):
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per kbps.
        """
        return self._get_attribute('minKbpsRate')
    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        self._set_attribute('minKbpsRate', value)

    @property
    def MinQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: Sets the minum Quick Search load rate
        """
        return self._get_attribute('minQuickSearchLoadRate')
    @MinQuickSearchLoadRate.setter
    def MinQuickSearchLoadRate(self, value):
        self._set_attribute('minQuickSearchLoadRate', value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute('minRandomFrameSize')
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute('minRandomFrameSize', value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Defines how many times each frame size will be tested.
        """
        return self._get_attribute('numtrials')
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute('numtrials', value)

    @property
    def PercentMaxRate(self):
        """
        Returns
        -------
        - number: The percentage of the maximum rate that is specified.
        """
        return self._get_attribute('percentMaxRate')
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute('percentMaxRate', value)

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
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured
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
        - number: Sets the port delay value
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
    def QuickSearchFrameLossUnit(self):
        """
        Returns
        -------
        - str(%): Sets the quick search frame loss unit
        """
        return self._get_attribute('quickSearchFrameLossUnit')
    @QuickSearchFrameLossUnit.setter
    def QuickSearchFrameLossUnit(self, value):
        self._set_attribute('quickSearchFrameLossUnit', value)

    @property
    def QuickSearchLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Sets the quick search load unit
        """
        return self._get_attribute('quickSearchLoadUnit')
    @QuickSearchLoadUnit.setter
    def QuickSearchLoadUnit(self, value):
        self._set_attribute('quickSearchLoadUnit', value)

    @property
    def QuickSearchResolution(self):
        """
        Returns
        -------
        - number: Sets the quick search resolution
        """
        return self._get_attribute('quickSearchResolution')
    @QuickSearchResolution.setter
    def QuickSearchResolution(self, value):
        self._set_attribute('quickSearchResolution', value)

    @property
    def QuickSearchSearchType(self):
        """
        Returns
        -------
        - str(linear | perFlow | perPort | perTrafficItem): Sets the quick search type
        """
        return self._get_attribute('quickSearchSearchType')
    @QuickSearchSearchType.setter
    def QuickSearchSearchType(self, value):
        self._set_attribute('quickSearchSearchType', value)

    @property
    def QuickSearchTolerance(self):
        """
        Returns
        -------
        - number: Sets the quick search tolerance
        """
        return self._get_attribute('quickSearchTolerance')
    @QuickSearchTolerance.setter
    def QuickSearchTolerance(self, value):
        self._set_attribute('quickSearchTolerance', value)

    @property
    def RateSelect(self):
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): It selects the rate value of the protocol.
        """
        return self._get_attribute('rateSelect')
    @RateSelect.setter
    def RateSelect(self, value):
        self._set_attribute('rateSelect', value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: Reports sequence errors in the test result.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The report throughput rate.
        """
        return self._get_attribute('reportTputRateUnit')
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute('reportTputRateUnit', value)

    @property
    def Resolution(self):
        """
        Returns
        -------
        - number: Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        """
        return self._get_attribute('resolution')
    @Resolution.setter
    def Resolution(self, value):
        self._set_attribute('resolution', value)

    @property
    def Rfc2889ordering(self):
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): Enables ordering.
        """
        return self._get_attribute('rfc2889ordering')
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        self._set_attribute('rfc2889ordering', value)

    @property
    def SendFullyMeshed(self):
        """
        Returns
        -------
        - bool: Indicates the source group mapping type used for sending data.
        """
        return self._get_attribute('sendFullyMeshed')
    @SendFullyMeshed.setter
    def SendFullyMeshed(self, value):
        self._set_attribute('sendFullyMeshed', value)

    @property
    def ShowDetailedBinaryResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('showDetailedBinaryResults')
    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        self._set_attribute('showDetailedBinaryResults', value)

    @property
    def StepComboLoadRate(self):
        """
        Returns
        -------
        - number: The step rate of the binary algorithm for Combo Load Type.
        """
        return self._get_attribute('stepComboLoadRate')
    @StepComboLoadRate.setter
    def StepComboLoadRate(self, value):
        self._set_attribute('stepComboLoadRate', value)

    @property
    def StepFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The step frame loss unit.
        """
        return self._get_attribute('stepFrameLossUnit')
    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        self._set_attribute('stepFrameLossUnit', value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The incremental step value of the frame size.
        """
        return self._get_attribute('stepIncrementFrameSize')
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute('stepIncrementFrameSize', value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The step load unit.
        """
        return self._get_attribute('stepLoadUnit')
    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        self._set_attribute('stepLoadUnit', value)

    @property
    def StepStepLoadRate(self):
        """
        Returns
        -------
        - number: The step rate of the binary algorithm.
        """
        return self._get_attribute('stepStepLoadRate')
    @StepStepLoadRate.setter
    def StepStepLoadRate(self, value):
        self._set_attribute('stepStepLoadRate', value)

    @property
    def StepTolerance(self):
        """
        Returns
        -------
        - number: The value of the tolerance level for Step Load Type.
        """
        return self._get_attribute('stepTolerance')
    @StepTolerance.setter
    def StepTolerance(self, value):
        self._set_attribute('stepTolerance', value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The traffic types supported.
        """
        return self._get_attribute('supportedTrafficTypes')
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute('supportedTrafficTypes', value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: The level of acceptable threshold.
        """
        return self._get_attribute('tolerance')
    @Tolerance.setter
    def Tolerance(self, value):
        self._set_attribute('tolerance', value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): It signifies the traffic type.
        """
        return self._get_attribute('trafficType')
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute('trafficType', value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute('txDelay')
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute('txDelay', value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - bool: Uses percentage offset value.
        """
        return self._get_attribute('usePercentOffsets')
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute('usePercentOffsets', value)

    def update(self, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountRandomFrameSize=None, CustomLoadUnit=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, ForceRegenerate=None, FrameLossUnit=None, FrameOrderingByRfc2889=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialStepLoadRate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2889ordering=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BinaryBackoff (number): The percentage to be applied to the search interval through which the next iterations rate is obtained.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit.
        - BinaryResolution (number): The resolution of the iteration during a binary search.
        - BinarySearchType (str(linear | perFlow | perPort)): The binary search type.
        - BinaryTolerance (number): The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.
        - BurstSize (number): It signifies the burst size of the protocol.
        - CalculateJitter (bool): If true, enables jitter calculation.
        - CalculateLatency (bool): If true, enables latency calculation.
        - ComboBackoff (number): The percentage to be applied to the search interval through which the next iterations rate is obtained, for Combo Load Type.
        - ComboFrameLossUnit (str(% | frames)): The combo frame loss unit.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The combo Load Unit.
        - ComboResolution (number): The resolution of the iteration for Combo Load Type.
        - ComboTolerance (number): The value of the tolerance level for Combo Load Type.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The custom load unit.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - DetailedResultsEnabled (bool): 
        - Duration (number): The duration of the test in hours, which is used to calculate the number of framesto transmit.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableExtraIterations (bool): If true, enables the tracking option in aggregation files.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableOldStatsForReef (bool): Enables old statistics for reef.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FastConvergenceDuration (number): sec
        - FastConvergenceThreshold (number): If true, enables fast convergence threshold value.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameLossUnit (str): The frame loss unit.
        - FrameOrderingByRfc2889 (bool): If true, indicates frame ordering by Rfc2889.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesPerBurstGap (number): It signifies the frames per burst gap.
        - Framesize (number): Bytes
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - Gap (number): Inter-frame gap.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - InitialBinaryLoadRate (number): The load rate used in the first iteration for each frame size during a binary search.
        - InitialComboLoadRate (number): The initial value of the load rate for Combo Load Type.
        - InitialStepLoadRate (number): The initial value of the load rate for Step Load Type.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The type of latency.
        - LoadRateList (str): The list of Load Rate.
        - LoadType (str(binary | combo | custom | quickSearch | step | unchanged)): The type of load.
        - MapType (str): The POS traffic map type.
        - MaxBinaryLoadRate (number): The lower bound of the iteration rates for each frame size during a binary search.
        - MaxComboLoadRate (number): The maximum value of the load rate Combo Load Type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxStepLoadRate (number): The maximum value of the load rate Step Load Type.
        - MinBinaryLoadRate (number): The lower bound of the iteration rates for each frame size during a binary search.
        - MinComboLoadRate (number): The minimum value of the load rate Combo Load Type.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PercentMaxRate (number): The percentage of the maximum rate that is specified.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear | perFlow | perPort | perTrafficItem)): Sets the quick search type
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): It selects the rate value of the protocol.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The report throughput rate.
        - Resolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): Enables ordering.
        - SendFullyMeshed (bool): Indicates the source group mapping type used for sending data.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepComboLoadRate (number): The step rate of the binary algorithm for Combo Load Type.
        - StepFrameLossUnit (str(% | frames)): The step frame loss unit.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The step load unit.
        - StepStepLoadRate (number): The step rate of the binary algorithm.
        - StepTolerance (number): The value of the tolerance level for Step Load Type.
        - SupportedTrafficTypes (str): The traffic types supported.
        - Tolerance (number): The level of acceptable threshold.
        - TrafficType (str(burstyLoading | constantLoading)): It signifies the traffic type.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - UsePercentOffsets (bool): Uses percentage offset value.

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
