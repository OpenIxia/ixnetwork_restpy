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


class Atm(Base):
    """On Asynchronous Transport Mode (ATM) is a Layer 2, connection-oriented, switching protocol, based on L2 Virtual Circuits (VCs). For operation in a connection-less IP routing or bridging environment, the IP PDUs must be encapsulated within the payload field of an ATM AAL5 CPCS-PDU (ATM Adaptation Layer 5 - Common Part Convergence Sublayer - Protocol Data Unit). The ATM CPCS-PDUs are divided into 48-byte segments which receive 5-byte headers - to form 53-byte ATM cells. The ATM cells are then switched across the ATM network, based on the Virtual Port Identifiers (VPIs) and the Virtual Connection Identifiers (VCIs).
    The Atm class encapsulates a required atm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'atm'
    _SDM_ATT_MAP = {
        'Encapsulation': 'encapsulation',
        'Vci': 'vci',
        'Vpi': 'vpi',
    }

    def __init__(self, parent):
        super(Atm, self).__init__(parent)

    @property
    def Encapsulation(self):
        """
        Returns
        -------
        - str(vcMuxIpv4 | vcMuxIpv6 | vcMuxBridgeFcs | vcMuxBridgeNoFcs | llcClip | llcBridgeFcs | llcBridgeNoFcs): The type of RFC 2684 ATM multiplexing encapsulation (routing) protocol to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Encapsulation'])
    @Encapsulation.setter
    def Encapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Encapsulation'], value)

    @property
    def Vci(self):
        """
        Returns
        -------
        - number: Virtual Circuit/Connection Identifier (VCI) for the ATM VC over which information is being transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vci'])
    @Vci.setter
    def Vci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vci'], value)

    @property
    def Vpi(self):
        """
        Returns
        -------
        - number: Virtual Path Identifier (VPI) for the ATM VC over which information is being transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vpi'])
    @Vpi.setter
    def Vpi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vpi'], value)

    def update(self, Encapsulation=None, Vci=None, Vpi=None):
        """Updates atm resource on the server.

        Args
        ----
        - Encapsulation (str(vcMuxIpv4 | vcMuxIpv6 | vcMuxBridgeFcs | vcMuxBridgeNoFcs | llcClip | llcBridgeFcs | llcBridgeNoFcs)): The type of RFC 2684 ATM multiplexing encapsulation (routing) protocol to be used.
        - Vci (number): Virtual Circuit/Connection Identifier (VCI) for the ATM VC over which information is being transmitted.
        - Vpi (number): Virtual Path Identifier (VPI) for the ATM VC over which information is being transmitted.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
