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


class Pattern(Base):
    """A pattern to match against incoming packets.
    The Pattern class encapsulates a list of pattern resources that are managed by the user.
    A list of resources can be retrieved from the server using the Pattern.find() method.
    The list can be managed by using the Pattern.add() and Pattern.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'pattern'
    _SDM_ATT_MAP = {
        'BitOffset': 'bitOffset',
        'Enabled': 'enabled',
        'Mask': 'mask',
        'Name': 'name',
        'Offset': 'offset',
        'Value': 'value',
        'Width': 'width',
    }

    def __init__(self, parent):
        super(Pattern, self).__init__(parent)

    @property
    def BitOffset(self):
        """
        Returns
        -------
        - number: Bit offset within a byte. Starting point of the mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BitOffset'])
    @BitOffset.setter
    def BitOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BitOffset'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, match incoming packets against this pattern.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Mask(self):
        """
        Returns
        -------
        - str: Bitmask to match against. Same format as value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mask'])
    @Mask.setter
    def Mask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mask'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of pattern.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: Byte offset from start of L2 frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: The field value to match. For MAC, IPv4, and IPv6 addresses, the value is a formatted address. For all other fields, the value is encoded as a string of hex bytes, most significant byte first, and most significant bit first within each byte. Each hex byte must be exactly two hex digits; A-F and a-f are both accepted. The hex bytes must be separated by a single white space. Example: 00 01 02 FF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    @property
    def Width(self):
        """
        Returns
        -------
        - number: Width of field, in bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Width'])
    @Width.setter
    def Width(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Width'], value)

    def update(self, BitOffset=None, Enabled=None, Mask=None, Name=None, Offset=None, Value=None, Width=None):
        """Updates pattern resource on the server.

        Args
        ----
        - BitOffset (number): Bit offset within a byte. Starting point of the mask.
        - Enabled (bool): If true, match incoming packets against this pattern.
        - Mask (str): Bitmask to match against. Same format as value.
        - Name (str): Name of pattern.
        - Offset (number): Byte offset from start of L2 frame.
        - Value (str): The field value to match. For MAC, IPv4, and IPv6 addresses, the value is a formatted address. For all other fields, the value is encoded as a string of hex bytes, most significant byte first, and most significant bit first within each byte. Each hex byte must be exactly two hex digits; A-F and a-f are both accepted. The hex bytes must be separated by a single white space. Example: 00 01 02 FF.
        - Width (number): Width of field, in bits.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BitOffset=None, Enabled=None, Mask=None, Name=None, Offset=None, Value=None, Width=None):
        """Adds a new pattern resource on the server and adds it to the container.

        Args
        ----
        - BitOffset (number): Bit offset within a byte. Starting point of the mask.
        - Enabled (bool): If true, match incoming packets against this pattern.
        - Mask (str): Bitmask to match against. Same format as value.
        - Name (str): Name of pattern.
        - Offset (number): Byte offset from start of L2 frame.
        - Value (str): The field value to match. For MAC, IPv4, and IPv6 addresses, the value is a formatted address. For all other fields, the value is encoded as a string of hex bytes, most significant byte first, and most significant bit first within each byte. Each hex byte must be exactly two hex digits; A-F and a-f are both accepted. The hex bytes must be separated by a single white space. Example: 00 01 02 FF.
        - Width (number): Width of field, in bits.

        Returns
        -------
        - self: This instance with all currently retrieved pattern resources using find and the newly added pattern resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pattern resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BitOffset=None, Enabled=None, Mask=None, Name=None, Offset=None, Value=None, Width=None):
        """Finds and retrieves pattern resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pattern resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pattern resources from the server.

        Args
        ----
        - BitOffset (number): Bit offset within a byte. Starting point of the mask.
        - Enabled (bool): If true, match incoming packets against this pattern.
        - Mask (str): Bitmask to match against. Same format as value.
        - Name (str): Name of pattern.
        - Offset (number): Byte offset from start of L2 frame.
        - Value (str): The field value to match. For MAC, IPv4, and IPv6 addresses, the value is a formatted address. For all other fields, the value is encoded as a string of hex bytes, most significant byte first, and most significant bit first within each byte. Each hex byte must be exactly two hex digits; A-F and a-f are both accepted. The hex bytes must be separated by a single white space. Example: 00 01 02 FF.
        - Width (number): Width of field, in bits.

        Returns
        -------
        - self: This instance with matching pattern resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pattern data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pattern resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
