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
		"""NOT DEFINED

		Returns:
			str(accumulated|distributed)
		"""
		return self._get_attribute('assignGroupType')
	@AssignGroupType.setter
	def AssignGroupType(self, value):
		self._set_attribute('assignGroupType', value)

	@property
	def BidirectionalOptionEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('bidirectionalOptionEnabled')
	@BidirectionalOptionEnabled.setter
	def BidirectionalOptionEnabled(self, value):
		self._set_attribute('bidirectionalOptionEnabled', value)

	@property
	def BurdenFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('burdenFrameSize')
	@BurdenFrameSize.setter
	def BurdenFrameSize(self, value):
		self._set_attribute('burdenFrameSize', value)

	@property
	def BurstSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CalculateJitter(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('calculateJitter')
	@CalculateJitter.setter
	def CalculateJitter(self, value):
		self._set_attribute('calculateJitter', value)

	@property
	def CalculateLatency(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def CountRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def DelayAfterTransmit(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def Duration(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableDataIntegrity(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableLayer1Rate(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableLayer1Rate')
	@EnableLayer1Rate.setter
	def EnableLayer1Rate(self, value):
		self._set_attribute('enableLayer1Rate', value)

	@property
	def EnableLeaveGroup(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableLeaveGroup')
	@EnableLeaveGroup.setter
	def EnableLeaveGroup(self, value):
		self._set_attribute('enableLeaveGroup', value)

	@property
	def EnableMinFrameSize(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableMulticastQuerier(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticastQuerier')
	@EnableMulticastQuerier.setter
	def EnableMulticastQuerier(self, value):
		self._set_attribute('enableMulticastQuerier', value)

	@property
	def EnableOldStatsForReef(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def FloodedFramesEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('floodedFramesEnabled')
	@FloodedFramesEnabled.setter
	def FloodedFramesEnabled(self, value):
		self._set_attribute('floodedFramesEnabled', value)

	@property
	def ForceRegenerate(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameSizeMode(self):
		"""NOT DEFINED

		Returns:
			str(custom|customlist|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesizeList(self):
		"""NOT DEFINED

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def Gap(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GroupCapacityGreaterThan(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('groupCapacityGreaterThan')
	@GroupCapacityGreaterThan.setter
	def GroupCapacityGreaterThan(self, value):
		self._set_attribute('groupCapacityGreaterThan', value)

	@property
	def GroupDistributionType(self):
		"""NOT DEFINED

		Returns:
			str(acrossHosts|acrossPorts)
		"""
		return self._get_attribute('groupDistributionType')
	@GroupDistributionType.setter
	def GroupDistributionType(self, value):
		self._set_attribute('groupDistributionType', value)

	@property
	def IgmpV1Timeout(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('igmpV1Timeout')
	@IgmpV1Timeout.setter
	def IgmpV1Timeout(self, value):
		self._set_attribute('igmpV1Timeout', value)

	@property
	def IgmpVersion(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('igmpVersion')
	@IgmpVersion.setter
	def IgmpVersion(self, value):
		self._set_attribute('igmpVersion', value)

	@property
	def Igmpv3MessageType(self):
		"""NOT DEFINED

		Returns:
			str(exclude|include)
		"""
		return self._get_attribute('igmpv3MessageType')
	@Igmpv3MessageType.setter
	def Igmpv3MessageType(self, value):
		self._set_attribute('igmpv3MessageType', value)

	@property
	def Igmpv3SourceAddrList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('igmpv3SourceAddrList')
	@Igmpv3SourceAddrList.setter
	def Igmpv3SourceAddrList(self, value):
		self._set_attribute('igmpv3SourceAddrList', value)

	@property
	def IncrAddresses(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('incrAddresses')
	@IncrAddresses.setter
	def IncrAddresses(self, value):
		self._set_attribute('incrAddresses', value)

	@property
	def IncrementBurdenLoadUnit(self):
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementBurdenLoadUnit')
	@IncrementBurdenLoadUnit.setter
	def IncrementBurdenLoadUnit(self, value):
		self._set_attribute('incrementBurdenLoadUnit', value)

	@property
	def IncrementLoadUnit(self):
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

	@property
	def InitialBurdenIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('initialBurdenIncrementLoadRate')
	@InitialBurdenIncrementLoadRate.setter
	def InitialBurdenIncrementLoadRate(self, value):
		self._set_attribute('initialBurdenIncrementLoadRate', value)

	@property
	def InitialIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('initialIncrementLoadRate')
	@InitialIncrementLoadRate.setter
	def InitialIncrementLoadRate(self, value):
		self._set_attribute('initialIncrementLoadRate', value)

	@property
	def InitialRate(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('initialRate')
	@InitialRate.setter
	def InitialRate(self, value):
		self._set_attribute('initialRate', value)

	@property
	def Ipv4Address(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('ipv4Address')
	@Ipv4Address.setter
	def Ipv4Address(self, value):
		self._set_attribute('ipv4Address', value)

	@property
	def Ipv6Address(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('ipv6Address')
	@Ipv6Address.setter
	def Ipv6Address(self, value):
		self._set_attribute('ipv6Address', value)

	@property
	def IsIPv6(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('isIPv6')
	@IsIPv6.setter
	def IsIPv6(self, value):
		self._set_attribute('isIPv6', value)

	@property
	def IsMulticastAutomaticFrameData(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('isMulticastAutomaticFrameData')
	@IsMulticastAutomaticFrameData.setter
	def IsMulticastAutomaticFrameData(self, value):
		self._set_attribute('isMulticastAutomaticFrameData', value)

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
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveRate')
	@JoinLeaveRate.setter
	def JoinLeaveRate(self, value):
		self._set_attribute('joinLeaveRate', value)

	@property
	def JoinLeaveWaitTime(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('joinLeaveWaitTime')
	@JoinLeaveWaitTime.setter
	def JoinLeaveWaitTime(self, value):
		self._set_attribute('joinLeaveWaitTime', value)

	@property
	def LatencyBins(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('latencyBins')
	@LatencyBins.setter
	def LatencyBins(self, value):
		self._set_attribute('latencyBins', value)

	@property
	def LatencyBinsEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('latencyBinsEnabled')
	@LatencyBinsEnabled.setter
	def LatencyBinsEnabled(self, value):
		self._set_attribute('latencyBinsEnabled', value)

	@property
	def LatencyType(self):
		"""NOT DEFINED

		Returns:
			str(cutThrough|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadInitialRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('loadInitialRate')
	@LoadInitialRate.setter
	def LoadInitialRate(self, value):
		self._set_attribute('loadInitialRate', value)

	@property
	def LoadType(self):
		"""NOT DEFINED

		Returns:
			str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementLoadRate')
	@MaxIncrementLoadRate.setter
	def MaxIncrementLoadRate(self, value):
		self._set_attribute('maxIncrementLoadRate', value)

	@property
	def MaxRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MinIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def MldVersion(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('mldVersion')
	@MldVersion.setter
	def MldVersion(self, value):
		self._set_attribute('mldVersion', value)

	@property
	def NumAddresses(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numAddresses')
	@NumAddresses.setter
	def NumAddresses(self, value):
		self._set_attribute('numAddresses', value)

	@property
	def NumIterations(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numIterations')
	@NumIterations.setter
	def NumIterations(self, value):
		self._set_attribute('numIterations', value)

	@property
	def Numtrials(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PortDelayEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('portDelayEnabled')
	@PortDelayEnabled.setter
	def PortDelayEnabled(self, value):
		self._set_attribute('portDelayEnabled', value)

	@property
	def PortDelayUnit(self):
		"""NOT DEFINED

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

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
	def ReportSequenceError(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""NOT DEFINED

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Rfc2889ordering(self):
		"""NOT DEFINED

		Returns:
			str(val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def RouterAlert(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('routerAlert')
	@RouterAlert.setter
	def RouterAlert(self, value):
		self._set_attribute('routerAlert', value)

	@property
	def StepBurdenIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('stepBurdenIncrementLoadRate')
	@StepBurdenIncrementLoadRate.setter
	def StepBurdenIncrementLoadRate(self, value):
		self._set_attribute('stepBurdenIncrementLoadRate', value)

	@property
	def StepIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def StepIncrementLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementLoadRate')
	@StepIncrementLoadRate.setter
	def StepIncrementLoadRate(self, value):
		self._set_attribute('stepIncrementLoadRate', value)

	@property
	def SupportedTrafficTypes(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def TestTrafficType(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('testTrafficType')
	@TestTrafficType.setter
	def TestTrafficType(self, value):
		self._set_attribute('testTrafficType', value)

	@property
	def TxDelay(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UseMulticast(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('useMulticast')
	@UseMulticast.setter
	def UseMulticast(self, value):
		self._set_attribute('useMulticast', value)

	def update(self, ApplyMode=None, AssignGroupType=None, BidirectionalOptionEnabled=None, BurdenFrameSize=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, CountRandomFrameSize=None, DelayAfterTransmit=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameSizeMode=None, FramesizeList=None, Gap=None, GroupCapacityGreaterThan=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, IncrementBurdenLoadUnit=None, IncrementLoadUnit=None, InitialBurdenIncrementLoadRate=None, InitialIncrementLoadRate=None, InitialRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadInitialRate=None, LoadType=None, MapType=None, MaxIncrementFrameSize=None, MaxIncrementLoadRate=None, MaxRandomFrameSize=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, MldVersion=None, NumAddresses=None, NumIterations=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Rfc2889ordering=None, RouterAlert=None, StepBurdenIncrementLoadRate=None, StepIncrementFrameSize=None, StepIncrementLoadRate=None, SupportedTrafficTypes=None, TestTrafficType=None, TxDelay=None, UseMulticast=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			ApplyMode (str): NOT DEFINED
			AssignGroupType (str(accumulated|distributed)): NOT DEFINED
			BidirectionalOptionEnabled (bool): NOT DEFINED
			BurdenFrameSize (number): NOT DEFINED
			BurstSize (number): NOT DEFINED
			CalculateJitter (bool): NOT DEFINED
			CalculateLatency (bool): NOT DEFINED
			CountRandomFrameSize (number): NOT DEFINED
			DelayAfterTransmit (number): NOT DEFINED
			Duration (number): NOT DEFINED
			EnableDataIntegrity (bool): NOT DEFINED
			EnableLayer1Rate (bool): NOT DEFINED
			EnableLeaveGroup (bool): NOT DEFINED
			EnableMinFrameSize (bool): NOT DEFINED
			EnableMulticastQuerier (bool): NOT DEFINED
			EnableOldStatsForReef (bool): NOT DEFINED
			FloodedFramesEnabled (bool): NOT DEFINED
			ForceRegenerate (bool): NOT DEFINED
			FrameSizeMode (str(custom|customlist|increment|random)): NOT DEFINED
			FramesizeList (list(str)): NOT DEFINED
			Gap (number): NOT DEFINED
			GroupCapacityGreaterThan (number): NOT DEFINED
			GroupDistributionType (str(acrossHosts|acrossPorts)): NOT DEFINED
			IgmpV1Timeout (number): NOT DEFINED
			IgmpVersion (number): NOT DEFINED
			Igmpv3MessageType (str(exclude|include)): NOT DEFINED
			Igmpv3SourceAddrList (str): NOT DEFINED
			IncrAddresses (number): NOT DEFINED
			IncrementBurdenLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			InitialBurdenIncrementLoadRate (number): NOT DEFINED
			InitialIncrementLoadRate (number): NOT DEFINED
			InitialRate (str): NOT DEFINED
			Ipv4Address (str): NOT DEFINED
			Ipv6Address (str): NOT DEFINED
			IsIPv6 (str): NOT DEFINED
			IsMulticastAutomaticFrameData (str): NOT DEFINED
			JoinLeaveMultiplier (number): NOT DEFINED
			JoinLeaveRate (number): NOT DEFINED
			JoinLeaveWaitTime (number): NOT DEFINED
			LatencyBins (str): NOT DEFINED
			LatencyBinsEnabled (bool): NOT DEFINED
			LatencyType (str(cutThrough|storeForward)): NOT DEFINED
			LoadInitialRate (number): NOT DEFINED
			LoadType (str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)): NOT DEFINED
			MapType (str): NOT DEFINED
			MaxIncrementFrameSize (number): NOT DEFINED
			MaxIncrementLoadRate (number): NOT DEFINED
			MaxRandomFrameSize (number): NOT DEFINED
			MinIncrementFrameSize (number): NOT DEFINED
			MinRandomFrameSize (number): NOT DEFINED
			MldVersion (number): NOT DEFINED
			NumAddresses (number): NOT DEFINED
			NumIterations (number): NOT DEFINED
			Numtrials (number): NOT DEFINED
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): NOT DEFINED
			PortDelayValue (number): NOT DEFINED
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			ReportSequenceError (bool): NOT DEFINED
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): NOT DEFINED
			Rfc2889ordering (str(val2889Ordering)): NOT DEFINED
			RouterAlert (bool): NOT DEFINED
			StepBurdenIncrementLoadRate (number): NOT DEFINED
			StepIncrementFrameSize (number): NOT DEFINED
			StepIncrementLoadRate (number): NOT DEFINED
			SupportedTrafficTypes (str): NOT DEFINED
			TestTrafficType (str): NOT DEFINED
			TxDelay (number): NOT DEFINED
			UseMulticast (bool): NOT DEFINED

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
