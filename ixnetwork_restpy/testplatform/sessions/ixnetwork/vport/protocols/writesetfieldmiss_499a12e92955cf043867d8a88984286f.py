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


class WriteSetFieldMiss(Base):
    """Select the type of Write Set Field Miss capability that the table miss flow entry will support.
    The WriteSetFieldMiss class encapsulates a required writeSetFieldMiss resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "writeSetFieldMiss"
    _SDM_ATT_MAP = {
        "ArpDestinationHardwareAddress": "arpDestinationHardwareAddress",
        "ArpDestinationIpv4Address": "arpDestinationIpv4Address",
        "ArpOpcode": "arpOpcode",
        "ArpSourceHardwareAddress": "arpSourceHardwareAddress",
        "ArpSourceIpv4Address": "arpSourceIpv4Address",
        "EthernetDestination": "ethernetDestination",
        "EthernetSource": "ethernetSource",
        "EthernetType": "ethernetType",
        "IcmpCode": "icmpCode",
        "IcmpType": "icmpType",
        "Icmpv6Code": "icmpv6Code",
        "Icmpv6Type": "icmpv6Type",
        "IpDscp": "ipDscp",
        "IpEcn": "ipEcn",
        "IpProtocol": "ipProtocol",
        "Ipv4Destination": "ipv4Destination",
        "Ipv4Source": "ipv4Source",
        "Ipv6Destination": "ipv6Destination",
        "Ipv6ExtHeader": "ipv6ExtHeader",
        "Ipv6FlowLabel": "ipv6FlowLabel",
        "Ipv6NdSll": "ipv6NdSll",
        "Ipv6NdTarget": "ipv6NdTarget",
        "Ipv6NdTll": "ipv6NdTll",
        "Ipv6Source": "ipv6Source",
        "MplsBos": "mplsBos",
        "MplsLabel": "mplsLabel",
        "MplsTc": "mplsTc",
        "PbbIsid": "pbbIsid",
        "SctpDestination": "sctpDestination",
        "SctpSource": "sctpSource",
        "TcpDestination": "tcpDestination",
        "TcpSource": "tcpSource",
        "TunnelId": "tunnelId",
        "UdpDestination": "udpDestination",
        "UdpSource": "udpSource",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(WriteSetFieldMiss, self).__init__(parent, list_op)

    @property
    def ArpDestinationHardwareAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ARP Destination Hardware Address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDestinationHardwareAddress"])

    @ArpDestinationHardwareAddress.setter
    def ArpDestinationHardwareAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpDestinationHardwareAddress"], value)

    @property
    def ArpDestinationIpv4Address(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ARP Destination IPv4 Address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDestinationIpv4Address"])

    @ArpDestinationIpv4Address.setter
    def ArpDestinationIpv4Address(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpDestinationIpv4Address"], value)

    @property
    def ArpOpcode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ARP Opcode is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpOpcode"])

    @ArpOpcode.setter
    def ArpOpcode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpOpcode"], value)

    @property
    def ArpSourceHardwareAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ARP Source Hardware Address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSourceHardwareAddress"])

    @ArpSourceHardwareAddress.setter
    def ArpSourceHardwareAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpSourceHardwareAddress"], value)

    @property
    def ArpSourceIpv4Address(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ARP Source IPv4 Address is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSourceIpv4Address"])

    @ArpSourceIpv4Address.setter
    def ArpSourceIpv4Address(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpSourceIpv4Address"], value)

    @property
    def EthernetDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for Ethernet Destination is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestination"])

    @EthernetDestination.setter
    def EthernetDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetDestination"], value)

    @property
    def EthernetSource(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for Ethernet Source is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSource"])

    @EthernetSource.setter
    def EthernetSource(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetSource"], value)

    @property
    def EthernetType(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for Ethernet Type is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @EthernetType.setter
    def EthernetType(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetType"], value)

    @property
    def IcmpCode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ICMP Code is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IcmpCode"])

    @IcmpCode.setter
    def IcmpCode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IcmpCode"], value)

    @property
    def IcmpType(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ICMP Type is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IcmpType"])

    @IcmpType.setter
    def IcmpType(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IcmpType"], value)

    @property
    def Icmpv6Code(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ICMPv6 Code is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Code"])

    @Icmpv6Code.setter
    def Icmpv6Code(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Icmpv6Code"], value)

    @property
    def Icmpv6Type(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for ICMPv6 Type is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Type"])

    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Icmpv6Type"], value)

    @property
    def IpDscp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IP DSCP is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDscp"])

    @IpDscp.setter
    def IpDscp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpDscp"], value)

    @property
    def IpEcn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IP ECN is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpEcn"])

    @IpEcn.setter
    def IpEcn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpEcn"], value)

    @property
    def IpProtocol(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IP Protocol is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpProtocol"])

    @IpProtocol.setter
    def IpProtocol(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpProtocol"], value)

    @property
    def Ipv4Destination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv4 Destination is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Destination"])

    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Destination"], value)

    @property
    def Ipv4Source(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv4 Source is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Source"])

    @Ipv4Source.setter
    def Ipv4Source(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Source"], value)

    @property
    def Ipv6Destination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 Destination is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Destination"])

    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Destination"], value)

    @property
    def Ipv6ExtHeader(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 Ext Header is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6ExtHeader"])

    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6ExtHeader"], value)

    @property
    def Ipv6FlowLabel(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 Flow Label is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"])

    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"], value)

    @property
    def Ipv6NdSll(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 ND SLL is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdSll"])

    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NdSll"], value)

    @property
    def Ipv6NdTarget(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 ND Target is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdTarget"])

    @Ipv6NdTarget.setter
    def Ipv6NdTarget(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NdTarget"], value)

    @property
    def Ipv6NdTll(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 ND TLL is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdTll"])

    @Ipv6NdTll.setter
    def Ipv6NdTll(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NdTll"], value)

    @property
    def Ipv6Source(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for IPv6 Source is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Source"])

    @Ipv6Source.setter
    def Ipv6Source(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Source"], value)

    @property
    def MplsBos(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for MPLS BoS is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsBos"])

    @MplsBos.setter
    def MplsBos(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsBos"], value)

    @property
    def MplsLabel(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for MPLS Label is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabel"])

    @MplsLabel.setter
    def MplsLabel(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsLabel"], value)

    @property
    def MplsTc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for MPLS TC is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsTc"])

    @MplsTc.setter
    def MplsTc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsTc"], value)

    @property
    def PbbIsid(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for PBB ISID is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsid"])

    @PbbIsid.setter
    def PbbIsid(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbIsid"], value)

    @property
    def SctpDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for SCTP Destination is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SctpDestination"])

    @SctpDestination.setter
    def SctpDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SctpDestination"], value)

    @property
    def SctpSource(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for SCTP Source is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SctpSource"])

    @SctpSource.setter
    def SctpSource(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SctpSource"], value)

    @property
    def TcpDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for TCP Destination is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpDestination"])

    @TcpDestination.setter
    def TcpDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpDestination"], value)

    @property
    def TcpSource(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for TCP Source is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpSource"])

    @TcpSource.setter
    def TcpSource(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpSource"], value)

    @property
    def TunnelId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for Tunnel ID is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelId"])

    @TunnelId.setter
    def TunnelId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TunnelId"], value)

    @property
    def UdpDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for UDP Destination is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpDestination"])

    @UdpDestination.setter
    def UdpDestination(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpDestination"], value)

    @property
    def UdpSource(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for UDP Source is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSource"])

    @UdpSource.setter
    def UdpSource(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpSource"], value)

    @property
    def VlanId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for VLAN ID is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Write Set Field Miss for VLAN Priority is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        ArpDestinationHardwareAddress=None,
        ArpDestinationIpv4Address=None,
        ArpOpcode=None,
        ArpSourceHardwareAddress=None,
        ArpSourceIpv4Address=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        IcmpCode=None,
        IcmpType=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
        IpDscp=None,
        IpEcn=None,
        IpProtocol=None,
        Ipv4Destination=None,
        Ipv4Source=None,
        Ipv6Destination=None,
        Ipv6ExtHeader=None,
        Ipv6FlowLabel=None,
        Ipv6NdSll=None,
        Ipv6NdTarget=None,
        Ipv6NdTll=None,
        Ipv6Source=None,
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        PbbIsid=None,
        SctpDestination=None,
        SctpSource=None,
        TcpDestination=None,
        TcpSource=None,
        TunnelId=None,
        UdpDestination=None,
        UdpSource=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> WriteSetFieldMiss
        """Updates writeSetFieldMiss resource on the server.

        Args
        ----
        - ArpDestinationHardwareAddress (bool): If selected, Write Set Field Miss for ARP Destination Hardware Address is supported.
        - ArpDestinationIpv4Address (bool): If selected, Write Set Field Miss for ARP Destination IPv4 Address is supported.
        - ArpOpcode (bool): If selected, Write Set Field Miss for ARP Opcode is supported.
        - ArpSourceHardwareAddress (bool): If selected, Write Set Field Miss for ARP Source Hardware Address is supported.
        - ArpSourceIpv4Address (bool): If selected, Write Set Field Miss for ARP Source IPv4 Address is supported.
        - EthernetDestination (bool): If selected, Write Set Field Miss for Ethernet Destination is supported.
        - EthernetSource (bool): If selected, Write Set Field Miss for Ethernet Source is supported.
        - EthernetType (bool): If selected, Write Set Field Miss for Ethernet Type is supported.
        - IcmpCode (bool): If selected, Write Set Field Miss for ICMP Code is supported.
        - IcmpType (bool): If selected, Write Set Field Miss for ICMP Type is supported.
        - Icmpv6Code (bool): If selected, Write Set Field Miss for ICMPv6 Code is supported.
        - Icmpv6Type (bool): If selected, Write Set Field Miss for ICMPv6 Type is supported.
        - IpDscp (bool): If selected, Write Set Field Miss for IP DSCP is supported.
        - IpEcn (bool): If selected, Write Set Field Miss for IP ECN is supported.
        - IpProtocol (bool): If selected, Write Set Field Miss for IP Protocol is supported.
        - Ipv4Destination (bool): If selected, Write Set Field Miss for IPv4 Destination is supported.
        - Ipv4Source (bool): If selected, Write Set Field Miss for IPv4 Source is supported.
        - Ipv6Destination (bool): If selected, Write Set Field Miss for IPv6 Destination is supported.
        - Ipv6ExtHeader (bool): If selected, Write Set Field Miss for IPv6 Ext Header is supported.
        - Ipv6FlowLabel (bool): If selected, Write Set Field Miss for IPv6 Flow Label is supported.
        - Ipv6NdSll (bool): If selected, Write Set Field Miss for IPv6 ND SLL is supported.
        - Ipv6NdTarget (bool): If selected, Write Set Field Miss for IPv6 ND Target is supported.
        - Ipv6NdTll (bool): If selected, Write Set Field Miss for IPv6 ND TLL is supported.
        - Ipv6Source (bool): If selected, Write Set Field Miss for IPv6 Source is supported.
        - MplsBos (bool): If selected, Write Set Field Miss for MPLS BoS is supported.
        - MplsLabel (bool): If selected, Write Set Field Miss for MPLS Label is supported.
        - MplsTc (bool): If selected, Write Set Field Miss for MPLS TC is supported.
        - PbbIsid (bool): If selected, Write Set Field Miss for PBB ISID is supported.
        - SctpDestination (bool): If selected, Write Set Field Miss for SCTP Destination is supported.
        - SctpSource (bool): If selected, Write Set Field Miss for SCTP Source is supported.
        - TcpDestination (bool): If selected, Write Set Field Miss for TCP Destination is supported.
        - TcpSource (bool): If selected, Write Set Field Miss for TCP Source is supported.
        - TunnelId (bool): If selected, Write Set Field Miss for Tunnel ID is supported.
        - UdpDestination (bool): If selected, Write Set Field Miss for UDP Destination is supported.
        - UdpSource (bool): If selected, Write Set Field Miss for UDP Source is supported.
        - VlanId (bool): If selected, Write Set Field Miss for VLAN ID is supported.
        - VlanPriority (bool): If selected, Write Set Field Miss for VLAN Priority is supported.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ArpDestinationHardwareAddress=None,
        ArpDestinationIpv4Address=None,
        ArpOpcode=None,
        ArpSourceHardwareAddress=None,
        ArpSourceIpv4Address=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        IcmpCode=None,
        IcmpType=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
        IpDscp=None,
        IpEcn=None,
        IpProtocol=None,
        Ipv4Destination=None,
        Ipv4Source=None,
        Ipv6Destination=None,
        Ipv6ExtHeader=None,
        Ipv6FlowLabel=None,
        Ipv6NdSll=None,
        Ipv6NdTarget=None,
        Ipv6NdTll=None,
        Ipv6Source=None,
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        PbbIsid=None,
        SctpDestination=None,
        SctpSource=None,
        TcpDestination=None,
        TcpSource=None,
        TunnelId=None,
        UdpDestination=None,
        UdpSource=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> WriteSetFieldMiss
        """Finds and retrieves writeSetFieldMiss resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve writeSetFieldMiss resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all writeSetFieldMiss resources from the server.

        Args
        ----
        - ArpDestinationHardwareAddress (bool): If selected, Write Set Field Miss for ARP Destination Hardware Address is supported.
        - ArpDestinationIpv4Address (bool): If selected, Write Set Field Miss for ARP Destination IPv4 Address is supported.
        - ArpOpcode (bool): If selected, Write Set Field Miss for ARP Opcode is supported.
        - ArpSourceHardwareAddress (bool): If selected, Write Set Field Miss for ARP Source Hardware Address is supported.
        - ArpSourceIpv4Address (bool): If selected, Write Set Field Miss for ARP Source IPv4 Address is supported.
        - EthernetDestination (bool): If selected, Write Set Field Miss for Ethernet Destination is supported.
        - EthernetSource (bool): If selected, Write Set Field Miss for Ethernet Source is supported.
        - EthernetType (bool): If selected, Write Set Field Miss for Ethernet Type is supported.
        - IcmpCode (bool): If selected, Write Set Field Miss for ICMP Code is supported.
        - IcmpType (bool): If selected, Write Set Field Miss for ICMP Type is supported.
        - Icmpv6Code (bool): If selected, Write Set Field Miss for ICMPv6 Code is supported.
        - Icmpv6Type (bool): If selected, Write Set Field Miss for ICMPv6 Type is supported.
        - IpDscp (bool): If selected, Write Set Field Miss for IP DSCP is supported.
        - IpEcn (bool): If selected, Write Set Field Miss for IP ECN is supported.
        - IpProtocol (bool): If selected, Write Set Field Miss for IP Protocol is supported.
        - Ipv4Destination (bool): If selected, Write Set Field Miss for IPv4 Destination is supported.
        - Ipv4Source (bool): If selected, Write Set Field Miss for IPv4 Source is supported.
        - Ipv6Destination (bool): If selected, Write Set Field Miss for IPv6 Destination is supported.
        - Ipv6ExtHeader (bool): If selected, Write Set Field Miss for IPv6 Ext Header is supported.
        - Ipv6FlowLabel (bool): If selected, Write Set Field Miss for IPv6 Flow Label is supported.
        - Ipv6NdSll (bool): If selected, Write Set Field Miss for IPv6 ND SLL is supported.
        - Ipv6NdTarget (bool): If selected, Write Set Field Miss for IPv6 ND Target is supported.
        - Ipv6NdTll (bool): If selected, Write Set Field Miss for IPv6 ND TLL is supported.
        - Ipv6Source (bool): If selected, Write Set Field Miss for IPv6 Source is supported.
        - MplsBos (bool): If selected, Write Set Field Miss for MPLS BoS is supported.
        - MplsLabel (bool): If selected, Write Set Field Miss for MPLS Label is supported.
        - MplsTc (bool): If selected, Write Set Field Miss for MPLS TC is supported.
        - PbbIsid (bool): If selected, Write Set Field Miss for PBB ISID is supported.
        - SctpDestination (bool): If selected, Write Set Field Miss for SCTP Destination is supported.
        - SctpSource (bool): If selected, Write Set Field Miss for SCTP Source is supported.
        - TcpDestination (bool): If selected, Write Set Field Miss for TCP Destination is supported.
        - TcpSource (bool): If selected, Write Set Field Miss for TCP Source is supported.
        - TunnelId (bool): If selected, Write Set Field Miss for Tunnel ID is supported.
        - UdpDestination (bool): If selected, Write Set Field Miss for UDP Destination is supported.
        - UdpSource (bool): If selected, Write Set Field Miss for UDP Source is supported.
        - VlanId (bool): If selected, Write Set Field Miss for VLAN ID is supported.
        - VlanPriority (bool): If selected, Write Set Field Miss for VLAN Priority is supported.

        Returns
        -------
        - self: This instance with matching writeSetFieldMiss resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of writeSetFieldMiss data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the writeSetFieldMiss resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
