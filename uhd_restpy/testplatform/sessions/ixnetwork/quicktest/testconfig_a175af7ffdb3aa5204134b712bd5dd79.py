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
    """NOT DEFINED
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'BinaryBackoff': 'binaryBackoff',
        'BinaryFrameLossUnit': 'binaryFrameLossUnit',
        'BinaryResolution': 'binaryResolution',
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
        'CalculateLatency': 'calculateLatency',
        'CalibrateLatency': 'calibrateLatency',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CountRandomIpRatio': 'countRandomIpRatio',
        'CountRandomLoadRate': 'countRandomLoadRate',
        'CustomLoadUnit': 'customLoadUnit',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DetailedResultsEnabled': 'detailedResultsEnabled',
        'Duration': 'duration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameSizeMode': 'frameSizeMode',
        'FramesPerBurstGap': 'framesPerBurstGap',
        'Framesize': 'framesize',
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
        'InitialIncrementLoadRate': 'initialIncrementLoadRate',
        'IpRatioMode': 'ipRatioMode',
        'Ipv4RatioList': 'ipv4RatioList',
        'Ipv4rate': 'ipv4rate',
        'Ipv6RatioList': 'ipv6RatioList',
        'Ipv6rate': 'ipv6rate',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LoadRate': 'loadRate',
        'LoadRateList': 'loadRateList',
        'LoadType': 'loadType',
        'LoadUnit': 'loadUnit',
        'MapType': 'mapType',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxIncrementIpv4Ratio': 'maxIncrementIpv4Ratio',
        'MaxIncrementIpv6Ratio': 'maxIncrementIpv6Ratio',
        'MaxIncrementLoadRate': 'maxIncrementLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxRandomIpv4Ratio': 'maxRandomIpv4Ratio',
        'MaxRandomIpv6Ratio': 'maxRandomIpv6Ratio',
        'MaxRandomLoadRate': 'maxRandomLoadRate',
        'MinFpsRate': 'minFpsRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinIncrementIpv4Ratio': 'minIncrementIpv4Ratio',
        'MinIncrementIpv6Ratio': 'minIncrementIpv6Ratio',
        'MinKbpsRate': 'minKbpsRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MinRandomIpv4Ratio': 'minRandomIpv4Ratio',
        'MinRandomIpv6Ratio': 'minRandomIpv6Ratio',
        'MinRandomLoadRate': 'minRandomLoadRate',
        'NumFrames': 'numFrames',
        'NumFramesFromula': 'numFramesFromula',
        'Numtrials': 'numtrials',
        'PeakLoadingReplicationCount': 'peakLoadingReplicationCount',
        'PerTrafficResults': 'perTrafficResults',
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
        'Rfc2544ImixDataQoS': 'rfc2544ImixDataQoS',
        'Rfc2889ordering': 'rfc2889ordering',
        'SendFullyMeshed': 'sendFullyMeshed',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'SpyderFramesizeList': 'spyderFramesizeList',
        'StaggeredStart': 'staggeredStart',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepIncrementIpv4Ratio': 'stepIncrementIpv4Ratio',
        'StepIncrementIpv6Ratio': 'stepIncrementIpv6Ratio',
        'StepIncrementLoadRate': 'stepIncrementLoadRate',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'Tolerance': 'tolerance',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
    }
    _SDM_ENUM_MAP = {
        'binaryFrameLossUnit': ['%', 'frames'],
        'binary_delay_modeAccLoss': ['average', 'maximum'],
        'binary_delay_scaleAccLoss': ['ms', 'ns', 'us'],
        'binary_latency_modeAccLoss': ['average', 'maximum'],
        'binary_latency_scaleAccLoss': ['ms', 'ns', 'us'],
        'binary_seq_modeAccLoss': ['average', 'maximum'],
        'customLoadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
        'frameSizeMode': ['custom', 'customlist', 'increment', 'random'],
        'imixDistribution': ['bwpercentage', 'weight'],
        'imixTemplates': ['cisco', 'imix', 'ipsec', 'ipv6', 'none', 'quadmodal', 'standard', 'tcp', 'tolly', 'trimodal'],
        'incrementLoadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
        'ipRatioMode': ['custom', 'fixed', 'increment', 'random'],
        'latencyType': ['cutThrough'],
        'loadType': ['binary'],
        'loadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
        'portDelayUnit': ['bytes', 'nanoseconds'],
        'randomLoadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
        'rateSelect': ['fpsRate', 'kbpsRate', 'percentMaxRate'],
        'reportTputRateUnit': ['gbps', 'gBps', 'kbps', 'kBps', 'mbps', 'mBps'],
        'rfc2889ordering': ['noOrdering', 'peakLoading', 'unchanged', 'val2889Ordering'],
        'trafficType': ['burstyLoading', 'constantLoading'],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def BinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryBackoff'])
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BinaryBackoff'], value)

    @property
    def BinaryFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryFrameLossUnit'])
    @BinaryFrameLossUnit.setter
    def BinaryFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['BinaryFrameLossUnit'], value)

    @property
    def BinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolution'])
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolution'], value)

    @property
    def BinaryTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryTolerance'])
    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BinaryTolerance'], value)

    @property
    def Binary_delay_enableAccLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_enableAccLoss'])
    @Binary_delay_enableAccLoss.setter
    def Binary_delay_enableAccLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_enableAccLoss'], value)

    @property
    def Binary_delay_modeAccLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_modeAccLoss'])
    @Binary_delay_modeAccLoss.setter
    def Binary_delay_modeAccLoss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_modeAccLoss'], value)

    @property
    def Binary_delay_scaleAccLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_scaleAccLoss'])
    @Binary_delay_scaleAccLoss.setter
    def Binary_delay_scaleAccLoss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_scaleAccLoss'], value)

    @property
    def Binary_delay_thresholdAccLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_delay_thresholdAccLoss'])
    @Binary_delay_thresholdAccLoss.setter
    def Binary_delay_thresholdAccLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_delay_thresholdAccLoss'], value)

    @property
    def Binary_flooded_enableAccLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_flooded_enableAccLoss'])
    @Binary_flooded_enableAccLoss.setter
    def Binary_flooded_enableAccLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_flooded_enableAccLoss'], value)

    @property
    def Binary_flooded_thresholdAccLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_flooded_thresholdAccLoss'])
    @Binary_flooded_thresholdAccLoss.setter
    def Binary_flooded_thresholdAccLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_flooded_thresholdAccLoss'], value)

    @property
    def Binary_integrity_enableAccLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_integrity_enableAccLoss'])
    @Binary_integrity_enableAccLoss.setter
    def Binary_integrity_enableAccLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_integrity_enableAccLoss'], value)

    @property
    def Binary_integrity_thresholdAccLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_integrity_thresholdAccLoss'])
    @Binary_integrity_thresholdAccLoss.setter
    def Binary_integrity_thresholdAccLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_integrity_thresholdAccLoss'], value)

    @property
    def Binary_latency_enableAccLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_enableAccLoss'])
    @Binary_latency_enableAccLoss.setter
    def Binary_latency_enableAccLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_enableAccLoss'], value)

    @property
    def Binary_latency_modeAccLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_modeAccLoss'])
    @Binary_latency_modeAccLoss.setter
    def Binary_latency_modeAccLoss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_modeAccLoss'], value)

    @property
    def Binary_latency_scaleAccLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_scaleAccLoss'])
    @Binary_latency_scaleAccLoss.setter
    def Binary_latency_scaleAccLoss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_scaleAccLoss'], value)

    @property
    def Binary_latency_thresholdAccLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_latency_thresholdAccLoss'])
    @Binary_latency_thresholdAccLoss.setter
    def Binary_latency_thresholdAccLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_latency_thresholdAccLoss'], value)

    @property
    def Binary_seq_enableAccLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_seq_enableAccLoss'])
    @Binary_seq_enableAccLoss.setter
    def Binary_seq_enableAccLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_seq_enableAccLoss'], value)

    @property
    def Binary_seq_modeAccLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_seq_modeAccLoss'])
    @Binary_seq_modeAccLoss.setter
    def Binary_seq_modeAccLoss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_seq_modeAccLoss'], value)

    @property
    def Binary_seq_thresholdAccLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Binary_seq_thresholdAccLoss'])
    @Binary_seq_thresholdAccLoss.setter
    def Binary_seq_thresholdAccLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Binary_seq_thresholdAccLoss'], value)

    @property
    def BurstSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def CalculateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def CalibrateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalibrateLatency'])
    @CalibrateLatency.setter
    def CalibrateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalibrateLatency'], value)

    @property
    def CountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def CountRandomIpRatio(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomIpRatio'])
    @CountRandomIpRatio.setter
    def CountRandomIpRatio(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CountRandomIpRatio'], value)

    @property
    def CountRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomLoadRate'])
    @CountRandomLoadRate.setter
    def CountRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CountRandomLoadRate'], value)

    @property
    def CustomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def DetailedResultsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DetailedResultsEnabled'])
    @DetailedResultsEnabled.setter
    def DetailedResultsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DetailedResultsEnabled'], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableDataIntegrity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'])
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'], value)

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
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableOldStatsForReef(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'])
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'], value)

    @property
    def FloodedFramesEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FloodedFramesEnabled'])
    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['FloodedFramesEnabled'], value)

    @property
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

    @property
    def FrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameLossUnit'])
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FrameLossUnit'], value)

    @property
    def FrameSizeMode(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - str(custom | customlist | increment | random): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def FramesPerBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'])
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'], value)

    @property
    def Framesize(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Framesize'])
    @Framesize.setter
    def Framesize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Framesize'], value)

    @property
    def FramesizeImixList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeImixList'])
    @FramesizeImixList.setter
    def FramesizeImixList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FramesizeImixList'], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeList'])
    @FramesizeList.setter
    def FramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['FramesizeList'], value)

    @property
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'])
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'], value)

    @property
    def ImixAdd(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixAdd'])
    @ImixAdd.setter
    def ImixAdd(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixAdd'], value)

    @property
    def ImixData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixData'])
    @ImixData.setter
    def ImixData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixData'], value)

    @property
    def ImixDelete(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixDelete'])
    @ImixDelete.setter
    def ImixDelete(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixDelete'], value)

    @property
    def ImixDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bwpercentage | weight): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixDistribution'])
    @ImixDistribution.setter
    def ImixDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixDistribution'], value)

    @property
    def ImixEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixEnabled'])
    @ImixEnabled.setter
    def ImixEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixEnabled'], value)

    @property
    def ImixTemplates(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixTemplates'])
    @ImixTemplates.setter
    def ImixTemplates(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixTemplates'], value)

    @property
    def ImixTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixTrafficType'])
    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ImixTrafficType'], value)

    @property
    def IncrementLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementLoadUnit'])
    @IncrementLoadUnit.setter
    def IncrementLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['IncrementLoadUnit'], value)

    @property
    def InitialIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialIncrementLoadRate'])
    @InitialIncrementLoadRate.setter
    def InitialIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InitialIncrementLoadRate'], value)

    @property
    def IpRatioMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpRatioMode'])
    @IpRatioMode.setter
    def IpRatioMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpRatioMode'], value)

    @property
    def Ipv4RatioList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4RatioList'])
    @Ipv4RatioList.setter
    def Ipv4RatioList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Ipv4RatioList'], value)

    @property
    def Ipv4rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4rate'])
    @Ipv4rate.setter
    def Ipv4rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Ipv4rate'], value)

    @property
    def Ipv6RatioList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6RatioList'])
    @Ipv6RatioList.setter
    def Ipv6RatioList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Ipv6RatioList'], value)

    @property
    def Ipv6rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6rate'])
    @Ipv6rate.setter
    def Ipv6rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Ipv6rate'], value)

    @property
    def LatencyBins(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - str(cutThrough): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRate'])
    @LoadRate.setter
    def LoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoadRate'], value)

    @property
    def LoadRateList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateList'])
    @LoadRateList.setter
    def LoadRateList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoadRateList'], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def LoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadUnit'])
    @LoadUnit.setter
    def LoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoadUnit'], value)

    @property
    def MapType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxIncrementIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementIpv4Ratio'])
    @MaxIncrementIpv4Ratio.setter
    def MaxIncrementIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementIpv4Ratio'], value)

    @property
    def MaxIncrementIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementIpv6Ratio'])
    @MaxIncrementIpv6Ratio.setter
    def MaxIncrementIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementIpv6Ratio'], value)

    @property
    def MaxIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementLoadRate'])
    @MaxIncrementLoadRate.setter
    def MaxIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementLoadRate'], value)

    @property
    def MaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxRandomIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomIpv4Ratio'])
    @MaxRandomIpv4Ratio.setter
    def MaxRandomIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomIpv4Ratio'], value)

    @property
    def MaxRandomIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomIpv6Ratio'])
    @MaxRandomIpv6Ratio.setter
    def MaxRandomIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomIpv6Ratio'], value)

    @property
    def MaxRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomLoadRate'])
    @MaxRandomLoadRate.setter
    def MaxRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomLoadRate'], value)

    @property
    def MinFpsRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinFpsRate'])
    @MinFpsRate.setter
    def MinFpsRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinFpsRate'], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinIncrementIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementIpv4Ratio'])
    @MinIncrementIpv4Ratio.setter
    def MinIncrementIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementIpv4Ratio'], value)

    @property
    def MinIncrementIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementIpv6Ratio'])
    @MinIncrementIpv6Ratio.setter
    def MinIncrementIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementIpv6Ratio'], value)

    @property
    def MinKbpsRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinKbpsRate'])
    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinKbpsRate'], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def MinRandomIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomIpv4Ratio'])
    @MinRandomIpv4Ratio.setter
    def MinRandomIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinRandomIpv4Ratio'], value)

    @property
    def MinRandomIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomIpv6Ratio'])
    @MinRandomIpv6Ratio.setter
    def MinRandomIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinRandomIpv6Ratio'], value)

    @property
    def MinRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'])
    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinRandomLoadRate'], value)

    @property
    def NumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumFrames'])
    @NumFrames.setter
    def NumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumFrames'], value)

    @property
    def NumFramesFromula(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumFramesFromula'])
    @NumFramesFromula.setter
    def NumFramesFromula(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumFramesFromula'], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PeakLoadingReplicationCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeakLoadingReplicationCount'])
    @PeakLoadingReplicationCount.setter
    def PeakLoadingReplicationCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PeakLoadingReplicationCount'], value)

    @property
    def PerTrafficResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PerTrafficResults'])
    @PerTrafficResults.setter
    def PerTrafficResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['PerTrafficResults'], value)

    @property
    def PercentMaxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMaxRate'])
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PercentMaxRate'], value)

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
        - str(bytes | nanoseconds): NOT DEFINED
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
        - number: NOT DEFINED
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
    def RandomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomLoadUnit'])
    @RandomLoadUnit.setter
    def RandomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RandomLoadUnit'], value)

    @property
    def RateSelect(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateSelect'])
    @RateSelect.setter
    def RateSelect(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RateSelect'], value)

    @property
    def ReportSequenceError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'])
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'], value)

    @property
    def Resolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Resolution'])
    @Resolution.setter
    def Resolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Resolution'], value)

    @property
    def Rfc2544ImixDataQoS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2544ImixDataQoS'])
    @Rfc2544ImixDataQoS.setter
    def Rfc2544ImixDataQoS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Rfc2544ImixDataQoS'], value)

    @property
    def Rfc2889ordering(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noOrdering | peakLoading | unchanged | val2889Ordering): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2889ordering'])
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Rfc2889ordering'], value)

    @property
    def SendFullyMeshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendFullyMeshed'])
    @SendFullyMeshed.setter
    def SendFullyMeshed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SendFullyMeshed'], value)

    @property
    def ShowDetailedBinaryResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'])
    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        # type: (bool) -> None
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
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStart'])
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStart'], value)

    @property
    def StepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def StepIncrementIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementIpv4Ratio'])
    @StepIncrementIpv4Ratio.setter
    def StepIncrementIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementIpv4Ratio'], value)

    @property
    def StepIncrementIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementIpv6Ratio'])
    @StepIncrementIpv6Ratio.setter
    def StepIncrementIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementIpv6Ratio'], value)

    @property
    def StepIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementLoadRate'])
    @StepIncrementLoadRate.setter
    def StepIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementLoadRate'], value)

    @property
    def SupportedTrafficTypes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def Tolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tolerance'])
    @Tolerance.setter
    def Tolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Tolerance'], value)

    @property
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    def update(self, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryResolution=None, BinaryTolerance=None, Binary_delay_enableAccLoss=None, Binary_delay_modeAccLoss=None, Binary_delay_scaleAccLoss=None, Binary_delay_thresholdAccLoss=None, Binary_flooded_enableAccLoss=None, Binary_flooded_thresholdAccLoss=None, Binary_integrity_enableAccLoss=None, Binary_integrity_thresholdAccLoss=None, Binary_latency_enableAccLoss=None, Binary_latency_modeAccLoss=None, Binary_latency_scaleAccLoss=None, Binary_latency_thresholdAccLoss=None, Binary_seq_enableAccLoss=None, Binary_seq_modeAccLoss=None, Binary_seq_thresholdAccLoss=None, BurstSize=None, CalculateLatency=None, CalibrateLatency=None, CountRandomFrameSize=None, CountRandomIpRatio=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialIncrementLoadRate=None, IpRatioMode=None, Ipv4RatioList=None, Ipv4rate=None, Ipv6RatioList=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRate=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxIncrementFrameSize=None, MaxIncrementIpv4Ratio=None, MaxIncrementIpv6Ratio=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomIpv4Ratio=None, MaxRandomIpv6Ratio=None, MaxRandomLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinIncrementIpv4Ratio=None, MinIncrementIpv6Ratio=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomIpv4Ratio=None, MinRandomIpv6Ratio=None, MinRandomLoadRate=None, NumFrames=None, NumFramesFromula=None, Numtrials=None, PeakLoadingReplicationCount=None, PerTrafficResults=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2544ImixDataQoS=None, Rfc2889ordering=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, SpyderFramesizeList=None, StaggeredStart=None, StepIncrementFrameSize=None, StepIncrementIpv4Ratio=None, StepIncrementIpv6Ratio=None, StepIncrementLoadRate=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BinaryBackoff (number): NOT DEFINED
        - BinaryFrameLossUnit (str(% | frames)): NOT DEFINED
        - BinaryResolution (number): NOT DEFINED
        - BinaryTolerance (number): NOT DEFINED
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
        - BurstSize (number): NOT DEFINED
        - CalculateLatency (bool): NOT DEFINED
        - CalibrateLatency (bool): NOT DEFINED
        - CountRandomFrameSize (number): NOT DEFINED
        - CountRandomIpRatio (number): NOT DEFINED
        - CountRandomLoadRate (number): NOT DEFINED
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - DelayAfterTransmit (number): NOT DEFINED
        - DetailedResultsEnabled (bool): NOT DEFINED
        - Duration (number): NOT DEFINED
        - EnableDataIntegrity (bool): NOT DEFINED
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): NOT DEFINED
        - EnableOldStatsForReef (bool): NOT DEFINED
        - FloodedFramesEnabled (bool): NOT DEFINED
        - ForceRegenerate (bool): NOT DEFINED
        - FrameLossUnit (str): NOT DEFINED
        - FrameSizeMode (str(custom | customlist | increment | random)): NOT DEFINED
        - FramesPerBurstGap (number): NOT DEFINED
        - Framesize (str): NOT DEFINED
        - FramesizeImixList (str): NOT DEFINED
        - FramesizeList (list(str)): NOT DEFINED
        - Gap (number): NOT DEFINED
        - GenerateTrackingOptionAggregationFiles (bool): NOT DEFINED
        - ImixAdd (str): NOT DEFINED
        - ImixData (str): NOT DEFINED
        - ImixDelete (str): NOT DEFINED
        - ImixDistribution (str(bwpercentage | weight)): NOT DEFINED
        - ImixEnabled (bool): NOT DEFINED
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): NOT DEFINED
        - ImixTrafficType (str): NOT DEFINED
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - InitialIncrementLoadRate (number): NOT DEFINED
        - IpRatioMode (str(custom | fixed | increment | random)): NOT DEFINED
        - Ipv4RatioList (str): NOT DEFINED
        - Ipv4rate (number): NOT DEFINED
        - Ipv6RatioList (str): NOT DEFINED
        - Ipv6rate (number): NOT DEFINED
        - LatencyBins (str): NOT DEFINED
        - LatencyBinsEnabled (bool): NOT DEFINED
        - LatencyType (str(cutThrough)): NOT DEFINED
        - LoadRate (number): NOT DEFINED
        - LoadRateList (str): NOT DEFINED
        - LoadType (str(binary)): NOT DEFINED
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - MapType (str): NOT DEFINED
        - MaxIncrementFrameSize (number): NOT DEFINED
        - MaxIncrementIpv4Ratio (str): NOT DEFINED
        - MaxIncrementIpv6Ratio (str): NOT DEFINED
        - MaxIncrementLoadRate (number): NOT DEFINED
        - MaxRandomFrameSize (number): NOT DEFINED
        - MaxRandomIpv4Ratio (str): NOT DEFINED
        - MaxRandomIpv6Ratio (str): NOT DEFINED
        - MaxRandomLoadRate (number): NOT DEFINED
        - MinFpsRate (number): NOT DEFINED
        - MinIncrementFrameSize (number): NOT DEFINED
        - MinIncrementIpv4Ratio (str): NOT DEFINED
        - MinIncrementIpv6Ratio (str): NOT DEFINED
        - MinKbpsRate (number): NOT DEFINED
        - MinRandomFrameSize (number): NOT DEFINED
        - MinRandomIpv4Ratio (str): NOT DEFINED
        - MinRandomIpv6Ratio (str): NOT DEFINED
        - MinRandomLoadRate (number): NOT DEFINED
        - NumFrames (number): NOT DEFINED
        - NumFramesFromula (str): 
        - Numtrials (number): NOT DEFINED
        - PeakLoadingReplicationCount (number): NOT DEFINED
        - PerTrafficResults (bool): 
        - PercentMaxRate (number): NOT DEFINED
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): NOT DEFINED
        - PortDelayValue (number): NOT DEFINED
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): NOT DEFINED
        - ReportSequenceError (bool): NOT DEFINED
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): NOT DEFINED
        - Resolution (number): NOT DEFINED
        - Rfc2544ImixDataQoS (bool): NOT DEFINED
        - Rfc2889ordering (str(noOrdering | peakLoading | unchanged | val2889Ordering)): NOT DEFINED
        - SendFullyMeshed (bool): NOT DEFINED
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - SpyderFramesizeList (list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../customImix | /api/v1/sessions/1/ixnetwork/quickTest/.../imix]))): 
        - StaggeredStart (bool): NOT DEFINED
        - StepIncrementFrameSize (number): NOT DEFINED
        - StepIncrementIpv4Ratio (str): NOT DEFINED
        - StepIncrementIpv6Ratio (str): NOT DEFINED
        - StepIncrementLoadRate (number): NOT DEFINED
        - SupportedTrafficTypes (str): NOT DEFINED
        - Tolerance (number): NOT DEFINED
        - TrafficType (str(burstyLoading | constantLoading)): NOT DEFINED
        - TxDelay (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryResolution=None, BinaryTolerance=None, Binary_delay_enableAccLoss=None, Binary_delay_modeAccLoss=None, Binary_delay_scaleAccLoss=None, Binary_delay_thresholdAccLoss=None, Binary_flooded_enableAccLoss=None, Binary_flooded_thresholdAccLoss=None, Binary_integrity_enableAccLoss=None, Binary_integrity_thresholdAccLoss=None, Binary_latency_enableAccLoss=None, Binary_latency_modeAccLoss=None, Binary_latency_scaleAccLoss=None, Binary_latency_thresholdAccLoss=None, Binary_seq_enableAccLoss=None, Binary_seq_modeAccLoss=None, Binary_seq_thresholdAccLoss=None, BurstSize=None, CalculateLatency=None, CalibrateLatency=None, CountRandomFrameSize=None, CountRandomIpRatio=None, CountRandomLoadRate=None, CustomLoadUnit=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialIncrementLoadRate=None, IpRatioMode=None, Ipv4RatioList=None, Ipv4rate=None, Ipv6RatioList=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRate=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxIncrementFrameSize=None, MaxIncrementIpv4Ratio=None, MaxIncrementIpv6Ratio=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MaxRandomIpv4Ratio=None, MaxRandomIpv6Ratio=None, MaxRandomLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinIncrementIpv4Ratio=None, MinIncrementIpv6Ratio=None, MinKbpsRate=None, MinRandomFrameSize=None, MinRandomIpv4Ratio=None, MinRandomIpv6Ratio=None, MinRandomLoadRate=None, NumFrames=None, NumFramesFromula=None, Numtrials=None, PeakLoadingReplicationCount=None, PerTrafficResults=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RandomLoadUnit=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2544ImixDataQoS=None, Rfc2889ordering=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, SpyderFramesizeList=None, StaggeredStart=None, StepIncrementFrameSize=None, StepIncrementIpv4Ratio=None, StepIncrementIpv6Ratio=None, StepIncrementLoadRate=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None):
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - BinaryBackoff (number): NOT DEFINED
        - BinaryFrameLossUnit (str(% | frames)): NOT DEFINED
        - BinaryResolution (number): NOT DEFINED
        - BinaryTolerance (number): NOT DEFINED
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
        - BurstSize (number): NOT DEFINED
        - CalculateLatency (bool): NOT DEFINED
        - CalibrateLatency (bool): NOT DEFINED
        - CountRandomFrameSize (number): NOT DEFINED
        - CountRandomIpRatio (number): NOT DEFINED
        - CountRandomLoadRate (number): NOT DEFINED
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - DelayAfterTransmit (number): NOT DEFINED
        - DetailedResultsEnabled (bool): NOT DEFINED
        - Duration (number): NOT DEFINED
        - EnableDataIntegrity (bool): NOT DEFINED
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): NOT DEFINED
        - EnableOldStatsForReef (bool): NOT DEFINED
        - FloodedFramesEnabled (bool): NOT DEFINED
        - ForceRegenerate (bool): NOT DEFINED
        - FrameLossUnit (str): NOT DEFINED
        - FrameSizeMode (str(custom | customlist | increment | random)): NOT DEFINED
        - FramesPerBurstGap (number): NOT DEFINED
        - Framesize (str): NOT DEFINED
        - FramesizeImixList (str): NOT DEFINED
        - FramesizeList (list(str)): NOT DEFINED
        - Gap (number): NOT DEFINED
        - GenerateTrackingOptionAggregationFiles (bool): NOT DEFINED
        - ImixAdd (str): NOT DEFINED
        - ImixData (str): NOT DEFINED
        - ImixDelete (str): NOT DEFINED
        - ImixDistribution (str(bwpercentage | weight)): NOT DEFINED
        - ImixEnabled (bool): NOT DEFINED
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): NOT DEFINED
        - ImixTrafficType (str): NOT DEFINED
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - InitialIncrementLoadRate (number): NOT DEFINED
        - IpRatioMode (str(custom | fixed | increment | random)): NOT DEFINED
        - Ipv4RatioList (str): NOT DEFINED
        - Ipv4rate (number): NOT DEFINED
        - Ipv6RatioList (str): NOT DEFINED
        - Ipv6rate (number): NOT DEFINED
        - LatencyBins (str): NOT DEFINED
        - LatencyBinsEnabled (bool): NOT DEFINED
        - LatencyType (str(cutThrough)): NOT DEFINED
        - LoadRate (number): NOT DEFINED
        - LoadRateList (str): NOT DEFINED
        - LoadType (str(binary)): NOT DEFINED
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - MapType (str): NOT DEFINED
        - MaxIncrementFrameSize (number): NOT DEFINED
        - MaxIncrementIpv4Ratio (str): NOT DEFINED
        - MaxIncrementIpv6Ratio (str): NOT DEFINED
        - MaxIncrementLoadRate (number): NOT DEFINED
        - MaxRandomFrameSize (number): NOT DEFINED
        - MaxRandomIpv4Ratio (str): NOT DEFINED
        - MaxRandomIpv6Ratio (str): NOT DEFINED
        - MaxRandomLoadRate (number): NOT DEFINED
        - MinFpsRate (number): NOT DEFINED
        - MinIncrementFrameSize (number): NOT DEFINED
        - MinIncrementIpv4Ratio (str): NOT DEFINED
        - MinIncrementIpv6Ratio (str): NOT DEFINED
        - MinKbpsRate (number): NOT DEFINED
        - MinRandomFrameSize (number): NOT DEFINED
        - MinRandomIpv4Ratio (str): NOT DEFINED
        - MinRandomIpv6Ratio (str): NOT DEFINED
        - MinRandomLoadRate (number): NOT DEFINED
        - NumFrames (number): NOT DEFINED
        - NumFramesFromula (str): 
        - Numtrials (number): NOT DEFINED
        - PeakLoadingReplicationCount (number): NOT DEFINED
        - PerTrafficResults (bool): 
        - PercentMaxRate (number): NOT DEFINED
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): NOT DEFINED
        - PortDelayValue (number): NOT DEFINED
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): NOT DEFINED
        - ReportSequenceError (bool): NOT DEFINED
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): NOT DEFINED
        - Resolution (number): NOT DEFINED
        - Rfc2544ImixDataQoS (bool): NOT DEFINED
        - Rfc2889ordering (str(noOrdering | peakLoading | unchanged | val2889Ordering)): NOT DEFINED
        - SendFullyMeshed (bool): NOT DEFINED
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - SpyderFramesizeList (list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../customImix | /api/v1/sessions/1/ixnetwork/quickTest/.../imix]))): 
        - StaggeredStart (bool): NOT DEFINED
        - StepIncrementFrameSize (number): NOT DEFINED
        - StepIncrementIpv4Ratio (str): NOT DEFINED
        - StepIncrementIpv6Ratio (str): NOT DEFINED
        - StepIncrementLoadRate (number): NOT DEFINED
        - SupportedTrafficTypes (str): NOT DEFINED
        - Tolerance (number): NOT DEFINED
        - TrafficType (str(burstyLoading | constantLoading)): NOT DEFINED
        - TxDelay (number): NOT DEFINED

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
