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


class DhcpServerPage(Base):
    """Describes the dhcp server page settings.
    The DhcpServerPage class encapsulates a list of dhcpServerPage resources that are managed by the system.
    A list of resources can be retrieved from the server using the DhcpServerPage.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "dhcpServerPage"
    _SDM_ATT_MAP = {
        "Count": "count",
        "Dhcp4EchoRelayInfo": "dhcp4EchoRelayInfo",
        "Dhcp6IaType": "dhcp6IaType",
        "IpAddress": "ipAddress",
        "IpAddressIncrement": "ipAddressIncrement",
        "IpAddressPoolIncrement": "ipAddressPoolIncrement",
        "IpAddressPrefix": "ipAddressPrefix",
        "IpAddressPrefixIncrement": "ipAddressPrefixIncrement",
        "IpAddressPrefixPoolIncrement": "ipAddressPrefixPoolIncrement",
        "IpDns1": "ipDns1",
        "IpDns2": "ipDns2",
        "IpGateway": "ipGateway",
        "IpPrefix": "ipPrefix",
        "IpType": "ipType",
        "PgIncrement": "pgIncrement",
        "PrefixCount": "prefixCount",
        "PrefixLength": "prefixLength",
        "RangeIncrement": "rangeIncrement",
        "ServerAddress": "serverAddress",
        "ServerAddressIncrement": "serverAddressIncrement",
        "ServerCount": "serverCount",
        "ServerGateway": "serverGateway",
        "ServerGatewayIncrement": "serverGatewayIncrement",
        "ServerPrefix": "serverPrefix",
        "UseRapidCommit": "useRapidCommit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DhcpServerPage, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of gateway address for DHCP server interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def Dhcp4EchoRelayInfo(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Describes the information on DHCP 4 echo relay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4EchoRelayInfo"])

    @Dhcp4EchoRelayInfo.setter
    def Dhcp4EchoRelayInfo(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4EchoRelayInfo"], value)

    @property
    def Dhcp6IaType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Identity Association Type. The IA types are IANA, IATA, and IAPD. The default is IANA.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaType"])

    @Dhcp6IaType.setter
    def Dhcp6IaType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaType"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Ip address assigned for DHCP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpAddressIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the incremental value of ip address that is assigned for DHCP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressIncrement"])

    @IpAddressIncrement.setter
    def IpAddressIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressIncrement"], value)

    @property
    def IpAddressPoolIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the increment in ip address pool for DHCP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressPoolIncrement"])

    @IpAddressPoolIncrement.setter
    def IpAddressPoolIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressPoolIncrement"], value)

    @property
    def IpAddressPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes pre-assigned IPv4 address prefix for DHCP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressPrefix"])

    @IpAddressPrefix.setter
    def IpAddressPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressPrefix"], value)

    @property
    def IpAddressPrefixIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the incremental value of pre-assigned IPv4 address prefix for DHCP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressPrefixIncrement"])

    @IpAddressPrefixIncrement.setter
    def IpAddressPrefixIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressPrefixIncrement"], value)

    @property
    def IpAddressPrefixPoolIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the incremental value for pre-assigned IPv4 pool address prefix for DHCP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressPrefixPoolIncrement"])

    @IpAddressPrefixPoolIncrement.setter
    def IpAddressPrefixPoolIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressPrefixPoolIncrement"], value)

    @property
    def IpDns1(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first DNS server associated with this address pool.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDns1"])

    @IpDns1.setter
    def IpDns1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpDns1"], value)

    @property
    def IpDns2(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The second DNS server associated with this address pool.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDns2"])

    @IpDns2.setter
    def IpDns2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpDns2"], value)

    @property
    def IpGateway(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The gateway address for all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpGateway"])

    @IpGateway.setter
    def IpGateway(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpGateway"], value)

    @property
    def IpPrefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of one bits in the subnet mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpPrefix"])

    @IpPrefix.setter
    def IpPrefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpPrefix"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Internet Protocol (IP version).
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def PgIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the page increment for the dhcp server page.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PgIncrement"])

    @PgIncrement.setter
    def PgIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PgIncrement"], value)

    @property
    def PrefixCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This attribute defines the multiple configurable options for DHCP server interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrefixCount"])

    @PrefixCount.setter
    def PrefixCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrefixCount"], value)

    @property
    def PrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A learned/allocated IPv4 address prefix length (mask) for DHCP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrefixLength"])

    @PrefixLength.setter
    def PrefixLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrefixLength"], value)

    @property
    def RangeIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which VLAN IDs will be incremented when the port group contains multiple ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeIncrement"])

    @RangeIncrement.setter
    def RangeIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeIncrement"], value)

    @property
    def ServerAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The address of the DHCP server from which the subnet will accept IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerAddress"])

    @ServerAddress.setter
    def ServerAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerAddress"], value)

    @property
    def ServerAddressIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which to increment the IP address for each DHCP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerAddressIncrement"])

    @ServerAddressIncrement.setter
    def ServerAddressIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerAddressIncrement"], value)

    @property
    def ServerCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Describes the server count for dhcp server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerCount"])

    @ServerCount.setter
    def ServerCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerCount"], value)

    @property
    def ServerGateway(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The gateway address associated with DHCP Server interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerGateway"])

    @ServerGateway.setter
    def ServerGateway(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerGateway"], value)

    @property
    def ServerGatewayIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The incremental gateway address associated with DHCP Server interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerGatewayIncrement"])

    @ServerGatewayIncrement.setter
    def ServerGatewayIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerGatewayIncrement"], value)

    @property
    def ServerPrefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The subnet prefix length associated with the DHCP Server interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerPrefix"])

    @ServerPrefix.setter
    def ServerPrefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerPrefix"], value)

    @property
    def UseRapidCommit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, rapid commit is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseRapidCommit"])

    @UseRapidCommit.setter
    def UseRapidCommit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseRapidCommit"], value)

    def update(
        self,
        Count=None,
        Dhcp4EchoRelayInfo=None,
        Dhcp6IaType=None,
        IpAddress=None,
        IpAddressIncrement=None,
        IpAddressPoolIncrement=None,
        IpAddressPrefix=None,
        IpAddressPrefixIncrement=None,
        IpAddressPrefixPoolIncrement=None,
        IpDns1=None,
        IpDns2=None,
        IpGateway=None,
        IpPrefix=None,
        IpType=None,
        PgIncrement=None,
        PrefixCount=None,
        PrefixLength=None,
        RangeIncrement=None,
        ServerAddress=None,
        ServerAddressIncrement=None,
        ServerCount=None,
        ServerGateway=None,
        ServerGatewayIncrement=None,
        ServerPrefix=None,
        UseRapidCommit=None,
    ):
        # type: (int, bool, str, str, str, str, str, str, str, str, str, str, int, str, str, int, int, str, str, str, int, str, str, int, bool) -> DhcpServerPage
        """Updates dhcpServerPage resource on the server.

        Args
        ----
        - Count (number): Number of gateway address for DHCP server interface.
        - Dhcp4EchoRelayInfo (bool): Describes the information on DHCP 4 echo relay.
        - Dhcp6IaType (str): The Identity Association Type. The IA types are IANA, IATA, and IAPD. The default is IANA.
        - IpAddress (str): Ip address assigned for DHCP server.
        - IpAddressIncrement (str): Describes the incremental value of ip address that is assigned for DHCP server.
        - IpAddressPoolIncrement (str): Describes the increment in ip address pool for DHCP server.
        - IpAddressPrefix (str): Describes pre-assigned IPv4 address prefix for DHCP interface.
        - IpAddressPrefixIncrement (str): Describes the incremental value of pre-assigned IPv4 address prefix for DHCP interface.
        - IpAddressPrefixPoolIncrement (str): Describes the incremental value for pre-assigned IPv4 pool address prefix for DHCP interface.
        - IpDns1 (str): The first DNS server associated with this address pool.
        - IpDns2 (str): The second DNS server associated with this address pool.
        - IpGateway (str): The gateway address for all the addresses in the range.
        - IpPrefix (number): The number of one bits in the subnet mask.
        - IpType (str): The Internet Protocol (IP version).
        - PgIncrement (str): Describes the page increment for the dhcp server page.
        - PrefixCount (number): This attribute defines the multiple configurable options for DHCP server interface.
        - PrefixLength (number): A learned/allocated IPv4 address prefix length (mask) for DHCP interface.
        - RangeIncrement (str): The value by which VLAN IDs will be incremented when the port group contains multiple ranges.
        - ServerAddress (str): The address of the DHCP server from which the subnet will accept IP addresses.
        - ServerAddressIncrement (str): The value by which to increment the IP address for each DHCP server.
        - ServerCount (number): Describes the server count for dhcp server.
        - ServerGateway (str): The gateway address associated with DHCP Server interfaces.
        - ServerGatewayIncrement (str): The incremental gateway address associated with DHCP Server interfaces.
        - ServerPrefix (number): The subnet prefix length associated with the DHCP Server interfaces.
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Count=None,
        Dhcp4EchoRelayInfo=None,
        Dhcp6IaType=None,
        IpAddress=None,
        IpAddressIncrement=None,
        IpAddressPoolIncrement=None,
        IpAddressPrefix=None,
        IpAddressPrefixIncrement=None,
        IpAddressPrefixPoolIncrement=None,
        IpDns1=None,
        IpDns2=None,
        IpGateway=None,
        IpPrefix=None,
        IpType=None,
        PgIncrement=None,
        PrefixCount=None,
        PrefixLength=None,
        RangeIncrement=None,
        ServerAddress=None,
        ServerAddressIncrement=None,
        ServerCount=None,
        ServerGateway=None,
        ServerGatewayIncrement=None,
        ServerPrefix=None,
        UseRapidCommit=None,
    ):
        # type: (int, bool, str, str, str, str, str, str, str, str, str, str, int, str, str, int, int, str, str, str, int, str, str, int, bool) -> DhcpServerPage
        """Adds a new dhcpServerPage resource on the json, only valid with batch add utility

        Args
        ----
        - Count (number): Number of gateway address for DHCP server interface.
        - Dhcp4EchoRelayInfo (bool): Describes the information on DHCP 4 echo relay.
        - Dhcp6IaType (str): The Identity Association Type. The IA types are IANA, IATA, and IAPD. The default is IANA.
        - IpAddress (str): Ip address assigned for DHCP server.
        - IpAddressIncrement (str): Describes the incremental value of ip address that is assigned for DHCP server.
        - IpAddressPoolIncrement (str): Describes the increment in ip address pool for DHCP server.
        - IpAddressPrefix (str): Describes pre-assigned IPv4 address prefix for DHCP interface.
        - IpAddressPrefixIncrement (str): Describes the incremental value of pre-assigned IPv4 address prefix for DHCP interface.
        - IpAddressPrefixPoolIncrement (str): Describes the incremental value for pre-assigned IPv4 pool address prefix for DHCP interface.
        - IpDns1 (str): The first DNS server associated with this address pool.
        - IpDns2 (str): The second DNS server associated with this address pool.
        - IpGateway (str): The gateway address for all the addresses in the range.
        - IpPrefix (number): The number of one bits in the subnet mask.
        - IpType (str): The Internet Protocol (IP version).
        - PgIncrement (str): Describes the page increment for the dhcp server page.
        - PrefixCount (number): This attribute defines the multiple configurable options for DHCP server interface.
        - PrefixLength (number): A learned/allocated IPv4 address prefix length (mask) for DHCP interface.
        - RangeIncrement (str): The value by which VLAN IDs will be incremented when the port group contains multiple ranges.
        - ServerAddress (str): The address of the DHCP server from which the subnet will accept IP addresses.
        - ServerAddressIncrement (str): The value by which to increment the IP address for each DHCP server.
        - ServerCount (number): Describes the server count for dhcp server.
        - ServerGateway (str): The gateway address associated with DHCP Server interfaces.
        - ServerGatewayIncrement (str): The incremental gateway address associated with DHCP Server interfaces.
        - ServerPrefix (number): The subnet prefix length associated with the DHCP Server interfaces.
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpServerPage resources using find and the newly added dhcpServerPage resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        Dhcp4EchoRelayInfo=None,
        Dhcp6IaType=None,
        IpAddress=None,
        IpAddressIncrement=None,
        IpAddressPoolIncrement=None,
        IpAddressPrefix=None,
        IpAddressPrefixIncrement=None,
        IpAddressPrefixPoolIncrement=None,
        IpDns1=None,
        IpDns2=None,
        IpGateway=None,
        IpPrefix=None,
        IpType=None,
        PgIncrement=None,
        PrefixCount=None,
        PrefixLength=None,
        RangeIncrement=None,
        ServerAddress=None,
        ServerAddressIncrement=None,
        ServerCount=None,
        ServerGateway=None,
        ServerGatewayIncrement=None,
        ServerPrefix=None,
        UseRapidCommit=None,
    ):
        # type: (int, bool, str, str, str, str, str, str, str, str, str, str, int, str, str, int, int, str, str, str, int, str, str, int, bool) -> DhcpServerPage
        """Finds and retrieves dhcpServerPage resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpServerPage resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpServerPage resources from the server.

        Args
        ----
        - Count (number): Number of gateway address for DHCP server interface.
        - Dhcp4EchoRelayInfo (bool): Describes the information on DHCP 4 echo relay.
        - Dhcp6IaType (str): The Identity Association Type. The IA types are IANA, IATA, and IAPD. The default is IANA.
        - IpAddress (str): Ip address assigned for DHCP server.
        - IpAddressIncrement (str): Describes the incremental value of ip address that is assigned for DHCP server.
        - IpAddressPoolIncrement (str): Describes the increment in ip address pool for DHCP server.
        - IpAddressPrefix (str): Describes pre-assigned IPv4 address prefix for DHCP interface.
        - IpAddressPrefixIncrement (str): Describes the incremental value of pre-assigned IPv4 address prefix for DHCP interface.
        - IpAddressPrefixPoolIncrement (str): Describes the incremental value for pre-assigned IPv4 pool address prefix for DHCP interface.
        - IpDns1 (str): The first DNS server associated with this address pool.
        - IpDns2 (str): The second DNS server associated with this address pool.
        - IpGateway (str): The gateway address for all the addresses in the range.
        - IpPrefix (number): The number of one bits in the subnet mask.
        - IpType (str): The Internet Protocol (IP version).
        - PgIncrement (str): Describes the page increment for the dhcp server page.
        - PrefixCount (number): This attribute defines the multiple configurable options for DHCP server interface.
        - PrefixLength (number): A learned/allocated IPv4 address prefix length (mask) for DHCP interface.
        - RangeIncrement (str): The value by which VLAN IDs will be incremented when the port group contains multiple ranges.
        - ServerAddress (str): The address of the DHCP server from which the subnet will accept IP addresses.
        - ServerAddressIncrement (str): The value by which to increment the IP address for each DHCP server.
        - ServerCount (number): Describes the server count for dhcp server.
        - ServerGateway (str): The gateway address associated with DHCP Server interfaces.
        - ServerGatewayIncrement (str): The incremental gateway address associated with DHCP Server interfaces.
        - ServerPrefix (number): The subnet prefix length associated with the DHCP Server interfaces.
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Returns
        -------
        - self: This instance with matching dhcpServerPage resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpServerPage data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpServerPage resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
