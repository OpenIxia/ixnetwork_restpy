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


class L2VcIpRange(Base):
    """This object holds a list of Layer 2 VC IP address ranges.
    The L2VcIpRange class encapsulates a required l2VcIpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "l2VcIpRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "IncrementBy": "incrementBy",
        "Mask": "mask",
        "NumHosts": "numHosts",
        "PeerAddress": "peerAddress",
        "StartAddress": "startAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(L2VcIpRange, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the Layer 2 IP address range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IncrementBy(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value to be added for creating each additional L2 VC IP route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementBy"])

    @IncrementBy.setter
    def IncrementBy(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementBy"], value)

    @property
    def Mask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the network address. The masked bits in the first network address form the address prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mask"])

    @Mask.setter
    def Mask(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mask"], value)

    @property
    def NumHosts(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of emulated LDP hosts to be created on this port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumHosts"])

    @NumHosts.setter
    def NumHosts(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumHosts"], value)

    @property
    def PeerAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 32-bit IPv4 address of the LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerAddress"])

    @property
    def StartAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address that starts the L2 VC IP range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartAddress"])

    @StartAddress.setter
    def StartAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartAddress"], value)

    def update(
        self,
        Enabled=None,
        IncrementBy=None,
        Mask=None,
        NumHosts=None,
        StartAddress=None,
    ):
        # type: (bool, int, int, int, str) -> L2VcIpRange
        """Updates l2VcIpRange resource on the server.

        Args
        ----
        - Enabled (bool): Enables the Layer 2 IP address range.
        - IncrementBy (number): The value to be added for creating each additional L2 VC IP route range.
        - Mask (number): The number of bits in the mask applied to the network address. The masked bits in the first network address form the address prefix.
        - NumHosts (number): The number of emulated LDP hosts to be created on this port.
        - StartAddress (str): The IP address that starts the L2 VC IP range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Enabled=None,
        IncrementBy=None,
        Mask=None,
        NumHosts=None,
        PeerAddress=None,
        StartAddress=None,
    ):
        # type: (bool, int, int, int, str, str) -> L2VcIpRange
        """Finds and retrieves l2VcIpRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2VcIpRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2VcIpRange resources from the server.

        Args
        ----
        - Enabled (bool): Enables the Layer 2 IP address range.
        - IncrementBy (number): The value to be added for creating each additional L2 VC IP route range.
        - Mask (number): The number of bits in the mask applied to the network address. The masked bits in the first network address form the address prefix.
        - NumHosts (number): The number of emulated LDP hosts to be created on this port.
        - PeerAddress (str): The 32-bit IPv4 address of the LDP peer.
        - StartAddress (str): The IP address that starts the L2 VC IP range.

        Returns
        -------
        - self: This instance with matching l2VcIpRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2VcIpRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2VcIpRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
