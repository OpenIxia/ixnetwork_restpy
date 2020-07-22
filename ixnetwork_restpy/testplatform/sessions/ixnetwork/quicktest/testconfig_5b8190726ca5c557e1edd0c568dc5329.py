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
        'BinaryTiLoss': 'binaryTiLoss',
        'BinaryTolerance': 'binaryTolerance',
        'Binary_delay_enableAccLoss': 'binary_delay_enableAccLoss',
        'Binary_delay_modeAccLoss': 'binary_delay_modeAccLoss',
        'Binary_delay_scaleAccLoss': 'binary_delay_scaleAccLoss',
        'Binary_delay_thresholdAccLoss': 'binary_delay_thresholdAccLoss',
        'Binary_flooded_enableAccLoss': 'binary_flooded_enableAccLoss',
        'Binary_flooded_thresholdAccLoss': 'binary_flooded_thresholdAccLoss',
        'Binary_integrity_enableAccLoss': 'binary_integrity_enableAccLoss',
        'Binary_integrity_thresholdAccLoss': 'binary_integrity_thresholdAccLoss',
        'Binary_latency_enableAccLoss': 'binary_latency_enableAccLoss',
        'Binary_latency_modeAccLoss': 'binary_latency_modeAccLoss',
        'Binary_latency_scaleAccLoss': 'binary_latency_scaleAccLoss',
        'Binary_latency_thresholdAccLoss': 'binary_latency_thresholdAccLoss',
        'Binary_seq_enableAccLoss': 'binary_seq_enableAccLoss',
        'Binary_seq_modeAccLoss': 'binary_seq_modeAccLoss',
        'Binary_seq_thresholdAccLoss': 'binary_seq_thresholdAccLoss',
        'BurstSize': 'burstSize',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'ComboBackoff': 'comboBackoff',
        'ComboFrameLossUnit': 'comboFrameLossUnit',
        'ComboLoadUnit': 'comboLoadUnit',
        'ComboResolution': 'comboResolution',
        'ComboTiLoss': 'comboTiLoss',
        'ComboTolerance': 'comboTolerance',
        'Combo_delay_enableAccLoss': 'combo_delay_enableAccLoss',
        'Combo_delay_modeAccLoss': 'combo_delay_modeAccLoss',
        'Combo_delay_scaleAccLoss': 'combo_delay_scaleAccLoss',
        'Combo_delay_thresholdAccLoss': 'combo_delay_thresholdAccLoss',
        'Combo_flooded_enableAccLoss': 'combo_flooded_enableAccLoss',
        'Combo_flooded_thresholdAccLoss': 'combo_flooded_thresholdAccLoss',
        'Combo_integrity_enableAccLoss': 'combo_integrity_enableAccLoss',
        'Combo_integrity_thresholdAccLoss': 'combo_integrity_thresholdAccLoss',
        'Combo_latency_enableAccLoss': 'combo_latency_enableAccLoss',
        'Combo_latency_modeAccLoss': 'combo_latency_modeAccLoss',
        'Combo_latency_scaleAccLoss': 'combo_latency_scaleAccLoss',
        'Combo_latency_thresholdAccLoss': 'combo_latency_thresholdAccLoss',
        'Combo_seq_enableAccLoss': 'combo_seq_enableAccLoss',
        'Combo_seq_modeAccLoss': 'combo_seq_modeAccLoss',
        'Combo_seq_thresholdAccLoss': 'combo_seq_thresholdAccLoss',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CountRandomIpRatio': 'countRandomIpRatio',
        'CountRandomLoadRate': 'countRandomLoadRate',
        'CustomLoadUnit': 'customLoadUnit',
        'CustomTiLoss': 'customTiLoss',
        'Custom_binary_delay_enableAccLoss': 'custom_binary_delay_enableAccLoss',
        'Custom_binary_delay_modeAccLoss': 'custom_binary_delay_modeAccLoss',
        'Custom_binary_delay_scaleAccLoss': 'custom_binary_delay_scaleAccLoss',
        'Custom_binary_delay_thresholdAccLoss': 'custom_binary_delay_thresholdAccLoss',
        'Custom_binary_flooded_enableAccLoss': 'custom_binary_flooded_enableAccLoss',
        'Custom_binary_flooded_thresholdAccLoss': 'custom_binary_flooded_thresholdAccLoss',
        'Custom_binary_integrity_enableAccLoss': 'custom_binary_integrity_enableAccLoss',
        'Custom_binary_integrity_thresholdAccLoss': 'custom_binary_integrity_thresholdAccLoss',
        'Custom_binary_latency_enableAccLoss': 'custom_binary_latency_enableAccLoss',
        'Custom_binary_latency_modeAccLoss': 'custom_binary_latency_modeAccLoss',
        'Custom_binary_latency_scaleAccLoss': 'custom_binary_latency_scaleAccLoss',
        'Custom_binary_latency_thresholdAccLoss': 'custom_binary_latency_thresholdAccLoss',
        'Custom_binary_peak_Backoff': 'custom_binary_peak_Backoff',
        'Custom_binary_peak_FrameLossUnit': 'custom_binary_peak_FrameLossUnit',
        'Custom_binary_peak_Resolution': 'custom_binary_peak_Resolution',
        'Custom_binary_peak_Tolerance': 'custom_binary_peak_Tolerance',
        'Custom_binary_peak_initialValue': 'custom_binary_peak_initialValue',
        'Custom_binary_peak_maxValue': 'custom_binary_peak_maxValue',
        'Custom_binary_peak_minValue': 'custom_binary_peak_minValue',
        'Custom_binary_seq_enableAccLoss': 'custom_binary_seq_enableAccLoss',
        'Custom_binary_seq_modeAccLoss': 'custom_binary_seq_modeAccLoss',
        'Custom_binary_seq_thresholdAccLoss': 'custom_binary_seq_thresholdAccLoss',
        'Custom_peak_loadType': 'custom_peak_loadType',
        'Custom_step_delay_enableAccLoss': 'custom_step_delay_enableAccLoss',
        'Custom_step_delay_modeAccLoss': 'custom_step_delay_modeAccLoss',
        'Custom_step_delay_scaleAccLoss': 'custom_step_delay_scaleAccLoss',
        'Custom_step_delay_thresholdAccLoss': 'custom_step_delay_thresholdAccLoss',
        'Custom_step_flooded_enableAccLoss': 'custom_step_flooded_enableAccLoss',
        'Custom_step_flooded_thresholdAccLoss': 'custom_step_flooded_thresholdAccLoss',
        'Custom_step_integrity_enableAccLoss': 'custom_step_integrity_enableAccLoss',
        'Custom_step_integrity_thresholdAccLoss': 'custom_step_integrity_thresholdAccLoss',
        'Custom_step_latency_enableAccLoss': 'custom_step_latency_enableAccLoss',
        'Custom_step_latency_modeAccLoss': 'custom_step_latency_modeAccLoss',
        'Custom_step_latency_scaleAccLoss': 'custom_step_latency_scaleAccLoss',
        'Custom_step_latency_thresholdAccLoss': 'custom_step_latency_thresholdAccLoss',
        'Custom_step_peak_FrameLossUnit': 'custom_step_peak_FrameLossUnit',
        'Custom_step_peak_initialValue': 'custom_step_peak_initialValue',
        'Custom_step_peak_maxValue': 'custom_step_peak_maxValue',
        'Custom_step_peak_stepTolerance': 'custom_step_peak_stepTolerance',
        'Custom_step_peak_stepValue': 'custom_step_peak_stepValue',
        'Custom_step_seq_enableAccLoss': 'custom_step_seq_enableAccLoss',
        'Custom_step_seq_modeAccLoss': 'custom_step_seq_modeAccLoss',
        'Custom_step_seq_thresholdAccLoss': 'custom_step_seq_thresholdAccLoss',
        'CustompeakvalueList': 'custompeakvalueList',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DetailedResultsEnabled': 'detailedResultsEnabled',
        'Duration': 'duration',
        'EnableBackoffIteration': 'enableBackoffIteration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableExtraIterations': 'enableExtraIterations',
        'EnableExtraRetriesOnLoss': 'enableExtraRetriesOnLoss',
        'EnableFastConvergence': 'enableFastConvergence',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'EnableSaturationIteration': 'enableSaturationIteration',
        'EnableStopTestOnHighLoss': 'enableStopTestOnHighLoss',
        'ExtraIterationOffsets': 'extraIterationOffsets',
        'ExtraRetriesOnLoss': 'extraRetriesOnLoss',
        'FastConvergenceDuration': 'fastConvergenceDuration',
        'FastConvergenceThreshold': 'fastConvergenceThreshold',
        'FixedLoadUnit': 'fixedLoadUnit',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameOrderingTemp': 'frameOrderingTemp',
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
        'IpRatioMode': 'ipRatioMode',
        'Ipv4RatioList': 'ipv4RatioList',
        'Ipv4rate': 'ipv4rate',
        'Ipv6RatioList': 'ipv6RatioList',
        'Ipv6rate': 'ipv6rate',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LoadRateList': 'loadRateList',
        'LoadRateValue': 'loadRateValue',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxComboLoadRate': 'maxComboLoadRate',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxIncrementIpv4Ratio': 'maxIncrementIpv4Ratio',
        'MaxIncrementIpv6Ratio': 'maxIncrementIpv6Ratio',
        'MaxIncrementLoadRate': 'maxIncrementLoadRate',
        'MaxQuickSearchLoadRate': 'maxQuickSearchLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxRandomIpv4Ratio': 'maxRandomIpv4Ratio',
        'MaxRandomIpv6Ratio': 'maxRandomIpv6Ratio',
        'MaxRandomLoadRate': 'maxRandomLoadRate',
        'MaxStepLoadRate': 'maxStepLoadRate',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinComboLoadRate': 'minComboLoadRate',
        'MinFpsRate': 'minFpsRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinIncrementIpv4Ratio': 'minIncrementIpv4Ratio',
        'MinIncrementIpv6Ratio': 'minIncrementIpv6Ratio',
        'MinKbpsRate': 'minKbpsRate',
        'MinQuickSearchLoadRate': 'minQuickSearchLoadRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MinRandomIpv4Ratio': 'minRandomIpv4Ratio',
        'MinRandomIpv6Ratio': 'minRandomIpv6Ratio',
        'MinRandomLoadRate': 'minRandomLoadRate',
        'Numtrials': 'numtrials',
        'PeakLoadingReplicationCount': 'peakLoadingReplicationCount',
        'Peak_customLoadUnit': 'peak_customLoadUnit',
        'Peak_initialStepLoadRate': 'peak_initialStepLoadRate',
        'Peak_loadRateList': 'peak_loadRateList',
        'Peak_maxStepLoadRate': 'peak_maxStepLoadRate',
        'Peak_rate_loadType': 'peak_rate_loadType',
        'Peak_stepLoadUnit': 'peak_stepLoadUnit',
        'Peak_stepStepLoadRate': 'peak_stepStepLoadRate',
        'PerTrafficResults': 'perTrafficResults',
        'PercentMaxRate': 'percentMaxRate',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'QuickBackoffIteration': 'quickBackoffIteration',
        'QuickEnableBackoffIteration': 'quickEnableBackoffIteration',
        'QuickEnableSaturationIteration': 'quickEnableSaturationIteration',
        'QuickSaturationIteration': 'quickSaturationIteration',
        'QuickSearchFrameLossUnit': 'quickSearchFrameLossUnit',
        'QuickSearchLoadUnit': 'quickSearchLoadUnit',
        'QuickSearchResolution': 'quickSearchResolution',
        'QuickSearchSearchType': 'quickSearchSearchType',
        'QuickSearchTiLoss': 'quickSearchTiLoss',
        'QuickSearchTolerance': 'quickSearchTolerance',
        'RandomLoadUnit': 'randomLoadUnit',
        'RandomTiLoss': 'randomTiLoss',
        'RateSelect': 'rateSelect',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'Resolution': 'resolution',
        'Rfc2544ImixDataQoS': 'rfc2544ImixDataQoS',
        'Rfc2889ordering': 'rfc2889ordering',
        'SaturationIteration': 'saturationIteration',
        'SearchBase': 'searchBase',
        'SendFullyMeshed': 'sendFullyMeshed',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'SpyderFramesizeList': 'spyderFramesizeList',
        'StaggeredStart': 'staggeredStart',
        'StepComboLoadRate': 'stepComboLoadRate',
        'StepFrameLossUnit': 'stepFrameLossUnit',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepIncrementIpv4Ratio': 'stepIncrementIpv4Ratio',
        'StepIncrementIpv6Ratio': 'stepIncrementIpv6Ratio',
        'StepIncrementLoadRate': 'stepIncrementLoadRate',
        'StepLoadUnit': 'stepLoadUnit',
        'StepStepLoadRate': 'stepStepLoadRate',
        'StepTiLoss': 'stepTiLoss',
        'StepTolerance': 'stepTolerance',
        'Step_binary_delay_enableAccLoss': 'step_binary_delay_enableAccLoss',
        'Step_binary_delay_modeAccLoss': 'step_binary_delay_modeAccLoss',
        'Step_binary_delay_scaleAccLoss': 'step_binary_delay_scaleAccLoss',
        'Step_binary_delay_thresholdAccLoss': 'step_binary_delay_thresholdAccLoss',
        'Step_binary_flooded_enableAccLoss': 'step_binary_flooded_enableAccLoss',
        'Step_binary_flooded_thresholdAccLoss': 'step_binary_flooded_thresholdAccLoss',
        'Step_binary_integrity_enableAccLoss': 'step_binary_integrity_enableAccLoss',
        'Step_binary_integrity_thresholdAccLoss': 'step_binary_integrity_thresholdAccLoss',
        'Step_binary_latency_enableAccLoss': 'step_binary_latency_enableAccLoss',
        'Step_binary_latency_modeAccLoss': 'step_binary_latency_modeAccLoss',
        'Step_binary_latency_scaleAccLoss': 'step_binary_latency_scaleAccLoss',
        'Step_binary_latency_thresholdAccLoss': 'step_binary_latency_thresholdAccLoss',
        'Step_binary_peak_Backoff': 'step_binary_peak_Backoff',
        'Step_binary_peak_FrameLossUnit': 'step_binary_peak_FrameLossUnit',
        'Step_binary_peak_Resolution': 'step_binary_peak_Resolution',
        'Step_binary_peak_Tolerance': 'step_binary_peak_Tolerance',
        'Step_binary_peak_initialValue': 'step_binary_peak_initialValue',
        'Step_binary_peak_maxValue': 'step_binary_peak_maxValue',
        'Step_binary_peak_minValue': 'step_binary_peak_minValue',
        'Step_binary_seq_enableAccLoss': 'step_binary_seq_enableAccLoss',
        'Step_binary_seq_modeAccLoss': 'step_binary_seq_modeAccLoss',
        'Step_binary_seq_thresholdAccLoss': 'step_binary_seq_thresholdAccLoss',
        'Step_delay_enableAccLoss': 'step_delay_enableAccLoss',
        'Step_delay_modeAccLoss': 'step_delay_modeAccLoss',
        'Step_delay_scaleAccLoss': 'step_delay_scaleAccLoss',
        'Step_delay_thresholdAccLoss': 'step_delay_thresholdAccLoss',
        'Step_flooded_enableAccLoss': 'step_flooded_enableAccLoss',
        'Step_flooded_thresholdAccLoss': 'step_flooded_thresholdAccLoss',
        'Step_integrity_enableAccLoss': 'step_integrity_enableAccLoss',
        'Step_integrity_thresholdAccLoss': 'step_integrity_thresholdAccLoss',
        'Step_latency_enableAccLoss': 'step_latency_enableAccLoss',
        'Step_latency_modeAccLoss': 'step_latency_modeAccLoss',
        'Step_latency_scaleAccLoss': 'step_latency_scaleAccLoss',
        'Step_latency_thresholdAccLoss': 'step_latency_thresholdAccLoss',
        'Step_peak_loadType': 'step_peak_loadType',
        'Step_seq_enableAccLoss': 'step_seq_enableAccLoss',
        'Step_seq_modeAccLoss': 'step_seq_modeAccLoss',
        'Step_seq_thresholdAccLoss': 'step_seq_thresholdAccLoss',
        'Step_step_delay_enableAccLoss': 'step_step_delay_enableAccLoss',
        'Step_step_delay_modeAccLoss': 'step_step_delay_modeAccLoss',
        'Step_step_delay_scaleAccLoss': 'step_step_delay_scaleAccLoss',
        'Step_step_delay_thresholdAccLoss': 'step_step_delay_thresholdAccLoss',
        'Step_step_flooded_enableAccLoss': 'step_step_flooded_enableAccLoss',
        'Step_step_flooded_thresholdAccLoss': 'step_step_flooded_thresholdAccLoss',
        'Step_step_integrity_enableAccLoss': 'step_step_integrity_enableAccLoss',
        'Step_step_integrity_thresholdAccLoss': 'step_step_integrity_thresholdAccLoss',
        'Step_step_latency_enableAccLoss': 'step_step_latency_enableAccLoss',
        'Step_step_latency_modeAccLoss': 'step_step_latency_modeAccLoss',
        'Step_step_latency_scaleAccLoss': 'step_step_latency_scaleAccLoss',
        'Step_step_latency_thresholdAccLoss': 'step_step_latency_thresholdAccLoss',
        'Step_step_peak_FrameLossUnit': 'step_step_peak_FrameLossUnit',
        'Step_step_peak_initialValue': 'step_step_peak_initialValue',
        'Step_step_peak_maxValue': 'step_step_peak_maxValue',
        'Step_step_peak_stepTolerance': 'step_step_peak_stepTolerance',
        'Step_step_peak_stepValue': 'step_step_peak_stepValue',
        'Step_step_seq_enableAccLoss': 'step_step_seq_enableAccLoss',
        'Step_step_seq_modeAccLoss': 'step_step_seq_modeAccLoss',
        'Step_step_seq_thresholdAccLoss': 'step_step_seq_thresholdAccLoss',
        'StopTestOnHighLoss': 'stopTestOnHighLoss',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'Tolerance': 'tolerance',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
        'UnchangedInitial': 'unchangedInitial',
        'UnchangedValueList': 'unchangedValueList',
        'UsePercentOffsets': 'usePercentOffsets',
        'UseTiLoss': 'useTiLoss',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

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
        - str(% | frames): The frame loss unit for traffic in binary.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The load unit value in binary. Possible values include:
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
        - str(linear | perFlow | perPort | perTrafficItem): The binary search type value. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinarySearchType'])
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinarySearchType'], value)

    @property
    def BinaryTiLoss(self):
        """
        Returns
        -------
        - bool: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryTiLoss'])
    @BinaryTiLoss.setter
    def BinaryTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryTiLoss'], value)

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
    def Binary_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_enableAccLoss'])
    @Binary_delay_enableAccLoss.setter
    def Binary_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_enableAccLoss'], value)

    @property
    def Binary_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_modeAccLoss'])
    @Binary_delay_modeAccLoss.setter
    def Binary_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_modeAccLoss'], value)

    @property
    def Binary_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_scaleAccLoss'])
    @Binary_delay_scaleAccLoss.setter
    def Binary_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_scaleAccLoss'], value)

    @property
    def Binary_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_thresholdAccLoss'])
    @Binary_delay_thresholdAccLoss.setter
    def Binary_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_thresholdAccLoss'], value)

    @property
    def Binary_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_flooded_enableAccLoss'])
    @Binary_flooded_enableAccLoss.setter
    def Binary_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_flooded_enableAccLoss'], value)

    @property
    def Binary_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_flooded_thresholdAccLoss'])
    @Binary_flooded_thresholdAccLoss.setter
    def Binary_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_flooded_thresholdAccLoss'], value)

    @property
    def Binary_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_integrity_enableAccLoss'])
    @Binary_integrity_enableAccLoss.setter
    def Binary_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_integrity_enableAccLoss'], value)

    @property
    def Binary_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_integrity_thresholdAccLoss'])
    @Binary_integrity_thresholdAccLoss.setter
    def Binary_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_integrity_thresholdAccLoss'], value)

    @property
    def Binary_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_enableAccLoss'])
    @Binary_latency_enableAccLoss.setter
    def Binary_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_enableAccLoss'], value)

    @property
    def Binary_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_modeAccLoss'])
    @Binary_latency_modeAccLoss.setter
    def Binary_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_modeAccLoss'], value)

    @property
    def Binary_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_scaleAccLoss'])
    @Binary_latency_scaleAccLoss.setter
    def Binary_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_scaleAccLoss'], value)

    @property
    def Binary_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_thresholdAccLoss'])
    @Binary_latency_thresholdAccLoss.setter
    def Binary_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_thresholdAccLoss'], value)

    @property
    def Binary_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_seq_enableAccLoss'])
    @Binary_seq_enableAccLoss.setter
    def Binary_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_seq_enableAccLoss'], value)

    @property
    def Binary_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_seq_modeAccLoss'])
    @Binary_seq_modeAccLoss.setter
    def Binary_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_seq_modeAccLoss'], value)

    @property
    def Binary_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_seq_thresholdAccLoss'])
    @Binary_seq_thresholdAccLoss.setter
    def Binary_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Binary_seq_thresholdAccLoss'], value)

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
    def ComboTiLoss(self):
        """
        Returns
        -------
        - bool: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboTiLoss'])
    @ComboTiLoss.setter
    def ComboTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboTiLoss'], value)

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
    def Combo_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_delay_enableAccLoss'])
    @Combo_delay_enableAccLoss.setter
    def Combo_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_delay_enableAccLoss'], value)

    @property
    def Combo_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_delay_modeAccLoss'])
    @Combo_delay_modeAccLoss.setter
    def Combo_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_delay_modeAccLoss'], value)

    @property
    def Combo_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_delay_scaleAccLoss'])
    @Combo_delay_scaleAccLoss.setter
    def Combo_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_delay_scaleAccLoss'], value)

    @property
    def Combo_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_delay_thresholdAccLoss'])
    @Combo_delay_thresholdAccLoss.setter
    def Combo_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_delay_thresholdAccLoss'], value)

    @property
    def Combo_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_flooded_enableAccLoss'])
    @Combo_flooded_enableAccLoss.setter
    def Combo_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_flooded_enableAccLoss'], value)

    @property
    def Combo_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_flooded_thresholdAccLoss'])
    @Combo_flooded_thresholdAccLoss.setter
    def Combo_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_flooded_thresholdAccLoss'], value)

    @property
    def Combo_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_integrity_enableAccLoss'])
    @Combo_integrity_enableAccLoss.setter
    def Combo_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_integrity_enableAccLoss'], value)

    @property
    def Combo_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_integrity_thresholdAccLoss'])
    @Combo_integrity_thresholdAccLoss.setter
    def Combo_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_integrity_thresholdAccLoss'], value)

    @property
    def Combo_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_latency_enableAccLoss'])
    @Combo_latency_enableAccLoss.setter
    def Combo_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_latency_enableAccLoss'], value)

    @property
    def Combo_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_latency_modeAccLoss'])
    @Combo_latency_modeAccLoss.setter
    def Combo_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_latency_modeAccLoss'], value)

    @property
    def Combo_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_latency_scaleAccLoss'])
    @Combo_latency_scaleAccLoss.setter
    def Combo_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_latency_scaleAccLoss'], value)

    @property
    def Combo_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_latency_thresholdAccLoss'])
    @Combo_latency_thresholdAccLoss.setter
    def Combo_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_latency_thresholdAccLoss'], value)

    @property
    def Combo_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_seq_enableAccLoss'])
    @Combo_seq_enableAccLoss.setter
    def Combo_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_seq_enableAccLoss'], value)

    @property
    def Combo_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_seq_modeAccLoss'])
    @Combo_seq_modeAccLoss.setter
    def Combo_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_seq_modeAccLoss'], value)

    @property
    def Combo_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Combo_seq_thresholdAccLoss'])
    @Combo_seq_thresholdAccLoss.setter
    def Combo_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Combo_seq_thresholdAccLoss'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: Randomly counts the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def CountRandomIpRatio(self):
        """
        Returns
        -------
        - number: Sets the count of the random ip ratio loop
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomIpRatio'])
    @CountRandomIpRatio.setter
    def CountRandomIpRatio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomIpRatio'], value)

    @property
    def CountRandomLoadRate(self):
        """
        Returns
        -------
        - number: Randomly counts the load rate.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the custom load unit. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def CustomTiLoss(self):
        """
        Returns
        -------
        - bool: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomTiLoss'])
    @CustomTiLoss.setter
    def CustomTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomTiLoss'], value)

    @property
    def Custom_binary_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_delay_enableAccLoss'])
    @Custom_binary_delay_enableAccLoss.setter
    def Custom_binary_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_delay_enableAccLoss'], value)

    @property
    def Custom_binary_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_delay_modeAccLoss'])
    @Custom_binary_delay_modeAccLoss.setter
    def Custom_binary_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_delay_modeAccLoss'], value)

    @property
    def Custom_binary_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_delay_scaleAccLoss'])
    @Custom_binary_delay_scaleAccLoss.setter
    def Custom_binary_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_delay_scaleAccLoss'], value)

    @property
    def Custom_binary_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_delay_thresholdAccLoss'])
    @Custom_binary_delay_thresholdAccLoss.setter
    def Custom_binary_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_delay_thresholdAccLoss'], value)

    @property
    def Custom_binary_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_flooded_enableAccLoss'])
    @Custom_binary_flooded_enableAccLoss.setter
    def Custom_binary_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_flooded_enableAccLoss'], value)

    @property
    def Custom_binary_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_flooded_thresholdAccLoss'])
    @Custom_binary_flooded_thresholdAccLoss.setter
    def Custom_binary_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_flooded_thresholdAccLoss'], value)

    @property
    def Custom_binary_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_integrity_enableAccLoss'])
    @Custom_binary_integrity_enableAccLoss.setter
    def Custom_binary_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_integrity_enableAccLoss'], value)

    @property
    def Custom_binary_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_integrity_thresholdAccLoss'])
    @Custom_binary_integrity_thresholdAccLoss.setter
    def Custom_binary_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_integrity_thresholdAccLoss'], value)

    @property
    def Custom_binary_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_latency_enableAccLoss'])
    @Custom_binary_latency_enableAccLoss.setter
    def Custom_binary_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_latency_enableAccLoss'], value)

    @property
    def Custom_binary_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_latency_modeAccLoss'])
    @Custom_binary_latency_modeAccLoss.setter
    def Custom_binary_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_latency_modeAccLoss'], value)

    @property
    def Custom_binary_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_latency_scaleAccLoss'])
    @Custom_binary_latency_scaleAccLoss.setter
    def Custom_binary_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_latency_scaleAccLoss'], value)

    @property
    def Custom_binary_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_latency_thresholdAccLoss'])
    @Custom_binary_latency_thresholdAccLoss.setter
    def Custom_binary_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_latency_thresholdAccLoss'], value)

    @property
    def Custom_binary_peak_Backoff(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_Backoff'])
    @Custom_binary_peak_Backoff.setter
    def Custom_binary_peak_Backoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_Backoff'], value)

    @property
    def Custom_binary_peak_FrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_FrameLossUnit'])
    @Custom_binary_peak_FrameLossUnit.setter
    def Custom_binary_peak_FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_FrameLossUnit'], value)

    @property
    def Custom_binary_peak_Resolution(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_Resolution'])
    @Custom_binary_peak_Resolution.setter
    def Custom_binary_peak_Resolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_Resolution'], value)

    @property
    def Custom_binary_peak_Tolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_Tolerance'])
    @Custom_binary_peak_Tolerance.setter
    def Custom_binary_peak_Tolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_Tolerance'], value)

    @property
    def Custom_binary_peak_initialValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_initialValue'])
    @Custom_binary_peak_initialValue.setter
    def Custom_binary_peak_initialValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_initialValue'], value)

    @property
    def Custom_binary_peak_maxValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_maxValue'])
    @Custom_binary_peak_maxValue.setter
    def Custom_binary_peak_maxValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_maxValue'], value)

    @property
    def Custom_binary_peak_minValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_peak_minValue'])
    @Custom_binary_peak_minValue.setter
    def Custom_binary_peak_minValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_peak_minValue'], value)

    @property
    def Custom_binary_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_seq_enableAccLoss'])
    @Custom_binary_seq_enableAccLoss.setter
    def Custom_binary_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_seq_enableAccLoss'], value)

    @property
    def Custom_binary_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_seq_modeAccLoss'])
    @Custom_binary_seq_modeAccLoss.setter
    def Custom_binary_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_seq_modeAccLoss'], value)

    @property
    def Custom_binary_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_binary_seq_thresholdAccLoss'])
    @Custom_binary_seq_thresholdAccLoss.setter
    def Custom_binary_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_binary_seq_thresholdAccLoss'], value)

    @property
    def Custom_peak_loadType(self):
        """
        Returns
        -------
        - str(binary | custom | step): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_peak_loadType'])
    @Custom_peak_loadType.setter
    def Custom_peak_loadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_peak_loadType'], value)

    @property
    def Custom_step_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_delay_enableAccLoss'])
    @Custom_step_delay_enableAccLoss.setter
    def Custom_step_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_delay_enableAccLoss'], value)

    @property
    def Custom_step_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_delay_modeAccLoss'])
    @Custom_step_delay_modeAccLoss.setter
    def Custom_step_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_delay_modeAccLoss'], value)

    @property
    def Custom_step_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_delay_scaleAccLoss'])
    @Custom_step_delay_scaleAccLoss.setter
    def Custom_step_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_delay_scaleAccLoss'], value)

    @property
    def Custom_step_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_delay_thresholdAccLoss'])
    @Custom_step_delay_thresholdAccLoss.setter
    def Custom_step_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_delay_thresholdAccLoss'], value)

    @property
    def Custom_step_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_flooded_enableAccLoss'])
    @Custom_step_flooded_enableAccLoss.setter
    def Custom_step_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_flooded_enableAccLoss'], value)

    @property
    def Custom_step_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_flooded_thresholdAccLoss'])
    @Custom_step_flooded_thresholdAccLoss.setter
    def Custom_step_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_flooded_thresholdAccLoss'], value)

    @property
    def Custom_step_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_integrity_enableAccLoss'])
    @Custom_step_integrity_enableAccLoss.setter
    def Custom_step_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_integrity_enableAccLoss'], value)

    @property
    def Custom_step_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_integrity_thresholdAccLoss'])
    @Custom_step_integrity_thresholdAccLoss.setter
    def Custom_step_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_integrity_thresholdAccLoss'], value)

    @property
    def Custom_step_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_latency_enableAccLoss'])
    @Custom_step_latency_enableAccLoss.setter
    def Custom_step_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_latency_enableAccLoss'], value)

    @property
    def Custom_step_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_latency_modeAccLoss'])
    @Custom_step_latency_modeAccLoss.setter
    def Custom_step_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_latency_modeAccLoss'], value)

    @property
    def Custom_step_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_latency_scaleAccLoss'])
    @Custom_step_latency_scaleAccLoss.setter
    def Custom_step_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_latency_scaleAccLoss'], value)

    @property
    def Custom_step_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_latency_thresholdAccLoss'])
    @Custom_step_latency_thresholdAccLoss.setter
    def Custom_step_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_latency_thresholdAccLoss'], value)

    @property
    def Custom_step_peak_FrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_peak_FrameLossUnit'])
    @Custom_step_peak_FrameLossUnit.setter
    def Custom_step_peak_FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_peak_FrameLossUnit'], value)

    @property
    def Custom_step_peak_initialValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_peak_initialValue'])
    @Custom_step_peak_initialValue.setter
    def Custom_step_peak_initialValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_peak_initialValue'], value)

    @property
    def Custom_step_peak_maxValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_peak_maxValue'])
    @Custom_step_peak_maxValue.setter
    def Custom_step_peak_maxValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_peak_maxValue'], value)

    @property
    def Custom_step_peak_stepTolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_peak_stepTolerance'])
    @Custom_step_peak_stepTolerance.setter
    def Custom_step_peak_stepTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_peak_stepTolerance'], value)

    @property
    def Custom_step_peak_stepValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_peak_stepValue'])
    @Custom_step_peak_stepValue.setter
    def Custom_step_peak_stepValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_peak_stepValue'], value)

    @property
    def Custom_step_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_seq_enableAccLoss'])
    @Custom_step_seq_enableAccLoss.setter
    def Custom_step_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_seq_enableAccLoss'], value)

    @property
    def Custom_step_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_seq_modeAccLoss'])
    @Custom_step_seq_modeAccLoss.setter
    def Custom_step_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_seq_modeAccLoss'], value)

    @property
    def Custom_step_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Custom_step_seq_thresholdAccLoss'])
    @Custom_step_seq_thresholdAccLoss.setter
    def Custom_step_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Custom_step_seq_thresholdAccLoss'], value)

    @property
    def CustompeakvalueList(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustompeakvalueList'])
    @CustompeakvalueList.setter
    def CustompeakvalueList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustompeakvalueList'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def DetailedResultsEnabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the detailed results for the fully meshed case
        """
        return self._get_attribute(self._SDM_ATT_MAP['DetailedResultsEnabled'])
    @DetailedResultsEnabled.setter
    def DetailedResultsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DetailedResultsEnabled'], value)

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
        - bool: If true, more iterations are performed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraIterations'])
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraIterations'], value)

    @property
    def EnableExtraRetriesOnLoss(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraRetriesOnLoss'])
    @EnableExtraRetriesOnLoss.setter
    def EnableExtraRetriesOnLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraRetriesOnLoss'], value)

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
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If Enabled, The minimum size of the frame is used .
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: If true, enables old statistics for reef load module.
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
    def ExtraRetriesOnLoss(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraRetriesOnLoss'])
    @ExtraRetriesOnLoss.setter
    def ExtraRetriesOnLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraRetriesOnLoss'], value)

    @property
    def FastConvergenceDuration(self):
        """
        Returns
        -------
        - number: sec
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
    def FixedLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedLoadUnit'])
    @FixedLoadUnit.setter
    def FixedLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedLoadUnit'], value)

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
        - str: The frame loss unit for traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameLossUnit'])
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameLossUnit'], value)

    @property
    def FrameOrderingTemp(self):
        """
        Returns
        -------
        - str(noOrdering | peakLoading | unchanged | val2889Ordering): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameOrderingTemp'])
    @FrameOrderingTemp.setter
    def FrameOrderingTemp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameOrderingTemp'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | customlist | increment | random | unchanged): This attribute is the frame size mode for the Quad Gaussian. Possible values includes:
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
        - number: Bytes
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
        - number: The fixed value of framesize.
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
        - str: The list of the available lmix frame size.
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
        - list(str): The list of the available frame size.
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
    def IncrementLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Possible values include:
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
        - number: The initial binary value of the load rate.
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
    def IpRatioMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): Sets the ip ratio mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpRatioMode'])
    @IpRatioMode.setter
    def IpRatioMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpRatioMode'], value)

    @property
    def Ipv4RatioList(self):
        """
        Returns
        -------
        - str: Sets the ipv4 ratio list
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4RatioList'])
    @Ipv4RatioList.setter
    def Ipv4RatioList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4RatioList'], value)

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
    def Ipv6RatioList(self):
        """
        Returns
        -------
        - str: Sets the ipv6 ratio list
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6RatioList'])
    @Ipv6RatioList.setter
    def Ipv6RatioList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6RatioList'], value)

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
        - str(cutThrough | forwardingDelay | mef | storeForward): The type of latency. Possible values include:
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
        - str: The list of Load Rate.
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
        - str(binary | combo | custom | quickSearch | random | step | unchanged): Possible values include:
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
        - number: The upper bound of the iteration rates for each frame size during a binary search.
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
        - number: It signifies the maximum increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxIncrementIpv4Ratio(self):
        """
        Returns
        -------
        - str: Sets the maximum increment value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementIpv4Ratio'])
    @MaxIncrementIpv4Ratio.setter
    def MaxIncrementIpv4Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementIpv4Ratio'], value)

    @property
    def MaxIncrementIpv6Ratio(self):
        """
        Returns
        -------
        - str: Sets the maximum increment value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementIpv6Ratio'])
    @MaxIncrementIpv6Ratio.setter
    def MaxIncrementIpv6Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementIpv6Ratio'], value)

    @property
    def MaxIncrementLoadRate(self):
        """
        Returns
        -------
        - number: It signifies the maximum increment load rate value.
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
        - number: It signifies the maximum random frame size value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxRandomIpv4Ratio(self):
        """
        Returns
        -------
        - str: Sets the maximum radom value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomIpv4Ratio'])
    @MaxRandomIpv4Ratio.setter
    def MaxRandomIpv4Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomIpv4Ratio'], value)

    @property
    def MaxRandomIpv6Ratio(self):
        """
        Returns
        -------
        - str: Sets the maximum random value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomIpv6Ratio'])
    @MaxRandomIpv6Ratio.setter
    def MaxRandomIpv6Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomIpv6Ratio'], value)

    @property
    def MaxRandomLoadRate(self):
        """
        Returns
        -------
        - number: It signifies the maximum random load rate value.
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
        - number: It signifies the maximum step value for load rate.
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
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: It signifies the minimum increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinIncrementIpv4Ratio(self):
        """
        Returns
        -------
        - str: Sets the minimum increment value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementIpv4Ratio'])
    @MinIncrementIpv4Ratio.setter
    def MinIncrementIpv4Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementIpv4Ratio'], value)

    @property
    def MinIncrementIpv6Ratio(self):
        """
        Returns
        -------
        - str: Sets the minimum increment value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementIpv6Ratio'])
    @MinIncrementIpv6Ratio.setter
    def MinIncrementIpv6Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementIpv6Ratio'], value)

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
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def MinRandomIpv4Ratio(self):
        """
        Returns
        -------
        - str: Sets the minimum random value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomIpv4Ratio'])
    @MinRandomIpv4Ratio.setter
    def MinRandomIpv4Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomIpv4Ratio'], value)

    @property
    def MinRandomIpv6Ratio(self):
        """
        Returns
        -------
        - str: Sets the minimum random value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomIpv6Ratio'])
    @MinRandomIpv6Ratio.setter
    def MinRandomIpv6Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomIpv6Ratio'], value)

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
        - number: The integer value that states the number of trials permitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PeakLoadingReplicationCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeakLoadingReplicationCount'])
    @PeakLoadingReplicationCount.setter
    def PeakLoadingReplicationCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeakLoadingReplicationCount'], value)

    @property
    def Peak_customLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_customLoadUnit'])
    @Peak_customLoadUnit.setter
    def Peak_customLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_customLoadUnit'], value)

    @property
    def Peak_initialStepLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_initialStepLoadRate'])
    @Peak_initialStepLoadRate.setter
    def Peak_initialStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_initialStepLoadRate'], value)

    @property
    def Peak_loadRateList(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_loadRateList'])
    @Peak_loadRateList.setter
    def Peak_loadRateList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_loadRateList'], value)

    @property
    def Peak_maxStepLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_maxStepLoadRate'])
    @Peak_maxStepLoadRate.setter
    def Peak_maxStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_maxStepLoadRate'], value)

    @property
    def Peak_rate_loadType(self):
        """
        Returns
        -------
        - str(custom | step): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_rate_loadType'])
    @Peak_rate_loadType.setter
    def Peak_rate_loadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_rate_loadType'], value)

    @property
    def Peak_stepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_stepLoadUnit'])
    @Peak_stepLoadUnit.setter
    def Peak_stepLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_stepLoadUnit'], value)

    @property
    def Peak_stepStepLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peak_stepStepLoadRate'])
    @Peak_stepStepLoadRate.setter
    def Peak_stepStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Peak_stepStepLoadRate'], value)

    @property
    def PerTrafficResults(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PerTrafficResults'])
    @PerTrafficResults.setter
    def PerTrafficResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PerTrafficResults'], value)

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
    def QuickSearchTiLoss(self):
        """
        Returns
        -------
        - bool: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchTiLoss'])
    @QuickSearchTiLoss.setter
    def QuickSearchTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchTiLoss'], value)

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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The random values of the load unit. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomLoadUnit'])
    @RandomLoadUnit.setter
    def RandomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomLoadUnit'], value)

    @property
    def RandomTiLoss(self):
        """
        Returns
        -------
        - bool: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomTiLoss'])
    @RandomTiLoss.setter
    def RandomTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomTiLoss'], value)

    @property
    def RateSelect(self):
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): Possible values include:
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
        - bool: Reports sequence errors in the test result.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The reported throughput rate unit values. Possible values include:
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
        - number: Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops .
        """
        return self._get_attribute(self._SDM_ATT_MAP['Resolution'])
    @Resolution.setter
    def Resolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Resolution'], value)

    @property
    def Rfc2544ImixDataQoS(self):
        """
        Returns
        -------
        - bool: If true, it uses the same frame data qos
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2544ImixDataQoS'])
    @Rfc2544ImixDataQoS.setter
    def Rfc2544ImixDataQoS(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rfc2544ImixDataQoS'], value)

    @property
    def Rfc2889ordering(self):
        """
        Returns
        -------
        - str(noOrdering | peakLoading | unchanged | val2889Ordering): If true, indicates frame ordering by Rfc2889.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2889ordering'])
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rfc2889ordering'], value)

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
    def SearchBase(self):
        """
        Returns
        -------
        - str(rate | replicationCount): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SearchBase'])
    @SearchBase.setter
    def SearchBase(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SearchBase'], value)

    @property
    def SendFullyMeshed(self):
        """
        Returns
        -------
        - bool: Indicates the source group mapping type used for sending data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendFullyMeshed'])
    @SendFullyMeshed.setter
    def SendFullyMeshed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendFullyMeshed'], value)

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
    def SpyderFramesizeList(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../customImix | /api/v1/sessions/1/ixnetwork/quickTest/.../imix])): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpyderFramesizeList'])
    @SpyderFramesizeList.setter
    def SpyderFramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpyderFramesizeList'], value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: Starts test with a stagger.
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
        - str(% | frames): The frame loss unit.
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
        - number: The traffic step increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def StepIncrementIpv4Ratio(self):
        """
        Returns
        -------
        - str: The step in which the ipv4 ratio loop is incremented
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementIpv4Ratio'])
    @StepIncrementIpv4Ratio.setter
    def StepIncrementIpv4Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementIpv4Ratio'], value)

    @property
    def StepIncrementIpv6Ratio(self):
        """
        Returns
        -------
        - str: The step in which the ipv6 ratio loop is incremented
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementIpv6Ratio'])
    @StepIncrementIpv6Ratio.setter
    def StepIncrementIpv6Ratio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementIpv6Ratio'], value)

    @property
    def StepIncrementLoadRate(self):
        """
        Returns
        -------
        - number: The incremental step value of the load rate.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit. Possible values include:
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
    def StepTiLoss(self):
        """
        Returns
        -------
        - bool: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepTiLoss'])
    @StepTiLoss.setter
    def StepTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepTiLoss'], value)

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
    def Step_binary_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_delay_enableAccLoss'])
    @Step_binary_delay_enableAccLoss.setter
    def Step_binary_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_delay_enableAccLoss'], value)

    @property
    def Step_binary_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_delay_modeAccLoss'])
    @Step_binary_delay_modeAccLoss.setter
    def Step_binary_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_delay_modeAccLoss'], value)

    @property
    def Step_binary_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_delay_scaleAccLoss'])
    @Step_binary_delay_scaleAccLoss.setter
    def Step_binary_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_delay_scaleAccLoss'], value)

    @property
    def Step_binary_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_delay_thresholdAccLoss'])
    @Step_binary_delay_thresholdAccLoss.setter
    def Step_binary_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_delay_thresholdAccLoss'], value)

    @property
    def Step_binary_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_flooded_enableAccLoss'])
    @Step_binary_flooded_enableAccLoss.setter
    def Step_binary_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_flooded_enableAccLoss'], value)

    @property
    def Step_binary_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_flooded_thresholdAccLoss'])
    @Step_binary_flooded_thresholdAccLoss.setter
    def Step_binary_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_flooded_thresholdAccLoss'], value)

    @property
    def Step_binary_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_integrity_enableAccLoss'])
    @Step_binary_integrity_enableAccLoss.setter
    def Step_binary_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_integrity_enableAccLoss'], value)

    @property
    def Step_binary_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_integrity_thresholdAccLoss'])
    @Step_binary_integrity_thresholdAccLoss.setter
    def Step_binary_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_integrity_thresholdAccLoss'], value)

    @property
    def Step_binary_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_latency_enableAccLoss'])
    @Step_binary_latency_enableAccLoss.setter
    def Step_binary_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_latency_enableAccLoss'], value)

    @property
    def Step_binary_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_latency_modeAccLoss'])
    @Step_binary_latency_modeAccLoss.setter
    def Step_binary_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_latency_modeAccLoss'], value)

    @property
    def Step_binary_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_latency_scaleAccLoss'])
    @Step_binary_latency_scaleAccLoss.setter
    def Step_binary_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_latency_scaleAccLoss'], value)

    @property
    def Step_binary_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_latency_thresholdAccLoss'])
    @Step_binary_latency_thresholdAccLoss.setter
    def Step_binary_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_latency_thresholdAccLoss'], value)

    @property
    def Step_binary_peak_Backoff(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_Backoff'])
    @Step_binary_peak_Backoff.setter
    def Step_binary_peak_Backoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_Backoff'], value)

    @property
    def Step_binary_peak_FrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_FrameLossUnit'])
    @Step_binary_peak_FrameLossUnit.setter
    def Step_binary_peak_FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_FrameLossUnit'], value)

    @property
    def Step_binary_peak_Resolution(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_Resolution'])
    @Step_binary_peak_Resolution.setter
    def Step_binary_peak_Resolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_Resolution'], value)

    @property
    def Step_binary_peak_Tolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_Tolerance'])
    @Step_binary_peak_Tolerance.setter
    def Step_binary_peak_Tolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_Tolerance'], value)

    @property
    def Step_binary_peak_initialValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_initialValue'])
    @Step_binary_peak_initialValue.setter
    def Step_binary_peak_initialValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_initialValue'], value)

    @property
    def Step_binary_peak_maxValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_maxValue'])
    @Step_binary_peak_maxValue.setter
    def Step_binary_peak_maxValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_maxValue'], value)

    @property
    def Step_binary_peak_minValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_peak_minValue'])
    @Step_binary_peak_minValue.setter
    def Step_binary_peak_minValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_peak_minValue'], value)

    @property
    def Step_binary_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_seq_enableAccLoss'])
    @Step_binary_seq_enableAccLoss.setter
    def Step_binary_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_seq_enableAccLoss'], value)

    @property
    def Step_binary_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_seq_modeAccLoss'])
    @Step_binary_seq_modeAccLoss.setter
    def Step_binary_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_seq_modeAccLoss'], value)

    @property
    def Step_binary_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_binary_seq_thresholdAccLoss'])
    @Step_binary_seq_thresholdAccLoss.setter
    def Step_binary_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_binary_seq_thresholdAccLoss'], value)

    @property
    def Step_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_delay_enableAccLoss'])
    @Step_delay_enableAccLoss.setter
    def Step_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_delay_enableAccLoss'], value)

    @property
    def Step_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_delay_modeAccLoss'])
    @Step_delay_modeAccLoss.setter
    def Step_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_delay_modeAccLoss'], value)

    @property
    def Step_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_delay_scaleAccLoss'])
    @Step_delay_scaleAccLoss.setter
    def Step_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_delay_scaleAccLoss'], value)

    @property
    def Step_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_delay_thresholdAccLoss'])
    @Step_delay_thresholdAccLoss.setter
    def Step_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_delay_thresholdAccLoss'], value)

    @property
    def Step_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_flooded_enableAccLoss'])
    @Step_flooded_enableAccLoss.setter
    def Step_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_flooded_enableAccLoss'], value)

    @property
    def Step_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_flooded_thresholdAccLoss'])
    @Step_flooded_thresholdAccLoss.setter
    def Step_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_flooded_thresholdAccLoss'], value)

    @property
    def Step_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_integrity_enableAccLoss'])
    @Step_integrity_enableAccLoss.setter
    def Step_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_integrity_enableAccLoss'], value)

    @property
    def Step_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_integrity_thresholdAccLoss'])
    @Step_integrity_thresholdAccLoss.setter
    def Step_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_integrity_thresholdAccLoss'], value)

    @property
    def Step_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_latency_enableAccLoss'])
    @Step_latency_enableAccLoss.setter
    def Step_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_latency_enableAccLoss'], value)

    @property
    def Step_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_latency_modeAccLoss'])
    @Step_latency_modeAccLoss.setter
    def Step_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_latency_modeAccLoss'], value)

    @property
    def Step_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_latency_scaleAccLoss'])
    @Step_latency_scaleAccLoss.setter
    def Step_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_latency_scaleAccLoss'], value)

    @property
    def Step_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_latency_thresholdAccLoss'])
    @Step_latency_thresholdAccLoss.setter
    def Step_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_latency_thresholdAccLoss'], value)

    @property
    def Step_peak_loadType(self):
        """
        Returns
        -------
        - str(binary | custom | step): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_peak_loadType'])
    @Step_peak_loadType.setter
    def Step_peak_loadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_peak_loadType'], value)

    @property
    def Step_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_seq_enableAccLoss'])
    @Step_seq_enableAccLoss.setter
    def Step_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_seq_enableAccLoss'], value)

    @property
    def Step_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_seq_modeAccLoss'])
    @Step_seq_modeAccLoss.setter
    def Step_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_seq_modeAccLoss'], value)

    @property
    def Step_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_seq_thresholdAccLoss'])
    @Step_seq_thresholdAccLoss.setter
    def Step_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_seq_thresholdAccLoss'], value)

    @property
    def Step_step_delay_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_delay_enableAccLoss'])
    @Step_step_delay_enableAccLoss.setter
    def Step_step_delay_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_delay_enableAccLoss'], value)

    @property
    def Step_step_delay_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_delay_modeAccLoss'])
    @Step_step_delay_modeAccLoss.setter
    def Step_step_delay_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_delay_modeAccLoss'], value)

    @property
    def Step_step_delay_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_delay_scaleAccLoss'])
    @Step_step_delay_scaleAccLoss.setter
    def Step_step_delay_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_delay_scaleAccLoss'], value)

    @property
    def Step_step_delay_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_delay_thresholdAccLoss'])
    @Step_step_delay_thresholdAccLoss.setter
    def Step_step_delay_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_delay_thresholdAccLoss'], value)

    @property
    def Step_step_flooded_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_flooded_enableAccLoss'])
    @Step_step_flooded_enableAccLoss.setter
    def Step_step_flooded_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_flooded_enableAccLoss'], value)

    @property
    def Step_step_flooded_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_flooded_thresholdAccLoss'])
    @Step_step_flooded_thresholdAccLoss.setter
    def Step_step_flooded_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_flooded_thresholdAccLoss'], value)

    @property
    def Step_step_integrity_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_integrity_enableAccLoss'])
    @Step_step_integrity_enableAccLoss.setter
    def Step_step_integrity_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_integrity_enableAccLoss'], value)

    @property
    def Step_step_integrity_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_integrity_thresholdAccLoss'])
    @Step_step_integrity_thresholdAccLoss.setter
    def Step_step_integrity_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_integrity_thresholdAccLoss'], value)

    @property
    def Step_step_latency_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_latency_enableAccLoss'])
    @Step_step_latency_enableAccLoss.setter
    def Step_step_latency_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_latency_enableAccLoss'], value)

    @property
    def Step_step_latency_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_latency_modeAccLoss'])
    @Step_step_latency_modeAccLoss.setter
    def Step_step_latency_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_latency_modeAccLoss'], value)

    @property
    def Step_step_latency_scaleAccLoss(self):
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_latency_scaleAccLoss'])
    @Step_step_latency_scaleAccLoss.setter
    def Step_step_latency_scaleAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_latency_scaleAccLoss'], value)

    @property
    def Step_step_latency_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_latency_thresholdAccLoss'])
    @Step_step_latency_thresholdAccLoss.setter
    def Step_step_latency_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_latency_thresholdAccLoss'], value)

    @property
    def Step_step_peak_FrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_peak_FrameLossUnit'])
    @Step_step_peak_FrameLossUnit.setter
    def Step_step_peak_FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_peak_FrameLossUnit'], value)

    @property
    def Step_step_peak_initialValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_peak_initialValue'])
    @Step_step_peak_initialValue.setter
    def Step_step_peak_initialValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_peak_initialValue'], value)

    @property
    def Step_step_peak_maxValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_peak_maxValue'])
    @Step_step_peak_maxValue.setter
    def Step_step_peak_maxValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_peak_maxValue'], value)

    @property
    def Step_step_peak_stepTolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_peak_stepTolerance'])
    @Step_step_peak_stepTolerance.setter
    def Step_step_peak_stepTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_peak_stepTolerance'], value)

    @property
    def Step_step_peak_stepValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_peak_stepValue'])
    @Step_step_peak_stepValue.setter
    def Step_step_peak_stepValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_peak_stepValue'], value)

    @property
    def Step_step_seq_enableAccLoss(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_seq_enableAccLoss'])
    @Step_step_seq_enableAccLoss.setter
    def Step_step_seq_enableAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_seq_enableAccLoss'], value)

    @property
    def Step_step_seq_modeAccLoss(self):
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_seq_modeAccLoss'])
    @Step_step_seq_modeAccLoss.setter
    def Step_step_seq_modeAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_seq_modeAccLoss'], value)

    @property
    def Step_step_seq_thresholdAccLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step_step_seq_thresholdAccLoss'])
    @Step_step_seq_thresholdAccLoss.setter
    def Step_step_seq_thresholdAccLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step_step_seq_thresholdAccLoss'], value)

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
        - str: The supported traffic types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: The tolerance value.
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
        - str(burstyLoading | constantLoading): It signifies the traffic type for the protocol. Possible values include:
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
        - number: The minimum delay between successive packets.
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
    def UnchangedValueList(self):
        """
        Returns
        -------
        - str: A list of variable parameter values that are unchanged.
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
        - bool: If true, sets the offset value in percentage.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    @property
    def UseTiLoss(self):
        """
        Returns
        -------
        - str: Use loss across Rx Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseTiLoss'])
    @UseTiLoss.setter
    def UseTiLoss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseTiLoss'], value)

    def update(self, BackoffIteration=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTiLoss=None, BinaryTolerance=None, Binary_delay_enableAccLoss=None, Binary_delay_modeAccLoss=None, Binary_delay_scaleAccLoss=None, Binary_delay_thresholdAccLoss=None, Binary_flooded_enableAccLoss=None, Binary_flooded_thresholdAccLoss=None, Binary_integrity_enableAccLoss=None, Binary_integrity_thresholdAccLoss=None, Binary_latency_enableAccLoss=None, Binary_latency_modeAccLoss=None, Binary_latency_scaleAccLoss=None, Binary_latency_thresholdAccLoss=None, Binary_seq_enableAccLoss=None, Binary_seq_modeAccLoss=None, Binary_seq_thresholdAccLoss=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTiLoss=None, ComboTolerance=None, Combo_delay_enableAccLoss=None, Combo_delay_modeAccLoss=None, Combo_delay_scaleAccLoss=None, Combo_delay_thresholdAccLoss=None, Combo_flooded_enableAccLoss=None, Combo_flooded_thresholdAccLoss=None, Combo_integrity_enableAccLoss=None, Combo_integrity_thresholdAccLoss=None, Combo_latency_enableAccLoss=None, Combo_latency_modeAccLoss=None, Combo_latency_scaleAccLoss=None, Combo_latency_thresholdAccLoss=None, Combo_seq_enableAccLoss=None, Combo_seq_modeAccLoss=None, Combo_seq_thresholdAccLoss=None, CountRandomFrameSize=None, CountRandomIpRatio=None, CountRandomLoadRate=None, CustomLoadUnit=None, CustomTiLoss=None, Custom_binary_delay_enableAccLoss=None, Custom_binary_delay_modeAccLoss=None, Custom_binary_delay_scaleAccLoss=None, Custom_binary_delay_thresholdAccLoss=None, Custom_binary_flooded_enableAccLoss=None, Custom_binary_flooded_thresholdAccLoss=None, Custom_binary_integrity_enableAccLoss=None, Custom_binary_integrity_thresholdAccLoss=None, Custom_binary_latency_enableAccLoss=None, Custom_binary_latency_modeAccLoss=None, Custom_binary_latency_scaleAccLoss=None, Custom_binary_latency_thresholdAccLoss=None, Custom_binary_peak_Backoff=None, Custom_binary_peak_FrameLossUnit=None, Custom_binary_peak_Resolution=None, Custom_binary_peak_Tolerance=None, Custom_binary_peak_initialValue=None, Custom_binary_peak_maxValue=None, Custom_binary_peak_minValue=None, Custom_binary_seq_enableAccLoss=None, Custom_binary_seq_modeAccLoss=None, Custom_binary_seq_thresholdAccLoss=None, Custom_peak_loadType=None, Custom_step_delay_enableAccLoss=None, Custom_step_delay_modeAccLoss=None, Custom_step_delay_scaleAccLoss=None, Custom_step_delay_thresholdAccLoss=None, Custom_step_flooded_enableAccLoss=None, Custom_step_flooded_thresholdAccLoss=None, Custom_step_integrity_enableAccLoss=None, Custom_step_integrity_thresholdAccLoss=None, Custom_step_latency_enableAccLoss=None, Custom_step_latency_modeAccLoss=None, Custom_step_latency_scaleAccLoss=None, Custom_step_latency_thresholdAccLoss=None, Custom_step_peak_FrameLossUnit=None, Custom_step_peak_initialValue=None, Custom_step_peak_maxValue=None, Custom_step_peak_stepTolerance=None, Custom_step_peak_stepValue=None, Custom_step_seq_enableAccLoss=None, Custom_step_seq_modeAccLoss=None, Custom_step_seq_thresholdAccLoss=None, CustompeakvalueList=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableExtraRetriesOnLoss=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, ExtraRetriesOnLoss=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FixedLoadUnit=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameOrderingTemp=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeFixedValue=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, IpRatioMode=None, Ipv4RatioList=None, Ipv4rate=None, Ipv6RatioList=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadRateValue=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxIncrementIpv4Ratio=None, MaxIncrementIpv6Ratio=None, MaxIncrementLoadRate=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxRandomIpv4Ratio=None, MaxRandomIpv6Ratio=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinIncrementIpv4Ratio=None, MinIncrementIpv6Ratio=None, MinKbpsRate=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MinRandomIpv4Ratio=None, MinRandomIpv6Ratio=None, MinRandomLoadRate=None, Numtrials=None, PeakLoadingReplicationCount=None, Peak_customLoadUnit=None, Peak_initialStepLoadRate=None, Peak_loadRateList=None, Peak_maxStepLoadRate=None, Peak_rate_loadType=None, Peak_stepLoadUnit=None, Peak_stepStepLoadRate=None, PerTrafficResults=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickBackoffIteration=None, QuickEnableBackoffIteration=None, QuickEnableSaturationIteration=None, QuickSaturationIteration=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTiLoss=None, QuickSearchTolerance=None, RandomLoadUnit=None, RandomTiLoss=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2544ImixDataQoS=None, Rfc2889ordering=None, SaturationIteration=None, SearchBase=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, SpyderFramesizeList=None, StaggeredStart=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepIncrementIpv4Ratio=None, StepIncrementIpv6Ratio=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTiLoss=None, StepTolerance=None, Step_binary_delay_enableAccLoss=None, Step_binary_delay_modeAccLoss=None, Step_binary_delay_scaleAccLoss=None, Step_binary_delay_thresholdAccLoss=None, Step_binary_flooded_enableAccLoss=None, Step_binary_flooded_thresholdAccLoss=None, Step_binary_integrity_enableAccLoss=None, Step_binary_integrity_thresholdAccLoss=None, Step_binary_latency_enableAccLoss=None, Step_binary_latency_modeAccLoss=None, Step_binary_latency_scaleAccLoss=None, Step_binary_latency_thresholdAccLoss=None, Step_binary_peak_Backoff=None, Step_binary_peak_FrameLossUnit=None, Step_binary_peak_Resolution=None, Step_binary_peak_Tolerance=None, Step_binary_peak_initialValue=None, Step_binary_peak_maxValue=None, Step_binary_peak_minValue=None, Step_binary_seq_enableAccLoss=None, Step_binary_seq_modeAccLoss=None, Step_binary_seq_thresholdAccLoss=None, Step_delay_enableAccLoss=None, Step_delay_modeAccLoss=None, Step_delay_scaleAccLoss=None, Step_delay_thresholdAccLoss=None, Step_flooded_enableAccLoss=None, Step_flooded_thresholdAccLoss=None, Step_integrity_enableAccLoss=None, Step_integrity_thresholdAccLoss=None, Step_latency_enableAccLoss=None, Step_latency_modeAccLoss=None, Step_latency_scaleAccLoss=None, Step_latency_thresholdAccLoss=None, Step_peak_loadType=None, Step_seq_enableAccLoss=None, Step_seq_modeAccLoss=None, Step_seq_thresholdAccLoss=None, Step_step_delay_enableAccLoss=None, Step_step_delay_modeAccLoss=None, Step_step_delay_scaleAccLoss=None, Step_step_delay_thresholdAccLoss=None, Step_step_flooded_enableAccLoss=None, Step_step_flooded_thresholdAccLoss=None, Step_step_integrity_enableAccLoss=None, Step_step_integrity_thresholdAccLoss=None, Step_step_latency_enableAccLoss=None, Step_step_latency_modeAccLoss=None, Step_step_latency_scaleAccLoss=None, Step_step_latency_thresholdAccLoss=None, Step_step_peak_FrameLossUnit=None, Step_step_peak_initialValue=None, Step_step_peak_maxValue=None, Step_step_peak_stepTolerance=None, Step_step_peak_stepValue=None, Step_step_seq_enableAccLoss=None, Step_step_seq_modeAccLoss=None, Step_step_seq_thresholdAccLoss=None, StopTestOnHighLoss=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedInitial=None, UnchangedValueList=None, UsePercentOffsets=None, UseTiLoss=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
        - BinaryBackoff (number): Specifies the percentage of binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): The frame loss unit for traffic in binary.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value in binary. Possible values include:
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - BinarySearchType (str(linear | perFlow | perPort | perTrafficItem)): The binary search type value. Possible values include:
        - BinaryTiLoss (bool): Use loss across Rx Ports
        - BinaryTolerance (number): The binary tolerance level.
        - Binary_delay_enableAccLoss (bool): NOT DEFINED
        - Binary_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Binary_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Binary_delay_thresholdAccLoss (number): NOT DEFINED
        - Binary_flooded_enableAccLoss (bool): NOT DEFINED
        - Binary_flooded_thresholdAccLoss (number): NOT DEFINED
        - Binary_integrity_enableAccLoss (bool): NOT DEFINED
        - Binary_integrity_thresholdAccLoss (number): NOT DEFINED
        - Binary_latency_enableAccLoss (bool): NOT DEFINED
        - Binary_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Binary_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Binary_latency_thresholdAccLoss (number): NOT DEFINED
        - Binary_seq_enableAccLoss (bool): NOT DEFINED
        - Binary_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Binary_seq_thresholdAccLoss (number): NOT DEFINED
        - BurstSize (number): The number of packets that are sent in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - ComboBackoff (number): The backoff combination of the test configuration.
        - ComboFrameLossUnit (str(% | frames)): The frame loss unit for traffic in binary.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The combination of load units. Possible values include:
        - ComboResolution (number): The combined resolution value.
        - ComboTiLoss (bool): Use loss across Rx Ports
        - ComboTolerance (number): The combined tolerance level.
        - Combo_delay_enableAccLoss (bool): NOT DEFINED
        - Combo_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Combo_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Combo_delay_thresholdAccLoss (number): NOT DEFINED
        - Combo_flooded_enableAccLoss (bool): NOT DEFINED
        - Combo_flooded_thresholdAccLoss (number): NOT DEFINED
        - Combo_integrity_enableAccLoss (bool): NOT DEFINED
        - Combo_integrity_thresholdAccLoss (number): NOT DEFINED
        - Combo_latency_enableAccLoss (bool): NOT DEFINED
        - Combo_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Combo_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Combo_latency_thresholdAccLoss (number): NOT DEFINED
        - Combo_seq_enableAccLoss (bool): NOT DEFINED
        - Combo_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Combo_seq_thresholdAccLoss (number): NOT DEFINED
        - CountRandomFrameSize (number): Randomly counts the frame size.
        - CountRandomIpRatio (number): Sets the count of the random ip ratio loop
        - CountRandomLoadRate (number): Randomly counts the load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit. Possible values include:
        - CustomTiLoss (bool): Use loss across Rx Ports
        - Custom_binary_delay_enableAccLoss (bool): NOT DEFINED
        - Custom_binary_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Custom_binary_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Custom_binary_delay_thresholdAccLoss (number): NOT DEFINED
        - Custom_binary_flooded_enableAccLoss (bool): NOT DEFINED
        - Custom_binary_flooded_thresholdAccLoss (number): NOT DEFINED
        - Custom_binary_integrity_enableAccLoss (bool): NOT DEFINED
        - Custom_binary_integrity_thresholdAccLoss (number): NOT DEFINED
        - Custom_binary_latency_enableAccLoss (bool): NOT DEFINED
        - Custom_binary_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Custom_binary_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Custom_binary_latency_thresholdAccLoss (number): NOT DEFINED
        - Custom_binary_peak_Backoff (number): NOT DEFINED
        - Custom_binary_peak_FrameLossUnit (str(% | frames)): NOT DEFINED
        - Custom_binary_peak_Resolution (number): NOT DEFINED
        - Custom_binary_peak_Tolerance (number): NOT DEFINED
        - Custom_binary_peak_initialValue (number): NOT DEFINED
        - Custom_binary_peak_maxValue (number): NOT DEFINED
        - Custom_binary_peak_minValue (number): NOT DEFINED
        - Custom_binary_seq_enableAccLoss (bool): NOT DEFINED
        - Custom_binary_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Custom_binary_seq_thresholdAccLoss (number): NOT DEFINED
        - Custom_peak_loadType (str(binary | custom | step)): NOT DEFINED
        - Custom_step_delay_enableAccLoss (bool): NOT DEFINED
        - Custom_step_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Custom_step_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Custom_step_delay_thresholdAccLoss (number): NOT DEFINED
        - Custom_step_flooded_enableAccLoss (bool): NOT DEFINED
        - Custom_step_flooded_thresholdAccLoss (number): NOT DEFINED
        - Custom_step_integrity_enableAccLoss (bool): NOT DEFINED
        - Custom_step_integrity_thresholdAccLoss (number): NOT DEFINED
        - Custom_step_latency_enableAccLoss (bool): NOT DEFINED
        - Custom_step_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Custom_step_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Custom_step_latency_thresholdAccLoss (number): NOT DEFINED
        - Custom_step_peak_FrameLossUnit (str(% | frames)): NOT DEFINED
        - Custom_step_peak_initialValue (number): NOT DEFINED
        - Custom_step_peak_maxValue (number): NOT DEFINED
        - Custom_step_peak_stepTolerance (number): NOT DEFINED
        - Custom_step_peak_stepValue (number): NOT DEFINED
        - Custom_step_seq_enableAccLoss (bool): NOT DEFINED
        - Custom_step_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Custom_step_seq_thresholdAccLoss (number): NOT DEFINED
        - CustompeakvalueList (str): NOT DEFINED
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit
        - DetailedResultsEnabled (bool): If true, it enables the detailed results for the fully meshed case
        - Duration (number): sec
        - EnableBackoffIteration (bool): If true, enables back off iteration test.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableExtraIterations (bool): If true, more iterations are performed.
        - EnableExtraRetriesOnLoss (bool): 
        - EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If Enabled, The minimum size of the frame is used .
        - EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
        - EnableSaturationIteration (bool): If true, SaturationIteration in enabled .
        - EnableStopTestOnHighLoss (bool): The test stops in case of a high loss.
        - ExtraIterationOffsets (str): This enables the test to run an extra iteration.
        - ExtraRetriesOnLoss (number): 
        - FastConvergenceDuration (number): sec
        - FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Possible values include:
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameLossUnit (str): The frame loss unit for traffic.
        - FrameOrderingTemp (str(noOrdering | peakLoading | unchanged | val2889Ordering)): NOT DEFINED
        - FrameSizeMode (str(custom | customlist | increment | random | unchanged)): This attribute is the frame size mode for the Quad Gaussian. Possible values includes:
        - FramesPerBurstGap (number): The number of frames to be sent after each burst.
        - Framesize (number): Bytes
        - FramesizeFixedValue (number): The fixed value of framesize.
        - FramesizeImixList (str): The list of the available lmix frame size.
        - FramesizeList (list(str)): The list of the available frame size.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - ImixAdd (str): Adds an imix data.
        - ImixData (str): Displays the imix Data.
        - ImixDelete (str): Deletes the imix data.
        - ImixDistribution (str(bwpercentage | weight)): Specifies the imix distribution unit.
        - ImixEnabled (bool): If True, Enables the imix value.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Specefies the imix templates.
        - ImixTrafficType (str): Displays the imix traffic type.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Possible values include:
        - InitialBinaryLoadRate (number): The initial binary value of the load rate.
        - InitialComboLoadRate (number): The initial combination value of the load rate .
        - InitialIncrementLoadRate (number): The initial incremental value of the load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - IpRatioMode (str(custom | fixed | increment | random)): Sets the ip ratio mode
        - Ipv4RatioList (str): Sets the ipv4 ratio list
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6RatioList (str): Sets the ipv6 ratio list
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)): The type of latency. Possible values include:
        - LoadRateList (str): The list of Load Rate.
        - LoadRateValue (number): The value of the load rate.
        - LoadType (str(binary | combo | custom | quickSearch | random | step | unchanged)): Possible values include:
        - MapType (str): The mapping type.
        - MaxBinaryLoadRate (number): The upper bound of the iteration rates for each frame size during a binary search.
        - MaxComboLoadRate (number): The maximum value of the load rate Combo Load Type.
        - MaxIncrementFrameSize (number): It signifies the maximum increment frame size.
        - MaxIncrementIpv4Ratio (str): Sets the maximum increment value for the ipv4 ratio
        - MaxIncrementIpv6Ratio (str): Sets the maximum increment value for the ipv6 ratio
        - MaxIncrementLoadRate (number): It signifies the maximum increment load rate value.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): It signifies the maximum random frame size value.
        - MaxRandomIpv4Ratio (str): Sets the maximum radom value for the ipv4 ratio
        - MaxRandomIpv6Ratio (str): Sets the maximum random value for the ipv6 ratio
        - MaxRandomLoadRate (number): It signifies the maximum random load rate value.
        - MaxStepLoadRate (number): It signifies the maximum step value for load rate.
        - MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
        - MinComboLoadRate (number): The minimum combination load rate.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinIncrementFrameSize (number): It signifies the minimum increment frame size.
        - MinIncrementIpv4Ratio (str): Sets the minimum increment value for the ipv4 ratio
        - MinIncrementIpv6Ratio (str): Sets the minimum increment value for the ipv6 ratio
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MinRandomIpv4Ratio (str): Sets the minimum random value for the ipv4 ratio
        - MinRandomIpv6Ratio (str): Sets the minimum random value for the ipv6 ratio
        - MinRandomLoadRate (number): The minimum random value of the load rate.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PeakLoadingReplicationCount (number): NOT DEFINED
        - Peak_customLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - Peak_initialStepLoadRate (number): NOT DEFINED
        - Peak_loadRateList (str): NOT DEFINED
        - Peak_maxStepLoadRate (number): NOT DEFINED
        - Peak_rate_loadType (str(custom | step)): NOT DEFINED
        - Peak_stepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): 
        - Peak_stepStepLoadRate (number): NOT DEFINED
        - PerTrafficResults (bool): 
        - PercentMaxRate (number): The maximum rate percentage.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - QuickBackoffIteration (number): Sets the quicksearch backoff iteration
        - QuickEnableBackoffIteration (bool): Enables the quick search backoff iteration
        - QuickEnableSaturationIteration (bool): Enables the Quick Search saturation iteration
        - QuickSaturationIteration (number): Sets the quick search saturation iteration
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear | perFlow | perPort | perTrafficItem)): Sets the quick search type
        - QuickSearchTiLoss (bool): Use loss across Rx Ports
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit. Possible values include:
        - RandomTiLoss (bool): Use loss across Rx Ports
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): Possible values include:
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The reported throughput rate unit values. Possible values include:
        - Resolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops .
        - Rfc2544ImixDataQoS (bool): If true, it uses the same frame data qos
        - Rfc2889ordering (str(noOrdering | peakLoading | unchanged | val2889Ordering)): If true, indicates frame ordering by Rfc2889.
        - SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
        - SearchBase (str(rate | replicationCount)): NOT DEFINED
        - SendFullyMeshed (bool): Indicates the source group mapping type used for sending data.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - SpyderFramesizeList (list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../customImix | /api/v1/sessions/1/ixnetwork/quickTest/.../imix]))): 
        - StaggeredStart (bool): Starts test with a stagger.
        - StepComboLoadRate (number): The step value of combination load rate.
        - StepFrameLossUnit (str(% | frames)): The frame loss unit.
        - StepIncrementFrameSize (number): The traffic step increment frame size.
        - StepIncrementIpv4Ratio (str): The step in which the ipv4 ratio loop is incremented
        - StepIncrementIpv6Ratio (str): The step in which the ipv6 ratio loop is incremented
        - StepIncrementLoadRate (number): The incremental step value of the load rate.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit. Possible values include:
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTiLoss (bool): Use loss across Rx Ports
        - StepTolerance (number): The step value of the tolerance level.
        - Step_binary_delay_enableAccLoss (bool): NOT DEFINED
        - Step_binary_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_binary_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Step_binary_delay_thresholdAccLoss (number): NOT DEFINED
        - Step_binary_flooded_enableAccLoss (bool): NOT DEFINED
        - Step_binary_flooded_thresholdAccLoss (number): NOT DEFINED
        - Step_binary_integrity_enableAccLoss (bool): NOT DEFINED
        - Step_binary_integrity_thresholdAccLoss (number): NOT DEFINED
        - Step_binary_latency_enableAccLoss (bool): NOT DEFINED
        - Step_binary_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_binary_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Step_binary_latency_thresholdAccLoss (number): NOT DEFINED
        - Step_binary_peak_Backoff (number): NOT DEFINED
        - Step_binary_peak_FrameLossUnit (str(% | frames)): NOT DEFINED
        - Step_binary_peak_Resolution (number): NOT DEFINED
        - Step_binary_peak_Tolerance (number): NOT DEFINED
        - Step_binary_peak_initialValue (number): NOT DEFINED
        - Step_binary_peak_maxValue (number): NOT DEFINED
        - Step_binary_peak_minValue (number): NOT DEFINED
        - Step_binary_seq_enableAccLoss (bool): NOT DEFINED
        - Step_binary_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_binary_seq_thresholdAccLoss (number): NOT DEFINED
        - Step_delay_enableAccLoss (bool): NOT DEFINED
        - Step_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Step_delay_thresholdAccLoss (number): NOT DEFINED
        - Step_flooded_enableAccLoss (bool): NOT DEFINED
        - Step_flooded_thresholdAccLoss (number): NOT DEFINED
        - Step_integrity_enableAccLoss (bool): NOT DEFINED
        - Step_integrity_thresholdAccLoss (number): NOT DEFINED
        - Step_latency_enableAccLoss (bool): NOT DEFINED
        - Step_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Step_latency_thresholdAccLoss (number): NOT DEFINED
        - Step_peak_loadType (str(binary | custom | step)): NOT DEFINED
        - Step_seq_enableAccLoss (bool): NOT DEFINED
        - Step_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_seq_thresholdAccLoss (number): NOT DEFINED
        - Step_step_delay_enableAccLoss (bool): NOT DEFINED
        - Step_step_delay_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_step_delay_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Step_step_delay_thresholdAccLoss (number): NOT DEFINED
        - Step_step_flooded_enableAccLoss (bool): NOT DEFINED
        - Step_step_flooded_thresholdAccLoss (number): NOT DEFINED
        - Step_step_integrity_enableAccLoss (bool): NOT DEFINED
        - Step_step_integrity_thresholdAccLoss (number): NOT DEFINED
        - Step_step_latency_enableAccLoss (bool): NOT DEFINED
        - Step_step_latency_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_step_latency_scaleAccLoss (str(ms | ns | us)): NOT DEFINED
        - Step_step_latency_thresholdAccLoss (number): NOT DEFINED
        - Step_step_peak_FrameLossUnit (str(% | frames)): NOT DEFINED
        - Step_step_peak_initialValue (number): NOT DEFINED
        - Step_step_peak_maxValue (number): NOT DEFINED
        - Step_step_peak_stepTolerance (number): NOT DEFINED
        - Step_step_peak_stepValue (number): NOT DEFINED
        - Step_step_seq_enableAccLoss (bool): NOT DEFINED
        - Step_step_seq_modeAccLoss (str(average | maximum)): NOT DEFINED
        - Step_step_seq_thresholdAccLoss (number): NOT DEFINED
        - StopTestOnHighLoss (number): It stops test on high loss.
        - SupportedTrafficTypes (str): The supported traffic types.
        - Tolerance (number): The tolerance value.
        - TrafficType (str(burstyLoading | constantLoading)): It signifies the traffic type for the protocol. Possible values include:
        - TxDelay (number): The minimum delay between successive packets.
        - UnchangedInitial (str(False | True)): The first value of an unchanged parameter.
        - UnchangedValueList (str): A list of variable parameter values that are unchanged.
        - UsePercentOffsets (bool): If true, sets the offset value in percentage.
        - UseTiLoss (str): Use loss across Rx Ports

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
