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


class Ipv6TrafficEndPoint(Base):
    """NOT DEFINED
    The Ipv6TrafficEndPoint class encapsulates a list of ipv6TrafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ipv6TrafficEndPoint.find() method.
    The list can be managed by using the Ipv6TrafficEndPoint.add() and Ipv6TrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "ipv6TrafficEndPoint"
    _SDM_ATT_MAP = {
        "ArpViaInterface": "arpViaInterface",
        "DestinationPort": "destinationPort",
        "EnableVlan": "enableVlan",
        "GatewayMac": "gatewayMac",
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
        "Name": "name",
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
        "ipv6NextHeader": ["custom", "tcp", "udp"],
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6TrafficEndPoint, self).__init__(parent, list_op)

    @property
    def ArpViaInterface(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, ARP request is conveyed through an Interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpViaInterface"])

    @ArpViaInterface.setter
    def ArpViaInterface(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpViaInterface"], value)

    @property
    def DestinationPort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationPort"])

    @DestinationPort.setter
    def DestinationPort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationPort"], value)

    @property
    def EnableVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select this check box to make VLAN available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVlan"])

    @EnableVlan.setter
    def EnableVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVlan"], value)

    @property
    def GatewayMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayMac"])

    @GatewayMac.setter
    def GatewayMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayMac"], value)

    @property
    def Ipv6Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Address"])

    @Ipv6Address.setter
    def Ipv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Address"], value)

    @property
    def Ipv6AddressMask(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the Mask value. The default value is 64.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6AddressMask"])

    @Ipv6AddressMask.setter
    def Ipv6AddressMask(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6AddressMask"], value)

    @property
    def Ipv6CustomHeaderLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Custom IPv6 Header Length value. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderLength"])

    @Ipv6CustomHeaderLength.setter
    def Ipv6CustomHeaderLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderLength"], value)

    @property
    def Ipv6CustomHeaderValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Custom IPv6 Header Value. The default value is 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderValue"])

    @Ipv6CustomHeaderValue.setter
    def Ipv6CustomHeaderValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6CustomHeaderValue"], value)

    @property
    def Ipv6CustomNextHeader(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Custom IPv6 Next Header value. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6CustomNextHeader"])

    @Ipv6CustomNextHeader.setter
    def Ipv6CustomNextHeader(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6CustomNextHeader"], value)

    @property
    def Ipv6Dscp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The priority specified for the IP address. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Dscp"])

    @Ipv6Dscp.setter
    def Ipv6Dscp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Dscp"], value)

    @property
    def Ipv6Ecn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The ECN value specified for the IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Ecn"])

    @Ipv6Ecn.setter
    def Ipv6Ecn(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Ecn"], value)

    @property
    def Ipv6FlowLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IPv6 Flow Label value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"])

    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6FlowLabel"], value)

    @property
    def Ipv6NextHeader(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | tcp | udp): The IPv6 Next Header value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NextHeader"])

    @Ipv6NextHeader.setter
    def Ipv6NextHeader(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NextHeader"], value)

    @property
    def MacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacAddress"])

    @MacAddress.setter
    def MacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacAddress"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ProtocolInterface(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolInterface"])

    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolInterface"], value)

    @property
    def RangeSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the size of the traffic range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeSize"])

    @RangeSize.setter
    def RangeSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeSize"], value)

    @property
    def SourcePort(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourcePort"])

    @SourcePort.setter
    def SourcePort(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourcePort"], value)

    @property
    def UdpDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the UDP Destination. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpDestination"])

    @UdpDestination.setter
    def UdpDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpDestination"], value)

    @property
    def UdpSource(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the UDP Source. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpSource"])

    @UdpSource.setter
    def UdpSource(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpSource"], value)

    @property
    def VlanCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the VLAN count. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanCount"])

    @VlanCount.setter
    def VlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanCount"], value)

    @property
    def VlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the VLAN ID (Outer and Inner).
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanId"])

    @VlanId.setter
    def VlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanId"], value)

    @property
    def VlanPriority(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the VLAN Priority (Outer and Inner).
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanPriority"])

    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanPriority"], value)

    def update(
        self,
        ArpViaInterface=None,
        DestinationPort=None,
        EnableVlan=None,
        GatewayMac=None,
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
        Name=None,
        ProtocolInterface=None,
        RangeSize=None,
        SourcePort=None,
        UdpDestination=None,
        UdpSource=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, str, bool, str, str, int, int, str, str, str, str, str, str, str, str, str, int, str, str, str, int, str, str) -> Ipv6TrafficEndPoint
        """Updates ipv6TrafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - DestinationPort (str): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Ipv6Address (str): Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        - Ipv6AddressMask (number): Specify the Mask value. The default value is 64.
        - Ipv6CustomHeaderLength (number): The Custom IPv6 Header Length value. The default value is 1.
        - Ipv6CustomHeaderValue (str): The Custom IPv6 Header Value. The default value is 00.
        - Ipv6CustomNextHeader (str): The Custom IPv6 Next Header value. The default value is 1.
        - Ipv6Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv6Ecn (str): The ECN value specified for the IP address.
        - Ipv6FlowLabel (str): The IPv6 Flow Label value.
        - Ipv6NextHeader (str(custom | tcp | udp)): The IPv6 Next Header value.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the traffic range.
        - SourcePort (str): NOT DEFINED
        - UdpDestination (str): Specify the UDP Destination. The default value is 1.
        - UdpSource (str): Specify the UDP Source. The default value is 1.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ArpViaInterface=None,
        DestinationPort=None,
        EnableVlan=None,
        GatewayMac=None,
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
        Name=None,
        ProtocolInterface=None,
        RangeSize=None,
        SourcePort=None,
        UdpDestination=None,
        UdpSource=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, str, bool, str, str, int, int, str, str, str, str, str, str, str, str, str, int, str, str, str, int, str, str) -> Ipv6TrafficEndPoint
        """Adds a new ipv6TrafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - DestinationPort (str): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Ipv6Address (str): Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        - Ipv6AddressMask (number): Specify the Mask value. The default value is 64.
        - Ipv6CustomHeaderLength (number): The Custom IPv6 Header Length value. The default value is 1.
        - Ipv6CustomHeaderValue (str): The Custom IPv6 Header Value. The default value is 00.
        - Ipv6CustomNextHeader (str): The Custom IPv6 Next Header value. The default value is 1.
        - Ipv6Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv6Ecn (str): The ECN value specified for the IP address.
        - Ipv6FlowLabel (str): The IPv6 Flow Label value.
        - Ipv6NextHeader (str(custom | tcp | udp)): The IPv6 Next Header value.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the traffic range.
        - SourcePort (str): NOT DEFINED
        - UdpDestination (str): Specify the UDP Destination. The default value is 1.
        - UdpSource (str): Specify the UDP Source. The default value is 1.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with all currently retrieved ipv6TrafficEndPoint resources using find and the newly added ipv6TrafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ipv6TrafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ArpViaInterface=None,
        DestinationPort=None,
        EnableVlan=None,
        GatewayMac=None,
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
        Name=None,
        ProtocolInterface=None,
        RangeSize=None,
        SourcePort=None,
        UdpDestination=None,
        UdpSource=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, str, bool, str, str, int, int, str, str, str, str, str, str, str, str, str, int, str, str, str, int, str, str) -> Ipv6TrafficEndPoint
        """Finds and retrieves ipv6TrafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv6TrafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv6TrafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - DestinationPort (str): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Ipv6Address (str): Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        - Ipv6AddressMask (number): Specify the Mask value. The default value is 64.
        - Ipv6CustomHeaderLength (number): The Custom IPv6 Header Length value. The default value is 1.
        - Ipv6CustomHeaderValue (str): The Custom IPv6 Header Value. The default value is 00.
        - Ipv6CustomNextHeader (str): The Custom IPv6 Next Header value. The default value is 1.
        - Ipv6Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv6Ecn (str): The ECN value specified for the IP address.
        - Ipv6FlowLabel (str): The IPv6 Flow Label value.
        - Ipv6NextHeader (str(custom | tcp | udp)): The IPv6 Next Header value.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the traffic range.
        - SourcePort (str): NOT DEFINED
        - UdpDestination (str): Specify the UDP Destination. The default value is 1.
        - UdpSource (str): Specify the UDP Source. The default value is 1.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with matching ipv6TrafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv6TrafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv6TrafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
