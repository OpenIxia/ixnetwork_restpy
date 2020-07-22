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


class MplsTrafficEndPoint(Base):
    """This endpoint window allows you to configure the MPLS traffic endpoints.
    The MplsTrafficEndPoint class encapsulates a list of mplsTrafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the MplsTrafficEndPoint.find() method.
    The list can be managed by using the MplsTrafficEndPoint.add() and MplsTrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mplsTrafficEndPoint'
    _SDM_ATT_MAP = {
        'ArpViaInterface': 'arpViaInterface',
        'EnableVlan': 'enableVlan',
        'GatewayMac': 'gatewayMac',
        'IpAddress': 'ipAddress',
        'IpMask': 'ipMask',
        'Ipv4Dscp': 'ipv4Dscp',
        'Ipv4Ecn': 'ipv4Ecn',
        'Ipv6Address': 'ipv6Address',
        'Ipv6AddressMask': 'ipv6AddressMask',
        'Ipv6Dscp': 'ipv6Dscp',
        'Ipv6Ecn': 'ipv6Ecn',
        'Ipv6FlowLabel': 'ipv6FlowLabel',
        'MacAddress': 'macAddress',
        'MplsInnerMacSource': 'mplsInnerMacSource',
        'MplsInnerVlanId': 'mplsInnerVlanId',
        'MplsInnerVlanPriority': 'mplsInnerVlanPriority',
        'MplsLabel': 'mplsLabel',
        'MplsLabelStackSize': 'mplsLabelStackSize',
        'MplsPayloadType': 'mplsPayloadType',
        'MplsTrafficClass': 'mplsTrafficClass',
        'Name': 'name',
        'ProtocolInterface': 'protocolInterface',
        'RangeSize': 'rangeSize',
        'VlanCount': 'vlanCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(MplsTrafficEndPoint, self).__init__(parent)

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
        - str: The Gateway MAC address of the destination traffic endpoint. The default value is 00 00 00 00 00 00.
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
        - str: Specify the IP address of the Source Traffic Endpoint. The default value is 0.
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
    def Ipv6Address(self):
        """
        Returns
        -------
        - str: Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Address'])
    @Ipv6Address.setter
    def Ipv6Address(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Address'], value)

    @property
    def Ipv6AddressMask(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6AddressMask'])
    @Ipv6AddressMask.setter
    def Ipv6AddressMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6AddressMask'], value)

    @property
    def Ipv6Dscp(self):
        """
        Returns
        -------
        - str: The priority specified for the IP address. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Dscp'])
    @Ipv6Dscp.setter
    def Ipv6Dscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Dscp'], value)

    @property
    def Ipv6Ecn(self):
        """
        Returns
        -------
        - str: The ECN value specified for the IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6Ecn'])
    @Ipv6Ecn.setter
    def Ipv6Ecn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6Ecn'], value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - str: The IPv6 Flow Label value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'])
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6FlowLabel'], value)

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
    def MplsInnerMacSource(self):
        """
        Returns
        -------
        - str: The MPLS Inner Source MAC value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsInnerMacSource'])
    @MplsInnerMacSource.setter
    def MplsInnerMacSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsInnerMacSource'], value)

    @property
    def MplsInnerVlanId(self):
        """
        Returns
        -------
        - str: The MPLS Inner VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsInnerVlanId'])
    @MplsInnerVlanId.setter
    def MplsInnerVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsInnerVlanId'], value)

    @property
    def MplsInnerVlanPriority(self):
        """
        Returns
        -------
        - str: The MPLS Inner VLAN Priority value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsInnerVlanPriority'])
    @MplsInnerVlanPriority.setter
    def MplsInnerVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsInnerVlanPriority'], value)

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabel'])
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabel'], value)

    @property
    def MplsLabelStackSize(self):
        """
        Returns
        -------
        - number: The size of the MPLS label stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabelStackSize'])
    @MplsLabelStackSize.setter
    def MplsLabelStackSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabelStackSize'], value)

    @property
    def MplsPayloadType(self):
        """
        Returns
        -------
        - str(ethernet | ipv4 | ipv6): Specify the MPLS Payload Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsPayloadType'])
    @MplsPayloadType.setter
    def MplsPayloadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsPayloadType'], value)

    @property
    def MplsTrafficClass(self):
        """
        Returns
        -------
        - str: The MPLS Traffic Class value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsTrafficClass'])
    @MplsTrafficClass.setter
    def MplsTrafficClass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsTrafficClass'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the Traffic Source Endpoint.
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
        - number: Specify the size of the Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RangeSize'])
    @RangeSize.setter
    def RangeSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RangeSize'], value)

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

    def update(self, ArpViaInterface=None, EnableVlan=None, GatewayMac=None, IpAddress=None, IpMask=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, ProtocolInterface=None, RangeSize=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates mplsTrafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the destination traffic endpoint. The default value is 00 00 00 00 00 00.
        - IpAddress (str): Specify the IP address of the Source Traffic Endpoint. The default value is 0.
        - IpMask (number): Specify the Mask value. The default value is 24.
        - Ipv4Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv4Ecn (str): The ECN value specified for the IP address.
        - Ipv6Address (str): Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        - Ipv6AddressMask (number): NOT DEFINED
        - Ipv6Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv6Ecn (str): The ECN value specified for the IP address.
        - Ipv6FlowLabel (str): The IPv6 Flow Label value.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - MplsInnerMacSource (str): The MPLS Inner Source MAC value.
        - MplsInnerVlanId (str): The MPLS Inner VLAN identifier.
        - MplsInnerVlanPriority (str): The MPLS Inner VLAN Priority value.
        - MplsLabel (str): NOT DEFINED
        - MplsLabelStackSize (number): The size of the MPLS label stack.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specify the MPLS Payload Type.
        - MplsTrafficClass (str): The MPLS Traffic Class value.
        - Name (str): The name of the Traffic Source Endpoint.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the Range.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ArpViaInterface=None, EnableVlan=None, GatewayMac=None, IpAddress=None, IpMask=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, ProtocolInterface=None, RangeSize=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new mplsTrafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the destination traffic endpoint. The default value is 00 00 00 00 00 00.
        - IpAddress (str): Specify the IP address of the Source Traffic Endpoint. The default value is 0.
        - IpMask (number): Specify the Mask value. The default value is 24.
        - Ipv4Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv4Ecn (str): The ECN value specified for the IP address.
        - Ipv6Address (str): Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        - Ipv6AddressMask (number): NOT DEFINED
        - Ipv6Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv6Ecn (str): The ECN value specified for the IP address.
        - Ipv6FlowLabel (str): The IPv6 Flow Label value.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - MplsInnerMacSource (str): The MPLS Inner Source MAC value.
        - MplsInnerVlanId (str): The MPLS Inner VLAN identifier.
        - MplsInnerVlanPriority (str): The MPLS Inner VLAN Priority value.
        - MplsLabel (str): NOT DEFINED
        - MplsLabelStackSize (number): The size of the MPLS label stack.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specify the MPLS Payload Type.
        - MplsTrafficClass (str): The MPLS Traffic Class value.
        - Name (str): The name of the Traffic Source Endpoint.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the Range.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with all currently retrieved mplsTrafficEndPoint resources using find and the newly added mplsTrafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mplsTrafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ArpViaInterface=None, EnableVlan=None, GatewayMac=None, IpAddress=None, IpMask=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, ProtocolInterface=None, RangeSize=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves mplsTrafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mplsTrafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mplsTrafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the destination traffic endpoint. The default value is 00 00 00 00 00 00.
        - IpAddress (str): Specify the IP address of the Source Traffic Endpoint. The default value is 0.
        - IpMask (number): Specify the Mask value. The default value is 24.
        - Ipv4Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv4Ecn (str): The ECN value specified for the IP address.
        - Ipv6Address (str): Specify the IPv6 address of the Source Traffic Endpoint. The default value is 0.0.0.0.0.0.0.0
        - Ipv6AddressMask (number): NOT DEFINED
        - Ipv6Dscp (str): The priority specified for the IP address. The default value is 0.
        - Ipv6Ecn (str): The ECN value specified for the IP address.
        - Ipv6FlowLabel (str): The IPv6 Flow Label value.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - MplsInnerMacSource (str): The MPLS Inner Source MAC value.
        - MplsInnerVlanId (str): The MPLS Inner VLAN identifier.
        - MplsInnerVlanPriority (str): The MPLS Inner VLAN Priority value.
        - MplsLabel (str): NOT DEFINED
        - MplsLabelStackSize (number): The size of the MPLS label stack.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specify the MPLS Payload Type.
        - MplsTrafficClass (str): The MPLS Traffic Class value.
        - Name (str): The name of the Traffic Source Endpoint.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the Range.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with matching mplsTrafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mplsTrafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mplsTrafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
