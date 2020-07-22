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


class PacketInHeaders(Base):
    """This object allows to configure the packet-in parameters.
    The PacketInHeaders class encapsulates a required packetInHeaders resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'packetInHeaders'
    _SDM_ATT_MAP = {
        'EthernetDestinationAddress': 'ethernetDestinationAddress',
        'EthernetSourceAddress': 'ethernetSourceAddress',
        'EthernetType': 'ethernetType',
        'Ipv4DestinationAddress': 'ipv4DestinationAddress',
        'Ipv4Protocol': 'ipv4Protocol',
        'Ipv4SourceAddress': 'ipv4SourceAddress',
        'Ipv6DestinationAddress': 'ipv6DestinationAddress',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'Ipv6SourceAddress': 'ipv6SourceAddress',
        'TcpDestinationPort': 'tcpDestinationPort',
        'TcpSourcePort': 'tcpSourcePort',
        'UdpDestinationPort': 'udpDestinationPort',
        'UdpSourcePort': 'udpSourcePort',
        'UniquePacketCount': 'uniquePacketCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(PacketInHeaders, self).__init__(parent)

    @property
    def EthernetDestinationAddress(self):
        """
        Returns
        -------
        - str: Indicates the Ethernet destination address for the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestinationAddress'])

    @property
    def EthernetSourceAddress(self):
        """
        Returns
        -------
        - str: Indicates the ethernet address of the source from which this packet arrived.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSourceAddress'])

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: Indicates the ethernet frame type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])

    @property
    def Ipv4DestinationAddress(self):
        """
        Returns
        -------
        - str: Indicates the IPv4 destination address for this packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4DestinationAddress'])

    @property
    def Ipv4Protocol(self):
        """
        Returns
        -------
        - str: Defines the protocol used in the data portion of the IP datagram.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Protocol'])

    @property
    def Ipv4SourceAddress(self):
        """
        Returns
        -------
        - str: Indicates the IPv4 address of the source from which this packet arrived.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4SourceAddress'])

    @property
    def Ipv6DestinationAddress(self):
        """
        Returns
        -------
        - str: Indicates the IPv6 destination address for this packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6DestinationAddress'])

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: Originally created for giving real-time applications special service.The flow label when set to a non-zero value now serves as a hint to routers and switches with multiple outbound paths that these packets should stay on the same path so that they will not be re-ordered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])

    @property
    def Ipv6SourceAddress(self):
        """
        Returns
        -------
        - str: Indicates the IPv6 address of the source from which this packet arrived.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6SourceAddress'])

    @property
    def TcpDestinationPort(self):
        """
        Returns
        -------
        - str: Identifies the TCP port number of the destination application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpDestinationPort'])

    @property
    def TcpSourcePort(self):
        """
        Returns
        -------
        - str: Identifies the TCP port number of the source application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpSourcePort'])

    @property
    def UdpDestinationPort(self):
        """
        Returns
        -------
        - str: Identifies the UDP port number of the destination application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestinationPort'])

    @property
    def UdpSourcePort(self):
        """
        Returns
        -------
        - str: Identifies the UDP port number of the source application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSourcePort'])

    @property
    def UniquePacketCount(self):
        """
        Returns
        -------
        - str: Indicates the packet-in count in this Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UniquePacketCount'])

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: Indicates the field specifying the VLAN to which the frame belongs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: Indicates the frame priority level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
