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


class OspfV3(Base):
    """This object simulates one or more OSPFv3 routers in a network of routers.
    The OspfV3 class encapsulates a required ospfV3 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ospfV3"
    _SDM_ATT_MAP = {
        "EnableDrOrBdr": "enableDrOrBdr",
        "Enabled": "enabled",
        "RunningState": "runningState",
    }
    _SDM_ENUM_MAP = {
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(OspfV3, self).__init__(parent, list_op)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_47de08a5e549c3a3ba83f5006b81e108.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_47de08a5e549c3a3ba83f5006b81e108 import (
            Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Router", None) is not None:
                return self._properties.get("Router")
        return Router(self)

    @property
    def EnableDrOrBdr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the OSPF Router to participate in DR/BDR election process
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDrOrBdr"])

    @EnableDrOrBdr.setter
    def EnableDrOrBdr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDrOrBdr"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables this emulated OSPFv3 router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current state of the OSPFv6 router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    def update(self, EnableDrOrBdr=None, Enabled=None):
        # type: (bool, bool) -> OspfV3
        """Updates ospfV3 resource on the server.

        Args
        ----
        - EnableDrOrBdr (bool): Enables the OSPF Router to participate in DR/BDR election process
        - Enabled (bool): Enables this emulated OSPFv3 router.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, EnableDrOrBdr=None, Enabled=None, RunningState=None):
        # type: (bool, bool, str) -> OspfV3
        """Finds and retrieves ospfV3 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfV3 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfV3 resources from the server.

        Args
        ----
        - EnableDrOrBdr (bool): Enables the OSPF Router to participate in DR/BDR election process
        - Enabled (bool): Enables this emulated OSPFv3 router.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current state of the OSPFv6 router.

        Returns
        -------
        - self: This instance with matching ospfV3 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfV3 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfV3 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GracefulRouterRestart(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the gracefulRouterRestart operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gracefulRouterRestart(Arg2=list, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/ospfV3/router])): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        gracefulRouterRestart(Arg2=list, Arg3=number, Arg4=enum, Arg5=number, async_operation=bool)string
        -------------------------------------------------------------------------------------------------
        - Arg2 (list(str[None | /api/v1/sessions/1/ixnetwork/vport/protocols/ospfV3/router])): NOT DEFINED
        - Arg3 (number): NOT DEFINED
        - Arg4 (str(softwareReloadOrUpgrade | softwareRestart | switchToRedundantControlProcessor | unknown)): NOT DEFINED
        - Arg5 (number): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

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
            "gracefulRouterRestart", payload=payload, response_object=None
        )

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the OSPFv3 protocol on a port or group of ports simultaneously.

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

        Stops the OSPFv3 protocol on a port or group of ports simultaneously.

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
