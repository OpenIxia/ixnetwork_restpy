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
    def ApplyMode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applyMode')
    @ApplyMode.setter
    def ApplyMode(self, value):
        self._set_attribute('applyMode', value)

    @property
    def AssignGroupType(self):
        """
        Returns
        -------
        - str(accumulated | distributed): The type assigned to the type.
        """
        return self._get_attribute('assignGroupType')
    @AssignGroupType.setter
    def AssignGroupType(self, value):
        self._set_attribute('assignGroupType', value)

    @property
    def BidirectionalOptionEnabled(self):
        """
        Returns
        -------
        - bool: If enabled, it shows the outer VLAN connections.
        """
        return self._get_attribute('bidirectionalOptionEnabled')
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute('bidirectionalOptionEnabled', value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: The number of packets to send in a burst .
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
    def CalibrateLatency(self):
        """
        Returns
        -------
        - bool: If true, calibrates the latency.
        """
        return self._get_attribute('calibrateLatency')
    @CalibrateLatency.setter
    def CalibrateLatency(self, value):
        self._set_attribute('calibrateLatency', value)

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
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
        """
        return self._get_attribute('delayAfterTransmit')
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute('delayAfterTransmit', value)

    @property
    def DelayBetweenIterations(self):
        """
        Returns
        -------
        - number: The delay in time between iterations of trasmit.
        """
        return self._get_attribute('delayBetweenIterations')
    @DelayBetweenIterations.setter
    def DelayBetweenIterations(self, value):
        self._set_attribute('delayBetweenIterations', value)

    @property
    def DelayMode(self):
        """
        Returns
        -------
        - str(average | max): The mode of delay.
        """
        return self._get_attribute('delayMode')
    @DelayMode.setter
    def DelayMode(self, value):
        self._set_attribute('delayMode', value)

    @property
    def DummyTrafficId(self):
        """
        Returns
        -------
        - str: The id of the monitor traffic item
        """
        return self._get_attribute('dummyTrafficId')
    @DummyTrafficId.setter
    def DummyTrafficId(self, value):
        self._set_attribute('dummyTrafficId', value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: sec
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
        - bool: If true, enables extra iterations.Sets extra iteration offset values.
        """
        return self._get_attribute('enableExtraIterations')
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute('enableExtraIterations', value)

    @property
    def EnableExtraJoinFrames(self):
        """
        Returns
        -------
        - bool: If true, enables extra join frames.
        """
        return self._get_attribute('enableExtraJoinFrames')
    @EnableExtraJoinFrames.setter
    def EnableExtraJoinFrames(self, value):
        self._set_attribute('enableExtraJoinFrames', value)

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
    def EnableLayer2(self):
        """
        Returns
        -------
        - bool: If true, enables Layer2 protocols.
        """
        return self._get_attribute('enableLayer2')
    @EnableLayer2.setter
    def EnableLayer2(self, value):
        self._set_attribute('enableLayer2', value)

    @property
    def EnableLeaveGroup(self):
        """
        Returns
        -------
        - bool: If true, enables leave group.
        """
        return self._get_attribute('enableLeaveGroup')
    @EnableLeaveGroup.setter
    def EnableLeaveGroup(self, value):
        self._set_attribute('enableLeaveGroup', value)

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
    def EnableMulticastQuerier(self):
        """
        Returns
        -------
        - bool: Enable Multicast Querier Settings
        """
        return self._get_attribute('enableMulticastQuerier')
    @EnableMulticastQuerier.setter
    def EnableMulticastQuerier(self, value):
        self._set_attribute('enableMulticastQuerier', value)

    @property
    def EnableRouterAlert(self):
        """
        Returns
        -------
        - bool: If true, enables router alert.
        """
        return self._get_attribute('enableRouterAlert')
    @EnableRouterAlert.setter
    def EnableRouterAlert(self, value):
        self._set_attribute('enableRouterAlert', value)

    @property
    def ExtraFramesFirstGroupAddress(self):
        """
        Returns
        -------
        - str: The extra frames first group IP address.
        """
        return self._get_attribute('extraFramesFirstGroupAddress')
    @ExtraFramesFirstGroupAddress.setter
    def ExtraFramesFirstGroupAddress(self, value):
        self._set_attribute('extraFramesFirstGroupAddress', value)

    @property
    def ExtraFramesFirstGroupAddressIPv6(self):
        """
        Returns
        -------
        - str: The extra frames first group IPv6 address.
        """
        return self._get_attribute('extraFramesFirstGroupAddressIPv6')
    @ExtraFramesFirstGroupAddressIPv6.setter
    def ExtraFramesFirstGroupAddressIPv6(self, value):
        self._set_attribute('extraFramesFirstGroupAddressIPv6', value)

    @property
    def ExtraFramesTotalGroupAddresses(self):
        """
        Returns
        -------
        - number: The extra frames total group address.
        """
        return self._get_attribute('extraFramesTotalGroupAddresses')
    @ExtraFramesTotalGroupAddresses.setter
    def ExtraFramesTotalGroupAddresses(self, value):
        self._set_attribute('extraFramesTotalGroupAddresses', value)

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
    def FirstMulticastDestMACAddress(self):
        """
        Returns
        -------
        - str: The first multicast destination MAC address.
        """
        return self._get_attribute('firstMulticastDestMACAddress')
    @FirstMulticastDestMACAddress.setter
    def FirstMulticastDestMACAddress(self, value):
        self._set_attribute('firstMulticastDestMACAddress', value)

    @property
    def FloodedFramesEnabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the flooded frames statistics
        """
        return self._get_attribute('floodedFramesEnabled')
    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        self._set_attribute('floodedFramesEnabled', value)

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
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute('frameSizeMode')
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute('frameSizeMode', value)

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
        - list(str): The list of the available frame size.
        """
        return self._get_attribute('framesizeList')
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute('framesizeList', value)

    @property
    def GroupCapacityGreaterThan(self):
        """
        Returns
        -------
        - number: The greater value of group capacity.
        """
        return self._get_attribute('groupCapacityGreaterThan')
    @GroupCapacityGreaterThan.setter
    def GroupCapacityGreaterThan(self, value):
        self._set_attribute('groupCapacityGreaterThan', value)

    @property
    def GroupDistributionType(self):
        """
        Returns
        -------
        - str(acrossHosts | acrossPorts): The type of group distribution.
        """
        return self._get_attribute('groupDistributionType')
    @GroupDistributionType.setter
    def GroupDistributionType(self, value):
        self._set_attribute('groupDistributionType', value)

    @property
    def IgmpV1Timeout(self):
        """
        Returns
        -------
        - number: The IGMPv1 timeout value.
        """
        return self._get_attribute('igmpV1Timeout')
    @IgmpV1Timeout.setter
    def IgmpV1Timeout(self, value):
        self._set_attribute('igmpV1Timeout', value)

    @property
    def IgmpVersion(self):
        """
        Returns
        -------
        - number: The version of IGMP.
        """
        return self._get_attribute('igmpVersion')
    @IgmpVersion.setter
    def IgmpVersion(self, value):
        self._set_attribute('igmpVersion', value)

    @property
    def Igmpv3MessageType(self):
        """
        Returns
        -------
        - str(exclude | include): The message type of IGMPv3.
        """
        return self._get_attribute('igmpv3MessageType')
    @Igmpv3MessageType.setter
    def Igmpv3MessageType(self, value):
        self._set_attribute('igmpv3MessageType', value)

    @property
    def Igmpv3SourceAddrList(self):
        """
        Returns
        -------
        - str: The source address list of IGMPv3.
        """
        return self._get_attribute('igmpv3SourceAddrList')
    @Igmpv3SourceAddrList.setter
    def Igmpv3SourceAddrList(self, value):
        self._set_attribute('igmpv3SourceAddrList', value)

    @property
    def IncMulticastDestMACAddress(self):
        """
        Returns
        -------
        - str: The incrementing multicast destination MAC address.
        """
        return self._get_attribute('incMulticastDestMACAddress')
    @IncMulticastDestMACAddress.setter
    def IncMulticastDestMACAddress(self, value):
        self._set_attribute('incMulticastDestMACAddress', value)

    @property
    def IncPortMACAddress(self):
        """
        Returns
        -------
        - str: The incrementing MAC address of the port.
        """
        return self._get_attribute('incPortMACAddress')
    @IncPortMACAddress.setter
    def IncPortMACAddress(self, value):
        self._set_attribute('incPortMACAddress', value)

    @property
    def IncrAddresses(self):
        """
        Returns
        -------
        - number: The incremental address.
        """
        return self._get_attribute('incrAddresses')
    @IncrAddresses.setter
    def IncrAddresses(self, value):
        self._set_attribute('incrAddresses', value)

    @property
    def IncrStep(self):
        """
        Returns
        -------
        - number: The incremental step value.
        """
        return self._get_attribute('incrStep')
    @IncrStep.setter
    def IncrStep(self, value):
        self._set_attribute('incrStep', value)

    @property
    def InitialRate(self):
        """
        Returns
        -------
        - str: The first rate of transmission.
        """
        return self._get_attribute('initialRate')
    @InitialRate.setter
    def InitialRate(self, value):
        self._set_attribute('initialRate', value)

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: The allocated IPv4 address for this interface.
        """
        return self._get_attribute('ipv4Address')
    @Ipv4Address.setter
    def Ipv4Address(self, value):
        self._set_attribute('ipv4Address', value)

    @property
    def Ipv6Address(self):
        """
        Returns
        -------
        - str: The allocated IPv6address for this interface.
        """
        return self._get_attribute('ipv6Address')
    @Ipv6Address.setter
    def Ipv6Address(self, value):
        self._set_attribute('ipv6Address', value)

    @property
    def IsIPv6(self):
        """
        Returns
        -------
        - str: Signifies if the address is an ipv6 address.
        """
        return self._get_attribute('isIPv6')
    @IsIPv6.setter
    def IsIPv6(self, value):
        self._set_attribute('isIPv6', value)

    @property
    def IsMulticastAutomaticFrameData(self):
        """
        Returns
        -------
        - str: Signifies automatic frameData for multicast.
        """
        return self._get_attribute('isMulticastAutomaticFrameData')
    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        self._set_attribute('isMulticastAutomaticFrameData', value)

    @property
    def JoinDelayRefUnit(self):
        """
        Returns
        -------
        - str(ms | ns | us): The reference unit of join delay.
        """
        return self._get_attribute('joinDelayRefUnit')
    @JoinDelayRefUnit.setter
    def JoinDelayRefUnit(self, value):
        self._set_attribute('joinDelayRefUnit', value)

    @property
    def JoinDelayRefValue(self):
        """
        Returns
        -------
        - number: The reference value of join delay.
        """
        return self._get_attribute('joinDelayRefValue')
    @JoinDelayRefValue.setter
    def JoinDelayRefValue(self, value):
        self._set_attribute('joinDelayRefValue', value)

    @property
    def JoinLeaveAlgorithm(self):
        """
        Returns
        -------
        - str(joinExisting | joinNew): The algorithm for join leave.
        """
        return self._get_attribute('joinLeaveAlgorithm')
    @JoinLeaveAlgorithm.setter
    def JoinLeaveAlgorithm(self, value):
        self._set_attribute('joinLeaveAlgorithm', value)

    @property
    def JoinLeaveFramesPerGroup(self):
        """
        Returns
        -------
        - number: The join leave frames per group.
        """
        return self._get_attribute('joinLeaveFramesPerGroup')
    @JoinLeaveFramesPerGroup.setter
    def JoinLeaveFramesPerGroup(self, value):
        self._set_attribute('joinLeaveFramesPerGroup', value)

    @property
    def JoinLeaveMode(self):
        """
        Returns
        -------
        - str(join | joinLeave | leave): The mode of join leave delay.
        """
        return self._get_attribute('joinLeaveMode')
    @JoinLeaveMode.setter
    def JoinLeaveMode(self, value):
        self._set_attribute('joinLeaveMode', value)

    @property
    def JoinLeaveMultiplier(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('joinLeaveMultiplier')
    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        self._set_attribute('joinLeaveMultiplier', value)

    @property
    def JoinLeaveRate(self):
        """
        Returns
        -------
        - number: The join leave rate.
        """
        return self._get_attribute('joinLeaveRate')
    @JoinLeaveRate.setter
    def JoinLeaveRate(self, value):
        self._set_attribute('joinLeaveRate', value)

    @property
    def JoinLeaveWaitTime(self):
        """
        Returns
        -------
        - number: The wait time for join delay.
        """
        return self._get_attribute('joinLeaveWaitTime')
    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        self._set_attribute('joinLeaveWaitTime', value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | storeForward): The type of latency
        """
        return self._get_attribute('latencyType')
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute('latencyType', value)

    @property
    def LeaveDelayRefUnit(self):
        """
        Returns
        -------
        - str(ms | ns | us): The reference unit of leave delay.
        """
        return self._get_attribute('leaveDelayRefUnit')
    @LeaveDelayRefUnit.setter
    def LeaveDelayRefUnit(self, value):
        self._set_attribute('leaveDelayRefUnit', value)

    @property
    def LeaveDelayRefValue(self):
        """
        Returns
        -------
        - number: The leave delay reference value.
        """
        return self._get_attribute('leaveDelayRefValue')
    @LeaveDelayRefValue.setter
    def LeaveDelayRefValue(self, value):
        self._set_attribute('leaveDelayRefValue', value)

    @property
    def LoadInitialRate(self):
        """
        Returns
        -------
        - number: The initial load rate.
        """
        return self._get_attribute('loadInitialRate')
    @LoadInitialRate.setter
    def LoadInitialRate(self, value):
        self._set_attribute('loadInitialRate', value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): The type of the payload setting
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
        """
        return self._get_attribute('loadUnit')
    @LoadUnit.setter
    def LoadUnit(self, value):
        self._set_attribute('loadUnit', value)

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
    def MaxRate(self):
        """
        Returns
        -------
        - number: The maximum rate.
        """
        return self._get_attribute('maxRate')
    @MaxRate.setter
    def MaxRate(self, value):
        self._set_attribute('maxRate', value)

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
    def MixedClassMulticast(self):
        """
        Returns
        -------
        - str: The mixed multicast class.
        """
        return self._get_attribute('mixedClassMulticast')
    @MixedClassMulticast.setter
    def MixedClassMulticast(self, value):
        self._set_attribute('mixedClassMulticast', value)

    @property
    def MldVersion(self):
        """
        Returns
        -------
        - number: The version of MLD.
        """
        return self._get_attribute('mldVersion')
    @MldVersion.setter
    def MldVersion(self, value):
        self._set_attribute('mldVersion', value)

    @property
    def Mldv2MessageType(self):
        """
        Returns
        -------
        - str(exclude | include): Signifies the message type of mldv2.
        """
        return self._get_attribute('mldv2MessageType')
    @Mldv2MessageType.setter
    def Mldv2MessageType(self, value):
        self._set_attribute('mldv2MessageType', value)

    @property
    def Mldv2SourceAddrList(self):
        """
        Returns
        -------
        - str: The source address list of mldv2.
        """
        return self._get_attribute('mldv2SourceAddrList')
    @Mldv2SourceAddrList.setter
    def Mldv2SourceAddrList(self, value):
        self._set_attribute('mldv2SourceAddrList', value)

    @property
    def NumAddresses(self):
        """
        Returns
        -------
        - number: The number address.
        """
        return self._get_attribute('numAddresses')
    @NumAddresses.setter
    def NumAddresses(self, value):
        self._set_attribute('numAddresses', value)

    @property
    def NumIterations(self):
        """
        Returns
        -------
        - number: The number of iterations.
        """
        return self._get_attribute('numIterations')
    @NumIterations.setter
    def NumIterations(self, value):
        self._set_attribute('numIterations', value)

    @property
    def NumTrials(self):
        """
        Returns
        -------
        - number: %
        """
        return self._get_attribute('numTrials')
    @NumTrials.setter
    def NumTrials(self, value):
        self._set_attribute('numTrials', value)

    @property
    def NumberOfExtraJoins(self):
        """
        Returns
        -------
        - number: The number of extra joins in the address.
        """
        return self._get_attribute('numberOfExtraJoins')
    @NumberOfExtraJoins.setter
    def NumberOfExtraJoins(self, value):
        self._set_attribute('numberOfExtraJoins', value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number address.
        """
        return self._get_attribute('numtrials')
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute('numtrials', value)

    @property
    def OffsetTime(self):
        """
        Returns
        -------
        - number: The offset time value.
        """
        return self._get_attribute('offsetTime')
    @OffsetTime.setter
    def OffsetTime(self, value):
        self._set_attribute('offsetTime', value)

    @property
    def PercentMaxRate(self):
        """
        Returns
        -------
        - number: Specifies the step rate of the load unit.
        """
        return self._get_attribute('percentMaxRate')
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute('percentMaxRate', value)

    @property
    def PercentMulticastFrames(self):
        """
        Returns
        -------
        - number: The percentage of multicast frames.
        """
        return self._get_attribute('percentMulticastFrames')
    @PercentMulticastFrames.setter
    def PercentMulticastFrames(self, value):
        self._set_attribute('percentMulticastFrames', value)

    @property
    def PercentUnicastFrames(self):
        """
        Returns
        -------
        - number: The percentage of unicast frames.
        """
        return self._get_attribute('percentUnicastFrames')
    @PercentUnicastFrames.setter
    def PercentUnicastFrames(self, value):
        self._set_attribute('percentUnicastFrames', value)

    @property
    def PortMACAddress(self):
        """
        Returns
        -------
        - str: The MAC address of the port.
        """
        return self._get_attribute('portMACAddress')
    @PortMACAddress.setter
    def PortMACAddress(self, value):
        self._set_attribute('portMACAddress', value)

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
    def RatePass(self):
        """
        Returns
        -------
        - number: A Pass criteria applied to each trial in the test to determine whether the trialpassed or failed.
        """
        return self._get_attribute('ratePass')
    @RatePass.setter
    def RatePass(self, value):
        self._set_attribute('ratePass', value)

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
    def SendJoinsBeforeLeave(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('sendJoinsBeforeLeave')
    @SendJoinsBeforeLeave.setter
    def SendJoinsBeforeLeave(self, value):
        self._set_attribute('sendJoinsBeforeLeave', value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: Starts test with a stagger.
        """
        return self._get_attribute('staggeredStart')
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute('staggeredStart', value)

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
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: It signifies the test traffic type value.
        """
        return self._get_attribute('testTrafficType')
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute('testTrafficType', value)

    @property
    def TrafficBeforeJoinLeave(self):
        """
        Returns
        -------
        - bool: The traffic sent before join leave.
        """
        return self._get_attribute('trafficBeforeJoinLeave')
    @TrafficBeforeJoinLeave.setter
    def TrafficBeforeJoinLeave(self, value):
        self._set_attribute('trafficBeforeJoinLeave', value)

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
    def Use3376mode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('use3376mode')
    @Use3376mode.setter
    def Use3376mode(self, value):
        self._set_attribute('use3376mode', value)

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
