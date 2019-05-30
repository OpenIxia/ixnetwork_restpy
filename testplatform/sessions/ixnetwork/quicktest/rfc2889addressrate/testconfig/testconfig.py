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
		"""The number of addresses that are to be used for each port in the current configuration.

		Returns:
			number
		"""
		return self._get_attribute('addrRateNumFrames')
	@AddrRateNumFrames.setter
	def AddrRateNumFrames(self, value):
		self._set_attribute('addrRateNumFrames', value)

	@property
	def AddrRateValidationFpsRate(self):
		"""The rate at which validation frames are sent.

		Returns:
			str
		"""
		return self._get_attribute('addrRateValidationFpsRate')
	@AddrRateValidationFpsRate.setter
	def AddrRateValidationFpsRate(self, value):
		self._set_attribute('addrRateValidationFpsRate', value)

	@property
	def AddrRateValidationRate(self):
		"""The number of validation frames that IxNetwork sends for each address.

		Returns:
			number
		"""
		return self._get_attribute('addrRateValidationRate')
	@AddrRateValidationRate.setter
	def AddrRateValidationRate(self, value):
		self._set_attribute('addrRateValidationRate', value)

	@property
	def AddrRateValidationRateUnit(self):
		"""Rate at which validation frames are transmitted for each address. Can be expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.

		Returns:
			str(fps|percentMaxRate)
		"""
		return self._get_attribute('addrRateValidationRateUnit')
	@AddrRateValidationRateUnit.setter
	def AddrRateValidationRateUnit(self, value):
		self._set_attribute('addrRateValidationRateUnit', value)

	@property
	def AddressRatePassCriteriaMode(self):
		"""Mode used to determine pass criteria. Can be Average Port or Minimum Port.

		Returns:
			str
		"""
		return self._get_attribute('addressRatePassCriteriaMode')
	@AddressRatePassCriteriaMode.setter
	def AddressRatePassCriteriaMode(self, value):
		self._set_attribute('addressRatePassCriteriaMode', value)

	@property
	def AddressRatePassFailValue(self):
		"""Determines whether the trial in the test passed or failed.

		Returns:
			number
		"""
		return self._get_attribute('addressRatePassFailValue')
	@AddressRatePassFailValue.setter
	def AddressRatePassFailValue(self, value):
		self._set_attribute('addressRatePassFailValue', value)

	@property
	def Age(self):
		"""This indicates the age in time, in seconds, since it was last refreshed.

		Returns:
			number
		"""
		return self._get_attribute('age')
	@Age.setter
	def Age(self, value):
		self._set_attribute('age', value)

	@property
	def BidirectionalOptionEnabled(self):
		"""If true, allows bidirectional traffic.

		Returns:
			bool
		"""
		return self._get_attribute('bidirectionalOptionEnabled')
	@BidirectionalOptionEnabled.setter
	def BidirectionalOptionEnabled(self, value):
		self._set_attribute('bidirectionalOptionEnabled', value)

	@property
	def BinaryBackoff(self):
		"""The percentage to be applied to the search interval through which the next iteration rate is obtained.

		Returns:
			number
		"""
		return self._get_attribute('binaryBackoff')
	@BinaryBackoff.setter
	def BinaryBackoff(self, value):
		self._set_attribute('binaryBackoff', value)

	@property
	def BinaryLoadUnit(self):
		"""The binary load unit value.

		Returns:
			str(fpsRate)
		"""
		return self._get_attribute('binaryLoadUnit')
	@BinaryLoadUnit.setter
	def BinaryLoadUnit(self, value):
		self._set_attribute('binaryLoadUnit', value)

	@property
	def BinaryResolution(self):
		"""The resolution of the iteration during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def BinarySearchType(self):
		"""It signifies the binary search type value.

		Returns:
			str(linear)
		"""
		return self._get_attribute('binarySearchType')
	@BinarySearchType.setter
	def BinarySearchType(self, value):
		self._set_attribute('binarySearchType', value)

	@property
	def BinaryTolerance(self):
		"""The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('binaryTolerance')
	@BinaryTolerance.setter
	def BinaryTolerance(self, value):
		self._set_attribute('binaryTolerance', value)

	@property
	def CountRandomFrameSize(self):
		"""If true, randomly counts the frame size.

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def DelayAfterTransmit(self):
		"""Specifies the amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def EnableAddressRatePassFail(self):
		"""If true, IxNetwork applies the pass or fail criteria to each trial in the test and determines whether the trial passed or failed.

		Returns:
			bool
		"""
		return self._get_attribute('enableAddressRatePassFail')
	@EnableAddressRatePassFail.setter
	def EnableAddressRatePassFail(self, value):
		self._set_attribute('enableAddressRatePassFail', value)

	@property
	def EnableDataIntegrity(self):
		"""If true, enables data integrity test.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableDropLink(self):
		"""If true, allows to drop link.

		Returns:
			bool
		"""
		return self._get_attribute('enableDropLink')
	@EnableDropLink.setter
	def EnableDropLink(self, value):
		self._set_attribute('enableDropLink', value)

	@property
	def EnableMinFrameSize(self):
		"""If true, enables minimum frame size.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnforceBidirectional(self):
		"""If true, uses bidirectional traffic mapping.

		Returns:
			bool
		"""
		return self._get_attribute('enforceBidirectional')
	@EnforceBidirectional.setter
	def EnforceBidirectional(self, value):
		self._set_attribute('enforceBidirectional', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian.

		Returns:
			str(custom|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesizeList(self):
		"""List containing the frame sizes used in the test.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def InitialBinaryLoadRate(self):
		"""The load rate used in the first iteration for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def LoadRateList(self):
		"""It signifies the list of load rate.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadType(self):
		"""Specifies the load type of the test configuration.

		Returns:
			str(binary)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def LoadUnit(self):
		"""The load unit value of the test configuration.

		Returns:
			str(fpsRate)
		"""
		return self._get_attribute('loadUnit')
	@LoadUnit.setter
	def LoadUnit(self, value):
		self._set_attribute('loadUnit', value)

	@property
	def MapType(self):
		"""The mapping type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxBinaryLoadRate(self):
		"""The upper bound of the iteration rates for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('maxBinaryLoadRate')
	@MaxBinaryLoadRate.setter
	def MaxBinaryLoadRate(self, value):
		self._set_attribute('maxBinaryLoadRate', value)

	@property
	def MaxIncrementFrameSize(self):
		"""The maximum incremental value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxRandomFrameSize(self):
		"""The maximum random frame size to be sent.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MinBinaryLoadRate(self):
		"""The lower bound of the iteration rates for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('minBinaryLoadRate')
	@MinBinaryLoadRate.setter
	def MinBinaryLoadRate(self, value):
		self._set_attribute('minBinaryLoadRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""The minimum incremental value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinRandomFrameSize(self):
		"""The minimum random frame size to be sent.

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def Numtrials(self):
		"""Defines how many times each frame size will be tested.

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
		"""The time interval during the port is down.

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
	def Rfc2889ordering(self):
		"""Enables ordering.

		Returns:
			str(noOrdering|unchanged|val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def ShowDetailedBinaryResults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('showDetailedBinaryResults')
	@ShowDetailedBinaryResults.setter
	def ShowDetailedBinaryResults(self, value):
		self._set_attribute('showDetailedBinaryResults', value)

	@property
	def StepIncrementFrameSize(self):
		"""The incremental step value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def SupportedTrafficTypes(self):
		"""The supported traffic types. Possible values of traffic types are ipmix, IPv4, IPv6 and MAC.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def Tablesize(self):
		"""New table size for each retry.

		Returns:
			number
		"""
		return self._get_attribute('tablesize')
	@Tablesize.setter
	def Tablesize(self, value):
		self._set_attribute('tablesize', value)

	@property
	def TxDelay(self):
		"""Signifies the transmission delay time.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	def update(self, AddrRateNumFrames=None, AddrRateValidationFpsRate=None, AddrRateValidationRate=None, AddrRateValidationRateUnit=None, AddressRatePassCriteriaMode=None, AddressRatePassFailValue=None, Age=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, CountRandomFrameSize=None, DelayAfterTransmit=None, EnableAddressRatePassFail=None, EnableDataIntegrity=None, EnableDropLink=None, EnableMinFrameSize=None, EnforceBidirectional=None, FrameSizeMode=None, FramesizeList=None, InitialBinaryLoadRate=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxBinaryLoadRate=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinBinaryLoadRate=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortDownTime=None, ProtocolItem=None, Rfc2889ordering=None, ShowDetailedBinaryResults=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, Tablesize=None, TxDelay=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			AddrRateNumFrames (number): The number of addresses that are to be used for each port in the current configuration.
			AddrRateValidationFpsRate (str): The rate at which validation frames are sent.
			AddrRateValidationRate (number): The number of validation frames that IxNetwork sends for each address.
			AddrRateValidationRateUnit (str(fps|percentMaxRate)): Rate at which validation frames are transmitted for each address. Can be expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
			AddressRatePassCriteriaMode (str): Mode used to determine pass criteria. Can be Average Port or Minimum Port.
			AddressRatePassFailValue (number): Determines whether the trial in the test passed or failed.
			Age (number): This indicates the age in time, in seconds, since it was last refreshed.
			BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
			BinaryBackoff (number): The percentage to be applied to the search interval through which the next iteration rate is obtained.
			BinaryLoadUnit (str(fpsRate)): The binary load unit value.
			BinaryResolution (number): The resolution of the iteration during a binary search.
			BinarySearchType (str(linear)): It signifies the binary search type value.
			BinaryTolerance (number): The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.
			CountRandomFrameSize (number): If true, randomly counts the frame size.
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
			EnableAddressRatePassFail (bool): If true, IxNetwork applies the pass or fail criteria to each trial in the test and determines whether the trial passed or failed.
			EnableDataIntegrity (bool): If true, enables data integrity test.
			EnableDropLink (bool): If true, allows to drop link.
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
			FrameSizeMode (str(custom|increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			FramesizeList (list(str)): List containing the frame sizes used in the test.
			InitialBinaryLoadRate (number): The load rate used in the first iteration for each frame size during a binary search.
			LoadRateList (str): It signifies the list of load rate.
			LoadType (str(binary)): Specifies the load type of the test configuration.
			LoadUnit (str(fpsRate)): The load unit value of the test configuration.
			MapType (str): The mapping type.
			MaxBinaryLoadRate (number): The upper bound of the iteration rates for each frame size during a binary search.
			MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
			MaxRandomFrameSize (number): The maximum random frame size to be sent.
			MinBinaryLoadRate (number): The lower bound of the iteration rates for each frame size during a binary search.
			MinIncrementFrameSize (number): The minimum incremental value of the frame size.
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			Numtrials (number): Defines how many times each frame size will be tested.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured.
			PortDelayValue (number): Sets the port delay value.
			PortDownTime (number): The time interval during the port is down.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			Rfc2889ordering (str(noOrdering|unchanged|val2889Ordering)): Enables ordering.
			ShowDetailedBinaryResults (bool): NOT DEFINED
			StepIncrementFrameSize (number): The incremental step value of the frame size.
			SupportedTrafficTypes (str): The supported traffic types. Possible values of traffic types are ipmix, IPv4, IPv6 and MAC.
			Tablesize (number): New table size for each retry.
			TxDelay (number): Signifies the transmission delay time.

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
