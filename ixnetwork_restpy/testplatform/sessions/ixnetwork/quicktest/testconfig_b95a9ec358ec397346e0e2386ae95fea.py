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
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def BackoffIteration(self):
        """
        Returns
        -------
        - number: The backoff of the test configuration.
        """
        return self._get_attribute('backoffIteration')
    @BackoffIteration.setter
    def BackoffIteration(self, value):
        self._set_attribute('backoffIteration', value)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: The binary search interval through which the next iteration's rate is obtained.
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
        - str(% | frames): Signifies the binary frame loss unit.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the binary load unit.
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
        - number: The binary resolution of the test configuration.
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
        - str(linear | perFlow | perPort | perTrafficItem): Signifies the binary search type.
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
        - number: The tolerance that a binary field can accept.
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
        - number: The number of packets to send in a burst.
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
        - bool: If true, calculates jitter.
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
        - bool: If true, calculates the latency.
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
        - number: The backoff combination of the test configuration.
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
        - str(% | frames): Signifies the combo frame loss unit.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the combo load unit.
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
        - number: Specify the combination resolution of the iteration.
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
        - number: The tolerance combination of the test configuration.
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
        - number: Signifies the count of random frame size.
        """
        return self._get_attribute('countRandomFrameSize')
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute('countRandomFrameSize', value)

    @property
    def CountRandomLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the count of random load rate.
        """
        return self._get_attribute('countRandomLoadRate')
    @CountRandomLoadRate.setter
    def CountRandomLoadRate(self, value):
        self._set_attribute('countRandomLoadRate', value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the custom load unit.
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
        - number: Signifies the delay time after transmit.
        """
        return self._get_attribute('delayAfterTransmit')
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute('delayAfterTransmit', value)

    @property
    def DisableInheritedImix(self):
        """
        Returns
        -------
        - str: Disabled inherited imix.
        """
        return self._get_attribute('disableInheritedImix')
    @DisableInheritedImix.setter
    def DisableInheritedImix(self, value):
        self._set_attribute('disableInheritedImix', value)

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
    def EnableBackoffIteration(self):
        """
        Returns
        -------
        - bool: If true, enables backoff of iteration.
        """
        return self._get_attribute('enableBackoffIteration')
    @EnableBackoffIteration.setter
    def EnableBackoffIteration(self, value):
        self._set_attribute('enableBackoffIteration', value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: If true, enables data integrity.
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
        - bool: If true, enables extra iterations.
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
    def EnableSaturationIteration(self):
        """
        Returns
        -------
        - bool: If true, enables the test to run an extra iteration for calculating the SaturationLatency.
        """
        return self._get_attribute('enableSaturationIteration')
    @EnableSaturationIteration.setter
    def EnableSaturationIteration(self, value):
        self._set_attribute('enableSaturationIteration', value)

    @property
    def EnableStopTestOnHighLoss(self):
        """
        Returns
        -------
        - bool: If true, stops the test in case of a high loss.
        """
        return self._get_attribute('enableStopTestOnHighLoss')
    @EnableStopTestOnHighLoss.setter
    def EnableStopTestOnHighLoss(self, value):
        self._set_attribute('enableStopTestOnHighLoss', value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: Signifies the extra iterations offsets.
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
        - number: Signifies the duration time between fast convergences.
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
        - number: Signifies the threshold of fast convergence.
        """
        return self._get_attribute('fastConvergenceThreshold')
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute('fastConvergenceThreshold', value)

    @property
    def FixedFramesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute('fixedFramesize')
    @FixedFramesize.setter
    def FixedFramesize(self, value):
        self._set_attribute('fixedFramesize', value)

    @property
    def FixedLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the fixed load unit values.
        """
        return self._get_attribute('fixedLoadUnit')
    @FixedLoadUnit.setter
    def FixedLoadUnit(self, value):
        self._set_attribute('fixedLoadUnit', value)

    @property
    def FixedRate(self):
        """
        Returns
        -------
        - number: Signifies the fixed rate.
        """
        return self._get_attribute('fixedRate')
    @FixedRate.setter
    def FixedRate(self, value):
        self._set_attribute('fixedRate', value)

    @property
    def ForceContinuosTraffic(self):
        """
        Returns
        -------
        - bool: Forces continuous traffic.
        """
        return self._get_attribute('forceContinuosTraffic')
    @ForceContinuosTraffic.setter
    def ForceContinuosTraffic(self, value):
        self._set_attribute('forceContinuosTraffic', value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: If true, forces regeneration.
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
        - str: Signifies the frame loss unit.
        """
        return self._get_attribute('frameLossUnit')
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        self._set_attribute('frameLossUnit', value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | increment | random): Signifies the frame size mode.
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
        - number: Signifies the frames per burst gap.
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
        - str: Signifies the framesize.
        """
        return self._get_attribute('framesize')
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute('framesize', value)

    @property
    def FramesizeFixedValue(self):
        """
        Returns
        -------
        - number: Signifies the fixed value of frame size.
        """
        return self._get_attribute('framesizeFixedValue')
    @FramesizeFixedValue.setter
    def FramesizeFixedValue(self, value):
        self._set_attribute('framesizeFixedValue', value)

    @property
    def FramesizeImixList(self):
        """
        Returns
        -------
        - str: Signifies the IMIX list of frame size.
        """
        return self._get_attribute('framesizeImixList')
    @FramesizeImixList.setter
    def FramesizeImixList(self, value):
        self._set_attribute('framesizeImixList', value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): Lists the frame size.
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
    def ImixAdd(self):
        """
        Returns
        -------
        - str: Signifies the IMIX address.
        """
        return self._get_attribute('imixAdd')
    @ImixAdd.setter
    def ImixAdd(self, value):
        self._set_attribute('imixAdd', value)

    @property
    def ImixData(self):
        """
        Returns
        -------
        - str: Signifies the IMIX data.
        """
        return self._get_attribute('imixData')
    @ImixData.setter
    def ImixData(self, value):
        self._set_attribute('imixData', value)

    @property
    def ImixDelete(self):
        """
        Returns
        -------
        - str: Signifies the deleted data of IMIX.
        """
        return self._get_attribute('imixDelete')
    @ImixDelete.setter
    def ImixDelete(self, value):
        self._set_attribute('imixDelete', value)

    @property
    def ImixDistribution(self):
        """
        Returns
        -------
        - str(bwpercentage | weight): Signifies the distribution list of IMIX.
        """
        return self._get_attribute('imixDistribution')
    @ImixDistribution.setter
    def ImixDistribution(self, value):
        self._set_attribute('imixDistribution', value)

    @property
    def ImixEnabled(self):
        """
        Returns
        -------
        - bool: If true, enables IMIX.
        """
        return self._get_attribute('imixEnabled')
    @ImixEnabled.setter
    def ImixEnabled(self, value):
        self._set_attribute('imixEnabled', value)

    @property
    def ImixTemplates(self):
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies the IMIX templates.
        """
        return self._get_attribute('imixTemplates')
    @ImixTemplates.setter
    def ImixTemplates(self, value):
        self._set_attribute('imixTemplates', value)

    @property
    def ImixTrafficType(self):
        """
        Returns
        -------
        - str: Signifies the traffic type of IMIX.
        """
        return self._get_attribute('imixTrafficType')
    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        self._set_attribute('imixTrafficType', value)

    @property
    def IncrementLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the incremented load unit.
        """
        return self._get_attribute('incrementLoadUnit')
    @IncrementLoadUnit.setter
    def IncrementLoadUnit(self, value):
        self._set_attribute('incrementLoadUnit', value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the initial binary load rate.
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
        - number: Signifies the initial combo load rate.
        """
        return self._get_attribute('initialComboLoadRate')
    @InitialComboLoadRate.setter
    def InitialComboLoadRate(self, value):
        self._set_attribute('initialComboLoadRate', value)

    @property
    def InitialIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the initial increment of load rate.
        """
        return self._get_attribute('initialIncrementLoadRate')
    @InitialIncrementLoadRate.setter
    def InitialIncrementLoadRate(self, value):
        self._set_attribute('initialIncrementLoadRate', value)

    @property
    def InitialStepLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the initial step load rate value.
        """
        return self._get_attribute('initialStepLoadRate')
    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        self._set_attribute('initialStepLoadRate', value)

    @property
    def Ipv4rate(self):
        """
        Returns
        -------
        - number: The rate at which IPv4 traffic is sent.
        """
        return self._get_attribute('ipv4rate')
    @Ipv4rate.setter
    def Ipv4rate(self, value):
        self._set_attribute('ipv4rate', value)

    @property
    def Ipv6rate(self):
        """
        Returns
        -------
        - number: The rate at which IPv6 traffic is sent.
        """
        return self._get_attribute('ipv6rate')
    @Ipv6rate.setter
    def Ipv6rate(self, value):
        self._set_attribute('ipv6rate', value)

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
        - str: Enter the Load Rate List.
        """
        return self._get_attribute('loadRateList')
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute('loadRateList', value)

    @property
    def LoadRateValue(self):
        """
        Returns
        -------
        - number: The value of the load rate.
        """
        return self._get_attribute('loadRateValue')
    @LoadRateValue.setter
    def LoadRateValue(self, value):
        self._set_attribute('loadRateValue', value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(fixed | random | unchanged): Type of load.
        """
        return self._get_attribute('loadType')
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute('loadType', value)

    @property
    def LoadUnit(self):
        """
        Returns
        -------
        - str: Signifies the load unit.
        """
        return self._get_attribute('loadUnit')
    @LoadUnit.setter
    def LoadUnit(self, value):
        self._set_attribute('loadUnit', value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum binary load rate.
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
        - number: Signifies the maximum combo load rate.
        """
        return self._get_attribute('maxComboLoadRate')
    @MaxComboLoadRate.setter
    def MaxComboLoadRate(self, value):
        self._set_attribute('maxComboLoadRate', value)

    @property
    def MaxFramesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute('maxFramesize')
    @MaxFramesize.setter
    def MaxFramesize(self, value):
        self._set_attribute('maxFramesize', value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: Signifies the maximum increment of frame size.
        """
        return self._get_attribute('maxIncrementFrameSize')
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute('maxIncrementFrameSize', value)

    @property
    def MaxIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum increment of load rate.
        """
        return self._get_attribute('maxIncrementLoadRate')
    @MaxIncrementLoadRate.setter
    def MaxIncrementLoadRate(self, value):
        self._set_attribute('maxIncrementLoadRate', value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: Signifies the maximum random frame size.
        """
        return self._get_attribute('maxRandomFrameSize')
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute('maxRandomFrameSize', value)

    @property
    def MaxRandomLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum random load rate.
        """
        return self._get_attribute('maxRandomLoadRate')
    @MaxRandomLoadRate.setter
    def MaxRandomLoadRate(self, value):
        self._set_attribute('maxRandomLoadRate', value)

    @property
    def MaxRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum rate.
        """
        return self._get_attribute('maxRate')
    @MaxRate.setter
    def MaxRate(self, value):
        self._set_attribute('maxRate', value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the maximum step load rate.
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
        - number: Signifies the minimum binary load rate.
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
        - number: Signifies the minimum combo load rate.
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
        - number: Signifies the Minimum fps rate.
        """
        return self._get_attribute('minFpsRate')
    @MinFpsRate.setter
    def MinFpsRate(self, value):
        self._set_attribute('minFpsRate', value)

    @property
    def MinFramesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute('minFramesize')
    @MinFramesize.setter
    def MinFramesize(self, value):
        self._set_attribute('minFramesize', value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: Signifies the minimum increment frame size.
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
        - number: Signifies the minimum kbps rate.
        """
        return self._get_attribute('minKbpsRate')
    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        self._set_attribute('minKbpsRate', value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: Signifies the minimum random frame size.
        """
        return self._get_attribute('minRandomFrameSize')
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute('minRandomFrameSize', value)

    @property
    def MinRandomLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the minimum random load rate.
        """
        return self._get_attribute('minRandomLoadRate')
    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        self._set_attribute('minRandomLoadRate', value)

    @property
    def MinRate(self):
        """
        Returns
        -------
        - number: Signifies the minimum rate.
        """
        return self._get_attribute('minRate')
    @MinRate.setter
    def MinRate(self, value):
        self._set_attribute('minRate', value)

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
        - number: The maximum rate percentage.
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
    def RandomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the random load unit value.
        """
        return self._get_attribute('randomLoadUnit')
    @RandomLoadUnit.setter
    def RandomLoadUnit(self, value):
        self._set_attribute('randomLoadUnit', value)

    @property
    def RateSelect(self):
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): Signifies the rate selected.
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
        - bool: If true, reports sequence error.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): Reports the throughput rate unit.
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
        - number: Specify the resolution of the iteration.
        """
        return self._get_attribute('resolution')
    @Resolution.setter
    def Resolution(self, value):
        self._set_attribute('resolution', value)

    @property
    def Runmode(self):
        """
        Returns
        -------
        - str(duration | noframes): Specifies the number of frames that IxNetwork sends from each port in running mode.
        """
        return self._get_attribute('runmode')
    @Runmode.setter
    def Runmode(self, value):
        self._set_attribute('runmode', value)

    @property
    def SaturationIteration(self):
        """
        Returns
        -------
        - number: The of iteration for saturation.
        """
        return self._get_attribute('saturationIteration')
    @SaturationIteration.setter
    def SaturationIteration(self, value):
        self._set_attribute('saturationIteration', value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: If true, staggers the start of the test.
        """
        return self._get_attribute('staggeredStart')
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute('staggeredStart', value)

    @property
    def StepComboLoadRate(self):
        """
        Returns
        -------
        - number: The combination step value of load rate.
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
        - str(% | frames): Signifies the step frame loss unit value.
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
        - number: Increments the step frame size.
        """
        return self._get_attribute('stepIncrementFrameSize')
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute('stepIncrementFrameSize', value)

    @property
    def StepIncrementLoadRate(self):
        """
        Returns
        -------
        - number: Signifies the incremented step load rate value.
        """
        return self._get_attribute('stepIncrementLoadRate')
    @StepIncrementLoadRate.setter
    def StepIncrementLoadRate(self, value):
        self._set_attribute('stepIncrementLoadRate', value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the step load unit value.
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
        - number: Signifies the step value of the load rate.
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
        - number: The step value of the tolerance level.
        """
        return self._get_attribute('stepTolerance')
    @StepTolerance.setter
    def StepTolerance(self, value):
        self._set_attribute('stepTolerance', value)

    @property
    def StopTestOnHighLoss(self):
        """
        Returns
        -------
        - number: It the stops the test on high loss.
        """
        return self._get_attribute('stopTestOnHighLoss')
    @StopTestOnHighLoss.setter
    def StopTestOnHighLoss(self, value):
        self._set_attribute('stopTestOnHighLoss', value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: The value set for the tolerance level.
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
        - str(burstyLoading | constantLoading): Signifies the type of traffic.
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
        - number: Signifies the transmission delay time.
        """
        return self._get_attribute('txDelay')
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute('txDelay', value)

    @property
    def UnchangedInitial(self):
        """
        Returns
        -------
        - str(False | True): Signifies the initial value that is unchanged.
        """
        return self._get_attribute('unchangedInitial')
    @UnchangedInitial.setter
    def UnchangedInitial(self, value):
        self._set_attribute('unchangedInitial', value)

    @property
    def UnchangedValueList(self):
        """
        Returns
        -------
        - str: Signifies the unchanged value list.
        """
        return self._get_attribute('unchangedValueList')
    @UnchangedValueList.setter
    def UnchangedValueList(self, value):
        self._set_attribute('unchangedValueList', value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - str: Signifies the use of percent offsets.
        """
        return self._get_attribute('usePercentOffsets')
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute('usePercentOffsets', value)

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
