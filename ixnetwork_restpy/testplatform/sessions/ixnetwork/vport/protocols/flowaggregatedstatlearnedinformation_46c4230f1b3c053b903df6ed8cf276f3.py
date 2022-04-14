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


class FlowAggregatedStatLearnedInformation(Base):
    """This object allows to define the learned information attributes from aggregated flow statistics.
    The FlowAggregatedStatLearnedInformation class encapsulates a list of flowAggregatedStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the FlowAggregatedStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "flowAggregatedStatLearnedInformation"
    _SDM_ATT_MAP = {
        "ArpDstHwAddr": "arpDstHwAddr",
        "ArpDstHwAddressMask": "arpDstHwAddressMask",
        "ArpDstIpv4Address": "arpDstIpv4Address",
        "ArpDstIpv4AddressMask": "arpDstIpv4AddressMask",
        "ArpOpcode": "arpOpcode",
        "ArpSrcHwAddr": "arpSrcHwAddr",
        "ArpSrcHwAddressMask": "arpSrcHwAddressMask",
        "ArpSrcIpv4Address": "arpSrcIpv4Address",
        "ArpSrcIpv4AddressMask": "arpSrcIpv4AddressMask",
        "BytesCount": "bytesCount",
        "Cookie": "cookie",
        "CookieMask": "cookieMask",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "ErrorCode": "errorCode",
        "ErrorType": "errorType",
        "EthernetDestination": "ethernetDestination",
        "EthernetDestinationMask": "ethernetDestinationMask",
        "EthernetSource": "ethernetSource",
        "EthernetSourceMask": "ethernetSourceMask",
        "EthernetType": "ethernetType",
        "ExperimenterData": "experimenterData",
        "ExperimenterDataLength": "experimenterDataLength",
        "ExperimenterField": "experimenterField",
        "ExperimenterHashmask": "experimenterHashmask",
        "ExperimenterId": "experimenterId",
        "FlowsCount": "flowsCount",
        "Icmpv6Code": "icmpv6Code",
        "Icmpv6Type": "icmpv6Type",
        "InPort": "inPort",
        "IpDscp": "ipDscp",
        "IpEcn": "ipEcn",
        "IpProtocol": "ipProtocol",
        "Ipv4Destination": "ipv4Destination",
        "Ipv4Source": "ipv4Source",
        "Ipv6Destination": "ipv6Destination",
        "Ipv6DestinationMask": "ipv6DestinationMask",
        "Ipv6ExtHeader": "ipv6ExtHeader",
        "Ipv6ExtHeaderMask": "ipv6ExtHeaderMask",
        "Ipv6FlowLabel": "ipv6FlowLabel",
        "Ipv6FlowLabelMask": "ipv6FlowLabelMask",
        "Ipv6NdDll": "ipv6NdDll",
        "Ipv6NdSll": "ipv6NdSll",
        "Ipv6NdTarget": "ipv6NdTarget",
        "Ipv6Source": "ipv6Source",
        "Ipv6SourceMask": "ipv6SourceMask",
        "Latency": "latency",
        "LocalIp": "localIp",
        "Metadata": "metadata",
        "MetadataMask": "metadataMask",
        "MplsBos": "mplsBos",
        "MplsLabel": "mplsLabel",
        "MplsTc": "mplsTc",
        "NegotiatedVersion": "negotiatedVersion",
        "OutGroup": "outGroup",
        "OutPort": "outPort",
        "PacketsCount": "packetsCount",
        "PbbISid": "pbbISid",
        "PbbISidMask": "pbbISidMask",
        "PhysicalInPort": "physicalInPort",
        "RemoteIp": "remoteIp",
        "ReplyState": "replyState",
        "SctpDestination": "sctpDestination",
        "SctpSource": "sctpSource",
        "TableId": "tableId",
        "TcpDestination": "tcpDestination",
        "TcpSource": "tcpSource",
        "TransportDestinationIcmpCode": "transportDestinationIcmpCode",
        "TransportSourceIcmpType": "transportSourceIcmpType",
        "TunnelId": "tunnelId",
        "TunnelIdMask": "tunnelIdMask",
        "UdpDestination": "udpDestination",
        "UdpSource": "udpSource",
        "VlanId": "vlanId",
        "VlanMask": "vlanMask",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FlowAggregatedStatLearnedInformation, self).__init__(parent, list_op)

    @property
    def ArpDstHwAddr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP destination hardware address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDstHwAddr"])

    @property
    def ArpDstHwAddressMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP destination hardware address mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDstHwAddressMask"])

    @property
    def ArpDstIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP destination IPv4 address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDstIpv4Address"])

    @property
    def ArpDstIpv4AddressMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP destination IPv4 address mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDstIpv4AddressMask"])

    @property
    def ArpOpcode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP opcode field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpOpcode"])

    @property
    def ArpSrcHwAddr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP source hardware address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSrcHwAddr"])

    @property
    def ArpSrcHwAddressMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP source hardware address mask field value
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSrcHwAddressMask"])

    @property
    def ArpSrcIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP source IPv4 address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSrcIpv4Address"])

    @property
    def ArpSrcIpv4AddressMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ARP source IPv4 address mask field
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSrcIpv4AddressMask"])

    @property
    def BytesCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the count of bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BytesCount"])

    @property
    def Cookie(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Cookie field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cookie"])

    @property
    def CookieMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the cookie mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CookieMask"])

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the datapath ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathIdAsHex"])

    @property
    def ErrorCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the error code of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorCode"])

    @property
    def ErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the type of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorType"])

    @property
    def EthernetDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the destination address of the Ethernet port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestination"])

    @property
    def EthernetDestinationMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The ethernet destination mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestinationMask"])

    @property
    def EthernetSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the source address of the Ethernet port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSource"])

    @property
    def EthernetSourceMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ethernet source mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSourceMask"])

    @property
    def EthernetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the type of Ethernet port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @property
    def ExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the experimenter data field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterData"])

    @property
    def ExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value of the Experimenter data length field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterDataLength"])

    @property
    def ExperimenterField(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value of the Experimenter Field field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterField"])

    @property
    def ExperimenterHashmask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Value of the experimenter hasmask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterHashmask"])

    @property
    def ExperimenterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the experimenter ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterId"])

    @property
    def FlowsCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the flow count value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowsCount"])

    @property
    def Icmpv6Code(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ICMPv6 code field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Code"])

    @property
    def Icmpv6Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the ICMPv6 type field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Type"])

    @property
    def InPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the input port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InPort"])

    @property
    def IpDscp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IP DSCP value for advertising.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDscp"])

    @property
    def IpEcn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IP ECN field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpEcn"])

    @property
    def IpProtocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IP Protocol used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpProtocol"])

    @property
    def Ipv4Destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifie the IPv4 Destination address for the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Destination"])

    @property
    def Ipv4Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the IPv4 Source address for the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Source"])

    @property
    def Ipv6Destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IPv6 destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Destination"])

    @property
    def Ipv6DestinationMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IPv6 destination mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6DestinationMask"])

    @property
    def Ipv6ExtHeader(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Ipv6 extension header field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6ExtHeader"])

    @property
    def Ipv6ExtHeaderMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Velue of ipv6 Extended header mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6ExtHeaderMask"])

    @property
    def Ipv6FlowLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IPv6 flow label field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"])

    @property
    def Ipv6FlowLabelMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IPv6 flow label mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabelMask"])

    @property
    def Ipv6NdDll(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IPv6 ND DLL field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdDll"])

    @property
    def Ipv6NdSll(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IPv6 ND SLL field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdSll"])

    @property
    def Ipv6NdTarget(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IPv6 ND target field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdTarget"])

    @property
    def Ipv6Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IPv6 source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Source"])

    @property
    def Ipv6SourceMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the IPv6 source mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceMask"])

    @property
    def Latency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the latency measurement for the OpenFlow channel in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Latency"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The local interface IP address through which the OpenFlow session is connected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def Metadata(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the metadata field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Metadata"])

    @property
    def MetadataMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Metadata mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetadataMask"])

    @property
    def MplsBos(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the MPLS BoS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsBos"])

    @property
    def MplsLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the MPLS label field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabel"])

    @property
    def MplsTc(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MPLS TC field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsTc"])

    @property
    def NegotiatedVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The OpenFlow version supported by this configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatedVersion"])

    @property
    def OutGroup(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value of the out group field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutGroup"])

    @property
    def OutPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value of the out port field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutPort"])

    @property
    def PacketsCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the count of packets transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketsCount"])

    @property
    def PbbISid(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the PBB I-SID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbISid"])

    @property
    def PbbISidMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the PBB I-SID mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbISidMask"])

    @property
    def PhysicalInPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the Physical IN port field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PhysicalInPort"])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def ReplyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the reply state of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyState"])

    @property
    def SctpDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The SCTP destination field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SctpDestination"])

    @property
    def SctpSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the SCTP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SctpSource"])

    @property
    def TableId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the identifier value for the table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableId"])

    @property
    def TcpDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Transport destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpDestination"])

    @property
    def TcpSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the TCP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpSource"])

    @property
    def TransportDestinationIcmpCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Transport destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransportDestinationIcmpCode"])

    @property
    def TransportSourceIcmpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Transport source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransportSourceIcmpType"])

    @property
    def TunnelId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the tunnel ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelId"])

    @property
    def TunnelIdMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the tunnel ID mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelIdMask"])

    @property
    def UdpDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the UDP destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpDestination"])

    @property
    def UdpSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Value of the UDP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSource"])

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the unique VLAN Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @property
    def VlanMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value of the VLAN mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanMask"])

    @property
    def VlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the User Priority for this VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    def add(self):
        """Adds a new flowAggregatedStatLearnedInformation resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved flowAggregatedStatLearnedInformation resources using find and the newly added flowAggregatedStatLearnedInformation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ArpDstHwAddr=None,
        ArpDstHwAddressMask=None,
        ArpDstIpv4Address=None,
        ArpDstIpv4AddressMask=None,
        ArpOpcode=None,
        ArpSrcHwAddr=None,
        ArpSrcHwAddressMask=None,
        ArpSrcIpv4Address=None,
        ArpSrcIpv4AddressMask=None,
        BytesCount=None,
        Cookie=None,
        CookieMask=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        ErrorCode=None,
        ErrorType=None,
        EthernetDestination=None,
        EthernetDestinationMask=None,
        EthernetSource=None,
        EthernetSourceMask=None,
        EthernetType=None,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterField=None,
        ExperimenterHashmask=None,
        ExperimenterId=None,
        FlowsCount=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
        InPort=None,
        IpDscp=None,
        IpEcn=None,
        IpProtocol=None,
        Ipv4Destination=None,
        Ipv4Source=None,
        Ipv6Destination=None,
        Ipv6DestinationMask=None,
        Ipv6ExtHeader=None,
        Ipv6ExtHeaderMask=None,
        Ipv6FlowLabel=None,
        Ipv6FlowLabelMask=None,
        Ipv6NdDll=None,
        Ipv6NdSll=None,
        Ipv6NdTarget=None,
        Ipv6Source=None,
        Ipv6SourceMask=None,
        Latency=None,
        LocalIp=None,
        Metadata=None,
        MetadataMask=None,
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        NegotiatedVersion=None,
        OutGroup=None,
        OutPort=None,
        PacketsCount=None,
        PbbISid=None,
        PbbISidMask=None,
        PhysicalInPort=None,
        RemoteIp=None,
        ReplyState=None,
        SctpDestination=None,
        SctpSource=None,
        TableId=None,
        TcpDestination=None,
        TcpSource=None,
        TransportDestinationIcmpCode=None,
        TransportSourceIcmpType=None,
        TunnelId=None,
        TunnelIdMask=None,
        UdpDestination=None,
        UdpSource=None,
        VlanId=None,
        VlanMask=None,
        VlanPriority=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, int, int, bool, str, int, str, str, str, str, str, str, str, str, str, str, int, int, str, str, str, str, str, str, str, int, str, str, str, str, str, str, str, int, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, int, str) -> FlowAggregatedStatLearnedInformation
        """Finds and retrieves flowAggregatedStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowAggregatedStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowAggregatedStatLearnedInformation resources from the server.

        Args
        ----
        - ArpDstHwAddr (str): Value of the ARP destination hardware address.
        - ArpDstHwAddressMask (str): Value of the ARP destination hardware address mask field.
        - ArpDstIpv4Address (str): Value of the ARP destination IPv4 address field.
        - ArpDstIpv4AddressMask (str): Value of the ARP destination IPv4 address mask field.
        - ArpOpcode (str): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcHwAddressMask (str): Value of the ARP source hardware address mask field value
        - ArpSrcIpv4Address (str): Value of the ARP source IPv4 address field.
        - ArpSrcIpv4AddressMask (str): Value of the ARP source IPv4 address mask field
        - BytesCount (str): Signifies the count of bytes.
        - Cookie (str): The Cookie field value.
        - CookieMask (str): Value of the cookie mask field.
        - DataPathId (str): Signifies the datapath ID of the OpenFlow switch.
        - DataPathIdAsHex (str): Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        - ErrorCode (str): Signifies the error code of the error received.
        - ErrorType (str): Signifies the type of the error received.
        - EthernetDestination (str): Signifies the destination address of the Ethernet port.
        - EthernetDestinationMask (str): The ethernet destination mask field.
        - EthernetSource (str): Signifies the source address of the Ethernet port.
        - EthernetSourceMask (str): Value of the ethernet source mask field.
        - EthernetType (str): Signifies the type of Ethernet port used.
        - ExperimenterData (str): Value of the experimenter data field.
        - ExperimenterDataLength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): Value of the Experimenter Field field.
        - ExperimenterHashmask (bool): Value of the experimenter hasmask field.
        - ExperimenterId (str): Value of the experimenter ID field.
        - FlowsCount (number): Signifies the flow count value.
        - Icmpv6Code (str): Value of the ICMPv6 code field.
        - Icmpv6Type (str): Value of the ICMPv6 type field.
        - InPort (str): Signifies the input port used.
        - IpDscp (str): Signifies the IP DSCP value for advertising.
        - IpEcn (str): Value of the IP ECN field.
        - IpProtocol (str): Signifies the IP Protocol used.
        - Ipv4Destination (str): Signifie the IPv4 Destination address for the port.
        - Ipv4Source (str): Signifies the IPv4 Source address for the port.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6DestinationMask (str): Value of the IPv6 destination mask field.
        - Ipv6ExtHeader (number): The Ipv6 extension header field value.
        - Ipv6ExtHeaderMask (number): Velue of ipv6 Extended header mask field.
        - Ipv6FlowLabel (str): Value of the IPv6 flow label field.
        - Ipv6FlowLabelMask (str): Value of the IPv6 flow label mask field.
        - Ipv6NdDll (str): The IPv6 ND DLL field value.
        - Ipv6NdSll (str): The IPv6 ND SLL field value.
        - Ipv6NdTarget (str): The IPv6 ND target field value.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6SourceMask (str): Value of the IPv6 source mask field.
        - Latency (number): Signifies the latency measurement for the OpenFlow channel in microseconds.
        - LocalIp (str): The local interface IP address through which the OpenFlow session is connected.
        - Metadata (str): Value of the metadata field.
        - MetadataMask (str): Metadata mask value.
        - MplsBos (str): Value of the MPLS BoS field.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsTc (str): The MPLS TC field value.
        - NegotiatedVersion (str): The OpenFlow version supported by this configuration.
        - OutGroup (number): Value of the out group field.
        - OutPort (number): Value of the out port field.
        - PacketsCount (str): Signifies the count of packets transmitted.
        - PbbISid (str): Value of the PBB I-SID field.
        - PbbISidMask (str): Value of the PBB I-SID mask field.
        - PhysicalInPort (str): Value of the Physical IN port field.
        - RemoteIp (str): Signifies the Remote IP address of the selected interface.
        - ReplyState (str): Signifies the reply state of the OF Channel.
        - SctpDestination (str): The SCTP destination field value.
        - SctpSource (str): Value of the SCTP source field.
        - TableId (str): Signifies the identifier value for the table.
        - TcpDestination (str): The Transport destination address.
        - TcpSource (str): Value of the TCP source field.
        - TransportDestinationIcmpCode (str): Signifies the Transport destination address.
        - TransportSourceIcmpType (str): Signifies the Transport source address.
        - TunnelId (str): Value of the tunnel ID field.
        - TunnelIdMask (str): Value of the tunnel ID mask field.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanId (str): Signifies the unique VLAN Identifier.
        - VlanMask (number): Value of the VLAN mask field.
        - VlanPriority (str): Signifies the User Priority for this VLAN.

        Returns
        -------
        - self: This instance with matching flowAggregatedStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flowAggregatedStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowAggregatedStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
