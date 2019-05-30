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
	def BinarySearchType(self):
		"""The binary search type value.

		Returns:
			str(linear|perFlow|perPort)
		"""
		return self._get_attribute('binarySearchType')
	@BinarySearchType.setter
	def BinarySearchType(self, value):
		self._set_attribute('binarySearchType', value)

	@property
	def BurstSize(self):
		"""The number of packets that are sent in a burst.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CountRandomFrameSize(self):
		"""If true, frame sizes are counted at random.

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

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
	def Duration(self):
		"""The duration of the test in hours, which is used to calculate the number of frames to transmit.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableAlignmentErr(self):
		"""If true, alignment error is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableAlignmentErr')
	@EnableAlignmentErr.setter
	def EnableAlignmentErr(self, value):
		self._set_attribute('enableAlignmentErr', value)

	@property
	def EnableBadCrcErr(self):
		"""If true, BadCrc error is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableBadCrcErr')
	@EnableBadCrcErr.setter
	def EnableBadCrcErr(self, value):
		self._set_attribute('enableBadCrcErr', value)

	@property
	def EnableDribbleErr(self):
		"""If true, dribble error. is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableDribbleErr')
	@EnableDribbleErr.setter
	def EnableDribbleErr(self, value):
		self._set_attribute('enableDribbleErr', value)

	@property
	def EnableFragmentErr(self):
		"""If true, fragment error is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableFragmentErr')
	@EnableFragmentErr.setter
	def EnableFragmentErr(self, value):
		self._set_attribute('enableFragmentErr', value)

	@property
	def EnableMinFrameSize(self):
		"""If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableOversizeErr(self):
		"""If true, oversize error is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableOversizeErr')
	@EnableOversizeErr.setter
	def EnableOversizeErr(self, value):
		self._set_attribute('enableOversizeErr', value)

	@property
	def EnableUndersizeErr(self):
		"""If true, oversize error is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableUndersizeErr')
	@EnableUndersizeErr.setter
	def EnableUndersizeErr(self, value):
		self._set_attribute('enableUndersizeErr', value)

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
	def ForceRegenerate(self):
		"""Initiates a forced regeneration.

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FragmentFramesizeList(self):
		"""The list of fragmented framesize.

		Returns:
			str
		"""
		return self._get_attribute('fragmentFramesizeList')
	@FragmentFramesizeList.setter
	def FragmentFramesizeList(self, value):
		self._set_attribute('fragmentFramesizeList', value)

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
	def LoadRatePercent(self):
		"""The percent value of Load Rate.

		Returns:
			number
		"""
		return self._get_attribute('loadRatePercent')
	@LoadRatePercent.setter
	def LoadRatePercent(self, value):
		self._set_attribute('loadRatePercent', value)

	@property
	def LoadType(self):
		"""The type of the payload setting.

		Returns:
			str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""The POS traffic map type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxIncrementFrameSize(self):
		"""The integer that states the maximum amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxRandomFrameSize(self):
		"""The integer that states the maximum random amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MinIncrementFrameSize(self):
		"""The integer that states the minimum amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinRandomFrameSize(self):
		"""The integer that states the minimum random amount to which the frame size can be incremented.

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
	def OversizeFramesizeList(self):
		"""The list of oversized framesize.

		Returns:
			str
		"""
		return self._get_attribute('oversizeFramesizeList')
	@OversizeFramesizeList.setter
	def OversizeFramesizeList(self, value):
		self._set_attribute('oversizeFramesizeList', value)

	@property
	def PassFailNote(self):
		"""The note that indicates whether the test has cleared the pass/fail criterion or not.

		Returns:
			str
		"""
		return self._get_attribute('passFailNote')
	@PassFailNote.setter
	def PassFailNote(self, value):
		self._set_attribute('passFailNote', value)

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
		"""Sets the port delay unit in which it will be measured

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value

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
	def SendFullyMeshed(self):
		"""Sending fully meshed traffic.

		Returns:
			bool
		"""
		return self._get_attribute('sendFullyMeshed')
	@SendFullyMeshed.setter
	def SendFullyMeshed(self, value):
		self._set_attribute('sendFullyMeshed', value)

	@property
	def StepIncrementFrameSize(self):
		"""The step to increment the frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

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
	def TrafficType(self):
		"""The test based on the traffic type.

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UndersizeFramesizeList(self):
		"""The list of undersized framesize.

		Returns:
			str
		"""
		return self._get_attribute('undersizeFramesizeList')
	@UndersizeFramesizeList.setter
	def UndersizeFramesizeList(self, value):
		self._set_attribute('undersizeFramesizeList', value)

	def update(self, BidirectionalOptionEnabled=None, BinarySearchType=None, BurstSize=None, CountRandomFrameSize=None, DelayAfterTransmit=None, Duration=None, EnableAlignmentErr=None, EnableBadCrcErr=None, EnableDribbleErr=None, EnableFragmentErr=None, EnableMinFrameSize=None, EnableOversizeErr=None, EnableUndersizeErr=None, EnforceBidirectional=None, ForceRegenerate=None, FragmentFramesizeList=None, FrameSizeMode=None, FramesizeList=None, LoadRatePercent=None, LoadType=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, Numtrials=None, OversizeFramesizeList=None, PassFailNote=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, SendFullyMeshed=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, TrafficType=None, TxDelay=None, UndersizeFramesizeList=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
			BinarySearchType (str(linear|perFlow|perPort)): The binary search type value.
			BurstSize (number): The number of packets that are sent in a burst.
			CountRandomFrameSize (number): If true, frame sizes are counted at random.
			DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
			Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
			EnableAlignmentErr (bool): If true, alignment error is enabled.
			EnableBadCrcErr (bool): If true, BadCrc error is enabled.
			EnableDribbleErr (bool): If true, dribble error. is enabled.
			EnableFragmentErr (bool): If true, fragment error is enabled.
			EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
			EnableOversizeErr (bool): If true, oversize error is enabled.
			EnableUndersizeErr (bool): If true, oversize error is enabled.
			EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
			ForceRegenerate (bool): Initiates a forced regeneration.
			FragmentFramesizeList (str): The list of fragmented framesize.
			FrameSizeMode (str(custom|increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			FramesizeList (list(str)): List containing the frame sizes used in the test.
			LoadRatePercent (number): The percent value of Load Rate.
			LoadType (str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)): The type of the payload setting.
			MapType (str): The POS traffic map type.
			MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
			MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
			MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
			MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
			Numtrials (number): Defines how many times each frame size will be tested.
			OversizeFramesizeList (str): The list of oversized framesize.
			PassFailNote (str): The note that indicates whether the test has cleared the pass/fail criterion or not.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured
			PortDelayValue (number): Sets the port delay value
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			SendFullyMeshed (bool): Sending fully meshed traffic.
			StepIncrementFrameSize (number): The step to increment the frame size.
			SupportedTrafficTypes (str): The traffic types supported.
			TrafficType (str(burstyLoading|constantLoading)): The test based on the traffic type.
			TxDelay (number): The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
			UndersizeFramesizeList (str): The list of undersized framesize.

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
