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


class LearnFrames(Base):
    """The learn frames.
    The LearnFrames class encapsulates a required learnFrames resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnFrames"
    _SDM_ATT_MAP = {
        "FastPathEnable": "fastPathEnable",
        "FastPathLearnFrameSize": "fastPathLearnFrameSize",
        "FastPathNumFrames": "fastPathNumFrames",
        "FastPathRate": "fastPathRate",
        "LearnFrequency": "learnFrequency",
        "LearnNumFrames": "learnNumFrames",
        "LearnRate": "learnRate",
        "LearnSendMacOnly": "learnSendMacOnly",
        "LearnSendRouterSolicitation": "learnSendRouterSolicitation",
        "LearnWaitTime": "learnWaitTime",
        "SendArp": "sendArp",
    }
    _SDM_ENUM_MAP = {
        "learnFrequency": [
            "onBinaryIteration",
            "oncePerFramesize",
            "oncePerTest",
            "onTrial",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(LearnFrames, self).__init__(parent, list_op)

    @property
    def FastPathEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the fast path is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastPathEnable"])

    @FastPathEnable.setter
    def FastPathEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastPathEnable"], value)

    @property
    def FastPathLearnFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The path in which the learnt frame sizes are saved.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastPathLearnFrameSize"])

    @FastPathLearnFrameSize.setter
    def FastPathLearnFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastPathLearnFrameSize"], value)

    @property
    def FastPathNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The learnt information on the number of frames to be tramsferred.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastPathNumFrames"])

    @FastPathNumFrames.setter
    def FastPathNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastPathNumFrames"], value)

    @property
    def FastPathRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The learnt inofrmation on the rate the data is to be transferred.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastPathRate"])

    @FastPathRate.setter
    def FastPathRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastPathRate"], value)

    @property
    def LearnFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(onBinaryIteration | oncePerFramesize | oncePerTest | onTrial): The learn frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnFrequency"])

    @LearnFrequency.setter
    def LearnFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnFrequency"], value)

    @property
    def LearnNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The learned numbered of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnNumFrames"])

    @LearnNumFrames.setter
    def LearnNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnNumFrames"], value)

    @property
    def LearnRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The learn rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnRate"])

    @LearnRate.setter
    def LearnRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnRate"], value)

    @property
    def LearnSendMacOnly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, sends the learned MAC only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnSendMacOnly"])

    @LearnSendMacOnly.setter
    def LearnSendMacOnly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnSendMacOnly"], value)

    @property
    def LearnSendRouterSolicitation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The learn send router solicitation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnSendRouterSolicitation"])

    @LearnSendRouterSolicitation.setter
    def LearnSendRouterSolicitation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnSendRouterSolicitation"], value)

    @property
    def LearnWaitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The learn wait time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnWaitTime"])

    @LearnWaitTime.setter
    def LearnWaitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnWaitTime"], value)

    @property
    def SendArp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The send Arp.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendArp"])

    @SendArp.setter
    def SendArp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendArp"], value)

    def update(
        self,
        FastPathEnable=None,
        FastPathLearnFrameSize=None,
        FastPathNumFrames=None,
        FastPathRate=None,
        LearnFrequency=None,
        LearnNumFrames=None,
        LearnRate=None,
        LearnSendMacOnly=None,
        LearnSendRouterSolicitation=None,
        LearnWaitTime=None,
        SendArp=None,
    ):
        # type: (bool, int, int, int, str, int, int, bool, bool, int, bool) -> LearnFrames
        """Updates learnFrames resource on the server.

        Args
        ----
        - FastPathEnable (bool): If true, the fast path is enabled.
        - FastPathLearnFrameSize (number): The path in which the learnt frame sizes are saved.
        - FastPathNumFrames (number): The learnt information on the number of frames to be tramsferred.
        - FastPathRate (number): The learnt inofrmation on the rate the data is to be transferred.
        - LearnFrequency (str(onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): The learn frequency.
        - LearnNumFrames (number): The learned numbered of frames.
        - LearnRate (number): The learn rate.
        - LearnSendMacOnly (bool): If true, sends the learned MAC only.
        - LearnSendRouterSolicitation (bool): The learn send router solicitation.
        - LearnWaitTime (number): The learn wait time.
        - SendArp (bool): The send Arp.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        FastPathEnable=None,
        FastPathLearnFrameSize=None,
        FastPathNumFrames=None,
        FastPathRate=None,
        LearnFrequency=None,
        LearnNumFrames=None,
        LearnRate=None,
        LearnSendMacOnly=None,
        LearnSendRouterSolicitation=None,
        LearnWaitTime=None,
        SendArp=None,
    ):
        # type: (bool, int, int, int, str, int, int, bool, bool, int, bool) -> LearnFrames
        """Finds and retrieves learnFrames resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnFrames resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnFrames resources from the server.

        Args
        ----
        - FastPathEnable (bool): If true, the fast path is enabled.
        - FastPathLearnFrameSize (number): The path in which the learnt frame sizes are saved.
        - FastPathNumFrames (number): The learnt information on the number of frames to be tramsferred.
        - FastPathRate (number): The learnt inofrmation on the rate the data is to be transferred.
        - LearnFrequency (str(onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): The learn frequency.
        - LearnNumFrames (number): The learned numbered of frames.
        - LearnRate (number): The learn rate.
        - LearnSendMacOnly (bool): If true, sends the learned MAC only.
        - LearnSendRouterSolicitation (bool): The learn send router solicitation.
        - LearnWaitTime (number): The learn wait time.
        - SendArp (bool): The send Arp.

        Returns
        -------
        - self: This instance with matching learnFrames resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnFrames data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnFrames resources from the server available through an iterator or index

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
