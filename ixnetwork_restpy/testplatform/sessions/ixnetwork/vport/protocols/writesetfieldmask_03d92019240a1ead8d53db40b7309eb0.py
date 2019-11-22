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


class WriteSetFieldMask(Base):
    """Select the type of Write Set Field Mask capability that the table will support.
    The WriteSetFieldMask class encapsulates a required writeSetFieldMask resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'writeSetFieldMask'

    def __init__(self, parent):
        super(WriteSetFieldMask, self).__init__(parent)

    @property
    def ArpDestinationIpv4AddressMask(self):
        """If selected, Write Set Field for ARP Destination IPv4 Address Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('arpDestinationIpv4AddressMask')
    @ArpDestinationIpv4AddressMask.setter
    def ArpDestinationIpv4AddressMask(self, value):
        self._set_attribute('arpDestinationIpv4AddressMask', value)

    @property
    def ArpDstHwAddressMask(self):
        """If selected, Write Set Field for ARP Destination Hardware Address Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('arpDstHwAddressMask')
    @ArpDstHwAddressMask.setter
    def ArpDstHwAddressMask(self, value):
        self._set_attribute('arpDstHwAddressMask', value)

    @property
    def ArpSourceIpv4AddressMask(self):
        """If selected, Write Set Field for ARP Source IPv4 Address Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('arpSourceIpv4AddressMask')
    @ArpSourceIpv4AddressMask.setter
    def ArpSourceIpv4AddressMask(self, value):
        self._set_attribute('arpSourceIpv4AddressMask', value)

    @property
    def ArpSrcHwAddressMask(self):
        """If selected, Write Set Field for ARP Source Hardware Address Mask is supported

        Returns:
            bool
        """
        return self._get_attribute('arpSrcHwAddressMask')
    @ArpSrcHwAddressMask.setter
    def ArpSrcHwAddressMask(self, value):
        self._set_attribute('arpSrcHwAddressMask', value)

    @property
    def EthernetDestinationMask(self):
        """If selected, Write Set Field for Ethernet Destination Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ethernetDestinationMask')
    @EthernetDestinationMask.setter
    def EthernetDestinationMask(self, value):
        self._set_attribute('ethernetDestinationMask', value)

    @property
    def EthernetSourceMask(self):
        """If selected, Write Set Field for Ethernet Source Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ethernetSourceMask')
    @EthernetSourceMask.setter
    def EthernetSourceMask(self, value):
        self._set_attribute('ethernetSourceMask', value)

    @property
    def Ipv4DestinationMask(self):
        """If selected, Write Set Field for IPv4 Destination Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ipv4DestinationMask')
    @Ipv4DestinationMask.setter
    def Ipv4DestinationMask(self, value):
        self._set_attribute('ipv4DestinationMask', value)

    @property
    def Ipv4SourceMask(self):
        """If selected, Write Set Field for IPv4 Source Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ipv4SourceMask')
    @Ipv4SourceMask.setter
    def Ipv4SourceMask(self, value):
        self._set_attribute('ipv4SourceMask', value)

    @property
    def Ipv6DestinationMask(self):
        """If selected, Write Set Field for IPv6 Destination Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ipv6DestinationMask')
    @Ipv6DestinationMask.setter
    def Ipv6DestinationMask(self, value):
        self._set_attribute('ipv6DestinationMask', value)

    @property
    def Ipv6ExtHeaderMask(self):
        """If selected, Write Set Field for IPv6 Ext Header Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ipv6ExtHeaderMask')
    @Ipv6ExtHeaderMask.setter
    def Ipv6ExtHeaderMask(self, value):
        self._set_attribute('ipv6ExtHeaderMask', value)

    @property
    def Ipv6FlowLabelMask(self):
        """If selected, Write Set Field for IPv6 Flow Label Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ipv6FlowLabelMask')
    @Ipv6FlowLabelMask.setter
    def Ipv6FlowLabelMask(self, value):
        self._set_attribute('ipv6FlowLabelMask', value)

    @property
    def Ipv6SourceMask(self):
        """If selected, Write Set Field for IPv6 Source Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('ipv6SourceMask')
    @Ipv6SourceMask.setter
    def Ipv6SourceMask(self, value):
        self._set_attribute('ipv6SourceMask', value)

    @property
    def PbbIsidMask(self):
        """If selected, Write Set Field for PBB ISID Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('pbbIsidMask')
    @PbbIsidMask.setter
    def PbbIsidMask(self, value):
        self._set_attribute('pbbIsidMask', value)

    @property
    def TunnelIdMask(self):
        """If selected, Write Set Field for Tunnel ID Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('tunnelIdMask')
    @TunnelIdMask.setter
    def TunnelIdMask(self, value):
        self._set_attribute('tunnelIdMask', value)

    @property
    def VlanMask(self):
        """If selected, Write Set Field for VLAN Mask is supported.

        Returns:
            bool
        """
        return self._get_attribute('vlanMask')
    @VlanMask.setter
    def VlanMask(self, value):
        self._set_attribute('vlanMask', value)

    def update(self, ArpDestinationIpv4AddressMask=None, ArpDstHwAddressMask=None, ArpSourceIpv4AddressMask=None, ArpSrcHwAddressMask=None, EthernetDestinationMask=None, EthernetSourceMask=None, Ipv4DestinationMask=None, Ipv4SourceMask=None, Ipv6DestinationMask=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabelMask=None, Ipv6SourceMask=None, PbbIsidMask=None, TunnelIdMask=None, VlanMask=None):
        """Updates a child instance of writeSetFieldMask on the server.

        Args:
            ArpDestinationIpv4AddressMask (bool): If selected, Write Set Field for ARP Destination IPv4 Address Mask is supported.
            ArpDstHwAddressMask (bool): If selected, Write Set Field for ARP Destination Hardware Address Mask is supported.
            ArpSourceIpv4AddressMask (bool): If selected, Write Set Field for ARP Source IPv4 Address Mask is supported.
            ArpSrcHwAddressMask (bool): If selected, Write Set Field for ARP Source Hardware Address Mask is supported
            EthernetDestinationMask (bool): If selected, Write Set Field for Ethernet Destination Mask is supported.
            EthernetSourceMask (bool): If selected, Write Set Field for Ethernet Source Mask is supported.
            Ipv4DestinationMask (bool): If selected, Write Set Field for IPv4 Destination Mask is supported.
            Ipv4SourceMask (bool): If selected, Write Set Field for IPv4 Source Mask is supported.
            Ipv6DestinationMask (bool): If selected, Write Set Field for IPv6 Destination Mask is supported.
            Ipv6ExtHeaderMask (bool): If selected, Write Set Field for IPv6 Ext Header Mask is supported.
            Ipv6FlowLabelMask (bool): If selected, Write Set Field for IPv6 Flow Label Mask is supported.
            Ipv6SourceMask (bool): If selected, Write Set Field for IPv6 Source Mask is supported.
            PbbIsidMask (bool): If selected, Write Set Field for PBB ISID Mask is supported.
            TunnelIdMask (bool): If selected, Write Set Field for Tunnel ID Mask is supported.
            VlanMask (bool): If selected, Write Set Field for VLAN Mask is supported.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
