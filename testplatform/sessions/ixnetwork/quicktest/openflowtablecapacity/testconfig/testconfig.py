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
	def BinaryLoadUnit(self):
		"""The load unit value in binary. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('binaryLoadUnit')
	@BinaryLoadUnit.setter
	def BinaryLoadUnit(self, value):
		self._set_attribute('binaryLoadUnit', value)

	@property
	def BinaryResolution(self):
		"""Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def CalculateLatency(self):
		"""If true, calculates the latency.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def CustomFramesizeValue(self):
		"""Sets the custom framesize value

		Returns:
			number
		"""
		return self._get_attribute('customFramesizeValue')
	@CustomFramesizeValue.setter
	def CustomFramesizeValue(self, value):
		self._set_attribute('customFramesizeValue', value)

	@property
	def CustomLoadUnit(self):
		"""Specifies the custom load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def DelayBeforeStartTransmit(self):
		"""If true, a delay is introduced before transmission is started.

		Returns:
			number
		"""
		return self._get_attribute('delayBeforeStartTransmit')
	@DelayBeforeStartTransmit.setter
	def DelayBeforeStartTransmit(self, value):
		self._set_attribute('delayBeforeStartTransmit', value)

	@property
	def DeleteFlowsAtStartup(self):
		"""If true, the test will delete the flowgroups at startup

		Returns:
			bool
		"""
		return self._get_attribute('deleteFlowsAtStartup')
	@DeleteFlowsAtStartup.setter
	def DeleteFlowsAtStartup(self, value):
		self._set_attribute('deleteFlowsAtStartup', value)

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
	def EnableTrafficValidation(self):
		"""If true, traffic validation is performed. It provides a high level view of the errors detected in each traffic item and flow group. With the help of this option you can easily identify the various categories of errors detected in each traffic item and flow group.

		Returns:
			bool
		"""
		return self._get_attribute('enableTrafficValidation')
	@EnableTrafficValidation.setter
	def EnableTrafficValidation(self, value):
		self._set_attribute('enableTrafficValidation', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian.

		Returns:
			str(increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def Gap(self):
		"""The gap in transmission of frames.

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def InitialBinaryLoadIntegerValues(self):
		"""Indicates the initial binary load integer values.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadIntegerValues')
	@InitialBinaryLoadIntegerValues.setter
	def InitialBinaryLoadIntegerValues(self, value):
		self._set_attribute('initialBinaryLoadIntegerValues', value)

	@property
	def InitialStepIntegerValues(self):
		"""Indicates the initial step value.

		Returns:
			number
		"""
		return self._get_attribute('initialStepIntegerValues')
	@InitialStepIntegerValues.setter
	def InitialStepIntegerValues(self, value):
		self._set_attribute('initialStepIntegerValues', value)

	@property
	def LatencyType(self):
		"""Indicate the type of latency that needs to be measured. Can be Cut-Through, Store-Forward and so on.

		Returns:
			str(cutThrough|forwardingDelay|mef|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadRateValue(self):
		"""The value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('loadRateValue')
	@LoadRateValue.setter
	def LoadRateValue(self, value):
		self._set_attribute('loadRateValue', value)

	@property
	def LoadType(self):
		"""Indicates the load type. Can be any of the following:

		Returns:
			str(binary|step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MaxBinaryLoadIntegerValue(self):
		"""Indicates the maximum load integer values.

		Returns:
			number
		"""
		return self._get_attribute('maxBinaryLoadIntegerValue')
	@MaxBinaryLoadIntegerValue.setter
	def MaxBinaryLoadIntegerValue(self, value):
		self._set_attribute('maxBinaryLoadIntegerValue', value)

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
	def MaxStepIntegerValues(self):
		"""Indicates the maximum step value.

		Returns:
			number
		"""
		return self._get_attribute('maxStepIntegerValues')
	@MaxStepIntegerValues.setter
	def MaxStepIntegerValues(self, value):
		self._set_attribute('maxStepIntegerValues', value)

	@property
	def MinAddressTableSize(self):
		"""Indicates the minimum size of the address table.

		Returns:
			number
		"""
		return self._get_attribute('minAddressTableSize')
	@MinAddressTableSize.setter
	def MinAddressTableSize(self, value):
		self._set_attribute('minAddressTableSize', value)

	@property
	def MinBinaryLoadIntegerValues(self):
		"""Indicates the minimum binary load integer values.

		Returns:
			number
		"""
		return self._get_attribute('minBinaryLoadIntegerValues')
	@MinBinaryLoadIntegerValues.setter
	def MinBinaryLoadIntegerValues(self, value):
		self._set_attribute('minBinaryLoadIntegerValues', value)

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
		"""Number of trials that can be run

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PacketsPerFlow(self):
		"""Indicates the number of packets per flow.

		Returns:
			number
		"""
		return self._get_attribute('packetsPerFlow')
	@PacketsPerFlow.setter
	def PacketsPerFlow(self, value):
		self._set_attribute('packetsPerFlow', value)

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
	def RangeCount(self):
		"""Indicates the range count.

		Returns:
			number
		"""
		return self._get_attribute('rangeCount')
	@RangeCount.setter
	def RangeCount(self, value):
		self._set_attribute('rangeCount', value)

	@property
	def StepLoadUnit(self):
		"""Specifies the step rate of the load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('stepLoadUnit')
	@StepLoadUnit.setter
	def StepLoadUnit(self, value):
		self._set_attribute('stepLoadUnit', value)

	@property
	def StepStepIntegerValues(self):
		"""Indicates the step integer value.

		Returns:
			number
		"""
		return self._get_attribute('stepStepIntegerValues')
	@StepStepIntegerValues.setter
	def StepStepIntegerValues(self, value):
		self._set_attribute('stepStepIntegerValues', value)

	@property
	def WaitAffterFlowAdd(self):
		"""If true, the traffic is paused after flowdetection is added.

		Returns:
			number
		"""
		return self._get_attribute('waitAffterFlowAdd')
	@WaitAffterFlowAdd.setter
	def WaitAffterFlowAdd(self, value):
		self._set_attribute('waitAffterFlowAdd', value)

	def update(self, BinaryLoadUnit=None, BinaryResolution=None, CalculateLatency=None, CustomFramesizeValue=None, CustomLoadUnit=None, DelayBeforeStartTransmit=None, DeleteFlowsAtStartup=None, EnableMinFrameSize=None, EnableTrafficValidation=None, FrameSizeMode=None, Gap=None, InitialBinaryLoadIntegerValues=None, InitialStepIntegerValues=None, LatencyType=None, LoadRateValue=None, LoadType=None, MaxBinaryLoadIntegerValue=None, MaxRandomFrameSize=None, MaxStepIntegerValues=None, MinAddressTableSize=None, MinBinaryLoadIntegerValues=None, MinRandomFrameSize=None, Numtrials=None, PacketsPerFlow=None, ProtocolItem=None, RangeCount=None, StepLoadUnit=None, StepStepIntegerValues=None, WaitAffterFlowAdd=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The load unit value in binary. Possible values include:
			BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops
			CalculateLatency (bool): If true, calculates the latency.
			CustomFramesizeValue (number): Sets the custom framesize value
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the custom load unit.
			DelayBeforeStartTransmit (number): If true, a delay is introduced before transmission is started.
			DeleteFlowsAtStartup (bool): If true, the test will delete the flowgroups at startup
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			EnableTrafficValidation (bool): If true, traffic validation is performed. It provides a high level view of the errors detected in each traffic item and flow group. With the help of this option you can easily identify the various categories of errors detected in each traffic item and flow group.
			FrameSizeMode (str(increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			Gap (number): The gap in transmission of frames.
			InitialBinaryLoadIntegerValues (number): Indicates the initial binary load integer values.
			InitialStepIntegerValues (number): Indicates the initial step value.
			LatencyType (str(cutThrough|forwardingDelay|mef|storeForward)): Indicate the type of latency that needs to be measured. Can be Cut-Through, Store-Forward and so on.
			LoadRateValue (number): The value of the load rate.
			LoadType (str(binary|step)): Indicates the load type. Can be any of the following:
			MaxBinaryLoadIntegerValue (number): Indicates the maximum load integer values.
			MaxRandomFrameSize (number): The maximum random frame size to be sent.
			MaxStepIntegerValues (number): Indicates the maximum step value.
			MinAddressTableSize (number): Indicates the minimum size of the address table.
			MinBinaryLoadIntegerValues (number): Indicates the minimum binary load integer values.
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			Numtrials (number): Number of trials that can be run
			PacketsPerFlow (number): Indicates the number of packets per flow.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			RangeCount (number): Indicates the range count.
			StepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the step rate of the load unit.
			StepStepIntegerValues (number): Indicates the step integer value.
			WaitAffterFlowAdd (number): If true, the traffic is paused after flowdetection is added.

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
