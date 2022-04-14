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


class Stp(Base):
    """This object simulates one or more STP/RSTP/MSTP/PVST+/RPVST+ bridges in a network of bridges.
    The Stp class encapsulates a required stp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "stp"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "RunningState": "runningState",
    }
    _SDM_ENUM_MAP = {
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Stp, self).__init__(parent, list_op)

    @property
    def Bridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_f5eb213292554c87fbba0896618d8189.Bridge): An instance of the Bridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_f5eb213292554c87fbba0896618d8189 import (
            Bridge,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bridge", None) is not None:
                return self._properties.get("Bridge")
        return Bridge(self)

    @property
    def Lan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_7e56cbddd866444e811691cca31f325e.Lan): An instance of the Lan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_7e56cbddd866444e811691cca31f325e import (
            Lan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lan", None) is not None:
                return self._properties.get("Lan")
        return Lan(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated spanning-tree protocol (STP) router in the emulated STP network. (default = disabled) STP is used to resolve and eliminate loops in a network.
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
        - str(unknown | stopped | stopping | starting | started): The current running state of the STP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    def update(self, Enabled=None):
        # type: (bool) -> Stp
        """Updates stp resource on the server.

        Args
        ----
        - Enabled (bool): Enables or disables the use of this emulated spanning-tree protocol (STP) router in the emulated STP network. (default = disabled) STP is used to resolve and eliminate loops in a network.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None, RunningState=None):
        # type: (bool, str) -> Stp
        """Finds and retrieves stp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve stp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all stp resources from the server.

        Args
        ----
        - Enabled (bool): Enables or disables the use of this emulated spanning-tree protocol (STP) router in the emulated STP network. (default = disabled) STP is used to resolve and eliminate loops in a network.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of the STP server.

        Returns
        -------
        - self: This instance with matching stp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of stp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the stp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts STP on a port or group of ports.

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

        Stops STP on a port or group of ports.

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
