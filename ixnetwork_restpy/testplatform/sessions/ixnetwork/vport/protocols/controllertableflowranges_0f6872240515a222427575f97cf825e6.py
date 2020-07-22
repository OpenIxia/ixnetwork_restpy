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


class ControllerTableFlowRanges(Base):
    """This object allows to configure the Controller Table Flow Ranges in OpenFlow.
    The ControllerTableFlowRanges class encapsulates a list of controllerTableFlowRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the ControllerTableFlowRanges.find() method.
    The list can be managed by using the ControllerTableFlowRanges.add() and ControllerTableFlowRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'controllerTableFlowRanges'
    _SDM_ATT_MAP = {
        'ArpDstHwAddr': 'arpDstHwAddr',
        'ArpDstHwAddrMask': 'arpDstHwAddrMask',
        'ArpDstIpv4Addr': 'arpDstIpv4Addr',
        'ArpDstIpv4AddrMask': 'arpDstIpv4AddrMask',
        'ArpOpcode': 'arpOpcode',
        'ArpSrcHwAddr': 'arpSrcHwAddr',
        'ArpSrcHwAddrMask': 'arpSrcHwAddrMask',
        'ArpSrcIpv4Addr': 'arpSrcIpv4Addr',
        'ArpSrcIpv4AddrMask': 'arpSrcIpv4AddrMask',
        'CheckOverlapFlags': 'checkOverlapFlags',
        'Cookie': 'cookie',
        'CookieMask': 'cookieMask',
        'Description': 'description',
        'Enabled': 'enabled',
        'EthernetDestination': 'ethernetDestination',
        'EthernetDestinationMask': 'ethernetDestinationMask',
        'EthernetSource': 'ethernetSource',
        'EthernetSourceMask': 'ethernetSourceMask',
        'EthernetType': 'ethernetType',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDatalength': 'experimenterDatalength',
        'ExperimenterField': 'experimenterField',
        'ExperimenterHasMask': 'experimenterHasMask',
        'ExperimenterId': 'experimenterId',
        'FlowAdvertise': 'flowAdvertise',
        'FlowModStatus': 'flowModStatus',
        'HardTimeout': 'hardTimeout',
        'Icmpv4Code': 'icmpv4Code',
        'Icmpv4Type': 'icmpv4Type',
        'Icmpv6Code': 'icmpv6Code',
        'Icmpv6Type': 'icmpv6Type',
        'IdleTimeout': 'idleTimeout',
        'InPhyPort': 'inPhyPort',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpEcn': 'ipEcn',
        'IpProtocol': 'ipProtocol',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4DestinationMask': 'ipv4DestinationMask',
        'Ipv4Source': 'ipv4Source',
        'Ipv4SourceMask': 'ipv4SourceMask',
        'Ipv6Destination': 'ipv6Destination',
        'Ipv6DestinationMask': 'ipv6DestinationMask',
        'Ipv6ExtHeader': 'ipv6ExtHeader',
        'Ipv6ExtHeaderMask': 'ipv6ExtHeaderMask',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'Ipv6FlowLabelMask': 'ipv6FlowLabelMask',
        'Ipv6NdDll': 'ipv6NdDll',
        'Ipv6NdSll': 'ipv6NdSll',
        'Ipv6NdTarget': 'ipv6NdTarget',
        'Ipv6Source': 'ipv6Source',
        'Ipv6SourceMask': 'ipv6SourceMask',
        'MatchType': 'matchType',
        'Metadata': 'metadata',
        'MetadataMask': 'metadataMask',
        'MplsBos': 'mplsBos',
        'MplsLabel': 'mplsLabel',
        'MplsTc': 'mplsTc',
        'NoByteCounts': 'noByteCounts',
        'NoPacketCounts': 'noPacketCounts',
        'NumberOfFlows': 'numberOfFlows',
        'PbbIsId': 'pbbIsId',
        'PbbIsIdMask': 'pbbIsIdMask',
        'Priority': 'priority',
        'ResetCounts': 'resetCounts',
        'SctpDestination': 'sctpDestination',
        'SctpSource': 'sctpSource',
        'SendFlowRemoved': 'sendFlowRemoved',
        'TcpDestination': 'tcpDestination',
        'TcpSource': 'tcpSource',
        'TunnelId': 'tunnelId',
        'TunnelIdMask': 'tunnelIdMask',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanId': 'vlanId',
        'VlanIdMask': 'vlanIdMask',
        'VlanMatchType': 'vlanMatchType',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(ControllerTableFlowRanges, self).__init__(parent)

    @property
    def Instructions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructions_5497c86fc28b0188cf9eea0ca484ecbf.Instructions): An instance of the Instructions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructions_5497c86fc28b0188cf9eea0ca484ecbf import Instructions
        return Instructions(self)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - str: The target hardware address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'])
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstHwAddr'], value)

    @property
    def ArpDstHwAddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the target hardware address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddrMask'])
    @ArpDstHwAddrMask.setter
    def ArpDstHwAddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstHwAddrMask'], value)

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
    def ArpDstIpv4AddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the target IPv4 address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4AddrMask'])
    @ArpDstIpv4AddrMask.setter
    def ArpDstIpv4AddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpDstIpv4AddrMask'], value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - str: Value of the ARP opcode field.
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
    def ArpSrcHwAddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the source hardware address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddrMask'])
    @ArpSrcHwAddrMask.setter
    def ArpSrcHwAddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcHwAddrMask'], value)

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
    def ArpSrcIpv4AddrMask(self):
        """
        Returns
        -------
        - str: The mask value of the source IPv4 address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4AddrMask'])
    @ArpSrcIpv4AddrMask.setter
    def ArpSrcIpv4AddrMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpSrcIpv4AddrMask'], value)

    @property
    def CheckOverlapFlags(self):
        """
        Returns
        -------
        - bool: If selected, the configuration checks for flow range overlaps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CheckOverlapFlags'])
    @CheckOverlapFlags.setter
    def CheckOverlapFlags(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CheckOverlapFlags'], value)

    @property
    def Cookie(self):
        """
        Returns
        -------
        - str: The Cookie field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cookie'])
    @Cookie.setter
    def Cookie(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cookie'], value)

    @property
    def CookieMask(self):
        """
        Returns
        -------
        - str: Value of the cookie mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CookieMask'])
    @CookieMask.setter
    def CookieMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CookieMask'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

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
    def EthernetDestinationMask(self):
        """
        Returns
        -------
        - str: The ethernet destination mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestinationMask'])
    @EthernetDestinationMask.setter
    def EthernetDestinationMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestinationMask'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: Specify the Ethernet source address for the flow range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetSourceMask(self):
        """
        Returns
        -------
        - str: Specify the Ethernet Source mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSourceMask'])
    @EthernetSourceMask.setter
    def EthernetSourceMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSourceMask'], value)

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
        - number: Value of the Experimenter Field field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterField'])
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterField'], value)

    @property
    def ExperimenterHasMask(self):
        """
        Returns
        -------
        - bool: The experimenter hash mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterHasMask'])
    @ExperimenterHasMask.setter
    def ExperimenterHasMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterHasMask'], value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - str: The experimenter ID field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterId'], value)

    @property
    def FlowAdvertise(self):
        """
        Returns
        -------
        - bool: If selected, the flows are advertised by the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAdvertise'])
    @FlowAdvertise.setter
    def FlowAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAdvertise'], value)

    @property
    def FlowModStatus(self):
        """
        Returns
        -------
        - str: Reflects the status of the selected flow range which is modified at runtime.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowModStatus'])

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - number: The inactive time in seconds after which the Flow range will hard timeout and close.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardTimeout'])
    @HardTimeout.setter
    def HardTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HardTimeout'], value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - str: The code of ICMPv4 port used.
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
        - str: The type of ICMPv4 port used.
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
        - str: The ICMPv6 code field value.
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
        - str: Value of the ICMPv6 type field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6Type'], value)

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - number: The inactive time in seconds after which the Flow range will timeout and become idle.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IdleTimeout'])
    @IdleTimeout.setter
    def IdleTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IdleTimeout'], value)

    @property
    def InPhyPort(self):
        """
        Returns
        -------
        - str: Specify the physical In port value for this flow range. It is the underlying physical port when packet is received on a logical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPhyPort'])
    @InPhyPort.setter
    def InPhyPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPhyPort'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: Specify the Ingress port. It is the numerical representation of incoming port, starting at 1. This may be a physical or switch-defined logical port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])
    @InPort.setter
    def InPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPort'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: The IP DSCP value for advertising.
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
        - str: The IP ECN field value.
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
        - str: The IP protocol used.
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
    def Ipv4DestinationMask(self):
        """
        Returns
        -------
        - str: The IPv4 destination address mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4DestinationMask'])
    @Ipv4DestinationMask.setter
    def Ipv4DestinationMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4DestinationMask'], value)

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
    def Ipv4SourceMask(self):
        """
        Returns
        -------
        - str: The IP source address mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4SourceMask'])
    @Ipv4SourceMask.setter
    def Ipv4SourceMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4SourceMask'], value)

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
    def Ipv6DestinationMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 destination mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6DestinationMask'])
    @Ipv6DestinationMask.setter
    def Ipv6DestinationMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6DestinationMask'], value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - str: The Ipv6 extension header field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'], value)

    @property
    def Ipv6ExtHeaderMask(self):
        """
        Returns
        -------
        - str: The mask value of the IPv6 Extension Header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeaderMask'])
    @Ipv6ExtHeaderMask.setter
    def Ipv6ExtHeaderMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ExtHeaderMask'], value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: Value of the IPv6 flow label field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'], value)

    @property
    def Ipv6FlowLabelMask(self):
        """
        Returns
        -------
        - str: Value of the IPv6 flow label mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabelMask'])
    @Ipv6FlowLabelMask.setter
    def Ipv6FlowLabelMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabelMask'], value)

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - str: The IPv6 ND DLL field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdDll'])
    @Ipv6NdDll.setter
    def Ipv6NdDll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdDll'], value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: The source link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdSll'])
    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdSll'], value)

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: The IPv6 ND target field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'])
    @Ipv6NdTarget.setter
    def Ipv6NdTarget(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'], value)

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
    def Ipv6SourceMask(self):
        """
        Returns
        -------
        - str: The mask value of IPv6 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6SourceMask'])
    @Ipv6SourceMask.setter
    def Ipv6SourceMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6SourceMask'], value)

    @property
    def MatchType(self):
        """
        Returns
        -------
        - str(loose | strict): The type of match to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchType'])
    @MatchType.setter
    def MatchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchType'], value)

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: Specify the table metadata value used to pass information between tables.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metadata'])
    @Metadata.setter
    def Metadata(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metadata'], value)

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: Specify the metadata bitmask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMask'])
    @MetadataMask.setter
    def MetadataMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetadataMask'], value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - str: Value of the MPLS BoS field.
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
        - str: Value of the MPLS label field.
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
        - str: The MPLS TC field value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTc'], value)

    @property
    def NoByteCounts(self):
        """
        Returns
        -------
        - bool: If selected, the byte count is not tracked anymore.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoByteCounts'])
    @NoByteCounts.setter
    def NoByteCounts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoByteCounts'], value)

    @property
    def NoPacketCounts(self):
        """
        Returns
        -------
        - bool: If selected, the packet count is not tracked anymore.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoPacketCounts'])
    @NoPacketCounts.setter
    def NoPacketCounts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoPacketCounts'], value)

    @property
    def NumberOfFlows(self):
        """
        Returns
        -------
        - number: Total number of flows in a flow range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfFlows'])
    @NumberOfFlows.setter
    def NumberOfFlows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfFlows'], value)

    @property
    def PbbIsId(self):
        """
        Returns
        -------
        - str: Value of the PBB I-SID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsId'])
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbIsId'], value)

    @property
    def PbbIsIdMask(self):
        """
        Returns
        -------
        - str: Value of the PBB I-SID mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsIdMask'])
    @PbbIsIdMask.setter
    def PbbIsIdMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PbbIsIdMask'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: The priority level for the Flow Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def ResetCounts(self):
        """
        Returns
        -------
        - bool: If selected, flow packet and byte counts are reset.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResetCounts'])
    @ResetCounts.setter
    def ResetCounts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResetCounts'], value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - str: The SCTP destination field value.
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
        - str: Value of the SCTP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SctpSource'], value)

    @property
    def SendFlowRemoved(self):
        """
        Returns
        -------
        - bool: If selected, Flow Remove message is sent to the controller, when the Flow entry is deleted from the Flow table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendFlowRemoved'])
    @SendFlowRemoved.setter
    def SendFlowRemoved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendFlowRemoved'], value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - str: The Transport destination address.
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
        - str: Value of the TCP source field.
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
    def TunnelIdMask(self):
        """
        Returns
        -------
        - str: Value of the tunnel ID mask field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdMask'])
    @TunnelIdMask.setter
    def TunnelIdMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIdMask'], value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - str: Value of the UDP destination field.
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
        - str: Value of the UDP source field.
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
        - str: The unique VLAN Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanIdMask(self):
        """
        Returns
        -------
        - str: The VLAN mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIdMask'])
    @VlanIdMask.setter
    def VlanIdMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIdMask'], value)

    @property
    def VlanMatchType(self):
        """
        Returns
        -------
        - str(anyVlanTag | withoutVlanTag | withVlanTag | specificVlanTag): The type of VLAN match to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanMatchType'])
    @VlanMatchType.setter
    def VlanMatchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanMatchType'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: The User Priority for this VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

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
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

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
