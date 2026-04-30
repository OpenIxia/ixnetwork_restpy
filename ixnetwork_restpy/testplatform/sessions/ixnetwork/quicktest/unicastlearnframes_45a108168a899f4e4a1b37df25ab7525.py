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


class UnicastLearnFrames(Base):
    """It signifies the learn frames for user network interface cast.
    The UnicastLearnFrames class encapsulates a required unicastLearnFrames resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "unicastLearnFrames"
    _SDM_ATT_MAP = {
        "UnicastFastPathEnable": "unicastFastPathEnable",
        "UnicastFastPathLearnFrameSize": "unicastFastPathLearnFrameSize",
        "UnicastFastPathNumFrames": "unicastFastPathNumFrames",
        "UnicastFastPathRate": "unicastFastPathRate",
        "UnicastLearnFrameSize": "unicastLearnFrameSize",
        "UnicastLearnFrequency": "unicastLearnFrequency",
        "UnicastLearnNumFrames": "unicastLearnNumFrames",
        "UnicastLearnRate": "unicastLearnRate",
        "UnicastLearnSendMacOnly": "unicastLearnSendMacOnly",
        "UnicastLearnSendRouterSolicitation": "unicastLearnSendRouterSolicitation",
        "UnicastLearnWaitTime": "unicastLearnWaitTime",
        "UnicastLearnWaitTimeBeforeTransmit": "unicastLearnWaitTimeBeforeTransmit",
    }
    _SDM_ENUM_MAP = {
        "unicastLearnFrequency": [
            "never",
            "onBinaryIteration",
            "oncePerFramesize",
            "oncePerTest",
            "onTrial",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(UnicastLearnFrames, self).__init__(parent, list_op)

    @property
    def UnicastFastPathEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it shows the fast path for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFastPathEnable"])

    @UnicastFastPathEnable.setter
    def UnicastFastPathEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFastPathEnable"], value)

    @property
    def UnicastFastPathLearnFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the fast path learn frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFastPathLearnFrameSize"])

    @UnicastFastPathLearnFrameSize.setter
    def UnicastFastPathLearnFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFastPathLearnFrameSize"], value)

    @property
    def UnicastFastPathNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the fast path number frames for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFastPathNumFrames"])

    @UnicastFastPathNumFrames.setter
    def UnicastFastPathNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFastPathNumFrames"], value)

    @property
    def UnicastFastPathRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the fast path rate for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastFastPathRate"])

    @UnicastFastPathRate.setter
    def UnicastFastPathRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastFastPathRate"], value)

    @property
    def UnicastLearnFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the learn frame size for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastLearnFrameSize"])

    @UnicastLearnFrameSize.setter
    def UnicastLearnFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastLearnFrameSize"], value)

    @property
    def UnicastLearnFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(never | onBinaryIteration | oncePerFramesize | oncePerTest | onTrial): It signifies the learn frequency of unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastLearnFrequency"])

    @UnicastLearnFrequency.setter
    def UnicastLearnFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastLearnFrequency"], value)

    @property
    def UnicastLearnNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It helps in learning number frames for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastLearnNumFrames"])

    @UnicastLearnNumFrames.setter
    def UnicastLearnNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastLearnNumFrames"], value)

    @property
    def UnicastLearnRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the learn rate for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastLearnRate"])

    @UnicastLearnRate.setter
    def UnicastLearnRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastLearnRate"], value)

    @property
    def UnicastLearnSendMacOnly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it learns and sends the MAC address only for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastLearnSendMacOnly"])

    @UnicastLearnSendMacOnly.setter
    def UnicastLearnSendMacOnly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastLearnSendMacOnly"], value)

    @property
    def UnicastLearnSendRouterSolicitation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, It learns and sends the router solicitation for unicast.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["UnicastLearnSendRouterSolicitation"]
        )

    @UnicastLearnSendRouterSolicitation.setter
    def UnicastLearnSendRouterSolicitation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["UnicastLearnSendRouterSolicitation"], value
        )

    @property
    def UnicastLearnWaitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the learning and waiting time for unicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastLearnWaitTime"])

    @UnicastLearnWaitTime.setter
    def UnicastLearnWaitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastLearnWaitTime"], value)

    @property
    def UnicastLearnWaitTimeBeforeTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the learning and waiting time before transmission of the unicast value.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["UnicastLearnWaitTimeBeforeTransmit"]
        )

    @UnicastLearnWaitTimeBeforeTransmit.setter
    def UnicastLearnWaitTimeBeforeTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["UnicastLearnWaitTimeBeforeTransmit"], value
        )

    def update(
        self,
        UnicastFastPathEnable=None,
        UnicastFastPathLearnFrameSize=None,
        UnicastFastPathNumFrames=None,
        UnicastFastPathRate=None,
        UnicastLearnFrameSize=None,
        UnicastLearnFrequency=None,
        UnicastLearnNumFrames=None,
        UnicastLearnRate=None,
        UnicastLearnSendMacOnly=None,
        UnicastLearnSendRouterSolicitation=None,
        UnicastLearnWaitTime=None,
        UnicastLearnWaitTimeBeforeTransmit=None,
    ):
        # type: (bool, int, int, int, int, str, int, int, bool, bool, int, int) -> UnicastLearnFrames
        """Updates unicastLearnFrames resource on the server.

        Args
        ----
        - UnicastFastPathEnable (bool): If enabled, it shows the fast path for unicast.
        - UnicastFastPathLearnFrameSize (number): It signifies the fast path learn frame size for unicast.
        - UnicastFastPathNumFrames (number): It signifies the fast path number frames for unicast.
        - UnicastFastPathRate (number): It signifies the fast path rate for unicast.
        - UnicastLearnFrameSize (number): It signifies the learn frame size for unicast.
        - UnicastLearnFrequency (str(never | onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): It signifies the learn frequency of unicast.
        - UnicastLearnNumFrames (number): It helps in learning number frames for unicast.
        - UnicastLearnRate (number): It signifies the learn rate for unicast.
        - UnicastLearnSendMacOnly (bool): If enabled, it learns and sends the MAC address only for unicast.
        - UnicastLearnSendRouterSolicitation (bool): If enabled, It learns and sends the router solicitation for unicast.
        - UnicastLearnWaitTime (number): It signifies the learning and waiting time for unicast.
        - UnicastLearnWaitTimeBeforeTransmit (number): It signifies the learning and waiting time before transmission of the unicast value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        UnicastFastPathEnable=None,
        UnicastFastPathLearnFrameSize=None,
        UnicastFastPathNumFrames=None,
        UnicastFastPathRate=None,
        UnicastLearnFrameSize=None,
        UnicastLearnFrequency=None,
        UnicastLearnNumFrames=None,
        UnicastLearnRate=None,
        UnicastLearnSendMacOnly=None,
        UnicastLearnSendRouterSolicitation=None,
        UnicastLearnWaitTime=None,
        UnicastLearnWaitTimeBeforeTransmit=None,
    ):
        # type: (bool, int, int, int, int, str, int, int, bool, bool, int, int) -> UnicastLearnFrames
        """Finds and retrieves unicastLearnFrames resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve unicastLearnFrames resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all unicastLearnFrames resources from the server.

        Args
        ----
        - UnicastFastPathEnable (bool): If enabled, it shows the fast path for unicast.
        - UnicastFastPathLearnFrameSize (number): It signifies the fast path learn frame size for unicast.
        - UnicastFastPathNumFrames (number): It signifies the fast path number frames for unicast.
        - UnicastFastPathRate (number): It signifies the fast path rate for unicast.
        - UnicastLearnFrameSize (number): It signifies the learn frame size for unicast.
        - UnicastLearnFrequency (str(never | onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): It signifies the learn frequency of unicast.
        - UnicastLearnNumFrames (number): It helps in learning number frames for unicast.
        - UnicastLearnRate (number): It signifies the learn rate for unicast.
        - UnicastLearnSendMacOnly (bool): If enabled, it learns and sends the MAC address only for unicast.
        - UnicastLearnSendRouterSolicitation (bool): If enabled, It learns and sends the router solicitation for unicast.
        - UnicastLearnWaitTime (number): It signifies the learning and waiting time for unicast.
        - UnicastLearnWaitTimeBeforeTransmit (number): It signifies the learning and waiting time before transmission of the unicast value.

        Returns
        -------
        - self: This instance with matching unicastLearnFrames resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of unicastLearnFrames data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the unicastLearnFrames resources from the server available through an iterator or index

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
