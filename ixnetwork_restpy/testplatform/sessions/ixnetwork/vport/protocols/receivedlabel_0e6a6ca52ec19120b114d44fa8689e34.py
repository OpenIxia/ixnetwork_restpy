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


class ReceivedLabel(Base):
    """List of labels received from the DUT.
    The ReceivedLabel class encapsulates a list of receivedLabel resources that are managed by the system.
    A list of resources can be retrieved from the server using the ReceivedLabel.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'receivedLabel'
    _SDM_ATT_MAP = {
        'CurrentLspOrSubLspUpTime': 'currentLspOrSubLspUpTime',
        'DestinationIp': 'destinationIp',
        'Label': 'label',
        'LeafIp': 'leafIp',
        'LspId': 'lspId',
        'LspOrSubLspSetupTime': 'lspOrSubLspSetupTime',
        'ReservationState': 'reservationState',
        'SourceIp': 'sourceIp',
        'TunnelId': 'tunnelId',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(ReceivedLabel, self).__init__(parent)

    @property
    def CurrentLspOrSubLspUpTime(self):
        """
        Returns
        -------
        - number: Indicates the re-optimization time per LSP/Sub LSP in port level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentLspOrSubLspUpTime'])

    @property
    def DestinationIp(self):
        """
        Returns
        -------
        - str: The destination router's IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationIp'])

    @property
    def Label(self):
        """
        Returns
        -------
        - number: Label value received from the DUT for the LSP/Tunnel ID, in response to a Label Request from the Ixia-emulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Label'])

    @property
    def LeafIp(self):
        """
        Returns
        -------
        - str: IP of the leaf range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LeafIp'])

    @property
    def LspId(self):
        """
        Returns
        -------
        - number: A unique LSP tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspId'])

    @property
    def LspOrSubLspSetupTime(self):
        """
        Returns
        -------
        - number: Indicates the set up time per LSP/Sub LSP in port level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspOrSubLspSetupTime'])

    @property
    def ReservationState(self):
        """
        Returns
        -------
        - str: The reservation state after there is a graceful restart. This is not applicable for Ingress and will be equal to None.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReservationState'])

    @property
    def SourceIp(self):
        """
        Returns
        -------
        - str: The source router's IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceIp'])

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - number: A unique tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])

    @property
    def Type(self):
        """
        Returns
        -------
        - str: Tunnel type, one of P2P or P2MP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])

    def find(self, CurrentLspOrSubLspUpTime=None, DestinationIp=None, Label=None, LeafIp=None, LspId=None, LspOrSubLspSetupTime=None, ReservationState=None, SourceIp=None, TunnelId=None, Type=None):
        """Finds and retrieves receivedLabel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve receivedLabel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all receivedLabel resources from the server.

        Args
        ----
        - CurrentLspOrSubLspUpTime (number): Indicates the re-optimization time per LSP/Sub LSP in port level.
        - DestinationIp (str): The destination router's IP address.
        - Label (number): Label value received from the DUT for the LSP/Tunnel ID, in response to a Label Request from the Ixia-emulated router.
        - LeafIp (str): IP of the leaf range.
        - LspId (number): A unique LSP tunnel ID.
        - LspOrSubLspSetupTime (number): Indicates the set up time per LSP/Sub LSP in port level.
        - ReservationState (str): The reservation state after there is a graceful restart. This is not applicable for Ingress and will be equal to None.
        - SourceIp (str): The source router's IP address.
        - TunnelId (number): A unique tunnel ID.
        - Type (str): Tunnel type, one of P2P or P2MP.

        Returns
        -------
        - self: This instance with matching receivedLabel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of receivedLabel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the receivedLabel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
