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


class Rsvp(Base):
    """Simulates one or more RSVP ingress or egress routers. Concentrates on Traffic Engineering parameters.
    The Rsvp class encapsulates a required rsvp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rsvp"
    _SDM_ATT_MAP = {
        "EnableBgpOverLsp": "enableBgpOverLsp",
        "EnableControlLspInitiationRate": "enableControlLspInitiationRate",
        "EnableShowTimeValue": "enableShowTimeValue",
        "EnableVpnLabelExchangeOverLsp": "enableVpnLabelExchangeOverLsp",
        "Enabled": "enabled",
        "MaxLspInitiationsPerSec": "maxLspInitiationsPerSec",
        "RunningState": "runningState",
        "UseTransportLabelsForMplsOam": "useTransportLabelsForMplsOam",
    }
    _SDM_ENUM_MAP = {
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Rsvp, self).__init__(parent, list_op)

    @property
    def NeighborPair(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborpair_62767236969162b40f4736b7bf4280eb.NeighborPair): An instance of the NeighborPair class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborpair_62767236969162b40f4736b7bf4280eb import (
            NeighborPair,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NeighborPair", None) is not None:
                return self._properties.get("NeighborPair")
        return NeighborPair(self)

    @property
    def EnableBgpOverLsp(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Enables the ability to exchange labels over LSP for VPNs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBgpOverLsp"])

    @EnableBgpOverLsp.setter
    def EnableBgpOverLsp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBgpOverLsp"], value)

    @property
    def EnableControlLspInitiationRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls the LSP initiation rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableControlLspInitiationRate"])

    @EnableControlLspInitiationRate.setter
    def EnableControlLspInitiationRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableControlLspInitiationRate"], value)

    @property
    def EnableShowTimeValue(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows to calculate LSP/sub LSP setup time. When a first path message is sent for an LSP or sub LSP, the state machine takes the time stamp and stores it in the internal structure. It repeats this, when a reserve message is received for that LSP or sub LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableShowTimeValue"])

    @EnableShowTimeValue.setter
    def EnableShowTimeValue(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableShowTimeValue"], value)

    @property
    def EnableVpnLabelExchangeOverLsp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables VPN label exchange over LSP
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVpnLabelExchangeOverLsp"])

    @EnableVpnLabelExchangeOverLsp.setter
    def EnableVpnLabelExchangeOverLsp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVpnLabelExchangeOverLsp"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated RSVP router in the emulated RSVP network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def MaxLspInitiationsPerSec(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of LSP Initiations sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxLspInitiationsPerSec"])

    @MaxLspInitiationsPerSec.setter
    def MaxLspInitiationsPerSec(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxLspInitiationsPerSec"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the RSVP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    @property
    def UseTransportLabelsForMplsOam(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseTransportLabelsForMplsOam"])

    @UseTransportLabelsForMplsOam.setter
    def UseTransportLabelsForMplsOam(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseTransportLabelsForMplsOam"], value)

    def update(
        self,
        EnableBgpOverLsp=None,
        EnableControlLspInitiationRate=None,
        EnableShowTimeValue=None,
        EnableVpnLabelExchangeOverLsp=None,
        Enabled=None,
        MaxLspInitiationsPerSec=None,
        UseTransportLabelsForMplsOam=None,
    ):
        # type: (bool, bool, bool, bool, bool, int, bool) -> Rsvp
        """Updates rsvp resource on the server.

        Args
        ----
        - EnableBgpOverLsp (bool): Enables the ability to exchange labels over LSP for VPNs.
        - EnableControlLspInitiationRate (bool): Controls the LSP initiation rate.
        - EnableShowTimeValue (bool): If true, allows to calculate LSP/sub LSP setup time. When a first path message is sent for an LSP or sub LSP, the state machine takes the time stamp and stores it in the internal structure. It repeats this, when a reserve message is received for that LSP or sub LSP.
        - EnableVpnLabelExchangeOverLsp (bool): If true, enables VPN label exchange over LSP
        - Enabled (bool): Enables or disables the use of this emulated RSVP router in the emulated RSVP network. (default = disabled)
        - MaxLspInitiationsPerSec (number): The maximum number of LSP Initiations sent per second.
        - UseTransportLabelsForMplsOam (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableBgpOverLsp=None,
        EnableControlLspInitiationRate=None,
        EnableShowTimeValue=None,
        EnableVpnLabelExchangeOverLsp=None,
        Enabled=None,
        MaxLspInitiationsPerSec=None,
        RunningState=None,
        UseTransportLabelsForMplsOam=None,
    ):
        # type: (bool, bool, bool, bool, bool, int, str, bool) -> Rsvp
        """Finds and retrieves rsvp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rsvp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rsvp resources from the server.

        Args
        ----
        - EnableBgpOverLsp (bool): Enables the ability to exchange labels over LSP for VPNs.
        - EnableControlLspInitiationRate (bool): Controls the LSP initiation rate.
        - EnableShowTimeValue (bool): If true, allows to calculate LSP/sub LSP setup time. When a first path message is sent for an LSP or sub LSP, the state machine takes the time stamp and stores it in the internal structure. It repeats this, when a reserve message is received for that LSP or sub LSP.
        - EnableVpnLabelExchangeOverLsp (bool): If true, enables VPN label exchange over LSP
        - Enabled (bool): Enables or disables the use of this emulated RSVP router in the emulated RSVP network. (default = disabled)
        - MaxLspInitiationsPerSec (number): The maximum number of LSP Initiations sent per second.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of the RSVP server.
        - UseTransportLabelsForMplsOam (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with matching rsvp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rsvp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rsvp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts RSVP on a port or a group of ports.

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

        Stops RSVP on a port or group of ports.

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
