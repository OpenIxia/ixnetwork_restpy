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


class MulticastLearnFrames(Base):
    """It signifies the learn frames for multicast.
    The MulticastLearnFrames class encapsulates a required multicastLearnFrames resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "multicastLearnFrames"
    _SDM_ATT_MAP = {
        "MulticastFastPathEnable": "multicastFastPathEnable",
        "MulticastFastPathLearnFrameSize": "multicastFastPathLearnFrameSize",
        "MulticastFastPathNumFrames": "multicastFastPathNumFrames",
        "MulticastFastPathRate": "multicastFastPathRate",
        "MulticastLearnFrequency": "multicastLearnFrequency",
        "MulticastLearnNumFrames": "multicastLearnNumFrames",
        "MulticastLearnSendRouterSolicitation": "multicastLearnSendRouterSolicitation",
        "MulticastLearnWaitTime": "multicastLearnWaitTime",
        "MulticastSendArp": "multicastSendArp",
    }
    _SDM_ENUM_MAP = {
        "multicastLearnFrequency": [
            "onBinaryIteration",
            "oncePerFramesize",
            "oncePerTest",
            "onTrial",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(MulticastLearnFrames, self).__init__(parent, list_op)

    @property
    def MulticastFastPathEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFastPathEnable"])

    @MulticastFastPathEnable.setter
    def MulticastFastPathEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFastPathEnable"], value)

    @property
    def MulticastFastPathLearnFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFastPathLearnFrameSize"])

    @MulticastFastPathLearnFrameSize.setter
    def MulticastFastPathLearnFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFastPathLearnFrameSize"], value)

    @property
    def MulticastFastPathNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFastPathNumFrames"])

    @MulticastFastPathNumFrames.setter
    def MulticastFastPathNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFastPathNumFrames"], value)

    @property
    def MulticastFastPathRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFastPathRate"])

    @MulticastFastPathRate.setter
    def MulticastFastPathRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFastPathRate"], value)

    @property
    def MulticastLearnFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(onBinaryIteration | oncePerFramesize | oncePerTest | onTrial): It signifies the learn frequency of multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastLearnFrequency"])

    @MulticastLearnFrequency.setter
    def MulticastLearnFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastLearnFrequency"], value)

    @property
    def MulticastLearnNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the number of learn frames for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastLearnNumFrames"])

    @MulticastLearnNumFrames.setter
    def MulticastLearnNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastLearnNumFrames"], value)

    @property
    def MulticastLearnSendRouterSolicitation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the learnt and sent router solicitation for multicast.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["MulticastLearnSendRouterSolicitation"]
        )

    @MulticastLearnSendRouterSolicitation.setter
    def MulticastLearnSendRouterSolicitation(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["MulticastLearnSendRouterSolicitation"], value
        )

    @property
    def MulticastLearnWaitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the learn and wait time for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastLearnWaitTime"])

    @MulticastLearnWaitTime.setter
    def MulticastLearnWaitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastLearnWaitTime"], value)

    @property
    def MulticastSendArp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It signifies the address resolution protocol sent as multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastSendArp"])

    @MulticastSendArp.setter
    def MulticastSendArp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastSendArp"], value)

    def update(
        self,
        MulticastFastPathEnable=None,
        MulticastFastPathLearnFrameSize=None,
        MulticastFastPathNumFrames=None,
        MulticastFastPathRate=None,
        MulticastLearnFrequency=None,
        MulticastLearnNumFrames=None,
        MulticastLearnSendRouterSolicitation=None,
        MulticastLearnWaitTime=None,
        MulticastSendArp=None,
    ):
        # type: (bool, int, int, int, str, int, str, int, bool) -> MulticastLearnFrames
        """Updates multicastLearnFrames resource on the server.

        Args
        ----
        - MulticastFastPathEnable (bool): NOT DEFINED
        - MulticastFastPathLearnFrameSize (number): NOT DEFINED
        - MulticastFastPathNumFrames (number): NOT DEFINED
        - MulticastFastPathRate (number): NOT DEFINED
        - MulticastLearnFrequency (str(onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): It signifies the learn frequency of multicast.
        - MulticastLearnNumFrames (number): It signifies the number of learn frames for multicast.
        - MulticastLearnSendRouterSolicitation (str): It signifies the learnt and sent router solicitation for multicast.
        - MulticastLearnWaitTime (number): It signifies the learn and wait time for multicast.
        - MulticastSendArp (bool): It signifies the address resolution protocol sent as multicast.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        MulticastFastPathEnable=None,
        MulticastFastPathLearnFrameSize=None,
        MulticastFastPathNumFrames=None,
        MulticastFastPathRate=None,
        MulticastLearnFrequency=None,
        MulticastLearnNumFrames=None,
        MulticastLearnSendRouterSolicitation=None,
        MulticastLearnWaitTime=None,
        MulticastSendArp=None,
    ):
        # type: (bool, int, int, int, str, int, str, int, bool) -> MulticastLearnFrames
        """Finds and retrieves multicastLearnFrames resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastLearnFrames resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastLearnFrames resources from the server.

        Args
        ----
        - MulticastFastPathEnable (bool): NOT DEFINED
        - MulticastFastPathLearnFrameSize (number): NOT DEFINED
        - MulticastFastPathNumFrames (number): NOT DEFINED
        - MulticastFastPathRate (number): NOT DEFINED
        - MulticastLearnFrequency (str(onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): It signifies the learn frequency of multicast.
        - MulticastLearnNumFrames (number): It signifies the number of learn frames for multicast.
        - MulticastLearnSendRouterSolicitation (str): It signifies the learnt and sent router solicitation for multicast.
        - MulticastLearnWaitTime (number): It signifies the learn and wait time for multicast.
        - MulticastSendArp (bool): It signifies the address resolution protocol sent as multicast.

        Returns
        -------
        - self: This instance with matching multicastLearnFrames resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastLearnFrames data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastLearnFrames resources from the server available through an iterator or index

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
