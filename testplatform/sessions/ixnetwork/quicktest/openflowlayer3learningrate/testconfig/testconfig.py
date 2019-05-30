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
	def AddrRateNumFrames(self):
		"""Indicates the address rate in number of frames.

		Returns:
			number
		"""
		return self._get_attribute('addrRateNumFrames')
	@AddrRateNumFrames.setter
	def AddrRateNumFrames(self, value):
		self._set_attribute('addrRateNumFrames', value)

	@property
	def AddrRateValidationFpsRate(self):
		"""Indicates that the step rate of the load unit is fpsRate.

		Returns:
			str
		"""
		return self._get_attribute('addrRateValidationFpsRate')
	@AddrRateValidationFpsRate.setter
	def AddrRateValidationFpsRate(self, value):
		self._set_attribute('addrRateValidationFpsRate', value)

	@property
	def AddrRateValidationRate(self):
		"""Indicates the address rate validation rate.

		Returns:
			number
		"""
		return self._get_attribute('addrRateValidationRate')
	@AddrRateValidationRate.setter
	def AddrRateValidationRate(self, value):
		self._set_attribute('addrRateValidationRate', value)

	@property
	def AddrRateValidationRateUnit(self):
		"""Indicates the address rate validation rate unit.

		Returns:
			str(fps|percentMaxRate)
		"""
		return self._get_attribute('addrRateValidationRateUnit')
	@AddrRateValidationRateUnit.setter
	def AddrRateValidationRateUnit(self, value):
		self._set_attribute('addrRateValidationRateUnit', value)

	@property
	def AddressRatePassCriteriaMode(self):
		"""Indicates the address rate pass criteria mode.

		Returns:
			str
		"""
		return self._get_attribute('addressRatePassCriteriaMode')
	@AddressRatePassCriteriaMode.setter
	def AddressRatePassCriteriaMode(self, value):
		self._set_attribute('addressRatePassCriteriaMode', value)

	@property
	def AddressRatePassFailValue(self):
		"""Indicates the Address Rate value.

		Returns:
			number
		"""
		return self._get_attribute('addressRatePassFailValue')
	@AddressRatePassFailValue.setter
	def AddressRatePassFailValue(self, value):
		self._set_attribute('addressRatePassFailValue', value)

	@property
	def BinaryBackoff(self):
		"""The binary search interval through which the next iteration's rate is obtained.

		Returns:
			number
		"""
		return self._get_attribute('binaryBackoff')
	@BinaryBackoff.setter
	def BinaryBackoff(self, value):
		self._set_attribute('binaryBackoff', value)

	@property
	def BinaryLoadUnit(self):
		"""Indicates the binary load unit.

		Returns:
			str(fpsRate)
		"""
		return self._get_attribute('binaryLoadUnit')
	@BinaryLoadUnit.setter
	def BinaryLoadUnit(self, value):
		self._set_attribute('binaryLoadUnit', value)

	@property
	def BinaryResolution(self):
		"""Indicates the resolution during the binary search.

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def BinarySearchType(self):
		"""Indicates the search type for a Binary search.

		Returns:
			str(linear)
		"""
		return self._get_attribute('binarySearchType')
	@BinarySearchType.setter
	def BinarySearchType(self, value):
		self._set_attribute('binarySearchType', value)

	@property
	def CacheTimeout(self):
		"""Indicates cache time out.

		Returns:
			number
		"""
		return self._get_attribute('cacheTimeout')
	@CacheTimeout.setter
	def CacheTimeout(self, value):
		self._set_attribute('cacheTimeout', value)

	@property
	def DelayAfterTransmit(self):
		"""A delay that is inserted after transmit is complete, before it continues with the test.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def EnableAddressRatePassFail(self):
		"""If true, allows Address Rate to be used as a Pass/Fail criteria.

		Returns:
			bool
		"""
		return self._get_attribute('enableAddressRatePassFail')
	@EnableAddressRatePassFail.setter
	def EnableAddressRatePassFail(self, value):
		self._set_attribute('enableAddressRatePassFail', value)

	@property
	def EnableCacheTimeout(self):
		"""If true, enables cache time out.

		Returns:
			bool
		"""
		return self._get_attribute('enableCacheTimeout')
	@EnableCacheTimeout.setter
	def EnableCacheTimeout(self, value):
		self._set_attribute('enableCacheTimeout', value)

	@property
	def EnableDaD(self):
		"""If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.

		Returns:
			bool
		"""
		return self._get_attribute('enableDaD')
	@EnableDaD.setter
	def EnableDaD(self, value):
		self._set_attribute('enableDaD', value)

	@property
	def EnableDropLink(self):
		"""If true, allows Route Range to be dropped.

		Returns:
			bool
		"""
		return self._get_attribute('enableDropLink')
	@EnableDropLink.setter
	def EnableDropLink(self, value):
		self._set_attribute('enableDropLink', value)

	@property
	def EnableExtraIterations(self):
		"""If true, enables extra iterations. Sets extra iteration offset values.

		Returns:
			bool
		"""
		return self._get_attribute('enableExtraIterations')
	@EnableExtraIterations.setter
	def EnableExtraIterations(self, value):
		self._set_attribute('enableExtraIterations', value)

	@property
	def EnableMinFrameSize(self):
		"""If true, allows to set minimum frame size.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def ExtraIterationOffsets(self):
		"""Sets extra iteration offset values.

		Returns:
			str
		"""
		return self._get_attribute('extraIterationOffsets')
	@ExtraIterationOffsets.setter
	def ExtraIterationOffsets(self, value):
		self._set_attribute('extraIterationOffsets', value)

	@property
	def FrameSizeMode(self):
		"""Indicates the frame size mode.

		Returns:
			str(fixed)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def Framesize(self):
		"""The frame size used by the service.

		Returns:
			str
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeFixedValue(self):
		"""It signifies the frame size fixed value.

		Returns:
			number
		"""
		return self._get_attribute('framesizeFixedValue')
	@FramesizeFixedValue.setter
	def FramesizeFixedValue(self, value):
		self._set_attribute('framesizeFixedValue', value)

	@property
	def FramesizeList(self):
		"""The list of the available frame size.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def InitialBinaryLoadRate(self):
		"""Indicates the initial binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def Layer3AddressCount(self):
		"""Indicates the Layer 3 address count.

		Returns:
			number
		"""
		return self._get_attribute('layer3AddressCount')
	@Layer3AddressCount.setter
	def Layer3AddressCount(self, value):
		self._set_attribute('layer3AddressCount', value)

	@property
	def LoadRateList(self):
		"""Enter the Load Rate List.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadType(self):
		"""Indicates the load type.

		Returns:
			str(binary)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def LoadUnit(self):
		"""Indicates the load unit.

		Returns:
			str(fpsRate)
		"""
		return self._get_attribute('loadUnit')
	@LoadUnit.setter
	def LoadUnit(self, value):
		self._set_attribute('loadUnit', value)

	@property
	def MapType(self):
		"""Indicates the traffic map type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxBinaryLoadRate(self):
		"""Indicates the maximum binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxBinaryLoadRate')
	@MaxBinaryLoadRate.setter
	def MaxBinaryLoadRate(self, value):
		self._set_attribute('maxBinaryLoadRate', value)

	@property
	def MaxOutstandingRequests(self):
		"""Indicates maximum outstanding request.

		Returns:
			number
		"""
		return self._get_attribute('maxOutstandingRequests')
	@MaxOutstandingRequests.setter
	def MaxOutstandingRequests(self, value):
		self._set_attribute('maxOutstandingRequests', value)

	@property
	def MinBinaryLoadRate(self):
		"""Indicates the minimum binary load rate.

		Returns:
			number
		"""
		return self._get_attribute('minBinaryLoadRate')
	@MinBinaryLoadRate.setter
	def MinBinaryLoadRate(self, value):
		self._set_attribute('minBinaryLoadRate', value)

	@property
	def Numtrials(self):
		"""Number of trials that can be run.

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
		"""Sets the port delay unit in which it will be measured.

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value.

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

	@property
	def PortDownTime(self):
		"""During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.

		Returns:
			number
		"""
		return self._get_attribute('portDownTime')
	@PortDownTime.setter
	def PortDownTime(self, value):
		self._set_attribute('portDownTime', value)

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
	def StaggeredStart(self):
		"""Enables a staggered start to traffic transmit.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def SupportedTrafficTypes(self):
		"""The traffic types supported.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def TxDelay(self):
		"""Specifies the amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	def update(self, AddrRateNumFrames=None, AddrRateValidationFpsRate=None, AddrRateValidationRate=None, AddrRateValidationRateUnit=None, AddressRatePassCriteriaMode=None, AddressRatePassFailValue=None, BinaryBackoff=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, CacheTimeout=None, DelayAfterTransmit=None, EnableAddressRatePassFail=None, EnableCacheTimeout=None, EnableDaD=None, EnableDropLink=None, EnableExtraIterations=None, EnableMinFrameSize=None, ExtraIterationOffsets=None, FrameSizeMode=None, Framesize=None, FramesizeFixedValue=None, FramesizeList=None, InitialBinaryLoadRate=None, Layer3AddressCount=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxBinaryLoadRate=None, MaxOutstandingRequests=None, MinBinaryLoadRate=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortDownTime=None, ProtocolItem=None, StaggeredStart=None, SupportedTrafficTypes=None, TxDelay=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			AddrRateNumFrames (number): Indicates the address rate in number of frames.
			AddrRateValidationFpsRate (str): Indicates that the step rate of the load unit is fpsRate.
			AddrRateValidationRate (number): Indicates the address rate validation rate.
			AddrRateValidationRateUnit (str(fps|percentMaxRate)): Indicates the address rate validation rate unit.
			AddressRatePassCriteriaMode (str): Indicates the address rate pass criteria mode.
			AddressRatePassFailValue (number): Indicates the Address Rate value.
			BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
			BinaryLoadUnit (str(fpsRate)): Indicates the binary load unit.
			BinaryResolution (number): Indicates the resolution during the binary search.
			BinarySearchType (str(linear)): Indicates the search type for a Binary search.
			CacheTimeout (number): Indicates cache time out.
			DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
			EnableAddressRatePassFail (bool): If true, allows Address Rate to be used as a Pass/Fail criteria.
			EnableCacheTimeout (bool): If true, enables cache time out.
			EnableDaD (bool): If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.
			EnableDropLink (bool): If true, allows Route Range to be dropped.
			EnableExtraIterations (bool): If true, enables extra iterations. Sets extra iteration offset values.
			EnableMinFrameSize (bool): If true, allows to set minimum frame size.
			ExtraIterationOffsets (str): Sets extra iteration offset values.
			FrameSizeMode (str(fixed)): Indicates the frame size mode.
			Framesize (str): The frame size used by the service.
			FramesizeFixedValue (number): It signifies the frame size fixed value.
			FramesizeList (list(str)): The list of the available frame size.
			InitialBinaryLoadRate (number): Indicates the initial binary load rate.
			Layer3AddressCount (number): Indicates the Layer 3 address count.
			LoadRateList (str): Enter the Load Rate List.
			LoadType (str(binary)): Indicates the load type.
			LoadUnit (str(fpsRate)): Indicates the load unit.
			MapType (str): Indicates the traffic map type.
			MaxBinaryLoadRate (number): Indicates the maximum binary load rate.
			MaxOutstandingRequests (number): Indicates maximum outstanding request.
			MinBinaryLoadRate (number): Indicates the minimum binary load rate.
			Numtrials (number): Number of trials that can be run.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value.
			PortDownTime (number): During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			StaggeredStart (bool): Enables a staggered start to traffic transmit.
			SupportedTrafficTypes (str): The traffic types supported.
			TxDelay (number): Specifies the amount of delay after every transmit.

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
