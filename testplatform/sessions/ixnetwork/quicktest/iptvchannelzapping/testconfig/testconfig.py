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
	def AutomaticEnableIptvStats(self):
		"""If true, enables the automatic Iptv Statistics.

		Returns:
			str
		"""
		return self._get_attribute('automaticEnableIptvStats')
	@AutomaticEnableIptvStats.setter
	def AutomaticEnableIptvStats(self, value):
		self._set_attribute('automaticEnableIptvStats', value)

	@property
	def BackgroundTrafficEnabled(self):
		"""If true, the traffic in background is enabled.

		Returns:
			str
		"""
		return self._get_attribute('backgroundTrafficEnabled')
	@BackgroundTrafficEnabled.setter
	def BackgroundTrafficEnabled(self, value):
		self._set_attribute('backgroundTrafficEnabled', value)

	@property
	def Duration(self):
		"""Period of time over which the configured IPTV subscribers and multicast traffic sources execute the configured behavior.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableJoinFailuresMode(self):
		"""If true, Failure Mode for Joined state is enabled.

		Returns:
			str
		"""
		return self._get_attribute('enableJoinFailuresMode')
	@EnableJoinFailuresMode.setter
	def EnableJoinFailuresMode(self, value):
		self._set_attribute('enableJoinFailuresMode', value)

	@property
	def EnableLeaveFailuresMode(self):
		"""If true, Failure Mode for Leave state is enabled.

		Returns:
			str
		"""
		return self._get_attribute('enableLeaveFailuresMode')
	@EnableLeaveFailuresMode.setter
	def EnableLeaveFailuresMode(self, value):
		self._set_attribute('enableLeaveFailuresMode', value)

	@property
	def LoadType(self):
		"""The type of load used to modify the variable parameter value.

		Returns:
			str(custom)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def Numtrials(self):
		"""The number of trials that can be run for the test.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PassCriteriaJoinFailuresValue(self):
		"""Denotes the value of Join actions marked as failed.

		Returns:
			number
		"""
		return self._get_attribute('passCriteriaJoinFailuresValue')
	@PassCriteriaJoinFailuresValue.setter
	def PassCriteriaJoinFailuresValue(self, value):
		self._set_attribute('passCriteriaJoinFailuresValue', value)

	@property
	def PassCriteriaJoinLatencyValue(self):
		"""The amount of time, in milliseconds, elapsed between the time the client sent an IGMP JOIN (broadcast channel) and the time it received the first byte of data.

		Returns:
			number
		"""
		return self._get_attribute('passCriteriaJoinLatencyValue')
	@PassCriteriaJoinLatencyValue.setter
	def PassCriteriaJoinLatencyValue(self, value):
		self._set_attribute('passCriteriaJoinLatencyValue', value)

	@property
	def PassCriteriaLeaveFailuresValue(self):
		"""How many Leave actions were marked as Failed.

		Returns:
			number
		"""
		return self._get_attribute('passCriteriaLeaveFailuresValue')
	@PassCriteriaLeaveFailuresValue.setter
	def PassCriteriaLeaveFailuresValue(self, value):
		self._set_attribute('passCriteriaLeaveFailuresValue', value)

	@property
	def PassCriteriaLeaveLatencyValue(self):
		"""The amount of time, in milliseconds, elapsed between the time the client sent an IGMP LEAVE (broadcast channel) and the time it received the last byte of data.

		Returns:
			number
		"""
		return self._get_attribute('passCriteriaLeaveLatencyValue')
	@PassCriteriaLeaveLatencyValue.setter
	def PassCriteriaLeaveLatencyValue(self, value):
		self._set_attribute('passCriteriaLeaveLatencyValue', value)

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
	def StartIptvEndpointsBeforeTraffic(self):
		"""The IPTV Endpoints are set before sending traffic.

		Returns:
			str
		"""
		return self._get_attribute('startIptvEndpointsBeforeTraffic')
	@StartIptvEndpointsBeforeTraffic.setter
	def StartIptvEndpointsBeforeTraffic(self, value):
		self._set_attribute('startIptvEndpointsBeforeTraffic', value)

	@property
	def TestTrafficType(self):
		"""Indicates the type of traffic to be tested.

		Returns:
			str
		"""
		return self._get_attribute('testTrafficType')
	@TestTrafficType.setter
	def TestTrafficType(self, value):
		self._set_attribute('testTrafficType', value)

	@property
	def TrackByEgressVlanId(self):
		"""If true, Custom Offset from Packet Locations can be configured.

		Returns:
			str
		"""
		return self._get_attribute('trackByEgressVlanId')
	@TrackByEgressVlanId.setter
	def TrackByEgressVlanId(self, value):
		self._set_attribute('trackByEgressVlanId', value)

	@property
	def TrackByFlowGroup(self):
		"""It configures flow tracking for all flow groups.

		Returns:
			str
		"""
		return self._get_attribute('trackByFlowGroup')
	@TrackByFlowGroup.setter
	def TrackByFlowGroup(self, value):
		self._set_attribute('trackByFlowGroup', value)

	@property
	def TrackByIpDestination(self):
		"""If true, flows are tracked by the IPv4 Destination Address as per the route ranges configured under destination endpoint.

		Returns:
			str
		"""
		return self._get_attribute('trackByIpDestination')
	@TrackByIpDestination.setter
	def TrackByIpDestination(self, value):
		self._set_attribute('trackByIpDestination', value)

	def update(self, AutomaticEnableIptvStats=None, BackgroundTrafficEnabled=None, Duration=None, EnableJoinFailuresMode=None, EnableLeaveFailuresMode=None, LoadType=None, Numtrials=None, PassCriteriaJoinFailuresValue=None, PassCriteriaJoinLatencyValue=None, PassCriteriaLeaveFailuresValue=None, PassCriteriaLeaveLatencyValue=None, ProtocolItem=None, StartIptvEndpointsBeforeTraffic=None, TestTrafficType=None, TrackByEgressVlanId=None, TrackByFlowGroup=None, TrackByIpDestination=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			AutomaticEnableIptvStats (str): If true, enables the automatic Iptv Statistics.
			BackgroundTrafficEnabled (str): If true, the traffic in background is enabled.
			Duration (number): Period of time over which the configured IPTV subscribers and multicast traffic sources execute the configured behavior.
			EnableJoinFailuresMode (str): If true, Failure Mode for Joined state is enabled.
			EnableLeaveFailuresMode (str): If true, Failure Mode for Leave state is enabled.
			LoadType (str(custom)): The type of load used to modify the variable parameter value.
			Numtrials (number): The number of trials that can be run for the test.
			PassCriteriaJoinFailuresValue (number): Denotes the value of Join actions marked as failed.
			PassCriteriaJoinLatencyValue (number): The amount of time, in milliseconds, elapsed between the time the client sent an IGMP JOIN (broadcast channel) and the time it received the first byte of data.
			PassCriteriaLeaveFailuresValue (number): How many Leave actions were marked as Failed.
			PassCriteriaLeaveLatencyValue (number): The amount of time, in milliseconds, elapsed between the time the client sent an IGMP LEAVE (broadcast channel) and the time it received the last byte of data.
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			StartIptvEndpointsBeforeTraffic (str): The IPTV Endpoints are set before sending traffic.
			TestTrafficType (str): Indicates the type of traffic to be tested.
			TrackByEgressVlanId (str): If true, Custom Offset from Packet Locations can be configured.
			TrackByFlowGroup (str): It configures flow tracking for all flow groups.
			TrackByIpDestination (str): If true, flows are tracked by the IPv4 Destination Address as per the route ranges configured under destination endpoint.

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
