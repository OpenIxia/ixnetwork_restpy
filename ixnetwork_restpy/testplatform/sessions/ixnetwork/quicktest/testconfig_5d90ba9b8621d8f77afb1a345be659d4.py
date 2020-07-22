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
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'Duration': 'duration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableLeaveGroup': 'enableLeaveGroup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableMulticastLearning': 'enableMulticastLearning',
        'EnableMulticastQuerier': 'enableMulticastQuerier',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'EnforceBidirectional': 'enforceBidirectional',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameSizeMode': 'frameSizeMode',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'GroupDistributionType': 'groupDistributionType',
        'IgmpV1Timeout': 'igmpV1Timeout',
        'IgmpVersion': 'igmpVersion',
        'Igmpv3MessageType': 'igmpv3MessageType',
        'Igmpv3SourceAddrList': 'igmpv3SourceAddrList',
        'IncrAddresses': 'incrAddresses',
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
        'LoadUnit': 'loadUnit',
        'MapType': 'mapType',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MldVersion': 'mldVersion',
        'NumAddresses': 'numAddresses',
        'NumIterations': 'numIterations',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'RouterAlert': 'routerAlert',
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
        - str(accumulated | distributed): It assigns the group type.
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
        - bool: If true, allows bidirectional traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'])
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'], value)

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
        - bool: If true, IxNetwork will allow the stream to use smaller packet sizes. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableMulticastLearning(self):
        """
        Returns
        -------
        - bool: If true, enables multicst learning.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMulticastLearning'])
    @EnableMulticastLearning.setter
    def EnableMulticastLearning(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMulticastLearning'], value)

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
        - bool: If true, enables old statistics for Reef.
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
        - list(str): List containing the frame sizes used in the test.
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
    def GroupDistributionType(self):
        """
        Returns
        -------
        - str(acrossHosts | acrossPorts): The type of group dsitribution for the test configuration.
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
        - number: It signifies the version of IGMP.
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
        - str: If true, the MAC address is incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrAddresses'])
    @IncrAddresses.setter
    def IncrAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrAddresses'], value)

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: It signifies the IP address for version 4.
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
        - str: Indicates if the address is an IPv6 address.
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
        - str: ndicates if the config is multicast automatic frame data.
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
        - number: It signifies the join and leave rate.
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
        - number: The wait time for thr leave.
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
        - str(cutThrough | storeForward): The type of latency.
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
        - number: loadInitialRate.
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
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): The type of load used to modify the variable parameter value.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The load unit value.
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
        - str: The test configuration map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

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
    def MldVersion(self):
        """
        Returns
        -------
        - number: It signifies the MLD version.
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
        - number: It signifies the number address.
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
        - bool: Sets the IP header Send Router Alert bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterAlert'])
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterAlert'], value)

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
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The list of supported traffic types.
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
        - str: Test based on the type of traffic endpoint to be configured.
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
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    def update(self, ApplyMode=None, AssignGroupType=None, BidirectionalOptionEnabled=None, CalculateJitter=None, CalculateLatency=None, CountRandomFrameSize=None, DelayAfterTransmit=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastLearning=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, EnforceBidirectional=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameSizeMode=None, FramesizeList=None, Gap=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadInitialRate=None, LoadType=None, LoadUnit=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, MldVersion=None, NumAddresses=None, NumIterations=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, RouterAlert=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, TestTrafficType=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): It assigns the group type.
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - CountRandomFrameSize (number): If true, frame sizes are counted at random.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        - EnableMulticastLearning (bool): If true, enables multicst learning.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): If true, enables old statistics for Reef.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - Gap (number): The gap in transmission of frames.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The type of group dsitribution for the test configuration.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): It signifies the version of IGMP.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (str): If true, the MAC address is incremented.
        - Ipv4Address (str): It signifies the IP address for version 4.
        - Ipv6Address (str): It signifies the IP address for version 6.
        - IsIPv6 (str): Indicates if the address is an IPv6 address.
        - IsMulticastAutomaticFrameData (str): ndicates if the config is multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): It signifies the join and leave rate.
        - JoinLeaveWaitTime (number): The wait time for thr leave.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The type of latency.
        - LoadInitialRate (number): loadInitialRate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of load used to modify the variable parameter value.
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value.
        - MapType (str): The test configuration map type.
        - MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
        - MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
        - MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
        - MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
        - MldVersion (number): It signifies the MLD version.
        - NumAddresses (number): It signifies the number address.
        - NumIterations (number): The integer value for the number of iterations.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Report identifying the unit for measuring the throughput rate in frames per second.
        - RouterAlert (bool): Sets the IP header Send Router Alert bit.
        - StepIncrementFrameSize (number): The step to increment the frame size.
        - SupportedTrafficTypes (str): The list of supported traffic types.
        - TestTrafficType (str): Test based on the type of traffic endpoint to be configured.
        - TxDelay (number): Specifies the amount of delay after every transmit.

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
