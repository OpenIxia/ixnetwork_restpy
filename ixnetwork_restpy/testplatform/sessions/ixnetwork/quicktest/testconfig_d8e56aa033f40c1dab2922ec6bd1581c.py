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
    """The test configuration.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'ApplyMode': 'applyMode',
        'AssignGroupType': 'assignGroupType',
        'BackoffIteration': 'backoffIteration',
        'BidirectionalOptionEnabled': 'bidirectionalOptionEnabled',
        'BinaryBackoff': 'binaryBackoff',
        'BinaryFrameLossUnit': 'binaryFrameLossUnit',
        'BinaryLoadUnit': 'binaryLoadUnit',
        'BinaryResolution': 'binaryResolution',
        'BinarySearchType': 'binarySearchType',
        'BinaryTolerance': 'binaryTolerance',
        'BurstSize': 'burstSize',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'Duration': 'duration',
        'EnableBackoffIteration': 'enableBackoffIteration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableExtraIterations': 'enableExtraIterations',
        'EnableFastConvergence': 'enableFastConvergence',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableLeaveGroup': 'enableLeaveGroup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableMulticastQuerier': 'enableMulticastQuerier',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'EnableSaturationIteration': 'enableSaturationIteration',
        'EnableStopTestOnHighLoss': 'enableStopTestOnHighLoss',
        'ExtraIterationOffsets': 'extraIterationOffsets',
        'FastConvergenceDuration': 'fastConvergenceDuration',
        'FastConvergenceThreshold': 'fastConvergenceThreshold',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameSizeMode': 'frameSizeMode',
        'FramelossPercentValue': 'framelossPercentValue',
        'FramesPerBurstGap': 'framesPerBurstGap',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'GroupDistributionType': 'groupDistributionType',
        'IgmpV1Timeout': 'igmpV1Timeout',
        'IgmpVersion': 'igmpVersion',
        'Igmpv3MessageType': 'igmpv3MessageType',
        'Igmpv3SourceAddrList': 'igmpv3SourceAddrList',
        'IncrAddresses': 'incrAddresses',
        'InitialBinaryLoadRate': 'initialBinaryLoadRate',
        'InitialRate': 'initialRate',
        'InitialStepLoadRate': 'initialStepLoadRate',
        'Ipv4Address': 'ipv4Address',
        'Ipv6Address': 'ipv6Address',
        'IsIPv6': 'isIPv6',
        'IsMulticastAutomaticFrameData': 'isMulticastAutomaticFrameData',
        'JoinLeaveMultiplier': 'joinLeaveMultiplier',
        'JoinLeaveRate': 'joinLeaveRate',
        'JoinLeaveWaitTime': 'joinLeaveWaitTime',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LoadInitialRate': 'loadInitialRate',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxQuickSearchLoadRate': 'maxQuickSearchLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxStepLoadRate': 'maxStepLoadRate',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinQuickSearchLoadRate': 'minQuickSearchLoadRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MldVersion': 'mldVersion',
        'NumAddresses': 'numAddresses',
        'NumIterations': 'numIterations',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'QuickSearchFrameLossUnit': 'quickSearchFrameLossUnit',
        'QuickSearchLoadUnit': 'quickSearchLoadUnit',
        'QuickSearchResolution': 'quickSearchResolution',
        'QuickSearchSearchType': 'quickSearchSearchType',
        'QuickSearchTolerance': 'quickSearchTolerance',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'RouterAlert': 'routerAlert',
        'SaturationIteration': 'saturationIteration',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'StepFrameLossUnit': 'stepFrameLossUnit',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepLoadUnit': 'stepLoadUnit',
        'StepStepLoadRate': 'stepStepLoadRate',
        'StepTolerance': 'stepTolerance',
        'StopTestOnHighLoss': 'stopTestOnHighLoss',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TestMapType': 'testMapType',
        'TestTrafficType': 'testTrafficType',
        'TxDelay': 'txDelay',
        'UnchangedInitial': 'unchangedInitial',
        'UsePercentOffsets': 'usePercentOffsets',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def ApplyMode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyMode'])
    @ApplyMode.setter
    def ApplyMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyMode'], value)

    @property
    def AssignGroupType(self):
        """
        Returns
        -------
        - str(accumulated | distributed): The assigned group type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AssignGroupType'])
    @AssignGroupType.setter
    def AssignGroupType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AssignGroupType'], value)

    @property
    def BackoffIteration(self):
        """
        Returns
        -------
        - number: IF true, the iteration is backed off.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackoffIteration'])
    @BackoffIteration.setter
    def BackoffIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackoffIteration'], value)

    @property
    def BidirectionalOptionEnabled(self):
        """
        Returns
        -------
        - bool: if true, the bidirectional option is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'])
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'], value)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: The binary backoff.
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
        - str(% | frames): The binary frame loss unit.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The binary load unit.
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
        - number: The binary resolution.
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
        - str(linear): The binary search type.
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
        - number: The binary tolerance.
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
        - number: The burst size.
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
        - bool: The calculated jitter.
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
        - bool: The latency is calculated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: if true, the random frame size is counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: The delay after transmit of test config.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The test configuration duration.
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
        - bool: If true, the back off iteration is enabled.
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
        - bool: If true, data integrity is enabled.
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
        - bool: If true, extra iterations are enabled.
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
        - bool: If true, fast convergence is enabled.
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
    def EnableLeaveGroup(self):
        """
        Returns
        -------
        - bool: If true, the leave group is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLeaveGroup'])
    @EnableLeaveGroup.setter
    def EnableLeaveGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLeaveGroup'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true,the minimum frame size is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableMulticastQuerier(self):
        """
        Returns
        -------
        - bool: Enable Multicast Querier Settings
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMulticastQuerier'])
    @EnableMulticastQuerier.setter
    def EnableMulticastQuerier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMulticastQuerier'], value)

    @property
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: If true, the old stats for reef is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'])
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'], value)

    @property
    def EnableSaturationIteration(self):
        """
        Returns
        -------
        - bool: If true, the saturation iteration us enabled.
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
        - bool: If true, the test is stopped on high loss.
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
        - str: The extra iteration offsets.
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
        - number: The fast convergence duration.
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
        - number: The fast convergence threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'])
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'], value)

    @property
    def FloodedFramesEnabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the flooded frames statistics
        """
        return self._get_attribute(self._SDM_ATT_MAP['FloodedFramesEnabled'])
    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FloodedFramesEnabled'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: If true, the test configuration is forcefully regenerated.
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
        - str: The frame loss unit.
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
        - str(custom | fixed | increment | random): The frame size mode of test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def FramelossPercentValue(self):
        """
        Returns
        -------
        - number: The frame loss percentage value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramelossPercentValue'])
    @FramelossPercentValue.setter
    def FramelossPercentValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramelossPercentValue'], value)

    @property
    def FramesPerBurstGap(self):
        """
        Returns
        -------
        - number: The frames per burst gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'])
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'], value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): The frame size list of the test configuration.
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
        - number: The test configuration gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def GroupDistributionType(self):
        """
        Returns
        -------
        - str(acrossHosts | acrossPorts): The group distribution type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupDistributionType'])
    @GroupDistributionType.setter
    def GroupDistributionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupDistributionType'], value)

    @property
    def IgmpV1Timeout(self):
        """
        Returns
        -------
        - number: The igmp V1 timeout.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IgmpV1Timeout'])
    @IgmpV1Timeout.setter
    def IgmpV1Timeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IgmpV1Timeout'], value)

    @property
    def IgmpVersion(self):
        """
        Returns
        -------
        - number: The igmp version of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IgmpVersion'])
    @IgmpVersion.setter
    def IgmpVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IgmpVersion'], value)

    @property
    def Igmpv3MessageType(self):
        """
        Returns
        -------
        - str(exclude | include): It gives details about the igmpv3 message type in the test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Igmpv3MessageType'])
    @Igmpv3MessageType.setter
    def Igmpv3MessageType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Igmpv3MessageType'], value)

    @property
    def Igmpv3SourceAddrList(self):
        """
        Returns
        -------
        - str: It gives details about the igmpv3 source address list in the test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Igmpv3SourceAddrList'])
    @Igmpv3SourceAddrList.setter
    def Igmpv3SourceAddrList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Igmpv3SourceAddrList'], value)

    @property
    def IncrAddresses(self):
        """
        Returns
        -------
        - number: The incremented address of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrAddresses'])
    @IncrAddresses.setter
    def IncrAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrAddresses'], value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'])
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'], value)

    @property
    def InitialRate(self):
        """
        Returns
        -------
        - str: The initial rate of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialRate'])
    @InitialRate.setter
    def InitialRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialRate'], value)

    @property
    def InitialStepLoadRate(self):
        """
        Returns
        -------
        - number: The initial step of the load type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialStepLoadRate'])
    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialStepLoadRate'], value)

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: The IPV4 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Address'])
    @Ipv4Address.setter
    def Ipv4Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Address'], value)

    @property
    def Ipv6Address(self):
        """
        Returns
        -------
        - str: The IPV6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Address'])
    @Ipv6Address.setter
    def Ipv6Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Address'], value)

    @property
    def IsIPv6(self):
        """
        Returns
        -------
        - str: The ipv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsIPv6'])
    @IsIPv6.setter
    def IsIPv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsIPv6'], value)

    @property
    def IsMulticastAutomaticFrameData(self):
        """
        Returns
        -------
        - str: The Multicast automatic frame data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMulticastAutomaticFrameData'])
    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsMulticastAutomaticFrameData'], value)

    @property
    def JoinLeaveMultiplier(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveMultiplier'])
    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveMultiplier'], value)

    @property
    def JoinLeaveRate(self):
        """
        Returns
        -------
        - number: The join and leave rate of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveRate'])
    @JoinLeaveRate.setter
    def JoinLeaveRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveRate'], value)

    @property
    def JoinLeaveWaitTime(self):
        """
        Returns
        -------
        - number: The join and leave wait time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveWaitTime'])
    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveWaitTime'], value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics
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
        - bool: Enables the latency bins statistics
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
        - str(cutThrough | storeForward): The latency type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadInitialRate(self):
        """
        Returns
        -------
        - number: The initial rate of the load.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadInitialRate'])
    @LoadInitialRate.setter
    def LoadInitialRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadInitialRate'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | quickSearch | step): The load type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: The map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The maximum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'])
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The maximum frame size incrememnt.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: Sets the maximum QuickSearch load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxQuickSearchLoadRate'])
    @MaxQuickSearchLoadRate.setter
    def MaxQuickSearchLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxQuickSearchLoadRate'], value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The maximum random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: The maximum step of the load rate.
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
        - number: The minimum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'])
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum frame size increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: Sets the minum Quick Search load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinQuickSearchLoadRate'])
    @MinQuickSearchLoadRate.setter
    def MinQuickSearchLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinQuickSearchLoadRate'], value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The minimum random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def MldVersion(self):
        """
        Returns
        -------
        - number: The mld version of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MldVersion'])
    @MldVersion.setter
    def MldVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MldVersion'], value)

    @property
    def NumAddresses(self):
        """
        Returns
        -------
        - number: The number of addresses of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumAddresses'])
    @NumAddresses.setter
    def NumAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumAddresses'], value)

    @property
    def NumIterations(self):
        """
        Returns
        -------
        - number: The number of iterations.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumIterations'])
    @NumIterations.setter
    def NumIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumIterations'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number of trials for the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

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
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured
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
        - number: Sets the port delay value
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
    def QuickSearchFrameLossUnit(self):
        """
        Returns
        -------
        - str(%): Sets the quick search frame loss unit
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchFrameLossUnit'])
    @QuickSearchFrameLossUnit.setter
    def QuickSearchFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchFrameLossUnit'], value)

    @property
    def QuickSearchLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Sets the quick search load unit
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchLoadUnit'])
    @QuickSearchLoadUnit.setter
    def QuickSearchLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchLoadUnit'], value)

    @property
    def QuickSearchResolution(self):
        """
        Returns
        -------
        - number: Sets the quick search resolution
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchResolution'])
    @QuickSearchResolution.setter
    def QuickSearchResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchResolution'], value)

    @property
    def QuickSearchSearchType(self):
        """
        Returns
        -------
        - str(linear): Sets the quick search type
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchSearchType'])
    @QuickSearchSearchType.setter
    def QuickSearchSearchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchSearchType'], value)

    @property
    def QuickSearchTolerance(self):
        """
        Returns
        -------
        - number: Sets the quick search tolerance
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchTolerance'])
    @QuickSearchTolerance.setter
    def QuickSearchTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchTolerance'], value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: The report of sequence error.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The report throughput rate unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'])
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'], value)

    @property
    def RouterAlert(self):
        """
        Returns
        -------
        - bool: The router alert.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterAlert'])
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterAlert'], value)

    @property
    def SaturationIteration(self):
        """
        Returns
        -------
        - number: The saturation iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SaturationIteration'])
    @SaturationIteration.setter
    def SaturationIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SaturationIteration'], value)

    @property
    def ShowDetailedBinaryResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'])
    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'], value)

    @property
    def StepFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The step frame loss unit.
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
        - number: The step increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The step load unit.
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
        - number: The step of the step load rate.
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
        - number: The step tolerance.
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
        - number: If true, the test is stopped at high loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StopTestOnHighLoss'])
    @StopTestOnHighLoss.setter
    def StopTestOnHighLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StopTestOnHighLoss'], value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The supported traffic types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def TestMapType(self):
        """
        Returns
        -------
        - str(fullymesh | one2many): The test map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestMapType'])
    @TestMapType.setter
    def TestMapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestMapType'], value)

    @property
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: The test traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTrafficType'])
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestTrafficType'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: The transmission delay.
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
        - str(False | True): If true, the initial is unchanged.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnchangedInitial'])
    @UnchangedInitial.setter
    def UnchangedInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnchangedInitial'], value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - str: The use percent offsets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, ApplyMode=None, AssignGroupType=None, BackoffIteration=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, CountRandomFrameSize=None, DelayAfterTransmit=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramelossPercentValue=None, FramesPerBurstGap=None, FramesizeList=None, Gap=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, InitialBinaryLoadRate=None, InitialRate=None, InitialStepLoadRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadInitialRate=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxIncrementFrameSize=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinIncrementFrameSize=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MldVersion=None, NumAddresses=None, NumIterations=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, ReportSequenceError=None, ReportTputRateUnit=None, RouterAlert=None, SaturationIteration=None, ShowDetailedBinaryResults=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, SupportedTrafficTypes=None, TestMapType=None, TestTrafficType=None, TxDelay=None, UnchangedInitial=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The assigned group type.
        - BackoffIteration (number): IF true, the iteration is backed off.
        - BidirectionalOptionEnabled (bool): if true, the bidirectional option is enabled.
        - BinaryBackoff (number): The binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit.
        - BinaryResolution (number): The binary resolution.
        - BinarySearchType (str(linear)): The binary search type.
        - BinaryTolerance (number): The binary tolerance.
        - BurstSize (number): The burst size.
        - CalculateJitter (bool): The calculated jitter.
        - CalculateLatency (bool): The latency is calculated.
        - CountRandomFrameSize (number): if true, the random frame size is counted.
        - DelayAfterTransmit (number): The delay after transmit of test config.
        - Duration (number): The test configuration duration.
        - EnableBackoffIteration (bool): If true, the back off iteration is enabled.
        - EnableDataIntegrity (bool): If true, data integrity is enabled.
        - EnableExtraIterations (bool): If true, extra iterations are enabled.
        - EnableFastConvergence (bool): If true, fast convergence is enabled.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If true,the minimum frame size is enabled.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): If true, the old stats for reef is enabled.
        - EnableSaturationIteration (bool): If true, the saturation iteration us enabled.
        - EnableStopTestOnHighLoss (bool): If true, the test is stopped on high loss.
        - ExtraIterationOffsets (str): The extra iteration offsets.
        - FastConvergenceDuration (number): The fast convergence duration.
        - FastConvergenceThreshold (number): The fast convergence threshold.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): If true, the test configuration is forcefully regenerated.
        - FrameLossUnit (str): The frame loss unit.
        - FrameSizeMode (str(custom | fixed | increment | random)): The frame size mode of test configuration.
        - FramelossPercentValue (number): The frame loss percentage value.
        - FramesPerBurstGap (number): The frames per burst gap.
        - FramesizeList (list(str)): The frame size list of the test configuration.
        - Gap (number): The test configuration gap.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The group distribution type.
        - IgmpV1Timeout (number): The igmp V1 timeout.
        - IgmpVersion (number): The igmp version of the test configuration.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (number): The incremented address of the test configuration.
        - InitialBinaryLoadRate (number): The initial binary load rate.
        - InitialRate (str): The initial rate of the test configuration.
        - InitialStepLoadRate (number): The initial step of the load type.
        - Ipv4Address (str): The IPV4 address.
        - Ipv6Address (str): The IPV6 address.
        - IsIPv6 (str): The ipv6 address.
        - IsMulticastAutomaticFrameData (str): The Multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join and leave rate of the test configuration.
        - JoinLeaveWaitTime (number): The join and leave wait time.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The latency type.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadType (str(binary | quickSearch | step)): The load type.
        - MapType (str): The map type.
        - MaxBinaryLoadRate (number): The maximum binary load rate.
        - MaxIncrementFrameSize (number): The maximum frame size incrememnt.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): The maximum random frame size.
        - MaxStepLoadRate (number): The maximum step of the load rate.
        - MinBinaryLoadRate (number): The minimum binary load rate.
        - MinIncrementFrameSize (number): The minimum frame size increment.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The minimum random frame size.
        - MldVersion (number): The mld version of the test configuration.
        - NumAddresses (number): The number of addresses of the test configuration.
        - NumIterations (number): The number of iterations.
        - Numtrials (number): The number of trials for the test configuration.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear)): Sets the quick search type
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - ReportSequenceError (bool): The report of sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The report throughput rate unit.
        - RouterAlert (bool): The router alert.
        - SaturationIteration (number): The saturation iteration.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepFrameLossUnit (str(% | frames)): The step frame loss unit.
        - StepIncrementFrameSize (number): The step increment frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The step load unit.
        - StepStepLoadRate (number): The step of the step load rate.
        - StepTolerance (number): The step tolerance.
        - StopTestOnHighLoss (number): If true, the test is stopped at high loss.
        - SupportedTrafficTypes (str): The supported traffic types.
        - TestMapType (str(fullymesh | one2many)): The test map type.
        - TestTrafficType (str): The test traffic type.
        - TxDelay (number): The transmission delay.
        - UnchangedInitial (str(False | True)): If true, the initial is unchanged.
        - UsePercentOffsets (str): The use percent offsets.

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
