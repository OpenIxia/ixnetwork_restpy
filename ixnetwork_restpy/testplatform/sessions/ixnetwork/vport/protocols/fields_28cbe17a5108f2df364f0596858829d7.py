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


class Fields(Base):
    """NOT DEFINED
    The Fields class encapsulates a required fields resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fields"
    _SDM_ATT_MAP = {
        "ArpDestinationIpv4Address": "arpDestinationIpv4Address",
        "ArpOpcode": "arpOpcode",
        "ArpSourceHardwareAddress": "arpSourceHardwareAddress",
        "ArpSourceIpv4Address": "arpSourceIpv4Address",
        "ArpTargetHardwareAddress": "arpTargetHardwareAddress",
        "EthernetDestination": "ethernetDestination",
        "EthernetSource": "ethernetSource",
        "EthernetType": "ethernetType",
        "IcmpCode": "icmpCode",
        "IcmpType": "icmpType",
        "Icmpv6Code": "icmpv6Code",
        "Icmpv6Type": "icmpv6Type",
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
        "MplsBos": "mplsBos",
        "MplsLabel": "mplsLabel",
        "MplsTc": "mplsTc",
        "PbbIsid": "pbbIsid",
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
        super(Fields, self).__init__(parent, list_op)

    @property
    def ArpDestinationIpv4Address(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpSourceIpv4Address"])

    @ArpSourceIpv4Address.setter
    def ArpSourceIpv4Address(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpSourceIpv4Address"], value)

    @property
    def ArpTargetHardwareAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpTargetHardwareAddress"])

    @ArpTargetHardwareAddress.setter
    def ArpTargetHardwareAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpTargetHardwareAddress"], value)

    @property
    def EthernetDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetType"])

    @EthernetType.setter
    def EthernetType(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetType"], value)

    @property
    def IcmpCode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Icmpv6Type"])

    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Icmpv6Type"], value)

    @property
    def IpDscp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Source"])

    @Ipv6Source.setter
    def Ipv6Source(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Source"], value)

    @property
    def MplsBos(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsid"])

    @PbbIsid.setter
    def PbbIsid(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbIsid"], value)

    @property
    def SctpDestination(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        ArpDestinationIpv4Address=None,
        ArpOpcode=None,
        ArpSourceHardwareAddress=None,
        ArpSourceIpv4Address=None,
        ArpTargetHardwareAddress=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        IcmpCode=None,
        IcmpType=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
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
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        PbbIsid=None,
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
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Fields
        """Updates fields resource on the server.

        Args
        ----
        - ArpDestinationIpv4Address (bool): NOT DEFINED
        - ArpOpcode (bool): NOT DEFINED
        - ArpSourceHardwareAddress (bool): NOT DEFINED
        - ArpSourceIpv4Address (bool): NOT DEFINED
        - ArpTargetHardwareAddress (bool): NOT DEFINED
        - EthernetDestination (bool): NOT DEFINED
        - EthernetSource (bool): NOT DEFINED
        - EthernetType (bool): NOT DEFINED
        - IcmpCode (bool): NOT DEFINED
        - IcmpType (bool): NOT DEFINED
        - Icmpv6Code (bool): NOT DEFINED
        - Icmpv6Type (bool): NOT DEFINED
        - IpDscp (bool): NOT DEFINED
        - IpEcn (bool): NOT DEFINED
        - IpProtocol (bool): NOT DEFINED
        - Ipv4Destination (bool): NOT DEFINED
        - Ipv4Source (bool): NOT DEFINED
        - Ipv6Destination (bool): NOT DEFINED
        - Ipv6ExtHeader (bool): NOT DEFINED
        - Ipv6FlowLabel (bool): NOT DEFINED
        - Ipv6NdSll (bool): NOT DEFINED
        - Ipv6NdTarget (bool): NOT DEFINED
        - Ipv6NdTll (bool): NOT DEFINED
        - Ipv6Source (bool): NOT DEFINED
        - MplsBos (bool): NOT DEFINED
        - MplsLabel (bool): NOT DEFINED
        - MplsTc (bool): NOT DEFINED
        - PbbIsid (bool): NOT DEFINED
        - SctpDestination (bool): NOT DEFINED
        - SctpSource (bool): NOT DEFINED
        - TcpDestination (bool): NOT DEFINED
        - TcpSource (bool): NOT DEFINED
        - TunnelId (bool): NOT DEFINED
        - UdpDestination (bool): NOT DEFINED
        - UdpSource (bool): NOT DEFINED
        - VlanId (bool): NOT DEFINED
        - VlanPriority (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ArpDestinationIpv4Address=None,
        ArpOpcode=None,
        ArpSourceHardwareAddress=None,
        ArpSourceIpv4Address=None,
        ArpTargetHardwareAddress=None,
        EthernetDestination=None,
        EthernetSource=None,
        EthernetType=None,
        IcmpCode=None,
        IcmpType=None,
        Icmpv6Code=None,
        Icmpv6Type=None,
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
        MplsBos=None,
        MplsLabel=None,
        MplsTc=None,
        PbbIsid=None,
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
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Fields
        """Finds and retrieves fields resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fields resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fields resources from the server.

        Args
        ----
        - ArpDestinationIpv4Address (bool): NOT DEFINED
        - ArpOpcode (bool): NOT DEFINED
        - ArpSourceHardwareAddress (bool): NOT DEFINED
        - ArpSourceIpv4Address (bool): NOT DEFINED
        - ArpTargetHardwareAddress (bool): NOT DEFINED
        - EthernetDestination (bool): NOT DEFINED
        - EthernetSource (bool): NOT DEFINED
        - EthernetType (bool): NOT DEFINED
        - IcmpCode (bool): NOT DEFINED
        - IcmpType (bool): NOT DEFINED
        - Icmpv6Code (bool): NOT DEFINED
        - Icmpv6Type (bool): NOT DEFINED
        - IpDscp (bool): NOT DEFINED
        - IpEcn (bool): NOT DEFINED
        - IpProtocol (bool): NOT DEFINED
        - Ipv4Destination (bool): NOT DEFINED
        - Ipv4Source (bool): NOT DEFINED
        - Ipv6Destination (bool): NOT DEFINED
        - Ipv6ExtHeader (bool): NOT DEFINED
        - Ipv6FlowLabel (bool): NOT DEFINED
        - Ipv6NdSll (bool): NOT DEFINED
        - Ipv6NdTarget (bool): NOT DEFINED
        - Ipv6NdTll (bool): NOT DEFINED
        - Ipv6Source (bool): NOT DEFINED
        - MplsBos (bool): NOT DEFINED
        - MplsLabel (bool): NOT DEFINED
        - MplsTc (bool): NOT DEFINED
        - PbbIsid (bool): NOT DEFINED
        - SctpDestination (bool): NOT DEFINED
        - SctpSource (bool): NOT DEFINED
        - TcpDestination (bool): NOT DEFINED
        - TcpSource (bool): NOT DEFINED
        - TunnelId (bool): NOT DEFINED
        - UdpDestination (bool): NOT DEFINED
        - UdpSource (bool): NOT DEFINED
        - VlanId (bool): NOT DEFINED
        - VlanPriority (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with matching fields resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fields data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fields resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
