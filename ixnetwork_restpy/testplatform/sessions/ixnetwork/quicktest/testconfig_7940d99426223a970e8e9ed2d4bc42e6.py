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
    """Allows to set the test parameters.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'AddrRateNumFrames': 'addrRateNumFrames',
        'AddrRateValidationFpsRate': 'addrRateValidationFpsRate',
        'AddrRateValidationRate': 'addrRateValidationRate',
        'AddrRateValidationRateUnit': 'addrRateValidationRateUnit',
        'Age': 'age',
        'BidirectionalOptionEnabled': 'bidirectionalOptionEnabled',
        'BinaryBackoff': 'binaryBackoff',
        'BinaryFrameLossUnit': 'binaryFrameLossUnit',
        'BinaryLoadUnit': 'binaryLoadUnit',
        'BinaryResolution': 'binaryResolution',
        'BinarySearchType': 'binarySearchType',
        'BinaryTolerance': 'binaryTolerance',
        'BurstSize': 'burstSize',
        'CalculateLatency': 'calculateLatency',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'Duration': 'duration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableDropLink': 'enableDropLink',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'EnforceBidirectional': 'enforceBidirectional',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameSizeMode': 'frameSizeMode',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'IncrementLoadUnit': 'incrementLoadUnit',
        'InitialBinaryLoadRate': 'initialBinaryLoadRate',
        'InitialIncrementLoadRate': 'initialIncrementLoadRate',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LoadRateList': 'loadRateList',
        'LoadType': 'loadType',
        'LoadUnit': 'loadUnit',
        'MapType': 'mapType',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxIncrementLoadRate': 'maxIncrementLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinIncrementLoadRate': 'minIncrementLoadRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'PortDownTime': 'portDownTime',
        'ProtocolItem': 'protocolItem',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'StaggeredStart': 'staggeredStart',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepIncrementLoadRate': 'stepIncrementLoadRate',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TargetValue': 'targetValue',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def AddrRateNumFrames(self):
        """
        Returns
        -------
        - number: The number of addresses that are to be used for each port in the current configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateNumFrames'])
    @AddrRateNumFrames.setter
    def AddrRateNumFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateNumFrames'], value)

    @property
    def AddrRateValidationFpsRate(self):
        """
        Returns
        -------
        - str: The rate at which validation frames are sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateValidationFpsRate'])
    @AddrRateValidationFpsRate.setter
    def AddrRateValidationFpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateValidationFpsRate'], value)

    @property
    def AddrRateValidationRate(self):
        """
        Returns
        -------
        - number: The number of validation frames that IxNetwork sends for each address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateValidationRate'])
    @AddrRateValidationRate.setter
    def AddrRateValidationRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateValidationRate'], value)

    @property
    def AddrRateValidationRateUnit(self):
        """
        Returns
        -------
        - str(fps | percentMaxRate): The unit of validation frames that IxNetwork sends for each address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateValidationRateUnit'])
    @AddrRateValidationRateUnit.setter
    def AddrRateValidationRateUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateValidationRateUnit'], value)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: New table size for each retry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])
    @Age.setter
    def Age(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Age'], value)

    @property
    def BidirectionalOptionEnabled(self):
        """
        Returns
        -------
        - bool: If true, allows bidirectional traffic.
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
        - number: The percentage to be applied to the search interval through which the next iteration rate is obtained.
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
        - str(% | frames): The binary frame loss unit, measured either as percentage value or number of frames lost.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The binary load unit value of test configuration.
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
        - number: The resolution of the iteration during a binary search.
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
        - str(linear | perFlow): Specify the binary search type of the test configuration.
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
        - number: The resolution of the iteration during a binary search.
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
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: If true, the latency is calculated.
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
        - number: If true, randomly counts the frame size.
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
        - number: Specifies the amount of delay after every transmit.
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
    def EnableDropLink(self):
        """
        Returns
        -------
        - bool: If true, allows to drop link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDropLink'])
    @EnableDropLink.setter
    def EnableDropLink(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDropLink'], value)

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
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: Enables old statistics for reef.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'])
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'], value)

    @property
    def EnforceBidirectional(self):
        """
        Returns
        -------
        - bool: If true, uses bidirectional traffic mapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnforceBidirectional'])
    @EnforceBidirectional.setter
    def EnforceBidirectional(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnforceBidirectional'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: Initiates a forced regeneration of the test configuration.
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
        - str: The frame loss unit of measurement for the algorithm.
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
        - str(custom | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

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
        - number: Inter-frame gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

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
        - number: The load rate used in the first iteration for each frame size during a binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'])
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'], value)

    @property
    def InitialIncrementLoadRate(self):
        """
        Returns
        -------
        - number: The initial incremental value of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialIncrementLoadRate'])
    @InitialIncrementLoadRate.setter
    def InitialIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialIncrementLoadRate'], value)

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
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | increment): The type of the payload setting.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The load unit value of test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadUnit'])
    @LoadUnit.setter
    def LoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadUnit'], value)

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
        - number: The maximum incremental value of the load rate.
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
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The lower bound of the iteration rates for each frame size during a binary search.
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
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinIncrementLoadRate(self):
        """
        Returns
        -------
        - number: The minimum incremental value of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementLoadRate'])
    @MinIncrementLoadRate.setter
    def MinIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementLoadRate'], value)

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
    def PortDownTime(self):
        """
        Returns
        -------
        - number: The time interval during the port is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDownTime'])
    @PortDownTime.setter
    def PortDownTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDownTime'], value)

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
        - number: The step incremental value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementLoadRate'])
    @StepIncrementLoadRate.setter
    def StepIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementLoadRate'], value)

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
    def TargetValue(self):
        """
        Returns
        -------
        - str: The value of the statistic that determines the success of the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetValue'])
    @TargetValue.setter
    def TargetValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetValue'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): Specify the type of the traffic of the test configuration.
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

    def update(self, AddrRateNumFrames=None, AddrRateValidationFpsRate=None, AddrRateValidationRate=None, AddrRateValidationRateUnit=None, Age=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateLatency=None, CountRandomFrameSize=None, DelayAfterTransmit=None, Duration=None, EnableDataIntegrity=None, EnableDropLink=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, EnforceBidirectional=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramesizeList=None, Gap=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialIncrementLoadRate=None, LatencyBins=None, LatencyBinsEnabled=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxBinaryLoadRate=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MinBinaryLoadRate=None, MinIncrementFrameSize=None, MinIncrementLoadRate=None, MinRandomFrameSize=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortDownTime=None, ProtocolItem=None, ShowDetailedBinaryResults=None, StaggeredStart=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, SupportedTrafficTypes=None, TargetValue=None, TrafficType=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - AddrRateNumFrames (number): The number of addresses that are to be used for each port in the current configuration.
        - AddrRateValidationFpsRate (str): The rate at which validation frames are sent.
        - AddrRateValidationRate (number): The number of validation frames that IxNetwork sends for each address.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): The unit of validation frames that IxNetwork sends for each address.
        - Age (number): New table size for each retry.
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - BinaryBackoff (number): The percentage to be applied to the search interval through which the next iteration rate is obtained.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit, measured either as percentage value or number of frames lost.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit value of test configuration.
        - BinaryResolution (number): The resolution of the iteration during a binary search.
        - BinarySearchType (str(linear | perFlow)): Specify the binary search type of the test configuration.
        - BinaryTolerance (number): The resolution of the iteration during a binary search.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CalculateLatency (bool): If true, the latency is calculated.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableDropLink (bool): If true, allows to drop link.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableOldStatsForReef (bool): Enables old statistics for reef.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - ForceRegenerate (bool): Initiates a forced regeneration of the test configuration.
        - FrameLossUnit (str): The frame loss unit of measurement for the algorithm.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): The list of the available frame size.
        - Gap (number): Inter-frame gap.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The incremental value of the load unit.
        - InitialBinaryLoadRate (number): The load rate used in the first iteration for each frame size during a binary search.
        - InitialIncrementLoadRate (number): The initial incremental value of load rate.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LoadRateList (str): Enter the Load Rate List.
        - LoadType (str(binary | increment)): The type of the payload setting.
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value of test configuration.
        - MapType (str): The mapping type.
        - MaxBinaryLoadRate (number): The upper bound of the iteration rates for each frame size during a binary search.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinBinaryLoadRate (number): The lower bound of the iteration rates for each frame size during a binary search.
        - MinIncrementFrameSize (number): The minimum random frame size to be sent.
        - MinIncrementLoadRate (number): The minimum incremental value of load rate.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): The time interval during the port is down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StaggeredStart (bool): If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepIncrementLoadRate (number): The step incremental value of the load rate.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TargetValue (str): The value of the statistic that determines the success of the test.
        - TrafficType (str(burstyLoading | constantLoading)): Specify the type of the traffic of the test configuration.
        - TxDelay (number): Signifies the transmission delay time.

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
