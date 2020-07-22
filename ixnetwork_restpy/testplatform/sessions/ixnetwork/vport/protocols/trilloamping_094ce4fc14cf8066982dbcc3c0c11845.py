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


class TrillOamPing(Base):
    """NOT DEFINED
    The TrillOamPing class encapsulates a list of trillOamPing resources that are managed by the system.
    A list of resources can be retrieved from the server using the TrillOamPing.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'trillOamPing'
    _SDM_ATT_MAP = {
        'DestinationNickname': 'destinationNickname',
        'IncomingPort': 'incomingPort',
        'NextHop': 'nextHop',
        'OutgoingPort': 'outgoingPort',
        'OutgoingPortMtu': 'outgoingPortMtu',
        'PreviousHop': 'previousHop',
        'ResponseTime': 'responseTime',
        'SequenceNumber': 'sequenceNumber',
        'SourceNickname': 'sourceNickname',
        'Status': 'status',
    }

    def __init__(self, parent):
        super(TrillOamPing, self).__init__(parent)

    @property
    def DestinationNickname(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationNickname'])

    @property
    def IncomingPort(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncomingPort'])

    @property
    def NextHop(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])

    @property
    def OutgoingPort(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingPort'])

    @property
    def OutgoingPortMtu(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutgoingPortMtu'])

    @property
    def PreviousHop(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreviousHop'])

    @property
    def ResponseTime(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResponseTime'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    @property
    def SourceNickname(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceNickname'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(Failure | Success): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    def find(self, DestinationNickname=None, IncomingPort=None, NextHop=None, OutgoingPort=None, OutgoingPortMtu=None, PreviousHop=None, ResponseTime=None, SequenceNumber=None, SourceNickname=None, Status=None):
        """Finds and retrieves trillOamPing resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trillOamPing resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trillOamPing resources from the server.

        Args
        ----
        - DestinationNickname (number): NOT DEFINED
        - IncomingPort (number): NOT DEFINED
        - NextHop (number): NOT DEFINED
        - OutgoingPort (number): NOT DEFINED
        - OutgoingPortMtu (number): NOT DEFINED
        - PreviousHop (number): NOT DEFINED
        - ResponseTime (number): NOT DEFINED
        - SequenceNumber (number): NOT DEFINED
        - SourceNickname (number): NOT DEFINED
        - Status (str(Failure | Success)): NOT DEFINED

        Returns
        -------
        - self: This instance with matching trillOamPing resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trillOamPing data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trillOamPing resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
