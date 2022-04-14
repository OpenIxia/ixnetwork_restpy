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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Ethernet(Base):
    """Controls the general Ethernet interface properties.
    The Ethernet class encapsulates a required ethernet resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ethernet"
    _SDM_ATT_MAP = {
        "MacAddress": "macAddress",
        "Mtu": "mtu",
        "UidFromMac": "uidFromMac",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ethernet, self).__init__(parent, list_op)

    @property
    def MacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A 48-bit hardware address that uniquely identifies each node of a network.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def Mtu(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum packet size, in bytes, that a particular interface can handle.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mtu"])

    @Mtu.setter
    def Mtu(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mtu"], value)

    @property
    def UidFromMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The interface identifier is derived from the MAC address. The interface identifier u (universal/local) bit will be set to zero to indicate global scope.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UidFromMac"])

    @UidFromMac.setter
    def UidFromMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UidFromMac"], value)

    def update(self, MacAddress=None, Mtu=None, UidFromMac=None):
        # type: (str, int, bool) -> Ethernet
        """Updates ethernet resource on the server.

        Args
        ----
        - MacAddress (str): A 48-bit hardware address that uniquely identifies each node of a network.
        - Mtu (number): The maximum packet size, in bytes, that a particular interface can handle.
        - UidFromMac (bool): The interface identifier is derived from the MAC address. The interface identifier u (universal/local) bit will be set to zero to indicate global scope.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, MacAddress=None, Mtu=None, UidFromMac=None):
        # type: (str, int, bool) -> Ethernet
        """Finds and retrieves ethernet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernet resources from the server.

        Args
        ----
        - MacAddress (str): A 48-bit hardware address that uniquely identifies each node of a network.
        - Mtu (number): The maximum packet size, in bytes, that a particular interface can handle.
        - UidFromMac (bool): The interface identifier is derived from the MAC address. The interface identifier u (universal/local) bit will be set to zero to indicate global scope.

        Returns
        -------
        - self: This instance with matching ethernet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
