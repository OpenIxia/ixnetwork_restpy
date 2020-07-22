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


class SwitchGroupActionLearnedInfo(Base):
    """NOT DEFINED
    The SwitchGroupActionLearnedInfo class encapsulates a list of switchGroupActionLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupActionLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchGroupActionLearnedInfo'
    _SDM_ATT_MAP = {
        'ActionType': 'actionType',
        'ArpDestinationHwAddress': 'arpDestinationHwAddress',
        'ArpDstIpv4Address': 'arpDstIpv4Address',
        'ArpOpcode': 'arpOpcode',
        'ArpSourceHwAddress': 'arpSourceHwAddress',
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
        'IpProto': 'ipProto',
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
        super(SwitchGroupActionLearnedInfo, self).__init__(parent)

    @property
    def ActionType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionType'])

    @property
    def ArpDestinationHwAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDestinationHwAddress'])

    @property
    def ArpDstIpv4Address(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpDstIpv4Address'])

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpOpcode'])

    @property
    def ArpSourceHwAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSourceHwAddress'])

    @property
    def ArpSrcIpv4Address(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpSrcIpv4Address'])

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])

    @property
    def ExperimenterDatalength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Code'])

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv4Type'])

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Code'])

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6Type'])

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpEcn'])

    @property
    def IpProto(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProto'])

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Destination'])

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ExtHeader'])

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdSll'])

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTarget'])

    @property
    def Ipv6NdTll(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6NdTll'])

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Source'])

    @property
    def MaxByteLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxByteLength'])

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsBos'])

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTc'])

    @property
    def MplsTtl(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTtl'])

    @property
    def NetworkTtl(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkTtl'])

    @property
    def OutputPort(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPort'])

    @property
    def OutputPortType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPortType'])

    @property
    def PbbIsid(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbIsid'])

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpDestination'])

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SctpSource'])

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpDestination'])

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpSource'])

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelId'])

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestination'])

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])

    def find(self, ActionType=None, ArpDestinationHwAddress=None, ArpDstIpv4Address=None, ArpOpcode=None, ArpSourceHwAddress=None, ArpSrcIpv4Address=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, ExperimenterData=None, ExperimenterDatalength=None, GroupId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, IpDscp=None, IpEcn=None, IpProto=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6NdTll=None, Ipv6Source=None, MaxByteLength=None, MplsBos=None, MplsLabel=None, MplsTc=None, MplsTtl=None, NetworkTtl=None, OutputPort=None, OutputPortType=None, PbbIsid=None, QueueId=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves switchGroupActionLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchGroupActionLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchGroupActionLearnedInfo resources from the server.

        Args
        ----
        - ActionType (str): NOT DEFINED
        - ArpDestinationHwAddress (str): NOT DEFINED
        - ArpDstIpv4Address (str): NOT DEFINED
        - ArpOpcode (number): NOT DEFINED
        - ArpSourceHwAddress (str): NOT DEFINED
        - ArpSrcIpv4Address (str): NOT DEFINED
        - EthernetDestination (str): NOT DEFINED
        - EthernetSource (str): NOT DEFINED
        - EthernetType (str): NOT DEFINED
        - Experimenter (number): NOT DEFINED
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDatalength (number): NOT DEFINED
        - GroupId (number): NOT DEFINED
        - Icmpv4Code (number): NOT DEFINED
        - Icmpv4Type (number): NOT DEFINED
        - Icmpv6Code (number): NOT DEFINED
        - Icmpv6Type (number): NOT DEFINED
        - IpDscp (str): NOT DEFINED
        - IpEcn (number): NOT DEFINED
        - IpProto (number): NOT DEFINED
        - Ipv4Destination (str): NOT DEFINED
        - Ipv4Source (str): NOT DEFINED
        - Ipv6Destination (str): NOT DEFINED
        - Ipv6ExtHeader (number): NOT DEFINED
        - Ipv6FlowLabel (number): NOT DEFINED
        - Ipv6NdSll (str): NOT DEFINED
        - Ipv6NdTarget (str): NOT DEFINED
        - Ipv6NdTll (str): NOT DEFINED
        - Ipv6Source (str): NOT DEFINED
        - MaxByteLength (number): NOT DEFINED
        - MplsBos (number): NOT DEFINED
        - MplsLabel (number): NOT DEFINED
        - MplsTc (number): NOT DEFINED
        - MplsTtl (number): NOT DEFINED
        - NetworkTtl (number): NOT DEFINED
        - OutputPort (number): NOT DEFINED
        - OutputPortType (str): NOT DEFINED
        - PbbIsid (number): NOT DEFINED
        - QueueId (number): NOT DEFINED
        - SctpDestination (number): NOT DEFINED
        - SctpSource (number): NOT DEFINED
        - TcpDestination (number): NOT DEFINED
        - TcpSource (number): NOT DEFINED
        - TunnelId (str): NOT DEFINED
        - UdpDestination (number): NOT DEFINED
        - UdpSource (number): NOT DEFINED
        - VlanId (number): NOT DEFINED
        - VlanPriority (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchGroupActionLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchGroupActionLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchGroupActionLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
