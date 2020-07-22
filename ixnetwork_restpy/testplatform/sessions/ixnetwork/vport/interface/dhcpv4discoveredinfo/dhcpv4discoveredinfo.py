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


class DhcpV4DiscoveredInfo(Base):
    """The Dynamic Host Configuration Protocol (DHCP) Discovered Information is based on DHCPv4 defined in RFC 2131.  When the protocol interface is set for DHCP and enabled, DHCP negotiations will be started.
    The DhcpV4DiscoveredInfo class encapsulates a required dhcpV4DiscoveredInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpV4DiscoveredInfo'
    _SDM_ATT_MAP = {
        'Gateway': 'gateway',
        'Ipv4Address': 'ipv4Address',
        'Ipv4Mask': 'ipv4Mask',
        'IsDhcpV4LearnedInfoRefreshed': 'isDhcpV4LearnedInfoRefreshed',
        'LeaseDuration': 'leaseDuration',
        'ProtocolInterface': 'protocolInterface',
        'Tlv': 'tlv',
    }

    def __init__(self, parent):
        super(DhcpV4DiscoveredInfo, self).__init__(parent)

    @property
    def Gateway(self):
        """
        Returns
        -------
        - str: (Read only) A learned/allocated IPv4 Gateway address for this interface on the router that connects to the network segment on which the source host is located.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gateway'])

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: (Read only) A learned/allocated IPv4 address for this interface,
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Address'])

    @property
    def Ipv4Mask(self):
        """
        Returns
        -------
        - number: (Read only) A 32-bit address mask used in IP to indicate the bits of an IP address that are being used for the subnet address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Mask'])

    @property
    def IsDhcpV4LearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (Read Only) When true, the DHCPv4 discovered information is refreshed automatically.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDhcpV4LearnedInfoRefreshed'])

    @property
    def LeaseDuration(self):
        """
        Returns
        -------
        - number: (Read Only) The user-specified value and the lease timer (from the DHCP Server) are compared. The lowest value is used as the release/renew timer. After this time period has elapsed, the address will be renewed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LeaseDuration'])

    @property
    def ProtocolInterface(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): (Read only) An Ixia protocol interface that is negotiating with the DHCP Server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])

    @property
    def Tlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str)): (Read only) Type Length Value for DHCPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tlv'])
