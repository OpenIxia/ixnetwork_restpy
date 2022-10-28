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


class TrafficEndPoint(Base):
    """Specifies the Traffic Endpoints added to the grid.
    The TrafficEndPoint class encapsulates a list of trafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficEndPoint.find() method.
    The list can be managed by using the TrafficEndPoint.add() and TrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "trafficEndPoint"
    _SDM_ATT_MAP = {
        "ArpViaInterface": "arpViaInterface",
        "CustomEtherHeaderLength": "customEtherHeaderLength",
        "CustomEtherHeaderValue": "customEtherHeaderValue",
        "CustomEtherType": "customEtherType",
        "CustomIpHeaderLength": "customIpHeaderLength",
        "CustomIpHeaderValue": "customIpHeaderValue",
        "CustomIpProtocol": "customIpProtocol",
        "DestinationPort": "destinationPort",
        "EnableMacInMac": "enableMacInMac",
        "EnableVlan": "enableVlan",
        "EtherType": "etherType",
        "GatewayMac": "gatewayMac",
        "IpAddress": "ipAddress",
        "IpMask": "ipMask",
        "IpProtocol": "ipProtocol",
        "IpTos": "ipTos",
        "Ipv4Dscp": "ipv4Dscp",
        "Ipv4Ecn": "ipv4Ecn",
        "Ipv6Address": "ipv6Address",
        "Ipv6AddressMask": "ipv6AddressMask",
        "Ipv6CustomHeaderLength": "ipv6CustomHeaderLength",
        "Ipv6CustomHeaderValue": "ipv6CustomHeaderValue",
        "Ipv6CustomNextHeader": "ipv6CustomNextHeader",
        "Ipv6Dscp": "ipv6Dscp",
        "Ipv6Ecn": "ipv6Ecn",
        "Ipv6FlowLabel": "ipv6FlowLabel",
        "Ipv6NextHeader": "ipv6NextHeader",
        "MacAddress": "macAddress",
        "MplsInnerMacSource": "mplsInnerMacSource",
        "MplsInnerVlanId": "mplsInnerVlanId",
        "MplsInnerVlanPriority": "mplsInnerVlanPriority",
        "MplsLabel": "mplsLabel",
        "MplsLabelStackSize": "mplsLabelStackSize",
        "MplsPayloadType": "mplsPayloadType",
        "MplsTrafficClass": "mplsTrafficClass",
        "Name": "name",
        "PbbDestinamtionMac": "pbbDestinamtionMac",
        "PbbEtherType": "pbbEtherType",
        "PbbIsId": "pbbIsId",
        "PbbSourceMac": "pbbSourceMac",
        "PbbVlanId": "pbbVlanId",
        "PbbVlanPcp": "pbbVlanPcp",
        "ProtocolInterface": "protocolInterface",
        "RangeSize": "rangeSize",
        "SourcePort": "sourcePort",
        "UdpDestination": "udpDestination",
        "UdpSource": "udpSource",
        "VlanCount": "vlanCount",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {
        "etherType": ["custom", "ipv4", "ipv6", "mplsUnicast"],
        "ipProtocol": ["custom", "tcp", "udp"],
        "ipv6NextHeader": ["custom", "tcp", "udp"],
        "mplsPayloadType": ["ethernet", "ipv4", "ipv6"],
        "pbbEtherType": [
            "bEtherType8100",
            "bEtherType88A8",
            "bEtherType88E7",
            "bEtherType9100",
            "bEtherType9200",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(TrafficEndPoint, self).__init__(parent, list_op)

    @property
    def ArpViaInterface(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, ARP request is conveyed through an Interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpViaInterface"])

    @ArpViaInterface.setter
    def ArpViaInterface(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpViaInterface"], value)

    @property
    def CustomEtherHeaderLength(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the Custom Header length in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomEtherHeaderLength"])

    @CustomEtherHeaderLength.setter
    def CustomEtherHeaderLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomEtherHeaderLength"], value)

    @property
    def CustomEtherHeaderValue(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the Custom ether Header value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomEtherHeaderValue"])

    @CustomEtherHeaderValue.setter
    def CustomEtherHeaderValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomEtherHeaderValue"], value)

    @property
    def CustomEtherType(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomEtherType"])

    @CustomEtherType.setter
    def CustomEtherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomEtherType"], value)

    @property
    def CustomIpHeaderLength(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the custom Header length in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomIpHeaderLength"])

    @CustomIpHeaderLength.setter
    def CustomIpHeaderLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomIpHeaderLength"], value)

    @property
    def CustomIpHeaderValue(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the Custom Header value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomIpHeaderValue"])

    @CustomIpHeaderValue.setter
    def CustomIpHeaderValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomIpHeaderValue"], value)

    @property
    def CustomIpProtocol(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomIpProtocol"])

    @CustomIpProtocol.setter
    def CustomIpProtocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomIpProtocol"], value)

    @property
    def DestinationPort(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationPort"])

    @DestinationPort.setter
    def DestinationPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationPort"], value)

    @property
    def EnableMacInMac(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Enables the PBB-specific fields.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMacInMac"])

    @EnableMacInMac.setter
    def EnableMacInMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMacInMac"], value)

    @property
    def EnableVlan(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If enabled, VLAN is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVlan"])

    @EnableVlan.setter
    def EnableVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVlan"], value)

    @property
    def EtherType(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(custom | ipv4 | ipv6 | mplsUnicast): Specifies the Ether Type to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EtherType"])

    @EtherType.setter
    def EtherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EtherType"], value)

    @property
    def GatewayMac(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayMac"])

    @GatewayMac.setter
    def GatewayMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayMac"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpMask(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the Mask value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpMask"])

    @IpMask.setter
    def IpMask(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpMask"], value)

    @property
    def IpProtocol(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(custom | tcp | udp): Specifies the IP Protocol to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpProtocol"])

    @IpProtocol.setter
    def IpProtocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpProtocol"], value)

    @property
    def IpTos(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpTos"])

    @IpTos.setter
    def IpTos(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpTos"], value)

    @property
    def Ipv4Dscp(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies value of Ipv4 DSCP field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Dscp"])

    @Ipv4Dscp.setter
    def Ipv4Dscp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Dscp"], value)

    @property
    def Ipv4Ecn(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Ecn"])

    @Ipv4Ecn.setter
    def Ipv4Ecn(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Ecn"], value)

    @property
    def Ipv6Address(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv6 address to be used in the traffic endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Address"])

    @Ipv6Address.setter
    def Ipv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Address"], value)

    @property
    def Ipv6AddressMask(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the mask of IPv6 address
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6AddressMask"])

    @Ipv6AddressMask.setter
    def Ipv6AddressMask(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6AddressMask"], value)

    @property
    def Ipv6CustomHeaderLength(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderLength"])

    @Ipv6CustomHeaderLength.setter
    def Ipv6CustomHeaderLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderLength"], value)

    @property
    def Ipv6CustomHeaderValue(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderValue"])

    @Ipv6CustomHeaderValue.setter
    def Ipv6CustomHeaderValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderValue"], value)

    @property
    def Ipv6CustomNextHeader(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6CustomNextHeader"])

    @Ipv6CustomNextHeader.setter
    def Ipv6CustomNextHeader(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6CustomNextHeader"], value)

    @property
    def Ipv6Dscp(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Dscp"])

    @Ipv6Dscp.setter
    def Ipv6Dscp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Dscp"], value)

    @property
    def Ipv6Ecn(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Ecn"])

    @Ipv6Ecn.setter
    def Ipv6Ecn(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Ecn"], value)

    @property
    def Ipv6FlowLabel(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the IPv6 flow label field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"])

    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"], value)

    @property
    def Ipv6NextHeader(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(custom | tcp | udp): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NextHeader"])

    @Ipv6NextHeader.setter
    def Ipv6NextHeader(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NextHeader"], value)

    @property
    def MacAddress(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def MplsInnerMacSource(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsInnerMacSource"])

    @MplsInnerMacSource.setter
    def MplsInnerMacSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsInnerMacSource"], value)

    @property
    def MplsInnerVlanId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsInnerVlanId"])

    @MplsInnerVlanId.setter
    def MplsInnerVlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsInnerVlanId"], value)

    @property
    def MplsInnerVlanPriority(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsInnerVlanPriority"])

    @MplsInnerVlanPriority.setter
    def MplsInnerVlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsInnerVlanPriority"], value)

    @property
    def MplsLabel(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Value of the MPLS label field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabel"])

    @MplsLabel.setter
    def MplsLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsLabel"], value)

    @property
    def MplsLabelStackSize(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabelStackSize"])

    @MplsLabelStackSize.setter
    def MplsLabelStackSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsLabelStackSize"], value)

    @property
    def MplsPayloadType(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(ethernet | ipv4 | ipv6): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsPayloadType"])

    @MplsPayloadType.setter
    def MplsPayloadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsPayloadType"], value)

    @property
    def MplsTrafficClass(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the MPLS traffic class.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsTrafficClass"])

    @MplsTrafficClass.setter
    def MplsTrafficClass(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsTrafficClass"], value)

    @property
    def Name(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the name of the Traffic endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def PbbDestinamtionMac(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the B-Destination MAC.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbDestinamtionMac"])

    @PbbDestinamtionMac.setter
    def PbbDestinamtionMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbDestinamtionMac"], value)

    @property
    def PbbEtherType(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200): Specifies the B-Ether Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbEtherType"])

    @PbbEtherType.setter
    def PbbEtherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbEtherType"], value)

    @property
    def PbbIsId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Value of the PBB I-SID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsId"])

    @PbbIsId.setter
    def PbbIsId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbIsId"], value)

    @property
    def PbbSourceMac(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the B-Source MAC.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbSourceMac"])

    @PbbSourceMac.setter
    def PbbSourceMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbSourceMac"], value)

    @property
    def PbbVlanId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the B-VLAN ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbVlanId"])

    @PbbVlanId.setter
    def PbbVlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbVlanId"], value)

    @property
    def PbbVlanPcp(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the B-VLAN priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbVlanPcp"])

    @PbbVlanPcp.setter
    def PbbVlanPcp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbVlanPcp"], value)

    @property
    def ProtocolInterface(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolInterface"])

    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolInterface"], value)

    @property
    def RangeSize(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the size of the traffic range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeSize"])

    @RangeSize.setter
    def RangeSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeSize"], value)

    @property
    def SourcePort(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourcePort"])

    @SourcePort.setter
    def SourcePort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourcePort"], value)

    @property
    def UdpDestination(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Value of the UDP destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpDestination"])

    @UdpDestination.setter
    def UdpDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpDestination"], value)

    @property
    def UdpSource(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Value of the UDP source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSource"])

    @UdpSource.setter
    def UdpSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpSource"], value)

    @property
    def VlanCount(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the VLAN Count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanCount"])

    @VlanCount.setter
    def VlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanCount"], value)

    @property
    def VlanId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        ArpViaInterface=None,
        CustomEtherHeaderLength=None,
        CustomEtherHeaderValue=None,
        CustomEtherType=None,
        CustomIpHeaderLength=None,
        CustomIpHeaderValue=None,
        CustomIpProtocol=None,
        DestinationPort=None,
        EnableMacInMac=None,
        EnableVlan=None,
        EtherType=None,
        GatewayMac=None,
        IpAddress=None,
        IpMask=None,
        IpProtocol=None,
        IpTos=None,
        Ipv4Dscp=None,
        Ipv4Ecn=None,
        Ipv6Address=None,
        Ipv6AddressMask=None,
        Ipv6CustomHeaderLength=None,
        Ipv6CustomHeaderValue=None,
        Ipv6CustomNextHeader=None,
        Ipv6Dscp=None,
        Ipv6Ecn=None,
        Ipv6FlowLabel=None,
        Ipv6NextHeader=None,
        MacAddress=None,
        MplsInnerMacSource=None,
        MplsInnerVlanId=None,
        MplsInnerVlanPriority=None,
        MplsLabel=None,
        MplsLabelStackSize=None,
        MplsPayloadType=None,
        MplsTrafficClass=None,
        Name=None,
        PbbDestinamtionMac=None,
        PbbEtherType=None,
        PbbIsId=None,
        PbbSourceMac=None,
        PbbVlanId=None,
        PbbVlanPcp=None,
        ProtocolInterface=None,
        RangeSize=None,
        SourcePort=None,
        UdpDestination=None,
        UdpSource=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, int, str, str, int, str, str, str, bool, bool, str, str, str, int, str, str, str, str, str, int, int, str, str, str, str, str, str, str, str, str, str, str, int, str, str, str, str, str, str, str, str, str, str, int, str, str, str, int, str, str) -> TrafficEndPoint
        """Updates trafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): If true, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specifies the Custom Header length in bytes.
        - CustomEtherHeaderValue (str): Specifies the Custom ether Header value.
        - CustomEtherType (str): Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - CustomIpHeaderLength (number): Specifies the custom Header length in bytes.
        - CustomIpHeaderValue (str): Specifies the Custom Header value.
        - CustomIpProtocol (str): Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - DestinationPort (str): Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EnableMacInMac (bool): Enables the PBB-specific fields.
        - EnableVlan (bool): If enabled, VLAN is available.
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): Specifies the Ether Type to be used.
        - GatewayMac (str): Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpAddress (str): Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpMask (number): Specifies the Mask value.
        - IpProtocol (str(custom | tcp | udp)): Specifies the IP Protocol to be used.
        - IpTos (str): Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Dscp (str): Specifies value of Ipv4 DSCP field.
        - Ipv4Ecn (str): Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6Address (str): Specifies the IPv6 address to be used in the traffic endpoint.
        - Ipv6AddressMask (number): Specifies the mask of IPv6 address
        - Ipv6CustomHeaderLength (number): Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        - Ipv6CustomHeaderValue (str): Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        - Ipv6CustomNextHeader (str): Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        - Ipv6Dscp (str): Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        - Ipv6Ecn (str): Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6FlowLabel (str): Specifies the IPv6 flow label field.
        - Ipv6NextHeader (str(custom | tcp | udp)): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        - MacAddress (str): Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MplsInnerMacSource (str): Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanId (str): Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanPriority (str): Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsLabelStackSize (number): Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        - MplsTrafficClass (str): Specifies the MPLS traffic class.
        - Name (str): Specifies the name of the Traffic endpoint.
        - PbbDestinamtionMac (str): Specifies the B-Destination MAC.
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): Specifies the B-Ether Type.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbSourceMac (str): Specifies the B-Source MAC.
        - PbbVlanId (str): Specifies the B-VLAN ID.
        - PbbVlanPcp (str): Specifies the B-VLAN priority.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        - RangeSize (number): Specifies the size of the traffic range.
        - SourcePort (str): Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanCount (number): Specifies the VLAN Count.
        - VlanId (str): Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ArpViaInterface=None,
        CustomEtherHeaderLength=None,
        CustomEtherHeaderValue=None,
        CustomEtherType=None,
        CustomIpHeaderLength=None,
        CustomIpHeaderValue=None,
        CustomIpProtocol=None,
        DestinationPort=None,
        EnableMacInMac=None,
        EnableVlan=None,
        EtherType=None,
        GatewayMac=None,
        IpAddress=None,
        IpMask=None,
        IpProtocol=None,
        IpTos=None,
        Ipv4Dscp=None,
        Ipv4Ecn=None,
        Ipv6Address=None,
        Ipv6AddressMask=None,
        Ipv6CustomHeaderLength=None,
        Ipv6CustomHeaderValue=None,
        Ipv6CustomNextHeader=None,
        Ipv6Dscp=None,
        Ipv6Ecn=None,
        Ipv6FlowLabel=None,
        Ipv6NextHeader=None,
        MacAddress=None,
        MplsInnerMacSource=None,
        MplsInnerVlanId=None,
        MplsInnerVlanPriority=None,
        MplsLabel=None,
        MplsLabelStackSize=None,
        MplsPayloadType=None,
        MplsTrafficClass=None,
        Name=None,
        PbbDestinamtionMac=None,
        PbbEtherType=None,
        PbbIsId=None,
        PbbSourceMac=None,
        PbbVlanId=None,
        PbbVlanPcp=None,
        ProtocolInterface=None,
        RangeSize=None,
        SourcePort=None,
        UdpDestination=None,
        UdpSource=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, int, str, str, int, str, str, str, bool, bool, str, str, str, int, str, str, str, str, str, int, int, str, str, str, str, str, str, str, str, str, str, str, int, str, str, str, str, str, str, str, str, str, str, int, str, str, str, int, str, str) -> TrafficEndPoint
        """Adds a new trafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): If true, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specifies the Custom Header length in bytes.
        - CustomEtherHeaderValue (str): Specifies the Custom ether Header value.
        - CustomEtherType (str): Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - CustomIpHeaderLength (number): Specifies the custom Header length in bytes.
        - CustomIpHeaderValue (str): Specifies the Custom Header value.
        - CustomIpProtocol (str): Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - DestinationPort (str): Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EnableMacInMac (bool): Enables the PBB-specific fields.
        - EnableVlan (bool): If enabled, VLAN is available.
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): Specifies the Ether Type to be used.
        - GatewayMac (str): Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpAddress (str): Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpMask (number): Specifies the Mask value.
        - IpProtocol (str(custom | tcp | udp)): Specifies the IP Protocol to be used.
        - IpTos (str): Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Dscp (str): Specifies value of Ipv4 DSCP field.
        - Ipv4Ecn (str): Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6Address (str): Specifies the IPv6 address to be used in the traffic endpoint.
        - Ipv6AddressMask (number): Specifies the mask of IPv6 address
        - Ipv6CustomHeaderLength (number): Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        - Ipv6CustomHeaderValue (str): Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        - Ipv6CustomNextHeader (str): Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        - Ipv6Dscp (str): Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        - Ipv6Ecn (str): Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6FlowLabel (str): Specifies the IPv6 flow label field.
        - Ipv6NextHeader (str(custom | tcp | udp)): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        - MacAddress (str): Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MplsInnerMacSource (str): Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanId (str): Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanPriority (str): Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsLabelStackSize (number): Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        - MplsTrafficClass (str): Specifies the MPLS traffic class.
        - Name (str): Specifies the name of the Traffic endpoint.
        - PbbDestinamtionMac (str): Specifies the B-Destination MAC.
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): Specifies the B-Ether Type.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbSourceMac (str): Specifies the B-Source MAC.
        - PbbVlanId (str): Specifies the B-VLAN ID.
        - PbbVlanPcp (str): Specifies the B-VLAN priority.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        - RangeSize (number): Specifies the size of the traffic range.
        - SourcePort (str): Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanCount (number): Specifies the VLAN Count.
        - VlanId (str): Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Returns
        -------
        - self: This instance with all currently retrieved trafficEndPoint resources using find and the newly added trafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ArpViaInterface=None,
        CustomEtherHeaderLength=None,
        CustomEtherHeaderValue=None,
        CustomEtherType=None,
        CustomIpHeaderLength=None,
        CustomIpHeaderValue=None,
        CustomIpProtocol=None,
        DestinationPort=None,
        EnableMacInMac=None,
        EnableVlan=None,
        EtherType=None,
        GatewayMac=None,
        IpAddress=None,
        IpMask=None,
        IpProtocol=None,
        IpTos=None,
        Ipv4Dscp=None,
        Ipv4Ecn=None,
        Ipv6Address=None,
        Ipv6AddressMask=None,
        Ipv6CustomHeaderLength=None,
        Ipv6CustomHeaderValue=None,
        Ipv6CustomNextHeader=None,
        Ipv6Dscp=None,
        Ipv6Ecn=None,
        Ipv6FlowLabel=None,
        Ipv6NextHeader=None,
        MacAddress=None,
        MplsInnerMacSource=None,
        MplsInnerVlanId=None,
        MplsInnerVlanPriority=None,
        MplsLabel=None,
        MplsLabelStackSize=None,
        MplsPayloadType=None,
        MplsTrafficClass=None,
        Name=None,
        PbbDestinamtionMac=None,
        PbbEtherType=None,
        PbbIsId=None,
        PbbSourceMac=None,
        PbbVlanId=None,
        PbbVlanPcp=None,
        ProtocolInterface=None,
        RangeSize=None,
        SourcePort=None,
        UdpDestination=None,
        UdpSource=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, int, str, str, int, str, str, str, bool, bool, str, str, str, int, str, str, str, str, str, int, int, str, str, str, str, str, str, str, str, str, str, str, int, str, str, str, str, str, str, str, str, str, str, int, str, str, str, int, str, str) -> TrafficEndPoint
        """Finds and retrieves trafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): If true, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specifies the Custom Header length in bytes.
        - CustomEtherHeaderValue (str): Specifies the Custom ether Header value.
        - CustomEtherType (str): Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - CustomIpHeaderLength (number): Specifies the custom Header length in bytes.
        - CustomIpHeaderValue (str): Specifies the Custom Header value.
        - CustomIpProtocol (str): Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - DestinationPort (str): Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EnableMacInMac (bool): Enables the PBB-specific fields.
        - EnableVlan (bool): If enabled, VLAN is available.
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): Specifies the Ether Type to be used.
        - GatewayMac (str): Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpAddress (str): Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpMask (number): Specifies the Mask value.
        - IpProtocol (str(custom | tcp | udp)): Specifies the IP Protocol to be used.
        - IpTos (str): Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Dscp (str): Specifies value of Ipv4 DSCP field.
        - Ipv4Ecn (str): Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6Address (str): Specifies the IPv6 address to be used in the traffic endpoint.
        - Ipv6AddressMask (number): Specifies the mask of IPv6 address
        - Ipv6CustomHeaderLength (number): Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        - Ipv6CustomHeaderValue (str): Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        - Ipv6CustomNextHeader (str): Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        - Ipv6Dscp (str): Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        - Ipv6Ecn (str): Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6FlowLabel (str): Specifies the IPv6 flow label field.
        - Ipv6NextHeader (str(custom | tcp | udp)): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        - MacAddress (str): Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MplsInnerMacSource (str): Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanId (str): Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanPriority (str): Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsLabelStackSize (number): Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        - MplsTrafficClass (str): Specifies the MPLS traffic class.
        - Name (str): Specifies the name of the Traffic endpoint.
        - PbbDestinamtionMac (str): Specifies the B-Destination MAC.
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): Specifies the B-Ether Type.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbSourceMac (str): Specifies the B-Source MAC.
        - PbbVlanId (str): Specifies the B-VLAN ID.
        - PbbVlanPcp (str): Specifies the B-VLAN priority.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        - RangeSize (number): Specifies the size of the traffic range.
        - SourcePort (str): Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanCount (number): Specifies the VLAN Count.
        - VlanId (str): Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Returns
        -------
        - self: This instance with matching trafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
