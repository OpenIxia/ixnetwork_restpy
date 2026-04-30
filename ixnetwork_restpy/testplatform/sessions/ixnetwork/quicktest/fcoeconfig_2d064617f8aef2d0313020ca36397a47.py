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


class FcoeConfig(Base):
    """It signifies the configuration of fibre channel over ethernet.
    The FcoeConfig class encapsulates a required fcoeConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fcoeConfig"
    _SDM_ATT_MAP = {
        "FcoeCountRandomFrameSize": "fcoeCountRandomFrameSize",
        "FcoeEnableMinFrameSize": "fcoeEnableMinFrameSize",
        "FcoeFrameSizeMode": "fcoeFrameSizeMode",
        "FcoeFramesizeList": "fcoeFramesizeList",
        "FcoeMaxIncrementFrameSize": "fcoeMaxIncrementFrameSize",
        "FcoeMaxRandomFrameSize": "fcoeMaxRandomFrameSize",
        "FcoeMinIncrementFrameSize": "fcoeMinIncrementFrameSize",
        "FcoeMinRandomFrameSize": "fcoeMinRandomFrameSize",
        "FcoeNumRetries": "fcoeNumRetries",
        "FcoeRequestRate": "fcoeRequestRate",
        "FcoeStepIncrementFrameSize": "fcoeStepIncrementFrameSize",
        "RetryInterval": "retryInterval",
    }
    _SDM_ENUM_MAP = {
        "fcoeFrameSizeMode": ["custom", "increment", "random"],
    }

    def __init__(self, parent, list_op=False):
        super(FcoeConfig, self).__init__(parent, list_op)

    @property
    def FcoeCountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the count random frame size for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeCountRandomFrameSize"])

    @FcoeCountRandomFrameSize.setter
    def FcoeCountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeCountRandomFrameSize"], value)

    @property
    def FcoeEnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it signifies the minimum frame size for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeEnableMinFrameSize"])

    @FcoeEnableMinFrameSize.setter
    def FcoeEnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeEnableMinFrameSize"], value)

    @property
    def FcoeFrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | increment | random): It signifies the frame size mode for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeFrameSizeMode"])

    @FcoeFrameSizeMode.setter
    def FcoeFrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeFrameSizeMode"], value)

    @property
    def FcoeFramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): It signifies frame size list for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeFramesizeList"])

    @FcoeFramesizeList.setter
    def FcoeFramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeFramesizeList"], value)

    @property
    def FcoeMaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the maximum increment frame size of fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeMaxIncrementFrameSize"])

    @FcoeMaxIncrementFrameSize.setter
    def FcoeMaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeMaxIncrementFrameSize"], value)

    @property
    def FcoeMaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the maximum random frame size for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeMaxRandomFrameSize"])

    @FcoeMaxRandomFrameSize.setter
    def FcoeMaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeMaxRandomFrameSize"], value)

    @property
    def FcoeMinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the minimum increment frame size of fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeMinIncrementFrameSize"])

    @FcoeMinIncrementFrameSize.setter
    def FcoeMinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeMinIncrementFrameSize"], value)

    @property
    def FcoeMinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the minimum random frame size for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeMinRandomFrameSize"])

    @FcoeMinRandomFrameSize.setter
    def FcoeMinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeMinRandomFrameSize"], value)

    @property
    def FcoeNumRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It shows the retries of number for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeNumRetries"])

    @FcoeNumRetries.setter
    def FcoeNumRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeNumRetries"], value)

    @property
    def FcoeRequestRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the request rates for fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeRequestRate"])

    @FcoeRequestRate.setter
    def FcoeRequestRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeRequestRate"], value)

    @property
    def FcoeStepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the step increment frame size of fibre channel over ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcoeStepIncrementFrameSize"])

    @FcoeStepIncrementFrameSize.setter
    def FcoeStepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcoeStepIncrementFrameSize"], value)

    @property
    def RetryInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the intervals between retries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RetryInterval"])

    @RetryInterval.setter
    def RetryInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RetryInterval"], value)

    def update(
        self,
        FcoeCountRandomFrameSize=None,
        FcoeEnableMinFrameSize=None,
        FcoeFrameSizeMode=None,
        FcoeFramesizeList=None,
        FcoeMaxIncrementFrameSize=None,
        FcoeMaxRandomFrameSize=None,
        FcoeMinIncrementFrameSize=None,
        FcoeMinRandomFrameSize=None,
        FcoeNumRetries=None,
        FcoeRequestRate=None,
        FcoeStepIncrementFrameSize=None,
        RetryInterval=None,
    ):
        # type: (int, bool, str, List[str], int, int, int, int, int, int, int, int) -> FcoeConfig
        """Updates fcoeConfig resource on the server.

        Args
        ----
        - FcoeCountRandomFrameSize (number): It signifies the count random frame size for fibre channel over ethernet.
        - FcoeEnableMinFrameSize (bool): If enabled, it signifies the minimum frame size for fibre channel over ethernet.
        - FcoeFrameSizeMode (str(custom | increment | random)): It signifies the frame size mode for fibre channel over ethernet.
        - FcoeFramesizeList (list(str)): It signifies frame size list for fibre channel over ethernet.
        - FcoeMaxIncrementFrameSize (number): It signifies the maximum increment frame size of fibre channel over ethernet.
        - FcoeMaxRandomFrameSize (number): It signifies the maximum random frame size for fibre channel over ethernet.
        - FcoeMinIncrementFrameSize (number): It signifies the minimum increment frame size of fibre channel over ethernet.
        - FcoeMinRandomFrameSize (number): It signifies the minimum random frame size for fibre channel over ethernet.
        - FcoeNumRetries (number): It shows the retries of number for fibre channel over ethernet.
        - FcoeRequestRate (number): It signifies the request rates for fibre channel over ethernet.
        - FcoeStepIncrementFrameSize (number): It signifies the step increment frame size of fibre channel over ethernet.
        - RetryInterval (number): It signifies the intervals between retries.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        FcoeCountRandomFrameSize=None,
        FcoeEnableMinFrameSize=None,
        FcoeFrameSizeMode=None,
        FcoeFramesizeList=None,
        FcoeMaxIncrementFrameSize=None,
        FcoeMaxRandomFrameSize=None,
        FcoeMinIncrementFrameSize=None,
        FcoeMinRandomFrameSize=None,
        FcoeNumRetries=None,
        FcoeRequestRate=None,
        FcoeStepIncrementFrameSize=None,
        RetryInterval=None,
    ):
        # type: (int, bool, str, List[str], int, int, int, int, int, int, int, int) -> FcoeConfig
        """Finds and retrieves fcoeConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeConfig resources from the server.

        Args
        ----
        - FcoeCountRandomFrameSize (number): It signifies the count random frame size for fibre channel over ethernet.
        - FcoeEnableMinFrameSize (bool): If enabled, it signifies the minimum frame size for fibre channel over ethernet.
        - FcoeFrameSizeMode (str(custom | increment | random)): It signifies the frame size mode for fibre channel over ethernet.
        - FcoeFramesizeList (list(str)): It signifies frame size list for fibre channel over ethernet.
        - FcoeMaxIncrementFrameSize (number): It signifies the maximum increment frame size of fibre channel over ethernet.
        - FcoeMaxRandomFrameSize (number): It signifies the maximum random frame size for fibre channel over ethernet.
        - FcoeMinIncrementFrameSize (number): It signifies the minimum increment frame size of fibre channel over ethernet.
        - FcoeMinRandomFrameSize (number): It signifies the minimum random frame size for fibre channel over ethernet.
        - FcoeNumRetries (number): It shows the retries of number for fibre channel over ethernet.
        - FcoeRequestRate (number): It signifies the request rates for fibre channel over ethernet.
        - FcoeStepIncrementFrameSize (number): It signifies the step increment frame size of fibre channel over ethernet.
        - RetryInterval (number): It signifies the intervals between retries.

        Returns
        -------
        - self: This instance with matching fcoeConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeConfig resources from the server available through an iterator or index

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
