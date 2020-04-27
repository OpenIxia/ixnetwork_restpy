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


class ControllerTableFlowRanges(Base):
    """This object allows to configure the Controller Table Flow Ranges in OpenFlow.
    The ControllerTableFlowRanges class encapsulates a list of controllerTableFlowRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the ControllerTableFlowRanges.find() method.
    The list can be managed by using the ControllerTableFlowRanges.add() and ControllerTableFlowRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'controllerTableFlowRanges'

    def __init__(self, parent):
        super(ControllerTableFlowRanges, self).__init__(parent)

    @property
    def Instructions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructions_37dc83672a98984a8b8effd51d9c9b68.Instructions): An instance of the Instructions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructions_37dc83672a98984a8b8effd51d9c9b68 import Instructions
        return Instructions(self)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: The target hardware address in the ARP payload.
        """
        return self._get_attribute('arpDstHwAddr')
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute('arpDstHwAddr', value)

    @property
    def ArpDstHwAddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the target hardware address in the ARP payload.
        """
        return self._get_attribute('arpDstHwAddrMask')
    @ArpDstHwAddrMask.setter
    def ArpDstHwAddrMask(self, value):
        self._set_attribute('arpDstHwAddrMask', value)

    @property
    def ArpDstIpv4Addr(self):
        """
        Returns
        -------
        - str: The ARP destination IPv4 address field value.
        """
        return self._get_attribute('arpDstIpv4Addr')
    @ArpDstIpv4Addr.setter
    def ArpDstIpv4Addr(self, value):
        self._set_attribute('arpDstIpv4Addr', value)

    @property
    def ArpDstIpv4AddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the target IPv4 address in the ARP payload.
        """
        return self._get_attribute('arpDstIpv4AddrMask')
    @ArpDstIpv4AddrMask.setter
    def ArpDstIpv4AddrMask(self, value):
        self._set_attribute('arpDstIpv4AddrMask', value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - str: Value of the ARP opcode field.
        """
        return self._get_attribute('arpOpcode')
    @ArpOpcode.setter
    def ArpOpcode(self, value):
        self._set_attribute('arpOpcode', value)

    @property
    def ArpSrcHwAddr(self):
        """
        Returns
        -------
        - str: Value of the ARP source hardware address.
        """
        return self._get_attribute('arpSrcHwAddr')
    @ArpSrcHwAddr.setter
    def ArpSrcHwAddr(self, value):
        self._set_attribute('arpSrcHwAddr', value)

    @property
    def ArpSrcHwAddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the source hardware address in the ARP payload.
        """
        return self._get_attribute('arpSrcHwAddrMask')
    @ArpSrcHwAddrMask.setter
    def ArpSrcHwAddrMask(self, value):
        self._set_attribute('arpSrcHwAddrMask', value)

    @property
    def ArpSrcIpv4Addr(self):
        """
        Returns
        -------
        - str: The ARP source IPv4 address field value.
        """
        return self._get_attribute('arpSrcIpv4Addr')
    @ArpSrcIpv4Addr.setter
    def ArpSrcIpv4Addr(self, value):
        self._set_attribute('arpSrcIpv4Addr', value)

    @property
    def ArpSrcIpv4AddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the source IPv4 address in the ARP payload.
        """
        return self._get_attribute('arpSrcIpv4AddrMask')
    @ArpSrcIpv4AddrMask.setter
    def ArpSrcIpv4AddrMask(self, value):
        self._set_attribute('arpSrcIpv4AddrMask', value)

    @property
    def CheckOverlapFlags(self):
        """
        Returns
        -------
        - bool: If selected, the configuration checks for flow range overlaps.
        """
        return self._get_attribute('checkOverlapFlags')
    @CheckOverlapFlags.setter
    def CheckOverlapFlags(self, value):
        self._set_attribute('checkOverlapFlags', value)

    @property
    def Cookie(self):
        """
        Returns
        -------
        - str: The Cookie field value.
        """
        return self._get_attribute('cookie')
    @Cookie.setter
    def Cookie(self, value):
        self._set_attribute('cookie', value)

    @property
    def CookieMask(self):
        """
        Returns
        -------
        - str: Value of the cookie mask field.
        """
        return self._get_attribute('cookieMask')
    @CookieMask.setter
    def CookieMask(self, value):
        self._set_attribute('cookieMask', value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of flow.
        """
        return self._get_attribute('description')
    @Description.setter
    def Description(self, value):
        self._set_attribute('description', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables flow.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: The Ethernet destination address.
        """
        return self._get_attribute('ethernetDestination')
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute('ethernetDestination', value)

    @property
    def EthernetDestinationMask(self):
        """
        Returns
        -------
        - str: The ethernet destination mask field.
        """
        return self._get_attribute('ethernetDestinationMask')
    @EthernetDestinationMask.setter
    def EthernetDestinationMask(self, value):
        self._set_attribute('ethernetDestinationMask', value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: Specify the Ethernet source address for the flow range.
        """
        return self._get_attribute('ethernetSource')
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute('ethernetSource', value)

    @property
    def EthernetSourceMask(self):
        """
        Returns
        -------
        - str: Specify the Ethernet Source mask value.
        """
        return self._get_attribute('ethernetSourceMask')
    @EthernetSourceMask.setter
    def EthernetSourceMask(self, value):
        self._set_attribute('ethernetSourceMask', value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: The type of Ethernet port used.
        """
        return self._get_attribute('ethernetType')
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute('ethernetType', value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: The experimenter data field value.
        """
        return self._get_attribute('experimenterData')
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute('experimenterData', value)

    @property
    def ExperimenterDatalength(self):
        """
        Returns
        -------
        - number: Value of the Experimenter data length field.
        """
        return self._get_attribute('experimenterDatalength')
    @ExperimenterDatalength.setter
    def ExperimenterDatalength(self, value):
        self._set_attribute('experimenterDatalength', value)

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - number: Value of the Experimenter Field field.
        """
        return self._get_attribute('experimenterField')
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute('experimenterField', value)

    @property
    def ExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: The experimenter hash mask value.
        """
        return self._get_attribute('experimenterHasMask')
    @ExperimenterHasMask.setter
    def ExperimenterHasMask(self, value):
        self._set_attribute('experimenterHasMask', value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - str: The experimenter ID field value.
        """
        return self._get_attribute('experimenterId')
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute('experimenterId', value)

    @property
    def FlowAdvertise(self):
        """
        Returns
        -------
        - bool: If selected, the flows are advertised by the OF Channel.
        """
        return self._get_attribute('flowAdvertise')
    @FlowAdvertise.setter
    def FlowAdvertise(self, value):
        self._set_attribute('flowAdvertise', value)

    @property
    def FlowModStatus(self):
        """
        Returns
        -------
        - str: Reflects the status of the selected flow range which is modified at runtime.
        """
        return self._get_attribute('flowModStatus')

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - number: The inactive time in seconds after which the Flow range will hard timeout and close.
        """
        return self._get_attribute('hardTimeout')
    @HardTimeout.setter
    def HardTimeout(self, value):
        self._set_attribute('hardTimeout', value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - str: The code of ICMPv4 port used.
        """
        return self._get_attribute('icmpv4Code')
    @Icmpv4Code.setter
    def Icmpv4Code(self, value):
        self._set_attribute('icmpv4Code', value)

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - str: The type of ICMPv4 port used.
        """
        return self._get_attribute('icmpv4Type')
    @Icmpv4Type.setter
    def Icmpv4Type(self, value):
        self._set_attribute('icmpv4Type', value)

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - str: The ICMPv6 code field value.
        """
        return self._get_attribute('icmpv6Code')
    @Icmpv6Code.setter
    def Icmpv6Code(self, value):
        self._set_attribute('icmpv6Code', value)

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - str: Value of the ICMPv6 type field.
        """
        return self._get_attribute('icmpv6Type')
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute('icmpv6Type', value)

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - number: The inactive time in seconds after which the Flow range will timeout and become idle.
        """
        return self._get_attribute('idleTimeout')
    @IdleTimeout.setter
    def IdleTimeout(self, value):
        self._set_attribute('idleTimeout', value)

    @property
    def InPhyPort(self):
        """
        Returns
        -------
        - str: Specify the physical In port value for this flow range. It is the underlying physical port when packet is received on a logical port.
        """
        return self._get_attribute('inPhyPort')
    @InPhyPort.setter
    def InPhyPort(self, value):
        self._set_attribute('inPhyPort', value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: Specify the Ingress port. It is the numerical representation of incoming port, starting at 1. This may be a physical or switch-defined logical port.
        """
        return self._get_attribute('inPort')
    @InPort.setter
    def InPort(self, value):
        self._set_attribute('inPort', value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: The IP DSCP value for advertising.
        """
        return self._get_attribute('ipDscp')
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute('ipDscp', value)

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - str: The IP ECN field value.
        """
        return self._get_attribute('ipEcn')
    @IpEcn.setter
    def IpEcn(self, value):
        self._set_attribute('ipEcn', value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: The IP protocol used.
        """
        return self._get_attribute('ipProtocol')
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute('ipProtocol', value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: The IPv4 destination address.
        """
        return self._get_attribute('ipv4Destination')
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute('ipv4Destination', value)

    @property
    def Ipv4DestinationMask(self):
        """
        Returns
        -------
        - str: The IPv4 destination address mask value.
        """
        return self._get_attribute('ipv4DestinationMask')
    @Ipv4DestinationMask.setter
    def Ipv4DestinationMask(self, value):
        self._set_attribute('ipv4DestinationMask', value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: The IPv4 source address.
        """
        return self._get_attribute('ipv4Source')
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute('ipv4Source', value)

    @property
    def Ipv4SourceMask(self):
        """
        Returns
        -------
        - str: The IP source address mask value.
        """
        return self._get_attribute('ipv4SourceMask')
    @Ipv4SourceMask.setter
    def Ipv4SourceMask(self, value):
        self._set_attribute('ipv4SourceMask', value)

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: Value of the IPv6 destination field.
        """
        return self._get_attribute('ipv6Destination')
    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        self._set_attribute('ipv6Destination', value)

    @property
    def Ipv6DestinationMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 destination mask field.
        """
        return self._get_attribute('ipv6DestinationMask')
    @Ipv6DestinationMask.setter
    def Ipv6DestinationMask(self, value):
        self._set_attribute('ipv6DestinationMask', value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - str: The Ipv6 extension header field value.
        """
        return self._get_attribute('ipv6ExtHeader')
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute('ipv6ExtHeader', value)

    @property
    def Ipv6ExtHeaderMask(self):
        """
        Returns
        -------
        - str: The mask value of the IPv6 Extension Header.
        """
        return self._get_attribute('ipv6ExtHeaderMask')
    @Ipv6ExtHeaderMask.setter
    def Ipv6ExtHeaderMask(self, value):
        self._set_attribute('ipv6ExtHeaderMask', value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: Value of the IPv6 flow label field.
        """
        return self._get_attribute('ipv6FlowLabel')
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute('ipv6FlowLabel', value)

    @property
    def Ipv6FlowLabelMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 flow label mask field.
        """
        return self._get_attribute('ipv6FlowLabelMask')
    @Ipv6FlowLabelMask.setter
    def Ipv6FlowLabelMask(self, value):
        self._set_attribute('ipv6FlowLabelMask', value)

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - str: The IPv6 ND DLL field value.
        """
        return self._get_attribute('ipv6NdDll')
    @Ipv6NdDll.setter
    def Ipv6NdDll(self, value):
        self._set_attribute('ipv6NdDll', value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: The source link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute('ipv6NdSll')
    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        self._set_attribute('ipv6NdSll', value)

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: The IPv6 ND target field value.
        """
        return self._get_attribute('ipv6NdTarget')
    @Ipv6NdTarget.setter
    def Ipv6NdTarget(self, value):
        self._set_attribute('ipv6NdTarget', value)

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: Value of the IPv6 source field.
        """
        return self._get_attribute('ipv6Source')
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute('ipv6Source', value)

    @property
    def Ipv6SourceMask(self):
        """
        Returns
        -------
        - str: The mask value of IPv6 source address.
        """
        return self._get_attribute('ipv6SourceMask')
    @Ipv6SourceMask.setter
    def Ipv6SourceMask(self, value):
        self._set_attribute('ipv6SourceMask', value)

    @property
    def MatchType(self):
        """
        Returns
        -------
        - str(loose | strict): The type of match to be configured.
        """
        return self._get_attribute('matchType')
    @MatchType.setter
    def MatchType(self, value):
        self._set_attribute('matchType', value)

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: Specify the table metadata value used to pass information between tables.
        """
        return self._get_attribute('metadata')
    @Metadata.setter
    def Metadata(self, value):
        self._set_attribute('metadata', value)

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: Specify the metadata bitmask value.
        """
        return self._get_attribute('metadataMask')
    @MetadataMask.setter
    def MetadataMask(self, value):
        self._set_attribute('metadataMask', value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - str: Value of the MPLS BoS field.
        """
        return self._get_attribute('mplsBos')
    @MplsBos.setter
    def MplsBos(self, value):
        self._set_attribute('mplsBos', value)

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - str: Value of the MPLS label field.
        """
        return self._get_attribute('mplsLabel')
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute('mplsLabel', value)

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - str: The MPLS TC field value.
        """
        return self._get_attribute('mplsTc')
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute('mplsTc', value)

    @property
    def NoByteCounts(self):
        """
        Returns
        -------
        - bool: If selected, the byte count is not tracked anymore.
        """
        return self._get_attribute('noByteCounts')
    @NoByteCounts.setter
    def NoByteCounts(self, value):
        self._set_attribute('noByteCounts', value)

    @property
    def NoPacketCounts(self):
        """
        Returns
        -------
        - bool: If selected, the packet count is not tracked anymore.
        """
        return self._get_attribute('noPacketCounts')
    @NoPacketCounts.setter
    def NoPacketCounts(self, value):
        self._set_attribute('noPacketCounts', value)

    @property
    def NumberOfFlows(self):
        """
        Returns
        -------
        - number: Total number of flows in a flow range.
        """
        return self._get_attribute('numberOfFlows')
    @NumberOfFlows.setter
    def NumberOfFlows(self, value):
        self._set_attribute('numberOfFlows', value)

    @property
    def PbbIsId(self):
        """
        Returns
        -------
        - str: Value of the PBB I-SID field.
        """
        return self._get_attribute('pbbIsId')
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute('pbbIsId', value)

    @property
    def PbbIsIdMask(self):
        """
        Returns
        -------
        - str: Value of the PBB I-SID mask field.
        """
        return self._get_attribute('pbbIsIdMask')
    @PbbIsIdMask.setter
    def PbbIsIdMask(self, value):
        self._set_attribute('pbbIsIdMask', value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: The priority level for the Flow Range.
        """
        return self._get_attribute('priority')
    @Priority.setter
    def Priority(self, value):
        self._set_attribute('priority', value)

    @property
    def ResetCounts(self):
        """
        Returns
        -------
        - bool: If selected, flow packet and byte counts are reset.
        """
        return self._get_attribute('resetCounts')
    @ResetCounts.setter
    def ResetCounts(self, value):
        self._set_attribute('resetCounts', value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - str: The SCTP destination field value.
        """
        return self._get_attribute('sctpDestination')
    @SctpDestination.setter
    def SctpDestination(self, value):
        self._set_attribute('sctpDestination', value)

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - str: Value of the SCTP source field.
        """
        return self._get_attribute('sctpSource')
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute('sctpSource', value)

    @property
    def SendFlowRemoved(self):
        """
        Returns
        -------
        - bool: If selected, Flow Remove message is sent to the controller, when the Flow entry is deleted from the Flow table.
        """
        return self._get_attribute('sendFlowRemoved')
    @SendFlowRemoved.setter
    def SendFlowRemoved(self, value):
        self._set_attribute('sendFlowRemoved', value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - str: The Transport destination address.
        """
        return self._get_attribute('tcpDestination')
    @TcpDestination.setter
    def TcpDestination(self, value):
        self._set_attribute('tcpDestination', value)

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - str: Value of the TCP source field.
        """
        return self._get_attribute('tcpSource')
    @TcpSource.setter
    def TcpSource(self, value):
        self._set_attribute('tcpSource', value)

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: Value of the tunnel ID field.
        """
        return self._get_attribute('tunnelId')
    @TunnelId.setter
    def TunnelId(self, value):
        self._set_attribute('tunnelId', value)

    @property
    def TunnelIdMask(self):
        """
        Returns
        -------
        - str: Value of the tunnel ID mask field.
        """
        return self._get_attribute('tunnelIdMask')
    @TunnelIdMask.setter
    def TunnelIdMask(self, value):
        self._set_attribute('tunnelIdMask', value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - str: Value of the UDP destination field.
        """
        return self._get_attribute('udpDestination')
    @UdpDestination.setter
    def UdpDestination(self, value):
        self._set_attribute('udpDestination', value)

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - str: Value of the UDP source field.
        """
        return self._get_attribute('udpSource')
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute('udpSource', value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: The unique VLAN Identifier.
        """
        return self._get_attribute('vlanId')
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute('vlanId', value)

    @property
    def VlanIdMask(self):
        """
        Returns
        -------
        - str: The VLAN mask value.
        """
        return self._get_attribute('vlanIdMask')
    @VlanIdMask.setter
    def VlanIdMask(self, value):
        self._set_attribute('vlanIdMask', value)

    @property
    def VlanMatchType(self):
        """
        Returns
        -------
        - str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag): The type of VLAN match to be configured.
        """
        return self._get_attribute('vlanMatchType')
    @VlanMatchType.setter
    def VlanMatchType(self, value):
        self._set_attribute('vlanMatchType', value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: The User Priority for this VLAN.
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, ArpDstHwAddr=None, ArpDstHwAddrMask=None, ArpDstIpv4Addr=None, ArpDstIpv4AddrMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddrMask=None, ArpSrcIpv4Addr=None, ArpSrcIpv4AddrMask=None, CheckOverlapFlags=None, Cookie=None, CookieMask=None, Description=None, Enabled=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None, FlowAdvertise=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPhyPort=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4DestinationMask=None, Ipv4Source=None, Ipv4SourceMask=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, MatchType=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NoByteCounts=None, NoPacketCounts=None, NumberOfFlows=None, PbbIsId=None, PbbIsIdMask=None, Priority=None, ResetCounts=None, SctpDestination=None, SctpSource=None, SendFlowRemoved=None, TcpDestination=None, TcpSource=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanIdMask=None, VlanMatchType=None, VlanPriority=None):
        """Updates controllerTableFlowRanges resource on the server.

        Args
        ----
        - ArpDstHwAddr (str): The target hardware address in the ARP payload.
        - ArpDstHwAddrMask (str): The mask value of the target hardware address in the ARP payload.
        - ArpDstIpv4Addr (str): The ARP destination IPv4 address field value.
        - ArpDstIpv4AddrMask (str): The mask value of the target IPv4 address in the ARP payload.
        - ArpOpcode (str): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcHwAddrMask (str): The mask value of the source hardware address in the ARP payload.
        - ArpSrcIpv4Addr (str): The ARP source IPv4 address field value.
        - ArpSrcIpv4AddrMask (str): The mask value of the source IPv4 address in the ARP payload.
        - CheckOverlapFlags (bool): If selected, the configuration checks for flow range overlaps.
        - Cookie (str): The Cookie field value.
        - CookieMask (str): Value of the cookie mask field.
        - Description (str): Description of flow.
        - Enabled (bool): Enables flow.
        - EthernetDestination (str): The Ethernet destination address.
        - EthernetDestinationMask (str): The ethernet destination mask field.
        - EthernetSource (str): Specify the Ethernet source address for the flow range.
        - EthernetSourceMask (str): Specify the Ethernet Source mask value.
        - EthernetType (str): The type of Ethernet port used.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDatalength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): Value of the Experimenter Field field.
        - ExperimenterHasMask (bool): The experimenter hash mask value.
        - ExperimenterId (str): The experimenter ID field value.
        - FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
        - HardTimeout (number): The inactive time in seconds after which the Flow range will hard timeout and close.
        - Icmpv4Code (str): The code of ICMPv4 port used.
        - Icmpv4Type (str): The type of ICMPv4 port used.
        - Icmpv6Code (str): The ICMPv6 code field value.
        - Icmpv6Type (str): Value of the ICMPv6 type field.
        - IdleTimeout (number): The inactive time in seconds after which the Flow range will timeout and become idle.
        - InPhyPort (str): Specify the physical In port value for this flow range. It is the underlying physical port when packet is received on a logical port.
        - InPort (str): Specify the Ingress port. It is the numerical representation of incoming port, starting at 1. This may be a physical or switch-defined logical port.
        - IpDscp (str): The IP DSCP value for advertising.
        - IpEcn (str): The IP ECN field value.
        - IpProtocol (str): The IP protocol used.
        - Ipv4Destination (str): The IPv4 destination address.
        - Ipv4DestinationMask (str): The IPv4 destination address mask value.
        - Ipv4Source (str): The IPv4 source address.
        - Ipv4SourceMask (str): The IP source address mask value.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6DestinationMask (str): Value of the IPv6 destination mask field.
        - Ipv6ExtHeader (str): The Ipv6 extension header field value.
        - Ipv6ExtHeaderMask (str): The mask value of the IPv6 Extension Header.
        - Ipv6FlowLabel (str): Value of the IPv6 flow label field.
        - Ipv6FlowLabelMask (str): Value of the IPv6 flow label mask field.
        - Ipv6NdDll (str): The IPv6 ND DLL field value.
        - Ipv6NdSll (str): The source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTarget (str): The IPv6 ND target field value.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6SourceMask (str): The mask value of IPv6 source address.
        - MatchType (str(loose | strict)): The type of match to be configured.
        - Metadata (str): Specify the table metadata value used to pass information between tables.
        - MetadataMask (str): Specify the metadata bitmask value.
        - MplsBos (str): Value of the MPLS BoS field.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsTc (str): The MPLS TC field value.
        - NoByteCounts (bool): If selected, the byte count is not tracked anymore.
        - NoPacketCounts (bool): If selected, the packet count is not tracked anymore.
        - NumberOfFlows (number): Total number of flows in a flow range.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbIsIdMask (str): Value of the PBB I-SID mask field.
        - Priority (number): The priority level for the Flow Range.
        - ResetCounts (bool): If selected, flow packet and byte counts are reset.
        - SctpDestination (str): The SCTP destination field value.
        - SctpSource (str): Value of the SCTP source field.
        - SendFlowRemoved (bool): If selected, Flow Remove message is sent to the controller, when the Flow entry is deleted from the Flow table.
        - TcpDestination (str): The Transport destination address.
        - TcpSource (str): Value of the TCP source field.
        - TunnelId (str): Value of the tunnel ID field.
        - TunnelIdMask (str): Value of the tunnel ID mask field.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanId (str): The unique VLAN Identifier.
        - VlanIdMask (str): The VLAN mask value.
        - VlanMatchType (str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag)): The type of VLAN match to be configured.
        - VlanPriority (str): The User Priority for this VLAN.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, ArpDstHwAddr=None, ArpDstHwAddrMask=None, ArpDstIpv4Addr=None, ArpDstIpv4AddrMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddrMask=None, ArpSrcIpv4Addr=None, ArpSrcIpv4AddrMask=None, CheckOverlapFlags=None, Cookie=None, CookieMask=None, Description=None, Enabled=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None, FlowAdvertise=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPhyPort=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4DestinationMask=None, Ipv4Source=None, Ipv4SourceMask=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, MatchType=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NoByteCounts=None, NoPacketCounts=None, NumberOfFlows=None, PbbIsId=None, PbbIsIdMask=None, Priority=None, ResetCounts=None, SctpDestination=None, SctpSource=None, SendFlowRemoved=None, TcpDestination=None, TcpSource=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanIdMask=None, VlanMatchType=None, VlanPriority=None):
        """Adds a new controllerTableFlowRanges resource on the server and adds it to the container.

        Args
        ----
        - ArpDstHwAddr (str): The target hardware address in the ARP payload.
        - ArpDstHwAddrMask (str): The mask value of the target hardware address in the ARP payload.
        - ArpDstIpv4Addr (str): The ARP destination IPv4 address field value.
        - ArpDstIpv4AddrMask (str): The mask value of the target IPv4 address in the ARP payload.
        - ArpOpcode (str): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcHwAddrMask (str): The mask value of the source hardware address in the ARP payload.
        - ArpSrcIpv4Addr (str): The ARP source IPv4 address field value.
        - ArpSrcIpv4AddrMask (str): The mask value of the source IPv4 address in the ARP payload.
        - CheckOverlapFlags (bool): If selected, the configuration checks for flow range overlaps.
        - Cookie (str): The Cookie field value.
        - CookieMask (str): Value of the cookie mask field.
        - Description (str): Description of flow.
        - Enabled (bool): Enables flow.
        - EthernetDestination (str): The Ethernet destination address.
        - EthernetDestinationMask (str): The ethernet destination mask field.
        - EthernetSource (str): Specify the Ethernet source address for the flow range.
        - EthernetSourceMask (str): Specify the Ethernet Source mask value.
        - EthernetType (str): The type of Ethernet port used.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDatalength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): Value of the Experimenter Field field.
        - ExperimenterHasMask (bool): The experimenter hash mask value.
        - ExperimenterId (str): The experimenter ID field value.
        - FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
        - HardTimeout (number): The inactive time in seconds after which the Flow range will hard timeout and close.
        - Icmpv4Code (str): The code of ICMPv4 port used.
        - Icmpv4Type (str): The type of ICMPv4 port used.
        - Icmpv6Code (str): The ICMPv6 code field value.
        - Icmpv6Type (str): Value of the ICMPv6 type field.
        - IdleTimeout (number): The inactive time in seconds after which the Flow range will timeout and become idle.
        - InPhyPort (str): Specify the physical In port value for this flow range. It is the underlying physical port when packet is received on a logical port.
        - InPort (str): Specify the Ingress port. It is the numerical representation of incoming port, starting at 1. This may be a physical or switch-defined logical port.
        - IpDscp (str): The IP DSCP value for advertising.
        - IpEcn (str): The IP ECN field value.
        - IpProtocol (str): The IP protocol used.
        - Ipv4Destination (str): The IPv4 destination address.
        - Ipv4DestinationMask (str): The IPv4 destination address mask value.
        - Ipv4Source (str): The IPv4 source address.
        - Ipv4SourceMask (str): The IP source address mask value.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6DestinationMask (str): Value of the IPv6 destination mask field.
        - Ipv6ExtHeader (str): The Ipv6 extension header field value.
        - Ipv6ExtHeaderMask (str): The mask value of the IPv6 Extension Header.
        - Ipv6FlowLabel (str): Value of the IPv6 flow label field.
        - Ipv6FlowLabelMask (str): Value of the IPv6 flow label mask field.
        - Ipv6NdDll (str): The IPv6 ND DLL field value.
        - Ipv6NdSll (str): The source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTarget (str): The IPv6 ND target field value.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6SourceMask (str): The mask value of IPv6 source address.
        - MatchType (str(loose | strict)): The type of match to be configured.
        - Metadata (str): Specify the table metadata value used to pass information between tables.
        - MetadataMask (str): Specify the metadata bitmask value.
        - MplsBos (str): Value of the MPLS BoS field.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsTc (str): The MPLS TC field value.
        - NoByteCounts (bool): If selected, the byte count is not tracked anymore.
        - NoPacketCounts (bool): If selected, the packet count is not tracked anymore.
        - NumberOfFlows (number): Total number of flows in a flow range.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbIsIdMask (str): Value of the PBB I-SID mask field.
        - Priority (number): The priority level for the Flow Range.
        - ResetCounts (bool): If selected, flow packet and byte counts are reset.
        - SctpDestination (str): The SCTP destination field value.
        - SctpSource (str): Value of the SCTP source field.
        - SendFlowRemoved (bool): If selected, Flow Remove message is sent to the controller, when the Flow entry is deleted from the Flow table.
        - TcpDestination (str): The Transport destination address.
        - TcpSource (str): Value of the TCP source field.
        - TunnelId (str): Value of the tunnel ID field.
        - TunnelIdMask (str): Value of the tunnel ID mask field.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanId (str): The unique VLAN Identifier.
        - VlanIdMask (str): The VLAN mask value.
        - VlanMatchType (str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag)): The type of VLAN match to be configured.
        - VlanPriority (str): The User Priority for this VLAN.

        Returns
        -------
        - self: This instance with all currently retrieved controllerTableFlowRanges resources using find and the newly added controllerTableFlowRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained controllerTableFlowRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ArpDstHwAddr=None, ArpDstHwAddrMask=None, ArpDstIpv4Addr=None, ArpDstIpv4AddrMask=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcHwAddrMask=None, ArpSrcIpv4Addr=None, ArpSrcIpv4AddrMask=None, CheckOverlapFlags=None, Cookie=None, CookieMask=None, Description=None, Enabled=None, EthernetDestination=None, EthernetDestinationMask=None, EthernetSource=None, EthernetSourceMask=None, EthernetType=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None, FlowAdvertise=None, FlowModStatus=None, HardTimeout=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IdleTimeout=None, InPhyPort=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4DestinationMask=None, Ipv4Source=None, Ipv4SourceMask=None, Ipv6Destination=None, Ipv6DestinationMask=None, Ipv6ExtHeader=None, Ipv6ExtHeaderMask=None, Ipv6FlowLabel=None, Ipv6FlowLabelMask=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, Ipv6SourceMask=None, MatchType=None, Metadata=None, MetadataMask=None, MplsBos=None, MplsLabel=None, MplsTc=None, NoByteCounts=None, NoPacketCounts=None, NumberOfFlows=None, PbbIsId=None, PbbIsIdMask=None, Priority=None, ResetCounts=None, SctpDestination=None, SctpSource=None, SendFlowRemoved=None, TcpDestination=None, TcpSource=None, TunnelId=None, TunnelIdMask=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanIdMask=None, VlanMatchType=None, VlanPriority=None):
        """Finds and retrieves controllerTableFlowRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve controllerTableFlowRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all controllerTableFlowRanges resources from the server.

        Args
        ----
        - ArpDstHwAddr (str): The target hardware address in the ARP payload.
        - ArpDstHwAddrMask (str): The mask value of the target hardware address in the ARP payload.
        - ArpDstIpv4Addr (str): The ARP destination IPv4 address field value.
        - ArpDstIpv4AddrMask (str): The mask value of the target IPv4 address in the ARP payload.
        - ArpOpcode (str): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcHwAddrMask (str): The mask value of the source hardware address in the ARP payload.
        - ArpSrcIpv4Addr (str): The ARP source IPv4 address field value.
        - ArpSrcIpv4AddrMask (str): The mask value of the source IPv4 address in the ARP payload.
        - CheckOverlapFlags (bool): If selected, the configuration checks for flow range overlaps.
        - Cookie (str): The Cookie field value.
        - CookieMask (str): Value of the cookie mask field.
        - Description (str): Description of flow.
        - Enabled (bool): Enables flow.
        - EthernetDestination (str): The Ethernet destination address.
        - EthernetDestinationMask (str): The ethernet destination mask field.
        - EthernetSource (str): Specify the Ethernet source address for the flow range.
        - EthernetSourceMask (str): Specify the Ethernet Source mask value.
        - EthernetType (str): The type of Ethernet port used.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDatalength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): Value of the Experimenter Field field.
        - ExperimenterHasMask (bool): The experimenter hash mask value.
        - ExperimenterId (str): The experimenter ID field value.
        - FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
        - FlowModStatus (str): Reflects the status of the selected flow range which is modified at runtime.
        - HardTimeout (number): The inactive time in seconds after which the Flow range will hard timeout and close.
        - Icmpv4Code (str): The code of ICMPv4 port used.
        - Icmpv4Type (str): The type of ICMPv4 port used.
        - Icmpv6Code (str): The ICMPv6 code field value.
        - Icmpv6Type (str): Value of the ICMPv6 type field.
        - IdleTimeout (number): The inactive time in seconds after which the Flow range will timeout and become idle.
        - InPhyPort (str): Specify the physical In port value for this flow range. It is the underlying physical port when packet is received on a logical port.
        - InPort (str): Specify the Ingress port. It is the numerical representation of incoming port, starting at 1. This may be a physical or switch-defined logical port.
        - IpDscp (str): The IP DSCP value for advertising.
        - IpEcn (str): The IP ECN field value.
        - IpProtocol (str): The IP protocol used.
        - Ipv4Destination (str): The IPv4 destination address.
        - Ipv4DestinationMask (str): The IPv4 destination address mask value.
        - Ipv4Source (str): The IPv4 source address.
        - Ipv4SourceMask (str): The IP source address mask value.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6DestinationMask (str): Value of the IPv6 destination mask field.
        - Ipv6ExtHeader (str): The Ipv6 extension header field value.
        - Ipv6ExtHeaderMask (str): The mask value of the IPv6 Extension Header.
        - Ipv6FlowLabel (str): Value of the IPv6 flow label field.
        - Ipv6FlowLabelMask (str): Value of the IPv6 flow label mask field.
        - Ipv6NdDll (str): The IPv6 ND DLL field value.
        - Ipv6NdSll (str): The source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTarget (str): The IPv6 ND target field value.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6SourceMask (str): The mask value of IPv6 source address.
        - MatchType (str(loose | strict)): The type of match to be configured.
        - Metadata (str): Specify the table metadata value used to pass information between tables.
        - MetadataMask (str): Specify the metadata bitmask value.
        - MplsBos (str): Value of the MPLS BoS field.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsTc (str): The MPLS TC field value.
        - NoByteCounts (bool): If selected, the byte count is not tracked anymore.
        - NoPacketCounts (bool): If selected, the packet count is not tracked anymore.
        - NumberOfFlows (number): Total number of flows in a flow range.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbIsIdMask (str): Value of the PBB I-SID mask field.
        - Priority (number): The priority level for the Flow Range.
        - ResetCounts (bool): If selected, flow packet and byte counts are reset.
        - SctpDestination (str): The SCTP destination field value.
        - SctpSource (str): Value of the SCTP source field.
        - SendFlowRemoved (bool): If selected, Flow Remove message is sent to the controller, when the Flow entry is deleted from the Flow table.
        - TcpDestination (str): The Transport destination address.
        - TcpSource (str): Value of the TCP source field.
        - TunnelId (str): Value of the tunnel ID field.
        - TunnelIdMask (str): Value of the tunnel ID mask field.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanId (str): The unique VLAN Identifier.
        - VlanIdMask (str): The VLAN mask value.
        - VlanMatchType (str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag)): The type of VLAN match to be configured.
        - VlanPriority (str): The User Priority for this VLAN.

        Returns
        -------
        - self: This instance with matching controllerTableFlowRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of controllerTableFlowRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the controllerTableFlowRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateFlowMod(self, *args, **kwargs):
        """Executes the updateFlowMod operation on the server.

        NOT DEFINED

        updateFlowMod(Arg2=enum)bool
        ----------------------------
        - Arg2 (str(sendFlowAdd | sendFlowModify | sendFlowRemove)): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('updateFlowMod', payload=payload, response_object=None)
