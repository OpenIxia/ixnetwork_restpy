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


class Results(Base):
	"""The Results class encapsulates a required results node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Results property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'results'

	def __init__(self, parent):
		super(Results, self).__init__(parent)

	@property
	def CurrentActions(self):
		"""Current actions

		Returns:
			list(dict(arg1:str,arg2:str[AgingTable|ApplyFlowGroups|CheckingForAvailableStats|CheckingLicense|ClearingStats|CollectingStats|DropLink|frameLossCriteriaNotMet|HoldDown|InitializingTest|IterationStart|LicenseFailed|LicenseVerified|None|NoRibInConvergenceStopping|SendingLearningFrames|SetTestConfiguration|SetupStatisticsCollection|StartingTraffic|TestEnded|TestStarted|ThresholdReachedStopping|TransmittingComplete|TransmittingFrames|WaitAfterFailover|WaitBeforeFailover|WaitingAfterLearningFramesSent|WaitingBeforeSendingTraffic|WaitingForDelayBetweenIterations|WaitingForPorts|WaitingForStats|WaitingTrafficToStop]))
		"""
		return self._get_attribute('currentActions')

	@property
	def CurrentViews(self):
		"""Views used by this QuickTest

		Returns:
			list(str)
		"""
		return self._get_attribute('currentViews')

	@property
	def Duration(self):
		"""Test duration

		Returns:
			str
		"""
		return self._get_attribute('duration')

	@property
	def IsRunning(self):
		"""Indicates whether the test is currently running

		Returns:
			bool
		"""
		return self._get_attribute('isRunning')

	@property
	def Progress(self):
		"""Test progress

		Returns:
			str
		"""
		return self._get_attribute('progress')

	@property
	def Result(self):
		"""Test result

		Returns:
			str
		"""
		return self._get_attribute('result')

	@property
	def ResultPath(self):
		"""Folder containing test result files

		Returns:
			str
		"""
		return self._get_attribute('resultPath')

	@property
	def StartTime(self):
		"""Test start time

		Returns:
			str
		"""
		return self._get_attribute('startTime')

	@property
	def Status(self):
		"""Test status

		Returns:
			str
		"""
		return self._get_attribute('status')

	@property
	def TrafficStatus(self):
		"""Test traffic status

		Returns:
			dict(arg1:number,arg2:number)
		"""
		return self._get_attribute('trafficStatus')

	@property
	def WaitingStatus(self):
		"""Test waiting status

		Returns:
			dict(arg1:number,arg2:number)
		"""
		return self._get_attribute('waitingStatus')

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
