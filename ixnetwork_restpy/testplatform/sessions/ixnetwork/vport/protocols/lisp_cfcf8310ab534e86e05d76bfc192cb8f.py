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


class Lisp(Base):
    """Details about the list processing are provided here
    The Lisp class encapsulates a required lisp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "lisp"
    _SDM_ATT_MAP = {
        "BurstIntervalInMs": "burstIntervalInMs",
        "Enabled": "enabled",
        "Ipv4MapRegisterPacketsPerBurst": "ipv4MapRegisterPacketsPerBurst",
        "Ipv4MapRequestPacketsPerBurst": "ipv4MapRequestPacketsPerBurst",
        "Ipv4SmrPacketsPerBurst": "ipv4SmrPacketsPerBurst",
        "Ipv6MapRegisterPacketsPerBurst": "ipv6MapRegisterPacketsPerBurst",
        "Ipv6MapRequestPacketsPerBurst": "ipv6MapRequestPacketsPerBurst",
        "Ipv6SmrPacketsPerBurst": "ipv6SmrPacketsPerBurst",
        "ProtocolState": "protocolState",
    }
    _SDM_ENUM_MAP = {
        "protocolState": ["stopped", "unknown", "stopping", "started", "starting"],
    }

    def __init__(self, parent, list_op=False):
        super(Lisp, self).__init__(parent, list_op)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_357d2cf668d2b194253f1fce270d5f0d.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_357d2cf668d2b194253f1fce270d5f0d import (
            Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Router", None) is not None:
                return self._properties.get("Router")
        return Router(self)

    @property
    def SiteEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.siteeidrange_bcf447bff5a7aca1758c0baa17c72645.SiteEidRange): An instance of the SiteEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.siteeidrange_bcf447bff5a7aca1758c0baa17c72645 import (
            SiteEidRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SiteEidRange", None) is not None:
                return self._properties.get("SiteEidRange")
        return SiteEidRange(self)

    @property
    def BurstIntervalInMs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It shows the details abou the burst interval in micro seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstIntervalInMs"])

    @BurstIntervalInMs.setter
    def BurstIntervalInMs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstIntervalInMs"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it shows enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Ipv4MapRegisterPacketsPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the ip v4 map register packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4MapRegisterPacketsPerBurst"])

    @Ipv4MapRegisterPacketsPerBurst.setter
    def Ipv4MapRegisterPacketsPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4MapRegisterPacketsPerBurst"], value)

    @property
    def Ipv4MapRequestPacketsPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the ip v4 map requests packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4MapRequestPacketsPerBurst"])

    @Ipv4MapRequestPacketsPerBurst.setter
    def Ipv4MapRequestPacketsPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4MapRequestPacketsPerBurst"], value)

    @property
    def Ipv4SmrPacketsPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the Ip v4 Smr packets per bursts
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4SmrPacketsPerBurst"])

    @Ipv4SmrPacketsPerBurst.setter
    def Ipv4SmrPacketsPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4SmrPacketsPerBurst"], value)

    @property
    def Ipv6MapRegisterPacketsPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the ip v6 map register packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6MapRegisterPacketsPerBurst"])

    @Ipv6MapRegisterPacketsPerBurst.setter
    def Ipv6MapRegisterPacketsPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6MapRegisterPacketsPerBurst"], value)

    @property
    def Ipv6MapRequestPacketsPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the ip v6 map requests packets per burst
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6MapRequestPacketsPerBurst"])

    @Ipv6MapRequestPacketsPerBurst.setter
    def Ipv6MapRequestPacketsPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6MapRequestPacketsPerBurst"], value)

    @property
    def Ipv6SmrPacketsPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the Ip v6 Smr packets per bursts
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6SmrPacketsPerBurst"])

    @Ipv6SmrPacketsPerBurst.setter
    def Ipv6SmrPacketsPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6SmrPacketsPerBurst"], value)

    @property
    def ProtocolState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(stopped | unknown | stopping | started | starting): Shows different protocol states (read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolState"])

    def update(
        self,
        BurstIntervalInMs=None,
        Enabled=None,
        Ipv4MapRegisterPacketsPerBurst=None,
        Ipv4MapRequestPacketsPerBurst=None,
        Ipv4SmrPacketsPerBurst=None,
        Ipv6MapRegisterPacketsPerBurst=None,
        Ipv6MapRequestPacketsPerBurst=None,
        Ipv6SmrPacketsPerBurst=None,
    ):
        # type: (int, bool, int, int, int, int, int, int) -> Lisp
        """Updates lisp resource on the server.

        Args
        ----
        - BurstIntervalInMs (number): It shows the details abou the burst interval in micro seconds
        - Enabled (bool): If true, it shows enabled.
        - Ipv4MapRegisterPacketsPerBurst (number): It gives details about the ip v4 map register packets per burst
        - Ipv4MapRequestPacketsPerBurst (number): It gives details about the ip v4 map requests packets per burst
        - Ipv4SmrPacketsPerBurst (number): It gives details about the Ip v4 Smr packets per bursts
        - Ipv6MapRegisterPacketsPerBurst (number): It gives details about the ip v6 map register packets per burst
        - Ipv6MapRequestPacketsPerBurst (number): It gives details about the ip v6 map requests packets per burst
        - Ipv6SmrPacketsPerBurst (number): It gives details about the Ip v6 Smr packets per bursts

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BurstIntervalInMs=None,
        Enabled=None,
        Ipv4MapRegisterPacketsPerBurst=None,
        Ipv4MapRequestPacketsPerBurst=None,
        Ipv4SmrPacketsPerBurst=None,
        Ipv6MapRegisterPacketsPerBurst=None,
        Ipv6MapRequestPacketsPerBurst=None,
        Ipv6SmrPacketsPerBurst=None,
        ProtocolState=None,
    ):
        # type: (int, bool, int, int, int, int, int, int, str) -> Lisp
        """Finds and retrieves lisp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lisp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lisp resources from the server.

        Args
        ----
        - BurstIntervalInMs (number): It shows the details abou the burst interval in micro seconds
        - Enabled (bool): If true, it shows enabled.
        - Ipv4MapRegisterPacketsPerBurst (number): It gives details about the ip v4 map register packets per burst
        - Ipv4MapRequestPacketsPerBurst (number): It gives details about the ip v4 map requests packets per burst
        - Ipv4SmrPacketsPerBurst (number): It gives details about the Ip v4 Smr packets per bursts
        - Ipv6MapRegisterPacketsPerBurst (number): It gives details about the ip v6 map register packets per burst
        - Ipv6MapRequestPacketsPerBurst (number): It gives details about the ip v6 map requests packets per burst
        - Ipv6SmrPacketsPerBurst (number): It gives details about the Ip v6 Smr packets per bursts
        - ProtocolState (str(stopped | unknown | stopping | started | starting)): Shows different protocol states (read-only)

        Returns
        -------
        - self: This instance with matching lisp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lisp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lisp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        NOT DEFINED

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

        NOT DEFINED

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
