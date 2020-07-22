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


class LearnedInfo(Base):
    """Views retrieved learned session information.
    The LearnedInfo class encapsulates a list of learnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfo'
    _SDM_ATT_MAP = {
        'DesMinTxInterval': 'desMinTxInterval',
        'MyDisc': 'myDisc',
        'MyIpAddress': 'myIpAddress',
        'PeerDisc': 'peerDisc',
        'PeerFlags': 'peerFlags',
        'PeerIpAddress': 'peerIpAddress',
        'PeerState': 'peerState',
        'PeerUpTime': 'peerUpTime',
        'ProtocolUsingSession': 'protocolUsingSession',
        'ReqMinEchoInterval': 'reqMinEchoInterval',
        'ReqMinRxInterval': 'reqMinRxInterval',
        'SessionState': 'sessionState',
        'SessionType': 'sessionType',
    }

    def __init__(self, parent):
        super(LearnedInfo, self).__init__(parent)

    @property
    def DesMinTxInterval(self):
        """
        Returns
        -------
        - number: This is the minimum interval, in microseconds, that the local system would like to use when transmitting BFD Control packets. The value zero is reserved.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DesMinTxInterval'])

    @property
    def MyDisc(self):
        """
        Returns
        -------
        - number: The discriminator for the session on this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyDisc'])

    @property
    def MyIpAddress(self):
        """
        Returns
        -------
        - str: The local IP address being used by the configured or auto-created BFD session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MyIpAddress'])

    @property
    def PeerDisc(self):
        """
        Returns
        -------
        - number: The discriminator for the for side of the BFD session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerDisc'])

    @property
    def PeerFlags(self):
        """
        Returns
        -------
        - str: The number of peer generated flags received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerFlags'])

    @property
    def PeerIpAddress(self):
        """
        Returns
        -------
        - str: The IP address for the far side of the BFD session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerIpAddress'])

    @property
    def PeerState(self):
        """
        Returns
        -------
        - str: The state of the far side of the BFD session, either active or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerState'])

    @property
    def PeerUpTime(self):
        """
        Returns
        -------
        - number: How long the peer has been active.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerUpTime'])

    @property
    def ProtocolUsingSession(self):
        """
        Returns
        -------
        - str: Which protocol is using the BFD session (for example, OSPF, BGP).
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolUsingSession'])

    @property
    def ReqMinEchoInterval(self):
        """
        Returns
        -------
        - number: This is the minimum interval, in microseconds, between received BFD Echo packets that this system is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReqMinEchoInterval'])

    @property
    def ReqMinRxInterval(self):
        """
        Returns
        -------
        - number: The minimum receive interval, in microseconds, for the far side of the BFD session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReqMinRxInterval'])

    @property
    def SessionState(self):
        """
        Returns
        -------
        - str: Whether the session is active or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionState'])

    @property
    def SessionType(self):
        """
        Returns
        -------
        - str: The type of BFD session, either single or multiple hop.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionType'])

    def find(self, DesMinTxInterval=None, MyDisc=None, MyIpAddress=None, PeerDisc=None, PeerFlags=None, PeerIpAddress=None, PeerState=None, PeerUpTime=None, ProtocolUsingSession=None, ReqMinEchoInterval=None, ReqMinRxInterval=None, SessionState=None, SessionType=None):
        """Finds and retrieves learnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInfo resources from the server.

        Args
        ----
        - DesMinTxInterval (number): This is the minimum interval, in microseconds, that the local system would like to use when transmitting BFD Control packets. The value zero is reserved.
        - MyDisc (number): The discriminator for the session on this interface.
        - MyIpAddress (str): The local IP address being used by the configured or auto-created BFD session.
        - PeerDisc (number): The discriminator for the for side of the BFD session.
        - PeerFlags (str): The number of peer generated flags received.
        - PeerIpAddress (str): The IP address for the far side of the BFD session.
        - PeerState (str): The state of the far side of the BFD session, either active or not.
        - PeerUpTime (number): How long the peer has been active.
        - ProtocolUsingSession (str): Which protocol is using the BFD session (for example, OSPF, BGP).
        - ReqMinEchoInterval (number): This is the minimum interval, in microseconds, between received BFD Echo packets that this system is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets.
        - ReqMinRxInterval (number): The minimum receive interval, in microseconds, for the far side of the BFD session.
        - SessionState (str): Whether the session is active or not.
        - SessionType (str): The type of BFD session, either single or multiple hop.

        Returns
        -------
        - self: This instance with matching learnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
