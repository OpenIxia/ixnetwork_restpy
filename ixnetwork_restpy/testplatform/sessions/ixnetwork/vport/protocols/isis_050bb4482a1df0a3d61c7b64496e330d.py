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


class Isis(Base):
    """This object simulates one or more IS-IS routers in a network of routers.
    The Isis class encapsulates a required isis resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "isis"
    _SDM_ATT_MAP = {
        "AllL1RbridgesMac": "allL1RbridgesMac",
        "EmulationType": "emulationType",
        "Enabled": "enabled",
        "HelloMulticastMac": "helloMulticastMac",
        "LspMgroupPdusPerInterval": "lspMgroupPdusPerInterval",
        "NlpId": "nlpId",
        "RateControlInterval": "rateControlInterval",
        "RunningState": "runningState",
        "SendP2PHellosToUnicastMac": "sendP2PHellosToUnicastMac",
        "SpbAllL1BridgesMac": "spbAllL1BridgesMac",
        "SpbHelloMulticastMac": "spbHelloMulticastMac",
        "SpbNlpId": "spbNlpId",
    }
    _SDM_ENUM_MAP = {
        "emulationType": ["isisL3Routing", "dceIsis", "spbIsis", "trillIsis"],
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Isis, self).__init__(parent, list_op)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_320e1c5c099823f4ba100b7eaf8bb8d9.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_320e1c5c099823f4ba100b7eaf8bb8d9 import (
            Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Router", None) is not None:
                return self._properties.get("Router")
        return Router(self)

    @property
    def AllL1RbridgesMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: ISIS All L1 RBridge MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP["AllL1RbridgesMac"])

    @AllL1RbridgesMac.setter
    def AllL1RbridgesMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AllL1RbridgesMac"], value)

    @property
    def EmulationType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(isisL3Routing | dceIsis | spbIsis | trillIsis): Sets the router emulation type of ISIS component of the protocol server for a particular port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EmulationType"])

    @EmulationType.setter
    def EmulationType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EmulationType"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated IS-IS router in the emulated IS-IS network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def HelloMulticastMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: ISIS Hello Multicast MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP["HelloMulticastMac"])

    @HelloMulticastMac.setter
    def HelloMulticastMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["HelloMulticastMac"], value)

    @property
    def LspMgroupPdusPerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the number of LSP MGROUP-PDUs to be sent for each interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspMgroupPdusPerInterval"])

    @LspMgroupPdusPerInterval.setter
    def LspMgroupPdusPerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspMgroupPdusPerInterval"], value)

    @property
    def NlpId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: ISIS NLP ID
        """
        return self._get_attribute(self._SDM_ATT_MAP["NlpId"])

    @NlpId.setter
    def NlpId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NlpId"], value)

    @property
    def RateControlInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the wait time for transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RateControlInterval"])

    @RateControlInterval.setter
    def RateControlInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RateControlInterval"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the ISIS server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    @property
    def SendP2PHellosToUnicastMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, sends point to point hello messages to unicast mac addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendP2PHellosToUnicastMac"])

    @SendP2PHellosToUnicastMac.setter
    def SendP2PHellosToUnicastMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendP2PHellosToUnicastMac"], value)

    @property
    def SpbAllL1BridgesMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Contains all SPB ISIS specific attributes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpbAllL1BridgesMac"])

    @SpbAllL1BridgesMac.setter
    def SpbAllL1BridgesMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpbAllL1BridgesMac"], value)

    @property
    def SpbHelloMulticastMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Contains all hello messages to multicast mac addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpbHelloMulticastMac"])

    @SpbHelloMulticastMac.setter
    def SpbHelloMulticastMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpbHelloMulticastMac"], value)

    @property
    def SpbNlpId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SPB NLP ID
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpbNlpId"])

    @SpbNlpId.setter
    def SpbNlpId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpbNlpId"], value)

    def update(
        self,
        AllL1RbridgesMac=None,
        EmulationType=None,
        Enabled=None,
        HelloMulticastMac=None,
        LspMgroupPdusPerInterval=None,
        NlpId=None,
        RateControlInterval=None,
        SendP2PHellosToUnicastMac=None,
        SpbAllL1BridgesMac=None,
        SpbHelloMulticastMac=None,
        SpbNlpId=None,
    ):
        # type: (str, str, bool, str, int, int, int, bool, str, str, int) -> Isis
        """Updates isis resource on the server.

        Args
        ----
        - AllL1RbridgesMac (str): ISIS All L1 RBridge MAC
        - EmulationType (str(isisL3Routing | dceIsis | spbIsis | trillIsis)): Sets the router emulation type of ISIS component of the protocol server for a particular port.
        - Enabled (bool): Enables or disables the use of this emulated IS-IS router in the emulated IS-IS network. (default = disabled)
        - HelloMulticastMac (str): ISIS Hello Multicast MAC
        - LspMgroupPdusPerInterval (number): Indicates the number of LSP MGROUP-PDUs to be sent for each interval.
        - NlpId (number): ISIS NLP ID
        - RateControlInterval (number): Indicates the wait time for transmission.
        - SendP2PHellosToUnicastMac (bool): If enabled, sends point to point hello messages to unicast mac addresses.
        - SpbAllL1BridgesMac (str): Contains all SPB ISIS specific attributes.
        - SpbHelloMulticastMac (str): Contains all hello messages to multicast mac addresses.
        - SpbNlpId (number): SPB NLP ID

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AllL1RbridgesMac=None,
        EmulationType=None,
        Enabled=None,
        HelloMulticastMac=None,
        LspMgroupPdusPerInterval=None,
        NlpId=None,
        RateControlInterval=None,
        RunningState=None,
        SendP2PHellosToUnicastMac=None,
        SpbAllL1BridgesMac=None,
        SpbHelloMulticastMac=None,
        SpbNlpId=None,
    ):
        # type: (str, str, bool, str, int, int, int, str, bool, str, str, int) -> Isis
        """Finds and retrieves isis resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isis resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isis resources from the server.

        Args
        ----
        - AllL1RbridgesMac (str): ISIS All L1 RBridge MAC
        - EmulationType (str(isisL3Routing | dceIsis | spbIsis | trillIsis)): Sets the router emulation type of ISIS component of the protocol server for a particular port.
        - Enabled (bool): Enables or disables the use of this emulated IS-IS router in the emulated IS-IS network. (default = disabled)
        - HelloMulticastMac (str): ISIS Hello Multicast MAC
        - LspMgroupPdusPerInterval (number): Indicates the number of LSP MGROUP-PDUs to be sent for each interval.
        - NlpId (number): ISIS NLP ID
        - RateControlInterval (number): Indicates the wait time for transmission.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of the ISIS server.
        - SendP2PHellosToUnicastMac (bool): If enabled, sends point to point hello messages to unicast mac addresses.
        - SpbAllL1BridgesMac (str): Contains all SPB ISIS specific attributes.
        - SpbHelloMulticastMac (str): Contains all hello messages to multicast mac addresses.
        - SpbNlpId (number): SPB NLP ID

        Returns
        -------
        - self: This instance with matching isis resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isis data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isis resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the ISIS protocol on a port or group of ports simultaneously.

        start(async_operation=bool)
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the ISIS protocol on a port or group of ports simultaneously.

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
