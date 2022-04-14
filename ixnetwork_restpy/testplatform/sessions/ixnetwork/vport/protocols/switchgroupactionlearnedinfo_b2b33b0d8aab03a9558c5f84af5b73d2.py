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


class SwitchGroupActionLearnedInfo(Base):
    """NOT DEFINED
    The SwitchGroupActionLearnedInfo class encapsulates a list of switchGroupActionLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupActionLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "switchGroupActionLearnedInfo"
    _SDM_ATT_MAP = {
        "ActionType": "actionType",
        "ArpDestinationHwAddress": "arpDestinationHwAddress",
        "ArpDstIpv4Address": "arpDstIpv4Address",
        "ArpOpcode": "arpOpcode",
        "ArpSourceHwAddress": "arpSourceHwAddress",
        "ArpSrcIpv4Address": "arpSrcIpv4Address",
        "EthernetDestination": "ethernetDestination",
        "EthernetSource": "ethernetSource",
        "EthernetType": "ethernetType",
        "Experimenter": "experimenter",
        "ExperimenterData": "experimenterData",
        "ExperimenterDatalength": "experimenterDatalength",
        "GroupId": "groupId",
        "Icmpv4Code": "icmpv4Code",
        "Icmpv4Type": "icmpv4Type",
        "Icmpv6Code": "icmpv6Code",
        "Icmpv6Type": "icmpv6Type",
        "IpDscp": "ipDscp",
        "IpEcn": "ipEcn",
        "IpProto": "ipProto",
        "Ipv4Destination": "ipv4Destination",
        "Ipv4Source": "ipv4Source",
        "Ipv6Destination": "ipv6Destination",
        "Ipv6ExtHeader": "ipv6ExtHeader",
        "Ipv6FlowLabel": "ipv6FlowLabel",
        "Ipv6NdSll": "ipv6NdSll",
        "Ipv6NdTarget": "ipv6NdTarget",
        "Ipv6NdTll": "ipv6NdTll",
        "Ipv6Source": "ipv6Source",
        "MaxByteLength": "maxByteLength",
        "MplsBos": "mplsBos",
        "MplsLabel": "mplsLabel",
        "MplsTc": "mplsTc",
        "MplsTtl": "mplsTtl",
        "NetworkTtl": "networkTtl",
        "OutputPort": "outputPort",
        "OutputPortType": "outputPortType",
        "PbbIsid": "pbbIsid",
        "QueueId": "queueId",
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
        super(SwitchGroupActionLearnedInfo, self).__init__(parent, list_op)

    @property
    def ActionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActionType"])

    @property
    def ArpDestinationHwAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDestinationHwAddress"])

    @property
    def ArpDstIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpDstIpv4Address"])

    @property
    def ArpOpcode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpOpcode"])

    @property
    def ArpSourceHwAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSourceHwAddress"])

    @property
    def ArpSrcIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSrcIpv4Address"])

    @property
    def EthernetDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetDestination"])

    @property
    def EthernetSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetSource"])

    @property
    def EthernetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @property
    def Experimenter(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Experimenter"])

    @property
    def ExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterData"])

    @property
    def ExperimenterDatalength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterDatalength"])

    @property
    def GroupId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupId"])

    @property
    def Icmpv4Code(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv4Code"])

    @property
    def Icmpv4Type(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv4Type"])

    @property
    def Icmpv6Code(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Code"])

    @property
    def Icmpv6Type(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Type"])

    @property
    def IpDscp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDscp"])

    @property
    def IpEcn(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpEcn"])

    @property
    def IpProto(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpProto"])

    @property
    def Ipv4Destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Destination"])

    @property
    def Ipv4Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Source"])

    @property
    def Ipv6Destination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Destination"])

    @property
    def Ipv6ExtHeader(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6ExtHeader"])

    @property
    def Ipv6FlowLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"])

    @property
    def Ipv6NdSll(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdSll"])

    @property
    def Ipv6NdTarget(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdTarget"])

    @property
    def Ipv6NdTll(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NdTll"])

    @property
    def Ipv6Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Source"])

    @property
    def MaxByteLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxByteLength"])

    @property
    def MplsBos(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsBos"])

    @property
    def MplsLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabel"])

    @property
    def MplsTc(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsTc"])

    @property
    def MplsTtl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsTtl"])

    @property
    def NetworkTtl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkTtl"])

    @property
    def OutputPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutputPort"])

    @property
    def OutputPortType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutputPortType"])

    @property
    def PbbIsid(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsid"])

    @property
    def QueueId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueId"])

    @property
    def SctpDestination(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SctpDestination"])

    @property
    def SctpSource(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SctpSource"])

    @property
    def TcpDestination(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpDestination"])

    @property
    def TcpSource(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpSource"])

    @property
    def TunnelId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelId"])

    @property
    def UdpDestination(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpDestination"])

    @property
    def UdpSource(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSource"])

    @property
    def VlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @property
    def VlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    def add(self):
        """Adds a new switchGroupActionLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved switchGroupActionLearnedInfo resources using find and the newly added switchGroupActionLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActionType=None,
        ArpDestinationHwAddress=None,
        ArpDstIpv4Address=None,
        ArpOpcode=None,
        ArpSourceHwAddress=None,
        ArpSrcIpv4Address=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        Experimenter=None,
        ExperimenterData=None,
        ExperimenterDatalength=None,
        GroupId=None,
        Icmpv4Code=None,
        Icmpv4Type=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
        IpDscp=None,
        IpEcn=None,
        IpProto=None,
        Ipv4Destination=None,
        Ipv4Source=None,
        Ipv6Destination=None,
        Ipv6ExtHeader=None,
        Ipv6FlowLabel=None,
        Ipv6NdSll=None,
        Ipv6NdTarget=None,
        Ipv6NdTll=None,
        Ipv6Source=None,
        MaxByteLength=None,
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        MplsTtl=None,
        NetworkTtl=None,
        OutputPort=None,
        OutputPortType=None,
        PbbIsid=None,
        QueueId=None,
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
        # type: (str, str, str, int, str, str, str, str, str, int, str, int, int, int, int, int, int, str, int, int, str, str, str, int, int, str, str, str, str, int, int, int, int, int, int, int, str, int, int, int, int, int, int, str, int, int, int, int) -> SwitchGroupActionLearnedInfo
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
