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


class FlowStatLearnedInformation(Base):
    """Signifies the information learned from flow statistics.
    The FlowStatLearnedInformation class encapsulates a list of flowStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the FlowStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'flowStatLearnedInformation'

    def __init__(self, parent):
        super(FlowStatLearnedInformation, self).__init__(parent)

    @property
    def ActiveNanoSeconds(self):
        """
        Returns
        -------
        - number: Signifies the active time in nano seconds for the session.
        """
        return self._get_attribute('activeNanoSeconds')

    @property
    def ActiveSeconds(self):
        """
        Returns
        -------
        - number: Signifies the number of active seconds for the session.
        """
        return self._get_attribute('activeSeconds')

    @property
    def ApplyActionsInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applyActionsInstruction')

    @property
    def ApplyMeterInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applyMeterInstruction')

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: The hardware address of the ARP destination.
        """
        return self._get_attribute('arpDstHwAddr')

    @property
    def ArpDstHwAddressMask(self):
        """
        Returns
        -------
        - str: Value of the ARP destination hardware address mask field.
        """
        return self._get_attribute('arpDstHwAddressMask')

    @property
    def ArpDstIpv4Address(self):
        """
        Returns
        -------
        - str: Value of the ARP destination IPv4 address field.
        """
        return self._get_attribute('arpDstIpv4Address')

    @property
    def ArpDstIpv4AddressMask(self):
        """
        Returns
        -------
        - str: Value of the ARP destination IPv4 address mask field value.
        """
        return self._get_attribute('arpDstIpv4AddressMask')

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - str: Value of the ARP opcode field.
        """
        return self._get_attribute('arpOpcode')

    @property
    def ArpSrcHwAddr(self):
        """
        Returns
        -------
        - str: The hardware address of the ARP source.
        """
        return self._get_attribute('arpSrcHwAddr')

    @property
    def ArpSrcHwAddressMask(self):
        """
        Returns
        -------
        - str: Value of the ARP source hardware address mask field.
        """
        return self._get_attribute('arpSrcHwAddressMask')

    @property
    def ArpSrcIpv4Address(self):
        """
        Returns
        -------
        - str: Value of the ARP source IPv4 address field.
        """
        return self._get_attribute('arpSrcIpv4Address')

    @property
    def ArpSrcIpv4AddressMask(self):
        """
        Returns
        -------
        - str: Value of the ARP source IPv4 address mask field.
        """
        return self._get_attribute('arpSrcIpv4AddressMask')

    @property
    def BytesCount(self):
        """
        Returns
        -------
        - str: Signifies the count of bytes.
        """
        return self._get_attribute('bytesCount')

    @property
    def ClearActionsInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('clearActionsInstruction')

    @property
    def Cookie(self):
        """
        Returns
        -------
        - str: Signifies the cookie value.
        """
        return self._get_attribute('cookie')

    @property
    def CookieMask(self):
        """
        Returns
        -------
        - str: Value of the cookie mask field.
        """
        return self._get_attribute('cookieMask')

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: The data path identification of the switch, in decimal format.
        """
        return self._get_attribute('dataPathId')

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute('dataPathIdAsHex')

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: The OpenFlow error code, if any error is received in reply to the statistics request.
        """
        return self._get_attribute('errorCode')

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: Signifies the type of the error received.
        """
        return self._get_attribute('errorType')

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: Signifies the destination address of the Ethernet port.
        """
        return self._get_attribute('ethernetDestination')

    @property
    def EthernetDestinationMask(self):
        """
        Returns
        -------
        - str: Value of the ethernet destination mask field.
        """
        return self._get_attribute('ethernetDestinationMask')

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: Signifies the source address of the Ethernet port.
        """
        return self._get_attribute('ethernetSource')

    @property
    def EthernetSourceMask(self):
        """
        Returns
        -------
        - str: Value of the ethernet source mask field.
        """
        return self._get_attribute('ethernetSourceMask')

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: Signifies the type of Ethernet port used.
        """
        return self._get_attribute('ethernetType')

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: Value of the experimenter data field.
        """
        return self._get_attribute('experimenterData')

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: Value of the Experimenter data length field.
        """
        return self._get_attribute('experimenterDataLength')

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - number: Value of the Experimenter field.
        """
        return self._get_attribute('experimenterField')

    @property
    def ExperimenterHashmask(self):
        """
        Returns
        -------
        - bool: Value of the experimenter hashmask field.
        """
        return self._get_attribute('experimenterHashmask')

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - str: Value of the experimenter ID field.
        """
        return self._get_attribute('experimenterId')

    @property
    def ExperimenterInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('experimenterInstruction')

    @property
    def Flags(self):
        """
        Returns
        -------
        - str: Specifies Flags configured.
        """
        return self._get_attribute('flags')

    @property
    def GoToTableInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('goToTableInstruction')

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - number: Signifies the inactive time in seconds after which the Flow range will hard timeout and close.
        """
        return self._get_attribute('hardTimeout')

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - str: The code of ICMPv4 port used.
        """
        return self._get_attribute('icmpv4Code')

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - str: Value of the ICMPv4 type field.
        """
        return self._get_attribute('icmpv4Type')

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - str: Value of the ICMPv6 code field.
        """
        return self._get_attribute('icmpv6Code')

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - str: Value of the ICMPv6 type field.
        """
        return self._get_attribute('icmpv6Type')

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - number: Signifies the inactive time in seconds after which the Flow range will timeout and become idle.
        """
        return self._get_attribute('idleTimeout')

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: Signifies the input port used.
        """
        return self._get_attribute('inPort')

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: Signifies the IP DSCP value for advertising.
        """
        return self._get_attribute('ipDscp')

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - str: Value of the IP ECN field.
        """
        return self._get_attribute('ipEcn')

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: Signifies the IP Protocol used.
        """
        return self._get_attribute('ipProtocol')

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: Signifies the IPv4 Destination address for the port.
        """
        return self._get_attribute('ipv4Destination')

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: Signifies the IPv4 Source address for the port.
        """
        return self._get_attribute('ipv4Source')

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: Value of the IPv6 destination field.
        """
        return self._get_attribute('ipv6Destination')

    @property
    def Ipv6DestinationMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 destination mask field.
        """
        return self._get_attribute('ipv6DestinationMask')

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - number: Value of the Ipv6 extension header field.
        """
        return self._get_attribute('ipv6ExtHeader')

    @property
    def Ipv6ExtHeaderMask(self):
        """
        Returns
        -------
        - number: Value of the IPv6 external header mask field.
        """
        return self._get_attribute('ipv6ExtHeaderMask')

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: Value of the IPv6 flow label field.
        """
        return self._get_attribute('ipv6FlowLabel')

    @property
    def Ipv6FlowLabelMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 flow label mask field.
        """
        return self._get_attribute('ipv6FlowLabelMask')

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - str: The IPv6 ND DLL field value.
        """
        return self._get_attribute('ipv6NdDll')

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: Value of the Ipv6 ND SLL field.
        """
        return self._get_attribute('ipv6NdSll')

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: Value of the IPv6 ND target field.
        """
        return self._get_attribute('ipv6NdTarget')

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: Value of the IPv6 source field.
        """
        return self._get_attribute('ipv6Source')

    @property
    def Ipv6SourceMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 source mask field.
        """
        return self._get_attribute('ipv6SourceMask')

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: The latency measured in microseconds. This shows the timethat is needed to receive a reply to the statistics request sent.
        """
        return self._get_attribute('latency')

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: The local interface IP address through which the OpenFlow session is connected.
        """
        return self._get_attribute('localIp')

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: Value of the metadata field.
        """
        return self._get_attribute('metadata')

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: Value of the metadata mask field.
        """
        return self._get_attribute('metadataMask')

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - str: Value of the MPLS BoS field.
        """
        return self._get_attribute('mplsBos')

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - str: Value of the MPLS label field.
        """
        return self._get_attribute('mplsLabel')

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - str: Value of the MPLS TC field.
        """
        return self._get_attribute('mplsTc')

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: The OpenFlow version supported by this configuration.
        """
        return self._get_attribute('negotiatedVersion')

    @property
    def NoOfApplyActions(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('noOfApplyActions')

    @property
    def NoOfWriteActions(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('noOfWriteActions')

    @property
    def NumberOfActions(self):
        """
        Returns
        -------
        - str: Signifies the number of actions configured for this OpenFlow channel.
        """
        return self._get_attribute('numberOfActions')

    @property
    def OutGroup(self):
        """
        Returns
        -------
        - number: Value of the out group field.
        """
        return self._get_attribute('outGroup')

    @property
    def OutPort(self):
        """
        Returns
        -------
        - number: Specifies Output port number.
        """
        return self._get_attribute('outPort')

    @property
    def PacketsCount(self):
        """
        Returns
        -------
        - str: Signifies the count of packets transmitted.
        """
        return self._get_attribute('packetsCount')

    @property
    def PbbISid(self):
        """
        Returns
        -------
        - str: Value of the PBB I-SID field.
        """
        return self._get_attribute('pbbISid')

    @property
    def PbbISidMask(self):
        """
        Returns
        -------
        - str: Value of the PBB I-SID mask field.
        """
        return self._get_attribute('pbbISidMask')

    @property
    def PhysicalInPort(self):
        """
        Returns
        -------
        - str: Value of the Physical IN port field.
        """
        return self._get_attribute('physicalInPort')

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: Signifies the level of priority.
        """
        return self._get_attribute('priority')

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: The IP address of the switch that is used to connect to controller.
        """
        return self._get_attribute('remoteIp')

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: This displays the status of the statistics request. It displays the following values: Reply Received Session Not Established Empty Reply Received No Reply Received.
        """
        return self._get_attribute('replyState')

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - str: Value of the SCTP destination field.
        """
        return self._get_attribute('sctpDestination')

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - str: Value of the SCTP source field.
        """
        return self._get_attribute('sctpSource')

    @property
    def TableId(self):
        """
        Returns
        -------
        - str: Signifies the identifier value for the table.
        """
        return self._get_attribute('tableId')

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - str: Value of the TCP destination field.
        """
        return self._get_attribute('tcpDestination')

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - str: Value of the TCP source field.
        """
        return self._get_attribute('tcpSource')

    @property
    def TransportDestinationIcmpCode(self):
        """
        Returns
        -------
        - str: Signifies the Transport destination address.
        """
        return self._get_attribute('transportDestinationIcmpCode')

    @property
    def TransportSourceIcmpType(self):
        """
        Returns
        -------
        - str: Signifies the Transport source address.
        """
        return self._get_attribute('transportSourceIcmpType')

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: Value of the tunnel ID field.
        """
        return self._get_attribute('tunnelId')

    @property
    def TunnelIdMask(self):
        """
        Returns
        -------
        - str: Value of the tunnel ID mask field.
        """
        return self._get_attribute('tunnelIdMask')

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - str: Value of the UDP destination field.
        """
        return self._get_attribute('udpDestination')

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - str: Value of the UDP source field.
        """
        return self._get_attribute('udpSource')

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: Signifies the unique VLAN Identifier.
        """
        return self._get_attribute('vlanId')

    @property
    def VlanMask(self):
        """
        Returns
        -------
        - number: Value of the VLAN mask field.
        """
        return self._get_attribute('vlanMask')

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: Signifies the User Priority for this VLAN.
        """
        return self._get_attribute('vlanPriority')

    @property
    def WriteActionsInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('writeActionsInstruction')

    @property
    def WriteMetadataInstruction(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('writeMetadataInstruction')

    def find(self, ActiveNanoSeconds=None, ActiveSeconds=None, ApplyActionsInstruction=None, ApplyMeterInstruction=None, ArpDstHwAddr=None, ArpDstHwAddressMask=None, ArpDstIpv4Address=None, ArpDstIpv4AddressMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddressMask=None, ArpSrcIpv4Address=None, ArpSrcIpv4AddressMask=None, BytesCount=None, ClearActionsInstruction=None, Cookie=None, CookieMask=None, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterField=None, ExperimenterHashmask=None, ExperimenterId=None, ExperimenterInstruction=None, Flags=None, GoToTableInstruction=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, Latency=None, LocalIp=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NegotiatedVersion=None, NoOfApplyActions=None, NoOfWriteActions=None, NumberOfActions=None, OutGroup=None, OutPort=None, PacketsCount=None, PbbISid=None, PbbISidMask=None, PhysicalInPort=None, Priority=None, RemoteIp=None, ReplyState=None, SctpDestination=None, SctpSource=None, TableId=None, TcpDestination=None, TcpSource=None, TransportDestinationIcmpCode=None, TransportSourceIcmpType=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanMask=None, VlanPriority=None, WriteActionsInstruction=None, WriteMetadataInstruction=None):
        """Finds and retrieves flowStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowStatLearnedInformation resources from the server.

        Args
        ----
        - ActiveNanoSeconds (number): Signifies the active time in nano seconds for the session.
        - ActiveSeconds (number): Signifies the number of active seconds for the session.
        - ApplyActionsInstruction (str): NOT DEFINED
        - ApplyMeterInstruction (str): NOT DEFINED
        - ArpDstHwAddr (str): The hardware address of the ARP destination.
        - ArpDstHwAddressMask (str): Value of the ARP destination hardware address mask field.
        - ArpDstIpv4Address (str): Value of the ARP destination IPv4 address field.
        - ArpDstIpv4AddressMask (str): Value of the ARP destination IPv4 address mask field value.
        - ArpOpcode (str): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): The hardware address of the ARP source.
        - ArpSrcHwAddressMask (str): Value of the ARP source hardware address mask field.
        - ArpSrcIpv4Address (str): Value of the ARP source IPv4 address field.
        - ArpSrcIpv4AddressMask (str): Value of the ARP source IPv4 address mask field.
        - BytesCount (str): Signifies the count of bytes.
        - ClearActionsInstruction (str): NOT DEFINED
        - Cookie (str): Signifies the cookie value.
        - CookieMask (str): Value of the cookie mask field.
        - DataPathId (str): The data path identification of the switch, in decimal format.
        - DataPathIdAsHex (str): Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        - ErrorCode (str): The OpenFlow error code, if any error is received in reply to the statistics request.
        - ErrorType (str): Signifies the type of the error received.
        - EthernetDestination (str): Signifies the destination address of the Ethernet port.
        - EthernetDestinationMask (str): Value of the ethernet destination mask field.
        - EthernetSource (str): Signifies the source address of the Ethernet port.
        - EthernetSourceMask (str): Value of the ethernet source mask field.
        - EthernetType (str): Signifies the type of Ethernet port used.
        - ExperimenterData (str): Value of the experimenter data field.
        - ExperimenterDataLength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): Value of the Experimenter field.
        - ExperimenterHashmask (bool): Value of the experimenter hashmask field.
        - ExperimenterId (str): Value of the experimenter ID field.
        - ExperimenterInstruction (str): NOT DEFINED
        - Flags (str): Specifies Flags configured.
        - GoToTableInstruction (str): NOT DEFINED
        - HardTimeout (number): Signifies the inactive time in seconds after which the Flow range will hard timeout and close.
        - Icmpv4Code (str): The code of ICMPv4 port used.
        - Icmpv4Type (str): Value of the ICMPv4 type field.
        - Icmpv6Code (str): Value of the ICMPv6 code field.
        - Icmpv6Type (str): Value of the ICMPv6 type field.
        - IdleTimeout (number): Signifies the inactive time in seconds after which the Flow range will timeout and become idle.
        - InPort (str): Signifies the input port used.
        - IpDscp (str): Signifies the IP DSCP value for advertising.
        - IpEcn (str): Value of the IP ECN field.
        - IpProtocol (str): Signifies the IP Protocol used.
        - Ipv4Destination (str): Signifies the IPv4 Destination address for the port.
        - Ipv4Source (str): Signifies the IPv4 Source address for the port.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6DestinationMask (str): Value of the IPv6 destination mask field.
        - Ipv6ExtHeader (number): Value of the Ipv6 extension header field.
        - Ipv6ExtHeaderMask (number): Value of the IPv6 external header mask field.
        - Ipv6FlowLabel (str): Value of the IPv6 flow label field.
        - Ipv6FlowLabelMask (str): Value of the IPv6 flow label mask field.
        - Ipv6NdDll (str): The IPv6 ND DLL field value.
        - Ipv6NdSll (str): Value of the Ipv6 ND SLL field.
        - Ipv6NdTarget (str): Value of the IPv6 ND target field.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6SourceMask (str): Value of the IPv6 source mask field.
        - Latency (number): The latency measured in microseconds. This shows the timethat is needed to receive a reply to the statistics request sent.
        - LocalIp (str): The local interface IP address through which the OpenFlow session is connected.
        - Metadata (str): Value of the metadata field.
        - MetadataMask (str): Value of the metadata mask field.
        - MplsBos (str): Value of the MPLS BoS field.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsTc (str): Value of the MPLS TC field.
        - NegotiatedVersion (str): The OpenFlow version supported by this configuration.
        - NoOfApplyActions (str): NOT DEFINED
        - NoOfWriteActions (str): NOT DEFINED
        - NumberOfActions (str): Signifies the number of actions configured for this OpenFlow channel.
        - OutGroup (number): Value of the out group field.
        - OutPort (number): Specifies Output port number.
        - PacketsCount (str): Signifies the count of packets transmitted.
        - PbbISid (str): Value of the PBB I-SID field.
        - PbbISidMask (str): Value of the PBB I-SID mask field.
        - PhysicalInPort (str): Value of the Physical IN port field.
        - Priority (number): Signifies the level of priority.
        - RemoteIp (str): The IP address of the switch that is used to connect to controller.
        - ReplyState (str): This displays the status of the statistics request. It displays the following values: Reply Received Session Not Established Empty Reply Received No Reply Received.
        - SctpDestination (str): Value of the SCTP destination field.
        - SctpSource (str): Value of the SCTP source field.
        - TableId (str): Signifies the identifier value for the table.
        - TcpDestination (str): Value of the TCP destination field.
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
        - WriteActionsInstruction (str): NOT DEFINED
        - WriteMetadataInstruction (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching flowStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of flowStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
