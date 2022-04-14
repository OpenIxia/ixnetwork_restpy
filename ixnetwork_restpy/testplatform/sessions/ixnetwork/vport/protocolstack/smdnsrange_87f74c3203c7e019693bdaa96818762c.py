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


class SmDnsRange(Base):
    """DNS Range
    The SmDnsRange class encapsulates a required smDnsRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "smDnsRange"
    _SDM_ATT_MAP = {
        "CacheReplies": "cacheReplies",
        "EdnsReceiveBufferSize": "ednsReceiveBufferSize",
        "Enabled": "enabled",
        "Name": "name",
        "ObjectId": "objectId",
        "ResolveDns": "resolveDns",
        "ServerIp": "serverIp",
        "UseAdditionalRecords": "useAdditionalRecords",
        "UseEdns": "useEdns",
        "UseTcp": "useTcp",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SmDnsRange, self).__init__(parent, list_op)

    @property
    def CacheReplies(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Cache DNS Replies
        """
        return self._get_attribute(self._SDM_ATT_MAP["CacheReplies"])

    @CacheReplies.setter
    def CacheReplies(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CacheReplies"], value)

    @property
    def EdnsReceiveBufferSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: UDP Payload Size
        """
        return self._get_attribute(self._SDM_ATT_MAP["EdnsReceiveBufferSize"])

    @EdnsReceiveBufferSize.setter
    def EdnsReceiveBufferSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EdnsReceiveBufferSize"], value)

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
    def ResolveDns(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Resolve DNS
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResolveDns"])

    @ResolveDns.setter
    def ResolveDns(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResolveDns"], value)

    @property
    def ServerIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: DNS server IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerIp"])

    @ServerIp.setter
    def ServerIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerIp"], value)

    @property
    def UseAdditionalRecords(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use Additional Records if included by the server to avoid doing redundant A/AAAA queries
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseAdditionalRecords"])

    @UseAdditionalRecords.setter
    def UseAdditionalRecords(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseAdditionalRecords"], value)

    @property
    def UseEdns(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use EDNS
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseEdns"])

    @UseEdns.setter
    def UseEdns(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseEdns"], value)

    @property
    def UseTcp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use TCP connections for DNS queries instead of UDP packets
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseTcp"])

    @UseTcp.setter
    def UseTcp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseTcp"], value)

    def update(
        self,
        CacheReplies=None,
        EdnsReceiveBufferSize=None,
        Enabled=None,
        Name=None,
        ResolveDns=None,
        ServerIp=None,
        UseAdditionalRecords=None,
        UseEdns=None,
        UseTcp=None,
    ):
        # type: (bool, int, bool, str, bool, str, bool, bool, bool) -> SmDnsRange
        """Updates smDnsRange resource on the server.

        Args
        ----
        - CacheReplies (bool): Cache DNS Replies
        - EdnsReceiveBufferSize (number): UDP Payload Size
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - ResolveDns (bool): Resolve DNS
        - ServerIp (str): DNS server IP address
        - UseAdditionalRecords (bool): Use Additional Records if included by the server to avoid doing redundant A/AAAA queries
        - UseEdns (bool): Use EDNS
        - UseTcp (bool): Use TCP connections for DNS queries instead of UDP packets

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CacheReplies=None,
        EdnsReceiveBufferSize=None,
        Enabled=None,
        Name=None,
        ObjectId=None,
        ResolveDns=None,
        ServerIp=None,
        UseAdditionalRecords=None,
        UseEdns=None,
        UseTcp=None,
    ):
        # type: (bool, int, bool, str, str, bool, str, bool, bool, bool) -> SmDnsRange
        """Finds and retrieves smDnsRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve smDnsRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all smDnsRange resources from the server.

        Args
        ----
        - CacheReplies (bool): Cache DNS Replies
        - EdnsReceiveBufferSize (number): UDP Payload Size
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - ResolveDns (bool): Resolve DNS
        - ServerIp (str): DNS server IP address
        - UseAdditionalRecords (bool): Use Additional Records if included by the server to avoid doing redundant A/AAAA queries
        - UseEdns (bool): Use EDNS
        - UseTcp (bool): Use TCP connections for DNS queries instead of UDP packets

        Returns
        -------
        - self: This instance with matching smDnsRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of smDnsRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the smDnsRange resources from the server available through an iterator or index

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
