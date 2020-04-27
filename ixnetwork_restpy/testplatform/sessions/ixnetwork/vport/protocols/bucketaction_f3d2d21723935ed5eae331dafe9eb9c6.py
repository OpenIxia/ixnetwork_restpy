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


class BucketAction(Base):
    """Bucket Actions are an ordered list of action buckets, where each action bucket contains a set of actions to execute and associated parameters.
    The BucketAction class encapsulates a list of bucketAction resources that are managed by the user.
    A list of resources can be retrieved from the server using the BucketAction.find() method.
    The list can be managed by using the BucketAction.add() and BucketAction.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bucketAction'

    def __init__(self, parent):
        super(BucketAction, self).__init__(parent)

    @property
    def ActionType(self):
        """
        Returns
        -------
        - str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter): It denotes the action type associated with bucket action.
        """
        return self._get_attribute('actionType')
    @ActionType.setter
    def ActionType(self, value):
        self._set_attribute('actionType', value)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: Set the destination hardware address in the ARP payload.
        """
        return self._get_attribute('arpDstHwAddr')
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute('arpDstHwAddr', value)

    @property
    def ArpDstIpv4Addr(self):
        """
        Returns
        -------
        - str: Set the destination IPv4 address in the ARP payload.
        """
        return self._get_attribute('arpDstIpv4Addr')
    @ArpDstIpv4Addr.setter
    def ArpDstIpv4Addr(self, value):
        self._set_attribute('arpDstIpv4Addr', value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - number: Set the ARP Opcode.
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
        - str: Set the source hardware address in the ARP payload.
        """
        return self._get_attribute('arpSrcHwAddr')
    @ArpSrcHwAddr.setter
    def ArpSrcHwAddr(self, value):
        self._set_attribute('arpSrcHwAddr', value)

    @property
    def ArpSrcIpv4Addr(self):
        """
        Returns
        -------
        - str: Set the source IPv4 address in the ARP payload.
        """
        return self._get_attribute('arpSrcIpv4Addr')
    @ArpSrcIpv4Addr.setter
    def ArpSrcIpv4Addr(self, value):
        self._set_attribute('arpSrcIpv4Addr', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If selected, the bucket action is used in this controller configuration. The default Value is False
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
        - str: The destination address of the Ethernet port.
        """
        return self._get_attribute('ethernetDestination')
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute('ethernetDestination', value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: The source address of the Ethernet port.
        """
        return self._get_attribute('ethernetSource')
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute('ethernetSource', value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: The the type of Ethernet used.
        """
        return self._get_attribute('ethernetType')
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute('ethernetType', value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: Set the Experimenter details.
        """
        return self._get_attribute('experimenter')
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute('experimenter', value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: The data of the Experimenter.
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
        - number: The data length of the Experimenter. The default value is 1.
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
        - number: NOT DEFINED
        """
        return self._get_attribute('experimenterField')
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute('experimenterField', value)

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: A 32-bit integer uniquely identifying thegroup.
        """
        return self._get_attribute('groupId')
    @GroupId.setter
    def GroupId(self, value):
        self._set_attribute('groupId', value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - number: Set the ICMP code.
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
        - number: Set the ICMP type.
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
        - number: Set the ICMP code.
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
        - number: Set the ICMP type.
        """
        return self._get_attribute('icmpv6Type')
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute('icmpv6Type', value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - number: Specify the IP DSCP value.
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
        - number: Set the ECN bits of the IP header.
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
        - number: Specify the IPv4 or IPv6 protocol number.
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
        - str: Specify the destination IPv4 address.
        """
        return self._get_attribute('ipv4Destination')
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute('ipv4Destination', value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: Specify the source IPv4 address.
        """
        return self._get_attribute('ipv4Source')
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute('ipv4Source', value)

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: Set the IPv6 destination address.
        """
        return self._get_attribute('ipv6Destination')
    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        self._set_attribute('ipv6Destination', value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - number: Set the IPv6 Extension Header pseudo-field.
        """
        return self._get_attribute('ipv6ExtHeader')
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute('ipv6ExtHeader', value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - number: Set the IPv6 Flow label.
        """
        return self._get_attribute('ipv6FlowLabel')
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute('ipv6FlowLabel', value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute('ipv6NdSll')
    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        self._set_attribute('ipv6NdSll', value)

    @property
    def Ipv6NdTll(self):
        """
        Returns
        -------
        - str: Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute('ipv6NdTll')
    @Ipv6NdTll.setter
    def Ipv6NdTll(self, value):
        self._set_attribute('ipv6NdTll', value)

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: Set the IPv6 source address.
        """
        return self._get_attribute('ipv6Source')
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute('ipv6Source', value)

    @property
    def Ipv6ndTarget(self):
        """
        Returns
        -------
        - str: Set the target address in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute('ipv6ndTarget')
    @Ipv6ndTarget.setter
    def Ipv6ndTarget(self, value):
        self._set_attribute('ipv6ndTarget', value)

    @property
    def MaxByteLength(self):
        """
        Returns
        -------
        - number: Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        """
        return self._get_attribute('maxByteLength')
    @MaxByteLength.setter
    def MaxByteLength(self, value):
        self._set_attribute('maxByteLength', value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - number: Set the BoS bit in the first MPLS shim header.
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
        - number: Set the LABEL in the first MPLS shim header.
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
        - number: Set the TC in the first MPLS shim header.
        """
        return self._get_attribute('mplsTc')
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute('mplsTc', value)

    @property
    def MplsTtl(self):
        """
        Returns
        -------
        - number: Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        """
        return self._get_attribute('mplsTtl')
    @MplsTtl.setter
    def MplsTtl(self, value):
        self._set_attribute('mplsTtl', value)

    @property
    def NwTtl(self):
        """
        Returns
        -------
        - number: Set the IP TTL.
        """
        return self._get_attribute('nwTtl')
    @NwTtl.setter
    def NwTtl(self, value):
        self._set_attribute('nwTtl', value)

    @property
    def OutputPort(self):
        """
        Returns
        -------
        - number: The Output port number to be used.
        """
        return self._get_attribute('outputPort')
    @OutputPort.setter
    def OutputPort(self, value):
        self._set_attribute('outputPort', value)

    @property
    def OutputPortType(self):
        """
        Returns
        -------
        - str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal): Specify the Output Port Type for this Instruction
        """
        return self._get_attribute('outputPortType')
    @OutputPortType.setter
    def OutputPortType(self, value):
        self._set_attribute('outputPortType', value)

    @property
    def PbbIsId(self):
        """
        Returns
        -------
        - number: Set the I-SID in the first PBB service instance tag.
        """
        return self._get_attribute('pbbIsId')
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute('pbbIsId', value)

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: Set queue ID when outputting to a port.
        """
        return self._get_attribute('queueId')
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute('queueId', value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - number: Specify the SCTP Destination address.
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
        - number: Specify the SCTP Source address.
        """
        return self._get_attribute('sctpSource')
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute('sctpSource', value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - number: Specify the TCP Destination address.
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
        - number: Specify the TCP Source address.
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
        - str: Set the unique identifier used for the Tunnel.
        """
        return self._get_attribute('tunnelId')
    @TunnelId.setter
    def TunnelId(self, value):
        self._set_attribute('tunnelId', value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - number: Specify the UDP Destination address.
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
        - number: Specify the UDP Source address.
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
        - number: The 802.1q VLAN identifier.
        """
        return self._get_attribute('vlanId')
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute('vlanId', value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: Set the 802.1q priority.
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, ActionType=None, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, Enabled=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTll=None, Ipv6Source=None, Ipv6ndTarget=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NwTtl=None, OutputPort=None, OutputPortType=None, PbbIsId=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Updates bucketAction resource on the server.

        Args
        ----
        - ActionType (str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter)): It denotes the action type associated with bucket action.
        - ArpDstHwAddr (str): Set the destination hardware address in the ARP payload.
        - ArpDstIpv4Addr (str): Set the destination IPv4 address in the ARP payload.
        - ArpOpcode (number): Set the ARP Opcode.
        - ArpSrcHwAddr (str): Set the source hardware address in the ARP payload.
        - ArpSrcIpv4Addr (str): Set the source IPv4 address in the ARP payload.
        - Enabled (bool): If selected, the bucket action is used in this controller configuration. The default Value is False
        - EthernetDestination (str): The destination address of the Ethernet port.
        - EthernetSource (str): The source address of the Ethernet port.
        - EthernetType (str): The the type of Ethernet used.
        - Experimenter (number): Set the Experimenter details.
        - ExperimenterData (str): The data of the Experimenter.
        - ExperimenterDatalength (number): The data length of the Experimenter. The default value is 1.
        - ExperimenterField (number): NOT DEFINED
        - GroupId (number): A 32-bit integer uniquely identifying thegroup.
        - Icmpv4Code (number): Set the ICMP code.
        - Icmpv4Type (number): Set the ICMP type.
        - Icmpv6Code (number): Set the ICMP code.
        - Icmpv6Type (number): Set the ICMP type.
        - IpDscp (number): Specify the IP DSCP value.
        - IpEcn (number): Set the ECN bits of the IP header.
        - IpProtocol (number): Specify the IPv4 or IPv6 protocol number.
        - Ipv4Destination (str): Specify the destination IPv4 address.
        - Ipv4Source (str): Specify the source IPv4 address.
        - Ipv6Destination (str): Set the IPv6 destination address.
        - Ipv6ExtHeader (number): Set the IPv6 Extension Header pseudo-field.
        - Ipv6FlowLabel (number): Set the IPv6 Flow label.
        - Ipv6NdSll (str): Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6Source (str): Set the IPv6 source address.
        - Ipv6ndTarget (str): Set the target address in an IPv6 Neighbor Discovery message.
        - MaxByteLength (number): Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        - MplsBos (number): Set the BoS bit in the first MPLS shim header.
        - MplsLabel (number): Set the LABEL in the first MPLS shim header.
        - MplsTc (number): Set the TC in the first MPLS shim header.
        - MplsTtl (number): Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NwTtl (number): Set the IP TTL.
        - OutputPort (number): The Output port number to be used.
        - OutputPortType (str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal)): Specify the Output Port Type for this Instruction
        - PbbIsId (number): Set the I-SID in the first PBB service instance tag.
        - QueueId (number): Set queue ID when outputting to a port.
        - SctpDestination (number): Specify the SCTP Destination address.
        - SctpSource (number): Specify the SCTP Source address.
        - TcpDestination (number): Specify the TCP Destination address.
        - TcpSource (number): Specify the TCP Source address.
        - TunnelId (str): Set the unique identifier used for the Tunnel.
        - UdpDestination (number): Specify the UDP Destination address.
        - UdpSource (number): Specify the UDP Source address.
        - VlanId (number): The 802.1q VLAN identifier.
        - VlanPriority (number): Set the 802.1q priority.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, ActionType=None, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, Enabled=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTll=None, Ipv6Source=None, Ipv6ndTarget=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NwTtl=None, OutputPort=None, OutputPortType=None, PbbIsId=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Adds a new bucketAction resource on the server and adds it to the container.

        Args
        ----
        - ActionType (str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter)): It denotes the action type associated with bucket action.
        - ArpDstHwAddr (str): Set the destination hardware address in the ARP payload.
        - ArpDstIpv4Addr (str): Set the destination IPv4 address in the ARP payload.
        - ArpOpcode (number): Set the ARP Opcode.
        - ArpSrcHwAddr (str): Set the source hardware address in the ARP payload.
        - ArpSrcIpv4Addr (str): Set the source IPv4 address in the ARP payload.
        - Enabled (bool): If selected, the bucket action is used in this controller configuration. The default Value is False
        - EthernetDestination (str): The destination address of the Ethernet port.
        - EthernetSource (str): The source address of the Ethernet port.
        - EthernetType (str): The the type of Ethernet used.
        - Experimenter (number): Set the Experimenter details.
        - ExperimenterData (str): The data of the Experimenter.
        - ExperimenterDatalength (number): The data length of the Experimenter. The default value is 1.
        - ExperimenterField (number): NOT DEFINED
        - GroupId (number): A 32-bit integer uniquely identifying thegroup.
        - Icmpv4Code (number): Set the ICMP code.
        - Icmpv4Type (number): Set the ICMP type.
        - Icmpv6Code (number): Set the ICMP code.
        - Icmpv6Type (number): Set the ICMP type.
        - IpDscp (number): Specify the IP DSCP value.
        - IpEcn (number): Set the ECN bits of the IP header.
        - IpProtocol (number): Specify the IPv4 or IPv6 protocol number.
        - Ipv4Destination (str): Specify the destination IPv4 address.
        - Ipv4Source (str): Specify the source IPv4 address.
        - Ipv6Destination (str): Set the IPv6 destination address.
        - Ipv6ExtHeader (number): Set the IPv6 Extension Header pseudo-field.
        - Ipv6FlowLabel (number): Set the IPv6 Flow label.
        - Ipv6NdSll (str): Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6Source (str): Set the IPv6 source address.
        - Ipv6ndTarget (str): Set the target address in an IPv6 Neighbor Discovery message.
        - MaxByteLength (number): Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        - MplsBos (number): Set the BoS bit in the first MPLS shim header.
        - MplsLabel (number): Set the LABEL in the first MPLS shim header.
        - MplsTc (number): Set the TC in the first MPLS shim header.
        - MplsTtl (number): Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NwTtl (number): Set the IP TTL.
        - OutputPort (number): The Output port number to be used.
        - OutputPortType (str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal)): Specify the Output Port Type for this Instruction
        - PbbIsId (number): Set the I-SID in the first PBB service instance tag.
        - QueueId (number): Set queue ID when outputting to a port.
        - SctpDestination (number): Specify the SCTP Destination address.
        - SctpSource (number): Specify the SCTP Source address.
        - TcpDestination (number): Specify the TCP Destination address.
        - TcpSource (number): Specify the TCP Source address.
        - TunnelId (str): Set the unique identifier used for the Tunnel.
        - UdpDestination (number): Specify the UDP Destination address.
        - UdpSource (number): Specify the UDP Source address.
        - VlanId (number): The 802.1q VLAN identifier.
        - VlanPriority (number): Set the 802.1q priority.

        Returns
        -------
        - self: This instance with all currently retrieved bucketAction resources using find and the newly added bucketAction resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained bucketAction resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActionType=None, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, Enabled=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTll=None, Ipv6Source=None, Ipv6ndTarget=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NwTtl=None, OutputPort=None, OutputPortType=None, PbbIsId=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves bucketAction resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bucketAction resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bucketAction resources from the server.

        Args
        ----
        - ActionType (str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter)): It denotes the action type associated with bucket action.
        - ArpDstHwAddr (str): Set the destination hardware address in the ARP payload.
        - ArpDstIpv4Addr (str): Set the destination IPv4 address in the ARP payload.
        - ArpOpcode (number): Set the ARP Opcode.
        - ArpSrcHwAddr (str): Set the source hardware address in the ARP payload.
        - ArpSrcIpv4Addr (str): Set the source IPv4 address in the ARP payload.
        - Enabled (bool): If selected, the bucket action is used in this controller configuration. The default Value is False
        - EthernetDestination (str): The destination address of the Ethernet port.
        - EthernetSource (str): The source address of the Ethernet port.
        - EthernetType (str): The the type of Ethernet used.
        - Experimenter (number): Set the Experimenter details.
        - ExperimenterData (str): The data of the Experimenter.
        - ExperimenterDatalength (number): The data length of the Experimenter. The default value is 1.
        - ExperimenterField (number): NOT DEFINED
        - GroupId (number): A 32-bit integer uniquely identifying thegroup.
        - Icmpv4Code (number): Set the ICMP code.
        - Icmpv4Type (number): Set the ICMP type.
        - Icmpv6Code (number): Set the ICMP code.
        - Icmpv6Type (number): Set the ICMP type.
        - IpDscp (number): Specify the IP DSCP value.
        - IpEcn (number): Set the ECN bits of the IP header.
        - IpProtocol (number): Specify the IPv4 or IPv6 protocol number.
        - Ipv4Destination (str): Specify the destination IPv4 address.
        - Ipv4Source (str): Specify the source IPv4 address.
        - Ipv6Destination (str): Set the IPv6 destination address.
        - Ipv6ExtHeader (number): Set the IPv6 Extension Header pseudo-field.
        - Ipv6FlowLabel (number): Set the IPv6 Flow label.
        - Ipv6NdSll (str): Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6Source (str): Set the IPv6 source address.
        - Ipv6ndTarget (str): Set the target address in an IPv6 Neighbor Discovery message.
        - MaxByteLength (number): Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        - MplsBos (number): Set the BoS bit in the first MPLS shim header.
        - MplsLabel (number): Set the LABEL in the first MPLS shim header.
        - MplsTc (number): Set the TC in the first MPLS shim header.
        - MplsTtl (number): Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NwTtl (number): Set the IP TTL.
        - OutputPort (number): The Output port number to be used.
        - OutputPortType (str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal)): Specify the Output Port Type for this Instruction
        - PbbIsId (number): Set the I-SID in the first PBB service instance tag.
        - QueueId (number): Set queue ID when outputting to a port.
        - SctpDestination (number): Specify the SCTP Destination address.
        - SctpSource (number): Specify the SCTP Source address.
        - TcpDestination (number): Specify the TCP Destination address.
        - TcpSource (number): Specify the TCP Source address.
        - TunnelId (str): Set the unique identifier used for the Tunnel.
        - UdpDestination (number): Specify the UDP Destination address.
        - UdpSource (number): Specify the UDP Source address.
        - VlanId (number): The 802.1q VLAN identifier.
        - VlanPriority (number): Set the 802.1q priority.

        Returns
        -------
        - self: This instance with matching bucketAction resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of bucketAction data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bucketAction resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
