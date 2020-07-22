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


class TriggeredTracerouteLearnedInfo(Base):
    """This object holds the attributes for triggered trace route learned information.
    The TriggeredTracerouteLearnedInfo class encapsulates a list of triggeredTracerouteLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the TriggeredTracerouteLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'triggeredTracerouteLearnedInfo'
    _SDM_ATT_MAP = {
        'Fec': 'fec',
        'Hops': 'hops',
        'IncomingLabelStack': 'incomingLabelStack',
        'NumberOfReplyingHops': 'numberOfReplyingHops',
        'OutgoingLabelStack': 'outgoingLabelStack',
        'Reachability': 'reachability',
        'SenderHandle': 'senderHandle',
    }

    def __init__(self, parent):
        super(TriggeredTracerouteLearnedInfo, self).__init__(parent)

    @property
    def Hops(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hops_afd65edf9d4aac0ccdf5a3a2bd672a47.Hops): An instance of the Hops class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hops_afd65edf9d4aac0ccdf5a3a2bd672a47 import Hops
        return Hops(self)

    @property
    def Fec(self):
        """
        Returns
        -------
        - str: This signifies the FEC component.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Fec'])

    @property
    def Hops(self):
        """
        Returns
        -------
        - str: This signifies the number of LSP hops.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Hops'])

    @property
    def IncomingLabelStack(self):
        """
        Returns
        -------
        - str: This signifies the information is sent to the MPLS-OAM module which is used for validation of FEC stack received in an echo request. This is the assigned labels stack by the Ixia router and bfd/ping messages are expected to be received from DUT with this stack values. The outer value corresponds to the PSN Tunnel Label and the inner value corresponds to the PW label.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncomingLabelStack'])

    @property
    def NumberOfReplyingHops(self):
        """
        Returns
        -------
        - number: This signifies the total number of replying LSP hops.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfReplyingHops'])

    @property
    def OutgoingLabelStack(self):
        """
        Returns
        -------
        - str: This signifies the information is sent to the MPLS-OAM module which is used for validation of FEC outgoing Label stack that is received in an echo request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingLabelStack'])

    @property
    def Reachability(self):
        """
        Returns
        -------
        - str: This signifies whether the LSP is reachable with a proper return code or not. If the return code is not set to 3, in the received reply message or if there is no reply message that is received, then the field will show unreachable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reachability'])

    @property
    def SenderHandle(self):
        """
        Returns
        -------
        - number: This signifies the sender handle details.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SenderHandle'])

    def find(self, Fec=None, Hops=None, IncomingLabelStack=None, NumberOfReplyingHops=None, OutgoingLabelStack=None, Reachability=None, SenderHandle=None):
        """Finds and retrieves triggeredTracerouteLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve triggeredTracerouteLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all triggeredTracerouteLearnedInfo resources from the server.

        Args
        ----
        - Fec (str): This signifies the FEC component.
        - Hops (str): This signifies the number of LSP hops.
        - IncomingLabelStack (str): This signifies the information is sent to the MPLS-OAM module which is used for validation of FEC stack received in an echo request. This is the assigned labels stack by the Ixia router and bfd/ping messages are expected to be received from DUT with this stack values. The outer value corresponds to the PSN Tunnel Label and the inner value corresponds to the PW label.
        - NumberOfReplyingHops (number): This signifies the total number of replying LSP hops.
        - OutgoingLabelStack (str): This signifies the information is sent to the MPLS-OAM module which is used for validation of FEC outgoing Label stack that is received in an echo request.
        - Reachability (str): This signifies whether the LSP is reachable with a proper return code or not. If the return code is not set to 3, in the received reply message or if there is no reply message that is received, then the field will show unreachable.
        - SenderHandle (number): This signifies the sender handle details.

        Returns
        -------
        - self: This instance with matching triggeredTracerouteLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of triggeredTracerouteLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the triggeredTracerouteLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
