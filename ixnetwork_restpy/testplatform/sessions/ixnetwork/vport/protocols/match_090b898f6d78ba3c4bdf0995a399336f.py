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


class Match(Base):
    """Select the type of match capability that the table will support.
    The Match class encapsulates a required match resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "match"
    _SDM_ATT_MAP = {
        "ArpDestinationHardwareAddress": "arpDestinationHardwareAddress",
        "ArpDestinationIpv4Address": "arpDestinationIpv4Address",
        "ArpOpcode": "arpOpcode",
        "ArpSourceHardwareAddress": "arpSourceHardwareAddress",
        "ArpSourceIpv4Address": "arpSourceIpv4Address",
        "EthernetDestination": "ethernetDestination",
        "EthernetSource": "ethernetSource",
        "EthernetType": "ethernetType",
        "Experimenter": "experimenter",
        "IcmpCode": "icmpCode",
        "IcmpType": "icmpType",
        "Icmpv6Code": "icmpv6Code",
        "Icmpv6Type": "icmpv6Type",
        "InPort": "inPort",
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
        "Metadata": "metadata",
        "MplsBos": "mplsBos",
        "MplsLabel": "mplsLabel",
        "MplsTc": "mplsTc",
        "PbbIsid": "pbbIsid",
        "PhysicalInPort": "physicalInPort",
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
        super(Match, self).__init__(parent, list_op)

    @property
    def ArpDestinationHardwareAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ARP Destination Hardware Address matching is supported.
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
        - bool: If selected, ARP Destination IPv4 Address matching is supported.
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
        - bool: If selected, ARP Opcode matching is supported.
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
        - bool: If selected, ARP Source Hardware Address matching is supported.
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
        - bool: If selected, ARP Source IPv4 Address matching is supported.
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
        - bool: If selected, Ethernet Destination matching is supported.
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
        - bool: If selected, Ethernet Source matching is supported.
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
        - bool: If selected, Ethernet Type matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @EthernetType.setter
    def EthernetType(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetType"], value)

    @property
    def Experimenter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Experimenter matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Experimenter"])

    @Experimenter.setter
    def Experimenter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Experimenter"], value)

    @property
    def IcmpCode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ICMP Code matching is supported.
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
        - bool: If selected, ICMP Type matching is supported.
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
        - bool: If selected, ICMPv6 Code matching is supported.
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
        - bool: If selected, ICMPv6 Type matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Type"])

    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Icmpv6Type"], value)

    @property
    def InPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, In Port matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InPort"])

    @InPort.setter
    def InPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InPort"], value)

    @property
    def IpDscp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IP DSCP matching is supported.
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
        - bool: If selected, IP ECN matching is supported.
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
        - bool: If selected, IP Protocol matching is supported.
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
        - bool: If selected, IPv4 Destination matching is supported.
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
        - bool: If selected, IPv4 Source matching is supported.
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
        - bool: If selected, IPv6 Destination matching is supported.
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
        - bool: If selected, IPv6 Ext Header matching is supported.
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
        - bool: If selected, IPv6 Flow Label matching is supported.
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
        - bool: If selected, IPv6 ND SLL matching is supported.
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
        - bool: If selected, IPv6 ND Target matching is supported.
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
        - bool: If selected, IPv6 ND TLL matching is supported.
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
        - bool: If selected, IPv6 Source matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Source"])

    @Ipv6Source.setter
    def Ipv6Source(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Source"], value)

    @property
    def Metadata(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Metadata matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Metadata"])

    @Metadata.setter
    def Metadata(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Metadata"], value)

    @property
    def MplsBos(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, MPLS BoS matching is supported.
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
        - bool: If selected, MPLS Label matching is supported.
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
        - bool: If selected, MPLS TC matching is supported.
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
        - bool: If selected, PBB ISID matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsid"])

    @PbbIsid.setter
    def PbbIsid(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbIsid"], value)

    @property
    def PhysicalInPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Physical In Port matching is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PhysicalInPort"])

    @PhysicalInPort.setter
    def PhysicalInPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PhysicalInPort"], value)

    @property
    def SctpDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, SCTP Destination matching is supported.
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
        - bool: If selected, SCTP Source matching is supported.
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
        - bool: If selected, TCP Destination matching is supported.
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
        - bool: If selected, TCP Source matching is supported.
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
        - bool: If selected, Tunnel ID matching is supported.
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
        - bool: If selected, UDP Destination matching is supported.
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
        - bool: If selected, UDP Source matching is supported.
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
        - bool: If selected, VLAN ID matching is supported.
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
        - bool: If selected, VLAN Priority matching is supported.
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
        Experimenter=None,
        IcmpCode=None,
        IcmpType=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
        InPort=None,
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
        Metadata=None,
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        PbbIsid=None,
        PhysicalInPort=None,
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
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Match
        """Updates match resource on the server.

        Args
        ----
        - ArpDestinationHardwareAddress (bool): If selected, ARP Destination Hardware Address matching is supported.
        - ArpDestinationIpv4Address (bool): If selected, ARP Destination IPv4 Address matching is supported.
        - ArpOpcode (bool): If selected, ARP Opcode matching is supported.
        - ArpSourceHardwareAddress (bool): If selected, ARP Source Hardware Address matching is supported.
        - ArpSourceIpv4Address (bool): If selected, ARP Source IPv4 Address matching is supported.
        - EthernetDestination (bool): If selected, Ethernet Destination matching is supported.
        - EthernetSource (bool): If selected, Ethernet Source matching is supported.
        - EthernetType (bool): If selected, Ethernet Type matching is supported.
        - Experimenter (bool): If selected, Experimenter matching is supported.
        - IcmpCode (bool): If selected, ICMP Code matching is supported.
        - IcmpType (bool): If selected, ICMP Type matching is supported.
        - Icmpv6Code (bool): If selected, ICMPv6 Code matching is supported.
        - Icmpv6Type (bool): If selected, ICMPv6 Type matching is supported.
        - InPort (bool): If selected, In Port matching is supported.
        - IpDscp (bool): If selected, IP DSCP matching is supported.
        - IpEcn (bool): If selected, IP ECN matching is supported.
        - IpProtocol (bool): If selected, IP Protocol matching is supported.
        - Ipv4Destination (bool): If selected, IPv4 Destination matching is supported.
        - Ipv4Source (bool): If selected, IPv4 Source matching is supported.
        - Ipv6Destination (bool): If selected, IPv6 Destination matching is supported.
        - Ipv6ExtHeader (bool): If selected, IPv6 Ext Header matching is supported.
        - Ipv6FlowLabel (bool): If selected, IPv6 Flow Label matching is supported.
        - Ipv6NdSll (bool): If selected, IPv6 ND SLL matching is supported.
        - Ipv6NdTarget (bool): If selected, IPv6 ND Target matching is supported.
        - Ipv6NdTll (bool): If selected, IPv6 ND TLL matching is supported.
        - Ipv6Source (bool): If selected, IPv6 Source matching is supported.
        - Metadata (bool): If selected, Metadata matching is supported.
        - MplsBos (bool): If selected, MPLS BoS matching is supported.
        - MplsLabel (bool): If selected, MPLS Label matching is supported.
        - MplsTc (bool): If selected, MPLS TC matching is supported.
        - PbbIsid (bool): If selected, PBB ISID matching is supported.
        - PhysicalInPort (bool): If selected, Physical In Port matching is supported.
        - SctpDestination (bool): If selected, SCTP Destination matching is supported.
        - SctpSource (bool): If selected, SCTP Source matching is supported.
        - TcpDestination (bool): If selected, TCP Destination matching is supported.
        - TcpSource (bool): If selected, TCP Source matching is supported.
        - TunnelId (bool): If selected, Tunnel ID matching is supported.
        - UdpDestination (bool): If selected, UDP Destination matching is supported.
        - UdpSource (bool): If selected, UDP Source matching is supported.
        - VlanId (bool): If selected, VLAN ID matching is supported.
        - VlanPriority (bool): If selected, VLAN Priority matching is supported.

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
        Experimenter=None,
        IcmpCode=None,
        IcmpType=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
        InPort=None,
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
        Metadata=None,
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        PbbIsid=None,
        PhysicalInPort=None,
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
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Match
        """Finds and retrieves match resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve match resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all match resources from the server.

        Args
        ----
        - ArpDestinationHardwareAddress (bool): If selected, ARP Destination Hardware Address matching is supported.
        - ArpDestinationIpv4Address (bool): If selected, ARP Destination IPv4 Address matching is supported.
        - ArpOpcode (bool): If selected, ARP Opcode matching is supported.
        - ArpSourceHardwareAddress (bool): If selected, ARP Source Hardware Address matching is supported.
        - ArpSourceIpv4Address (bool): If selected, ARP Source IPv4 Address matching is supported.
        - EthernetDestination (bool): If selected, Ethernet Destination matching is supported.
        - EthernetSource (bool): If selected, Ethernet Source matching is supported.
        - EthernetType (bool): If selected, Ethernet Type matching is supported.
        - Experimenter (bool): If selected, Experimenter matching is supported.
        - IcmpCode (bool): If selected, ICMP Code matching is supported.
        - IcmpType (bool): If selected, ICMP Type matching is supported.
        - Icmpv6Code (bool): If selected, ICMPv6 Code matching is supported.
        - Icmpv6Type (bool): If selected, ICMPv6 Type matching is supported.
        - InPort (bool): If selected, In Port matching is supported.
        - IpDscp (bool): If selected, IP DSCP matching is supported.
        - IpEcn (bool): If selected, IP ECN matching is supported.
        - IpProtocol (bool): If selected, IP Protocol matching is supported.
        - Ipv4Destination (bool): If selected, IPv4 Destination matching is supported.
        - Ipv4Source (bool): If selected, IPv4 Source matching is supported.
        - Ipv6Destination (bool): If selected, IPv6 Destination matching is supported.
        - Ipv6ExtHeader (bool): If selected, IPv6 Ext Header matching is supported.
        - Ipv6FlowLabel (bool): If selected, IPv6 Flow Label matching is supported.
        - Ipv6NdSll (bool): If selected, IPv6 ND SLL matching is supported.
        - Ipv6NdTarget (bool): If selected, IPv6 ND Target matching is supported.
        - Ipv6NdTll (bool): If selected, IPv6 ND TLL matching is supported.
        - Ipv6Source (bool): If selected, IPv6 Source matching is supported.
        - Metadata (bool): If selected, Metadata matching is supported.
        - MplsBos (bool): If selected, MPLS BoS matching is supported.
        - MplsLabel (bool): If selected, MPLS Label matching is supported.
        - MplsTc (bool): If selected, MPLS TC matching is supported.
        - PbbIsid (bool): If selected, PBB ISID matching is supported.
        - PhysicalInPort (bool): If selected, Physical In Port matching is supported.
        - SctpDestination (bool): If selected, SCTP Destination matching is supported.
        - SctpSource (bool): If selected, SCTP Source matching is supported.
        - TcpDestination (bool): If selected, TCP Destination matching is supported.
        - TcpSource (bool): If selected, TCP Source matching is supported.
        - TunnelId (bool): If selected, Tunnel ID matching is supported.
        - UdpDestination (bool): If selected, UDP Destination matching is supported.
        - UdpSource (bool): If selected, UDP Source matching is supported.
        - VlanId (bool): If selected, VLAN ID matching is supported.
        - VlanPriority (bool): If selected, VLAN Priority matching is supported.

        Returns
        -------
        - self: This instance with matching match resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of match data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the match resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
