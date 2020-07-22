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
    """It signifies the configuration of the test.
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
        'ComboBackoff': 'comboBackoff',
        'ComboFrameLossUnit': 'comboFrameLossUnit',
        'ComboLoadUnit': 'comboLoadUnit',
        'ComboResolution': 'comboResolution',
        'ComboTolerance': 'comboTolerance',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CountRandomLoadRate': 'countRandomLoadRate',
        'CustomLoadUnit': 'customLoadUnit',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'Duration': 'duration',
        'EnableBackoffIteration': 'enableBackoffIteration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableExtraIterations': 'enableExtraIterations',
        'EnableFastConvergence': 'enableFastConvergence',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableLayer2': 'enableLayer2',
        'EnableLeaveGroup': 'enableLeaveGroup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableMulticastQuerier': 'enableMulticastQuerier',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'EnableSaturationIteration': 'enableSaturationIteration',
        'EnableStopTestOnHighLoss': 'enableStopTestOnHighLoss',
        'ExtraIterationOffsets': 'extraIterationOffsets',
        'FastConvergence': 'fastConvergence',
        'FastConvergenceDuration': 'fastConvergenceDuration',
        'FastConvergenceThreshold': 'fastConvergenceThreshold',
        'FirstMulticastDestMACAddress': 'firstMulticastDestMACAddress',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameSizeMode': 'frameSizeMode',
        'FramesizeImixList': 'framesizeImixList',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'GenerateTrackingOptionAggregationFiles': 'generateTrackingOptionAggregationFiles',
        'GroupCapacityGreaterThan': 'groupCapacityGreaterThan',
        'GroupDistributionType': 'groupDistributionType',
        'IgmpV1Timeout': 'igmpV1Timeout',
        'IgmpVersion': 'igmpVersion',
        'Igmpv3MessageType': 'igmpv3MessageType',
        'Igmpv3SourceAddrList': 'igmpv3SourceAddrList',
        'ImixAdd': 'imixAdd',
        'ImixData': 'imixData',
        'ImixDataQoS': 'imixDataQoS',
        'ImixDelete': 'imixDelete',
        'ImixDistribution': 'imixDistribution',
        'ImixEnabled': 'imixEnabled',
        'ImixTemplates': 'imixTemplates',
        'ImixTrafficType': 'imixTrafficType',
        'IncMulticastDestMACAddress': 'incMulticastDestMACAddress',
        'IncPortMACAddress': 'incPortMACAddress',
        'IncrAddresses': 'incrAddresses',
        'IncrStep': 'incrStep',
        'IncrementLoadRate': 'incrementLoadRate',
        'IncrementLoadUnit': 'incrementLoadUnit',
        'InitialBinaryLoadRate': 'initialBinaryLoadRate',
        'InitialComboLoadRate': 'initialComboLoadRate',
        'InitialIncrementLoadRate': 'initialIncrementLoadRate',
        'InitialStepLoadRate': 'initialStepLoadRate',
        'Ipv4Address': 'ipv4Address',
        'Ipv6Address': 'ipv6Address',
        'IsIPv6': 'isIPv6',
        'IsMulticastAutomaticFrameData': 'isMulticastAutomaticFrameData',
        'IsNewMode': 'isNewMode',
        'JoinLeaveMultiplier': 'joinLeaveMultiplier',
        'JoinLeaveRate': 'joinLeaveRate',
        'JoinLeaveWaitTime': 'joinLeaveWaitTime',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LearnRateMac': 'learnRateMac',
        'LearnSendMac': 'learnSendMac',
        'LearnSendMacEnabled': 'learnSendMacEnabled',
        'LoadInitialRate': 'loadInitialRate',
        'LoadRateList': 'loadRateList',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxComboLoadRate': 'maxComboLoadRate',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxIncrementLoadRate': 'maxIncrementLoadRate',
        'MaxQuickSearchLoadRate': 'maxQuickSearchLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxRandomLoadRate': 'maxRandomLoadRate',
        'MaxStepLoadRate': 'maxStepLoadRate',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinComboLoadRate': 'minComboLoadRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinQuickSearchLoadRate': 'minQuickSearchLoadRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MinRandomLoadRate': 'minRandomLoadRate',
        'MixedClassMulticast': 'mixedClassMulticast',
        'MldVersion': 'mldVersion',
        'NumAddresses': 'numAddresses',
        'NumIterations': 'numIterations',
        'Numtrials': 'numtrials',
        'PercentMulticastFrames': 'percentMulticastFrames',
        'PercentUnicastFrames': 'percentUnicastFrames',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'PortMACAddress': 'portMACAddress',
        'ProtocolItem': 'protocolItem',
        'QuickBackoffIteration': 'quickBackoffIteration',
        'QuickEnableBackoffIteration': 'quickEnableBackoffIteration',
        'QuickEnableSaturationIteration': 'quickEnableSaturationIteration',
        'QuickSaturationIteration': 'quickSaturationIteration',
        'QuickSearchFrameLossUnit': 'quickSearchFrameLossUnit',
        'QuickSearchLoadUnit': 'quickSearchLoadUnit',
        'QuickSearchResolution': 'quickSearchResolution',
        'QuickSearchSearchType': 'quickSearchSearchType',
        'QuickSearchTolerance': 'quickSearchTolerance',
        'RandomLoadUnit': 'randomLoadUnit',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'RouterAlert': 'routerAlert',
        'SaturationIteration': 'saturationIteration',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'StepComboLoadRate': 'stepComboLoadRate',
        'StepFrameLossUnit': 'stepFrameLossUnit',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepIncrementLoadRate': 'stepIncrementLoadRate',
        'StepLoadUnit': 'stepLoadUnit',
        'StepStepLoadRate': 'stepStepLoadRate',
        'StepTolerance': 'stepTolerance',
        'StopTestOnHighLoss': 'stopTestOnHighLoss',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TestTrafficType': 'testTrafficType',
        'TrafficDistribution': 'trafficDistribution',
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
        - str(accumulated | distributed): Assigns the group type.
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
        - number: This enables the test to run an extra iteration for calculating the Backoff Latency.
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
        - bool: If true, enables bidirectional option.
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
        - number: Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
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
        - number: The number of packets that are sent in a burst.
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
        - str(% | frames): The frame loss unit for traffic in binary.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The combination of load units. Possible values include:
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
        - number: The combined resolution value.
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
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: If true, frame sizes are counted at random.
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
        - number: The amount of delay after every transmit.
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
        - bool: If true, enables back off iteration test.
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
        - bool: enableDataIntegrity
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
        - str: If true, more iterations are performed.
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
        - bool: If true, the test perform iterations using the fast convergence duration configured.
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
    def EnableLayer2(self):
        """
        Returns
        -------
        - bool: If true, enables Layer2 protocols.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLayer2'])
    @EnableLayer2.setter
    def EnableLayer2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLayer2'], value)

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
        - bool: If enabled, it shows the minimum frame size.
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
        - bool: Enable old statistics for reef.
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
        - bool: If true, SaturationIteration in enabled .
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
        - bool: The test stops in case of a high loss.
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
        - str: This enables the test to run an extra iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraIterationOffsets'])
    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraIterationOffsets'], value)

    @property
    def FastConvergence(self):
        """
        Returns
        -------
        - str: If true, enables fast convergence.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergence'])
    @FastConvergence.setter
    def FastConvergence(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergence'], value)

    @property
    def FastConvergenceDuration(self):
        """
        Returns
        -------
        - number: This enables the test to perform iterations using the fast convergence duration configured.
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
        - number: This enables the test to perform iterations using the fast convergence threshold configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'])
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'], value)

    @property
    def FirstMulticastDestMACAddress(self):
        """
        Returns
        -------
        - str: The first multicast destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstMulticastDestMACAddress'])
    @FirstMulticastDestMACAddress.setter
    def FirstMulticastDestMACAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstMulticastDestMACAddress'], value)

    @property
    def FloodedFramesEnabled(self):
        """
        Returns
        -------
        - bool: Show Flooded Frames
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
        - str(custom | fixed | increment | random): This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def FramesizeImixList(self):
        """
        Returns
        -------
        - str: The list of frame size to be used
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
        - list(str): The list of frame sizes.
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
        - bool: If true, enables the tracking option in aggregation files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'])
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'], value)

    @property
    def GroupCapacityGreaterThan(self):
        """
        Returns
        -------
        - number: The integer that distinguishes the group capacity that could be greater than the specified integer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupCapacityGreaterThan'])
    @GroupCapacityGreaterThan.setter
    def GroupCapacityGreaterThan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupCapacityGreaterThan'], value)

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
        - number: The IGMPv1 timeout value.
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
        - number: The igmp version .
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
    def ImixAdd(self):
        """
        Returns
        -------
        - str: Adds an imix data.
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
        - str: Displays the imix Data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixData'])
    @ImixData.setter
    def ImixData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixData'], value)

    @property
    def ImixDataQoS(self):
        """
        Returns
        -------
        - bool: Enables Imix Data QoS
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixDataQoS'])
    @ImixDataQoS.setter
    def ImixDataQoS(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixDataQoS'], value)

    @property
    def ImixDelete(self):
        """
        Returns
        -------
        - str: Deletes the imix data.
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
        - str(bwpercentage | weight): Specifies the imix distribution unit.
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
        - bool: If True, Enables the imix value.
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
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Specefies the imix templates.
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
        - str: Displays the imix traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixTrafficType'])
    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixTrafficType'], value)

    @property
    def IncMulticastDestMACAddress(self):
        """
        Returns
        -------
        - str: The incrementing multicast destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncMulticastDestMACAddress'])
    @IncMulticastDestMACAddress.setter
    def IncMulticastDestMACAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncMulticastDestMACAddress'], value)

    @property
    def IncPortMACAddress(self):
        """
        Returns
        -------
        - str: The incrementing MAC address of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncPortMACAddress'])
    @IncPortMACAddress.setter
    def IncPortMACAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncPortMACAddress'], value)

    @property
    def IncrAddresses(self):
        """
        Returns
        -------
        - number: The incremental address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrAddresses'])
    @IncrAddresses.setter
    def IncrAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrAddresses'], value)

    @property
    def IncrStep(self):
        """
        Returns
        -------
        - number: The option to increment step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrStep'])
    @IncrStep.setter
    def IncrStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrStep'], value)

    @property
    def IncrementLoadRate(self):
        """
        Returns
        -------
        - str: The incremental value of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementLoadRate'])
    @IncrementLoadRate.setter
    def IncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementLoadRate'], value)

    @property
    def IncrementLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The incremental value of the load unit.
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
        - number: Specifies the initial rate of the binary algorithm.
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
        - number: The initial combination value of the load rate .
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
        - number: The initial incremental value of the load rate.
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
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: The allocated IPv4 address for this interface.
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
        - str: The allocated IPv6address for this interface.
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
        - str: The allocated IPv6address for this interface.
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
        - str: The multicast automatic frame data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMulticastAutomaticFrameData'])
    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsMulticastAutomaticFrameData'], value)

    @property
    def IsNewMode(self):
        """
        Returns
        -------
        - bool: Is New Mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsNewMode'])
    @IsNewMode.setter
    def IsNewMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsNewMode'], value)

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
        - number: The join leave rate.
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
        - number: The wait time for join delay.
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
        - str(cutThrough | forwardingDelay | mef | storeForward): The type of latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LearnRateMac(self):
        """
        Returns
        -------
        - str: Rates learning frames to MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnRateMac'])
    @LearnRateMac.setter
    def LearnRateMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnRateMac'], value)

    @property
    def LearnSendMac(self):
        """
        Returns
        -------
        - str: Sends learning frames to MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnSendMac'])
    @LearnSendMac.setter
    def LearnSendMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnSendMac'], value)

    @property
    def LearnSendMacEnabled(self):
        """
        Returns
        -------
        - str: Send Mac learning
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnSendMacEnabled'])
    @LearnSendMacEnabled.setter
    def LearnSendMacEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnSendMacEnabled'], value)

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
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | combo | custom | increment | quickSearch | random | step): The type of the payload setting.
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
        - str: The mapping type.
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
        - number: The maximum value of the load rate Combo Load Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxComboLoadRate'])
    @MaxComboLoadRate.setter
    def MaxComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxComboLoadRate'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The integer that states the maximum amount to which the frame size can be incremented.
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
        - number: The maximum incremental value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementLoadRate'])
    @MaxIncrementLoadRate.setter
    def MaxIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementLoadRate'], value)

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
        - number: The integer that states the maximum random amount to which the frame size can be incremented.
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
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The integer that states the minimum amount to which the frame size can be incremented.
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
        - number: The integer that states the minimum random amount to which the frame size can be incremented.
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
        - number: The maximum random value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'])
    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'], value)

    @property
    def MixedClassMulticast(self):
        """
        Returns
        -------
        - str: The mixed multicast class.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MixedClassMulticast'])
    @MixedClassMulticast.setter
    def MixedClassMulticast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MixedClassMulticast'], value)

    @property
    def MldVersion(self):
        """
        Returns
        -------
        - number: The version of the MLD messages.
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
        - number: The integer value for the number of addresses.
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
        - number: The integer value for the number of iterations.
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
        - number: The integer value that states the number of trials permitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PercentMulticastFrames(self):
        """
        Returns
        -------
        - number: The percentage of multicast frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMulticastFrames'])
    @PercentMulticastFrames.setter
    def PercentMulticastFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentMulticastFrames'], value)

    @property
    def PercentUnicastFrames(self):
        """
        Returns
        -------
        - number: The percentage of unicast frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentUnicastFrames'])
    @PercentUnicastFrames.setter
    def PercentUnicastFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentUnicastFrames'], value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: Enable Delay Between Ports
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
    def PortMACAddress(self):
        """
        Returns
        -------
        - str: The MAC address of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortMACAddress'])
    @PortMACAddress.setter
    def PortMACAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortMACAddress'], value)

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
    def QuickBackoffIteration(self):
        """
        Returns
        -------
        - number: Sets the quicksearch backoff iteration
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickBackoffIteration'])
    @QuickBackoffIteration.setter
    def QuickBackoffIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickBackoffIteration'], value)

    @property
    def QuickEnableBackoffIteration(self):
        """
        Returns
        -------
        - bool: Enables the quick search backoff iteration
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickEnableBackoffIteration'])
    @QuickEnableBackoffIteration.setter
    def QuickEnableBackoffIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickEnableBackoffIteration'], value)

    @property
    def QuickEnableSaturationIteration(self):
        """
        Returns
        -------
        - bool: Enables the Quick Search saturation iteration
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickEnableSaturationIteration'])
    @QuickEnableSaturationIteration.setter
    def QuickEnableSaturationIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickEnableSaturationIteration'], value)

    @property
    def QuickSaturationIteration(self):
        """
        Returns
        -------
        - number: Sets the quick search saturation iteration
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSaturationIteration'])
    @QuickSaturationIteration.setter
    def QuickSaturationIteration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSaturationIteration'], value)

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
        - str(linear | perFlow | perPort | perTrafficItem): Sets the quick search type
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
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: If enabled, it reports sequence error.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The throughput rate unit.
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
        - bool: The router alert selected from the Hop-by-hop Options.
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
        - number: This enables the test to run an extra iteration for calculating the Saturation latency.
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
    def StepComboLoadRate(self):
        """
        Returns
        -------
        - number: The step value of combination load rate.
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
        - str(% | frames): The frame loss unit for traffic.
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
        - number: The step to increment the frame size.
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
        - number: The step incremental value of the load rate.
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
        - number: It stops test on high loss.
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
        - str: The traffic types supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: It signifies the test traffic type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTrafficType'])
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestTrafficType'], value)

    @property
    def TrafficDistribution(self):
        """
        Returns
        -------
        - str(mixed | multicast | unicast): Sets the traffic distribution type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficDistribution'])
    @TrafficDistribution.setter
    def TrafficDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficDistribution'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: the delay recorded in the transmit port.
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
        - str(False | True): The first value of an unchanged parameter.
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
        - str: If true, sets the offset value in percentage.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, ApplyMode=None, AssignGroupType=None, BackoffIteration=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountRandomFrameSize=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableLayer2=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergence=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FirstMulticastDestMACAddress=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, ImixAdd=None, ImixData=None, ImixDataQoS=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncMulticastDestMACAddress=None, IncPortMACAddress=None, IncrAddresses=None, IncrStep=None, IncrementLoadRate=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, IsNewMode=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LearnRateMac=None, LearnSendMac=None, LearnSendMacEnabled=None, LoadInitialRate=None, LoadRateList=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinIncrementFrameSize=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MinRandomLoadRate=None, MixedClassMulticast=None, MldVersion=None, NumAddresses=None, NumIterations=None, Numtrials=None, PercentMulticastFrames=None, PercentUnicastFrames=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortMACAddress=None, ProtocolItem=None, QuickBackoffIteration=None, QuickEnableBackoffIteration=None, QuickEnableSaturationIteration=None, QuickSaturationIteration=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, RandomLoadUnit=None, ReportSequenceError=None, ReportTputRateUnit=None, RouterAlert=None, SaturationIteration=None, ShowDetailedBinaryResults=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, SupportedTrafficTypes=None, TestTrafficType=None, TrafficDistribution=None, TxDelay=None, UnchangedInitial=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): Assigns the group type.
        - BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
        - BidirectionalOptionEnabled (bool): If true, enables bidirectional option.
        - BinaryBackoff (number): Specifies the percentage of binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit.
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - BinarySearchType (str(linear | perFlow | perPort | perTrafficItem)): The binary search type value.
        - BinaryTolerance (number): The binary tolerance level.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - ComboBackoff (number): The backoff combination of the test configuration.
        - ComboFrameLossUnit (str(% | frames)): The frame loss unit for traffic in binary.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The combination of load units. Possible values include:
        - ComboResolution (number): The combined resolution value.
        - ComboTolerance (number): The combined tolerance level.
        - CountRandomFrameSize (number): If true, frame sizes are counted at random.
        - CountRandomLoadRate (number): The random count of the load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): The amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableBackoffIteration (bool): If true, enables back off iteration test.
        - EnableDataIntegrity (bool): enableDataIntegrity
        - EnableExtraIterations (str): If true, more iterations are performed.
        - EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLayer2 (bool): If true, enables Layer2 protocols.
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If enabled, it shows the minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): Enable old statistics for reef.
        - EnableSaturationIteration (bool): If true, SaturationIteration in enabled .
        - EnableStopTestOnHighLoss (bool): The test stops in case of a high loss.
        - ExtraIterationOffsets (str): This enables the test to run an extra iteration.
        - FastConvergence (str): If true, enables fast convergence.
        - FastConvergenceDuration (number): This enables the test to perform iterations using the fast convergence duration configured.
        - FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
        - FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
        - FloodedFramesEnabled (bool): Show Flooded Frames
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameLossUnit (str): The frame loss unit.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.
        - FramesizeImixList (str): The list of frame size to be used
        - FramesizeList (list(str)): The list of frame sizes.
        - Gap (number): It signifies the gap value for the protocol.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - GroupCapacityGreaterThan (number): The integer that distinguishes the group capacity that could be greater than the specified integer.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The group distribution type.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): The igmp version .
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - ImixAdd (str): Adds an imix data.
        - ImixData (str): Displays the imix Data.
        - ImixDataQoS (bool): Enables Imix Data QoS
        - ImixDelete (str): Deletes the imix data.
        - ImixDistribution (str(bwpercentage | weight)): Specifies the imix distribution unit.
        - ImixEnabled (bool): If True, Enables the imix value.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Specefies the imix templates.
        - ImixTrafficType (str): Displays the imix traffic type.
        - IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
        - IncPortMACAddress (str): The incrementing MAC address of the port.
        - IncrAddresses (number): The incremental address.
        - IncrStep (number): The option to increment step value.
        - IncrementLoadRate (str): The incremental value of load rate.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The incremental value of the load unit.
        - InitialBinaryLoadRate (number): Specifies the initial rate of the binary algorithm.
        - InitialComboLoadRate (number): The initial combination value of the load rate .
        - InitialIncrementLoadRate (number): The initial incremental value of the load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - Ipv4Address (str): The allocated IPv4 address for this interface.
        - Ipv6Address (str): The allocated IPv6address for this interface.
        - IsIPv6 (str): The allocated IPv6address for this interface.
        - IsMulticastAutomaticFrameData (str): The multicast automatic frame data.
        - IsNewMode (bool): Is New Mode
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join leave rate.
        - JoinLeaveWaitTime (number): The wait time for join delay.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)): The type of latency.
        - LearnRateMac (str): Rates learning frames to MAC address.
        - LearnSendMac (str): Sends learning frames to MAC address.
        - LearnSendMacEnabled (str): Send Mac learning
        - LoadInitialRate (number): The initial rate of the load.
        - LoadRateList (str): Enters the Load Rate List.
        - LoadType (str(binary | combo | custom | increment | quickSearch | random | step)): The type of the payload setting.
        - MapType (str): The mapping type.
        - MaxBinaryLoadRate (number): Specifies the maximum rate of the binary algorithm.
        - MaxComboLoadRate (number): The maximum value of the load rate Combo Load Type.
        - MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
        - MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
        - MaxRandomLoadRate (number): The maximum random value of the load rate.
        - MaxStepLoadRate (number): The maximum step value of the load rate.
        - MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
        - MinComboLoadRate (number): The minimum combination load rate.
        - MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
        - MinRandomLoadRate (number): The maximum random value of the load rate.
        - MixedClassMulticast (str): The mixed multicast class.
        - MldVersion (number): The version of the MLD messages.
        - NumAddresses (number): The integer value for the number of addresses.
        - NumIterations (number): The integer value for the number of iterations.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PercentMulticastFrames (number): The percentage of multicast frames.
        - PercentUnicastFrames (number): The percentage of unicast frames.
        - PortDelayEnabled (bool): Enable Delay Between Ports
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - PortMACAddress (str): The MAC address of the port.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - QuickBackoffIteration (number): Sets the quicksearch backoff iteration
        - QuickEnableBackoffIteration (bool): Enables the quick search backoff iteration
        - QuickEnableSaturationIteration (bool): Enables the Quick Search saturation iteration
        - QuickSaturationIteration (number): Sets the quick search saturation iteration
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear | perFlow | perPort | perTrafficItem)): Sets the quick search type
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit.
        - ReportSequenceError (bool): If enabled, it reports sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The throughput rate unit.
        - RouterAlert (bool): The router alert selected from the Hop-by-hop Options.
        - SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepComboLoadRate (number): The step value of combination load rate.
        - StepFrameLossUnit (str(% | frames)): The frame loss unit for traffic.
        - StepIncrementFrameSize (number): The step to increment the frame size.
        - StepIncrementLoadRate (number): The step incremental value of the load rate.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTolerance (number): The step value of the tolerance level.
        - StopTestOnHighLoss (number): It stops test on high loss.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TrafficDistribution (str(mixed | multicast | unicast)): Sets the traffic distribution type
        - TxDelay (number): the delay recorded in the transmit port.
        - UnchangedInitial (str(False | True)): The first value of an unchanged parameter.
        - UsePercentOffsets (str): If true, sets the offset value in percentage.

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
