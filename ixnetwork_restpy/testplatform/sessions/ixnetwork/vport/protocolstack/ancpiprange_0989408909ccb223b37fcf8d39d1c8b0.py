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


class AncpIpRange(Base):
    """Manages a range of IP addresses within a IpV4V6 stack element plugin.
    The AncpIpRange class encapsulates a required ancpIpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ancpIpRange"
    _SDM_ATT_MAP = {
        "AutoMacGeneration": "autoMacGeneration",
        "Count": "count",
        "EnableGatewayArp": "enableGatewayArp",
        "Enabled": "enabled",
        "GatewayAddress": "gatewayAddress",
        "GatewayIncrement": "gatewayIncrement",
        "GatewayIncrementMode": "gatewayIncrementMode",
        "IncrementBy": "incrementBy",
        "IpAddress": "ipAddress",
        "IpType": "ipType",
        "Mss": "mss",
        "Name": "name",
        "ObjectId": "objectId",
        "Prefix": "prefix",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AncpIpRange, self).__init__(parent, list_op)

    @property
    def AutoMacGeneration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set, MAC addresses will be auto-generated based on IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoMacGeneration"])

    @AutoMacGeneration.setter
    def AutoMacGeneration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoMacGeneration"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The total number of addresses to be created for the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def EnableGatewayArp(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Deprecated property, please use Static IP globals instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGatewayArp"])

    @EnableGatewayArp.setter
    def EnableGatewayArp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGatewayArp"], value)

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
    def GatewayAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the gateway to be associated with all the addresses created in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayAddress"])

    @GatewayAddress.setter
    def GatewayAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayAddress"], value)

    @property
    def GatewayIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the gateway step size to be used in the association with the addresses created in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayIncrement"])

    @GatewayIncrement.setter
    def GatewayIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayIncrement"], value)

    @property
    def GatewayIncrementMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the gateway step size to be used in the association with the addresses created in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayIncrementMode"])

    @GatewayIncrementMode.setter
    def GatewayIncrementMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayIncrementMode"], value)

    @property
    def IncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the increment to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementBy"])

    @IncrementBy.setter
    def IncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementBy"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the base address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

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
    def Mss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Maximum Segment Size, defines the maximum length of the data. TCP MSS = MTU - TCP header size - IP header size. Theoretically, this value can be as large as 65495, but such a large value is never used. For traditional Ethernet the maximum value for MSS is 1460 = 1500-40. With Jumbo Frame support, the maximum value is 9460 = 9500-40.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mss"])

    @Mss.setter
    def Mss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mss"], value)

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
    def Prefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Prefix"])

    @Prefix.setter
    def Prefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Prefix"], value)

    def update(
        self,
        AutoMacGeneration=None,
        Count=None,
        EnableGatewayArp=None,
        Enabled=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        GatewayIncrementMode=None,
        IncrementBy=None,
        IpAddress=None,
        IpType=None,
        Mss=None,
        Name=None,
        Prefix=None,
    ):
        # type: (bool, int, bool, bool, str, str, str, str, str, str, int, str, int) -> AncpIpRange
        """Updates ancpIpRange resource on the server.

        Args
        ----
        - AutoMacGeneration (bool): If set, MAC addresses will be auto-generated based on IP
        - Count (number): The total number of addresses to be created for the range.
        - EnableGatewayArp (bool): Deprecated property, please use Static IP globals instead.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GatewayAddress (str): Defines the gateway to be associated with all the addresses created in the range.
        - GatewayIncrement (str): Defines the gateway step size to be used in the association with the addresses created in the range.
        - GatewayIncrementMode (str): Defines the gateway step size to be used in the association with the addresses created in the range.
        - IncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - IpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Mss (number): The Maximum Segment Size, defines the maximum length of the data. TCP MSS = MTU - TCP header size - IP header size. Theoretically, this value can be as large as 65495, but such a large value is never used. For traditional Ethernet the maximum value for MSS is 1460 = 1500-40. With Jumbo Frame support, the maximum value is 9460 = 9500-40.
        - Name (str): Name of range
        - Prefix (number): Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoMacGeneration=None,
        Count=None,
        EnableGatewayArp=None,
        Enabled=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        GatewayIncrementMode=None,
        IncrementBy=None,
        IpAddress=None,
        IpType=None,
        Mss=None,
        Name=None,
        ObjectId=None,
        Prefix=None,
    ):
        # type: (bool, int, bool, bool, str, str, str, str, str, str, int, str, str, int) -> AncpIpRange
        """Finds and retrieves ancpIpRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ancpIpRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ancpIpRange resources from the server.

        Args
        ----
        - AutoMacGeneration (bool): If set, MAC addresses will be auto-generated based on IP
        - Count (number): The total number of addresses to be created for the range.
        - EnableGatewayArp (bool): Deprecated property, please use Static IP globals instead.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GatewayAddress (str): Defines the gateway to be associated with all the addresses created in the range.
        - GatewayIncrement (str): Defines the gateway step size to be used in the association with the addresses created in the range.
        - GatewayIncrementMode (str): Defines the gateway step size to be used in the association with the addresses created in the range.
        - IncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - IpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Mss (number): The Maximum Segment Size, defines the maximum length of the data. TCP MSS = MTU - TCP header size - IP header size. Theoretically, this value can be as large as 65495, but such a large value is never used. For traditional Ethernet the maximum value for MSS is 1460 = 1500-40. With Jumbo Frame support, the maximum value is 9460 = 9500-40.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Prefix (number): Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.

        Returns
        -------
        - self: This instance with matching ancpIpRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ancpIpRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ancpIpRange resources from the server available through an iterator or index

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
