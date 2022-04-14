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


class Cfm(Base):
    """This object contains the configuration of the CFM protocol.
    The Cfm class encapsulates a required cfm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cfm"
    _SDM_ATT_MAP = {
        "EnableOptionalLmFunctionality": "enableOptionalLmFunctionality",
        "EnableOptionalTlvValidation": "enableOptionalTlvValidation",
        "Enabled": "enabled",
        "ReceiveCcm": "receiveCcm",
        "RunningState": "runningState",
        "SendCcm": "sendCcm",
        "SuppressErrorsOnAis": "suppressErrorsOnAis",
    }
    _SDM_ENUM_MAP = {
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Cfm, self).__init__(parent, list_op)

    @property
    def Bridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_303490481015947d17e8f3098590185b.Bridge): An instance of the Bridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_303490481015947d17e8f3098590185b import (
            Bridge,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bridge", None) is not None:
                return self._properties.get("Bridge")
        return Bridge(self)

    @property
    def EnableOptionalLmFunctionality(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOptionalLmFunctionality"])

    @EnableOptionalLmFunctionality.setter
    def EnableOptionalLmFunctionality(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOptionalLmFunctionality"], value)

    @property
    def EnableOptionalTlvValidation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the CFM protocol will validate optional TLVs present in CFM packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOptionalTlvValidation"])

    @EnableOptionalTlvValidation.setter
    def EnableOptionalTlvValidation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOptionalTlvValidation"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the CFM protcol is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ReceiveCcm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the CFM protocol can receive CFM CCMs on this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveCcm"])

    @ReceiveCcm.setter
    def ReceiveCcm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveCcm"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the CFM protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    @property
    def SendCcm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the CFM protocol can send CFM CCMs from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendCcm"])

    @SendCcm.setter
    def SendCcm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendCcm"], value)

    @property
    def SuppressErrorsOnAis(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the errors on AIS are suopressed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SuppressErrorsOnAis"])

    @SuppressErrorsOnAis.setter
    def SuppressErrorsOnAis(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SuppressErrorsOnAis"], value)

    def update(
        self,
        EnableOptionalLmFunctionality=None,
        EnableOptionalTlvValidation=None,
        Enabled=None,
        ReceiveCcm=None,
        SendCcm=None,
        SuppressErrorsOnAis=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool) -> Cfm
        """Updates cfm resource on the server.

        Args
        ----
        - EnableOptionalLmFunctionality (bool): NOT DEFINED
        - EnableOptionalTlvValidation (bool): If true, the CFM protocol will validate optional TLVs present in CFM packets.
        - Enabled (bool): If true, the CFM protcol is enabled.
        - ReceiveCcm (bool): If true, the CFM protocol can receive CFM CCMs on this port.
        - SendCcm (bool): If true, the CFM protocol can send CFM CCMs from this port.
        - SuppressErrorsOnAis (bool): If true, the errors on AIS are suopressed.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableOptionalLmFunctionality=None,
        EnableOptionalTlvValidation=None,
        Enabled=None,
        ReceiveCcm=None,
        RunningState=None,
        SendCcm=None,
        SuppressErrorsOnAis=None,
    ):
        # type: (bool, bool, bool, bool, str, bool, bool) -> Cfm
        """Finds and retrieves cfm resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cfm resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cfm resources from the server.

        Args
        ----
        - EnableOptionalLmFunctionality (bool): NOT DEFINED
        - EnableOptionalTlvValidation (bool): If true, the CFM protocol will validate optional TLVs present in CFM packets.
        - Enabled (bool): If true, the CFM protcol is enabled.
        - ReceiveCcm (bool): If true, the CFM protocol can receive CFM CCMs on this port.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of the CFM protocol.
        - SendCcm (bool): If true, the CFM protocol can send CFM CCMs from this port.
        - SuppressErrorsOnAis (bool): If true, the errors on AIS are suopressed.

        Returns
        -------
        - self: This instance with matching cfm resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cfm data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cfm resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the CFM protocol on a port or group of ports.

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

        Stops the CFM protocol on a port or group of ports.

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
