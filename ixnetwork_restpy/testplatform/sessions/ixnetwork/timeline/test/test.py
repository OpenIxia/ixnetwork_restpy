# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
from typing import List, Any, Union


class Test(Base):
    """
    The Test class encapsulates a list of test resources that are managed by the system.
    A list of resources can be retrieved from the server using the Test.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'test'
    _SDM_ATT_MAP = {
        'AvailableTrackBy': 'availableTrackBy',
        'ConfigId': 'configId',
        'Enabled': 'enabled',
        'EndTime': 'endTime',
        'MonitorPorts': 'monitorPorts',
        'MonitorTrafficItemId': 'monitorTrafficItemId',
        'Name': 'name',
        'NowTime': 'nowTime',
        'QuickTestId': 'quickTestId',
        'StartTime': 'startTime',
        'State': 'state',
        'SupportsMonitoring': 'supportsMonitoring',
        'SupportsTiming': 'supportsTiming',
        'TimingPort': 'timingPort',
        'TimingTopologyId': 'timingTopologyId',
        'TimingTrafficItemId': 'timingTrafficItemId',
        'TrackBy': 'trackBy',
        'TrafficItemIds': 'trafficItemIds',
    }
    _SDM_ENUM_MAP = {
        'state': ['cancelled', 'cpDpConvergenceNotReached', 'fail', 'failedCriteria', 'pass', 'preflightCheck', 'preflightFail', 'ribInConvergenceThresholdNotReached', 'running', 'skipped', 'waitingForStart'],
    }

    def __init__(self, parent, list_op=False):
        super(Test, self).__init__(parent, list_op)

    @property
    def AvailableTrackBy(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): Shows all possible tracking options
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableTrackBy'])

    @property
    def ConfigId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: ID number of the added test
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigId'])

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Boolean, If True, the test will be included in Timeline for running. If false, the test will be skipped from execution
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EndTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: End time for the test
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndTime'])

    @property
    def MonitorPorts(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Showing the monitor port , also the hardware
        """
        return self._get_attribute(self._SDM_ATT_MAP['MonitorPorts'])
    @MonitorPorts.setter
    def MonitorPorts(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['MonitorPorts'], value)

    @property
    def MonitorTrafficItemId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MonitorTrafficItemId'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Quick Test name property
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def NowTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Current time
        """
        return self._get_attribute(self._SDM_ATT_MAP['NowTime'])

    @property
    def QuickTestId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/quickTest/.../*): The id of the QT
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickTestId'])

    @property
    def StartTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Start time for the test
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartTime'])

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart): Current state of the QT
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])
    @State.setter
    def State(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['State'], value)

    @property
    def SupportsMonitoring(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Boolean, True if a monitor port is selected for a test
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsMonitoring'])

    @property
    def SupportsTiming(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Boolean, True if a timing port is selected for a test
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsTiming'])

    @property
    def TimingPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Showing the timing port, also the hardware
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimingPort'])
    @TimingPort.setter
    def TimingPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TimingPort'], value)

    @property
    def TimingTopologyId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology): The id for the topology with timing port (when a timing port is used)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimingTopologyId'])

    @property
    def TimingTrafficItemId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimingTrafficItemId'])

    @property
    def TrackBy(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Currently set tracking options
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackBy'])
    @TrackBy.setter
    def TrackBy(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrackBy'], value)

    @property
    def TrafficItemIds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem]): Id(s) of traffic item(s)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemIds'])
    @TrafficItemIds.setter
    def TrafficItemIds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemIds'], value)

    def update(self, Enabled=None, MonitorPorts=None, State=None, TimingPort=None, TrackBy=None, TrafficItemIds=None):
        # type: (bool, List[str], str, str, List[str], List[str]) -> Test
        """Updates test resource on the server.

        Args
        ----
        - Enabled (bool): Boolean, If True, the test will be included in Timeline for running. If false, the test will be skipped from execution
        - MonitorPorts (list(str)): Showing the monitor port , also the hardware
        - State (str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart)): Current state of the QT
        - TimingPort (str): Showing the timing port, also the hardware
        - TrackBy (list(str)): Currently set tracking options
        - TrafficItemIds (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem])): Id(s) of traffic item(s)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, MonitorPorts=None, State=None, TimingPort=None, TrackBy=None, TrafficItemIds=None):
        # type: (bool, List[str], str, str, List[str], List[str]) -> Test
        """Adds a new test resource on the json, only valid with config assistant

        Args
        ----
        - Enabled (bool): Boolean, If True, the test will be included in Timeline for running. If false, the test will be skipped from execution
        - MonitorPorts (list(str)): Showing the monitor port , also the hardware
        - State (str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart)): Current state of the QT
        - TimingPort (str): Showing the timing port, also the hardware
        - TrackBy (list(str)): Currently set tracking options
        - TrafficItemIds (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem])): Id(s) of traffic item(s)

        Returns
        -------
        - self: This instance with all currently retrieved test resources using find and the newly added test resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableTrackBy=None, ConfigId=None, Enabled=None, EndTime=None, MonitorPorts=None, MonitorTrafficItemId=None, Name=None, NowTime=None, QuickTestId=None, StartTime=None, State=None, SupportsMonitoring=None, SupportsTiming=None, TimingPort=None, TimingTopologyId=None, TimingTrafficItemId=None, TrackBy=None, TrafficItemIds=None):
        """Finds and retrieves test resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve test resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all test resources from the server.

        Args
        ----
        - AvailableTrackBy (list(dict(arg1:str,arg2:str))): Shows all possible tracking options
        - ConfigId (number): ID number of the added test
        - Enabled (bool): Boolean, If True, the test will be included in Timeline for running. If false, the test will be skipped from execution
        - EndTime (str): End time for the test
        - MonitorPorts (list(str)): Showing the monitor port , also the hardware
        - MonitorTrafficItemId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem)): 
        - Name (str): Quick Test name property
        - NowTime (str): Current time
        - QuickTestId (str(None | /api/v1/sessions/1/ixnetwork/quickTest/.../*)): The id of the QT
        - StartTime (str): Start time for the test
        - State (str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart)): Current state of the QT
        - SupportsMonitoring (bool): Boolean, True if a monitor port is selected for a test
        - SupportsTiming (bool): Boolean, True if a timing port is selected for a test
        - TimingPort (str): Showing the timing port, also the hardware
        - TimingTopologyId (str(None | /api/v1/sessions/1/ixnetwork/topology)): The id for the topology with timing port (when a timing port is used)
        - TimingTrafficItemId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem)): 
        - TrackBy (list(str)): Currently set tracking options
        - TrafficItemIds (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem])): Id(s) of traffic item(s)

        Returns
        -------
        - self: This instance with matching test resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of test data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the test resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
