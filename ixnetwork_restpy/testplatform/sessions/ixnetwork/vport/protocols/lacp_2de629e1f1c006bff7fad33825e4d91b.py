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


class Lacp(Base):
    """This object holds the Link Aggregation Control Protocol (LACP) configuration.
    The Lacp class encapsulates a required lacp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "lacp"
    _SDM_ATT_MAP = {
        "EnablePreservePartnerInfo": "enablePreservePartnerInfo",
        "Enabled": "enabled",
        "IsLacpPortLearnedInfoRefreshed": "isLacpPortLearnedInfoRefreshed",
        "RunningState": "runningState",
    }
    _SDM_ENUM_MAP = {
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Lacp, self).__init__(parent, list_op)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_4e6b30ede278e0f1f44ceef59a7cc716.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_4e6b30ede278e0f1f44ceef59a7cc716 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_05cc0903dd20fb640a82079159eed6bc.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_05cc0903dd20fb640a82079159eed6bc import (
            Link,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Link", None) is not None:
                return self._properties.get("Link")
        return Link(self)

    @property
    def EnablePreservePartnerInfo(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the fields of previous link are updatedw
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePreservePartnerInfo"])

    @EnablePreservePartnerInfo.setter
    def EnablePreservePartnerInfo(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePreservePartnerInfo"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the Link Aggregation Control Protocol (LACP) is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IsLacpPortLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the learned port information is up to date.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLacpPortLearnedInfoRefreshed"])

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of LACP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    def update(self, EnablePreservePartnerInfo=None, Enabled=None):
        # type: (bool, bool) -> Lacp
        """Updates lacp resource on the server.

        Args
        ----
        - EnablePreservePartnerInfo (bool): If true, the fields of previous link are updatedw
        - Enabled (bool): If true, the Link Aggregation Control Protocol (LACP) is enabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnablePreservePartnerInfo=None,
        Enabled=None,
        IsLacpPortLearnedInfoRefreshed=None,
        RunningState=None,
    ):
        # type: (bool, bool, bool, str) -> Lacp
        """Finds and retrieves lacp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lacp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lacp resources from the server.

        Args
        ----
        - EnablePreservePartnerInfo (bool): If true, the fields of previous link are updatedw
        - Enabled (bool): If true, the Link Aggregation Control Protocol (LACP) is enabled.
        - IsLacpPortLearnedInfoRefreshed (bool): (read only) If true, the learned port information is up to date.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of LACP.

        Returns
        -------
        - self: This instance with matching lacp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lacp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lacp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLacpPortLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the refreshLacpPortLearnedInfo operation on the server.

        This exec refreshes the LACP port learned information.

        refreshLacpPortLearnedInfo(async_operation=bool)
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
            "refreshLacpPortLearnedInfo", payload=payload, response_object=None
        )

    def SendMarkerRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendMarkerRequest operation on the server.

        This sends a marker request. The contents of the marker PDU contain the current view of partner (which can be defaulted if no partner is present). The marker will be sent regardless of which state the link is in.

        sendMarkerRequest(async_operation=bool)
        ---------------------------------------
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
        return self._execute("sendMarkerRequest", payload=payload, response_object=None)

    def SendUpdate(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendUpdate operation on the server.

        This exec sends an update to the actor's partners after a change has been made to the link's parameters.

        sendUpdate(async_operation=bool)
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
        return self._execute("sendUpdate", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        This exec starts the LACP protocol.

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

    def StartPdu(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startPdu operation on the server.

        This exec starts PDUs related to LACP (for example, LACPDU, Marker Request PDU, Marker Response PDU) while the protocol is running on the port.

        startPdu(async_operation=bool)
        ------------------------------
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
        return self._execute("startPdu", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        This exec stops the LACP protocol.

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

    def StopPdu(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopPdu operation on the server.

        This exec stops PDUs related to LACP (for example, LACPDU, Marker Request PDU, Marker Response PDU) while the protocol is running on the port.

        stopPdu(async_operation=bool)
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
        return self._execute("stopPdu", payload=payload, response_object=None)
