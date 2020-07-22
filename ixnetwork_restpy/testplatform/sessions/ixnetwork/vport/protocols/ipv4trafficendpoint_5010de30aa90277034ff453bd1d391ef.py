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


class Ipv4TrafficEndPoint(Base):
    """NOT DEFINED
    The Ipv4TrafficEndPoint class encapsulates a list of ipv4TrafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ipv4TrafficEndPoint.find() method.
    The list can be managed by using the Ipv4TrafficEndPoint.add() and Ipv4TrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4TrafficEndPoint'
    _SDM_ATT_MAP = {
        'ArpViaInterface': 'arpViaInterface',
        'CustomIpHeaderLength': 'customIpHeaderLength',
        'CustomIpHeaderValue': 'customIpHeaderValue',
        'CustomIpProtocol': 'customIpProtocol',
        'DestinationPort': 'destinationPort',
        'EnableVlan': 'enableVlan',
        'GatewayMac': 'gatewayMac',
        'IpAddress': 'ipAddress',
        'IpMask': 'ipMask',
        'IpProtocol': 'ipProtocol',
        'Ipv4Dscp': 'ipv4Dscp',
        'Ipv4Ecn': 'ipv4Ecn',
        'MacAddress': 'macAddress',
        'Name': 'name',
        'ProtocolInterface': 'protocolInterface',
        'RangeSize': 'rangeSize',
        'SourcePort': 'sourcePort',
        'UdpDestination': 'udpDestination',
        'UdpSource': 'udpSource',
        'VlanCount': 'vlanCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(Ipv4TrafficEndPoint, self).__init__(parent)

    @property
    def ArpViaInterface(self):
        """
        Returns
        -------
        - bool: If selected, ARP request is conveyed through an Interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpViaInterface'])
    @ArpViaInterface.setter
    def ArpViaInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpViaInterface'], value)

    @property
    def CustomIpHeaderLength(self):
        """
        Returns
        -------
        - number: The Custom IPv4 Header Length value. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomIpHeaderLength'])
    @CustomIpHeaderLength.setter
    def CustomIpHeaderLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomIpHeaderLength'], value)

    @property
    def CustomIpHeaderValue(self):
        """
        Returns
        -------
        - str: The Custom IPv4 Header Value. The default value is 00
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomIpHeaderValue'])
    @CustomIpHeaderValue.setter
    def CustomIpHeaderValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomIpHeaderValue'], value)

    @property
    def CustomIpProtocol(self):
        """
        Returns
        -------
        - str: Specify the custom IP Protocol for the Source Traffic Endpoints.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomIpProtocol'])
    @CustomIpProtocol.setter
    def CustomIpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomIpProtocol'], value)

    @property
    def DestinationPort(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationPort'])
    @DestinationPort.setter
    def DestinationPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationPort'], value)

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - bool: Select this check box to make VLAN available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVlan'])
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVlan'], value)

    @property
    def GatewayMac(self):
        """
        Returns
        -------
        - str: The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GatewayMac'])
    @GatewayMac.setter
    def GatewayMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GatewayMac'], value)

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: Specify the IPv4 address of the Source Traffic Endpoint. The default value is 0.0.0.0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def IpMask(self):
        """
        Returns
        -------
        - number: Specify the Mask value. The default value is 24.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpMask'])
    @IpMask.setter
    def IpMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpMask'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str(custom | tcp | udp): Click the IP Protocol type to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def Ipv4Dscp(self):
        """
        Returns
        -------
        - str: The priority specified for the IP address. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Dscp'])
    @Ipv4Dscp.setter
    def Ipv4Dscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Dscp'], value)

    @property
    def Ipv4Ecn(self):
        """
        Returns
        -------
        - str: The ECN value specified for the IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Ecn'])
    @Ipv4Ecn.setter
    def Ipv4Ecn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Ecn'], value)

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - str: The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ProtocolInterface(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def RangeSize(self):
        """
        Returns
        -------
        - number: Specify the size of the traffic range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RangeSize'])
    @RangeSize.setter
    def RangeSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RangeSize'], value)

    @property
    def SourcePort(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourcePort'])
    @SourcePort.setter
    def SourcePort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourcePort'], value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - str: Specify the UDP Destination. The default value is 1.
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
        - str: Specify the UDP Source. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSource'])
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSource'], value)

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - number: Specify the VLAN count. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanCount'])
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanCount'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: Specify the VLAN ID (Outer and Inner).
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
        - str: Specify the VLAN Priority (Outer and Inner).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, ArpViaInterface=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableVlan=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, Ipv4Dscp=None, Ipv4Ecn=None, MacAddress=None, Name=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates ipv4TrafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - CustomIpHeaderLength (number): The Custom IPv4 Header Length value. The default value is 1.
        - CustomIpHeaderValue (str): The Custom IPv4 Header Value. The default value is 00
        - CustomIpProtocol (str): Specify the custom IP Protocol for the Source Traffic Endpoints.
        - DestinationPort (str): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - IpAddress (str): Specify the IPv4 address of the Source Traffic Endpoint. The default value is 0.0.0.0.
        - IpMask (number): Specify the Mask value. The default value is 24.
        - IpProtocol (str(custom | tcp | udp)): Click the IP Protocol type to be used.
        - Ipv4Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv4Ecn (str): The ECN value specified for the IP address.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): NOT DEFINED
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

    def add(self, ArpViaInterface=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableVlan=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, Ipv4Dscp=None, Ipv4Ecn=None, MacAddress=None, Name=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new ipv4TrafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - CustomIpHeaderLength (number): The Custom IPv4 Header Length value. The default value is 1.
        - CustomIpHeaderValue (str): The Custom IPv4 Header Value. The default value is 00
        - CustomIpProtocol (str): Specify the custom IP Protocol for the Source Traffic Endpoints.
        - DestinationPort (str): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - IpAddress (str): Specify the IPv4 address of the Source Traffic Endpoint. The default value is 0.0.0.0.
        - IpMask (number): Specify the Mask value. The default value is 24.
        - IpProtocol (str(custom | tcp | udp)): Click the IP Protocol type to be used.
        - Ipv4Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv4Ecn (str): The ECN value specified for the IP address.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the traffic range.
        - SourcePort (str): NOT DEFINED
        - UdpDestination (str): Specify the UDP Destination. The default value is 1.
        - UdpSource (str): Specify the UDP Source. The default value is 1.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with all currently retrieved ipv4TrafficEndPoint resources using find and the newly added ipv4TrafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ipv4TrafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ArpViaInterface=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableVlan=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, Ipv4Dscp=None, Ipv4Ecn=None, MacAddress=None, Name=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves ipv4TrafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4TrafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4TrafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - CustomIpHeaderLength (number): The Custom IPv4 Header Length value. The default value is 1.
        - CustomIpHeaderValue (str): The Custom IPv4 Header Value. The default value is 00
        - CustomIpProtocol (str): Specify the custom IP Protocol for the Source Traffic Endpoints.
        - DestinationPort (str): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - IpAddress (str): Specify the IPv4 address of the Source Traffic Endpoint. The default value is 0.0.0.0.
        - IpMask (number): Specify the Mask value. The default value is 24.
        - IpProtocol (str(custom | tcp | udp)): Click the IP Protocol type to be used.
        - Ipv4Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv4Ecn (str): The ECN value specified for the IP address.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic endpoint. It is an auto-populated field but can be customized for convenience.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the traffic range.
        - SourcePort (str): NOT DEFINED
        - UdpDestination (str): Specify the UDP Destination. The default value is 1.
        - UdpSource (str): Specify the UDP Source. The default value is 1.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with matching ipv4TrafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4TrafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4TrafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
