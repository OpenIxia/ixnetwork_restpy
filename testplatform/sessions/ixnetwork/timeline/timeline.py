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


class Timeline(Base):
	"""The Timeline class encapsulates a required timeline node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Timeline property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'timeline'

	def __init__(self, parent):
		super(Timeline, self).__init__(parent)

	@property
	def Test(self):
		"""An instance of the Test class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.test.test.Test)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.test.test import Test
		return Test(self)

	@property
	def CurrentTime(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('currentTime')

	@property
	def EndTime(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('endTime')

	@property
	def EndTimeAsTicks(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('endTimeAsTicks')
	@EndTimeAsTicks.setter
	def EndTimeAsTicks(self, value):
		self._set_attribute('endTimeAsTicks', value)

	@property
	def ExecutingTest(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/timeline?deepchild=test)
		"""
		return self._get_attribute('executingTest')
	@ExecutingTest.setter
	def ExecutingTest(self, value):
		self._set_attribute('executingTest', value)

	@property
	def ExecutingTestProgress(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('executingTestProgress')

	@property
	def ForceTakePorts(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('forceTakePorts')
	@ForceTakePorts.setter
	def ForceTakePorts(self, value):
		self._set_attribute('forceTakePorts', value)

	@property
	def MonitorTopologyId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/topology)
		"""
		return self._get_attribute('monitorTopologyId')

	@property
	def PauseOnError(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('pauseOnError')
	@PauseOnError.setter
	def PauseOnError(self, value):
		self._set_attribute('pauseOnError', value)

	@property
	def StartTime(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('startTime')

	@property
	def StartTimeAsTicks(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('startTimeAsTicks')
	@StartTimeAsTicks.setter
	def StartTimeAsTicks(self, value):
		self._set_attribute('startTimeAsTicks', value)

	@property
	def State(self):
		"""

		Returns:
			dict(arg1:str,arg2:str[cancelled|complete|idle|postflightReleasingPorts|postflightStoppingProtocols|postflightStoppingTimeline|preflightAggregatingCards|preflightCheckingPorts|preflightConnectingPorts|preflightFailed|preflightSettingUpChassisChain|preflightSettingUpPorts|preflightStart|preflightValidateTopologyPortCount|preflightValidatingTimeline|preflightWaitingForChassisConnect|running])
		"""
		return self._get_attribute('state')

	@property
	def TestOrder(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/timeline?deepchild=test])
		"""
		return self._get_attribute('testOrder')
	@TestOrder.setter
	def TestOrder(self, value):
		self._set_attribute('testOrder', value)

	@property
	def TimingTopologyIds(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('timingTopologyIds')

	def update(self, EndTimeAsTicks=None, ExecutingTest=None, ForceTakePorts=None, PauseOnError=None, StartTimeAsTicks=None, TestOrder=None):
		"""Updates a child instance of timeline on the server.

		Args:
			EndTimeAsTicks (number): 
			ExecutingTest (str(None|/api/v1/sessions/1/ixnetwork/timeline?deepchild=test)): 
			ForceTakePorts (bool): 
			PauseOnError (bool): 
			StartTimeAsTicks (number): 
			TestOrder (list(str[None|/api/v1/sessions/1/ixnetwork/timeline?deepchild=test])): 

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def CreateProtocol(self, *args, **kwargs):
		"""Executes the createProtocol operation on the server.

		createProtocol(Arg2:enum, Arg3:href)href
			Args:
				args[0] is Arg2 (str(bfdv4Interface|bfdv6Interface|bgpBfdIpv4Ipv6Peer|bgpBfdIpv4Peer|bgpBfdIpv4PeerIpv4Pools|bgpBfdIpv6Peer|bgpBfdIpv6PeerIpv6Pools|bgpBfdMixedPeerPools|bgpIpv4Ipv6Peer|bgpIpv4Peer|bgpIpv4PeerIpv4Pools|bgpIpv6Peer|bgpIpv6PeerIpv6Pools|bgpMixedPeerPools|chainedIpv4|chainedIpv6|ethernetVlan|ipv4|ipv4IgmpHost|ipv4IgmpQuerierHost|ipv4ipv6|ipv6|ipv6MldHost|ipv6MldQuerierHost|none)): 
				args[1] is Arg3 (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=deviceGroup)): 

			Returns:
				str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('createProtocol', payload=payload, response_object=None)

	def CreateTest(self, *args, **kwargs):
		"""Executes the createTest operation on the server.

		createTest(Arg2:enum, Arg3:enum)object
			Args:
				args[0] is Arg2 (str(rfc2544back2back|rfc2544frameLoss|rfc2544throughput|rfc2889addressCache|rfc2889addressRate|rfc3918joinLeaveDelay|rfc7747failover|rfc7747ribIn|trafficTest)): 
				args[1] is Arg3 (str(bfdv4Interface|bfdv6Interface|bgpBfdIpv4Ipv6Peer|bgpBfdIpv4Peer|bgpBfdIpv4PeerIpv4Pools|bgpBfdIpv6Peer|bgpBfdIpv6PeerIpv6Pools|bgpBfdMixedPeerPools|bgpIpv4Ipv6Peer|bgpIpv4Peer|bgpIpv4PeerIpv4Pools|bgpIpv6Peer|bgpIpv6PeerIpv6Pools|bgpMixedPeerPools|chainedIpv4|chainedIpv6|ethernetVlan|ipv4|ipv4IgmpHost|ipv4IgmpQuerierHost|ipv4ipv6|ipv6|ipv6MldHost|ipv6MldQuerierHost|none)): 

			Returns:
				dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/timeline?deepchild=test],arg2:str[None|/api/v1/sessions/1/ixnetwork/quickTest?deepchild=*],arg3:list[str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem]]): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('createTest', payload=payload, response_object=None)

	def CreateTraffic(self, *args, **kwargs):
		"""Executes the createTraffic operation on the server.

		createTraffic(Arg2:enum)href
			Args:
				args[0] is Arg2 (str(ethernetVlan|ipv4|ipv4WithChainedDG|ipv4WithDG|ipv6|ipv6WithChainedDG|ipv6WithDG)): 

			Returns:
				str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('createTraffic', payload=payload, response_object=None)

	def Retry(self):
		"""Executes the retry operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('retry', payload=payload, response_object=None)

	def Start(self):
		"""Executes the start operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
