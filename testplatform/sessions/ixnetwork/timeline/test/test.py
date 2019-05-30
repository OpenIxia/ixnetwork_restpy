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


class Test(Base):
	"""The Test class encapsulates a system managed test node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Test property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'test'

	def __init__(self, parent):
		super(Test, self).__init__(parent)

	@property
	def AvailableTrackBy(self):
		"""

		Returns:
			list(dict(arg1:str,arg2:str))
		"""
		return self._get_attribute('availableTrackBy')

	@property
	def ConfigId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('configId')

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

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
	def IncrementalState(self):
		"""

		Returns:
			dict(arg1:number,arg2:number)
		"""
		return self._get_attribute('incrementalState')

	@property
	def MonitorPorts(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('monitorPorts')
	@MonitorPorts.setter
	def MonitorPorts(self, value):
		self._set_attribute('monitorPorts', value)

	@property
	def MonitorTrafficItemId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem)
		"""
		return self._get_attribute('monitorTrafficItemId')

	@property
	def NowTime(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('nowTime')

	@property
	def PreflightCheckState(self):
		"""

		Returns:
			str(license|none|portLink|protocols|traffic|validity)
		"""
		return self._get_attribute('preflightCheckState')

	@property
	def PreflightComplete(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('preflightComplete')

	@property
	def QuickTestId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/quickTest?deepchild=*)
		"""
		return self._get_attribute('quickTestId')

	@property
	def Repeat(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('repeat')
	@Repeat.setter
	def Repeat(self, value):
		self._set_attribute('repeat', value)

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
			str(cancelled|cpDpConvergenceNotReached|fail|failedCriteria|pass|preflightCheck|preflightFail|ribInConvergenceThresholdNotReached|running|skipped|waitingForStart)
		"""
		return self._get_attribute('state')
	@State.setter
	def State(self, value):
		self._set_attribute('state', value)

	@property
	def SupportsMonitoring(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('supportsMonitoring')

	@property
	def SupportsTiming(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('supportsTiming')

	@property
	def TimingPort(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('timingPort')
	@TimingPort.setter
	def TimingPort(self, value):
		self._set_attribute('timingPort', value)

	@property
	def TimingTopologyId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('timingTopologyId')

	@property
	def TimingTrafficItemId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem)
		"""
		return self._get_attribute('timingTrafficItemId')

	@property
	def TrackBy(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('trackBy')
	@TrackBy.setter
	def TrackBy(self, value):
		self._set_attribute('trackBy', value)

	@property
	def TrafficItemIds(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])
		"""
		return self._get_attribute('trafficItemIds')
	@TrafficItemIds.setter
	def TrafficItemIds(self, value):
		self._set_attribute('trafficItemIds', value)

	def update(self, Enabled=None, EndTimeAsTicks=None, MonitorPorts=None, Repeat=None, StartTimeAsTicks=None, State=None, TimingPort=None, TrackBy=None, TrafficItemIds=None):
		"""Updates a child instance of test on the server.

		Args:
			Enabled (bool): 
			EndTimeAsTicks (number): 
			MonitorPorts (list(str)): 
			Repeat (number): 
			StartTimeAsTicks (number): 
			State (str(cancelled|cpDpConvergenceNotReached|fail|failedCriteria|pass|preflightCheck|preflightFail|ribInConvergenceThresholdNotReached|running|skipped|waitingForStart)): 
			TimingPort (str): 
			TrackBy (list(str)): 
			TrafficItemIds (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): 

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, AvailableTrackBy=None, ConfigId=None, Enabled=None, EndTime=None, EndTimeAsTicks=None, IncrementalState=None, MonitorPorts=None, MonitorTrafficItemId=None, NowTime=None, PreflightCheckState=None, PreflightComplete=None, QuickTestId=None, Repeat=None, StartTime=None, StartTimeAsTicks=None, State=None, SupportsMonitoring=None, SupportsTiming=None, TimingPort=None, TimingTopologyId=None, TimingTrafficItemId=None, TrackBy=None, TrafficItemIds=None):
		"""Finds and retrieves test data from the server.

		All named parameters support regex and can be used to selectively retrieve test data from the server.
		By default the find method takes no parameters and will retrieve all test data from the server.

		Args:
			AvailableTrackBy (list(dict(arg1:str,arg2:str))): 
			ConfigId (number): 
			Enabled (bool): 
			EndTime (str): 
			EndTimeAsTicks (number): 
			IncrementalState (dict(arg1:number,arg2:number)): 
			MonitorPorts (list(str)): 
			MonitorTrafficItemId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem)): 
			NowTime (str): 
			PreflightCheckState (str(license|none|portLink|protocols|traffic|validity)): 
			PreflightComplete (bool): 
			QuickTestId (str(None|/api/v1/sessions/1/ixnetwork/quickTest?deepchild=*)): 
			Repeat (number): 
			StartTime (str): 
			StartTimeAsTicks (number): 
			State (str(cancelled|cpDpConvergenceNotReached|fail|failedCriteria|pass|preflightCheck|preflightFail|ribInConvergenceThresholdNotReached|running|skipped|waitingForStart)): 
			SupportsMonitoring (bool): 
			SupportsTiming (bool): 
			TimingPort (str): 
			TimingTopologyId (str): 
			TimingTrafficItemId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem)): 
			TrackBy (list(str)): 
			TrafficItemIds (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): 

		Returns:
			self: This instance with matching test data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of test data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the test data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
