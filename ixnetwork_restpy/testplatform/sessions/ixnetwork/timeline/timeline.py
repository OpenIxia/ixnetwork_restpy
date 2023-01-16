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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Timeline(Base):
    """It helps to run a sequence of QT tests, create configuration with test/protocol and interfaces/traffic items etc. Currently it's supported only in Linux API server
    The Timeline class encapsulates a required timeline resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "timeline"
    _SDM_ATT_MAP = {
        "CurrentTime": "currentTime",
        "EndTime": "endTime",
        "ExecutingTest": "executingTest",
        "ExecutingTestProgress": "executingTestProgress",
        "MonitorTopologyId": "monitorTopologyId",
        "PauseOnError": "pauseOnError",
        "StartTime": "startTime",
        "State": "state",
        "TestOrder": "testOrder",
        "TimingTopologyIds": "timingTopologyIds",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Timeline, self).__init__(parent, list_op)

    @property
    def Test(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.test.test.Test): An instance of the Test class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.timeline.test.test import (
            Test,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Test", None) is not None:
                return self._properties.get("Test")
        return Test(self)

    @property
    def CurrentTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Current time
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentTime"])

    @property
    def EndTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The end time of the test
        """
        return self._get_attribute(self._SDM_ATT_MAP["EndTime"])

    @property
    def ExecutingTest(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/timeline/test): The id of the test under execution
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExecutingTest"])

    @ExecutingTest.setter
    def ExecutingTest(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExecutingTest"], value)

    @property
    def ExecutingTestProgress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Current specific state for the Quick Test after the ports are connected (e.g. preflightWaitingForChassisConnect, checkingPorts, checkingProtocols, sendinglearningframes, transmittingframes, etc)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExecutingTestProgress"])

    @property
    def MonitorTopologyId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology): Id for the topology with monitor port (when a monitor port is used)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MonitorTopologyId"])

    @property
    def PauseOnError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pauses the test when an error is found
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseOnError"])

    @PauseOnError.setter
    def PauseOnError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseOnError"], value)

    @property
    def StartTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Start time of the test
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartTime"])

    @property
    def State(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str[cancelled | complete | idle | postflightReleasingPorts | postflightStoppingProtocols | postflightStoppingTimeline | preflightAggregatingCards | preflightCheckingPorts | preflightCheckingProtocols | preflightConnectingPorts | preflightFailed | preflightSettingUpPorts | preflightStart | preflightValidatingTimeline | preflightWaitingForChassisConnect | running]): The general state of the ports and QT (e.g. preflightConnectingPorts , prefligtCheckingPorts, running, complete)
        """
        return self._get_attribute(self._SDM_ATT_MAP["State"])

    @property
    def TestOrder(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/timeline/test]): The desired order for the tests to run
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestOrder"])

    @TestOrder.setter
    def TestOrder(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestOrder"], value)

    @property
    def TimingTopologyIds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): Id for the topology with timing port (when a timing port is used
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimingTopologyIds"])

    def update(self, ExecutingTest=None, PauseOnError=None, TestOrder=None):
        # type: (str, bool, List[str]) -> Timeline
        """Updates timeline resource on the server.

        Args
        ----
        - ExecutingTest (str(None | /api/v1/sessions/1/ixnetwork/timeline/test)): The id of the test under execution
        - PauseOnError (bool): Pauses the test when an error is found
        - TestOrder (list(str[None | /api/v1/sessions/1/ixnetwork/timeline/test])): The desired order for the tests to run

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CurrentTime=None,
        EndTime=None,
        ExecutingTest=None,
        ExecutingTestProgress=None,
        MonitorTopologyId=None,
        PauseOnError=None,
        StartTime=None,
        State=None,
        TestOrder=None,
        TimingTopologyIds=None,
    ):
        """Finds and retrieves timeline resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve timeline resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all timeline resources from the server.

        Args
        ----
        - CurrentTime (str): Current time
        - EndTime (str): The end time of the test
        - ExecutingTest (str(None | /api/v1/sessions/1/ixnetwork/timeline/test)): The id of the test under execution
        - ExecutingTestProgress (str): Current specific state for the Quick Test after the ports are connected (e.g. preflightWaitingForChassisConnect, checkingPorts, checkingProtocols, sendinglearningframes, transmittingframes, etc)
        - MonitorTopologyId (str(None | /api/v1/sessions/1/ixnetwork/topology)): Id for the topology with monitor port (when a monitor port is used)
        - PauseOnError (bool): Pauses the test when an error is found
        - StartTime (str): Start time of the test
        - State (dict(arg1:str,arg2:str[cancelled | complete | idle | postflightReleasingPorts | postflightStoppingProtocols | postflightStoppingTimeline | preflightAggregatingCards | preflightCheckingPorts | preflightCheckingProtocols | preflightConnectingPorts | preflightFailed | preflightSettingUpPorts | preflightStart | preflightValidatingTimeline | preflightWaitingForChassisConnect | running])): The general state of the ports and QT (e.g. preflightConnectingPorts , prefligtCheckingPorts, running, complete)
        - TestOrder (list(str[None | /api/v1/sessions/1/ixnetwork/timeline/test])): The desired order for the tests to run
        - TimingTopologyIds (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): Id for the topology with timing port (when a timing port is used

        Returns
        -------
        - self: This instance with matching timeline resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of timeline data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the timeline resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ConnectTimelinePorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the connectTimelinePorts operation on the server.

        Connect timeline ports

        connectTimelinePorts(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "connectTimelinePorts", payload=payload, response_object=None
        )

    def CreateProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the createProtocol operation on the server.

        Creates a new topology and device group (with the specified protocol in it) using timeline. Used for creating and running a QuickTest.

        createProtocol(Arg2=enum, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(bgpBfdIpv4PeerIpv4Pools | bgpBfdIpv6PeerIpv6Pools | bgpBfdMixedPeerPools | bgpIpv4PeerIpv4Pools | bgpIpv6PeerIpv6Pools | bgpMixedPeerPools | chainedIpv4 | chainedIpv6 | ethernetVlan | ipv4 | ipv4IgmpHost | ipv4IgmpQuerierHost | ipv4ipv6 | ipv6 | ipv6MldHost | ipv6MldQuerierHost)): The protocol type (from the list of supported protocol types for QT) to be created
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/topology):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("createProtocol", payload=payload, response_object=None)

    def CreateTest(self, *args, **kwargs):
        """Executes the createTest operation on the server.

        Creates a new QuickTest with traffic items and Topologies or just the test

        createTest(Arg2=enum, Arg3=enum, async_operation=bool)object
        ------------------------------------------------------------
        - Arg2 (str(rfc2544back2back | rfc2544frameLoss | rfc2544throughput | rfc2889addressCache | rfc2889addressRate | rfc3918joinLeaveDelay | rfc3918mixedClassThroughput | rfc7747failover | rfc7747ribIn | trafficTest)): The list with all supported tests
        - Arg3 (str(bgpBfdIpv4PeerIpv4Pools | bgpBfdIpv6PeerIpv6Pools | bgpBfdMixedPeerPools | bgpIpv4PeerIpv4Pools | bgpIpv6PeerIpv6Pools | bgpMixedPeerPools | chainedIpv4 | chainedIpv6 | ethernetVlan | ipv4 | ipv4IgmpHost | ipv4IgmpQuerierHost | ipv4ipv6 | ipv6 | ipv6MldHost | ipv6MldQuerierHost | none)): The list of supported protocols
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/timeline/test],arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest],arg3:list[str[None | /api/v1/sessions/1/ixnetwork/traffic/trafficItem]]):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("createTest", payload=payload, response_object=None)

    def CreateTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the createTraffic operation on the server.

        Creates the traffic item for the QuickTest, with or without protocols

        createTraffic(Arg2=enum, async_operation=bool)href
        --------------------------------------------------
        - Arg2 (str(ethernetVlan | ipv4 | ipv4WithChainedDG | ipv4WithDG | ipv6 | ipv6WithChainedDG | ipv6WithDG)): The desired traffic added from Timeline
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficItem):

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("createTraffic", payload=payload, response_object=None)

    def ReleaseTimelinePorts(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the releaseTimelinePorts operation on the server.

        Release timeline ports

        releaseTimelinePorts(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "releaseTimelinePorts", payload=payload, response_object=None
        )

    def Retry(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the retry operation on the server.

        If an error occurs when starting protocols, retry to run the QuickTest test sequence

        retry(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("retry", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the timeline QuickTest sequence

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def StartTimelineProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startTimelineProtocols operation on the server.

        Start timeline protocols

        startTimelineProtocols(async_operation=bool)
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "startTimelineProtocols", payload=payload, response_object=None
        )

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the timeline QuickTest sequence

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def StopTimelineProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopTimelineProtocols operation on the server.

        Stop timeline protocols

        stopTimelineProtocols(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "stopTimelineProtocols", payload=payload, response_object=None
        )
