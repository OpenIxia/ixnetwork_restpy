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


class Cfm(Base):
    """This object contains the configuration of the CFM protocol.
    The Cfm class encapsulates a required cfm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cfm'
    _SDM_ATT_MAP = {
        'EnableOptionalLmFunctionality': 'enableOptionalLmFunctionality',
        'EnableOptionalTlvValidation': 'enableOptionalTlvValidation',
        'Enabled': 'enabled',
        'ReceiveCcm': 'receiveCcm',
        'RunningState': 'runningState',
        'SendCcm': 'sendCcm',
        'SuppressErrorsOnAis': 'suppressErrorsOnAis',
    }

    def __init__(self, parent):
        super(Cfm, self).__init__(parent)

    @property
    def Bridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_1ef5aad5f0fd904d1f4f7c72e4e0bb2a.Bridge): An instance of the Bridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_1ef5aad5f0fd904d1f4f7c72e4e0bb2a import Bridge
        return Bridge(self)

    @property
    def EnableOptionalLmFunctionality(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOptionalLmFunctionality'])
    @EnableOptionalLmFunctionality.setter
    def EnableOptionalLmFunctionality(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOptionalLmFunctionality'], value)

    @property
    def EnableOptionalTlvValidation(self):
        """
        Returns
        -------
        - bool: If true, the CFM protocol will validate optional TLVs present in CFM packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOptionalTlvValidation'])
    @EnableOptionalTlvValidation.setter
    def EnableOptionalTlvValidation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOptionalTlvValidation'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the CFM protcol is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ReceiveCcm(self):
        """
        Returns
        -------
        - bool: If true, the CFM protocol can receive CFM CCMs on this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveCcm'])
    @ReceiveCcm.setter
    def ReceiveCcm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReceiveCcm'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the CFM protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def SendCcm(self):
        """
        Returns
        -------
        - bool: If true, the CFM protocol can send CFM CCMs from this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendCcm'])
    @SendCcm.setter
    def SendCcm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendCcm'], value)

    @property
    def SuppressErrorsOnAis(self):
        """
        Returns
        -------
        - bool: If true, the errors on AIS are suopressed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SuppressErrorsOnAis'])
    @SuppressErrorsOnAis.setter
    def SuppressErrorsOnAis(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SuppressErrorsOnAis'], value)

    def update(self, EnableOptionalLmFunctionality=None, EnableOptionalTlvValidation=None, Enabled=None, ReceiveCcm=None, SendCcm=None, SuppressErrorsOnAis=None):
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

    def Start(self):
        """Executes the start operation on the server.

        Starts the CFM protocol on a port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the CFM protocol on a port or group of ports.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
