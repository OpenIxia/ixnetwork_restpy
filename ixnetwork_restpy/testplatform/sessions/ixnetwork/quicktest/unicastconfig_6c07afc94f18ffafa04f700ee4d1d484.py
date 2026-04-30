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


class UnicastConfig(Base):
    """It signifies the configuration of unicast.
    The UnicastConfig class encapsulates a required unicastConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "unicastConfig"
    _SDM_ATT_MAP = {
        "UnicastCountRandomFrameSize": "unicastCountRandomFrameSize",
        "UnicastEnableMinFrameSize": "unicastEnableMinFrameSize",
        "UnicastForceRegenerate": "unicastForceRegenerate",
        "UnicastFrameSizeMode": "unicastFrameSizeMode",
        "UnicastFramesizeFixedValue": "unicastFramesizeFixedValue",
        "UnicastFramesizeList": "unicastFramesizeList",
        "UnicastMaxIncrementFrameSize": "unicastMaxIncrementFrameSize",
        "UnicastMaxRandomFrameSize": "unicastMaxRandomFrameSize",
        "UnicastMinIncrementFrameSize": "unicastMinIncrementFrameSize",
        "UnicastMinRandomFrameSize": "unicastMinRandomFrameSize",
        "UnicastStepIncrementFrameSize": "unicastStepIncrementFrameSize",
    }
    _SDM_ENUM_MAP = {
        "unicastFrameSizeMode": ["custom", "fixed", "increment", "random"],
    }

    def __init__(self, parent, list_op=False):
        super(UnicastConfig, self).__init__(parent, list_op)

    @property
    def UnicastCountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the count random frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastCountRandomFrameSize"])

    @UnicastCountRandomFrameSize.setter
    def UnicastCountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastCountRandomFrameSize"], value)

    @property
    def UnicastEnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it shows the minimum frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastEnableMinFrameSize"])

    @UnicastEnableMinFrameSize.setter
    def UnicastEnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastEnableMinFrameSize"], value)

    @property
    def UnicastForceRegenerate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the mode for unicast frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastForceRegenerate"])

    @UnicastForceRegenerate.setter
    def UnicastForceRegenerate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastForceRegenerate"], value)

    @property
    def UnicastFrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random): It signifies the mode for unicast frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFrameSizeMode"])

    @UnicastFrameSizeMode.setter
    def UnicastFrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFrameSizeMode"], value)

    @property
    def UnicastFramesizeFixedValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the fixed value for unicast frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFramesizeFixedValue"])

    @UnicastFramesizeFixedValue.setter
    def UnicastFramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFramesizeFixedValue"], value)

    @property
    def UnicastFramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): It lists the frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFramesizeList"])

    @UnicastFramesizeList.setter
    def UnicastFramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFramesizeList"], value)

    @property
    def UnicastMaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the maximum increment frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMaxIncrementFrameSize"])

    @UnicastMaxIncrementFrameSize.setter
    def UnicastMaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMaxIncrementFrameSize"], value)

    @property
    def UnicastMaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the maximum random frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMaxRandomFrameSize"])

    @UnicastMaxRandomFrameSize.setter
    def UnicastMaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMaxRandomFrameSize"], value)

    @property
    def UnicastMinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the minimum increment frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMinIncrementFrameSize"])

    @UnicastMinIncrementFrameSize.setter
    def UnicastMinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMinIncrementFrameSize"], value)

    @property
    def UnicastMinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the minimum random frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMinRandomFrameSize"])

    @UnicastMinRandomFrameSize.setter
    def UnicastMinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMinRandomFrameSize"], value)

    @property
    def UnicastStepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the step increment frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastStepIncrementFrameSize"])

    @UnicastStepIncrementFrameSize.setter
    def UnicastStepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastStepIncrementFrameSize"], value)

    def update(
        self,
        UnicastCountRandomFrameSize=None,
        UnicastEnableMinFrameSize=None,
        UnicastForceRegenerate=None,
        UnicastFrameSizeMode=None,
        UnicastFramesizeFixedValue=None,
        UnicastFramesizeList=None,
        UnicastMaxIncrementFrameSize=None,
        UnicastMaxRandomFrameSize=None,
        UnicastMinIncrementFrameSize=None,
        UnicastMinRandomFrameSize=None,
        UnicastStepIncrementFrameSize=None,
    ):
        # type: (int, bool, str, str, int, List[str], int, int, int, int, int) -> UnicastConfig
        """Updates unicastConfig resource on the server.

        Args
        ----
        - UnicastCountRandomFrameSize (number): It signifies the count random frame size for unicast.
        - UnicastEnableMinFrameSize (bool): If enabled, it shows the minimum frame size for unicast.
        - UnicastForceRegenerate (str): It signifies the mode for unicast frame size.
        - UnicastFrameSizeMode (str(custom | fixed | increment | random)): It signifies the mode for unicast frame size.
        - UnicastFramesizeFixedValue (number): It signifies the fixed value for unicast frame size.
        - UnicastFramesizeList (list(str)): It lists the frame size for unicast.
        - UnicastMaxIncrementFrameSize (number): It signifies the maximum increment frame size for unicast.
        - UnicastMaxRandomFrameSize (number): It signifies the maximum random frame size for unicast.
        - UnicastMinIncrementFrameSize (number): It signifies the minimum increment frame size for unicast.
        - UnicastMinRandomFrameSize (number): It signifies the minimum random frame size for unicast.
        - UnicastStepIncrementFrameSize (number): It signifies the step increment frame size for unicast.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        UnicastCountRandomFrameSize=None,
        UnicastEnableMinFrameSize=None,
        UnicastForceRegenerate=None,
        UnicastFrameSizeMode=None,
        UnicastFramesizeFixedValue=None,
        UnicastFramesizeList=None,
        UnicastMaxIncrementFrameSize=None,
        UnicastMaxRandomFrameSize=None,
        UnicastMinIncrementFrameSize=None,
        UnicastMinRandomFrameSize=None,
        UnicastStepIncrementFrameSize=None,
    ):
        # type: (int, bool, str, str, int, List[str], int, int, int, int, int) -> UnicastConfig
        """Finds and retrieves unicastConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve unicastConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all unicastConfig resources from the server.

        Args
        ----
        - UnicastCountRandomFrameSize (number): It signifies the count random frame size for unicast.
        - UnicastEnableMinFrameSize (bool): If enabled, it shows the minimum frame size for unicast.
        - UnicastForceRegenerate (str): It signifies the mode for unicast frame size.
        - UnicastFrameSizeMode (str(custom | fixed | increment | random)): It signifies the mode for unicast frame size.
        - UnicastFramesizeFixedValue (number): It signifies the fixed value for unicast frame size.
        - UnicastFramesizeList (list(str)): It lists the frame size for unicast.
        - UnicastMaxIncrementFrameSize (number): It signifies the maximum increment frame size for unicast.
        - UnicastMaxRandomFrameSize (number): It signifies the maximum random frame size for unicast.
        - UnicastMinIncrementFrameSize (number): It signifies the minimum increment frame size for unicast.
        - UnicastMinRandomFrameSize (number): It signifies the minimum random frame size for unicast.
        - UnicastStepIncrementFrameSize (number): It signifies the step increment frame size for unicast.

        Returns
        -------
        - self: This instance with matching unicastConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of unicastConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the unicastConfig resources from the server available through an iterator or index

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
