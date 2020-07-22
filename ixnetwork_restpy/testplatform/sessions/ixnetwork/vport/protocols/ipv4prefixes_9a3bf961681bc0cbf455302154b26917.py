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


class Ipv4Prefixes(Base):
    """This object helps to set the prefixes count of IPv4 prefix type.
    The Ipv4Prefixes class encapsulates a list of ipv4Prefixes resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4Prefixes.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4Prefixes'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'HostName': 'hostName',
        'Ipv4Prefix': 'ipv4Prefix',
        'LearnedVia': 'learnedVia',
        'LspId': 'lspId',
        'Metric': 'metric',
        'SequenceNumber': 'sequenceNumber',
    }

    def __init__(self, parent):
        super(Ipv4Prefixes, self).__init__(parent)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: The time since last refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: The host name as retrieved from the related packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])

    @property
    def Ipv4Prefix(self):
        """
        Returns
        -------
        - str: Mask width of IPv4 Prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Prefix'])

    @property
    def LearnedVia(self):
        """
        Returns
        -------
        - str: Learned via L1 Adjacency/L2 Adjacency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnedVia'])

    @property
    def LspId(self):
        """
        Returns
        -------
        - str: The LSP number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspId'])

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: The route metric.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: Sequence number of the LSP containing the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    def find(self, Age=None, HostName=None, Ipv4Prefix=None, LearnedVia=None, LspId=None, Metric=None, SequenceNumber=None):
        """Finds and retrieves ipv4Prefixes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4Prefixes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4Prefixes resources from the server.

        Args
        ----
        - Age (number): The time since last refreshed.
        - HostName (str): The host name as retrieved from the related packets.
        - Ipv4Prefix (str): Mask width of IPv4 Prefix.
        - LearnedVia (str): Learned via L1 Adjacency/L2 Adjacency.
        - LspId (str): The LSP number.
        - Metric (number): The route metric.
        - SequenceNumber (number): Sequence number of the LSP containing the route.

        Returns
        -------
        - self: This instance with matching ipv4Prefixes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4Prefixes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4Prefixes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
