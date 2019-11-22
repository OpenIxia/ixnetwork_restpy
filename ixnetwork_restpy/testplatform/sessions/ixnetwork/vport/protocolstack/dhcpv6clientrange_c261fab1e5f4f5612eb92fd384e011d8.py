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


class Dhcpv6ClientRange(Base):
    """Manages a range of IP addresses that are configured using DHCP protocol.
    The Dhcpv6ClientRange class encapsulates a list of dhcpv6ClientRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6ClientRange.find() method.
    The list can be managed by the user by using the Dhcpv6ClientRange.add() and Dhcpv6ClientRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6ClientRange'

    def __init__(self, parent):
        super(Dhcpv6ClientRange, self).__init__(parent)

    @property
    def Dhcp6DuidEnterpriseId(self):
        """The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.

        Returns:
            number
        """
        return self._get_attribute('dhcp6DuidEnterpriseId')
    @Dhcp6DuidEnterpriseId.setter
    def Dhcp6DuidEnterpriseId(self, value):
        self._set_attribute('dhcp6DuidEnterpriseId', value)

    @property
    def Dhcp6DuidType(self):
        """DHCP Unique Identifier Type.

        Returns:
            str
        """
        return self._get_attribute('dhcp6DuidType')
    @Dhcp6DuidType.setter
    def Dhcp6DuidType(self, value):
        self._set_attribute('dhcp6DuidType', value)

    @property
    def Dhcp6DuidVendorId(self):
        """The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.

        Returns:
            number
        """
        return self._get_attribute('dhcp6DuidVendorId')
    @Dhcp6DuidVendorId.setter
    def Dhcp6DuidVendorId(self, value):
        self._set_attribute('dhcp6DuidVendorId', value)

    @property
    def Dhcp6DuidVendorIdIncrement(self):
        """The value by which the VENDOR-ID is incremented for each DHCP client.

        Returns:
            number
        """
        return self._get_attribute('dhcp6DuidVendorIdIncrement')
    @Dhcp6DuidVendorIdIncrement.setter
    def Dhcp6DuidVendorIdIncrement(self, value):
        self._set_attribute('dhcp6DuidVendorIdIncrement', value)

    @property
    def Dhcp6ParamRequestList(self):
        """The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.

        Returns:
            str
        """
        return self._get_attribute('dhcp6ParamRequestList')
    @Dhcp6ParamRequestList.setter
    def Dhcp6ParamRequestList(self, value):
        self._set_attribute('dhcp6ParamRequestList', value)

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
    def IpType(self):
        """Defines the version of IP address style to be used for describing the range.

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
    def UseVendorClassId(self):
        """Enables use of the Vendor Class Identifier configured in the field below.

        Returns:
            bool
        """
        return self._get_attribute('useVendorClassId')
    @UseVendorClassId.setter
    def UseVendorClassId(self, value):
        self._set_attribute('useVendorClassId', value)

    @property
    def VendorClassId(self):
        """This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns:
            str
        """
        return self._get_attribute('vendorClassId')
    @VendorClassId.setter
    def VendorClassId(self, value):
        self._set_attribute('vendorClassId', value)

    def update(self, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6DuidVendorIdIncrement=None, Dhcp6ParamRequestList=None, Enabled=None, IpType=None, Name=None, UseVendorClassId=None, VendorClassId=None):
        """Updates a child instance of dhcpv6ClientRange on the server.

        Args:
            Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
            Dhcp6DuidType (str): DHCP Unique Identifier Type.
            Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
            Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
            Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the version of IP address style to be used for describing the range.
            Name (str): Name of range
            UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
            VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6DuidVendorIdIncrement=None, Dhcp6ParamRequestList=None, Enabled=None, IpType=None, Name=None, UseVendorClassId=None, VendorClassId=None):
        """Adds a new dhcpv6ClientRange node on the server and retrieves it in this instance.

        Args:
            Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
            Dhcp6DuidType (str): DHCP Unique Identifier Type.
            Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
            Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
            Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the version of IP address style to be used for describing the range.
            Name (str): Name of range
            UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
            VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns:
            self: This instance with all currently retrieved dhcpv6ClientRange data using find and the newly added dhcpv6ClientRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpv6ClientRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6DuidVendorIdIncrement=None, Dhcp6ParamRequestList=None, Enabled=None, IpType=None, Name=None, ObjectId=None, UseVendorClassId=None, VendorClassId=None):
        """Finds and retrieves dhcpv6ClientRange data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpv6ClientRange data from the server.
        By default the find method takes no parameters and will retrieve all dhcpv6ClientRange data from the server.

        Args:
            Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
            Dhcp6DuidType (str): DHCP Unique Identifier Type.
            Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
            Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
            Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the version of IP address style to be used for describing the range.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
            VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns:
            self: This instance with matching dhcpv6ClientRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpv6ClientRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpv6ClientRange data from the server available through an iterator or index

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
