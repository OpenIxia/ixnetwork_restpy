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
        'BurstSize': 'burstSize',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'CalibrateLatency': 'calibrateLatency',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DelayBetweenIterations': 'delayBetweenIterations',
        'DelayMode': 'delayMode',
        'DummyTrafficId': 'dummyTrafficId',
        'Duration': 'duration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableExtraIterations': 'enableExtraIterations',
        'EnableExtraJoinFrames': 'enableExtraJoinFrames',
        'EnableFastConvergence': 'enableFastConvergence',
        'EnableLayer2': 'enableLayer2',
        'EnableLeaveGroup': 'enableLeaveGroup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableMulticastQuerier': 'enableMulticastQuerier',
        'EnableRouterAlert': 'enableRouterAlert',
        'ExtraFramesFirstGroupAddress': 'extraFramesFirstGroupAddress',
        'ExtraFramesFirstGroupAddressIPv6': 'extraFramesFirstGroupAddressIPv6',
        'ExtraFramesTotalGroupAddresses': 'extraFramesTotalGroupAddresses',
        'ExtraIterationOffsets': 'extraIterationOffsets',
        'FastConvergenceDuration': 'fastConvergenceDuration',
        'FastConvergenceThreshold': 'fastConvergenceThreshold',
        'FirstMulticastDestMACAddress': 'firstMulticastDestMACAddress',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameSizeMode': 'frameSizeMode',
        'Framesize': 'framesize',
        'FramesizeList': 'framesizeList',
        'GroupCapacityGreaterThan': 'groupCapacityGreaterThan',
        'GroupDistributionType': 'groupDistributionType',
        'IgmpV1Timeout': 'igmpV1Timeout',
        'IgmpVersion': 'igmpVersion',
        'Igmpv3MessageType': 'igmpv3MessageType',
        'Igmpv3SourceAddrList': 'igmpv3SourceAddrList',
        'IncMulticastDestMACAddress': 'incMulticastDestMACAddress',
        'IncPortMACAddress': 'incPortMACAddress',
        'IncrAddresses': 'incrAddresses',
        'IncrStep': 'incrStep',
        'InitialRate': 'initialRate',
        'Ipv4Address': 'ipv4Address',
        'Ipv6Address': 'ipv6Address',
        'IsIPv6': 'isIPv6',
        'IsMulticastAutomaticFrameData': 'isMulticastAutomaticFrameData',
        'JoinDelayRefUnit': 'joinDelayRefUnit',
        'JoinDelayRefValue': 'joinDelayRefValue',
        'JoinLeaveAlgorithm': 'joinLeaveAlgorithm',
        'JoinLeaveFramesPerGroup': 'joinLeaveFramesPerGroup',
        'JoinLeaveMode': 'joinLeaveMode',
        'JoinLeaveMultiplier': 'joinLeaveMultiplier',
        'JoinLeaveRate': 'joinLeaveRate',
        'JoinLeaveWaitTime': 'joinLeaveWaitTime',
        'LatencyType': 'latencyType',
        'LeaveDelayRefUnit': 'leaveDelayRefUnit',
        'LeaveDelayRefValue': 'leaveDelayRefValue',
        'LoadInitialRate': 'loadInitialRate',
        'LoadType': 'loadType',
        'LoadUnit': 'loadUnit',
        'MapType': 'mapType',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxRate': 'maxRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MixedClassMulticast': 'mixedClassMulticast',
        'MldVersion': 'mldVersion',
        'Mldv2MessageType': 'mldv2MessageType',
        'Mldv2SourceAddrList': 'mldv2SourceAddrList',
        'NumAddresses': 'numAddresses',
        'NumIterations': 'numIterations',
        'NumTrials': 'numTrials',
        'NumberOfExtraJoins': 'numberOfExtraJoins',
        'Numtrials': 'numtrials',
        'OffsetTime': 'offsetTime',
        'PercentMaxRate': 'percentMaxRate',
        'PercentMulticastFrames': 'percentMulticastFrames',
        'PercentUnicastFrames': 'percentUnicastFrames',
        'PortMACAddress': 'portMACAddress',
        'ProtocolItem': 'protocolItem',
        'RatePass': 'ratePass',
        'ReportSequenceError': 'reportSequenceError',
        'SendJoinsBeforeLeave': 'sendJoinsBeforeLeave',
        'StaggeredStart': 'staggeredStart',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TestTrafficType': 'testTrafficType',
        'TrafficBeforeJoinLeave': 'trafficBeforeJoinLeave',
        'TxDelay': 'txDelay',
        'Use3376mode': 'use3376mode',
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
        - str(accumulated | distributed): The type assigned to the type.
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
        - bool: If enabled, it shows the outer VLAN connections.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'])
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'], value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: The number of packets to send in a burst .
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
    def CalibrateLatency(self):
        """
        Returns
        -------
        - bool: If true, calibrates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalibrateLatency'])
    @CalibrateLatency.setter
    def CalibrateLatency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalibrateLatency'], value)

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
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def DelayBetweenIterations(self):
        """
        Returns
        -------
        - number: The delay in time between iterations of trasmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayBetweenIterations'])
    @DelayBetweenIterations.setter
    def DelayBetweenIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayBetweenIterations'], value)

    @property
    def DelayMode(self):
        """
        Returns
        -------
        - str(average | max): The mode of delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayMode'])
    @DelayMode.setter
    def DelayMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayMode'], value)

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
        - number: sec
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
    def EnableExtraIterations(self):
        """
        Returns
        -------
        - bool: If true, enables extra iterations.Sets extra iteration offset values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraIterations'])
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraIterations'], value)

    @property
    def EnableExtraJoinFrames(self):
        """
        Returns
        -------
        - bool: If true, enables extra join frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraJoinFrames'])
    @EnableExtraJoinFrames.setter
    def EnableExtraJoinFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraJoinFrames'], value)

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
        - bool: If true, enables leave group.
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
    def EnableRouterAlert(self):
        """
        Returns
        -------
        - bool: If true, enables router alert.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRouterAlert'])
    @EnableRouterAlert.setter
    def EnableRouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRouterAlert'], value)

    @property
    def ExtraFramesFirstGroupAddress(self):
        """
        Returns
        -------
        - str: The extra frames first group IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraFramesFirstGroupAddress'])
    @ExtraFramesFirstGroupAddress.setter
    def ExtraFramesFirstGroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraFramesFirstGroupAddress'], value)

    @property
    def ExtraFramesFirstGroupAddressIPv6(self):
        """
        Returns
        -------
        - str: The extra frames first group IPv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraFramesFirstGroupAddressIPv6'])
    @ExtraFramesFirstGroupAddressIPv6.setter
    def ExtraFramesFirstGroupAddressIPv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraFramesFirstGroupAddressIPv6'], value)

    @property
    def ExtraFramesTotalGroupAddresses(self):
        """
        Returns
        -------
        - number: The extra frames total group address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraFramesTotalGroupAddresses'])
    @ExtraFramesTotalGroupAddresses.setter
    def ExtraFramesTotalGroupAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraFramesTotalGroupAddresses'], value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: Sets extra iteration offset values.
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
        - number: If true, enables fast convergence threshold value.
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
    def GroupCapacityGreaterThan(self):
        """
        Returns
        -------
        - number: The greater value of group capacity.
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
        - str(acrossHosts | acrossPorts): The type of group distribution.
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
        - number: The version of IGMP.
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
        - str(exclude | include): The message type of IGMPv3.
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
        - str: The source address list of IGMPv3.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Igmpv3SourceAddrList'])
    @Igmpv3SourceAddrList.setter
    def Igmpv3SourceAddrList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Igmpv3SourceAddrList'], value)

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
        - number: The incremental step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrStep'])
    @IncrStep.setter
    def IncrStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrStep'], value)

    @property
    def InitialRate(self):
        """
        Returns
        -------
        - str: The first rate of transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialRate'])
    @InitialRate.setter
    def InitialRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialRate'], value)

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
        - str: Signifies if the address is an ipv6 address.
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
        - str: Signifies automatic frameData for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMulticastAutomaticFrameData'])
    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsMulticastAutomaticFrameData'], value)

    @property
    def JoinDelayRefUnit(self):
        """
        Returns
        -------
        - str(ms | ns | us): The reference unit of join delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinDelayRefUnit'])
    @JoinDelayRefUnit.setter
    def JoinDelayRefUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinDelayRefUnit'], value)

    @property
    def JoinDelayRefValue(self):
        """
        Returns
        -------
        - number: The reference value of join delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinDelayRefValue'])
    @JoinDelayRefValue.setter
    def JoinDelayRefValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinDelayRefValue'], value)

    @property
    def JoinLeaveAlgorithm(self):
        """
        Returns
        -------
        - str(joinExisting | joinNew): The algorithm for join leave.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveAlgorithm'])
    @JoinLeaveAlgorithm.setter
    def JoinLeaveAlgorithm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveAlgorithm'], value)

    @property
    def JoinLeaveFramesPerGroup(self):
        """
        Returns
        -------
        - number: The join leave frames per group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveFramesPerGroup'])
    @JoinLeaveFramesPerGroup.setter
    def JoinLeaveFramesPerGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveFramesPerGroup'], value)

    @property
    def JoinLeaveMode(self):
        """
        Returns
        -------
        - str(join | joinLeave | leave): The mode of join leave delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveMode'])
    @JoinLeaveMode.setter
    def JoinLeaveMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveMode'], value)

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
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | storeForward): The type of latency
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LeaveDelayRefUnit(self):
        """
        Returns
        -------
        - str(ms | ns | us): The reference unit of leave delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LeaveDelayRefUnit'])
    @LeaveDelayRefUnit.setter
    def LeaveDelayRefUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LeaveDelayRefUnit'], value)

    @property
    def LeaveDelayRefValue(self):
        """
        Returns
        -------
        - number: The leave delay reference value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LeaveDelayRefValue'])
    @LeaveDelayRefValue.setter
    def LeaveDelayRefValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LeaveDelayRefValue'], value)

    @property
    def LoadInitialRate(self):
        """
        Returns
        -------
        - number: The initial load rate.
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
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): The type of the payload setting
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
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
        - str: The POS traffic map type.
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
        - number: The maximum incremental value of the frame size.
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
    def MaxRate(self):
        """
        Returns
        -------
        - number: The maximum rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRate'])
    @MaxRate.setter
    def MaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRate'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum incremental value of the frame size.
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
        - number: The version of MLD.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MldVersion'])
    @MldVersion.setter
    def MldVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MldVersion'], value)

    @property
    def Mldv2MessageType(self):
        """
        Returns
        -------
        - str(exclude | include): Signifies the message type of mldv2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mldv2MessageType'])
    @Mldv2MessageType.setter
    def Mldv2MessageType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mldv2MessageType'], value)

    @property
    def Mldv2SourceAddrList(self):
        """
        Returns
        -------
        - str: The source address list of mldv2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mldv2SourceAddrList'])
    @Mldv2SourceAddrList.setter
    def Mldv2SourceAddrList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mldv2SourceAddrList'], value)

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
    def NumTrials(self):
        """
        Returns
        -------
        - number: %
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumTrials'])
    @NumTrials.setter
    def NumTrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumTrials'], value)

    @property
    def NumberOfExtraJoins(self):
        """
        Returns
        -------
        - number: The number of extra joins in the address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfExtraJoins'])
    @NumberOfExtraJoins.setter
    def NumberOfExtraJoins(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfExtraJoins'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def OffsetTime(self):
        """
        Returns
        -------
        - number: The offset time value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetTime'])
    @OffsetTime.setter
    def OffsetTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OffsetTime'], value)

    @property
    def PercentMaxRate(self):
        """
        Returns
        -------
        - number: Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMaxRate'])
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentMaxRate'], value)

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
    def RatePass(self):
        """
        Returns
        -------
        - number: A Pass criteria applied to each trial in the test to determine whether the trialpassed or failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RatePass'])
    @RatePass.setter
    def RatePass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RatePass'], value)

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
    def SendJoinsBeforeLeave(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendJoinsBeforeLeave'])
    @SendJoinsBeforeLeave.setter
    def SendJoinsBeforeLeave(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendJoinsBeforeLeave'], value)

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
    def TrafficBeforeJoinLeave(self):
        """
        Returns
        -------
        - bool: The traffic sent before join leave.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficBeforeJoinLeave'])
    @TrafficBeforeJoinLeave.setter
    def TrafficBeforeJoinLeave(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficBeforeJoinLeave'], value)

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

    @property
    def Use3376mode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Use3376mode'])
    @Use3376mode.setter
    def Use3376mode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Use3376mode'], value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - bool: Uses percentage offset value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, ApplyMode=None, AssignGroupType=None, BidirectionalOptionEnabled=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, CalibrateLatency=None, CountRandomFrameSize=None, DelayAfterTransmit=None, DelayBetweenIterations=None, DelayMode=None, DummyTrafficId=None, Duration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableExtraJoinFrames=None, EnableFastConvergence=None, EnableLayer2=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableRouterAlert=None, ExtraFramesFirstGroupAddress=None, ExtraFramesFirstGroupAddressIPv6=None, ExtraFramesTotalGroupAddresses=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FirstMulticastDestMACAddress=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameSizeMode=None, Framesize=None, FramesizeList=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncMulticastDestMACAddress=None, IncPortMACAddress=None, IncrAddresses=None, IncrStep=None, InitialRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinDelayRefUnit=None, JoinDelayRefValue=None, JoinLeaveAlgorithm=None, JoinLeaveFramesPerGroup=None, JoinLeaveMode=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyType=None, LeaveDelayRefUnit=None, LeaveDelayRefValue=None, LoadInitialRate=None, LoadType=None, LoadUnit=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MaxRate=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, MixedClassMulticast=None, MldVersion=None, Mldv2MessageType=None, Mldv2SourceAddrList=None, NumAddresses=None, NumIterations=None, NumTrials=None, NumberOfExtraJoins=None, Numtrials=None, OffsetTime=None, PercentMaxRate=None, PercentMulticastFrames=None, PercentUnicastFrames=None, PortMACAddress=None, ProtocolItem=None, RatePass=None, ReportSequenceError=None, SendJoinsBeforeLeave=None, StaggeredStart=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, TestTrafficType=None, TrafficBeforeJoinLeave=None, TxDelay=None, Use3376mode=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The type assigned to the type.
        - BidirectionalOptionEnabled (bool): If enabled, it shows the outer VLAN connections.
        - BurstSize (number): The number of packets to send in a burst .
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - CalibrateLatency (bool): If true, calibrates the latency.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - DelayBetweenIterations (number): The delay in time between iterations of trasmit.
        - DelayMode (str(average | max)): The mode of delay.
        - DummyTrafficId (str): The id of the monitor traffic item
        - Duration (number): sec
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableExtraIterations (bool): If true, enables extra iterations.Sets extra iteration offset values.
        - EnableExtraJoinFrames (bool): If true, enables extra join frames.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer2 (bool): If true, enables Layer2 protocols.
        - EnableLeaveGroup (bool): If true, enables leave group.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableRouterAlert (bool): If true, enables router alert.
        - ExtraFramesFirstGroupAddress (str): The extra frames first group IP address.
        - ExtraFramesFirstGroupAddressIPv6 (str): The extra frames first group IPv6 address.
        - ExtraFramesTotalGroupAddresses (number): The extra frames total group address.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FastConvergenceDuration (number): sec
        - FastConvergenceThreshold (number): If true, enables fast convergence threshold value.
        - FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Framesize (number): Bytes
        - FramesizeList (list(str)): The list of the available frame size.
        - GroupCapacityGreaterThan (number): The greater value of group capacity.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The type of group distribution.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): The version of IGMP.
        - Igmpv3MessageType (str(exclude | include)): The message type of IGMPv3.
        - Igmpv3SourceAddrList (str): The source address list of IGMPv3.
        - IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
        - IncPortMACAddress (str): The incrementing MAC address of the port.
        - IncrAddresses (number): The incremental address.
        - IncrStep (number): The incremental step value.
        - InitialRate (str): The first rate of transmission.
        - Ipv4Address (str): The allocated IPv4 address for this interface.
        - Ipv6Address (str): The allocated IPv6address for this interface.
        - IsIPv6 (str): Signifies if the address is an ipv6 address.
        - IsMulticastAutomaticFrameData (str): Signifies automatic frameData for multicast.
        - JoinDelayRefUnit (str(ms | ns | us)): The reference unit of join delay.
        - JoinDelayRefValue (number): The reference value of join delay.
        - JoinLeaveAlgorithm (str(joinExisting | joinNew)): The algorithm for join leave.
        - JoinLeaveFramesPerGroup (number): The join leave frames per group.
        - JoinLeaveMode (str(join | joinLeave | leave)): The mode of join leave delay.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join leave rate.
        - JoinLeaveWaitTime (number): The wait time for join delay.
        - LatencyType (str(cutThrough | storeForward)): The type of latency
        - LeaveDelayRefUnit (str(ms | ns | us)): The reference unit of leave delay.
        - LeaveDelayRefValue (number): The leave delay reference value.
        - LoadInitialRate (number): The initial load rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRate (number): The maximum rate.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MixedClassMulticast (str): The mixed multicast class.
        - MldVersion (number): The version of MLD.
        - Mldv2MessageType (str(exclude | include)): Signifies the message type of mldv2.
        - Mldv2SourceAddrList (str): The source address list of mldv2.
        - NumAddresses (number): The number address.
        - NumIterations (number): The number of iterations.
        - NumTrials (number): %
        - NumberOfExtraJoins (number): The number of extra joins in the address.
        - Numtrials (number): The number address.
        - OffsetTime (number): The offset time value.
        - PercentMaxRate (number): Specifies the step rate of the load unit.
        - PercentMulticastFrames (number): The percentage of multicast frames.
        - PercentUnicastFrames (number): The percentage of unicast frames.
        - PortMACAddress (str): The MAC address of the port.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RatePass (number): A Pass criteria applied to each trial in the test to determine whether the trialpassed or failed.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - SendJoinsBeforeLeave (bool): 
        - StaggeredStart (bool): Starts test with a stagger.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TrafficBeforeJoinLeave (bool): The traffic sent before join leave.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - Use3376mode (bool): 
        - UsePercentOffsets (bool): Uses percentage offset value.

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
