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


class IpRangeOptions(Base):
    """Ip V4V6 Range session specific data
    The IpRangeOptions class encapsulates a list of ipRangeOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the IpRangeOptions.find() method.
    The list can be managed by using the IpRangeOptions.add() and IpRangeOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipRangeOptions'
    _SDM_ATT_MAP = {
        'GatewayArpRequestRate': 'gatewayArpRequestRate',
        'Icmpv6DiscardRouterAdvertisements': 'icmpv6DiscardRouterAdvertisements',
        'Ipv6AddressMode': 'ipv6AddressMode',
        'Ipv6ConfigRate': 'ipv6ConfigRate',
        'Ipv6ConfigRateEnable': 'ipv6ConfigRateEnable',
        'MaxOutstandingGatewayArpRequests': 'maxOutstandingGatewayArpRequests',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(IpRangeOptions, self).__init__(parent)

    @property
    def GatewayArpRequestRate(self):
        """DEPRECATED 
        Returns
        -------
        - number: Maximum ARP request rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['GatewayArpRequestRate'])
    @GatewayArpRequestRate.setter
    def GatewayArpRequestRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GatewayArpRequestRate'], value)

    @property
    def Icmpv6DiscardRouterAdvertisements(self):
        """
        Returns
        -------
        - bool: When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Icmpv6DiscardRouterAdvertisements'])
    @Icmpv6DiscardRouterAdvertisements.setter
    def Icmpv6DiscardRouterAdvertisements(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Icmpv6DiscardRouterAdvertisements'], value)

    @property
    def Ipv6AddressMode(self):
        """
        Returns
        -------
        - str: Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6AddressMode'])
    @Ipv6AddressMode.setter
    def Ipv6AddressMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6AddressMode'], value)

    @property
    def Ipv6ConfigRate(self):
        """
        Returns
        -------
        - number: Number of IPv6 addresses to be configured per second. This is a best effort rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ConfigRate'])
    @Ipv6ConfigRate.setter
    def Ipv6ConfigRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ConfigRate'], value)

    @property
    def Ipv6ConfigRateEnable(self):
        """
        Returns
        -------
        - bool: When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ConfigRateEnable'])
    @Ipv6ConfigRateEnable.setter
    def Ipv6ConfigRateEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6ConfigRateEnable'], value)

    @property
    def MaxOutstandingGatewayArpRequests(self):
        """DEPRECATED 
        Returns
        -------
        - number: Threshold at which the plugin begins throttling back the number of new requests sent out.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingGatewayArpRequests'])
    @MaxOutstandingGatewayArpRequests.setter
    def MaxOutstandingGatewayArpRequests(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingGatewayArpRequests'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, GatewayArpRequestRate=None, Icmpv6DiscardRouterAdvertisements=None, Ipv6AddressMode=None, Ipv6ConfigRate=None, Ipv6ConfigRateEnable=None, MaxOutstandingGatewayArpRequests=None):
        """Updates ipRangeOptions resource on the server.

        Args
        ----
        - GatewayArpRequestRate (number): Maximum ARP request rate
        - Icmpv6DiscardRouterAdvertisements (bool): When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
        - Ipv6AddressMode (str): Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
        - Ipv6ConfigRate (number): Number of IPv6 addresses to be configured per second. This is a best effort rate.
        - Ipv6ConfigRateEnable (bool): When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
        - MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new requests sent out.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, GatewayArpRequestRate=None, Icmpv6DiscardRouterAdvertisements=None, Ipv6AddressMode=None, Ipv6ConfigRate=None, Ipv6ConfigRateEnable=None, MaxOutstandingGatewayArpRequests=None):
        """Adds a new ipRangeOptions resource on the server and adds it to the container.

        Args
        ----
        - GatewayArpRequestRate (number): Maximum ARP request rate
        - Icmpv6DiscardRouterAdvertisements (bool): When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
        - Ipv6AddressMode (str): Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
        - Ipv6ConfigRate (number): Number of IPv6 addresses to be configured per second. This is a best effort rate.
        - Ipv6ConfigRateEnable (bool): When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
        - MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new requests sent out.

        Returns
        -------
        - self: This instance with all currently retrieved ipRangeOptions resources using find and the newly added ipRangeOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ipRangeOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, GatewayArpRequestRate=None, Icmpv6DiscardRouterAdvertisements=None, Ipv6AddressMode=None, Ipv6ConfigRate=None, Ipv6ConfigRateEnable=None, MaxOutstandingGatewayArpRequests=None, ObjectId=None):
        """Finds and retrieves ipRangeOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipRangeOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipRangeOptions resources from the server.

        Args
        ----
        - GatewayArpRequestRate (number): Maximum ARP request rate
        - Icmpv6DiscardRouterAdvertisements (bool): When enabled, IPv6 plugin will filter out ICMPv6 RA messages.
        - Ipv6AddressMode (str): Indicates whether static allocation or autoconfiguration of IPv6 addresses is used. Please note that this setting will only be applied to IPv6 stacks configured on the port. More settings in Protocols->Options.
        - Ipv6ConfigRate (number): Number of IPv6 addresses to be configured per second. This is a best effort rate.
        - Ipv6ConfigRateEnable (bool): When enabled, IPv6 plugin will configure IPv6 addresses at specified rate. This is a best effort rate.
        - MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new requests sent out.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching ipRangeOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipRangeOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipRangeOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
