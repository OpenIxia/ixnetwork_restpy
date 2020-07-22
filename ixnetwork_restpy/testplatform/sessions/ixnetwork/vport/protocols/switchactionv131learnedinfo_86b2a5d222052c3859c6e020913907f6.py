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


class SwitchActionV131LearnedInfo(Base):
    """This object allows to configure switch action V131 learned Information for OpenFlow.
    The SwitchActionV131LearnedInfo class encapsulates a list of switchActionV131LearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchActionV131LearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchActionV131LearnedInfo'
    _SDM_ATT_MAP = {
        'ActionType': 'actionType',
        'ArpDstHwAddress': 'arpDstHwAddress',
        'ArpDstIpv4Address': 'arpDstIpv4Address',
        'ArpOpcode': 'arpOpcode',
        'ArpSrcHwAddress': 'arpSrcHwAddress',
        'ArpSrcIpv4Address': 'arpSrcIpv4Address',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'EthernetType': 'ethernetType',
        'Experimenter': 'experimenter',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDatalength': 'experimenterDatalength',
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
        'Ipv6NdTarget': 'ipv6NdTarget',
        'Ipv6NdTll': 'ipv6NdTll',
        'Ipv6Source': 'ipv6Source',
        'MaxByteLength': 'maxByteLength',
        'MplsBos': 'mplsBos',
        'MplsLabel': 'mplsLabel',
        'MplsTc': 'mplsTc',
        'MplsTtl': 'mplsTtl',
        'NetworkTtl': 'networkTtl',
        'OutputPort': 'outputPort',
        'OutputPortType': 'outputPortType',
        'PbbIsid': 'pbbIsid',
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
        super(SwitchActionV131LearnedInfo, self).__init__(parent)

    @property
    def ActionType(self):
        """
        Returns
        -------
        - str: This describes the action associated with the flow entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionType'])

    @property
    def ArpDstHwAddress(self):
        """
        Returns
        -------
        - str: This describes the target hardware address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstHwAddress'])

    @property
    def ArpDstIpv4Address(self):
        """
        Returns
        -------
        - number: This describes the target IPv4 address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4Address'])

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - number: This describes the ARP opcode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpOpcode'])

    @property
    def ArpSrcHwAddress(self):
        """
        Returns
        -------
        - str: This describes the source hardware address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcHwAddress'])

    @property
    def ArpSrcIpv4Address(self):
        """
        Returns
        -------
        - number: This describes the source IPv4 address in the ARP payload.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Address'])

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: This describes the destination address of the Ethernet port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: This describes the source address of the Ethernet port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: This describes the Ethernet type of the flow match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: This describes the unique Experimenter identifier. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: This describes the data of the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])

    @property
    def ExperimenterDatalength(self):
        """
        Returns
        -------
        - number: This describes the data length of the Experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDatalength'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - number: This describes the ICMP code.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Code'])

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - number: This describes the ICMP type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Type'])

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - number: This describes the ICMPv6 code.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Code'])

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - number: This describes the ICMPv6 type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: This describes the IP DSCP value for advertising.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - number: This describes the ECN bits of the IP header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpEcn'])

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - number: This describes the IP Protocol used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: This describes the IPv4 destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: This describes the IPv4 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: This describes the IPv6 destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Destination'])

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - number: This describes the IPv6 Extension Header pseudo-field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - number: This describes the IPv6 Flow label.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: This describes the source link-layer address option in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdSll'])

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: This describes the target address in an IPv6 Neighbor Discovery message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'])

    @property
    def Ipv6NdTll(self):
        """
        Returns
        -------
        - str: This describes the target link-layer address option in an IPv6 Neighbor Discovery message
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTll'])

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: This describes the IPv6 source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Source'])

    @property
    def MaxByteLength(self):
        """
        Returns
        -------
        - number: This describes the maximum amount of data from a packet that should be sent when the port is OFPP_CONTROLLER.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxByteLength'])

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - number: This describes the BoS bit in the first MPLS shim header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsBos'])

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - number: This describes the LABEL in the first MPLS shim header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - number: This describes the TC in the first MPLS shim header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])

    @property
    def MplsTtl(self):
        """
        Returns
        -------
        - number: This replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTtl'])

    @property
    def NetworkTtl(self):
        """
        Returns
        -------
        - number: This describes the IP TTL.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkTtl'])

    @property
    def OutputPort(self):
        """
        Returns
        -------
        - number: This describes the out port value. It requires matching entries to include this as an output port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPort'])

    @property
    def OutputPortType(self):
        """
        Returns
        -------
        - str: This describes the Output Port Type for this Flow Range
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPortType'])

    @property
    def PbbIsid(self):
        """
        Returns
        -------
        - number: This describes the I-SID in the first PBB service instance tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsid'])

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: This describes the queue of the port in which the packet should be enqueued.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - number: This describes the SCTP target port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpDestination'])

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - number: This describes the SCTP source port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - number: This describes the TCP destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpDestination'])

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - number: This describes the TCP source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpSource'])

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: This describes the unique identifier used for the Tunnel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - number: This describes the UDP destination port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestination'])

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - number: This describes the UDP source port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: This describes the unique VLAN Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: This describes the User Priority for this VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])

    def find(self, ActionType=None, ArpDstHwAddress=None, ArpDstIpv4Address=None, ArpOpcode=None, ArpSrcHwAddress=None, ArpSrcIpv4Address=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6NdTll=None, Ipv6Source=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NetworkTtl=None, OutputPort=None, OutputPortType=None, PbbIsid=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves switchActionV131LearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchActionV131LearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchActionV131LearnedInfo resources from the server.

        Args
        ----
        - ActionType (str): This describes the action associated with the flow entry.
        - ArpDstHwAddress (str): This describes the target hardware address in the ARP payload.
        - ArpDstIpv4Address (number): This describes the target IPv4 address in the ARP payload.
        - ArpOpcode (number): This describes the ARP opcode.
        - ArpSrcHwAddress (str): This describes the source hardware address in the ARP payload.
        - ArpSrcIpv4Address (number): This describes the source IPv4 address in the ARP payload.
        - EthernetDestination (str): This describes the destination address of the Ethernet port.
        - EthernetSource (str): This describes the source address of the Ethernet port.
        - EthernetType (str): This describes the Ethernet type of the flow match.
        - Experimenter (number): This describes the unique Experimenter identifier. The default value is 1.
        - ExperimenterData (str): This describes the data of the Experimenter.
        - ExperimenterDatalength (number): This describes the data length of the Experimenter.
        - GroupId (number): NOT DEFINED
        - Icmpv4Code (number): This describes the ICMP code.
        - Icmpv4Type (number): This describes the ICMP type.
        - Icmpv6Code (number): This describes the ICMPv6 code.
        - Icmpv6Type (number): This describes the ICMPv6 type.
        - IpDscp (str): This describes the IP DSCP value for advertising.
        - IpEcn (number): This describes the ECN bits of the IP header.
        - IpProtocol (number): This describes the IP Protocol used.
        - Ipv4Destination (str): This describes the IPv4 destination address.
        - Ipv4Source (str): This describes the IPv4 source address.
        - Ipv6Destination (str): This describes the IPv6 destination address.
        - Ipv6ExtHeader (number): This describes the IPv6 Extension Header pseudo-field.
        - Ipv6FlowLabel (number): This describes the IPv6 Flow label.
        - Ipv6NdSll (str): This describes the source link-layer address option in an IPv6 Neighbor Discovery message.
        - Ipv6NdTarget (str): This describes the target address in an IPv6 Neighbor Discovery message.
        - Ipv6NdTll (str): This describes the target link-layer address option in an IPv6 Neighbor Discovery message
        - Ipv6Source (str): This describes the IPv6 source address.
        - MaxByteLength (number): This describes the maximum amount of data from a packet that should be sent when the port is OFPP_CONTROLLER.
        - MplsBos (number): This describes the BoS bit in the first MPLS shim header.
        - MplsLabel (number): This describes the LABEL in the first MPLS shim header.
        - MplsTc (number): This describes the TC in the first MPLS shim header.
        - MplsTtl (number): This replaces the existing MPLS TTL. Only applies to packets with an existing MPLS shim header.
        - NetworkTtl (number): This describes the IP TTL.
        - OutputPort (number): This describes the out port value. It requires matching entries to include this as an output port.
        - OutputPortType (str): This describes the Output Port Type for this Flow Range
        - PbbIsid (number): This describes the I-SID in the first PBB service instance tag.
        - QueueId (number): This describes the queue of the port in which the packet should be enqueued.
        - SctpDestination (number): This describes the SCTP target port.
        - SctpSource (number): This describes the SCTP source port.
        - TcpDestination (number): This describes the TCP destination address.
        - TcpSource (number): This describes the TCP source address.
        - TunnelId (str): This describes the unique identifier used for the Tunnel.
        - UdpDestination (number): This describes the UDP destination port.
        - UdpSource (number): This describes the UDP source port.
        - VlanId (number): This describes the unique VLAN Identifier.
        - VlanPriority (number): This describes the User Priority for this VLAN.

        Returns
        -------
        - self: This instance with matching switchActionV131LearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchActionV131LearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchActionV131LearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
