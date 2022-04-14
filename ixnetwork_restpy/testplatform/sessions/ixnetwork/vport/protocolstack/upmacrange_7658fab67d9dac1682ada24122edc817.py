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


class UpMacRange(Base):
    """Range of multiple MAC addresses for fine grained configuration
    The UpMacRange class encapsulates a required upMacRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "upMacRange"
    _SDM_ATT_MAP = {
        "Count": "count",
        "Enabled": "enabled",
        "IncrementBy": "incrementBy",
        "Mac": "mac",
        "Mtu": "mtu",
        "Name": "name",
        "ObjectId": "objectId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(UpMacRange, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The total number of interfaces to be created for the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

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
    def IncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Incrementor used when the plugin creates a range of MACs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementBy"])

    @IncrementBy.setter
    def IncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementBy"], value)

    @property
    def Mac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Base value used when the plugin creates a MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mac"])

    @Mac.setter
    def Mac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mac"], value)

    @property
    def Mtu(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum Transmission Unit. The largest packet that a given network medium can carry. Ethernet, for example, has a fixed MTU of 1500 bytes without and 9500 bytes with Jumbo frame support. ATM has a fixed MTU of 48 bytes and PPP has a negotiated MTU that is usually between 500 and 2000 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mtu"])

    @Mtu.setter
    def Mtu(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mtu"], value)

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

    def update(
        self, Count=None, Enabled=None, IncrementBy=None, Mac=None, Mtu=None, Name=None
    ):
        # type: (int, bool, str, str, int, str) -> UpMacRange
        """Updates upMacRange resource on the server.

        Args
        ----
        - Count (number): The total number of interfaces to be created for the range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IncrementBy (str): Incrementor used when the plugin creates a range of MACs.
        - Mac (str): Base value used when the plugin creates a MAC address.
        - Mtu (number): Maximum Transmission Unit. The largest packet that a given network medium can carry. Ethernet, for example, has a fixed MTU of 1500 bytes without and 9500 bytes with Jumbo frame support. ATM has a fixed MTU of 48 bytes and PPP has a negotiated MTU that is usually between 500 and 2000 bytes.
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        Enabled=None,
        IncrementBy=None,
        Mac=None,
        Mtu=None,
        Name=None,
        ObjectId=None,
    ):
        # type: (int, bool, str, str, int, str, str) -> UpMacRange
        """Finds and retrieves upMacRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve upMacRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all upMacRange resources from the server.

        Args
        ----
        - Count (number): The total number of interfaces to be created for the range.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IncrementBy (str): Incrementor used when the plugin creates a range of MACs.
        - Mac (str): Base value used when the plugin creates a MAC address.
        - Mtu (number): Maximum Transmission Unit. The largest packet that a given network medium can carry. Ethernet, for example, has a fixed MTU of 1500 bytes without and 9500 bytes with Jumbo frame support. ATM has a fixed MTU of 48 bytes and PPP has a negotiated MTU that is usually between 500 and 2000 bytes.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching upMacRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of upMacRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the upMacRange resources from the server available through an iterator or index

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
