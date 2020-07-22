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
        'ApplyMode': 'applyMode',
        'AssignGroupType': 'assignGroupType',
        'BidirectionalOptionEnabled': 'bidirectionalOptionEnabled',
        'BinaryBackoff': 'binaryBackoff',
        'BinaryResolution': 'binaryResolution',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DummyTrafficId': 'dummyTrafficId',
        'Duration': 'duration',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableLeaveGroup': 'enableLeaveGroup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableMulticastQuerier': 'enableMulticastQuerier',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'FloodedFramesProcessing': 'floodedFramesProcessing',
        'FloodedFramesTemp': 'floodedFramesTemp',
        'ForceRegenerate': 'forceRegenerate',
        'FrameSizeMode': 'frameSizeMode',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'GroupCapacityGreaterThan': 'groupCapacityGreaterThan',
        'GroupDistributionType': 'groupDistributionType',
        'IgmpV1Timeout': 'igmpV1Timeout',
        'IgmpVersion': 'igmpVersion',
        'Igmpv3MessageType': 'igmpv3MessageType',
        'Igmpv3SourceAddrList': 'igmpv3SourceAddrList',
        'IncrAddresses': 'incrAddresses',
        'IncrementLoadUnit': 'incrementLoadUnit',
        'InitialBinaryLoadIntegerValues': 'initialBinaryLoadIntegerValues',
        'Ipv4Address': 'ipv4Address',
        'Ipv6Address': 'ipv6Address',
        'IsIPv6': 'isIPv6',
        'IsMulticastAutomaticFrameData': 'isMulticastAutomaticFrameData',
        'JoinLeaveMultiplier': 'joinLeaveMultiplier',
        'JoinLeaveRate': 'joinLeaveRate',
        'JoinLeaveWaitTime': 'joinLeaveWaitTime',
        'LoadInitialRate': 'loadInitialRate',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxBinaryLoadIntegerValue': 'maxBinaryLoadIntegerValue',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MinBinaryLoadIntegerValues': 'minBinaryLoadIntegerValues',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MldVersion': 'mldVersion',
        'MulticastProtocolUsed': 'multicastProtocolUsed',
        'NumAddresses': 'numAddresses',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'RouterAlert': 'routerAlert',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TestTrafficType': 'testTrafficType',
        'TxDelay': 'txDelay',
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
    def BidirectionalOptionEnabled(self):
        """
        Returns
        -------
        - bool: If true, enables the bidirectional option.
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
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: The count of the random frame size to be sent.
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
    def DummyTrafficId(self):
        """
        Returns
        -------
        - str: The id of the monitor traffic item
        """
        return self._get_attribute(self._SDM_ATT_MAP['DummyTrafficId'])
    @DummyTrafficId.setter
    def DummyTrafficId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DummyTrafficId'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The duration of the test in hours, minutes, or seconds, which is used to calculate the number of frames to transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

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
        - bool: If true, enables minimum frame size.
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
        - bool: If true, enables the old statistics for Reef.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'])
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'], value)

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
    def FloodedFramesProcessing(self):
        """
        Returns
        -------
        - bool: Flooded Frames Processing
        """
        return self._get_attribute(self._SDM_ATT_MAP['FloodedFramesProcessing'])
    @FloodedFramesProcessing.setter
    def FloodedFramesProcessing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FloodedFramesProcessing'], value)

    @property
    def FloodedFramesTemp(self):
        """
        Returns
        -------
        - str: Flooded Frames Temp
        """
        return self._get_attribute(self._SDM_ATT_MAP['FloodedFramesTemp'])
    @FloodedFramesTemp.setter
    def FloodedFramesTemp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FloodedFramesTemp'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: If true, enables force regenerate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

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
        - number: The gap in transmission of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def GroupCapacityGreaterThan(self):
        """
        Returns
        -------
        - number: Indicates the value by which the group capacity is greater than.
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
        - str(acrossHosts | acrossPorts): Indicates the group distribution type.
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
        - number: It signifies the timeout of version 1 of IGMP.
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
        - number: The igmp version.
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
        - number: If true, the MAC address is incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrAddresses'])
    @IncrAddresses.setter
    def IncrAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrAddresses'], value)

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
    def InitialBinaryLoadIntegerValues(self):
        """
        Returns
        -------
        - number: Initial Binary Load Integer Values
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadIntegerValues'])
    @InitialBinaryLoadIntegerValues.setter
    def InitialBinaryLoadIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadIntegerValues'], value)

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: The selected IPv4 address.
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
        - str: It signifies the IP address for version 6.
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
        - str: If true, indicates an IPv6 address.
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
        - str: If true, indicates a multicast automatic frame data.
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
        - number: The leave rate.
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
        - number: The wait time for the leave.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveWaitTime'])
    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveWaitTime'], value)

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
        - str(binary | step): The type of load used to modify the variable parameter value.
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
    def MaxBinaryLoadIntegerValue(self):
        """
        Returns
        -------
        - number: Max Binary Load Integer Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadIntegerValue'])
    @MaxBinaryLoadIntegerValue.setter
    def MaxBinaryLoadIntegerValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadIntegerValue'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The maximum increment value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

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
    def MinBinaryLoadIntegerValues(self):
        """
        Returns
        -------
        - number: Min Binary Load Integer Values
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadIntegerValues'])
    @MinBinaryLoadIntegerValues.setter
    def MinBinaryLoadIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadIntegerValues'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum increment value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

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
    def MulticastProtocolUsed(self):
        """
        Returns
        -------
        - str: The multicast protocol that is used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastProtocolUsed'])
    @MulticastProtocolUsed.setter
    def MulticastProtocolUsed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastProtocolUsed'], value)

    @property
    def NumAddresses(self):
        """
        Returns
        -------
        - number: The number address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumAddresses'])
    @NumAddresses.setter
    def NumAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumAddresses'], value)

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
    def ReportTputRateUnit(self):
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): Report identifying the unit for measuring the throughput rate in frames per second.
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
        - bool: If enabled, it alerts the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterAlert'])
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterAlert'], value)

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
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The step increment value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

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
    def TxDelay(self):
        """
        Returns
        -------
        - number: The delay in transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    def update(self, ApplyMode=None, AssignGroupType=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryResolution=None, CountRandomFrameSize=None, DelayAfterTransmit=None, DummyTrafficId=None, Duration=None, EnableLayer1Rate=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, FloodedFramesEnabled=None, FloodedFramesProcessing=None, FloodedFramesTemp=None, ForceRegenerate=None, FrameSizeMode=None, FramesizeList=None, Gap=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, IncrementLoadUnit=None, InitialBinaryLoadIntegerValues=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LoadInitialRate=None, LoadType=None, MapType=None, MaxBinaryLoadIntegerValue=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinBinaryLoadIntegerValues=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, MldVersion=None, MulticastProtocolUsed=None, NumAddresses=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportTputRateUnit=None, RouterAlert=None, ShowDetailedBinaryResults=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, TestTrafficType=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): Assigns the group type.
        - BidirectionalOptionEnabled (bool): If true, enables the bidirectional option.
        - BinaryBackoff (number): Specifies the percentage of binary backoff.
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - CountRandomFrameSize (number): The count of the random frame size to be sent.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - DummyTrafficId (str): The id of the monitor traffic item
        - Duration (number): The duration of the test in hours, minutes, or seconds, which is used to calculate the number of frames to transmit.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): If true, enables the old statistics for Reef.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - FloodedFramesProcessing (bool): Flooded Frames Processing
        - FloodedFramesTemp (str): Flooded Frames Temp
        - ForceRegenerate (bool): If true, enables force regenerate.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): The list of the available frame sizes.
        - Gap (number): The gap in transmission of frames.
        - GroupCapacityGreaterThan (number): Indicates the value by which the group capacity is greater than.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): Indicates the group distribution type.
        - IgmpV1Timeout (number): It signifies the timeout of version 1 of IGMP.
        - IgmpVersion (number): The igmp version.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (number): If true, the MAC address is incremented.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The incremental value of the load unit.
        - InitialBinaryLoadIntegerValues (number): Initial Binary Load Integer Values
        - Ipv4Address (str): The selected IPv4 address.
        - Ipv6Address (str): It signifies the IP address for version 6.
        - IsIPv6 (str): If true, indicates an IPv6 address.
        - IsMulticastAutomaticFrameData (str): If true, indicates a multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The leave rate.
        - JoinLeaveWaitTime (number): The wait time for the leave.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadType (str(binary | step)): The type of load used to modify the variable parameter value.
        - MapType (str): The mapping type.
        - MaxBinaryLoadIntegerValue (number): Max Binary Load Integer Value
        - MaxIncrementFrameSize (number): The maximum increment value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinBinaryLoadIntegerValues (number): Min Binary Load Integer Values
        - MinIncrementFrameSize (number): The minimum increment value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MldVersion (number): The version of the MLD messages.
        - MulticastProtocolUsed (str): The multicast protocol that is used.
        - NumAddresses (number): The number address.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Report identifying the unit for measuring the throughput rate in frames per second.
        - RouterAlert (bool): If enabled, it alerts the router.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepIncrementFrameSize (number): The step increment value of the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TxDelay (number): The delay in transmission.

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
