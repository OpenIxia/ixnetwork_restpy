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


class InstructionActions(Base):
    """This object allows to configure the instruction actions in Controller Table Flow Ranges.
    The InstructionActions class encapsulates a list of instructionActions resources that are managed by the user.
    A list of resources can be retrieved from the server using the InstructionActions.find() method.
    The list can be managed by using the InstructionActions.add() and InstructionActions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'instructionActions'
    _SDM_ATT_MAP = {
        'ActionType': 'actionType',
        'ArpDstHwAddr': 'arpDstHwAddr',
        'ArpDstIpv4Addr': 'arpDstIpv4Addr',
        'ArpOpcode': 'arpOpcode',
        'ArpSrcHwAddr': 'arpSrcHwAddr',
        'ArpSrcIpv4Addr': 'arpSrcIpv4Addr',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'EthernetType': 'ethernetType',
        'Experimenter': 'experimenter',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDatalength': 'experimenterDatalength',
        'ExperimenterField': 'experimenterField',
        'GroupId': 'groupId',
        'Icmpv4Code': 'icmpv4Code',
        'Icmpv4Type': 'icmpv4Type',
        'Icmpv6Code': 'icmpv6Code',
        'Icmpv6Type': 'icmpv6Type',
        'IpDscp': 'ipDscp',
        'IpEcn': 'ipEcn',
        'IpProtocol': 'ipProtocol',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
        'Ipv6Destination': 'ipv6Destination',
        'Ipv6ExtHeader': 'ipv6ExtHeader',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'Ipv6NdSll': 'ipv6NdSll',
        'Ipv6NdTll': 'ipv6NdTll',
        'Ipv6Source': 'ipv6Source',
        'Ipv6ndTarget': 'ipv6ndTarget',
        'MaxByteLength': 'maxByteLength',
        'MplsBos': 'mplsBos',
        'MplsLabel': 'mplsLabel',
        'MplsTc': 'mplsTc',
        'MplsTtl': 'mplsTtl',
        'NwTtl': 'nwTtl',
        'OutputPort': 'outputPort',
        'OutputPortType': 'outputPortType',
        'PbbIsId': 'pbbIsId',
        'QueueId': 'queueId',
        'SctpDestination': 'sctpDestination',
        'SctpSource': 'sctpSource',
        'TcpDestination': 'tcpDestination',
        'TcpSource': 'tcpSource',
        'TunnelId': 'tunnelId',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(InstructionActions, self).__init__(parent)

    @property
    def ActionType(self):
        """
        Returns
        -------
        - str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter): The action type associated with this instruction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionType'])
    @ActionType.setter
    def ActionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActionType'], value)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: Value of the ARP destination hardware address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'])
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'], value)

    @property
    def ArpDstIpv4Addr(self):
        """
        Returns
        -------
        - str: The ARP destination IPv4 address field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4Addr'])
    @ArpDstIpv4Addr.setter
    def ArpDstIpv4Addr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstIpv4Addr'], value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - number: Value of the ARP opcode field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpOpcode'])
    @ArpOpcode.setter
    def ArpOpcode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpOpcode'], value)

    @property
    def ArpSrcHwAddr(self):
        """
        Returns
        -------
        - str: Value of the ARP source hardware address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'])
    @ArpSrcHwAddr.setter
    def ArpSrcHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcHwAddr'], value)

    @property
    def ArpSrcIpv4Addr(self):
        """
        Returns
        -------
        - str: The ARP source IPv4 address field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Addr'])
    @ArpSrcIpv4Addr.setter
    def ArpSrcIpv4Addr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Addr'], value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: The Ethernet destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestination'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: The Ethernet source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: The type of Ethernet port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetType'], value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: The unique Experimenter identifier. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Experimenter'], value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: The experimenter data field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterData'], value)

    @property
    def ExperimenterDatalength(self):
        """
        Returns
        -------
        - number: Value of the Experimenter data length field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDatalength'])
    @ExperimenterDatalength.setter
    def ExperimenterDatalength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDatalength'], value)

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterField'])
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterField'], value)

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: Set the Group identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])
    @GroupId.setter
    def GroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupId'], value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - number: The code of ICMPv4 port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Code'])
    @Icmpv4Code.setter
    def Icmpv4Code(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv4Code'], value)

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - number: The type of ICMPv4 port used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Type'])
    @Icmpv4Type.setter
    def Icmpv4Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv4Type'], value)

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - number: Value of the ICMPv6 code field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Code'])
    @Icmpv6Code.setter
    def Icmpv6Code(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6Code'], value)

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - number: Value of the ICMPv6 type field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6Type'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - number: The IP DSCP value for advertising.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - number: The IP ECN field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpEcn'])
    @IpEcn.setter
    def IpEcn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpEcn'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - number: The IP protocol used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: The IPv4 destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Destination'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: The IPv4 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: Value of the IPv6 destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Destination'])
    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Destination'], value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - number: The Ipv6 extension header field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'], value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - number: Value of the IPv6 flow label field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'], value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdSll'])
    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdSll'], value)

    @property
    def Ipv6NdTll(self):
        """
        Returns
        -------
        - str: Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTll'])
    @Ipv6NdTll.setter
    def Ipv6NdTll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdTll'], value)

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: Value of the IPv6 source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Source'])
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Source'], value)

    @property
    def Ipv6ndTarget(self):
        """
        Returns
        -------
        - str: The IPv6 ND target field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ndTarget'])
    @Ipv6ndTarget.setter
    def Ipv6ndTarget(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ndTarget'], value)

    @property
    def MaxByteLength(self):
        """
        Returns
        -------
        - number: Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxByteLength'])
    @MaxByteLength.setter
    def MaxByteLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxByteLength'], value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - number: Value of the MPLS BoS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsBos'])
    @MplsBos.setter
    def MplsBos(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsBos'], value)

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - number: Set the LABEL in the first MPLS shim header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabel'], value)

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - number: The MPLS TC field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTc'], value)

    @property
    def MplsTtl(self):
        """
        Returns
        -------
        - number: Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTtl'])
    @MplsTtl.setter
    def MplsTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTtl'], value)

    @property
    def NwTtl(self):
        """
        Returns
        -------
        - number: Set the IP TTL.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NwTtl'])
    @NwTtl.setter
    def NwTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NwTtl'], value)

    @property
    def OutputPort(self):
        """
        Returns
        -------
        - number: The Output port number to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPort'])
    @OutputPort.setter
    def OutputPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutputPort'], value)

    @property
    def OutputPortType(self):
        """
        Returns
        -------
        - str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal): Specify the Output Port Type for this Instruction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPortType'])
    @OutputPortType.setter
    def OutputPortType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutputPortType'], value)

    @property
    def PbbIsId(self):
        """
        Returns
        -------
        - number: Value of the PBB I-SID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsId'])
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbIsId'], value)

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: The identifier of the Queue.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueId'], value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - number: The SCTP destination field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpDestination'])
    @SctpDestination.setter
    def SctpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SctpDestination'], value)

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - number: Value of the SCTP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SctpSource'], value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - number: The Transport destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpDestination'])
    @TcpDestination.setter
    def TcpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpDestination'], value)

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - number: Value of the TCP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpSource'])
    @TcpSource.setter
    def TcpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpSource'], value)

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: Value of the tunnel ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])
    @TunnelId.setter
    def TunnelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelId'], value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - number: Value of the UDP destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestination'])
    @UdpDestination.setter
    def UdpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpDestination'], value)

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - number: Value of the UDP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSource'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: The unique VLAN Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: The User Priority for this VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, ActionType=None, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTll=None, Ipv6Source=None, Ipv6ndTarget=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NwTtl=None, OutputPort=None, OutputPortType=None, PbbIsId=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Updates instructionActions resource on the server.

        Args
        ----
        - ActionType (str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter)): The action type associated with this instruction.
        - ArpDstHwAddr (str): Value of the ARP destination hardware address.
        - ArpDstIpv4Addr (str): The ARP destination IPv4 address field value.
        - ArpOpcode (number): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcIpv4Addr (str): The ARP source IPv4 address field value.
        - EthernetDestination (str): The Ethernet destination address.
        - EthernetSource (str): The Ethernet source address.
        - EthernetType (str): The type of Ethernet port used.
        - Experimenter (number): The unique Experimenter identifier. The default value is 1.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDatalength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): NOT DEFINED
        - GroupId (number): Set the Group identifier.
        - Icmpv4Code (number): The code of ICMPv4 port used.
        - Icmpv4Type (number): The type of ICMPv4 port used.
        - Icmpv6Code (number): Value of the ICMPv6 code field.
        - Icmpv6Type (number): Value of the ICMPv6 type field.
        - IpDscp (number): The IP DSCP value for advertising.
        - IpEcn (number): The IP ECN field value.
        - IpProtocol (number): The IP protocol used.
        - Ipv4Destination (str): The IPv4 destination address.
        - Ipv4Source (str): The IPv4 source address.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6ExtHeader (number): The Ipv6 extension header field value.
        - Ipv6FlowLabel (number): Value of the IPv6 flow label field.
        - Ipv6NdSll (str): Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6ndTarget (str): The IPv6 ND target field value.
        - MaxByteLength (number): Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        - MplsBos (number): Value of the MPLS BoS field.
        - MplsLabel (number): Set the LABEL in the first MPLS shim header.
        - MplsTc (number): The MPLS TC field value.
        - MplsTtl (number): Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NwTtl (number): Set the IP TTL.
        - OutputPort (number): The Output port number to be used.
        - OutputPortType (str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal)): Specify the Output Port Type for this Instruction.
        - PbbIsId (number): Value of the PBB I-SID field.
        - QueueId (number): The identifier of the Queue.
        - SctpDestination (number): The SCTP destination field value.
        - SctpSource (number): Value of the SCTP source field.
        - TcpDestination (number): The Transport destination address.
        - TcpSource (number): Value of the TCP source field.
        - TunnelId (str): Value of the tunnel ID field.
        - UdpDestination (number): Value of the UDP destination field.
        - UdpSource (number): Value of the UDP source field.
        - VlanId (number): The unique VLAN Identifier.
        - VlanPriority (number): The User Priority for this VLAN.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActionType=None, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTll=None, Ipv6Source=None, Ipv6ndTarget=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NwTtl=None, OutputPort=None, OutputPortType=None, PbbIsId=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Adds a new instructionActions resource on the server and adds it to the container.

        Args
        ----
        - ActionType (str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter)): The action type associated with this instruction.
        - ArpDstHwAddr (str): Value of the ARP destination hardware address.
        - ArpDstIpv4Addr (str): The ARP destination IPv4 address field value.
        - ArpOpcode (number): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcIpv4Addr (str): The ARP source IPv4 address field value.
        - EthernetDestination (str): The Ethernet destination address.
        - EthernetSource (str): The Ethernet source address.
        - EthernetType (str): The type of Ethernet port used.
        - Experimenter (number): The unique Experimenter identifier. The default value is 1.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDatalength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): NOT DEFINED
        - GroupId (number): Set the Group identifier.
        - Icmpv4Code (number): The code of ICMPv4 port used.
        - Icmpv4Type (number): The type of ICMPv4 port used.
        - Icmpv6Code (number): Value of the ICMPv6 code field.
        - Icmpv6Type (number): Value of the ICMPv6 type field.
        - IpDscp (number): The IP DSCP value for advertising.
        - IpEcn (number): The IP ECN field value.
        - IpProtocol (number): The IP protocol used.
        - Ipv4Destination (str): The IPv4 destination address.
        - Ipv4Source (str): The IPv4 source address.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6ExtHeader (number): The Ipv6 extension header field value.
        - Ipv6FlowLabel (number): Value of the IPv6 flow label field.
        - Ipv6NdSll (str): Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6ndTarget (str): The IPv6 ND target field value.
        - MaxByteLength (number): Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        - MplsBos (number): Value of the MPLS BoS field.
        - MplsLabel (number): Set the LABEL in the first MPLS shim header.
        - MplsTc (number): The MPLS TC field value.
        - MplsTtl (number): Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NwTtl (number): Set the IP TTL.
        - OutputPort (number): The Output port number to be used.
        - OutputPortType (str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal)): Specify the Output Port Type for this Instruction.
        - PbbIsId (number): Value of the PBB I-SID field.
        - QueueId (number): The identifier of the Queue.
        - SctpDestination (number): The SCTP destination field value.
        - SctpSource (number): Value of the SCTP source field.
        - TcpDestination (number): The Transport destination address.
        - TcpSource (number): Value of the TCP source field.
        - TunnelId (str): Value of the tunnel ID field.
        - UdpDestination (number): Value of the UDP destination field.
        - UdpSource (number): Value of the UDP source field.
        - VlanId (number): The unique VLAN Identifier.
        - VlanPriority (number): The User Priority for this VLAN.

        Returns
        -------
        - self: This instance with all currently retrieved instructionActions resources using find and the newly added instructionActions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained instructionActions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActionType=None, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, ExperimenterField=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTll=None, Ipv6Source=None, Ipv6ndTarget=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NwTtl=None, OutputPort=None, OutputPortType=None, PbbIsId=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves instructionActions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve instructionActions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all instructionActions resources from the server.

        Args
        ----
        - ActionType (str(drop | output | setEthernetSource | setEthernetDestination | setEthernetType | setVlanId | setVlanPriority | setIpDscp | setIpEcn | setIpProtocol | setIpv4Source | setIpv4Destination | setTcpSource | setTcpDestination | setUdpSource | setUdpDestination | setSctpSource | setSctpDestination | setIcmpv4Type | setIcmpv4Code | setArpOpcode | setArpSourceHwAddress | setArpTargetHwAddress | setArpSourceIpv4Address | setArpTargetIpv4Address | setIpv6Source | setIpv6Destination | setIpv6FlowLabel | setIcmpv6Type | setIcmpv6Code | setIpv6NdTarget | setIpv6NdSll | setIpv6NdTll | setMplsLabel | setMplsTc | setMplsBos | setPbbIsid | setTunnelId | setIpv6ExtHeader | copyTtlOut | copyTtlIn | setMplsTtl | decrementMplsTtl | pushVlan | popVlan | pushMpls | popMpls | setQueue | group | setNetworkTtl | decrementNetworkTtl | pushPbb | popPbb | experimenter | setExperimenter)): The action type associated with this instruction.
        - ArpDstHwAddr (str): Value of the ARP destination hardware address.
        - ArpDstIpv4Addr (str): The ARP destination IPv4 address field value.
        - ArpOpcode (number): Value of the ARP opcode field.
        - ArpSrcHwAddr (str): Value of the ARP source hardware address.
        - ArpSrcIpv4Addr (str): The ARP source IPv4 address field value.
        - EthernetDestination (str): The Ethernet destination address.
        - EthernetSource (str): The Ethernet source address.
        - EthernetType (str): The type of Ethernet port used.
        - Experimenter (number): The unique Experimenter identifier. The default value is 1.
        - ExperimenterData (str): The experimenter data field value.
        - ExperimenterDatalength (number): Value of the Experimenter data length field.
        - ExperimenterField (number): NOT DEFINED
        - GroupId (number): Set the Group identifier.
        - Icmpv4Code (number): The code of ICMPv4 port used.
        - Icmpv4Type (number): The type of ICMPv4 port used.
        - Icmpv6Code (number): Value of the ICMPv6 code field.
        - Icmpv6Type (number): Value of the ICMPv6 type field.
        - IpDscp (number): The IP DSCP value for advertising.
        - IpEcn (number): The IP ECN field value.
        - IpProtocol (number): The IP protocol used.
        - Ipv4Destination (str): The IPv4 destination address.
        - Ipv4Source (str): The IPv4 source address.
        - Ipv6Destination (str): Value of the IPv6 destination field.
        - Ipv6ExtHeader (number): The Ipv6 extension header field value.
        - Ipv6FlowLabel (number): Value of the IPv6 flow label field.
        - Ipv6NdSll (str): Set the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): Set the target link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6Source (str): Value of the IPv6 source field.
        - Ipv6ndTarget (str): The IPv6 ND target field value.
        - MaxByteLength (number): Sets the maximum length in bytes. The minimum value is 0 and the maximum value is 65,535 bytes.
        - MplsBos (number): Value of the MPLS BoS field.
        - MplsLabel (number): Set the LABEL in the first MPLS shim header.
        - MplsTc (number): The MPLS TC field value.
        - MplsTtl (number): Replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NwTtl (number): Set the IP TTL.
        - OutputPort (number): The Output port number to be used.
        - OutputPortType (str(ofppInPort | manual | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal)): Specify the Output Port Type for this Instruction.
        - PbbIsId (number): Value of the PBB I-SID field.
        - QueueId (number): The identifier of the Queue.
        - SctpDestination (number): The SCTP destination field value.
        - SctpSource (number): Value of the SCTP source field.
        - TcpDestination (number): The Transport destination address.
        - TcpSource (number): Value of the TCP source field.
        - TunnelId (str): Value of the tunnel ID field.
        - UdpDestination (number): Value of the UDP destination field.
        - UdpSource (number): Value of the UDP source field.
        - VlanId (number): The unique VLAN Identifier.
        - VlanPriority (number): The User Priority for this VLAN.

        Returns
        -------
        - self: This instance with matching instructionActions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of instructionActions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the instructionActions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
