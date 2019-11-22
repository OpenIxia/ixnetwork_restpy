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


class IpRangeOptions(Base):
    """Ip V4V6 Range session specific data
    The IpRangeOptions class encapsulates a list of ipRangeOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IpRangeOptions.find() method.
    The list can be managed by the user by using the IpRangeOptions.add() and IpRangeOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipRangeOptions'

    def __init__(self, parent):
        super(IpRangeOptions, self).__init__(parent)

    @property
    def GatewayArpRequestRate(self):
        """DEPRECATED Maximum ARP request rate

        Returns:
            number
        """
        return self._get_attribute('gatewayArpRequestRate')
    @GatewayArpRequestRate.setter
    def GatewayArpRequestRate(self, value):
        self._set_attribute('gatewayArpRequestRate', value)

    @property
    def Icmpv6DiscardRouterAdvertisements(self):
        """When enabled, IPv6 plugin will filter out ICMPv6 RA messages.

        Returns:
            bool
        """
        return self._get_attribute('icmpv6DiscardRouterAdvertisements')
    @Icmpv6DiscardRouterAdvertisements.setter
    def Icmpv6DiscardRouterAdvertisements(self, value):
        self._set_attribute('icmpv6DiscardRouterAdvertisements', value)

    @property
    def Ipv6AddressMode(self):
        """Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.

        Returns:
            str
        """
        return self._get_attribute('ipv6AddressMode')
    @Ipv6AddressMode.setter
    def Ipv6AddressMode(self, value):
        self._set_attribute('ipv6AddressMode', value)

    @property
    def Ipv6ConfigRate(self):
        """Number of IPv6 addresses to be configured per second. This is a best effort rate.

        Returns:
            number
        """
        return self._get_attribute('ipv6ConfigRate')
    @Ipv6ConfigRate.setter
    def Ipv6ConfigRate(self, value):
        self._set_attribute('ipv6ConfigRate', value)

    @property
    def Ipv6ConfigRateEnable(self):
        """When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.

        Returns:
            bool
        """
        return self._get_attribute('ipv6ConfigRateEnable')
    @Ipv6ConfigRateEnable.setter
    def Ipv6ConfigRateEnable(self, value):
        self._set_attribute('ipv6ConfigRateEnable', value)

    @property
    def MaxOutstandingGatewayArpRequests(self):
        """DEPRECATED Threshold at which the plugin begins throttling back the number of new requests sent out.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingGatewayArpRequests')
    @MaxOutstandingGatewayArpRequests.setter
    def MaxOutstandingGatewayArpRequests(self, value):
        self._set_attribute('maxOutstandingGatewayArpRequests', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, GatewayArpRequestRate=None, Icmpv6DiscardRouterAdvertisements=None, Ipv6AddressMode=None, Ipv6ConfigRate=None, Ipv6ConfigRateEnable=None, MaxOutstandingGatewayArpRequests=None):
        """Updates a child instance of ipRangeOptions on the server.

        Args:
            GatewayArpRequestRate (number): Maximum ARP request rate
            Icmpv6DiscardRouterAdvertisements (bool): When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
            Ipv6AddressMode (str): Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
            Ipv6ConfigRate (number): Number of IPv6 addresses to be configured per second. This is a best effort rate.
            Ipv6ConfigRateEnable (bool): When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new requests sent out.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, GatewayArpRequestRate=None, Icmpv6DiscardRouterAdvertisements=None, Ipv6AddressMode=None, Ipv6ConfigRate=None, Ipv6ConfigRateEnable=None, MaxOutstandingGatewayArpRequests=None):
        """Adds a new ipRangeOptions node on the server and retrieves it in this instance.

        Args:
            GatewayArpRequestRate (number): Maximum ARP request rate
            Icmpv6DiscardRouterAdvertisements (bool): When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
            Ipv6AddressMode (str): Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
            Ipv6ConfigRate (number): Number of IPv6 addresses to be configured per second. This is a best effort rate.
            Ipv6ConfigRateEnable (bool): When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new requests sent out.

        Returns:
            self: This instance with all currently retrieved ipRangeOptions data using find and the newly added ipRangeOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the ipRangeOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, GatewayArpRequestRate=None, Icmpv6DiscardRouterAdvertisements=None, Ipv6AddressMode=None, Ipv6ConfigRate=None, Ipv6ConfigRateEnable=None, MaxOutstandingGatewayArpRequests=None, ObjectId=None):
        """Finds and retrieves ipRangeOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve ipRangeOptions data from the server.
        By default the find method takes no parameters and will retrieve all ipRangeOptions data from the server.

        Args:
            GatewayArpRequestRate (number): Maximum ARP request rate
            Icmpv6DiscardRouterAdvertisements (bool): When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
            Ipv6AddressMode (str): Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
            Ipv6ConfigRate (number): Number of IPv6 addresses to be configured per second. This is a best effort rate.
            Ipv6ConfigRateEnable (bool): When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new requests sent out.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching ipRangeOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ipRangeOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ipRangeOptions data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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
