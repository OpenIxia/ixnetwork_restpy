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


class DhcpV4DiscoveredInfo(Base):
    """The Dynamic Host Configuration Protocol (DHCP) Discovered Information is based on DHCPv4 defined in RFC 2131.  When the protocol interface is set for DHCP and enabled, DHCP negotiations will be started.
    The DhcpV4DiscoveredInfo class encapsulates a required dhcpV4DiscoveredInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dhcpV4DiscoveredInfo"
    _SDM_ATT_MAP = {
        "Gateway": "gateway",
        "Ipv4Address": "ipv4Address",
        "Ipv4Mask": "ipv4Mask",
        "IsDhcpV4LearnedInfoRefreshed": "isDhcpV4LearnedInfoRefreshed",
        "LeaseDuration": "leaseDuration",
        "ProtocolInterface": "protocolInterface",
        "Tlv": "tlv",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DhcpV4DiscoveredInfo, self).__init__(parent, list_op)

    @property
    def Gateway(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read only) A learned/allocated IPv4 Gateway address for this interface on the router that connects to the network segment on which the source host is located.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gateway"])

    @property
    def Ipv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read only) A learned/allocated IPv4 address for this interface,
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Address"])

    @property
    def Ipv4Mask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read only) A 32-bit address mask used in IP to indicate the bits of an IP address that are being used for the subnet address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Mask"])

    @property
    def IsDhcpV4LearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (Read Only) When true, the DHCPv4 discovered information is refreshed automatically.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsDhcpV4LearnedInfoRefreshed"])

    @property
    def LeaseDuration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read Only) The user-specified value and the lease timer (from the DHCP Server) are compared. The lowest value is used as the release/renew timer. After this time period has elapsed, the address will be renewed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LeaseDuration"])

    @property
    def ProtocolInterface(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): (Read only) An Ixia protocol interface that is negotiating with the DHCP Server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolInterface"])

    @property
    def Tlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str)): (Read only) Type Length Value for DHCPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tlv"])

    def find(
        self,
        Gateway=None,
        Ipv4Address=None,
        Ipv4Mask=None,
        IsDhcpV4LearnedInfoRefreshed=None,
        LeaseDuration=None,
        ProtocolInterface=None,
        Tlv=None,
    ):
        """Finds and retrieves dhcpV4DiscoveredInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpV4DiscoveredInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpV4DiscoveredInfo resources from the server.

        Args
        ----
        - Gateway (str): (Read only) A learned/allocated IPv4 Gateway address for this interface on the router that connects to the network segment on which the source host is located.
        - Ipv4Address (str): (Read only) A learned/allocated IPv4 address for this interface,
        - Ipv4Mask (number): (Read only) A 32-bit address mask used in IP to indicate the bits of an IP address that are being used for the subnet address.
        - IsDhcpV4LearnedInfoRefreshed (bool): (Read Only) When true, the DHCPv4 discovered information is refreshed automatically.
        - LeaseDuration (number): (Read Only) The user-specified value and the lease timer (from the DHCP Server) are compared. The lowest value is used as the release/renew timer. After this time period has elapsed, the address will be renewed.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): (Read only) An Ixia protocol interface that is negotiating with the DHCP Server.
        - Tlv (list(dict(arg1:number,arg2:str))): (Read only) Type Length Value for DHCPv4.

        Returns
        -------
        - self: This instance with matching dhcpV4DiscoveredInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpV4DiscoveredInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpV4DiscoveredInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
