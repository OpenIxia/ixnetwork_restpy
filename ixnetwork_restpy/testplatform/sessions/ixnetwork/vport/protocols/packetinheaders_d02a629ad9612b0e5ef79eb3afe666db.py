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


class PacketInHeaders(Base):
    """This object allows to configure the packet-in parameters.
    The PacketInHeaders class encapsulates a required packetInHeaders resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'packetInHeaders'

    def __init__(self, parent):
        super(PacketInHeaders, self).__init__(parent)

    @property
    def EthernetDestinationAddress(self):
        """Indicates the Ethernet destination address for the packet.

        Returns:
            str
        """
        return self._get_attribute('ethernetDestinationAddress')
    @EthernetDestinationAddress.setter
    def EthernetDestinationAddress(self, value):
        self._set_attribute('ethernetDestinationAddress', value)

    @property
    def EthernetSourceAddress(self):
        """Indicates the ethernet address of the source from which this packet arrived.

        Returns:
            str
        """
        return self._get_attribute('ethernetSourceAddress')
    @EthernetSourceAddress.setter
    def EthernetSourceAddress(self, value):
        self._set_attribute('ethernetSourceAddress', value)

    @property
    def EthernetType(self):
        """Indicates the ethernet frame type.

        Returns:
            str
        """
        return self._get_attribute('ethernetType')
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute('ethernetType', value)

    @property
    def Ipv4DestinationAddress(self):
        """Indicates the IPv4 destination address for this packet.

        Returns:
            str
        """
        return self._get_attribute('ipv4DestinationAddress')
    @Ipv4DestinationAddress.setter
    def Ipv4DestinationAddress(self, value):
        self._set_attribute('ipv4DestinationAddress', value)

    @property
    def Ipv4Protocol(self):
        """Defines the protocol used in the data portion of the IP datagram.

        Returns:
            str
        """
        return self._get_attribute('ipv4Protocol')
    @Ipv4Protocol.setter
    def Ipv4Protocol(self, value):
        self._set_attribute('ipv4Protocol', value)

    @property
    def Ipv4SourceAddress(self):
        """Indicates the IPv4 address of the source from which this packet arrived.

        Returns:
            str
        """
        return self._get_attribute('ipv4SourceAddress')
    @Ipv4SourceAddress.setter
    def Ipv4SourceAddress(self, value):
        self._set_attribute('ipv4SourceAddress', value)

    @property
    def Ipv6DestinationAddress(self):
        """Indicates the IPv6 destination address for this packet.

        Returns:
            str
        """
        return self._get_attribute('ipv6DestinationAddress')
    @Ipv6DestinationAddress.setter
    def Ipv6DestinationAddress(self, value):
        self._set_attribute('ipv6DestinationAddress', value)

    @property
    def Ipv6FlowLabel(self):
        """Originally created for giving real-time applications special service.The flow label when set to a non-zero value now serves as a hint to routers and switches with multiple outbound paths that these packets should stay on the same path so that they will not be re-ordered.

        Returns:
            str
        """
        return self._get_attribute('ipv6FlowLabel')
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute('ipv6FlowLabel', value)

    @property
    def Ipv6SourceAddress(self):
        """Indicates the IPv6 address of the source from which this packet arrived.

        Returns:
            str
        """
        return self._get_attribute('ipv6SourceAddress')
    @Ipv6SourceAddress.setter
    def Ipv6SourceAddress(self, value):
        self._set_attribute('ipv6SourceAddress', value)

    @property
    def TcpDestinationPort(self):
        """Identifies the TCP port number of the destination application program.

        Returns:
            str
        """
        return self._get_attribute('tcpDestinationPort')
    @TcpDestinationPort.setter
    def TcpDestinationPort(self, value):
        self._set_attribute('tcpDestinationPort', value)

    @property
    def TcpSourcePort(self):
        """Identifies the TCP port number of the source application program.

        Returns:
            str
        """
        return self._get_attribute('tcpSourcePort')
    @TcpSourcePort.setter
    def TcpSourcePort(self, value):
        self._set_attribute('tcpSourcePort', value)

    @property
    def UdpDestinationPort(self):
        """Identifies the UDP port number of the destination application program.

        Returns:
            str
        """
        return self._get_attribute('udpDestinationPort')
    @UdpDestinationPort.setter
    def UdpDestinationPort(self, value):
        self._set_attribute('udpDestinationPort', value)

    @property
    def UdpSourcePort(self):
        """Identifies the UDP port number of the source application program.

        Returns:
            str
        """
        return self._get_attribute('udpSourcePort')
    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        self._set_attribute('udpSourcePort', value)

    @property
    def UniquePacketCount(self):
        """Indicates the packet-in count in this Range.

        Returns:
            str
        """
        return self._get_attribute('uniquePacketCount')

    @property
    def VlanId(self):
        """Indicates the field specifying the VLAN to which the frame belongs.

        Returns:
            str
        """
        return self._get_attribute('vlanId')
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute('vlanId', value)

    @property
    def VlanPriority(self):
        """Indicates the frame priority level.

        Returns:
            str
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, EthernetDestinationAddress=None, EthernetSourceAddress=None, EthernetType=None, Ipv4DestinationAddress=None, Ipv4Protocol=None, Ipv4SourceAddress=None, Ipv6DestinationAddress=None, Ipv6FlowLabel=None, Ipv6SourceAddress=None, TcpDestinationPort=None, TcpSourcePort=None, UdpDestinationPort=None, UdpSourcePort=None, VlanId=None, VlanPriority=None):
        """Updates a child instance of packetInHeaders on the server.

        Args:
            EthernetDestinationAddress (str): Indicates the Ethernet destination address for the packet.
            EthernetSourceAddress (str): Indicates the ethernet address of the source from which this packet arrived.
            EthernetType (str): Indicates the ethernet frame type.
            Ipv4DestinationAddress (str): Indicates the IPv4 destination address for this packet.
            Ipv4Protocol (str): Defines the protocol used in the data portion of the IP datagram.
            Ipv4SourceAddress (str): Indicates the IPv4 address of the source from which this packet arrived.
            Ipv6DestinationAddress (str): Indicates the IPv6 destination address for this packet.
            Ipv6FlowLabel (str): Originally created for giving real-time applications special service.The flow label when set to a non-zero value now serves as a hint to routers and switches with multiple outbound paths that these packets should stay on the same path so that they will not be re-ordered.
            Ipv6SourceAddress (str): Indicates the IPv6 address of the source from which this packet arrived.
            TcpDestinationPort (str): Identifies the TCP port number of the destination application program.
            TcpSourcePort (str): Identifies the TCP port number of the source application program.
            UdpDestinationPort (str): Identifies the UDP port number of the destination application program.
            UdpSourcePort (str): Identifies the UDP port number of the source application program.
            VlanId (str): Indicates the field specifying the VLAN to which the frame belongs.
            VlanPriority (str): Indicates the frame priority level.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
