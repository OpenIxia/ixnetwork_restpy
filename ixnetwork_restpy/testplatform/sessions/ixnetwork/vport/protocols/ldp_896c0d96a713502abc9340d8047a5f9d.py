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


class Ldp(Base):
    """This object simulates one or more routers that use the label distribution protocol.
    The Ldp class encapsulates a required ldp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ldp'
    _SDM_ATT_MAP = {
        'EnableDiscardSelfAdvFecs': 'enableDiscardSelfAdvFecs',
        'EnableHelloJitter': 'enableHelloJitter',
        'EnableLabelExchangeOverLsp': 'enableLabelExchangeOverLsp',
        'EnableVpnLabelExchangeOverLsp': 'enableVpnLabelExchangeOverLsp',
        'Enabled': 'enabled',
        'HelloHoldTime': 'helloHoldTime',
        'HelloInterval': 'helloInterval',
        'KeepAliveHoldTime': 'keepAliveHoldTime',
        'KeepAliveInterval': 'keepAliveInterval',
        'P2mpCapabilityParam': 'p2mpCapabilityParam',
        'P2mpFecType': 'p2mpFecType',
        'RunningState': 'runningState',
        'TargetedHelloInterval': 'targetedHelloInterval',
        'TargetedHoldTime': 'targetedHoldTime',
        'UseTransportLabelsForMplsOam': 'useTransportLabelsForMplsOam',
    }

    def __init__(self, parent):
        super(Ldp, self).__init__(parent)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_bd5429e3853f2e2fb3074aeade9110a8.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_bd5429e3853f2e2fb3074aeade9110a8 import Router
        return Router(self)

    @property
    def EnableDiscardSelfAdvFecs(self):
        """
        Returns
        -------
        - bool: Discards learned labels from the DUT that match any of the enabled configured IPv4 FEC ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDiscardSelfAdvFecs'])
    @EnableDiscardSelfAdvFecs.setter
    def EnableDiscardSelfAdvFecs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDiscardSelfAdvFecs'], value)

    @property
    def EnableHelloJitter(self):
        """
        Returns
        -------
        - bool: Allows staggered transmission of many HELLO messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHelloJitter'])
    @EnableHelloJitter.setter
    def EnableHelloJitter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHelloJitter'], value)

    @property
    def EnableLabelExchangeOverLsp(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Enables the ability to exchange labels over LSP for VPNs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLabelExchangeOverLsp'])
    @EnableLabelExchangeOverLsp.setter
    def EnableLabelExchangeOverLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLabelExchangeOverLsp'], value)

    @property
    def EnableVpnLabelExchangeOverLsp(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: Enables or disables the use of this emulated LDP router in the emulated LDP network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def HelloHoldTime(self):
        """
        Returns
        -------
        - number: One of the timers associated with maintaining adjacencies based on hello messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloHoldTime'])
    @HelloHoldTime.setter
    def HelloHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloHoldTime'], value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: One of the timers associated with maintaining adjacencies based on hello messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def KeepAliveHoldTime(self):
        """
        Returns
        -------
        - number: One of the timers associated with maintaining adjacencies based on PDU and keep-alive messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeepAliveHoldTime'])
    @KeepAliveHoldTime.setter
    def KeepAliveHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeepAliveHoldTime'], value)

    @property
    def KeepAliveInterval(self):
        """
        Returns
        -------
        - number: One of the timers associated with maintaining adjacencies based on PDU and keep-alive messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeepAliveInterval'])
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeepAliveInterval'], value)

    @property
    def P2mpCapabilityParam(self):
        """
        Returns
        -------
        - number: The P2MP capability parameter value in hexadecimal.
        """
        return self._get_attribute(self._SDM_ATT_MAP['P2mpCapabilityParam'])
    @P2mpCapabilityParam.setter
    def P2mpCapabilityParam(self, value):
        self._set_attribute(self._SDM_ATT_MAP['P2mpCapabilityParam'], value)

    @property
    def P2mpFecType(self):
        """
        Returns
        -------
        - number: The MLDP P2MP FEC type value in hexadecimal.
        """
        return self._get_attribute(self._SDM_ATT_MAP['P2mpFecType'])
    @P2mpFecType.setter
    def P2mpFecType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['P2mpFecType'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current state of the LDP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def TargetedHelloInterval(self):
        """
        Returns
        -------
        - number: One of the timers associated with maintaining targeted peer adjacencies based on hello messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetedHelloInterval'])
    @TargetedHelloInterval.setter
    def TargetedHelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetedHelloInterval'], value)

    @property
    def TargetedHoldTime(self):
        """
        Returns
        -------
        - number: One of the timers associated with maintaining targeted peer adjacencies based on hello messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetedHoldTime'])
    @TargetedHoldTime.setter
    def TargetedHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetedHoldTime'], value)

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

    def update(self, EnableDiscardSelfAdvFecs=None, EnableHelloJitter=None, EnableLabelExchangeOverLsp=None, EnableVpnLabelExchangeOverLsp=None, Enabled=None, HelloHoldTime=None, HelloInterval=None, KeepAliveHoldTime=None, KeepAliveInterval=None, P2mpCapabilityParam=None, P2mpFecType=None, TargetedHelloInterval=None, TargetedHoldTime=None, UseTransportLabelsForMplsOam=None):
        """Updates ldp resource on the server.

        Args
        ----
        - EnableDiscardSelfAdvFecs (bool): Discards learned labels from the DUT that match any of the enabled configured IPv4 FEC ranges.
        - EnableHelloJitter (bool): Allows staggered transmission of many HELLO messages.
        - EnableLabelExchangeOverLsp (bool): Enables the ability to exchange labels over LSP for VPNs.
        - EnableVpnLabelExchangeOverLsp (bool): NOT DEFINED
        - Enabled (bool): Enables or disables the use of this emulated LDP router in the emulated LDP network. (default = disabled)
        - HelloHoldTime (number): One of the timers associated with maintaining adjacencies based on hello messages.
        - HelloInterval (number): One of the timers associated with maintaining adjacencies based on hello messages.
        - KeepAliveHoldTime (number): One of the timers associated with maintaining adjacencies based on PDU and keep-alive messages.
        - KeepAliveInterval (number): One of the timers associated with maintaining adjacencies based on PDU and keep-alive messages.
        - P2mpCapabilityParam (number): The P2MP capability parameter value in hexadecimal.
        - P2mpFecType (number): The MLDP P2MP FEC type value in hexadecimal.
        - TargetedHelloInterval (number): One of the timers associated with maintaining targeted peer adjacencies based on hello messages.
        - TargetedHoldTime (number): One of the timers associated with maintaining targeted peer adjacencies based on hello messages.
        - UseTransportLabelsForMplsOam (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self):
        """Executes the start operation on the server.

        Starts the LDP protocol on a port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the LDP protocol on a port of group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
