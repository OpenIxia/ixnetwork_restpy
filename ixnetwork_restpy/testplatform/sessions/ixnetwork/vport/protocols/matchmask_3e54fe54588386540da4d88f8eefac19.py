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


class MatchMask(Base):
    """Select the type of match mask capability that the table will support.
    The MatchMask class encapsulates a required matchMask resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "matchMask"
    _SDM_ATT_MAP = {
        "ArpDestinationIpv4AddressMask": "arpDestinationIpv4AddressMask",
        "ArpDstHwAddressMask": "arpDstHwAddressMask",
        "ArpSourceIpv4AddressMask": "arpSourceIpv4AddressMask",
        "ArpSrcHwAddressMask": "arpSrcHwAddressMask",
        "EthernetDestinationMask": "ethernetDestinationMask",
        "EthernetSourceMask": "ethernetSourceMask",
        "Ipv4DestinationMask": "ipv4DestinationMask",
        "Ipv4SourceMask": "ipv4SourceMask",
        "Ipv6DestinationMask": "ipv6DestinationMask",
        "Ipv6ExtHeaderMask": "ipv6ExtHeaderMask",
        "Ipv6FlowLabelMask": "ipv6FlowLabelMask",
        "Ipv6SourceMask": "ipv6SourceMask",
        "MetadataMask": "metadataMask",
        "PbbIsidMask": "pbbIsidMask",
        "TunnelIdMask": "tunnelIdMask",
        "VlanMask": "vlanMask",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(MatchMask, self).__init__(parent, list_op)

    @property
    def ArpDestinationIpv4AddressMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ARP Destination IPv4 Address Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDestinationIpv4AddressMask"])

    @ArpDestinationIpv4AddressMask.setter
    def ArpDestinationIpv4AddressMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpDestinationIpv4AddressMask"], value)

    @property
    def ArpDstHwAddressMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ARP Destination Hardware Address Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDstHwAddressMask"])

    @ArpDstHwAddressMask.setter
    def ArpDstHwAddressMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpDstHwAddressMask"], value)

    @property
    def ArpSourceIpv4AddressMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ARP Source IPv4 Address Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSourceIpv4AddressMask"])

    @ArpSourceIpv4AddressMask.setter
    def ArpSourceIpv4AddressMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpSourceIpv4AddressMask"], value)

    @property
    def ArpSrcHwAddressMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ARP Source Hardware Address Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSrcHwAddressMask"])

    @ArpSrcHwAddressMask.setter
    def ArpSrcHwAddressMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpSrcHwAddressMask"], value)

    @property
    def EthernetDestinationMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Ethernet Destination Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestinationMask"])

    @EthernetDestinationMask.setter
    def EthernetDestinationMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetDestinationMask"], value)

    @property
    def EthernetSourceMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Ethernet Source Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSourceMask"])

    @EthernetSourceMask.setter
    def EthernetSourceMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetSourceMask"], value)

    @property
    def Ipv4DestinationMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IPv4 Destination Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4DestinationMask"])

    @Ipv4DestinationMask.setter
    def Ipv4DestinationMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4DestinationMask"], value)

    @property
    def Ipv4SourceMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IPv4 Source Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceMask"])

    @Ipv4SourceMask.setter
    def Ipv4SourceMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4SourceMask"], value)

    @property
    def Ipv6DestinationMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IPv6 Destination Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6DestinationMask"])

    @Ipv6DestinationMask.setter
    def Ipv6DestinationMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6DestinationMask"], value)

    @property
    def Ipv6ExtHeaderMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IPv6 Ext Header Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6ExtHeaderMask"])

    @Ipv6ExtHeaderMask.setter
    def Ipv6ExtHeaderMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6ExtHeaderMask"], value)

    @property
    def Ipv6FlowLabelMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IPv6 Flow Label Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabelMask"])

    @Ipv6FlowLabelMask.setter
    def Ipv6FlowLabelMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6FlowLabelMask"], value)

    @property
    def Ipv6SourceMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IPv6 Source Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceMask"])

    @Ipv6SourceMask.setter
    def Ipv6SourceMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6SourceMask"], value)

    @property
    def MetadataMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, MetaData Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetadataMask"])

    @MetadataMask.setter
    def MetadataMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MetadataMask"], value)

    @property
    def PbbIsidMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Tunnel ID Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsidMask"])

    @PbbIsidMask.setter
    def PbbIsidMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbIsidMask"], value)

    @property
    def TunnelIdMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Tunnel ID Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelIdMask"])

    @TunnelIdMask.setter
    def TunnelIdMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TunnelIdMask"], value)

    @property
    def VlanMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, VLAN Mask matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanMask"])

    @VlanMask.setter
    def VlanMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanMask"], value)

    def update(
        self,
        ArpDestinationIpv4AddressMask=None,
        ArpDstHwAddressMask=None,
        ArpSourceIpv4AddressMask=None,
        ArpSrcHwAddressMask=None,
        EthernetDestinationMask=None,
        EthernetSourceMask=None,
        Ipv4DestinationMask=None,
        Ipv4SourceMask=None,
        Ipv6DestinationMask=None,
        Ipv6ExtHeaderMask=None,
        Ipv6FlowLabelMask=None,
        Ipv6SourceMask=None,
        MetadataMask=None,
        PbbIsidMask=None,
        TunnelIdMask=None,
        VlanMask=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> MatchMask
        """Updates matchMask resource on the server.

        Args
        ----
        - ArpDestinationIpv4AddressMask (bool): If selected, ARP Destination IPv4 Address Mask matching is supported.
        - ArpDstHwAddressMask (bool): If selected, ARP Destination Hardware Address Mask matching is supported.
        - ArpSourceIpv4AddressMask (bool): If selected, ARP Source IPv4 Address Mask matching is supported.
        - ArpSrcHwAddressMask (bool): If selected, ARP Source Hardware Address Mask matching is supported.
        - EthernetDestinationMask (bool): If selected, Ethernet Destination Mask matching is supported.
        - EthernetSourceMask (bool): If selected, Ethernet Source Mask matching is supported.
        - Ipv4DestinationMask (bool): If selected, IPv4 Destination Mask matching is supported.
        - Ipv4SourceMask (bool): If selected, IPv4 Source Mask matching is supported.
        - Ipv6DestinationMask (bool): If selected, IPv6 Destination Mask matching is supported.
        - Ipv6ExtHeaderMask (bool): If selected, IPv6 Ext Header Mask matching is supported.
        - Ipv6FlowLabelMask (bool): If selected, IPv6 Flow Label Mask matching is supported.
        - Ipv6SourceMask (bool): If selected, IPv6 Source Mask matching is supported.
        - MetadataMask (bool): If selected, MetaData Mask matching is supported.
        - PbbIsidMask (bool): If selected, Tunnel ID Mask matching is supported.
        - TunnelIdMask (bool): If selected, Tunnel ID Mask matching is supported.
        - VlanMask (bool): If selected, VLAN Mask matching is supported.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ArpDestinationIpv4AddressMask=None,
        ArpDstHwAddressMask=None,
        ArpSourceIpv4AddressMask=None,
        ArpSrcHwAddressMask=None,
        EthernetDestinationMask=None,
        EthernetSourceMask=None,
        Ipv4DestinationMask=None,
        Ipv4SourceMask=None,
        Ipv6DestinationMask=None,
        Ipv6ExtHeaderMask=None,
        Ipv6FlowLabelMask=None,
        Ipv6SourceMask=None,
        MetadataMask=None,
        PbbIsidMask=None,
        TunnelIdMask=None,
        VlanMask=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> MatchMask
        """Finds and retrieves matchMask resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve matchMask resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all matchMask resources from the server.

        Args
        ----
        - ArpDestinationIpv4AddressMask (bool): If selected, ARP Destination IPv4 Address Mask matching is supported.
        - ArpDstHwAddressMask (bool): If selected, ARP Destination Hardware Address Mask matching is supported.
        - ArpSourceIpv4AddressMask (bool): If selected, ARP Source IPv4 Address Mask matching is supported.
        - ArpSrcHwAddressMask (bool): If selected, ARP Source Hardware Address Mask matching is supported.
        - EthernetDestinationMask (bool): If selected, Ethernet Destination Mask matching is supported.
        - EthernetSourceMask (bool): If selected, Ethernet Source Mask matching is supported.
        - Ipv4DestinationMask (bool): If selected, IPv4 Destination Mask matching is supported.
        - Ipv4SourceMask (bool): If selected, IPv4 Source Mask matching is supported.
        - Ipv6DestinationMask (bool): If selected, IPv6 Destination Mask matching is supported.
        - Ipv6ExtHeaderMask (bool): If selected, IPv6 Ext Header Mask matching is supported.
        - Ipv6FlowLabelMask (bool): If selected, IPv6 Flow Label Mask matching is supported.
        - Ipv6SourceMask (bool): If selected, IPv6 Source Mask matching is supported.
        - MetadataMask (bool): If selected, MetaData Mask matching is supported.
        - PbbIsidMask (bool): If selected, Tunnel ID Mask matching is supported.
        - TunnelIdMask (bool): If selected, Tunnel ID Mask matching is supported.
        - VlanMask (bool): If selected, VLAN Mask matching is supported.

        Returns
        -------
        - self: This instance with matching matchMask resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of matchMask data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the matchMask resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
