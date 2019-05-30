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
	def CustomLoadUnit(self):
		"""

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def DataPlaneJitterWindow(self):
		"""

		Returns:
			str(k_10485760|k_1310720|k_167772160|k_20971520|k_2621440|k_335544320|k_41943040|k_5242880|k_671088640|k_83886080)
		"""
		return self._get_attribute('dataPlaneJitterWindow')
	@DataPlaneJitterWindow.setter
	def DataPlaneJitterWindow(self, value):
		self._set_attribute('dataPlaneJitterWindow', value)

	@property
	def EnableBFD(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableBFD')
	@EnableBFD.setter
	def EnableBFD(self, value):
		self._set_attribute('enableBFD', value)

	@property
	def EnableTolerance(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableTolerance')
	@EnableTolerance.setter
	def EnableTolerance(self, value):
		self._set_attribute('enableTolerance', value)

	@property
	def FailoverMode(self):
		"""

		Returns:
			str(portDown|withdrawRoutes)
		"""
		return self._get_attribute('failoverMode')
	@FailoverMode.setter
	def FailoverMode(self, value):
		self._set_attribute('failoverMode', value)

	@property
	def FailoverPortIndex(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('failoverPortIndex')
	@FailoverPortIndex.setter
	def FailoverPortIndex(self, value):
		self._set_attribute('failoverPortIndex', value)

	@property
	def FixedFrameSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('fixedFrameSize')
	@FixedFrameSize.setter
	def FixedFrameSize(self, value):
		self._set_attribute('fixedFrameSize', value)

	@property
	def ForceContinuosTraffic(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('forceContinuosTraffic')
	@ForceContinuosTraffic.setter
	def ForceContinuosTraffic(self, value):
		self._set_attribute('forceContinuosTraffic', value)

	@property
	def FrameSizeMode(self):
		"""

		Returns:
			str(fixed)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def Framesize(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def HoldDownTimer(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('holdDownTimer')
	@HoldDownTimer.setter
	def HoldDownTimer(self, value):
		self._set_attribute('holdDownTimer', value)

	@property
	def IpRatioMode(self):
		"""

		Returns:
			str(custom|fixed|increment|random)
		"""
		return self._get_attribute('ipRatioMode')
	@IpRatioMode.setter
	def IpRatioMode(self, value):
		self._set_attribute('ipRatioMode', value)

	@property
	def Ipv4rate(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ipv4rate')
	@Ipv4rate.setter
	def Ipv4rate(self, value):
		self._set_attribute('ipv4rate', value)

	@property
	def Ipv6rate(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ipv6rate')
	@Ipv6rate.setter
	def Ipv6rate(self, value):
		self._set_attribute('ipv6rate', value)

	@property
	def LoadRateValue(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('loadRateValue')
	@LoadRateValue.setter
	def LoadRateValue(self, value):
		self._set_attribute('loadRateValue', value)

	@property
	def LoadType(self):
		"""

		Returns:
			str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def NetworkGroupRoutesType(self):
		"""

		Returns:
			str(ipv4|ipv4/ipv6|ipv6)
		"""
		return self._get_attribute('networkGroupRoutesType')
	@NetworkGroupRoutesType.setter
	def NetworkGroupRoutesType(self, value):
		self._set_attribute('networkGroupRoutesType', value)

	@property
	def NetworkGroupSizeListIpv4(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('networkGroupSizeListIpv4')
	@NetworkGroupSizeListIpv4.setter
	def NetworkGroupSizeListIpv4(self, value):
		self._set_attribute('networkGroupSizeListIpv4', value)

	@property
	def NetworkGroupSizeListIpv6(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('networkGroupSizeListIpv6')
	@NetworkGroupSizeListIpv6.setter
	def NetworkGroupSizeListIpv6(self, value):
		self._set_attribute('networkGroupSizeListIpv6', value)

	@property
	def NetworkGroupSizeModeIpv4(self):
		"""

		Returns:
			str(custom)
		"""
		return self._get_attribute('networkGroupSizeModeIpv4')
	@NetworkGroupSizeModeIpv4.setter
	def NetworkGroupSizeModeIpv4(self, value):
		self._set_attribute('networkGroupSizeModeIpv4', value)

	@property
	def NetworkGroupSizeModeIpv6(self):
		"""

		Returns:
			str(custom)
		"""
		return self._get_attribute('networkGroupSizeModeIpv6')
	@NetworkGroupSizeModeIpv6.setter
	def NetworkGroupSizeModeIpv6(self, value):
		self._set_attribute('networkGroupSizeModeIpv6', value)

	@property
	def Numtrials(self):
		"""

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
		"""

		Returns:
			str(ms|s|us)
		"""
		return self._get_attribute('reportConvergenceUnit')
	@ReportConvergenceUnit.setter
	def ReportConvergenceUnit(self, value):
		self._set_attribute('reportConvergenceUnit', value)

	@property
	def ReportPacketLossDurationUnit(self):
		"""

		Returns:
			str(ms)
		"""
		return self._get_attribute('reportPacketLossDurationUnit')
	@ReportPacketLossDurationUnit.setter
	def ReportPacketLossDurationUnit(self, value):
		self._set_attribute('reportPacketLossDurationUnit', value)

	@property
	def ReportTputRateUnit(self):
		"""

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def RoutesDistribution(self):
		"""

		Returns:
			str(distributedAcrossPorts|equalCostOnEachPort)
		"""
		return self._get_attribute('routesDistribution')
	@RoutesDistribution.setter
	def RoutesDistribution(self, value):
		self._set_attribute('routesDistribution', value)

	@property
	def TestMethodology(self):
		"""

		Returns:
			str(packetLossDuration|trueViewConvergence)
		"""
		return self._get_attribute('testMethodology')
	@TestMethodology.setter
	def TestMethodology(self, value):
		self._set_attribute('testMethodology', value)

	@property
	def TestTrafficType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('testTrafficType')
	@TestTrafficType.setter
	def TestTrafficType(self, value):
		self._set_attribute('testTrafficType', value)

	@property
	def Threshold(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('threshold')
	@Threshold.setter
	def Threshold(self, value):
		self._set_attribute('threshold', value)

	@property
	def TimeoutAfterFailover(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('timeoutAfterFailover')
	@TimeoutAfterFailover.setter
	def TimeoutAfterFailover(self, value):
		self._set_attribute('timeoutAfterFailover', value)

	@property
	def TimeoutBeforeFailover(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('timeoutBeforeFailover')
	@TimeoutBeforeFailover.setter
	def TimeoutBeforeFailover(self, value):
		self._set_attribute('timeoutBeforeFailover', value)

	@property
	def Tolerance(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	def update(self, CustomLoadUnit=None, DataPlaneJitterWindow=None, EnableBFD=None, EnableTolerance=None, FailoverMode=None, FailoverPortIndex=None, FixedFrameSize=None, ForceContinuosTraffic=None, FrameSizeMode=None, Framesize=None, HoldDownTimer=None, IpRatioMode=None, Ipv4rate=None, Ipv6rate=None, LoadRateValue=None, LoadType=None, NetworkGroupRoutesType=None, NetworkGroupSizeListIpv4=None, NetworkGroupSizeListIpv6=None, NetworkGroupSizeModeIpv4=None, NetworkGroupSizeModeIpv6=None, Numtrials=None, ProtocolItem=None, ReportConvergenceUnit=None, ReportPacketLossDurationUnit=None, ReportTputRateUnit=None, RoutesDistribution=None, TestMethodology=None, TestTrafficType=None, Threshold=None, TimeoutAfterFailover=None, TimeoutBeforeFailover=None, Tolerance=None, TrafficType=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): 
			DataPlaneJitterWindow (str(k_10485760|k_1310720|k_167772160|k_20971520|k_2621440|k_335544320|k_41943040|k_5242880|k_671088640|k_83886080)): 
			EnableBFD (bool): 
			EnableTolerance (bool): 
			FailoverMode (str(portDown|withdrawRoutes)): 
			FailoverPortIndex (str): 
			FixedFrameSize (number): 
			ForceContinuosTraffic (bool): 
			FrameSizeMode (str(fixed)): 
			Framesize (str): 
			HoldDownTimer (number): 
			IpRatioMode (str(custom|fixed|increment|random)): 
			Ipv4rate (number): 
			Ipv6rate (number): 
			LoadRateValue (number): 
			LoadType (str(binary|combo|custom|fixed|increment|quickSearch|random|step|unchanged)): 
			NetworkGroupRoutesType (str(ipv4|ipv4/ipv6|ipv6)): 
			NetworkGroupSizeListIpv4 (list(str)): 
			NetworkGroupSizeListIpv6 (list(str)): 
			NetworkGroupSizeModeIpv4 (str(custom)): 
			NetworkGroupSizeModeIpv6 (str(custom)): 
			Numtrials (number): 
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			ReportConvergenceUnit (str(ms|s|us)): 
			ReportPacketLossDurationUnit (str(ms)): 
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): 
			RoutesDistribution (str(distributedAcrossPorts|equalCostOnEachPort)): 
			TestMethodology (str(packetLossDuration|trueViewConvergence)): 
			TestTrafficType (str): 
			Threshold (number): 
			TimeoutAfterFailover (number): 
			TimeoutBeforeFailover (number): 
			Tolerance (number): 
			TrafficType (str(burstyLoading|constantLoading)): 

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
