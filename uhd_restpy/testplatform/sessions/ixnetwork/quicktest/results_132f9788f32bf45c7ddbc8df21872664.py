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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Results(Base):
    """This object shows the results of the session rate setup in progress.
    The Results class encapsulates a required results resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'results'
    _SDM_ATT_MAP = {
        'CurrentActions': 'currentActions',
        'CurrentViews': 'currentViews',
        'Duration': 'duration',
        'IsRunning': 'isRunning',
        'Progress': 'progress',
        'Result': 'result',
        'ResultPath': 'resultPath',
        'StartTime': 'startTime',
        'Status': 'status',
        'TrafficStatus': 'trafficStatus',
        'WaitingStatus': 'waitingStatus',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Results, self).__init__(parent, list_op)

    @property
    def CurrentActions(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str[AgingTable | ApplyFlowGroups | CheckingForAvailableStats | CheckingLicense | ClearingStats | CollectingStats | DropLink | frameLossCriteriaNotMet | HoldDown | InitializingTest | IterationStart | LicenseFailed | LicenseVerified | None | NoRibInConvergenceStopping | ReleasingResources | SendingLearningFrames | SetTestConfiguration | SetupStatisticsCollection | StartingTraffic | TestEnded | TestStarted | ThresholdReachedStopping | TransmittingComplete | TransmittingFrames | WaitAfterFailover | WaitBeforeFailover | WaitingAfterLearningFramesSent | WaitingBeforeSendingTraffic | WaitingForDelayBetweenIterations | WaitingForPorts | WaitingForStats | WaitingTrafficToStop])): Current actions
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentActions'])

    @property
    def CurrentViews(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Views used by this QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentViews'])

    @property
    def Duration(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test duration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])

    @property
    def IsRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether the test is currently running
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRunning'])

    @property
    def Progress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test progress
        """
        return self._get_attribute(self._SDM_ATT_MAP['Progress'])

    @property
    def Result(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test result
        """
        return self._get_attribute(self._SDM_ATT_MAP['Result'])

    @property
    def ResultPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Folder containing test result files
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResultPath'])

    @property
    def StartTime(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test start time
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartTime'])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test status
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TrafficStatus(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number): Test traffic status
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficStatus'])

    @property
    def WaitingStatus(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number): Test waiting status
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitingStatus'])

    def find(self, CurrentActions=None, CurrentViews=None, Duration=None, IsRunning=None, Progress=None, Result=None, ResultPath=None, StartTime=None, Status=None, TrafficStatus=None, WaitingStatus=None):
        """Finds and retrieves results resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve results resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all results resources from the server.

        Args
        ----
        - CurrentActions (list(dict(arg1:str,arg2:str[AgingTable | ApplyFlowGroups | CheckingForAvailableStats | CheckingLicense | ClearingStats | CollectingStats | DropLink | frameLossCriteriaNotMet | HoldDown | InitializingTest | IterationStart | LicenseFailed | LicenseVerified | None | NoRibInConvergenceStopping | ReleasingResources | SendingLearningFrames | SetTestConfiguration | SetupStatisticsCollection | StartingTraffic | TestEnded | TestStarted | ThresholdReachedStopping | TransmittingComplete | TransmittingFrames | WaitAfterFailover | WaitBeforeFailover | WaitingAfterLearningFramesSent | WaitingBeforeSendingTraffic | WaitingForDelayBetweenIterations | WaitingForPorts | WaitingForStats | WaitingTrafficToStop]))): Current actions
        - CurrentViews (list(str)): Views used by this QuickTest
        - Duration (str): Test duration
        - IsRunning (bool): Indicates whether the test is currently running
        - Progress (str): Test progress
        - Result (str): Test result
        - ResultPath (str): Folder containing test result files
        - StartTime (str): Test start time
        - Status (str): Test status
        - TrafficStatus (dict(arg1:number,arg2:number)): Test traffic status
        - WaitingStatus (dict(arg1:number,arg2:number)): Test waiting status

        Returns
        -------
        - self: This instance with matching results resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of results data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the results resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('waitForTest', payload=payload, response_object=None)
