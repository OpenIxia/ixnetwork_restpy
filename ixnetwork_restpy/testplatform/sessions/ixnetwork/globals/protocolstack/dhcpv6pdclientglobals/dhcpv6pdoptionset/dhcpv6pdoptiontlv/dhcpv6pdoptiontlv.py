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


class Dhcpv6PdOptionTlv(Base):
    """DHCPv6PD Option TLV (Type-Length-Value)
    The Dhcpv6PdOptionTlv class encapsulates a list of dhcpv6PdOptionTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6PdOptionTlv.find() method.
    The list can be managed by using the Dhcpv6PdOptionTlv.add() and Dhcpv6PdOptionTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6PdOptionTlv'
    _SDM_ATT_MAP = {
        'Code': 'code',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Rfc': 'rfc',
        'Type': 'type',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(Dhcpv6PdOptionTlv, self).__init__(parent)

    @property
    def Code(self):
        """
        Returns
        -------
        - number: Option code.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Code'])
    @Code.setter
    def Code(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Code'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Option name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Rfc(self):
        """
        Returns
        -------
        - bool: True if defined in RFC documents.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc'])
    @Rfc.setter
    def Rfc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rfc'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(boolean | domainName | hexadecimal | integer16 | integer16List | integer32 | integer32List | integer8 | integer8List | ipv4Address | ipv4AddressList | ipv4Prefix | ipv6Address | ipv6AddressList | ipv6Prefix | string | zeroLength): Option value type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: Option value represented as string.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Code=None, Name=None, Rfc=None, Type=None, Value=None):
        """Updates dhcpv6PdOptionTlv resource on the server.

        Args
        ----
        - Code (number): Option code.
        - Name (str): Option name.
        - Rfc (bool): True if defined in RFC documents.
        - Type (str(boolean | domainName | hexadecimal | integer16 | integer16List | integer32 | integer32List | integer8 | integer8List | ipv4Address | ipv4AddressList | ipv4Prefix | ipv6Address | ipv6AddressList | ipv6Prefix | string | zeroLength)): Option value type.
        - Value (str): Option value represented as string.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Code=None, Name=None, Rfc=None, Type=None, Value=None):
        """Adds a new dhcpv6PdOptionTlv resource on the server and adds it to the container.

        Args
        ----
        - Code (number): Option code.
        - Name (str): Option name.
        - Rfc (bool): True if defined in RFC documents.
        - Type (str(boolean | domainName | hexadecimal | integer16 | integer16List | integer32 | integer32List | integer8 | integer8List | ipv4Address | ipv4AddressList | ipv4Prefix | ipv6Address | ipv6AddressList | ipv6Prefix | string | zeroLength)): Option value type.
        - Value (str): Option value represented as string.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpv6PdOptionTlv resources using find and the newly added dhcpv6PdOptionTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpv6PdOptionTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Code=None, Name=None, ObjectId=None, Rfc=None, Type=None, Value=None):
        """Finds and retrieves dhcpv6PdOptionTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv6PdOptionTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv6PdOptionTlv resources from the server.

        Args
        ----
        - Code (number): Option code.
        - Name (str): Option name.
        - ObjectId (str): Unique identifier for this object
        - Rfc (bool): True if defined in RFC documents.
        - Type (str(boolean | domainName | hexadecimal | integer16 | integer16List | integer32 | integer32List | integer8 | integer8List | ipv4Address | ipv4AddressList | ipv4Prefix | ipv6Address | ipv6AddressList | ipv6Prefix | string | zeroLength)): Option value type.
        - Value (str): Option value represented as string.

        Returns
        -------
        - self: This instance with matching dhcpv6PdOptionTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv6PdOptionTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv6PdOptionTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
