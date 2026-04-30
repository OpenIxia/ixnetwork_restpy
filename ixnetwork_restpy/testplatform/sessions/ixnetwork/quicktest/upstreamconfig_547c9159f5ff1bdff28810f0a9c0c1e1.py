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


class UpstreamConfig(Base):
    """The configuration parameters for upstream traffic.
    The UpstreamConfig class encapsulates a required upstreamConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "upstreamConfig"
    _SDM_ATT_MAP = {
        "UpstreamCountRandomFrameSize": "upstreamCountRandomFrameSize",
        "UpstreamEnableMinFrameSize": "upstreamEnableMinFrameSize",
        "UpstreamFrameSizeMode": "upstreamFrameSizeMode",
        "UpstreamFramesizeFixedValue": "upstreamFramesizeFixedValue",
        "UpstreamFramesizeList": "upstreamFramesizeList",
        "UpstreamMaxIncrementFrameSize": "upstreamMaxIncrementFrameSize",
        "UpstreamMaxRandomFrameSize": "upstreamMaxRandomFrameSize",
        "UpstreamMinIncrementFrameSize": "upstreamMinIncrementFrameSize",
        "UpstreamMinRandomFrameSize": "upstreamMinRandomFrameSize",
        "UpstreamStepIncrementFrameSize": "upstreamStepIncrementFrameSize",
    }
    _SDM_ENUM_MAP = {
        "upstreamFrameSizeMode": ["custom", "increment", "random", "unchanged"],
    }

    def __init__(self, parent, list_op=False):
        super(UpstreamConfig, self).__init__(parent, list_op)

    @property
    def UpstreamCountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream traffic count for random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamCountRandomFrameSize"])

    @UpstreamCountRandomFrameSize.setter
    def UpstreamCountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamCountRandomFrameSize"], value)

    @property
    def UpstreamEnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables minimum frame size of upstream traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamEnableMinFrameSize"])

    @UpstreamEnableMinFrameSize.setter
    def UpstreamEnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamEnableMinFrameSize"], value)

    @property
    def UpstreamFrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | increment | random | unchanged): The upstream frame size mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamFrameSizeMode"])

    @UpstreamFrameSizeMode.setter
    def UpstreamFrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamFrameSizeMode"], value)

    @property
    def UpstreamFramesizeFixedValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream traffic frame size fixed value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamFramesizeFixedValue"])

    @UpstreamFramesizeFixedValue.setter
    def UpstreamFramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamFramesizeFixedValue"], value)

    @property
    def UpstreamFramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The upstream frame size list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamFramesizeList"])

    @UpstreamFramesizeList.setter
    def UpstreamFramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamFramesizeList"], value)

    @property
    def UpstreamMaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream traffic maximum increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMaxIncrementFrameSize"])

    @UpstreamMaxIncrementFrameSize.setter
    def UpstreamMaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMaxIncrementFrameSize"], value)

    @property
    def UpstreamMaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream maximum random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMaxRandomFrameSize"])

    @UpstreamMaxRandomFrameSize.setter
    def UpstreamMaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMaxRandomFrameSize"], value)

    @property
    def UpstreamMinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream minimum increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMinIncrementFrameSize"])

    @UpstreamMinIncrementFrameSize.setter
    def UpstreamMinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMinIncrementFrameSize"], value)

    @property
    def UpstreamMinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream traffic random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMinRandomFrameSize"])

    @UpstreamMinRandomFrameSize.setter
    def UpstreamMinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMinRandomFrameSize"], value)

    @property
    def UpstreamStepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream traffic step increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamStepIncrementFrameSize"])

    @UpstreamStepIncrementFrameSize.setter
    def UpstreamStepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamStepIncrementFrameSize"], value)

    def update(
        self,
        UpstreamCountRandomFrameSize=None,
        UpstreamEnableMinFrameSize=None,
        UpstreamFrameSizeMode=None,
        UpstreamFramesizeFixedValue=None,
        UpstreamFramesizeList=None,
        UpstreamMaxIncrementFrameSize=None,
        UpstreamMaxRandomFrameSize=None,
        UpstreamMinIncrementFrameSize=None,
        UpstreamMinRandomFrameSize=None,
        UpstreamStepIncrementFrameSize=None,
    ):
        # type: (int, bool, str, int, List[str], int, int, int, int, int) -> UpstreamConfig
        """Updates upstreamConfig resource on the server.

        Args
        ----
        - UpstreamCountRandomFrameSize (number): The upstream traffic count for random frame size.
        - UpstreamEnableMinFrameSize (bool): Enables minimum frame size of upstream traffic.
        - UpstreamFrameSizeMode (str(custom | increment | random | unchanged)): The upstream frame size mode.
        - UpstreamFramesizeFixedValue (number): The upstream traffic frame size fixed value.
        - UpstreamFramesizeList (list(str)): The upstream frame size list.
        - UpstreamMaxIncrementFrameSize (number): The upstream traffic maximum increment frame size.
        - UpstreamMaxRandomFrameSize (number): The upstream maximum random frame size.
        - UpstreamMinIncrementFrameSize (number): The upstream minimum increment frame size.
        - UpstreamMinRandomFrameSize (number): The upstream traffic random frame size.
        - UpstreamStepIncrementFrameSize (number): The upstream traffic step increment frame size.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        UpstreamCountRandomFrameSize=None,
        UpstreamEnableMinFrameSize=None,
        UpstreamFrameSizeMode=None,
        UpstreamFramesizeFixedValue=None,
        UpstreamFramesizeList=None,
        UpstreamMaxIncrementFrameSize=None,
        UpstreamMaxRandomFrameSize=None,
        UpstreamMinIncrementFrameSize=None,
        UpstreamMinRandomFrameSize=None,
        UpstreamStepIncrementFrameSize=None,
    ):
        # type: (int, bool, str, int, List[str], int, int, int, int, int) -> UpstreamConfig
        """Finds and retrieves upstreamConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve upstreamConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all upstreamConfig resources from the server.

        Args
        ----
        - UpstreamCountRandomFrameSize (number): The upstream traffic count for random frame size.
        - UpstreamEnableMinFrameSize (bool): Enables minimum frame size of upstream traffic.
        - UpstreamFrameSizeMode (str(custom | increment | random | unchanged)): The upstream frame size mode.
        - UpstreamFramesizeFixedValue (number): The upstream traffic frame size fixed value.
        - UpstreamFramesizeList (list(str)): The upstream frame size list.
        - UpstreamMaxIncrementFrameSize (number): The upstream traffic maximum increment frame size.
        - UpstreamMaxRandomFrameSize (number): The upstream maximum random frame size.
        - UpstreamMinIncrementFrameSize (number): The upstream minimum increment frame size.
        - UpstreamMinRandomFrameSize (number): The upstream traffic random frame size.
        - UpstreamStepIncrementFrameSize (number): The upstream traffic step increment frame size.

        Returns
        -------
        - self: This instance with matching upstreamConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of upstreamConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the upstreamConfig resources from the server available through an iterator or index

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
