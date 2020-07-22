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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rsvp(Base):
    """Simulates one or more RSVP ingress or egress routers. Concentrates on Traffic Engineering parameters.
    The Rsvp class encapsulates a required rsvp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvp'
    _SDM_ATT_MAP = {
        'EnableBgpOverLsp': 'enableBgpOverLsp',
        'EnableControlLspInitiationRate': 'enableControlLspInitiationRate',
        'EnableShowTimeValue': 'enableShowTimeValue',
        'EnableVpnLabelExchangeOverLsp': 'enableVpnLabelExchangeOverLsp',
        'Enabled': 'enabled',
        'MaxLspInitiationsPerSec': 'maxLspInitiationsPerSec',
        'RunningState': 'runningState',
        'UseTransportLabelsForMplsOam': 'useTransportLabelsForMplsOam',
    }

    def __init__(self, parent):
        super(Rsvp, self).__init__(parent)

    @property
    def NeighborPair(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborpair_6b451188874d8642de25a3b708fcb4f1.NeighborPair): An instance of the NeighborPair class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborpair_6b451188874d8642de25a3b708fcb4f1 import NeighborPair
        return NeighborPair(self)

    @property
    def EnableBgpOverLsp(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Enables the ability to exchange labels over LSP for VPNs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBgpOverLsp'])
    @EnableBgpOverLsp.setter
    def EnableBgpOverLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBgpOverLsp'], value)

    @property
    def EnableControlLspInitiationRate(self):
        """
        Returns
        -------
        - bool: Controls the LSP initiation rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableControlLspInitiationRate'])
    @EnableControlLspInitiationRate.setter
    def EnableControlLspInitiationRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableControlLspInitiationRate'], value)

    @property
    def EnableShowTimeValue(self):
        """
        Returns
        -------
        - bool: If true, allows to calculate LSP/sub LSP setup time. When a first path message is sent for an LSP or sub LSP, the state machine takes the time stamp and stores it in the internal structure. It repeats this, when a reserve message is received for that LSP or sub LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableShowTimeValue'])
    @EnableShowTimeValue.setter
    def EnableShowTimeValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableShowTimeValue'], value)

    @property
    def EnableVpnLabelExchangeOverLsp(self):
        """
        Returns
        -------
        - bool: If true, enables VPN label exchange over LSP
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVpnLabelExchangeOverLsp'])
    @EnableVpnLabelExchangeOverLsp.setter
    def EnableVpnLabelExchangeOverLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVpnLabelExchangeOverLsp'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated RSVP router in the emulated RSVP network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def MaxLspInitiationsPerSec(self):
        """
        Returns
        -------
        - number: The maximum number of LSP Initiations sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxLspInitiationsPerSec'])
    @MaxLspInitiationsPerSec.setter
    def MaxLspInitiationsPerSec(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxLspInitiationsPerSec'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the RSVP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def UseTransportLabelsForMplsOam(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseTransportLabelsForMplsOam'])
    @UseTransportLabelsForMplsOam.setter
    def UseTransportLabelsForMplsOam(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseTransportLabelsForMplsOam'], value)

    def update(self, EnableBgpOverLsp=None, EnableControlLspInitiationRate=None, EnableShowTimeValue=None, EnableVpnLabelExchangeOverLsp=None, Enabled=None, MaxLspInitiationsPerSec=None, UseTransportLabelsForMplsOam=None):
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

    def Start(self):
        """Executes the start operation on the server.

        Starts RSVP on a port or a group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops RSVP on a port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
