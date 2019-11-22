# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
    The LearnedLsa class encapsulates a list of learnedLsa resources that is managed by the system.
    A list of resources can be retrieved from the server using the LearnedLsa.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedLsa'

    def __init__(self, parent):
        super(LearnedLsa, self).__init__(parent)

    @property
    def AdvRouterId(self):
        """The router ID for the originating router of the LSA.

        Returns:
            str
        """
        return self._get_attribute('advRouterId')

    @property
    def Age(self):
        """The number of seconds that have elapsed since the origination of the LSA by the advertising router.

        Returns:
            number
        """
        return self._get_attribute('age')

    @property
    def LinkStateId(self):
        """An identifier for this LSA that was assigned by the originating router. A unique identifier for the LSA is created when the Link State ID, LS Type, and Advertising Router information are used together.

        Returns:
            str
        """
        return self._get_attribute('linkStateId')

    @property
    def PrefixLength(self):
        """Indicates the Prefix Length

        Returns:
            number
        """
        return self._get_attribute('prefixLength')

    @property
    def PrefixV4Address(self):
        """Indicates the IPv4 Address

        Returns:
            str
        """
        return self._get_attribute('prefixV4Address')

    @property
    def PrefixV6Address(self):
        """Indicates the IPv6 Address

        Returns:
            str
        """
        return self._get_attribute('prefixV6Address')

    @property
    def SequenceNo(self):
        """The sequence number for this LSA. Each instance of an LSA is given an LS sequence number, in order to detect duplicates or old LSAs.

        Returns:
            str
        """
        return self._get_attribute('sequenceNo')

    @property
    def Type(self):
        """The router type of the learned LSA.

        Returns:
            str
        """
        return self._get_attribute('type')

    def find(self, AdvRouterId=None, Age=None, LinkStateId=None, PrefixLength=None, PrefixV4Address=None, PrefixV6Address=None, SequenceNo=None, Type=None):
        """Finds and retrieves learnedLsa data from the server.

        All named parameters support regex and can be used to selectively retrieve learnedLsa data from the server.
        By default the find method takes no parameters and will retrieve all learnedLsa data from the server.

        Args:
            AdvRouterId (str): The router ID for the originating router of the LSA.
            Age (number): The number of seconds that have elapsed since the origination of the LSA by the advertising router.
            LinkStateId (str): An identifier for this LSA that was assigned by the originating router. A unique identifier for the LSA is created when the Link State ID, LS Type, and Advertising Router information are used together.
            PrefixLength (number): Indicates the Prefix Length
            PrefixV4Address (str): Indicates the IPv4 Address
            PrefixV6Address (str): Indicates the IPv6 Address
            SequenceNo (str): The sequence number for this LSA. Each instance of an LSA is given an LS sequence number, in order to detect duplicates or old LSAs.
            Type (str): The router type of the learned LSA.

        Returns:
            self: This instance with matching learnedLsa data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of learnedLsa data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the learnedLsa data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
