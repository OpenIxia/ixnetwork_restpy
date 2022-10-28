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


class EthernetTrafficEndPoint(Base):
    """NOT DEFINED
    The EthernetTrafficEndPoint class encapsulates a list of ethernetTrafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the EthernetTrafficEndPoint.find() method.
    The list can be managed by using the EthernetTrafficEndPoint.add() and EthernetTrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "ethernetTrafficEndPoint"
    _SDM_ATT_MAP = {
        "ArpViaInterface": "arpViaInterface",
        "CustomEtherHeaderLength": "customEtherHeaderLength",
        "CustomEtherHeaderValue": "customEtherHeaderValue",
        "CustomEtherType": "customEtherType",
        "EnableMacInMac": "enableMacInMac",
        "EnableVlan": "enableVlan",
        "GatewayMac": "gatewayMac",
        "MacAddress": "macAddress",
        "Name": "name",
        "PbbDestinamtionMac": "pbbDestinamtionMac",
        "PbbEtherType": "pbbEtherType",
        "PbbIsId": "pbbIsId",
        "PbbSourceMac": "pbbSourceMac",
        "PbbVlanId": "pbbVlanId",
        "PbbVlanPcp": "pbbVlanPcp",
        "ProtocolInterface": "protocolInterface",
        "RangeSize": "rangeSize",
        "VlanCount": "vlanCount",
        "VlanId": "vlanId",
        "VlanPriority": "vlanPriority",
    }
    _SDM_ENUM_MAP = {
        "pbbEtherType": [
            "bEtherType8100",
            "bEtherType88A8",
            "bEtherType88E7",
            "bEtherType9100",
            "bEtherType9200",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(EthernetTrafficEndPoint, self).__init__(parent, list_op)

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
    def CustomEtherHeaderLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the Custom Header length in bytes. The default length is 46 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomEtherHeaderLength"])

    @CustomEtherHeaderLength.setter
    def CustomEtherHeaderLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomEtherHeaderLength"], value)

    @property
    def CustomEtherHeaderValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the Custom Header value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomEtherHeaderValue"])

    @CustomEtherHeaderValue.setter
    def CustomEtherHeaderValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomEtherHeaderValue"], value)

    @property
    def CustomEtherType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specify the Custom Ether type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomEtherType"])

    @CustomEtherType.setter
    def CustomEtherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomEtherType"], value)

    @property
    def EnableMacInMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMacInMac"])

    @EnableMacInMac.setter
    def EnableMacInMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMacInMac"], value)

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
        - str: The name of the Traffic Source Endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def PbbDestinamtionMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbDestinamtionMac"])

    @PbbDestinamtionMac.setter
    def PbbDestinamtionMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbDestinamtionMac"], value)

    @property
    def PbbEtherType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbEtherType"])

    @PbbEtherType.setter
    def PbbEtherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbEtherType"], value)

    @property
    def PbbIsId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbIsId"])

    @PbbIsId.setter
    def PbbIsId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbIsId"], value)

    @property
    def PbbSourceMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbSourceMac"])

    @PbbSourceMac.setter
    def PbbSourceMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbSourceMac"], value)

    @property
    def PbbVlanId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbVlanId"])

    @PbbVlanId.setter
    def PbbVlanId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbVlanId"], value)

    @property
    def PbbVlanPcp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbVlanPcp"])

    @PbbVlanPcp.setter
    def PbbVlanPcp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PbbVlanPcp"], value)

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
        - number: Specify the size of the Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeSize"])

    @RangeSize.setter
    def RangeSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeSize"], value)

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
        CustomEtherHeaderLength=None,
        CustomEtherHeaderValue=None,
        CustomEtherType=None,
        EnableMacInMac=None,
        EnableVlan=None,
        GatewayMac=None,
        MacAddress=None,
        Name=None,
        PbbDestinamtionMac=None,
        PbbEtherType=None,
        PbbIsId=None,
        PbbSourceMac=None,
        PbbVlanId=None,
        PbbVlanPcp=None,
        ProtocolInterface=None,
        RangeSize=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, int, str, str, bool, bool, str, str, str, str, str, str, str, str, str, str, int, int, str, str) -> EthernetTrafficEndPoint
        """Updates ethernetTrafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specify the Custom Header length in bytes. The default length is 46 bytes.
        - CustomEtherHeaderValue (str): Specify the Custom Header value.
        - CustomEtherType (str): Specify the Custom Ether type.
        - EnableMacInMac (bool): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic Source Endpoint.
        - PbbDestinamtionMac (str): NOT DEFINED
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): NOT DEFINED
        - PbbIsId (str): NOT DEFINED
        - PbbSourceMac (str): NOT DEFINED
        - PbbVlanId (str): NOT DEFINED
        - PbbVlanPcp (str): NOT DEFINED
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the Range.
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
        CustomEtherHeaderLength=None,
        CustomEtherHeaderValue=None,
        CustomEtherType=None,
        EnableMacInMac=None,
        EnableVlan=None,
        GatewayMac=None,
        MacAddress=None,
        Name=None,
        PbbDestinamtionMac=None,
        PbbEtherType=None,
        PbbIsId=None,
        PbbSourceMac=None,
        PbbVlanId=None,
        PbbVlanPcp=None,
        ProtocolInterface=None,
        RangeSize=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, int, str, str, bool, bool, str, str, str, str, str, str, str, str, str, str, int, int, str, str) -> EthernetTrafficEndPoint
        """Adds a new ethernetTrafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specify the Custom Header length in bytes. The default length is 46 bytes.
        - CustomEtherHeaderValue (str): Specify the Custom Header value.
        - CustomEtherType (str): Specify the Custom Ether type.
        - EnableMacInMac (bool): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic Source Endpoint.
        - PbbDestinamtionMac (str): NOT DEFINED
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): NOT DEFINED
        - PbbIsId (str): NOT DEFINED
        - PbbSourceMac (str): NOT DEFINED
        - PbbVlanId (str): NOT DEFINED
        - PbbVlanPcp (str): NOT DEFINED
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the Range.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with all currently retrieved ethernetTrafficEndPoint resources using find and the newly added ethernetTrafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ethernetTrafficEndPoint resources in this instance from the server.

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
        EnableMacInMac=None,
        EnableVlan=None,
        GatewayMac=None,
        MacAddress=None,
        Name=None,
        PbbDestinamtionMac=None,
        PbbEtherType=None,
        PbbIsId=None,
        PbbSourceMac=None,
        PbbVlanId=None,
        PbbVlanPcp=None,
        ProtocolInterface=None,
        RangeSize=None,
        VlanCount=None,
        VlanId=None,
        VlanPriority=None,
    ):
        # type: (bool, int, str, str, bool, bool, str, str, str, str, str, str, str, str, str, str, int, int, str, str) -> EthernetTrafficEndPoint
        """Finds and retrieves ethernetTrafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernetTrafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernetTrafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): If selected, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specify the Custom Header length in bytes. The default length is 46 bytes.
        - CustomEtherHeaderValue (str): Specify the Custom Header value.
        - CustomEtherType (str): Specify the Custom Ether type.
        - EnableMacInMac (bool): NOT DEFINED
        - EnableVlan (bool): Select this check box to make VLAN available.
        - GatewayMac (str): The Gateway MAC address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - MacAddress (str): The MAC Address of the source traffic endpoint. The default value is 00 00 00 00 00 00.
        - Name (str): The name of the Traffic Source Endpoint.
        - PbbDestinamtionMac (str): NOT DEFINED
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): NOT DEFINED
        - PbbIsId (str): NOT DEFINED
        - PbbSourceMac (str): NOT DEFINED
        - PbbVlanId (str): NOT DEFINED
        - PbbVlanPcp (str): NOT DEFINED
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): NOT DEFINED
        - RangeSize (number): Specify the size of the Range.
        - VlanCount (number): Specify the VLAN count. The default value is 1.
        - VlanId (str): Specify the VLAN ID (Outer and Inner).
        - VlanPriority (str): Specify the VLAN Priority (Outer and Inner).

        Returns
        -------
        - self: This instance with matching ethernetTrafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernetTrafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernetTrafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
