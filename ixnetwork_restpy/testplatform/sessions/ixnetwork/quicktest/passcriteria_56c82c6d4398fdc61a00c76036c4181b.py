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


class PassCriteria(Base):
    """
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "passCriteria"
    _SDM_ATT_MAP = {
        "CpDpConvergenceFactorScale": "cpDpConvergenceFactorScale",
        "CpDpConvergenceTime": "cpDpConvergenceTime",
        "EnableCpDpPassFail": "enableCpDpPassFail",
        "EnablePacketLossDurationPassFail": "enablePacketLossDurationPassFail",
        "EnablePassFail": "enablePassFail",
        "PacketLossDurationConvergenceTime": "packetLossDurationConvergenceTime",
        "PacketLossDurationFactorScale": "packetLossDurationFactorScale",
        "PassFailFrequency": "passFailFrequency",
    }
    _SDM_ENUM_MAP = {
        "passFailFrequency": ["iteration"],
    }

    def __init__(self, parent, list_op=False):
        super(PassCriteria, self).__init__(parent, list_op)

    @property
    def CpDpConvergenceFactorScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpDpConvergenceFactorScale"])

    @CpDpConvergenceFactorScale.setter
    def CpDpConvergenceFactorScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpDpConvergenceFactorScale"], value)

    @property
    def CpDpConvergenceTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpDpConvergenceTime"])

    @CpDpConvergenceTime.setter
    def CpDpConvergenceTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpDpConvergenceTime"], value)

    @property
    def EnableCpDpPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCpDpPassFail"])

    @EnableCpDpPassFail.setter
    def EnableCpDpPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCpDpPassFail"], value)

    @property
    def EnablePacketLossDurationPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnablePacketLossDurationPassFail"]
        )

    @EnablePacketLossDurationPassFail.setter
    def EnablePacketLossDurationPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnablePacketLossDurationPassFail"], value
        )

    @property
    def EnablePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePassFail"])

    @EnablePassFail.setter
    def EnablePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePassFail"], value)

    @property
    def PacketLossDurationConvergenceTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["PacketLossDurationConvergenceTime"]
        )

    @PacketLossDurationConvergenceTime.setter
    def PacketLossDurationConvergenceTime(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["PacketLossDurationConvergenceTime"], value
        )

    @property
    def PacketLossDurationFactorScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketLossDurationFactorScale"])

    @PacketLossDurationFactorScale.setter
    def PacketLossDurationFactorScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketLossDurationFactorScale"], value)

    @property
    def PassFailFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(iteration):
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassFailFrequency"])

    @PassFailFrequency.setter
    def PassFailFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassFailFrequency"], value)

    def update(
        self,
        CpDpConvergenceFactorScale=None,
        CpDpConvergenceTime=None,
        EnableCpDpPassFail=None,
        EnablePacketLossDurationPassFail=None,
        EnablePassFail=None,
        PacketLossDurationConvergenceTime=None,
        PacketLossDurationFactorScale=None,
        PassFailFrequency=None,
    ):
        # type: (str, int, bool, bool, bool, int, str, str) -> PassCriteria
        """Updates passCriteria resource on the server.

        Args
        ----
        - CpDpConvergenceFactorScale (str):
        - CpDpConvergenceTime (number):
        - EnableCpDpPassFail (bool):
        - EnablePacketLossDurationPassFail (bool):
        - EnablePassFail (bool):
        - PacketLossDurationConvergenceTime (number):
        - PacketLossDurationFactorScale (str):
        - PassFailFrequency (str(iteration)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CpDpConvergenceFactorScale=None,
        CpDpConvergenceTime=None,
        EnableCpDpPassFail=None,
        EnablePacketLossDurationPassFail=None,
        EnablePassFail=None,
        PacketLossDurationConvergenceTime=None,
        PacketLossDurationFactorScale=None,
        PassFailFrequency=None,
    ):
        # type: (str, int, bool, bool, bool, int, str, str) -> PassCriteria
        """Finds and retrieves passCriteria resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve passCriteria resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all passCriteria resources from the server.

        Args
        ----
        - CpDpConvergenceFactorScale (str):
        - CpDpConvergenceTime (number):
        - EnableCpDpPassFail (bool):
        - EnablePacketLossDurationPassFail (bool):
        - EnablePassFail (bool):
        - PacketLossDurationConvergenceTime (number):
        - PacketLossDurationFactorScale (str):
        - PassFailFrequency (str(iteration)):

        Returns
        -------
        - self: This instance with matching passCriteria resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of passCriteria data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the passCriteria resources from the server available through an iterator or index

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
