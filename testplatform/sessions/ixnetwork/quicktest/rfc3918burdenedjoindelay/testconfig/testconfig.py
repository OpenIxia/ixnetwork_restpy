# Copyright 1997 - 2018 by IXIA Keysight
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
	"""The TestConfig class encapsulates a required testConfig node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TestConfig property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'testConfig'

	def __init__(self, parent):
		super(TestConfig, self).__init__(parent)

	@property
	def ApplyMode(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('applyMode')
	@ApplyMode.setter
	def ApplyMode(self, value):
		self._set_attribute('applyMode', value)

	@property
	def AssignGroupType(self):
		"""It gives details about the assigned group types

		Returns:
			str(accumulated|distributed)
		"""
		return self._get_attribute('assignGroupType')
	@AssignGroupType.setter
	def AssignGroupType(self, value):
		self._set_attribute('assignGroupType', value)

	@property
	def BidirectionalOptionEnabled(self):
		"""It the bi directional option enabled

		Returns:
			bool
		"""
		return self._get_attribute('bidirectionalOptionEnabled')
	@BidirectionalOptionEnabled.setter
	def BidirectionalOptionEnabled(self, value):
		self._set_attribute('bidirectionalOptionEnabled', value)

	@property
	def BurdenFrameSize(self):
		"""It gives details about the burden frame size

		Returns:
			number
		"""
		return self._get_attribute('burdenFrameSize')
	@BurdenFrameSize.setter
	def BurdenFrameSize(self, value):
		self._set_attribute('burdenFrameSize', value)

	@property
	def BurdenProtocolItems(self):
		"""NOT DEFINED

		Returns:
			list(str)
		"""
		return self._get_attribute('burdenProtocolItems')
	@BurdenProtocolItems.setter
	def BurdenProtocolItems(self, value):
		self._set_attribute('burdenProtocolItems', value)

	@property
	def CountRandomFrameSize(self):
		"""It gives a count of the random frame sizes

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def DelayAfterTransmit(self):
		"""It gives details about the delay after the transmission

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DelayBetweenIterations(self):
		"""It gives details about the delay between the Iterations

		Returns:
			number
		"""
		return self._get_attribute('delayBetweenIterations')
	@DelayBetweenIterations.setter
	def DelayBetweenIterations(self, value):
		self._set_attribute('delayBetweenIterations', value)

	@property
	def DelayMode(self):
		"""It gives details about the delay mode

		Returns:
			str(average|max)
		"""
		return self._get_attribute('delayMode')
	@DelayMode.setter
	def DelayMode(self, value):
		self._set_attribute('delayMode', value)

	@property
	def Duration(self):
		"""The duration till of the test run

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableExtraJoinFrames(self):
		"""If true, It enables the extra join frames

		Returns:
			bool
		"""
		return self._get_attribute('enableExtraJoinFrames')
	@EnableExtraJoinFrames.setter
	def EnableExtraJoinFrames(self, value):
		self._set_attribute('enableExtraJoinFrames', value)

	@property
	def EnableLeaveGroup(self):
		"""If True, it enables the leave group

		Returns:
			bool
		"""
		return self._get_attribute('enableLeaveGroup')
	@EnableLeaveGroup.setter
	def EnableLeaveGroup(self, value):
		self._set_attribute('enableLeaveGroup', value)

	@property
	def EnableMinFrameSize(self):
		"""If true, it enables the minimum frame size

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableMulticastLearning(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticastLearning')
	@EnableMulticastLearning.setter
	def EnableMulticastLearning(self, value):
		self._set_attribute('enableMulticastLearning', value)

	@property
	def EnableMulticastQuerier(self):
		"""Enable Multicast Querier Settings

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticastQuerier')
	@EnableMulticastQuerier.setter
	def EnableMulticastQuerier(self, value):
		self._set_attribute('enableMulticastQuerier', value)

	@property
	def EnableRouterAlert(self):
		"""If true, It enables the router alert

		Returns:
			bool
		"""
		return self._get_attribute('enableRouterAlert')
	@EnableRouterAlert.setter
	def EnableRouterAlert(self, value):
		self._set_attribute('enableRouterAlert', value)

	@property
	def ExtraFramesFirstGroupAddress(self):
		"""It gives details about the extra First frame group address

		Returns:
			str
		"""
		return self._get_attribute('extraFramesFirstGroupAddress')
	@ExtraFramesFirstGroupAddress.setter
	def ExtraFramesFirstGroupAddress(self, value):
		self._set_attribute('extraFramesFirstGroupAddress', value)

	@property
	def ExtraFramesFirstGroupAddressIPv6(self):
		"""It gives details about the extra First frame group address in IP version 6 version

		Returns:
			str
		"""
		return self._get_attribute('extraFramesFirstGroupAddressIPv6')
	@ExtraFramesFirstGroupAddressIPv6.setter
	def ExtraFramesFirstGroupAddressIPv6(self, value):
		self._set_attribute('extraFramesFirstGroupAddressIPv6', value)

	@property
	def ExtraFramesTotalGroupAddresses(self):
		"""It gives details about the extra frame total group address

		Returns:
			number
		"""
		return self._get_attribute('extraFramesTotalGroupAddresses')
	@ExtraFramesTotalGroupAddresses.setter
	def ExtraFramesTotalGroupAddresses(self, value):
		self._set_attribute('extraFramesTotalGroupAddresses', value)

	@property
	def FloodedFramesEnabled(self):
		"""If true, it enables the flooded frames statistics

		Returns:
			bool
		"""
		return self._get_attribute('floodedFramesEnabled')
	@FloodedFramesEnabled.setter
	def FloodedFramesEnabled(self, value):
		self._set_attribute('floodedFramesEnabled', value)

	@property
	def ForceRegenerate(self):
		"""It makes the test to force regenerate

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameSizeMode(self):
		"""It provides details about the frame size mode

		Returns:
			str(custom|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesizeList(self):
		"""It provides details about the list of frame size

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def GroupCapacityGreaterThan(self):
		"""It provides details about the protocols which are greater than group capacity

		Returns:
			number
		"""
		return self._get_attribute('groupCapacityGreaterThan')
	@GroupCapacityGreaterThan.setter
	def GroupCapacityGreaterThan(self, value):
		self._set_attribute('groupCapacityGreaterThan', value)

	@property
	def GroupDistributionType(self):
		"""It gives details about the distribution group types

		Returns:
			str(acrossHosts|acrossPorts)
		"""
		return self._get_attribute('groupDistributionType')
	@GroupDistributionType.setter
	def GroupDistributionType(self, value):
		self._set_attribute('groupDistributionType', value)

	@property
	def IgmpV1Timeout(self):
		"""It gives details about the igmp v1 timeout

		Returns:
			number
		"""
		return self._get_attribute('igmpV1Timeout')
	@IgmpV1Timeout.setter
	def IgmpV1Timeout(self, value):
		self._set_attribute('igmpV1Timeout', value)

	@property
	def IgmpVersion(self):
		"""It provides details about the version of the igmp

		Returns:
			number
		"""
		return self._get_attribute('igmpVersion')
	@IgmpVersion.setter
	def IgmpVersion(self, value):
		self._set_attribute('igmpVersion', value)

	@property
	def Igmpv3MessageType(self):
		"""It gives details about the igmpv3 message type in the test configuration

		Returns:
			str(exclude|include)
		"""
		return self._get_attribute('igmpv3MessageType')
	@Igmpv3MessageType.setter
	def Igmpv3MessageType(self, value):
		self._set_attribute('igmpv3MessageType', value)

	@property
	def Igmpv3SourceAddrList(self):
		"""It gives details about the igmpv3 source address list in the test configuration

		Returns:
			str
		"""
		return self._get_attribute('igmpv3SourceAddrList')
	@Igmpv3SourceAddrList.setter
	def Igmpv3SourceAddrList(self, value):
		self._set_attribute('igmpv3SourceAddrList', value)

	@property
	def IncrAddresses(self):
		"""It gives details about the Incrementing addresses

		Returns:
			number
		"""
		return self._get_attribute('incrAddresses')
	@IncrAddresses.setter
	def IncrAddresses(self, value):
		self._set_attribute('incrAddresses', value)

	@property
	def IncrStep(self):
		"""It gives details about the incremental step test configuration

		Returns:
			number
		"""
		return self._get_attribute('incrStep')
	@IncrStep.setter
	def IncrStep(self, value):
		self._set_attribute('incrStep', value)

	@property
	def IncrementBurdenLoadUnit(self):
		"""It gives details about the incremental burden load unit

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementBurdenLoadUnit')
	@IncrementBurdenLoadUnit.setter
	def IncrementBurdenLoadUnit(self, value):
		self._set_attribute('incrementBurdenLoadUnit', value)

	@property
	def IncrementLoadUnit(self):
		"""It gives details about the increment load unit

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

	@property
	def InitialBurdenIncrementLoadRate(self):
		"""It gives details about the initial burden incremental load rate

		Returns:
			number
		"""
		return self._get_attribute('initialBurdenIncrementLoadRate')
	@InitialBurdenIncrementLoadRate.setter
	def InitialBurdenIncrementLoadRate(self, value):
		self._set_attribute('initialBurdenIncrementLoadRate', value)

	@property
	def InitialRate(self):
		"""It provides details of the initial rate

		Returns:
			str
		"""
		return self._get_attribute('initialRate')
	@InitialRate.setter
	def InitialRate(self, value):
		self._set_attribute('initialRate', value)

	@property
	def Ipv4Address(self):
		"""It provides IP version 4 address

		Returns:
			str
		"""
		return self._get_attribute('ipv4Address')
	@Ipv4Address.setter
	def Ipv4Address(self, value):
		self._set_attribute('ipv4Address', value)

	@property
	def Ipv6Address(self):
		"""It provides IP version 6 address

		Returns:
			str
		"""
		return self._get_attribute('ipv6Address')
	@Ipv6Address.setter
	def Ipv6Address(self, value):
		self._set_attribute('ipv6Address', value)

	@property
	def IsIPv6(self):
		"""It provides with the confirmation whether ipv6 address is in use

		Returns:
			str
		"""
		return self._get_attribute('isIPv6')
	@IsIPv6.setter
	def IsIPv6(self, value):
		self._set_attribute('isIPv6', value)

	@property
	def IsMulticastAutomaticFrameData(self):
		"""It provides details multicast automatic frame data is in use or not?

		Returns:
			str
		"""
		return self._get_attribute('isMulticastAutomaticFrameData')
	@IsMulticastAutomaticFrameData.setter
	def IsMulticastAutomaticFrameData(self, value):
		self._set_attribute('isMulticastAutomaticFrameData', value)

	@property
	def JoinDelayRefUnit(self):
		"""It gives details about the Join delay in Reference unit

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('joinDelayRefUnit')
	@JoinDelayRefUnit.setter
	def JoinDelayRefUnit(self, value):
		self._set_attribute('joinDelayRefUnit', value)

	@property
	def JoinDelayRefValue(self):
		"""It gives details about the Join delay in Reference value

		Returns:
			number
		"""
		return self._get_attribute('joinDelayRefValue')
	@JoinDelayRefValue.setter
	def JoinDelayRefValue(self, value):
		self._set_attribute('joinDelayRefValue', value)

	@property
	def JoinLeaveAlgorithm(self):
		"""It gives details about the join leave algorithm in the test configuration

		Returns:
			str(joinExisting|joinNew)
		"""
		return self._get_attribute('joinLeaveAlgorithm')
	@JoinLeaveAlgorithm.setter
	def JoinLeaveAlgorithm(self, value):
		self._set_attribute('joinLeaveAlgorithm', value)

	@property
	def JoinLeaveFramesPerGroup(self):
		"""It gives details about the Join leave frames per group

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveFramesPerGroup')
	@JoinLeaveFramesPerGroup.setter
	def JoinLeaveFramesPerGroup(self, value):
		self._set_attribute('joinLeaveFramesPerGroup', value)

	@property
	def JoinLeaveMode(self):
		"""It gives details about the join leave mode

		Returns:
			str(join)
		"""
		return self._get_attribute('joinLeaveMode')
	@JoinLeaveMode.setter
	def JoinLeaveMode(self, value):
		self._set_attribute('joinLeaveMode', value)

	@property
	def JoinLeaveMultiplier(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveMultiplier')
	@JoinLeaveMultiplier.setter
	def JoinLeaveMultiplier(self, value):
		self._set_attribute('joinLeaveMultiplier', value)

	@property
	def JoinLeaveRate(self):
		"""It gives details about the join leave rate of the test configuration

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveRate')
	@JoinLeaveRate.setter
	def JoinLeaveRate(self, value):
		self._set_attribute('joinLeaveRate', value)

	@property
	def JoinLeaveWaitTime(self):
		"""It gives details about the join leave rate of the test configuration

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveWaitTime')
	@JoinLeaveWaitTime.setter
	def JoinLeaveWaitTime(self, value):
		self._set_attribute('joinLeaveWaitTime', value)

	@property
	def LeaveDelayRefUnit(self):
		"""It gives details about the leave delay reference unit

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('leaveDelayRefUnit')
	@LeaveDelayRefUnit.setter
	def LeaveDelayRefUnit(self, value):
		self._set_attribute('leaveDelayRefUnit', value)

	@property
	def LeaveDelayRefValue(self):
		"""It gives details about the leave delay reference value

		Returns:
			number
		"""
		return self._get_attribute('leaveDelayRefValue')
	@LeaveDelayRefValue.setter
	def LeaveDelayRefValue(self, value):
		self._set_attribute('leaveDelayRefValue', value)

	@property
	def LoadInitialRate(self):
		"""It loads the initial rate in the test configuration

		Returns:
			number
		"""
		return self._get_attribute('loadInitialRate')
	@LoadInitialRate.setter
	def LoadInitialRate(self, value):
		self._set_attribute('loadInitialRate', value)

	@property
	def LoadType(self):
		"""It gives details about the load type

		Returns:
			str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""The mapping type of the test configuration is displayed here

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxIncrementFrameSize(self):
		"""It gives details about the maximum increment in frame size

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxRandomFrameSize(self):
		"""It provides details about the maximum random frame size

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MaxRate(self):
		"""It gives the maximum rate

		Returns:
			number
		"""
		return self._get_attribute('maxRate')
	@MaxRate.setter
	def MaxRate(self, value):
		self._set_attribute('maxRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""It gives details about the minimum increment in frame size

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinRandomFrameSize(self):
		"""It provides details about the minimum random frame size

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def MldVersion(self):
		"""It provides details about the mld version

		Returns:
			number
		"""
		return self._get_attribute('mldVersion')
	@MldVersion.setter
	def MldVersion(self, value):
		self._set_attribute('mldVersion', value)

	@property
	def Mldv2MessageType(self):
		"""It gives details about the mldv2 message type in the test configuration

		Returns:
			str(exclude|include)
		"""
		return self._get_attribute('mldv2MessageType')
	@Mldv2MessageType.setter
	def Mldv2MessageType(self, value):
		self._set_attribute('mldv2MessageType', value)

	@property
	def Mldv2SourceAddrList(self):
		"""It gives details about the mldv2 source address list in the test configuration

		Returns:
			str
		"""
		return self._get_attribute('mldv2SourceAddrList')
	@Mldv2SourceAddrList.setter
	def Mldv2SourceAddrList(self, value):
		self._set_attribute('mldv2SourceAddrList', value)

	@property
	def NumAddresses(self):
		"""It provides with the number addresses

		Returns:
			number
		"""
		return self._get_attribute('numAddresses')
	@NumAddresses.setter
	def NumAddresses(self, value):
		self._set_attribute('numAddresses', value)

	@property
	def NumIterations(self):
		"""It provides with the number of iterations

		Returns:
			number
		"""
		return self._get_attribute('numIterations')
	@NumIterations.setter
	def NumIterations(self, value):
		self._set_attribute('numIterations', value)

	@property
	def NumberOfExtraJoins(self):
		"""It gives details about the number of extra joins

		Returns:
			number
		"""
		return self._get_attribute('numberOfExtraJoins')
	@NumberOfExtraJoins.setter
	def NumberOfExtraJoins(self, value):
		self._set_attribute('numberOfExtraJoins', value)

	@property
	def Numtrials(self):
		"""It provides with the number trials

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def OffsetTime(self):
		"""It provides details about the off set time

		Returns:
			number
		"""
		return self._get_attribute('offsetTime')
	@OffsetTime.setter
	def OffsetTime(self, value):
		self._set_attribute('offsetTime', value)

	@property
	def PercentMaxRate(self):
		"""It provides with the percentage of the maximum rate

		Returns:
			number
		"""
		return self._get_attribute('percentMaxRate')
	@PercentMaxRate.setter
	def PercentMaxRate(self, value):
		self._set_attribute('percentMaxRate', value)

	@property
	def ProtocolItem(self):
		"""Protocol Items

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])
		"""
		return self._get_attribute('protocolItem')
	@ProtocolItem.setter
	def ProtocolItem(self, value):
		self._set_attribute('protocolItem', value)

	@property
	def Rfc2889ordering(self):
		"""The rfc 2889 ordering in the the test configuration is shown here

		Returns:
			str(val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def StaggeredStart(self):
		"""It gives a staggered start to the test configuration

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def StepBurdenIncrementLoadRate(self):
		"""It gives details about the step burden incremental load rate

		Returns:
			number
		"""
		return self._get_attribute('stepBurdenIncrementLoadRate')
	@StepBurdenIncrementLoadRate.setter
	def StepBurdenIncrementLoadRate(self, value):
		self._set_attribute('stepBurdenIncrementLoadRate', value)

	@property
	def StepIncrementFrameSize(self):
		"""It gives details about the step increment in frame size

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def SupportedTrafficTypes(self):
		"""All the supported test types are displayed of the test configuration

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def TestTrafficType(self):
		"""It signifies the test traffic type value.

		Returns:
			str
		"""
		return self._get_attribute('testTrafficType')
	@TestTrafficType.setter
	def TestTrafficType(self, value):
		self._set_attribute('testTrafficType', value)

	@property
	def TrafficBeforeJoinLeave(self):
		"""It gives details about the traffic reported before the Join Leave

		Returns:
			bool
		"""
		return self._get_attribute('trafficBeforeJoinLeave')
	@TrafficBeforeJoinLeave.setter
	def TrafficBeforeJoinLeave(self, value):
		self._set_attribute('trafficBeforeJoinLeave', value)

	@property
	def TxDelay(self):
		"""It provides with the information of the delay the transmitter causes

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def Use3376mode(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('use3376mode')
	@Use3376mode.setter
	def Use3376mode(self, value):
		self._set_attribute('use3376mode', value)

	@property
	def UseMulticast(self):
		"""It uses Multicast for the test configuration

		Returns:
			bool
		"""
		return self._get_attribute('useMulticast')
	@UseMulticast.setter
	def UseMulticast(self, value):
		self._set_attribute('useMulticast', value)

	def update(self, ApplyMode=None, AssignGroupType=None, BidirectionalOptionEnabled=None, BurdenFrameSize=None, BurdenProtocolItems=None, CountRandomFrameSize=None, DelayAfterTransmit=None, DelayBetweenIterations=None, DelayMode=None, Duration=None, EnableExtraJoinFrames=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastLearning=None, EnableMulticastQuerier=None, EnableRouterAlert=None, ExtraFramesFirstGroupAddress=None, ExtraFramesFirstGroupAddressIPv6=None, ExtraFramesTotalGroupAddresses=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameSizeMode=None, FramesizeList=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, IncrStep=None, IncrementBurdenLoadUnit=None, IncrementLoadUnit=None, InitialBurdenIncrementLoadRate=None, InitialRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinDelayRefUnit=None, JoinDelayRefValue=None, JoinLeaveAlgorithm=None, JoinLeaveFramesPerGroup=None, JoinLeaveMode=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LeaveDelayRefUnit=None, LeaveDelayRefValue=None, LoadInitialRate=None, LoadType=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MaxRate=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, MldVersion=None, Mldv2MessageType=None, Mldv2SourceAddrList=None, NumAddresses=None, NumIterations=None, NumberOfExtraJoins=None, Numtrials=None, OffsetTime=None, PercentMaxRate=None, ProtocolItem=None, Rfc2889ordering=None, StaggeredStart=None, StepBurdenIncrementLoadRate=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, TestTrafficType=None, TrafficBeforeJoinLeave=None, TxDelay=None, Use3376mode=None, UseMulticast=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			ApplyMode (str): NOT DEFINED
			AssignGroupType (str(accumulated|distributed)): It gives details about the assigned group types
			BidirectionalOptionEnabled (bool): It the bi directional option enabled
			BurdenFrameSize (number): It gives details about the burden frame size
			BurdenProtocolItems (list(str)): NOT DEFINED
			CountRandomFrameSize (number): It gives a count of the random frame sizes
			DelayAfterTransmit (number): It gives details about the delay after the transmission
			DelayBetweenIterations (number): It gives details about the delay between the Iterations
			DelayMode (str(average|max)): It gives details about the delay mode
			Duration (number): The duration till of the test run
			EnableExtraJoinFrames (bool): If true, It enables the extra join frames
			EnableLeaveGroup (bool): If True, it enables the leave group
			EnableMinFrameSize (bool): If true, it enables the minimum frame size
			EnableMulticastLearning (bool): NOT DEFINED
			EnableMulticastQuerier (bool): Enable Multicast Querier Settings
			EnableRouterAlert (bool): If true, It enables the router alert
			ExtraFramesFirstGroupAddress (str): It gives details about the extra First frame group address
			ExtraFramesFirstGroupAddressIPv6 (str): It gives details about the extra First frame group address in IP version 6 version
			ExtraFramesTotalGroupAddresses (number): It gives details about the extra frame total group address
			FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
			ForceRegenerate (bool): It makes the test to force regenerate
			FrameSizeMode (str(custom|increment|random)): It provides details about the frame size mode
			FramesizeList (list(str)): It provides details about the list of frame size
			GroupCapacityGreaterThan (number): It provides details about the protocols which are greater than group capacity
			GroupDistributionType (str(acrossHosts|acrossPorts)): It gives details about the distribution group types
			IgmpV1Timeout (number): It gives details about the igmp v1 timeout
			IgmpVersion (number): It provides details about the version of the igmp
			Igmpv3MessageType (str(exclude|include)): It gives details about the igmpv3 message type in the test configuration
			Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
			IncrAddresses (number): It gives details about the Incrementing addresses
			IncrStep (number): It gives details about the incremental step test configuration
			IncrementBurdenLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): It gives details about the incremental burden load unit
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): It gives details about the increment load unit
			InitialBurdenIncrementLoadRate (number): It gives details about the initial burden incremental load rate
			InitialRate (str): It provides details of the initial rate
			Ipv4Address (str): It provides IP version 4 address
			Ipv6Address (str): It provides IP version 6 address
			IsIPv6 (str): It provides with the confirmation whether ipv6 address is in use
			IsMulticastAutomaticFrameData (str): It provides details multicast automatic frame data is in use or not?
			JoinDelayRefUnit (str(ms|ns|us)): It gives details about the Join delay in Reference unit
			JoinDelayRefValue (number): It gives details about the Join delay in Reference value
			JoinLeaveAlgorithm (str(joinExisting|joinNew)): It gives details about the join leave algorithm in the test configuration
			JoinLeaveFramesPerGroup (number): It gives details about the Join leave frames per group
			JoinLeaveMode (str(join)): It gives details about the join leave mode
			JoinLeaveMultiplier (number): NOT DEFINED
			JoinLeaveRate (number): It gives details about the join leave rate of the test configuration
			JoinLeaveWaitTime (number): It gives details about the join leave rate of the test configuration
			LeaveDelayRefUnit (str(ms|ns|us)): It gives details about the leave delay reference unit
			LeaveDelayRefValue (number): It gives details about the leave delay reference value
			LoadInitialRate (number): It loads the initial rate in the test configuration
			LoadType (str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)): It gives details about the load type
			MapType (str): The mapping type of the test configuration is displayed here
			MaxIncrementFrameSize (number): It gives details about the maximum increment in frame size
			MaxRandomFrameSize (number): It provides details about the maximum random frame size
			MaxRate (number): It gives the maximum rate
			MinIncrementFrameSize (number): It gives details about the minimum increment in frame size
			MinRandomFrameSize (number): It provides details about the minimum random frame size
			MldVersion (number): It provides details about the mld version
			Mldv2MessageType (str(exclude|include)): It gives details about the mldv2 message type in the test configuration
			Mldv2SourceAddrList (str): It gives details about the mldv2 source address list in the test configuration
			NumAddresses (number): It provides with the number addresses
			NumIterations (number): It provides with the number of iterations
			NumberOfExtraJoins (number): It gives details about the number of extra joins
			Numtrials (number): It provides with the number trials
			OffsetTime (number): It provides details about the off set time
			PercentMaxRate (number): It provides with the percentage of the maximum rate
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			Rfc2889ordering (str(val2889Ordering)): The rfc 2889 ordering in the the test configuration is shown here
			StaggeredStart (bool): It gives a staggered start to the test configuration
			StepBurdenIncrementLoadRate (number): It gives details about the step burden incremental load rate
			StepIncrementFrameSize (number): It gives details about the step increment in frame size
			SupportedTrafficTypes (str): All the supported test types are displayed of the test configuration
			TestTrafficType (str): It signifies the test traffic type value.
			TrafficBeforeJoinLeave (bool): It gives details about the traffic reported before the Join Leave
			TxDelay (number): It provides with the information of the delay the transmitter causes
			Use3376mode (bool): 
			UseMulticast (bool): It uses Multicast for the test configuration

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Apply(self):
		"""Executes the apply operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('apply', payload=payload, response_object=None)

	def ApplyAsync(self):
		"""Executes the applyAsync operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsync', payload=payload, response_object=None)

	def ApplyAsyncResult(self):
		"""Executes the applyAsyncResult operation on the server.

			Returns:
				bool: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsyncResult', payload=payload, response_object=None)

	def ApplyITWizardConfiguration(self):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		Generate a PDF report for the last succesfull test run.

			Returns:
				str: This method is asynchronous and has no return value.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('generateReport', payload=payload, response_object=None)

	def Run(self, *args, **kwargs):
		"""Executes the run operation on the server.

		Starts the specified Quick Test and waits for its execution to finish.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		run()list

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		run(InputParameters:string)list
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('run', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Starts the specified Quick Test.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(InputParameters:string)
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)

	def WaitForTest(self):
		"""Executes the waitForTest operation on the server.

		Waits for the execution of the specified Quick Test to be completed.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('waitForTest', payload=payload, response_object=None)
