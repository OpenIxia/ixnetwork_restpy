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
	def CpDpConvergenceFactorScale(self):
		"""Indicates the convergence factor scale.

		Returns:
			str
		"""
		return self._get_attribute('cpDpConvergenceFactorScale')
	@CpDpConvergenceFactorScale.setter
	def CpDpConvergenceFactorScale(self, value):
		self._set_attribute('cpDpConvergenceFactorScale', value)

	@property
	def CpDpConvergenceTime(self):
		"""Indicates the convergence time.

		Returns:
			number
		"""
		return self._get_attribute('cpDpConvergenceTime')
	@CpDpConvergenceTime.setter
	def CpDpConvergenceTime(self, value):
		self._set_attribute('cpDpConvergenceTime', value)

	@property
	def CustomFramesizeValue(self):
		"""Sets the custom frame size value.

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
	def DelayAfterFailover(self):
		"""Sets the delay after failover.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterFailover')
	@DelayAfterFailover.setter
	def DelayAfterFailover(self, value):
		self._set_attribute('delayAfterFailover', value)

	@property
	def DelayBeforeFailover(self):
		"""Sets the delay before failover.

		Returns:
			number
		"""
		return self._get_attribute('delayBeforeFailover')
	@DelayBeforeFailover.setter
	def DelayBeforeFailover(self, value):
		self._set_attribute('delayBeforeFailover', value)

	@property
	def DeleteFlowsAtStartup(self):
		"""If true, the test will delete the flowgroups at startup.

		Returns:
			bool
		"""
		return self._get_attribute('deleteFlowsAtStartup')
	@DeleteFlowsAtStartup.setter
	def DeleteFlowsAtStartup(self, value):
		self._set_attribute('deleteFlowsAtStartup', value)

	@property
	def DpDpConvergenceFactorScale(self):
		"""Indicates the convergence factor scale.

		Returns:
			str
		"""
		return self._get_attribute('dpDpConvergenceFactorScale')
	@DpDpConvergenceFactorScale.setter
	def DpDpConvergenceFactorScale(self, value):
		self._set_attribute('dpDpConvergenceFactorScale', value)

	@property
	def DpDpConvergenceTime(self):
		"""Indicates the convergence time.

		Returns:
			number
		"""
		return self._get_attribute('dpDpConvergenceTime')
	@DpDpConvergenceTime.setter
	def DpDpConvergenceTime(self, value):
		self._set_attribute('dpDpConvergenceTime', value)

	@property
	def EnableCpDpPassFail(self):
		"""Enables the CP DP pass fail.

		Returns:
			bool
		"""
		return self._get_attribute('enableCpDpPassFail')
	@EnableCpDpPassFail.setter
	def EnableCpDpPassFail(self, value):
		self._set_attribute('enableCpDpPassFail', value)

	@property
	def EnableDpDpPassFail(self):
		"""Enables the DP DP pass fail

		Returns:
			bool
		"""
		return self._get_attribute('enableDpDpPassFail')
	@EnableDpDpPassFail.setter
	def EnableDpDpPassFail(self, value):
		self._set_attribute('enableDpDpPassFail', value)

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
	def FailureMode(self):
		"""Sets the failure mode.

		Returns:
			str(delPrimaryFlow|modifyRxPort)
		"""
		return self._get_attribute('failureMode')
	@FailureMode.setter
	def FailureMode(self, value):
		self._set_attribute('failureMode', value)

	@property
	def FailureType(self):
		"""Sets the type of failure.

		Returns:
			str(proactive)
		"""
		return self._get_attribute('failureType')
	@FailureType.setter
	def FailureType(self, value):
		self._set_attribute('failureType', value)

	@property
	def ForceContinuosTraffic(self):
		"""Forces continuous traffic.

		Returns:
			bool
		"""
		return self._get_attribute('forceContinuosTraffic')
	@ForceContinuosTraffic.setter
	def ForceContinuosTraffic(self, value):
		self._set_attribute('forceContinuosTraffic', value)

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
		"""The integer value that states the number of trials permitted.

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
	def ReportConvergenceUnit(self):
		"""The unit in which convergence will be reported.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('reportConvergenceUnit')
	@ReportConvergenceUnit.setter
	def ReportConvergenceUnit(self, value):
		self._set_attribute('reportConvergenceUnit', value)

	@property
	def ReportTputRateUnit(self):
		"""The unit of rate for throughput.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def SecondaryRxPort(self):
		"""Sets the secondary receiving Port.

		Returns:
			number
		"""
		return self._get_attribute('secondaryRxPort')
	@SecondaryRxPort.setter
	def SecondaryRxPort(self, value):
		self._set_attribute('secondaryRxPort', value)

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

	def update(self, CpDpConvergenceFactorScale=None, CpDpConvergenceTime=None, CustomFramesizeValue=None, CustomLoadUnit=None, DelayAfterFailover=None, DelayBeforeFailover=None, DeleteFlowsAtStartup=None, DpDpConvergenceFactorScale=None, DpDpConvergenceTime=None, EnableCpDpPassFail=None, EnableDpDpPassFail=None, EnableMinFrameSize=None, FailureMode=None, FailureType=None, ForceContinuosTraffic=None, FrameSizeMode=None, Gap=None, LoadRateValue=None, MaxRandomFrameSize=None, MinRandomFrameSize=None, Numtrials=None, ProtocolItem=None, ReportConvergenceUnit=None, ReportTputRateUnit=None, SecondaryRxPort=None, TestTrafficType=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			CpDpConvergenceFactorScale (str): Indicates the convergence factor scale.
			CpDpConvergenceTime (number): Indicates the convergence time.
			CustomFramesizeValue (number): Sets the custom frame size value.
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the custom load unit.
			DelayAfterFailover (number): Sets the delay after failover.
			DelayBeforeFailover (number): Sets the delay before failover.
			DeleteFlowsAtStartup (bool): If true, the test will delete the flowgroups at startup.
			DpDpConvergenceFactorScale (str): Indicates the convergence factor scale.
			DpDpConvergenceTime (number): Indicates the convergence time.
			EnableCpDpPassFail (bool): Enables the CP DP pass fail.
			EnableDpDpPassFail (bool): Enables the DP DP pass fail
			EnableMinFrameSize (bool): If true, enables minimum frame size.
			FailureMode (str(delPrimaryFlow|modifyRxPort)): Sets the failure mode.
			FailureType (str(proactive)): Sets the type of failure.
			ForceContinuosTraffic (bool): Forces continuous traffic.
			FrameSizeMode (str(increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			Gap (number): The gap in transmission of frames.
			LoadRateValue (number): The value of the load rate.
			MaxRandomFrameSize (number): The maximum random frame size to be sent.
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			Numtrials (number): The integer value that states the number of trials permitted.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			ReportConvergenceUnit (str(ms|ns|us)): The unit in which convergence will be reported.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The unit of rate for throughput.
			SecondaryRxPort (number): Sets the secondary receiving Port.
			TestTrafficType (str): It signifies the test traffic type value.

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
