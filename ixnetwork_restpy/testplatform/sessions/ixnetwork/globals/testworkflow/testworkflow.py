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


class Testworkflow(Base):
    """
    The Testworkflow class encapsulates a required testworkflow resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testworkflow"
    _SDM_ATT_MAP = {
        "CurrentDescription": "currentDescription",
        "CurrentState": "currentState",
        "IsCaptureRunning": "isCaptureRunning",
    }
    _SDM_ENUM_MAP = {
        "currentState": [
            "kApplyTraffic",
            "kConnectPorts",
            "kError",
            "kGenerateTraffic",
            "kIdle",
            "kReleaseCrashedPorts",
            "kStartLAG",
            "kStartProtocols",
            "kStartTopology",
            "kStartTraffic",
            "kStopLAG",
            "kStopProtocols",
            "kStopTraffic",
            "kWaitForChassisUp",
            "kWaitForLicenseBroadcast",
            "kWaitForPortsUp",
            "kWaitForProtocolsUp",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Testworkflow, self).__init__(parent, list_op)

    @property
    def CurrentDescription(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentDescription"])

    @property
    def CurrentState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kApplyTraffic | kConnectPorts | kError | kGenerateTraffic | kIdle | kReleaseCrashedPorts | kStartLAG | kStartProtocols | kStartTopology | kStartTraffic | kStopLAG | kStopProtocols | kStopTraffic | kWaitForChassisUp | kWaitForLicenseBroadcast | kWaitForPortsUp | kWaitForProtocolsUp):
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentState"])

    @property
    def IsCaptureRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether capture is running on any port in config.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsCaptureRunning"])

    def find(self, CurrentDescription=None, CurrentState=None, IsCaptureRunning=None):
        # type: (str, str, bool) -> Testworkflow
        """Finds and retrieves testworkflow resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testworkflow resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testworkflow resources from the server.

        Args
        ----
        - CurrentDescription (str):
        - CurrentState (str(kApplyTraffic | kConnectPorts | kError | kGenerateTraffic | kIdle | kReleaseCrashedPorts | kStartLAG | kStartProtocols | kStartTopology | kStartTraffic | kStopLAG | kStopProtocols | kStopTraffic | kWaitForChassisUp | kWaitForLicenseBroadcast | kWaitForPortsUp | kWaitForProtocolsUp)):
        - IsCaptureRunning (bool): Indicates whether capture is running on any port in config.

        Returns
        -------
        - self: This instance with matching testworkflow resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testworkflow data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testworkflow resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        connect ports, start protocols and generate/apply/start traffic

        start(Arg2=bool, async_operation=bool)
        --------------------------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully
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

    def StartAllProtocolsGlobally(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startAllProtocolsGlobally operation on the server.

        connect ports and start specific protocol globally

        startAllProtocolsGlobally(Arg2=string, async_operation=bool)
        ------------------------------------------------------------
        - Arg2 (str): argument should be action id which return from the API getAllProtocolsAvailableforGlobalStartStop. like start_ethernet_id, start_ipv4_id or start_ospfv2_id
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
            "startAllProtocolsGlobally", payload=payload, response_object=None
        )

    def Startlag(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startlag operation on the server.

        connect ports and start LAG

        startlag(Arg2=bool, async_operation=bool)
        -----------------------------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully
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
        return self._execute("startlag", payload=payload, response_object=None)

    def Startprotocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startprotocols operation on the server.

        connect ports and start protocols

        startprotocols(Arg2=bool, async_operation=bool)
        -----------------------------------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully
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
        return self._execute("startprotocols", payload=payload, response_object=None)

    def Startselected(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startselected operation on the server.

        connect ports and start the selected item

        startselected(Arg2=href, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/topology | /api/v1/sessions/1/ixnetwork/topology/.../deviceGroup | /api/v1/sessions/1/ixnetwork/topology/deviceGroup)): objref to /topology or device group
        - Arg3 (bool): a boolean indicating if ownership should be taken forcefully
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
        return self._execute("startselected", payload=payload, response_object=None)

    def Starttraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the starttraffic operation on the server.

        generates (if required), applies and starts traffic

        starttraffic(async_operation=bool)
        ----------------------------------
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
        return self._execute("starttraffic", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        stop protocols and traffic

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

    def Stoplag(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stoplag operation on the server.

        stop LAG

        stoplag(async_operation=bool)
        -----------------------------
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
        return self._execute("stoplag", payload=payload, response_object=None)

    def Stopprotocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopprotocols operation on the server.

        stop protocols

        stopprotocols(async_operation=bool)
        -----------------------------------
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
        return self._execute("stopprotocols", payload=payload, response_object=None)

    def Stoptraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stoptraffic operation on the server.

        stop protocols and traffic

        stoptraffic(async_operation=bool)
        ---------------------------------
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
        return self._execute("stoptraffic", payload=payload, response_object=None)
