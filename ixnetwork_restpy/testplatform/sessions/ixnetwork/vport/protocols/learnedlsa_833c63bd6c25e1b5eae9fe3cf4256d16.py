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


class LearnedLsa(Base):
    """List of learned LSAs for this router.
    The LearnedLsa class encapsulates a list of learnedLsa resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedLsa.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedLsa'
    _SDM_ATT_MAP = {
        'AdvRouterId': 'advRouterId',
        'Age': 'age',
        'LinkStateId': 'linkStateId',
        'PrefixLength': 'prefixLength',
        'PrefixV4Address': 'prefixV4Address',
        'PrefixV6Address': 'prefixV6Address',
        'SequenceNo': 'sequenceNo',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(LearnedLsa, self).__init__(parent)

    @property
    def AdvRouterId(self):
        """
        Returns
        -------
        - str: The router ID for the originating router of the LSA.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvRouterId'])

    @property
    def Age(self):
        """
        Returns
        -------
        - number: The number of seconds that have elapsed since the origination of the LSA by the advertising router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def LinkStateId(self):
        """
        Returns
        -------
        - str: An identifier for this LSA that was assigned by the originating router. A unique identifier for the LSA is created when the Link State ID, LS Type, and Advertising Router information are used together.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkStateId'])

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: Indicates the Prefix Length
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])

    @property
    def PrefixV4Address(self):
        """
        Returns
        -------
        - str: Indicates the IPv4 Address
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixV4Address'])

    @property
    def PrefixV6Address(self):
        """
        Returns
        -------
        - str: Indicates the IPv6 Address
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixV6Address'])

    @property
    def SequenceNo(self):
        """
        Returns
        -------
        - str: The sequence number for this LSA. Each instance of an LSA is given an LS sequence number, in order to detect duplicates or old LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNo'])

    @property
    def Type(self):
        """
        Returns
        -------
        - str: The router type of the learned LSA.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])

    def find(self, AdvRouterId=None, Age=None, LinkStateId=None, PrefixLength=None, PrefixV4Address=None, PrefixV6Address=None, SequenceNo=None, Type=None):
        """Finds and retrieves learnedLsa resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedLsa resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedLsa resources from the server.

        Args
        ----
        - AdvRouterId (str): The router ID for the originating router of the LSA.
        - Age (number): The number of seconds that have elapsed since the origination of the LSA by the advertising router.
        - LinkStateId (str): An identifier for this LSA that was assigned by the originating router. A unique identifier for the LSA is created when the Link State ID, LS Type, and Advertising Router information are used together.
        - PrefixLength (number): Indicates the Prefix Length
        - PrefixV4Address (str): Indicates the IPv4 Address
        - PrefixV6Address (str): Indicates the IPv6 Address
        - SequenceNo (str): The sequence number for this LSA. Each instance of an LSA is given an LS sequence number, in order to detect duplicates or old LSAs.
        - Type (str): The router type of the learned LSA.

        Returns
        -------
        - self: This instance with matching learnedLsa resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedLsa data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedLsa resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
