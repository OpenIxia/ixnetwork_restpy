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


class DcbxTlvEtsQaz(Base):
    """DCBX ETS Configuration/Recommendation TLV for 802.1Qaz.
    The DcbxTlvEtsQaz class encapsulates a required dcbxTlvEtsQaz resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dcbxTlvEtsQaz"
    _SDM_ATT_MAP = {
        "Cbs": "cbs",
        "MaxTcs": "maxTcs",
        "ObjectId": "objectId",
        "TcGroupBwPercentMap": "tcGroupBwPercentMap",
        "TcGroupPriorityMap": "tcGroupPriorityMap",
        "TcGroupTsaMap": "tcGroupTsaMap",
        "TlvSendOrder": "tlvSendOrder",
        "TlvSendRestriction": "tlvSendRestriction",
        "Willing": "willing",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DcbxTlvEtsQaz, self).__init__(parent, list_op)

    @property
    def Cbs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether the station supports credit-based shaper transmission selection algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cbs"])

    @Cbs.setter
    def Cbs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Cbs"], value)

    @property
    def MaxTcs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of traffic classes supported by device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxTcs"])

    @MaxTcs.setter
    def MaxTcs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxTcs"], value)

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
    def TcGroupBwPercentMap(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Bandwidth percentage
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcGroupBwPercentMap"])

    @TcGroupBwPercentMap.setter
    def TcGroupBwPercentMap(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcGroupBwPercentMap"], value)

    @property
    def TcGroupPriorityMap(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number):
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcGroupPriorityMap"])

    @TcGroupPriorityMap.setter
    def TcGroupPriorityMap(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcGroupPriorityMap"], value)

    @property
    def TcGroupTsaMap(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Transmission selection algorithm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcGroupTsaMap"])

    @TcGroupTsaMap.setter
    def TcGroupTsaMap(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcGroupTsaMap"], value)

    @property
    def TlvSendOrder(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Configure the order in which the ETS TLVs are sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["TlvSendOrder"])

    @TlvSendOrder.setter
    def TlvSendOrder(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TlvSendOrder"], value)

    @property
    def TlvSendRestriction(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Configure if ETS will send the Configuration TLV, Recommendation TLV or both
        """
        return self._get_attribute(self._SDM_ATT_MAP["TlvSendRestriction"])

    @TlvSendRestriction.setter
    def TlvSendRestriction(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TlvSendRestriction"], value)

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

    def update(
        self,
        Cbs=None,
        MaxTcs=None,
        TcGroupBwPercentMap=None,
        TcGroupPriorityMap=None,
        TcGroupTsaMap=None,
        TlvSendOrder=None,
        TlvSendRestriction=None,
        Willing=None,
    ):
        # type: (bool, int, List[int], List[int], List[int], int, int, bool) -> DcbxTlvEtsQaz
        """Updates dcbxTlvEtsQaz resource on the server.

        Args
        ----
        - Cbs (bool): Indicates whether the station supports credit-based shaper transmission selection algorithm.
        - MaxTcs (number): Number of traffic classes supported by device.
        - TcGroupBwPercentMap (list(number)): Bandwidth percentage
        - TcGroupPriorityMap (list(number)):
        - TcGroupTsaMap (list(number)): Transmission selection algorithm
        - TlvSendOrder (number): Configure the order in which the ETS TLVs are sent
        - TlvSendRestriction (number): Configure if ETS will send the Configuration TLV, Recommendation TLV or both
        - Willing (bool): Indicates whether this feature accepts its configuration from remote peers.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Cbs=None,
        MaxTcs=None,
        ObjectId=None,
        TcGroupBwPercentMap=None,
        TcGroupPriorityMap=None,
        TcGroupTsaMap=None,
        TlvSendOrder=None,
        TlvSendRestriction=None,
        Willing=None,
    ):
        # type: (bool, int, str, List[int], List[int], List[int], int, int, bool) -> DcbxTlvEtsQaz
        """Finds and retrieves dcbxTlvEtsQaz resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxTlvEtsQaz resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxTlvEtsQaz resources from the server.

        Args
        ----
        - Cbs (bool): Indicates whether the station supports credit-based shaper transmission selection algorithm.
        - MaxTcs (number): Number of traffic classes supported by device.
        - ObjectId (str): Unique identifier for this object
        - TcGroupBwPercentMap (list(number)): Bandwidth percentage
        - TcGroupPriorityMap (list(number)):
        - TcGroupTsaMap (list(number)): Transmission selection algorithm
        - TlvSendOrder (number): Configure the order in which the ETS TLVs are sent
        - TlvSendRestriction (number): Configure if ETS will send the Configuration TLV, Recommendation TLV or both
        - Willing (bool): Indicates whether this feature accepts its configuration from remote peers.

        Returns
        -------
        - self: This instance with matching dcbxTlvEtsQaz resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxTlvEtsQaz data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxTlvEtsQaz resources from the server available through an iterator or index

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
