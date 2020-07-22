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


class MplsTp(Base):
    """This object contains the MPLSTP protocol configuration.
    The MplsTp class encapsulates a required mplsTp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'mplsTp'
    _SDM_ATT_MAP = {
        'ApsChannelType': 'apsChannelType',
        'BfdCcChannelType': 'bfdCcChannelType',
        'DelayManagementChannelType': 'delayManagementChannelType',
        'EnableHighPerformanceMode': 'enableHighPerformanceMode',
        'Enabled': 'enabled',
        'FaultManagementChannelType': 'faultManagementChannelType',
        'LossMeasurementChannelType': 'lossMeasurementChannelType',
        'OnDemandCvChannelType': 'onDemandCvChannelType',
        'PwStatusChannelType': 'pwStatusChannelType',
        'RunningState': 'runningState',
        'Y1731ChannelType': 'y1731ChannelType',
    }

    def __init__(self, parent):
        super(MplsTp, self).__init__(parent)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_e0546e4a1984ffc97eb083a90a9d6d33.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_e0546e4a1984ffc97eb083a90a9d6d33 import Router
        return Router(self)

    @property
    def ApsChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the Automatic Protection Switching Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApsChannelType'])
    @ApsChannelType.setter
    def ApsChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApsChannelType'], value)

    @property
    def BfdCcChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the BFD Continuity Check Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdCcChannelType'])
    @BfdCcChannelType.setter
    def BfdCcChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BfdCcChannelType'], value)

    @property
    def DelayManagementChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the Delay Measurement Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayManagementChannelType'])
    @DelayManagementChannelType.setter
    def DelayManagementChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayManagementChannelType'], value)

    @property
    def EnableHighPerformanceMode(self):
        """
        Returns
        -------
        - bool: This signifies select the checkbox to enable high performance mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHighPerformanceMode'])
    @EnableHighPerformanceMode.setter
    def EnableHighPerformanceMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHighPerformanceMode'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: This signifies that the mplsTp protocol is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FaultManagementChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the Fault Management Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FaultManagementChannelType'])
    @FaultManagementChannelType.setter
    def FaultManagementChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FaultManagementChannelType'], value)

    @property
    def LossMeasurementChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the Loss Measurement Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LossMeasurementChannelType'])
    @LossMeasurementChannelType.setter
    def LossMeasurementChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LossMeasurementChannelType'], value)

    @property
    def OnDemandCvChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the On Demand Connectivity Verification Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OnDemandCvChannelType'])
    @OnDemandCvChannelType.setter
    def OnDemandCvChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OnDemandCvChannelType'], value)

    @property
    def PwStatusChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the Pseudowire Status Channel Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PwStatusChannelType'])
    @PwStatusChannelType.setter
    def PwStatusChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PwStatusChannelType'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): This signifies the running state of the protocol. Possible values include Started, Starting, Unknown, Stopping and Stopped.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def Y1731ChannelType(self):
        """DEPRECATED 
        Returns
        -------
        - str: This signifies the Y.1731 Channel Type in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Y1731ChannelType'])
    @Y1731ChannelType.setter
    def Y1731ChannelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Y1731ChannelType'], value)

    def update(self, ApsChannelType=None, BfdCcChannelType=None, DelayManagementChannelType=None, EnableHighPerformanceMode=None, Enabled=None, FaultManagementChannelType=None, LossMeasurementChannelType=None, OnDemandCvChannelType=None, PwStatusChannelType=None, Y1731ChannelType=None):
        """Updates mplsTp resource on the server.

        Args
        ----
        - ApsChannelType (str): This signifies the Automatic Protection Switching Channel Type in hexadecimal format.
        - BfdCcChannelType (str): This signifies the BFD Continuity Check Channel Type in hexadecimal format.
        - DelayManagementChannelType (str): This signifies the Delay Measurement Channel Type in hexadecimal format.
        - EnableHighPerformanceMode (bool): This signifies select the checkbox to enable high performance mode.
        - Enabled (bool): This signifies that the mplsTp protocol is enabled.
        - FaultManagementChannelType (str): This signifies the Fault Management Channel Type in hexadecimal format.
        - LossMeasurementChannelType (str): This signifies the Loss Measurement Channel Type in hexadecimal format.
        - OnDemandCvChannelType (str): This signifies the On Demand Connectivity Verification Channel Type in hexadecimal format.
        - PwStatusChannelType (str): This signifies the Pseudowire Status Channel Type.
        - Y1731ChannelType (str): This signifies the Y.1731 Channel Type in hexadecimal format.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self):
        """Executes the start operation on the server.

        This signifies the starting of the MPLSTP protocol on a port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        This signifies the stopping of the MPLSTP protocol on a port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
