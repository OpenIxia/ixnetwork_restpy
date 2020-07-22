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


class TriggeredPingLearnedInfo(Base):
    """This object holds lists of the triggered ping learned information.
    The TriggeredPingLearnedInfo class encapsulates a list of triggeredPingLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the TriggeredPingLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'triggeredPingLearnedInfo'
    _SDM_ATT_MAP = {
        'Fec': 'fec',
        'IncomingLabelStack': 'incomingLabelStack',
        'OutgoingLabelStack': 'outgoingLabelStack',
        'PeerIpAddress': 'peerIpAddress',
        'Reachability': 'reachability',
        'ReturnCode': 'returnCode',
        'ReturnSubCode': 'returnSubCode',
        'Rtt': 'rtt',
    }

    def __init__(self, parent):
        super(TriggeredPingLearnedInfo, self).__init__(parent)

    @property
    def Fec(self):
        """
        Returns
        -------
        - str: This signifies the Forwarding Equivalence Class component.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Fec'])

    @property
    def IncomingLabelStack(self):
        """
        Returns
        -------
        - str: This signifies the incoming label stack value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncomingLabelStack'])

    @property
    def OutgoingLabelStack(self):
        """
        Returns
        -------
        - str: This signifies the outgoing label stack value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingLabelStack'])

    @property
    def PeerIpAddress(self):
        """
        Returns
        -------
        - str: This signifies the learnt IP address for the session.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerIpAddress'])

    @property
    def Reachability(self):
        """
        Returns
        -------
        - str: This signifies the specification of whether the queried MEP could be reached or not, Failure/Partial/Complete.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reachability'])

    @property
    def ReturnCode(self):
        """
        Returns
        -------
        - str: This signifies the return code value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReturnCode'])

    @property
    def ReturnSubCode(self):
        """
        Returns
        -------
        - number: This signifies the return subcode value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReturnSubCode'])

    @property
    def Rtt(self):
        """
        Returns
        -------
        - str: This signifies the Round Trip Time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rtt'])

    def find(self, Fec=None, IncomingLabelStack=None, OutgoingLabelStack=None, PeerIpAddress=None, Reachability=None, ReturnCode=None, ReturnSubCode=None, Rtt=None):
        """Finds and retrieves triggeredPingLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve triggeredPingLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all triggeredPingLearnedInfo resources from the server.

        Args
        ----
        - Fec (str): This signifies the Forwarding Equivalence Class component.
        - IncomingLabelStack (str): This signifies the incoming label stack value.
        - OutgoingLabelStack (str): This signifies the outgoing label stack value.
        - PeerIpAddress (str): This signifies the learnt IP address for the session.
        - Reachability (str): This signifies the specification of whether the queried MEP could be reached or not, Failure/Partial/Complete.
        - ReturnCode (str): This signifies the return code value.
        - ReturnSubCode (number): This signifies the return subcode value.
        - Rtt (str): This signifies the Round Trip Time.

        Returns
        -------
        - self: This instance with matching triggeredPingLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of triggeredPingLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the triggeredPingLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
