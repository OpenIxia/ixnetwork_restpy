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


class Dhcpv6ClientRange(Base):
    """Manages a range of IP addresses that are configured using DHCP protocol.
    The Dhcpv6ClientRange class encapsulates a list of dhcpv6ClientRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6ClientRange.find() method.
    The list can be managed by using the Dhcpv6ClientRange.add() and Dhcpv6ClientRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "dhcpv6ClientRange"
    _SDM_ATT_MAP = {
        "Dhcp6DuidEnterpriseId": "dhcp6DuidEnterpriseId",
        "Dhcp6DuidType": "dhcp6DuidType",
        "Dhcp6DuidVendorId": "dhcp6DuidVendorId",
        "Dhcp6DuidVendorIdIncrement": "dhcp6DuidVendorIdIncrement",
        "Dhcp6ParamRequestList": "dhcp6ParamRequestList",
        "Enabled": "enabled",
        "IpType": "ipType",
        "Name": "name",
        "ObjectId": "objectId",
        "UseVendorClassId": "useVendorClassId",
        "VendorClassId": "vendorClassId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Dhcpv6ClientRange, self).__init__(parent, list_op)

    @property
    def Dhcp6DuidEnterpriseId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidEnterpriseId"])

    @Dhcp6DuidEnterpriseId.setter
    def Dhcp6DuidEnterpriseId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidEnterpriseId"], value)

    @property
    def Dhcp6DuidType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: DHCP Unique Identifier Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidType"])

    @Dhcp6DuidType.setter
    def Dhcp6DuidType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidType"], value)

    @property
    def Dhcp6DuidVendorId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorId"])

    @Dhcp6DuidVendorId.setter
    def Dhcp6DuidVendorId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorId"], value)

    @property
    def Dhcp6DuidVendorIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value by which the VENDOR-ID is incremented for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorIdIncrement"])

    @Dhcp6DuidVendorIdIncrement.setter
    def Dhcp6DuidVendorIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorIdIncrement"], value)

    @property
    def Dhcp6ParamRequestList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6ParamRequestList"])

    @Dhcp6ParamRequestList.setter
    def Dhcp6ParamRequestList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6ParamRequestList"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the version of IP address style to be used for describing the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def UseVendorClassId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables use of the Vendor Class Identifier configured in the field below.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseVendorClassId"])

    @UseVendorClassId.setter
    def UseVendorClassId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseVendorClassId"], value)

    @property
    def VendorClassId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorClassId"])

    @VendorClassId.setter
    def VendorClassId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorClassId"], value)

    def update(
        self,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6ParamRequestList=None,
        Enabled=None,
        IpType=None,
        Name=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (int, str, int, int, str, bool, str, str, bool, str) -> Dhcpv6ClientRange
        """Updates dhcpv6ClientRange resource on the server.

        Args
        ----
        - Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        - Dhcp6DuidType (str): DHCP Unique Identifier Type.
        - Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
        - Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Name (str): Name of range
        - UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
        - VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6ParamRequestList=None,
        Enabled=None,
        IpType=None,
        Name=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (int, str, int, int, str, bool, str, str, bool, str) -> Dhcpv6ClientRange
        """Adds a new dhcpv6ClientRange resource on the server and adds it to the container.

        Args
        ----
        - Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        - Dhcp6DuidType (str): DHCP Unique Identifier Type.
        - Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
        - Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Name (str): Name of range
        - UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
        - VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpv6ClientRange resources using find and the newly added dhcpv6ClientRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpv6ClientRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6ParamRequestList=None,
        Enabled=None,
        IpType=None,
        Name=None,
        ObjectId=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (int, str, int, int, str, bool, str, str, str, bool, str) -> Dhcpv6ClientRange
        """Finds and retrieves dhcpv6ClientRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv6ClientRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv6ClientRange resources from the server.

        Args
        ----
        - Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        - Dhcp6DuidType (str): DHCP Unique Identifier Type.
        - Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
        - Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
        - VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns
        -------
        - self: This instance with matching dhcpv6ClientRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv6ClientRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv6ClientRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
            "enableProtocolStack", payload=payload, response_object=None
        )
