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


class DcbxTlvPfcQaz(Base):
    """DCBX Priority-based Flow Control Configuration TLV for 802.1Qaz.
    The DcbxTlvPfcQaz class encapsulates a required dcbxTlvPfcQaz resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dcbxTlvPfcQaz"
    _SDM_ATT_MAP = {
        "Mbc": "mbc",
        "ObjectId": "objectId",
        "PfcCapability": "pfcCapability",
        "PfcEnableVector": "pfcEnableVector",
        "Willing": "willing",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DcbxTlvPfcQaz, self).__init__(parent, list_op)

    @property
    def Mbc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MACsec Bypass Capability Bit. Indicates whether the station is capable of bypassing MACsec when MACsec is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mbc"])

    @Mbc.setter
    def Mbc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mbc"], value)

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
    def PfcCapability(self):
        # type: () -> int
        """
        Returns
        -------
        - number: How many traffic classes may simultaneously support PFC.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcCapability"])

    @PfcCapability.setter
    def PfcCapability(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcCapability"], value)

    @property
    def PfcEnableVector(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): enable/disable PFC for each priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcEnableVector"])

    @PfcEnableVector.setter
    def PfcEnableVector(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcEnableVector"], value)

    @property
    def Willing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether this feature accepts its configuration from remote peers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Willing"])

    @Willing.setter
    def Willing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Willing"], value)

    def update(self, Mbc=None, PfcCapability=None, PfcEnableVector=None, Willing=None):
        # type: (bool, int, List[int], bool) -> DcbxTlvPfcQaz
        """Updates dcbxTlvPfcQaz resource on the server.

        Args
        ----
        - Mbc (bool): MACsec Bypass Capability Bit. Indicates whether the station is capable of bypassing MACsec when MACsec is disabled.
        - PfcCapability (number): How many traffic classes may simultaneously support PFC.
        - PfcEnableVector (list(number)): enable/disable PFC for each priority.
        - Willing (bool): Indicates whether this feature accepts its configuration from remote peers.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Mbc=None,
        ObjectId=None,
        PfcCapability=None,
        PfcEnableVector=None,
        Willing=None,
    ):
        # type: (bool, str, int, List[int], bool) -> DcbxTlvPfcQaz
        """Finds and retrieves dcbxTlvPfcQaz resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxTlvPfcQaz resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxTlvPfcQaz resources from the server.

        Args
        ----
        - Mbc (bool): MACsec Bypass Capability Bit. Indicates whether the station is capable of bypassing MACsec when MACsec is disabled.
        - ObjectId (str): Unique identifier for this object
        - PfcCapability (number): How many traffic classes may simultaneously support PFC.
        - PfcEnableVector (list(number)): enable/disable PFC for each priority.
        - Willing (bool): Indicates whether this feature accepts its configuration from remote peers.

        Returns
        -------
        - self: This instance with matching dcbxTlvPfcQaz resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxTlvPfcQaz data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxTlvPfcQaz resources from the server available through an iterator or index

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
