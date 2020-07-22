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


class Isis(Base):
    """This object simulates one or more IS-IS routers in a network of routers.
    The Isis class encapsulates a required isis resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isis'
    _SDM_ATT_MAP = {
        'AllL1RbridgesMac': 'allL1RbridgesMac',
        'EmulationType': 'emulationType',
        'Enabled': 'enabled',
        'HelloMulticastMac': 'helloMulticastMac',
        'LspMgroupPdusPerInterval': 'lspMgroupPdusPerInterval',
        'NlpId': 'nlpId',
        'RateControlInterval': 'rateControlInterval',
        'RunningState': 'runningState',
        'SendP2PHellosToUnicastMac': 'sendP2PHellosToUnicastMac',
        'SpbAllL1BridgesMac': 'spbAllL1BridgesMac',
        'SpbHelloMulticastMac': 'spbHelloMulticastMac',
        'SpbNlpId': 'spbNlpId',
    }

    def __init__(self, parent):
        super(Isis, self).__init__(parent)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_1ecea4c371bb121a40e7a349f412c55d.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_1ecea4c371bb121a40e7a349f412c55d import Router
        return Router(self)

    @property
    def AllL1RbridgesMac(self):
        """
        Returns
        -------
        - str: ISIS All L1 RBridge MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllL1RbridgesMac'])
    @AllL1RbridgesMac.setter
    def AllL1RbridgesMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllL1RbridgesMac'], value)

    @property
    def EmulationType(self):
        """
        Returns
        -------
        - str(isisL3Routing | dceIsis | spbIsis | trillIsis): Sets the router emulation type of ISIS component of the protocol server for a particular port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EmulationType'])
    @EmulationType.setter
    def EmulationType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EmulationType'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated IS-IS router in the emulated IS-IS network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def HelloMulticastMac(self):
        """
        Returns
        -------
        - str: ISIS Hello Multicast MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloMulticastMac'])
    @HelloMulticastMac.setter
    def HelloMulticastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloMulticastMac'], value)

    @property
    def LspMgroupPdusPerInterval(self):
        """
        Returns
        -------
        - number: Indicates the number of LSP MGROUP-PDUs to be sent for each interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspMgroupPdusPerInterval'])
    @LspMgroupPdusPerInterval.setter
    def LspMgroupPdusPerInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspMgroupPdusPerInterval'], value)

    @property
    def NlpId(self):
        """
        Returns
        -------
        - number: ISIS NLP ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['NlpId'])
    @NlpId.setter
    def NlpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NlpId'], value)

    @property
    def RateControlInterval(self):
        """
        Returns
        -------
        - number: Indicates the wait time for transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateControlInterval'])
    @RateControlInterval.setter
    def RateControlInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RateControlInterval'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the ISIS server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def SendP2PHellosToUnicastMac(self):
        """
        Returns
        -------
        - bool: If enabled, sends point to point hello messages to unicast mac addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendP2PHellosToUnicastMac'])
    @SendP2PHellosToUnicastMac.setter
    def SendP2PHellosToUnicastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendP2PHellosToUnicastMac'], value)

    @property
    def SpbAllL1BridgesMac(self):
        """
        Returns
        -------
        - str: Contains all SPB ISIS specific attributes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpbAllL1BridgesMac'])
    @SpbAllL1BridgesMac.setter
    def SpbAllL1BridgesMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpbAllL1BridgesMac'], value)

    @property
    def SpbHelloMulticastMac(self):
        """
        Returns
        -------
        - str: Contains all hello messages to multicast mac addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpbHelloMulticastMac'])
    @SpbHelloMulticastMac.setter
    def SpbHelloMulticastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpbHelloMulticastMac'], value)

    @property
    def SpbNlpId(self):
        """
        Returns
        -------
        - number: SPB NLP ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpbNlpId'])
    @SpbNlpId.setter
    def SpbNlpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpbNlpId'], value)

    def update(self, AllL1RbridgesMac=None, EmulationType=None, Enabled=None, HelloMulticastMac=None, LspMgroupPdusPerInterval=None, NlpId=None, RateControlInterval=None, SendP2PHellosToUnicastMac=None, SpbAllL1BridgesMac=None, SpbHelloMulticastMac=None, SpbNlpId=None):
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

    def Start(self):
        """Executes the start operation on the server.

        Starts the ISIS protocol on a port or group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the ISIS protocol on a port or group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
