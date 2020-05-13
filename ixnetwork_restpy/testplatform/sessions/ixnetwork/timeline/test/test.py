# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
        'EndTimeAsTicks': 'endTimeAsTicks',
        'IncrementalState': 'incrementalState',
        'MonitorPorts': 'monitorPorts',
        'MonitorTrafficItemId': 'monitorTrafficItemId',
        'NowTime': 'nowTime',
        'PreflightCheckState': 'preflightCheckState',
        'PreflightComplete': 'preflightComplete',
        'QuickTestId': 'quickTestId',
        'Repeat': 'repeat',
        'StartTime': 'startTime',
        'StartTimeAsTicks': 'startTimeAsTicks',
        'State': 'state',
        'SupportsMonitoring': 'supportsMonitoring',
        'SupportsTiming': 'supportsTiming',
        'TimingPort': 'timingPort',
        'TimingTopologyId': 'timingTopologyId',
        'TimingTrafficItemId': 'timingTrafficItemId',
        'TrackBy': 'trackBy',
        'TrafficItemIds': 'trafficItemIds',
    }

    def __init__(self, parent):
        super(Test, self).__init__(parent)

    @property
    def AvailableTrackBy(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableTrackBy'])

    @property
    def ConfigId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigId'])

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EndTime(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndTime'])

    @property
    def EndTimeAsTicks(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndTimeAsTicks'])
    @EndTimeAsTicks.setter
    def EndTimeAsTicks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EndTimeAsTicks'], value)

    @property
    def IncrementalState(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementalState'])

    @property
    def MonitorPorts(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MonitorPorts'])
    @MonitorPorts.setter
    def MonitorPorts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MonitorPorts'], value)

    @property
    def MonitorTrafficItemId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MonitorTrafficItemId'])

    @property
    def NowTime(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NowTime'])

    @property
    def PreflightCheckState(self):
        """
        Returns
        -------
        - str(license | none | portLink | protocols | traffic | validity): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreflightCheckState'])

    @property
    def PreflightComplete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreflightComplete'])

    @property
    def QuickTestId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/quickTest/.../*): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickTestId'])

    @property
    def Repeat(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Repeat'])
    @Repeat.setter
    def Repeat(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Repeat'], value)

    @property
    def StartTime(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartTime'])

    @property
    def StartTimeAsTicks(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartTimeAsTicks'])
    @StartTimeAsTicks.setter
    def StartTimeAsTicks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartTimeAsTicks'], value)

    @property
    def State(self):
        """
        Returns
        -------
        - str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])
    @State.setter
    def State(self, value):
        self._set_attribute(self._SDM_ATT_MAP['State'], value)

    @property
    def SupportsMonitoring(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsMonitoring'])

    @property
    def SupportsTiming(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsTiming'])

    @property
    def TimingPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimingPort'])
    @TimingPort.setter
    def TimingPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimingPort'], value)

    @property
    def TimingTopologyId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimingTopologyId'])

    @property
    def TimingTrafficItemId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimingTrafficItemId'])

    @property
    def TrackBy(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackBy'])
    @TrackBy.setter
    def TrackBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackBy'], value)

    @property
    def TrafficItemIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemIds'])
    @TrafficItemIds.setter
    def TrafficItemIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemIds'], value)

    def update(self, Enabled=None, EndTimeAsTicks=None, MonitorPorts=None, Repeat=None, StartTimeAsTicks=None, State=None, TimingPort=None, TrackBy=None, TrafficItemIds=None):
        """Updates test resource on the server.

        Args
        ----
        - Enabled (bool): 
        - EndTimeAsTicks (number): 
        - MonitorPorts (list(str)): 
        - Repeat (number): 
        - StartTimeAsTicks (number): 
        - State (str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart)): 
        - TimingPort (str): 
        - TrackBy (list(str)): 
        - TrafficItemIds (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem])): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableTrackBy=None, ConfigId=None, Enabled=None, EndTime=None, EndTimeAsTicks=None, IncrementalState=None, MonitorPorts=None, MonitorTrafficItemId=None, NowTime=None, PreflightCheckState=None, PreflightComplete=None, QuickTestId=None, Repeat=None, StartTime=None, StartTimeAsTicks=None, State=None, SupportsMonitoring=None, SupportsTiming=None, TimingPort=None, TimingTopologyId=None, TimingTrafficItemId=None, TrackBy=None, TrafficItemIds=None):
        """Finds and retrieves test resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve test resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all test resources from the server.

        Args
        ----
        - AvailableTrackBy (list(dict(arg1:str,arg2:str))): 
        - ConfigId (number): 
        - Enabled (bool): 
        - EndTime (str): 
        - EndTimeAsTicks (number): 
        - IncrementalState (dict(arg1:number,arg2:number)): 
        - MonitorPorts (list(str)): 
        - MonitorTrafficItemId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem)): 
        - NowTime (str): 
        - PreflightCheckState (str(license | none | portLink | protocols | traffic | validity)): 
        - PreflightComplete (bool): 
        - QuickTestId (str(None | /api/v1/sessions/1/ixnetwork/quickTest/.../*)): 
        - Repeat (number): 
        - StartTime (str): 
        - StartTimeAsTicks (number): 
        - State (str(cancelled | cpDpConvergenceNotReached | fail | failedCriteria | pass | preflightCheck | preflightFail | ribInConvergenceThresholdNotReached | running | skipped | waitingForStart)): 
        - SupportsMonitoring (bool): 
        - SupportsTiming (bool): 
        - TimingPort (str): 
        - TimingTopologyId (str): 
        - TimingTrafficItemId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem)): 
        - TrackBy (list(str)): 
        - TrafficItemIds (list(str[None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem])): 

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
