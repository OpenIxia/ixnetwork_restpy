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


class PacketInHeaders(Base):
    """This object allows to configure the packet-in parameters.
    The PacketInHeaders class encapsulates a required packetInHeaders resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "packetInHeaders"
    _SDM_ATT_MAP = {
        "EthernetDestinationAddress": "ethernetDestinationAddress",
        "EthernetSourceAddress": "ethernetSourceAddress",
        "EthernetType": "ethernetType",
        "Ipv4DestinationAddress": "ipv4DestinationAddress",
        "Ipv4Protocol": "ipv4Protocol",
        "Ipv4SourceAddress": "ipv4SourceAddress",
        "Ipv6DestinationAddress": "ipv6DestinationAddress",
        "Ipv6FlowLabel": "ipv6FlowLabel",
        "Ipv6SourceAddress": "ipv6SourceAddress",
        "TcpDestinationPort": "tcpDestinationPort",
        "TcpSourcePort": "tcpSourcePort",
        "UdpDestinationPort": "udpDestinationPort",
        "UdpSourcePort": "udpSourcePort",
        "UniquePacketCount": "uniquePacketCount",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PacketInHeaders, self).__init__(parent, list_op)

    @property
    def EthernetDestinationAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the Ethernet destination address for the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestinationAddress"])

    @EthernetDestinationAddress.setter
    def EthernetDestinationAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetDestinationAddress"], value)

    @property
    def EthernetSourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the ethernet address of the source from which this packet arrived.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSourceAddress"])

    @EthernetSourceAddress.setter
    def EthernetSourceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetSourceAddress"], value)

    @property
    def EthernetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the ethernet frame type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @EthernetType.setter
    def EthernetType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetType"], value)

    @property
    def Ipv4DestinationAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the IPv4 destination address for this packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4DestinationAddress"])

    @Ipv4DestinationAddress.setter
    def Ipv4DestinationAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4DestinationAddress"], value)

    @property
    def Ipv4Protocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the protocol used in the data portion of the IP datagram.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Protocol"])

    @Ipv4Protocol.setter
    def Ipv4Protocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Protocol"], value)

    @property
    def Ipv4SourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the IPv4 address of the source from which this packet arrived.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceAddress"])

    @Ipv4SourceAddress.setter
    def Ipv4SourceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4SourceAddress"], value)

    @property
    def Ipv6DestinationAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the IPv6 destination address for this packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6DestinationAddress"])

    @Ipv6DestinationAddress.setter
    def Ipv6DestinationAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6DestinationAddress"], value)

    @property
    def Ipv6FlowLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Originally created for giving real-time applications special service.The flow label when set to a non-zero value now serves as a hint to routers and switches with multiple outbound paths that these packets should stay on the same path so that they will not be re-ordered.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"])

    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"], value)

    @property
    def Ipv6SourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the IPv6 address of the source from which this packet arrived.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceAddress"])

    @Ipv6SourceAddress.setter
    def Ipv6SourceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6SourceAddress"], value)

    @property
    def TcpDestinationPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identifies the TCP port number of the destination application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpDestinationPort"])

    @TcpDestinationPort.setter
    def TcpDestinationPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpDestinationPort"], value)

    @property
    def TcpSourcePort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identifies the TCP port number of the source application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpSourcePort"])

    @TcpSourcePort.setter
    def TcpSourcePort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpSourcePort"], value)

    @property
    def UdpDestinationPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identifies the UDP port number of the destination application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpDestinationPort"])

    @UdpDestinationPort.setter
    def UdpDestinationPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpDestinationPort"], value)

    @property
    def UdpSourcePort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identifies the UDP port number of the source application program.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSourcePort"])

    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpSourcePort"], value)

    @property
    def UniquePacketCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the packet-in count in this Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UniquePacketCount"])

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the field specifying the VLAN to which the frame belongs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the frame priority level.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        EthernetDestinationAddress=None,
        EthernetSourceAddress=None,
        EthernetType=None,
        Ipv4DestinationAddress=None,
        Ipv4Protocol=None,
        Ipv4SourceAddress=None,
        Ipv6DestinationAddress=None,
        Ipv6FlowLabel=None,
        Ipv6SourceAddress=None,
        TcpDestinationPort=None,
        TcpSourcePort=None,
        UdpDestinationPort=None,
        UdpSourcePort=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, str, str, str) -> PacketInHeaders
        """Updates packetInHeaders resource on the server.

        Args
        ----
        - EthernetDestinationAddress (str): Indicates the Ethernet destination address for the packet.
        - EthernetSourceAddress (str): Indicates the ethernet address of the source from which this packet arrived.
        - EthernetType (str): Indicates the ethernet frame type.
        - Ipv4DestinationAddress (str): Indicates the IPv4 destination address for this packet.
        - Ipv4Protocol (str): Defines the protocol used in the data portion of the IP datagram.
        - Ipv4SourceAddress (str): Indicates the IPv4 address of the source from which this packet arrived.
        - Ipv6DestinationAddress (str): Indicates the IPv6 destination address for this packet.
        - Ipv6FlowLabel (str): Originally created for giving real-time applications special service.The flow label when set to a non-zero value now serves as a hint to routers and switches with multiple outbound paths that these packets should stay on the same path so that they will not be re-ordered.
        - Ipv6SourceAddress (str): Indicates the IPv6 address of the source from which this packet arrived.
        - TcpDestinationPort (str): Identifies the TCP port number of the destination application program.
        - TcpSourcePort (str): Identifies the TCP port number of the source application program.
        - UdpDestinationPort (str): Identifies the UDP port number of the destination application program.
        - UdpSourcePort (str): Identifies the UDP port number of the source application program.
        - VlanId (str): Indicates the field specifying the VLAN to which the frame belongs.
        - VlanPriority (str): Indicates the frame priority level.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EthernetDestinationAddress=None,
        EthernetSourceAddress=None,
        EthernetType=None,
        Ipv4DestinationAddress=None,
        Ipv4Protocol=None,
        Ipv4SourceAddress=None,
        Ipv6DestinationAddress=None,
        Ipv6FlowLabel=None,
        Ipv6SourceAddress=None,
        TcpDestinationPort=None,
        TcpSourcePort=None,
        UdpDestinationPort=None,
        UdpSourcePort=None,
        UniquePacketCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str) -> PacketInHeaders
        """Finds and retrieves packetInHeaders resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve packetInHeaders resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all packetInHeaders resources from the server.

        Args
        ----
        - EthernetDestinationAddress (str): Indicates the Ethernet destination address for the packet.
        - EthernetSourceAddress (str): Indicates the ethernet address of the source from which this packet arrived.
        - EthernetType (str): Indicates the ethernet frame type.
        - Ipv4DestinationAddress (str): Indicates the IPv4 destination address for this packet.
        - Ipv4Protocol (str): Defines the protocol used in the data portion of the IP datagram.
        - Ipv4SourceAddress (str): Indicates the IPv4 address of the source from which this packet arrived.
        - Ipv6DestinationAddress (str): Indicates the IPv6 destination address for this packet.
        - Ipv6FlowLabel (str): Originally created for giving real-time applications special service.The flow label when set to a non-zero value now serves as a hint to routers and switches with multiple outbound paths that these packets should stay on the same path so that they will not be re-ordered.
        - Ipv6SourceAddress (str): Indicates the IPv6 address of the source from which this packet arrived.
        - TcpDestinationPort (str): Identifies the TCP port number of the destination application program.
        - TcpSourcePort (str): Identifies the TCP port number of the source application program.
        - UdpDestinationPort (str): Identifies the UDP port number of the destination application program.
        - UdpSourcePort (str): Identifies the UDP port number of the source application program.
        - UniquePacketCount (str): Indicates the packet-in count in this Range.
        - VlanId (str): Indicates the field specifying the VLAN to which the frame belongs.
        - VlanPriority (str): Indicates the frame priority level.

        Returns
        -------
        - self: This instance with matching packetInHeaders resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of packetInHeaders data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the packetInHeaders resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
