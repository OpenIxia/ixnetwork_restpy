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


class DownstreamConfig(Base):
    """The downstream traffic configuration parameters.
    The DownstreamConfig class encapsulates a required downstreamConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "downstreamConfig"
    _SDM_ATT_MAP = {
        "DownstreamCountRandomFrameSize": "downstreamCountRandomFrameSize",
        "DownstreamEnableMinFrameSize": "downstreamEnableMinFrameSize",
        "DownstreamFrameSizeMode": "downstreamFrameSizeMode",
        "DownstreamFramesizeFixedValue": "downstreamFramesizeFixedValue",
        "DownstreamFramesizeList": "downstreamFramesizeList",
        "DownstreamMaxIncrementFrameSize": "downstreamMaxIncrementFrameSize",
        "DownstreamMaxRandomFrameSize": "downstreamMaxRandomFrameSize",
        "DownstreamMinIncrementFrameSize": "downstreamMinIncrementFrameSize",
        "DownstreamMinRandomFrameSize": "downstreamMinRandomFrameSize",
        "DownstreamStepIncrementFrameSize": "downstreamStepIncrementFrameSize",
        "UseUpstreamFrameSize": "useUpstreamFrameSize",
    }
    _SDM_ENUM_MAP = {
        "downstreamFrameSizeMode": ["custom", "increment", "random", "unchanged"],
    }

    def __init__(self, parent, list_op=False):
        super(DownstreamConfig, self).__init__(parent, list_op)

    @property
    def DownstreamCountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The downstream traffic count for random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamCountRandomFrameSize"])

    @DownstreamCountRandomFrameSize.setter
    def DownstreamCountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamCountRandomFrameSize"], value)

    @property
    def DownstreamEnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables minimum frame size of downstream traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamEnableMinFrameSize"])

    @DownstreamEnableMinFrameSize.setter
    def DownstreamEnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamEnableMinFrameSize"], value)

    @property
    def DownstreamFrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | increment | random | unchanged): The downstream frame size mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamFrameSizeMode"])

    @DownstreamFrameSizeMode.setter
    def DownstreamFrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamFrameSizeMode"], value)

    @property
    def DownstreamFramesizeFixedValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The fixed value of framesize of downstream traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamFramesizeFixedValue"])

    @DownstreamFramesizeFixedValue.setter
    def DownstreamFramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamFramesizeFixedValue"], value)

    @property
    def DownstreamFramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The downstream frame size list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamFramesizeList"])

    @DownstreamFramesizeList.setter
    def DownstreamFramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamFramesizeList"], value)

    @property
    def DownstreamMaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The downstream traffic maximum increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMaxIncrementFrameSize"])

    @DownstreamMaxIncrementFrameSize.setter
    def DownstreamMaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMaxIncrementFrameSize"], value)

    @property
    def DownstreamMaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The downstream maximum random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMaxRandomFrameSize"])

    @DownstreamMaxRandomFrameSize.setter
    def DownstreamMaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMaxRandomFrameSize"], value)

    @property
    def DownstreamMinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The downstream minimum increment frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMinIncrementFrameSize"])

    @DownstreamMinIncrementFrameSize.setter
    def DownstreamMinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMinIncrementFrameSize"], value)

    @property
    def DownstreamMinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The downstream traffic random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMinRandomFrameSize"])

    @DownstreamMinRandomFrameSize.setter
    def DownstreamMinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMinRandomFrameSize"], value)

    @property
    def DownstreamStepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The downstream traffic step increment frame size.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DownstreamStepIncrementFrameSize"]
        )

    @DownstreamStepIncrementFrameSize.setter
    def DownstreamStepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DownstreamStepIncrementFrameSize"], value
        )

    @property
    def UseUpstreamFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Allows to use upstream traffic frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseUpstreamFrameSize"])

    @UseUpstreamFrameSize.setter
    def UseUpstreamFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseUpstreamFrameSize"], value)

    def update(
        self,
        DownstreamCountRandomFrameSize=None,
        DownstreamEnableMinFrameSize=None,
        DownstreamFrameSizeMode=None,
        DownstreamFramesizeFixedValue=None,
        DownstreamFramesizeList=None,
        DownstreamMaxIncrementFrameSize=None,
        DownstreamMaxRandomFrameSize=None,
        DownstreamMinIncrementFrameSize=None,
        DownstreamMinRandomFrameSize=None,
        DownstreamStepIncrementFrameSize=None,
        UseUpstreamFrameSize=None,
    ):
        # type: (int, bool, str, int, List[str], int, int, int, int, int, bool) -> DownstreamConfig
        """Updates downstreamConfig resource on the server.

        Args
        ----
        - DownstreamCountRandomFrameSize (number): The downstream traffic count for random frame size.
        - DownstreamEnableMinFrameSize (bool): Enables minimum frame size of downstream traffic.
        - DownstreamFrameSizeMode (str(custom | increment | random | unchanged)): The downstream frame size mode.
        - DownstreamFramesizeFixedValue (number): The fixed value of framesize of downstream traffic.
        - DownstreamFramesizeList (list(str)): The downstream frame size list.
        - DownstreamMaxIncrementFrameSize (number): The downstream traffic maximum increment frame size.
        - DownstreamMaxRandomFrameSize (number): The downstream maximum random frame size.
        - DownstreamMinIncrementFrameSize (number): The downstream minimum increment frame size.
        - DownstreamMinRandomFrameSize (number): The downstream traffic random frame size.
        - DownstreamStepIncrementFrameSize (number): The downstream traffic step increment frame size.
        - UseUpstreamFrameSize (bool): Allows to use upstream traffic frame size.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DownstreamCountRandomFrameSize=None,
        DownstreamEnableMinFrameSize=None,
        DownstreamFrameSizeMode=None,
        DownstreamFramesizeFixedValue=None,
        DownstreamFramesizeList=None,
        DownstreamMaxIncrementFrameSize=None,
        DownstreamMaxRandomFrameSize=None,
        DownstreamMinIncrementFrameSize=None,
        DownstreamMinRandomFrameSize=None,
        DownstreamStepIncrementFrameSize=None,
        UseUpstreamFrameSize=None,
    ):
        # type: (int, bool, str, int, List[str], int, int, int, int, int, bool) -> DownstreamConfig
        """Finds and retrieves downstreamConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve downstreamConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all downstreamConfig resources from the server.

        Args
        ----
        - DownstreamCountRandomFrameSize (number): The downstream traffic count for random frame size.
        - DownstreamEnableMinFrameSize (bool): Enables minimum frame size of downstream traffic.
        - DownstreamFrameSizeMode (str(custom | increment | random | unchanged)): The downstream frame size mode.
        - DownstreamFramesizeFixedValue (number): The fixed value of framesize of downstream traffic.
        - DownstreamFramesizeList (list(str)): The downstream frame size list.
        - DownstreamMaxIncrementFrameSize (number): The downstream traffic maximum increment frame size.
        - DownstreamMaxRandomFrameSize (number): The downstream maximum random frame size.
        - DownstreamMinIncrementFrameSize (number): The downstream minimum increment frame size.
        - DownstreamMinRandomFrameSize (number): The downstream traffic random frame size.
        - DownstreamStepIncrementFrameSize (number): The downstream traffic step increment frame size.
        - UseUpstreamFrameSize (bool): Allows to use upstream traffic frame size.

        Returns
        -------
        - self: This instance with matching downstreamConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of downstreamConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the downstreamConfig resources from the server available through an iterator or index

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
