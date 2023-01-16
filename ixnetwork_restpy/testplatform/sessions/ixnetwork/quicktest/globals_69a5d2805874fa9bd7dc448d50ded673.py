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


class Globals(Base):
    """This object holds the configurable global values of IxNetwork for interfaces and the quick test.
    The Globals class encapsulates a required globals resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "globals"
    _SDM_ATT_MAP = {
        "Comments": "comments",
        "EnableAbortIfLinkDown": "enableAbortIfLinkDown",
        "EnableCapture": "enableCapture",
        "EnableCheckLinkState": "enableCheckLinkState",
        "EnableGenerateReportAfterRun": "enableGenerateReportAfterRun",
        "EnableRebootCpu": "enableRebootCpu",
        "EnableSwitchToResult": "enableSwitchToResult",
        "EnableSwitchToStats": "enableSwitchToStats",
        "LinkDownTimeout": "linkDownTimeout",
        "MaxLinesToDisplay": "maxLinesToDisplay",
        "OutputRootPath": "outputRootPath",
        "ProductLabel": "productLabel",
        "SaveCaptureBeforeRun": "saveCaptureBeforeRun",
        "SerialNumber": "serialNumber",
        "SleepTimeAfterReboot": "sleepTimeAfterReboot",
        "TitlePageComments": "titlePageComments",
        "UseDefaultRootPath": "useDefaultRootPath",
        "UserName": "userName",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Globals, self).__init__(parent, list_op)

    @property
    def Comments(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User-specified comments for reporting
        """
        return self._get_attribute(self._SDM_ATT_MAP["Comments"])

    @Comments.setter
    def Comments(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Comments"], value)

    @property
    def EnableAbortIfLinkDown(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls how long to wait for an up link state before aborting the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAbortIfLinkDown"])

    @EnableAbortIfLinkDown.setter
    def EnableAbortIfLinkDown(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAbortIfLinkDown"], value)

    @property
    def EnableCapture(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Available only if the (L1) receive mode has been set to capture packets. Select this option to save the packet capture file.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCapture"])

    @EnableCapture.setter
    def EnableCapture(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCapture"], value)

    @property
    def EnableCheckLinkState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Initiates a link state check of the port before a test is run.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCheckLinkState"])

    @EnableCheckLinkState.setter
    def EnableCheckLinkState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCheckLinkState"], value)

    @property
    def EnableGenerateReportAfterRun(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When this option is enabled, IxNetwork automatically generates a test report after the test is complete.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGenerateReportAfterRun"])

    @EnableGenerateReportAfterRun.setter
    def EnableGenerateReportAfterRun(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGenerateReportAfterRun"], value)

    @property
    def EnableRebootCpu(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Reboots the port CPU before a test is run.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRebootCpu"])

    @EnableRebootCpu.setter
    def EnableRebootCpu(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRebootCpu"], value)

    @property
    def EnableSwitchToResult(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When this option is enabled, IxNetwork immediately switches to the result display after the test is complete.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSwitchToResult"])

    @EnableSwitchToResult.setter
    def EnableSwitchToResult(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSwitchToResult"], value)

    @property
    def EnableSwitchToStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the IxNetwork GUI immediately switches to the Result display after the test is complete.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSwitchToStats"])

    @EnableSwitchToStats.setter
    def EnableSwitchToStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSwitchToStats"], value)

    @property
    def LinkDownTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Select this option to simulate a port link being down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkDownTimeout"])

    @LinkDownTimeout.setter
    def LinkDownTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkDownTimeout"], value)

    @property
    def MaxLinesToDisplay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of lines to display.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxLinesToDisplay"])

    @MaxLinesToDisplay.setter
    def MaxLinesToDisplay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxLinesToDisplay"], value)

    @property
    def OutputRootPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This object holds the configurable output root path of IxNetwork for quick test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutputRootPath"])

    @OutputRootPath.setter
    def OutputRootPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutputRootPath"], value)

    @property
    def ProductLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User-specified product label for reporting
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProductLabel"])

    @ProductLabel.setter
    def ProductLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProductLabel"], value)

    @property
    def SaveCaptureBeforeRun(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This command saves the current capture data to the specified directory before run.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SaveCaptureBeforeRun"])

    @SaveCaptureBeforeRun.setter
    def SaveCaptureBeforeRun(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SaveCaptureBeforeRun"], value)

    @property
    def SerialNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User-specified serial number for reporting
        """
        return self._get_attribute(self._SDM_ATT_MAP["SerialNumber"])

    @SerialNumber.setter
    def SerialNumber(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SerialNumber"], value)

    @property
    def SleepTimeAfterReboot(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If a reboot is initiated, the sleep after reboot is the number of seconds to wait after the port CPU goes into sleep mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SleepTimeAfterReboot"])

    @SleepTimeAfterReboot.setter
    def SleepTimeAfterReboot(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SleepTimeAfterReboot"], value)

    @property
    def TitlePageComments(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User-specified comments for title page
        """
        return self._get_attribute(self._SDM_ATT_MAP["TitlePageComments"])

    @TitlePageComments.setter
    def TitlePageComments(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TitlePageComments"], value)

    @property
    def UseDefaultRootPath(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This object uses the default root path for quick test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseDefaultRootPath"])

    @UseDefaultRootPath.setter
    def UseDefaultRootPath(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseDefaultRootPath"], value)

    @property
    def UserName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User-specified version for reporting
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserName"])

    @UserName.setter
    def UserName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserName"], value)

    @property
    def Version(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User-specified version for reporting
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    def update(
        self,
        Comments=None,
        EnableAbortIfLinkDown=None,
        EnableCapture=None,
        EnableCheckLinkState=None,
        EnableGenerateReportAfterRun=None,
        EnableRebootCpu=None,
        EnableSwitchToResult=None,
        EnableSwitchToStats=None,
        LinkDownTimeout=None,
        MaxLinesToDisplay=None,
        OutputRootPath=None,
        ProductLabel=None,
        SaveCaptureBeforeRun=None,
        SerialNumber=None,
        SleepTimeAfterReboot=None,
        TitlePageComments=None,
        UseDefaultRootPath=None,
        UserName=None,
        Version=None,
    ):
        # type: (str, bool, bool, bool, bool, bool, bool, bool, int, int, str, str, bool, str, int, str, bool, str, str) -> Globals
        """Updates globals resource on the server.

        Args
        ----
        - Comments (str): User-specified comments for reporting
        - EnableAbortIfLinkDown (bool): Controls how long to wait for an up link state before aborting the test.
        - EnableCapture (bool): Available only if the (L1) receive mode has been set to capture packets. Select this option to save the packet capture file.
        - EnableCheckLinkState (bool): Initiates a link state check of the port before a test is run.
        - EnableGenerateReportAfterRun (bool): When this option is enabled, IxNetwork automatically generates a test report after the test is complete.
        - EnableRebootCpu (bool): Reboots the port CPU before a test is run.
        - EnableSwitchToResult (bool): When this option is enabled, IxNetwork immediately switches to the result display after the test is complete.
        - EnableSwitchToStats (bool): If true, the IxNetwork GUI immediately switches to the Result display after the test is complete.
        - LinkDownTimeout (number): Select this option to simulate a port link being down.
        - MaxLinesToDisplay (number): The maximum number of lines to display.
        - OutputRootPath (str): This object holds the configurable output root path of IxNetwork for quick test.
        - ProductLabel (str): User-specified product label for reporting
        - SaveCaptureBeforeRun (bool): This command saves the current capture data to the specified directory before run.
        - SerialNumber (str): User-specified serial number for reporting
        - SleepTimeAfterReboot (number): If a reboot is initiated, the sleep after reboot is the number of seconds to wait after the port CPU goes into sleep mode.
        - TitlePageComments (str): User-specified comments for title page
        - UseDefaultRootPath (bool): This object uses the default root path for quick test.
        - UserName (str): User-specified version for reporting
        - Version (str): User-specified version for reporting

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Comments=None,
        EnableAbortIfLinkDown=None,
        EnableCapture=None,
        EnableCheckLinkState=None,
        EnableGenerateReportAfterRun=None,
        EnableRebootCpu=None,
        EnableSwitchToResult=None,
        EnableSwitchToStats=None,
        LinkDownTimeout=None,
        MaxLinesToDisplay=None,
        OutputRootPath=None,
        ProductLabel=None,
        SaveCaptureBeforeRun=None,
        SerialNumber=None,
        SleepTimeAfterReboot=None,
        TitlePageComments=None,
        UseDefaultRootPath=None,
        UserName=None,
        Version=None,
    ):
        # type: (str, bool, bool, bool, bool, bool, bool, bool, int, int, str, str, bool, str, int, str, bool, str, str) -> Globals
        """Finds and retrieves globals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globals resources from the server.

        Args
        ----
        - Comments (str): User-specified comments for reporting
        - EnableAbortIfLinkDown (bool): Controls how long to wait for an up link state before aborting the test.
        - EnableCapture (bool): Available only if the (L1) receive mode has been set to capture packets. Select this option to save the packet capture file.
        - EnableCheckLinkState (bool): Initiates a link state check of the port before a test is run.
        - EnableGenerateReportAfterRun (bool): When this option is enabled, IxNetwork automatically generates a test report after the test is complete.
        - EnableRebootCpu (bool): Reboots the port CPU before a test is run.
        - EnableSwitchToResult (bool): When this option is enabled, IxNetwork immediately switches to the result display after the test is complete.
        - EnableSwitchToStats (bool): If true, the IxNetwork GUI immediately switches to the Result display after the test is complete.
        - LinkDownTimeout (number): Select this option to simulate a port link being down.
        - MaxLinesToDisplay (number): The maximum number of lines to display.
        - OutputRootPath (str): This object holds the configurable output root path of IxNetwork for quick test.
        - ProductLabel (str): User-specified product label for reporting
        - SaveCaptureBeforeRun (bool): This command saves the current capture data to the specified directory before run.
        - SerialNumber (str): User-specified serial number for reporting
        - SleepTimeAfterReboot (number): If a reboot is initiated, the sleep after reboot is the number of seconds to wait after the port CPU goes into sleep mode.
        - TitlePageComments (str): User-specified comments for title page
        - UseDefaultRootPath (bool): This object uses the default root path for quick test.
        - UserName (str): User-specified version for reporting
        - Version (str): User-specified version for reporting

        Returns
        -------
        - self: This instance with matching globals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of globals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globals resources from the server available through an iterator or index

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
