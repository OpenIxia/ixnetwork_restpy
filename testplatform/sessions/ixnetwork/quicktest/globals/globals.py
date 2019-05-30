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


class Globals(Base):
	"""The Globals class encapsulates a required globals node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Globals property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'globals'

	def __init__(self, parent):
		super(Globals, self).__init__(parent)

	@property
	def Comments(self):
		"""User-specified comments for reporting

		Returns:
			str
		"""
		return self._get_attribute('comments')
	@Comments.setter
	def Comments(self, value):
		self._set_attribute('comments', value)

	@property
	def EnableAbortIfLinkDown(self):
		"""Controls how long to wait for an up link state before aborting the test.

		Returns:
			bool
		"""
		return self._get_attribute('enableAbortIfLinkDown')
	@EnableAbortIfLinkDown.setter
	def EnableAbortIfLinkDown(self, value):
		self._set_attribute('enableAbortIfLinkDown', value)

	@property
	def EnableCapture(self):
		"""Available only if the (L1) receive mode has been set to capture packets. Select this option to save the packet capture file.

		Returns:
			bool
		"""
		return self._get_attribute('enableCapture')
	@EnableCapture.setter
	def EnableCapture(self, value):
		self._set_attribute('enableCapture', value)

	@property
	def EnableCheckLinkState(self):
		"""Initiates a link state check of the port before a test is run.

		Returns:
			bool
		"""
		return self._get_attribute('enableCheckLinkState')
	@EnableCheckLinkState.setter
	def EnableCheckLinkState(self, value):
		self._set_attribute('enableCheckLinkState', value)

	@property
	def EnableGenerateReportAfterRun(self):
		"""When this option is enabled, IxNetwork automatically generates a test report after the test is complete.

		Returns:
			bool
		"""
		return self._get_attribute('enableGenerateReportAfterRun')
	@EnableGenerateReportAfterRun.setter
	def EnableGenerateReportAfterRun(self, value):
		self._set_attribute('enableGenerateReportAfterRun', value)

	@property
	def EnableRebootCpu(self):
		"""Reboots the port CPU before a test is run.

		Returns:
			bool
		"""
		return self._get_attribute('enableRebootCpu')
	@EnableRebootCpu.setter
	def EnableRebootCpu(self, value):
		self._set_attribute('enableRebootCpu', value)

	@property
	def EnableSwitchToResult(self):
		"""When this option is enabled, IxNetwork immediately switches to the result display after the test is complete.

		Returns:
			bool
		"""
		return self._get_attribute('enableSwitchToResult')
	@EnableSwitchToResult.setter
	def EnableSwitchToResult(self, value):
		self._set_attribute('enableSwitchToResult', value)

	@property
	def EnableSwitchToStats(self):
		"""If true, the IxNetwork GUI immediately switches to the Result display after the test is complete.

		Returns:
			bool
		"""
		return self._get_attribute('enableSwitchToStats')
	@EnableSwitchToStats.setter
	def EnableSwitchToStats(self, value):
		self._set_attribute('enableSwitchToStats', value)

	@property
	def LinkDownTimeout(self):
		"""Select this option to simulate a port link being down.

		Returns:
			number
		"""
		return self._get_attribute('linkDownTimeout')
	@LinkDownTimeout.setter
	def LinkDownTimeout(self, value):
		self._set_attribute('linkDownTimeout', value)

	@property
	def MaxLinesToDisplay(self):
		"""The maximum number of lines to display.

		Returns:
			number
		"""
		return self._get_attribute('maxLinesToDisplay')
	@MaxLinesToDisplay.setter
	def MaxLinesToDisplay(self, value):
		self._set_attribute('maxLinesToDisplay', value)

	@property
	def OutputRootPath(self):
		"""This object holds the configurable output root path of IxNetwork for quick test.

		Returns:
			str
		"""
		return self._get_attribute('outputRootPath')
	@OutputRootPath.setter
	def OutputRootPath(self, value):
		self._set_attribute('outputRootPath', value)

	@property
	def ProductLabel(self):
		"""User-specified product label for reporting

		Returns:
			str
		"""
		return self._get_attribute('productLabel')
	@ProductLabel.setter
	def ProductLabel(self, value):
		self._set_attribute('productLabel', value)

	@property
	def SaveCaptureBeforeRun(self):
		"""This command saves the current capture data to the specified directory before run.

		Returns:
			bool
		"""
		return self._get_attribute('saveCaptureBeforeRun')
	@SaveCaptureBeforeRun.setter
	def SaveCaptureBeforeRun(self, value):
		self._set_attribute('saveCaptureBeforeRun', value)

	@property
	def SerialNumber(self):
		"""User-specified serial number for reporting

		Returns:
			str
		"""
		return self._get_attribute('serialNumber')
	@SerialNumber.setter
	def SerialNumber(self, value):
		self._set_attribute('serialNumber', value)

	@property
	def SleepTimeAfterReboot(self):
		"""If a reboot is initiated, the sleep after reboot is the number of seconds to wait after the port CPU goes into sleep mode.

		Returns:
			number
		"""
		return self._get_attribute('sleepTimeAfterReboot')
	@SleepTimeAfterReboot.setter
	def SleepTimeAfterReboot(self, value):
		self._set_attribute('sleepTimeAfterReboot', value)

	@property
	def TitlePageComments(self):
		"""User-specified comments for title page

		Returns:
			str
		"""
		return self._get_attribute('titlePageComments')
	@TitlePageComments.setter
	def TitlePageComments(self, value):
		self._set_attribute('titlePageComments', value)

	@property
	def UseDefaultRootPath(self):
		"""This object uses the default root path for quick test.

		Returns:
			bool
		"""
		return self._get_attribute('useDefaultRootPath')
	@UseDefaultRootPath.setter
	def UseDefaultRootPath(self, value):
		self._set_attribute('useDefaultRootPath', value)

	@property
	def Version(self):
		"""User-specified version for reporting

		Returns:
			str
		"""
		return self._get_attribute('version')
	@Version.setter
	def Version(self, value):
		self._set_attribute('version', value)

	def update(self, Comments=None, EnableAbortIfLinkDown=None, EnableCapture=None, EnableCheckLinkState=None, EnableGenerateReportAfterRun=None, EnableRebootCpu=None, EnableSwitchToResult=None, EnableSwitchToStats=None, LinkDownTimeout=None, MaxLinesToDisplay=None, OutputRootPath=None, ProductLabel=None, SaveCaptureBeforeRun=None, SerialNumber=None, SleepTimeAfterReboot=None, TitlePageComments=None, UseDefaultRootPath=None, Version=None):
		"""Updates a child instance of globals on the server.

		Args:
			Comments (str): User-specified comments for reporting
			EnableAbortIfLinkDown (bool): Controls how long to wait for an up link state before aborting the test.
			EnableCapture (bool): Available only if the (L1) receive mode has been set to capture packets. Select this option to save the packet capture file.
			EnableCheckLinkState (bool): Initiates a link state check of the port before a test is run.
			EnableGenerateReportAfterRun (bool): When this option is enabled, IxNetwork automatically generates a test report after the test is complete.
			EnableRebootCpu (bool): Reboots the port CPU before a test is run.
			EnableSwitchToResult (bool): When this option is enabled, IxNetwork immediately switches to the result display after the test is complete.
			EnableSwitchToStats (bool): If true, the IxNetwork GUI immediately switches to the Result display after the test is complete.
			LinkDownTimeout (number): Select this option to simulate a port link being down.
			MaxLinesToDisplay (number): The maximum number of lines to display.
			OutputRootPath (str): This object holds the configurable output root path of IxNetwork for quick test.
			ProductLabel (str): User-specified product label for reporting
			SaveCaptureBeforeRun (bool): This command saves the current capture data to the specified directory before run.
			SerialNumber (str): User-specified serial number for reporting
			SleepTimeAfterReboot (number): If a reboot is initiated, the sleep after reboot is the number of seconds to wait after the port CPU goes into sleep mode.
			TitlePageComments (str): User-specified comments for title page
			UseDefaultRootPath (bool): This object uses the default root path for quick test.
			Version (str): User-specified version for reporting

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
