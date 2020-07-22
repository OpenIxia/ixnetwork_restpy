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
    """It gives details about the test configuration
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'ApplyMode': 'applyMode',
        'AssignGroupType': 'assignGroupType',
        'BidirectionalOptionEnabled': 'bidirectionalOptionEnabled',
        'BurdenFrameSize': 'burdenFrameSize',
        'BurdenProtocolItems': 'burdenProtocolItems',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DelayBetweenIterations': 'delayBetweenIterations',
        'DelayMode': 'delayMode',
        'Duration': 'duration',
        'EnableExtraJoinFrames': 'enableExtraJoinFrames',
        'EnableLeaveGroup': 'enableLeaveGroup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableMulticastLearning': 'enableMulticastLearning',
        'EnableMulticastQuerier': 'enableMulticastQuerier',
        'EnableRouterAlert': 'enableRouterAlert',
        'ExtraFramesFirstGroupAddress': 'extraFramesFirstGroupAddress',
        'ExtraFramesFirstGroupAddressIPv6': 'extraFramesFirstGroupAddressIPv6',
        'ExtraFramesTotalGroupAddresses': 'extraFramesTotalGroupAddresses',
        'FloodedFramesEnabled': 'floodedFramesEnabled',
        'ForceRegenerate': 'forceRegenerate',
        'FrameSizeMode': 'frameSizeMode',
        'FramesizeList': 'framesizeList',
        'GroupCapacityGreaterThan': 'groupCapacityGreaterThan',
        'GroupDistributionType': 'groupDistributionType',
        'IgmpV1Timeout': 'igmpV1Timeout',
        'IgmpVersion': 'igmpVersion',
        'Igmpv3MessageType': 'igmpv3MessageType',
        'Igmpv3SourceAddrList': 'igmpv3SourceAddrList',
        'IncrAddresses': 'incrAddresses',
        'IncrStep': 'incrStep',
        'IncrementBurdenLoadUnit': 'incrementBurdenLoadUnit',
        'IncrementLoadUnit': 'incrementLoadUnit',
        'InitialBurdenIncrementLoadRate': 'initialBurdenIncrementLoadRate',
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
        'LeaveDelayRefUnit': 'leaveDelayRefUnit',
        'LeaveDelayRefValue': 'leaveDelayRefValue',
        'LoadInitialRate': 'loadInitialRate',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxRate': 'maxRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'MldVersion': 'mldVersion',
        'Mldv2MessageType': 'mldv2MessageType',
        'Mldv2SourceAddrList': 'mldv2SourceAddrList',
        'NumAddresses': 'numAddresses',
        'NumIterations': 'numIterations',
        'NumberOfExtraJoins': 'numberOfExtraJoins',
        'Numtrials': 'numtrials',
        'OffsetTime': 'offsetTime',
        'PercentMaxRate': 'percentMaxRate',
        'ProtocolItem': 'protocolItem',
        'Rfc2889ordering': 'rfc2889ordering',
        'StaggeredStart': 'staggeredStart',
        'StepBurdenIncrementLoadRate': 'stepBurdenIncrementLoadRate',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TestTrafficType': 'testTrafficType',
        'TrafficBeforeJoinLeave': 'trafficBeforeJoinLeave',
        'TxDelay': 'txDelay',
        'Use3376mode': 'use3376mode',
        'UseMulticast': 'useMulticast',
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
        - str(accumulated | distributed): It gives details about the assigned group types
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
        - bool: It the bi directional option enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'])
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'], value)

    @property
    def BurdenFrameSize(self):
        """
        Returns
        -------
        - number: It gives details about the burden frame size
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurdenFrameSize'])
    @BurdenFrameSize.setter
    def BurdenFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurdenFrameSize'], value)

    @property
    def BurdenProtocolItems(self):
        """
        Returns
        -------
        - list(str): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurdenProtocolItems'])
    @BurdenProtocolItems.setter
    def BurdenProtocolItems(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurdenProtocolItems'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: It gives a count of the random frame sizes
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
        - number: It gives details about the delay after the transmission
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
        - number: It gives details about the delay between the Iterations
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
        - str(average | max): It gives details about the delay mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayMode'])
    @DelayMode.setter
    def DelayMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayMode'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The duration till of the test run
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableExtraJoinFrames(self):
        """
        Returns
        -------
        - bool: If true, It enables the extra join frames
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraJoinFrames'])
    @EnableExtraJoinFrames.setter
    def EnableExtraJoinFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraJoinFrames'], value)

    @property
    def EnableLeaveGroup(self):
        """
        Returns
        -------
        - bool: If True, it enables the leave group
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
        - bool: If true, it enables the minimum frame size
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
        - bool: NOT DEFINED
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
    def EnableRouterAlert(self):
        """
        Returns
        -------
        - bool: If true, It enables the router alert
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
        - str: It gives details about the extra First frame group address
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
        - str: It gives details about the extra First frame group address in IP version 6 version
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
        - number: It gives details about the extra frame total group address
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraFramesTotalGroupAddresses'])
    @ExtraFramesTotalGroupAddresses.setter
    def ExtraFramesTotalGroupAddresses(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraFramesTotalGroupAddresses'], value)

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
        - bool: It makes the test to force regenerate
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
        - str(custom | increment | random): It provides details about the frame size mode
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
        - list(str): It provides details about the list of frame size
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
        - number: It provides details about the protocols which are greater than group capacity
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
        - str(acrossHosts | acrossPorts): It gives details about the distribution group types
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
        - number: It gives details about the igmp v1 timeout
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
        - number: It provides details about the version of the igmp
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
        - number: It gives details about the Incrementing addresses
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
        - number: It gives details about the incremental step test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrStep'])
    @IncrStep.setter
    def IncrStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrStep'], value)

    @property
    def IncrementBurdenLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): It gives details about the incremental burden load unit
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementBurdenLoadUnit'])
    @IncrementBurdenLoadUnit.setter
    def IncrementBurdenLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementBurdenLoadUnit'], value)

    @property
    def IncrementLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): It gives details about the increment load unit
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementLoadUnit'])
    @IncrementLoadUnit.setter
    def IncrementLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementLoadUnit'], value)

    @property
    def InitialBurdenIncrementLoadRate(self):
        """
        Returns
        -------
        - number: It gives details about the initial burden incremental load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBurdenIncrementLoadRate'])
    @InitialBurdenIncrementLoadRate.setter
    def InitialBurdenIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBurdenIncrementLoadRate'], value)

    @property
    def InitialRate(self):
        """
        Returns
        -------
        - str: It provides details of the initial rate
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
        - str: It provides IP version 4 address
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
        - str: It provides IP version 6 address
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
        - str: It provides with the confirmation whether ipv6 address is in use
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
        - str: It provides details multicast automatic frame data is in use or not?
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
        - str(ms | ns | us): It gives details about the Join delay in Reference unit
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
        - number: It gives details about the Join delay in Reference value
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
        - str(joinExisting | joinNew): It gives details about the join leave algorithm in the test configuration
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
        - number: It gives details about the Join leave frames per group
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
        - str(join): It gives details about the join leave mode
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
        - number: It gives details about the join leave rate of the test configuration
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
        - number: It gives details about the join leave rate of the test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinLeaveWaitTime'])
    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinLeaveWaitTime'], value)

    @property
    def LeaveDelayRefUnit(self):
        """
        Returns
        -------
        - str(ms | ns | us): It gives details about the leave delay reference unit
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
        - number: It gives details about the leave delay reference value
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
        - number: It loads the initial rate in the test configuration
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
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): It gives details about the load type
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
        - str: The mapping type of the test configuration is displayed here
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
        - number: It gives details about the maximum increment in frame size
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
        - number: It provides details about the maximum random frame size
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
        - number: It gives the maximum rate
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
        - number: It gives details about the minimum increment in frame size
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
        - number: It provides details about the minimum random frame size
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
        - number: It provides details about the mld version
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
        - str(exclude | include): It gives details about the mldv2 message type in the test configuration
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
        - str: It gives details about the mldv2 source address list in the test configuration
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
        - number: It provides with the number addresses
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
        - number: It provides with the number of iterations
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumIterations'])
    @NumIterations.setter
    def NumIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumIterations'], value)

    @property
    def NumberOfExtraJoins(self):
        """
        Returns
        -------
        - number: It gives details about the number of extra joins
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
        - number: It provides with the number trials
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
        - number: It provides details about the off set time
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
        - number: It provides with the percentage of the maximum rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMaxRate'])
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentMaxRate'], value)

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
    def Rfc2889ordering(self):
        """
        Returns
        -------
        - str(val2889Ordering): The rfc 2889 ordering in the the test configuration is shown here
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2889ordering'])
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rfc2889ordering'], value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: It gives a staggered start to the test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStart'])
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStart'], value)

    @property
    def StepBurdenIncrementLoadRate(self):
        """
        Returns
        -------
        - number: It gives details about the step burden incremental load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepBurdenIncrementLoadRate'])
    @StepBurdenIncrementLoadRate.setter
    def StepBurdenIncrementLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepBurdenIncrementLoadRate'], value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: It gives details about the step increment in frame size
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
        - str: All the supported test types are displayed of the test configuration
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
        - bool: It gives details about the traffic reported before the Join Leave
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
        - number: It provides with the information of the delay the transmitter causes
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
    def UseMulticast(self):
        """
        Returns
        -------
        - bool: It uses Multicast for the test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseMulticast'])
    @UseMulticast.setter
    def UseMulticast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseMulticast'], value)

    def update(self, ApplyMode=None, AssignGroupType=None, BidirectionalOptionEnabled=None, BurdenFrameSize=None, BurdenProtocolItems=None, CountRandomFrameSize=None, DelayAfterTransmit=None, DelayBetweenIterations=None, DelayMode=None, Duration=None, EnableExtraJoinFrames=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastLearning=None, EnableMulticastQuerier=None, EnableRouterAlert=None, ExtraFramesFirstGroupAddress=None, ExtraFramesFirstGroupAddressIPv6=None, ExtraFramesTotalGroupAddresses=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameSizeMode=None, FramesizeList=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, IncrStep=None, IncrementBurdenLoadUnit=None, IncrementLoadUnit=None, InitialBurdenIncrementLoadRate=None, InitialRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinDelayRefUnit=None, JoinDelayRefValue=None, JoinLeaveAlgorithm=None, JoinLeaveFramesPerGroup=None, JoinLeaveMode=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LeaveDelayRefUnit=None, LeaveDelayRefValue=None, LoadInitialRate=None, LoadType=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MaxRate=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, MldVersion=None, Mldv2MessageType=None, Mldv2SourceAddrList=None, NumAddresses=None, NumIterations=None, NumberOfExtraJoins=None, Numtrials=None, OffsetTime=None, PercentMaxRate=None, ProtocolItem=None, Rfc2889ordering=None, StaggeredStart=None, StepBurdenIncrementLoadRate=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, TestTrafficType=None, TrafficBeforeJoinLeave=None, TxDelay=None, Use3376mode=None, UseMulticast=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): It gives details about the assigned group types
        - BidirectionalOptionEnabled (bool): It the bi directional option enabled
        - BurdenFrameSize (number): It gives details about the burden frame size
        - BurdenProtocolItems (list(str)): NOT DEFINED
        - CountRandomFrameSize (number): It gives a count of the random frame sizes
        - DelayAfterTransmit (number): It gives details about the delay after the transmission
        - DelayBetweenIterations (number): It gives details about the delay between the Iterations
        - DelayMode (str(average | max)): It gives details about the delay mode
        - Duration (number): The duration till of the test run
        - EnableExtraJoinFrames (bool): If true, It enables the extra join frames
        - EnableLeaveGroup (bool): If True, it enables the leave group
        - EnableMinFrameSize (bool): If true, it enables the minimum frame size
        - EnableMulticastLearning (bool): NOT DEFINED
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableRouterAlert (bool): If true, It enables the router alert
        - ExtraFramesFirstGroupAddress (str): It gives details about the extra First frame group address
        - ExtraFramesFirstGroupAddressIPv6 (str): It gives details about the extra First frame group address in IP version 6 version
        - ExtraFramesTotalGroupAddresses (number): It gives details about the extra frame total group address
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): It makes the test to force regenerate
        - FrameSizeMode (str(custom | increment | random)): It provides details about the frame size mode
        - FramesizeList (list(str)): It provides details about the list of frame size
        - GroupCapacityGreaterThan (number): It provides details about the protocols which are greater than group capacity
        - GroupDistributionType (str(acrossHosts | acrossPorts)): It gives details about the distribution group types
        - IgmpV1Timeout (number): It gives details about the igmp v1 timeout
        - IgmpVersion (number): It provides details about the version of the igmp
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (number): It gives details about the Incrementing addresses
        - IncrStep (number): It gives details about the incremental step test configuration
        - IncrementBurdenLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): It gives details about the incremental burden load unit
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): It gives details about the increment load unit
        - InitialBurdenIncrementLoadRate (number): It gives details about the initial burden incremental load rate
        - InitialRate (str): It provides details of the initial rate
        - Ipv4Address (str): It provides IP version 4 address
        - Ipv6Address (str): It provides IP version 6 address
        - IsIPv6 (str): It provides with the confirmation whether ipv6 address is in use
        - IsMulticastAutomaticFrameData (str): It provides details multicast automatic frame data is in use or not?
        - JoinDelayRefUnit (str(ms | ns | us)): It gives details about the Join delay in Reference unit
        - JoinDelayRefValue (number): It gives details about the Join delay in Reference value
        - JoinLeaveAlgorithm (str(joinExisting | joinNew)): It gives details about the join leave algorithm in the test configuration
        - JoinLeaveFramesPerGroup (number): It gives details about the Join leave frames per group
        - JoinLeaveMode (str(join)): It gives details about the join leave mode
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): It gives details about the join leave rate of the test configuration
        - JoinLeaveWaitTime (number): It gives details about the join leave rate of the test configuration
        - LeaveDelayRefUnit (str(ms | ns | us)): It gives details about the leave delay reference unit
        - LeaveDelayRefValue (number): It gives details about the leave delay reference value
        - LoadInitialRate (number): It loads the initial rate in the test configuration
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): It gives details about the load type
        - MapType (str): The mapping type of the test configuration is displayed here
        - MaxIncrementFrameSize (number): It gives details about the maximum increment in frame size
        - MaxRandomFrameSize (number): It provides details about the maximum random frame size
        - MaxRate (number): It gives the maximum rate
        - MinIncrementFrameSize (number): It gives details about the minimum increment in frame size
        - MinRandomFrameSize (number): It provides details about the minimum random frame size
        - MldVersion (number): It provides details about the mld version
        - Mldv2MessageType (str(exclude | include)): It gives details about the mldv2 message type in the test configuration
        - Mldv2SourceAddrList (str): It gives details about the mldv2 source address list in the test configuration
        - NumAddresses (number): It provides with the number addresses
        - NumIterations (number): It provides with the number of iterations
        - NumberOfExtraJoins (number): It gives details about the number of extra joins
        - Numtrials (number): It provides with the number trials
        - OffsetTime (number): It provides details about the off set time
        - PercentMaxRate (number): It provides with the percentage of the maximum rate
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - Rfc2889ordering (str(val2889Ordering)): The rfc 2889 ordering in the the test configuration is shown here
        - StaggeredStart (bool): It gives a staggered start to the test configuration
        - StepBurdenIncrementLoadRate (number): It gives details about the step burden incremental load rate
        - StepIncrementFrameSize (number): It gives details about the step increment in frame size
        - SupportedTrafficTypes (str): All the supported test types are displayed of the test configuration
        - TestTrafficType (str): It signifies the test traffic type value.
        - TrafficBeforeJoinLeave (bool): It gives details about the traffic reported before the Join Leave
        - TxDelay (number): It provides with the information of the delay the transmitter causes
        - Use3376mode (bool): 
        - UseMulticast (bool): It uses Multicast for the test configuration

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
