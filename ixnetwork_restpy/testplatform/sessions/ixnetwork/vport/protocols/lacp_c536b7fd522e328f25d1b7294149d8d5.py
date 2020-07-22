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


class Lacp(Base):
    """This object holds the Link Aggregation Control Protocol (LACP) configuration.
    The Lacp class encapsulates a required lacp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'lacp'
    _SDM_ATT_MAP = {
        'EnablePreservePartnerInfo': 'enablePreservePartnerInfo',
        'Enabled': 'enabled',
        'IsLacpPortLearnedInfoRefreshed': 'isLacpPortLearnedInfoRefreshed',
        'RunningState': 'runningState',
    }

    def __init__(self, parent):
        super(Lacp, self).__init__(parent)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_0415bac4883a6513064dc137e097d25e.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_0415bac4883a6513064dc137e097d25e import LearnedInfo
        return LearnedInfo(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_5d122e850068d22407103423c33741c8.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_5d122e850068d22407103423c33741c8 import Link
        return Link(self)

    @property
    def EnablePreservePartnerInfo(self):
        """
        Returns
        -------
        - bool: If true, the fields of previous link are updatedw
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePreservePartnerInfo'])
    @EnablePreservePartnerInfo.setter
    def EnablePreservePartnerInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePreservePartnerInfo'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the Link Aggregation Control Protocol (LACP) is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IsLacpPortLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned port information is up to date.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLacpPortLearnedInfoRefreshed'])

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of LACP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    def update(self, EnablePreservePartnerInfo=None, Enabled=None):
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

    def RefreshLacpPortLearnedInfo(self):
        """Executes the refreshLacpPortLearnedInfo operation on the server.

        This exec refreshes the LACP port learned information.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLacpPortLearnedInfo', payload=payload, response_object=None)

    def SendMarkerRequest(self):
        """Executes the sendMarkerRequest operation on the server.

        This sends a marker request. The contents of the marker PDU contain the current view of partner (which can be defaulted if no partner is present). The marker will be sent regardless of which state the link is in.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendMarkerRequest', payload=payload, response_object=None)

    def SendUpdate(self):
        """Executes the sendUpdate operation on the server.

        This exec sends an update to the actor's partners after a change has been made to the link's parameters.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendUpdate', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        This exec starts the LACP protocol.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def StartPdu(self):
        """Executes the startPdu operation on the server.

        This exec starts PDUs related to LACP (for example, LACPDU, Marker Request PDU, Marker Response PDU) while the protocol is running on the port.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startPdu', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        This exec stops the LACP protocol.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def StopPdu(self):
        """Executes the stopPdu operation on the server.

        This exec stops PDUs related to LACP (for example, LACPDU, Marker Request PDU, Marker Response PDU) while the protocol is running on the port.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stopPdu', payload=payload, response_object=None)
