# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class DhcpServerRange(Base):
    """Configuration parameters for a pool of IPv4/IPv6 addresses.
    The DhcpServerRange class encapsulates a required dhcpServerRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpServerRange'

    def __init__(self, parent):
        super(DhcpServerRange, self).__init__(parent)

    @property
    def Count(self):
        """The number of leases to be allocated per each server address.

        Returns:
            number
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def Dhcp4EchoRelayInfo(self):
        """Enable echoing of DHCP option 82.

        Returns:
            bool
        """
        return self._get_attribute('dhcp4EchoRelayInfo')
    @Dhcp4EchoRelayInfo.setter
    def Dhcp4EchoRelayInfo(self, value):
        self._set_attribute('dhcp4EchoRelayInfo', value)

    @property
    def Dhcp6IaType(self):
        """The Identity Association type supported by IPv6 address pools.

        Returns:
            str
        """
        return self._get_attribute('dhcp6IaType')
    @Dhcp6IaType.setter
    def Dhcp6IaType(self, value):
        self._set_attribute('dhcp6IaType', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IpAddress(self):
        """The IP address of the first lease pool.

        Returns:
            str
        """
        return self._get_attribute('ipAddress')
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute('ipAddress', value)

    @property
    def IpAddressIncrement(self):
        """The increment value for the lease address within the lease pool.

        Returns:
            str
        """
        return self._get_attribute('ipAddressIncrement')
    @IpAddressIncrement.setter
    def IpAddressIncrement(self, value):
        self._set_attribute('ipAddressIncrement', value)

    @property
    def IpAddressPoolIncrement(self):
        """The increment value for the starting lease address.

        Returns:
            str
        """
        return self._get_attribute('ipAddressPoolIncrement')
    @IpAddressPoolIncrement.setter
    def IpAddressPoolIncrement(self, value):
        self._set_attribute('ipAddressPoolIncrement', value)

    @property
    def IpAddressPrefix(self):
        """The prefix of the first lease pool.

        Returns:
            str
        """
        return self._get_attribute('ipAddressPrefix')
    @IpAddressPrefix.setter
    def IpAddressPrefix(self, value):
        self._set_attribute('ipAddressPrefix', value)

    @property
    def IpAddressPrefixIncrement(self):
        """The increment value for the prefix of the lease address within the lease pool.

        Returns:
            str
        """
        return self._get_attribute('ipAddressPrefixIncrement')
    @IpAddressPrefixIncrement.setter
    def IpAddressPrefixIncrement(self, value):
        self._set_attribute('ipAddressPrefixIncrement', value)

    @property
    def IpAddressPrefixPoolIncrement(self):
        """The increment value for the prefix of the starting lease.

        Returns:
            str
        """
        return self._get_attribute('ipAddressPrefixPoolIncrement')
    @IpAddressPrefixPoolIncrement.setter
    def IpAddressPrefixPoolIncrement(self, value):
        self._set_attribute('ipAddressPrefixPoolIncrement', value)

    @property
    def IpDns1(self):
        """The first DNS address advertised in DHCP Offer and Reply messages.

        Returns:
            str
        """
        return self._get_attribute('ipDns1')
    @IpDns1.setter
    def IpDns1(self, value):
        self._set_attribute('ipDns1', value)

    @property
    def IpDns2(self):
        """The second DNS address advertised in DHCP Offer and Reply messages.

        Returns:
            str
        """
        return self._get_attribute('ipDns2')
    @IpDns2.setter
    def IpDns2(self, value):
        self._set_attribute('ipDns2', value)

    @property
    def IpGateway(self):
        """The Router address advertised in DHCP Offer and Reply messages.

        Returns:
            str
        """
        return self._get_attribute('ipGateway')
    @IpGateway.setter
    def IpGateway(self, value):
        self._set_attribute('ipGateway', value)

    @property
    def IpGatewayIncrement(self):
        """The increment value for the Router address.

        Returns:
            str
        """
        return self._get_attribute('ipGatewayIncrement')
    @IpGatewayIncrement.setter
    def IpGatewayIncrement(self, value):
        self._set_attribute('ipGatewayIncrement', value)

    @property
    def IpPrefix(self):
        """The Subnet Address length used to compute the subnetwork the advertised lease is part of.

        Returns:
            number
        """
        return self._get_attribute('ipPrefix')
    @IpPrefix.setter
    def IpPrefix(self, value):
        self._set_attribute('ipPrefix', value)

    @property
    def IpType(self):
        """The type of IP addresses to be created by this range.

        Returns:
            str
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PrefixCount(self):
        """The number of leases to be allocated per each server prefix.

        Returns:
            number
        """
        return self._get_attribute('prefixCount')
    @PrefixCount.setter
    def PrefixCount(self, value):
        self._set_attribute('prefixCount', value)

    @property
    def PrefixLength(self):
        """The Subnet Prefix length advertised in DHCP Offer and Reply messages.

        Returns:
            number
        """
        return self._get_attribute('prefixLength')
    @PrefixLength.setter
    def PrefixLength(self, value):
        self._set_attribute('prefixLength', value)

    @property
    def ServerAddress(self):
        """The IP address of the first server interface.

        Returns:
            str
        """
        return self._get_attribute('serverAddress')
    @ServerAddress.setter
    def ServerAddress(self, value):
        self._set_attribute('serverAddress', value)

    @property
    def ServerAddressIncrement(self):
        """The increment value for the server address.

        Returns:
            str
        """
        return self._get_attribute('serverAddressIncrement')
    @ServerAddressIncrement.setter
    def ServerAddressIncrement(self, value):
        self._set_attribute('serverAddressIncrement', value)

    @property
    def ServerCount(self):
        """The number of server addresses to create for this range.

        Returns:
            number
        """
        return self._get_attribute('serverCount')
    @ServerCount.setter
    def ServerCount(self, value):
        self._set_attribute('serverCount', value)

    @property
    def ServerGateway(self):
        """The gateway address associated with DHCP server interfaces.

        Returns:
            str
        """
        return self._get_attribute('serverGateway')
    @ServerGateway.setter
    def ServerGateway(self, value):
        self._set_attribute('serverGateway', value)

    @property
    def ServerGatewayIncrement(self):
        """The increment value for the gateway addresses.

        Returns:
            str
        """
        return self._get_attribute('serverGatewayIncrement')
    @ServerGatewayIncrement.setter
    def ServerGatewayIncrement(self, value):
        self._set_attribute('serverGatewayIncrement', value)

    @property
    def ServerPrefix(self):
        """The subnet prefix length associated with server interfaces.

        Returns:
            number
        """
        return self._get_attribute('serverPrefix')
    @ServerPrefix.setter
    def ServerPrefix(self, value):
        self._set_attribute('serverPrefix', value)

    @property
    def UseRapidCommit(self):
        """Enables DHCP Server to negotiate leases with rapid commit for DHCP Clients that request it.

        Returns:
            bool
        """
        return self._get_attribute('useRapidCommit')
    @UseRapidCommit.setter
    def UseRapidCommit(self, value):
        self._set_attribute('useRapidCommit', value)

    def update(self, Count=None, Dhcp4EchoRelayInfo=None, Dhcp6IaType=None, Enabled=None, IpAddress=None, IpAddressIncrement=None, IpAddressPoolIncrement=None, IpAddressPrefix=None, IpAddressPrefixIncrement=None, IpAddressPrefixPoolIncrement=None, IpDns1=None, IpDns2=None, IpGateway=None, IpGatewayIncrement=None, IpPrefix=None, IpType=None, Name=None, PrefixCount=None, PrefixLength=None, ServerAddress=None, ServerAddressIncrement=None, ServerCount=None, ServerGateway=None, ServerGatewayIncrement=None, ServerPrefix=None, UseRapidCommit=None):
        """Updates a child instance of dhcpServerRange on the server.

        Args:
            Count (number): The number of leases to be allocated per each server address.
            Dhcp4EchoRelayInfo (bool): Enable echoing of DHCP option 82.
            Dhcp6IaType (str): The Identity Association type supported by IPv6 address pools.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpAddress (str): The IP address of the first lease pool.
            IpAddressIncrement (str): The increment value for the lease address within the lease pool.
            IpAddressPoolIncrement (str): The increment value for the starting lease address.
            IpAddressPrefix (str): The prefix of the first lease pool.
            IpAddressPrefixIncrement (str): The increment value for the prefix of the lease address within the lease pool.
            IpAddressPrefixPoolIncrement (str): The increment value for the prefix of the starting lease.
            IpDns1 (str): The first DNS address advertised in DHCP Offer and Reply messages.
            IpDns2 (str): The second DNS address advertised in DHCP Offer and Reply messages.
            IpGateway (str): The Router address advertised in DHCP Offer and Reply messages.
            IpGatewayIncrement (str): The increment value for the Router address.
            IpPrefix (number): The Subnet Address length used to compute the subnetwork the advertised lease is part of.
            IpType (str): The type of IP addresses to be created by this range.
            Name (str): Name of range
            PrefixCount (number): The number of leases to be allocated per each server prefix.
            PrefixLength (number): The Subnet Prefix length advertised in DHCP Offer and Reply messages.
            ServerAddress (str): The IP address of the first server interface.
            ServerAddressIncrement (str): The increment value for the server address.
            ServerCount (number): The number of server addresses to create for this range.
            ServerGateway (str): The gateway address associated with DHCP server interfaces.
            ServerGatewayIncrement (str): The increment value for the gateway addresses.
            ServerPrefix (number): The subnet prefix length associated with server interfaces.
            UseRapidCommit (bool): Enables DHCP Server to negotiate leases with rapid commit for DHCP Clients that request it.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
