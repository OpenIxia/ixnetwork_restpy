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
	def BinaryResolutionSlaveNumber(self):
		"""Specifies the binary resolution slave number.

		Returns:
			number
		"""
		return self._get_attribute('binaryResolutionSlaveNumber')
	@BinaryResolutionSlaveNumber.setter
	def BinaryResolutionSlaveNumber(self, value):
		self._set_attribute('binaryResolutionSlaveNumber', value)

	@property
	def Duration(self):
		"""The duration of the test in hours, minutes, or seconds, which is used to calculate.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableSlavesPassFail(self):
		"""If true, enables slaves pass fail.

		Returns:
			str
		"""
		return self._get_attribute('enableSlavesPassFail')
	@EnableSlavesPassFail.setter
	def EnableSlavesPassFail(self, value):
		self._set_attribute('enableSlavesPassFail', value)

	@property
	def IncrementStepSlaveNumber(self):
		"""The incremental step value for the slave number.

		Returns:
			number
		"""
		return self._get_attribute('incrementStepSlaveNumber')
	@IncrementStepSlaveNumber.setter
	def IncrementStepSlaveNumber(self, value):
		self._set_attribute('incrementStepSlaveNumber', value)

	@property
	def InitialBinarySlaveNumber(self):
		"""The initial incremental value of the binary slave number.

		Returns:
			number
		"""
		return self._get_attribute('initialBinarySlaveNumber')
	@InitialBinarySlaveNumber.setter
	def InitialBinarySlaveNumber(self, value):
		self._set_attribute('initialBinarySlaveNumber', value)

	@property
	def InitialStepSlaveNumber(self):
		"""The initial step value of the slave number.

		Returns:
			number
		"""
		return self._get_attribute('initialStepSlaveNumber')
	@InitialStepSlaveNumber.setter
	def InitialStepSlaveNumber(self, value):
		self._set_attribute('initialStepSlaveNumber', value)

	@property
	def LoadType(self):
		"""The type of the payload setting.

		Returns:
			str(binary|step)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MaxBinarySlaveNumber(self):
		"""The maximum value of the binary slave number.

		Returns:
			number
		"""
		return self._get_attribute('maxBinarySlaveNumber')
	@MaxBinarySlaveNumber.setter
	def MaxBinarySlaveNumber(self, value):
		self._set_attribute('maxBinarySlaveNumber', value)

	@property
	def MaxOutstanding(self):
		"""The maximum oustanding value of the slave scalability.

		Returns:
			number
		"""
		return self._get_attribute('maxOutstanding')
	@MaxOutstanding.setter
	def MaxOutstanding(self, value):
		self._set_attribute('maxOutstanding', value)

	@property
	def MaxStepSlaveNumber(self):
		"""The maximum step value of the slave number.

		Returns:
			number
		"""
		return self._get_attribute('maxStepSlaveNumber')
	@MaxStepSlaveNumber.setter
	def MaxStepSlaveNumber(self, value):
		self._set_attribute('maxStepSlaveNumber', value)

	@property
	def MinBinarySlaveNumber(self):
		"""The minimum binary value of the slave number.

		Returns:
			number
		"""
		return self._get_attribute('minBinarySlaveNumber')
	@MinBinarySlaveNumber.setter
	def MinBinarySlaveNumber(self, value):
		self._set_attribute('minBinarySlaveNumber', value)

	@property
	def NumberOfSlavesPassFail(self):
		"""The number of slaves pass fail.

		Returns:
			number
		"""
		return self._get_attribute('numberOfSlavesPassFail')
	@NumberOfSlavesPassFail.setter
	def NumberOfSlavesPassFail(self, value):
		self._set_attribute('numberOfSlavesPassFail', value)

	@property
	def Numtrials(self):
		"""The number of trials.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

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
	def Runmode(self):
		"""It gives the run mode

		Returns:
			str(duration|noframes)
		"""
		return self._get_attribute('runmode')
	@Runmode.setter
	def Runmode(self, value):
		self._set_attribute('runmode', value)

	@property
	def SetupRate(self):
		"""The setup rate.

		Returns:
			number
		"""
		return self._get_attribute('setupRate')
	@SetupRate.setter
	def SetupRate(self, value):
		self._set_attribute('setupRate', value)

	@property
	def StartTraffic(self):
		"""It starts the traffic

		Returns:
			str
		"""
		return self._get_attribute('startTraffic')
	@StartTraffic.setter
	def StartTraffic(self, value):
		self._set_attribute('startTraffic', value)

	@property
	def TeardownRate(self):
		"""The teardown rate.

		Returns:
			number
		"""
		return self._get_attribute('teardownRate')
	@TeardownRate.setter
	def TeardownRate(self, value):
		self._set_attribute('teardownRate', value)

	@property
	def UseExistingSetupRate(self):
		"""If True, it uses the Existing Setup rate

		Returns:
			bool
		"""
		return self._get_attribute('useExistingSetupRate')
	@UseExistingSetupRate.setter
	def UseExistingSetupRate(self, value):
		self._set_attribute('useExistingSetupRate', value)

	def update(self, BinaryResolutionSlaveNumber=None, Duration=None, EnableSlavesPassFail=None, IncrementStepSlaveNumber=None, InitialBinarySlaveNumber=None, InitialStepSlaveNumber=None, LoadType=None, MaxBinarySlaveNumber=None, MaxOutstanding=None, MaxStepSlaveNumber=None, MinBinarySlaveNumber=None, NumberOfSlavesPassFail=None, Numtrials=None, ProtocolItem=None, Runmode=None, SetupRate=None, StartTraffic=None, TeardownRate=None, UseExistingSetupRate=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BinaryResolutionSlaveNumber (number): Specifies the binary resolution slave number.
			Duration (number): The duration of the test in hours, minutes, or seconds, which is used to calculate.
			EnableSlavesPassFail (str): If true, enables slaves pass fail.
			IncrementStepSlaveNumber (number): The incremental step value for the slave number.
			InitialBinarySlaveNumber (number): The initial incremental value of the binary slave number.
			InitialStepSlaveNumber (number): The initial step value of the slave number.
			LoadType (str(binary|step)): The type of the payload setting.
			MaxBinarySlaveNumber (number): The maximum value of the binary slave number.
			MaxOutstanding (number): The maximum oustanding value of the slave scalability.
			MaxStepSlaveNumber (number): The maximum step value of the slave number.
			MinBinarySlaveNumber (number): The minimum binary value of the slave number.
			NumberOfSlavesPassFail (number): The number of slaves pass fail.
			Numtrials (number): The number of trials.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			Runmode (str(duration|noframes)): It gives the run mode
			SetupRate (number): The setup rate.
			StartTraffic (str): It starts the traffic
			TeardownRate (number): The teardown rate.
			UseExistingSetupRate (bool): If True, it uses the Existing Setup rate

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
