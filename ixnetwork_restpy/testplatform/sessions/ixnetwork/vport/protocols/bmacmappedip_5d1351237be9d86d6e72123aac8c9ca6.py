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


class BMacMappedIp(Base):
    """This objects holds all the IP (V4/V6) addresses associated with a B-MAC of an ethernet segment.
    The BMacMappedIp class encapsulates a list of bMacMappedIp resources that are managed by the user.
    A list of resources can be retrieved from the server using the BMacMappedIp.find() method.
    The list can be managed by using the BMacMappedIp.add() and BMacMappedIp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bMacMappedIp"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "IpAddress": "ipAddress",
        "IpType": "ipType",
    }
    _SDM_ENUM_MAP = {
        "ipType": ["ipV4", "ipV6"],
    }

    def __init__(self, parent, list_op=False):
        super(BMacMappedIp, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IP address value is given here depending on the IP Type. Default value is all zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipV4 | ipV6): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    def update(self, Enabled=None, IpAddress=None, IpType=None):
        # type: (bool, str, str) -> BMacMappedIp
        """Updates bMacMappedIp resource on the server.

        Args
        ----
        - Enabled (bool): If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        - IpAddress (str): IP address value is given here depending on the IP Type. Default value is all zero.
        - IpType (str(ipV4 | ipV6)): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, IpAddress=None, IpType=None):
        # type: (bool, str, str) -> BMacMappedIp
        """Adds a new bMacMappedIp resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        - IpAddress (str): IP address value is given here depending on the IP Type. Default value is all zero.
        - IpType (str(ipV4 | ipV6)): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.

        Returns
        -------
        - self: This instance with all currently retrieved bMacMappedIp resources using find and the newly added bMacMappedIp resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bMacMappedIp resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, IpAddress=None, IpType=None):
        # type: (bool, str, str) -> BMacMappedIp
        """Finds and retrieves bMacMappedIp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bMacMappedIp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bMacMappedIp resources from the server.

        Args
        ----
        - Enabled (bool): If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        - IpAddress (str): IP address value is given here depending on the IP Type. Default value is all zero.
        - IpType (str(ipV4 | ipV6)): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.

        Returns
        -------
        - self: This instance with matching bMacMappedIp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bMacMappedIp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bMacMappedIp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
