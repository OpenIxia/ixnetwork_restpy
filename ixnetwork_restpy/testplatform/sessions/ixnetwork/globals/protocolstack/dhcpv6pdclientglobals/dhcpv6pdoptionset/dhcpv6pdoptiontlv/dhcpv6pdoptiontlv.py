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


class Dhcpv6PdOptionTlv(Base):
    """DHCPv6PD Option TLV (Type-Length-Value)
    The Dhcpv6PdOptionTlv class encapsulates a list of dhcpv6PdOptionTlv resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6PdOptionTlv.find() method.
    The list can be managed by the user by using the Dhcpv6PdOptionTlv.add() and Dhcpv6PdOptionTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6PdOptionTlv'

    def __init__(self, parent):
        super(Dhcpv6PdOptionTlv, self).__init__(parent)

    @property
    def Code(self):
        """Option code.

        Returns:
            number
        """
        return self._get_attribute('code')
    @Code.setter
    def Code(self, value):
        self._set_attribute('code', value)

    @property
    def Name(self):
        """Option name.

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def Rfc(self):
        """True if defined in RFC documents.

        Returns:
            bool
        """
        return self._get_attribute('rfc')
    @Rfc.setter
    def Rfc(self, value):
        self._set_attribute('rfc', value)

    @property
    def Type(self):
        """Option value type.

        Returns:
            str(boolean|domainName|hexadecimal|integer16|integer16List|integer32|integer32List|integer8|integer8List|ipv4Address|ipv4AddressList|ipv4Prefix|ipv6Address|ipv6AddressList|ipv6Prefix|string|zeroLength)
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    @property
    def Value(self):
        """Option value represented as string.

        Returns:
            str
        """
        return self._get_attribute('value')
    @Value.setter
    def Value(self, value):
        self._set_attribute('value', value)

    def update(self, Code=None, Name=None, Rfc=None, Type=None, Value=None):
        """Updates a child instance of dhcpv6PdOptionTlv on the server.

        Args:
            Code (number): Option code.
            Name (str): Option name.
            Rfc (bool): True if defined in RFC documents.
            Type (str(boolean|domainName|hexadecimal|integer16|integer16List|integer32|integer32List|integer8|integer8List|ipv4Address|ipv4AddressList|ipv4Prefix|ipv6Address|ipv6AddressList|ipv6Prefix|string|zeroLength)): Option value type.
            Value (str): Option value represented as string.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Code=None, Name=None, Rfc=None, Type=None, Value=None):
        """Adds a new dhcpv6PdOptionTlv node on the server and retrieves it in this instance.

        Args:
            Code (number): Option code.
            Name (str): Option name.
            Rfc (bool): True if defined in RFC documents.
            Type (str(boolean|domainName|hexadecimal|integer16|integer16List|integer32|integer32List|integer8|integer8List|ipv4Address|ipv4AddressList|ipv4Prefix|ipv6Address|ipv6AddressList|ipv6Prefix|string|zeroLength)): Option value type.
            Value (str): Option value represented as string.

        Returns:
            self: This instance with all currently retrieved dhcpv6PdOptionTlv data using find and the newly added dhcpv6PdOptionTlv data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpv6PdOptionTlv data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Code=None, Name=None, ObjectId=None, Rfc=None, Type=None, Value=None):
        """Finds and retrieves dhcpv6PdOptionTlv data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpv6PdOptionTlv data from the server.
        By default the find method takes no parameters and will retrieve all dhcpv6PdOptionTlv data from the server.

        Args:
            Code (number): Option code.
            Name (str): Option name.
            ObjectId (str): Unique identifier for this object
            Rfc (bool): True if defined in RFC documents.
            Type (str(boolean|domainName|hexadecimal|integer16|integer16List|integer32|integer32List|integer8|integer8List|ipv4Address|ipv4AddressList|ipv4Prefix|ipv6Address|ipv6AddressList|ipv6Prefix|string|zeroLength)): Option value type.
            Value (str): Option value represented as string.

        Returns:
            self: This instance with matching dhcpv6PdOptionTlv data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpv6PdOptionTlv data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpv6PdOptionTlv data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
