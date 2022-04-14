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


class DcbxTlvPgIeee(Base):
    """DCBX Priority Groups TLV for IEEE 1.01.
    The DcbxTlvPgIeee class encapsulates a required dcbxTlvPgIeee resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dcbxTlvPgIeee"
    _SDM_ATT_MAP = {
        "ObjectId": "objectId",
        "PriorityGroupIdMap": "priorityGroupIdMap",
        "PriorityGroupPercentageMap": "priorityGroupPercentageMap",
        "TcsSupported": "tcsSupported",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DcbxTlvPgIeee, self).__init__(parent, list_op)

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
    def PriorityGroupIdMap(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Priority group ID associated to each priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityGroupIdMap"])

    @PriorityGroupIdMap.setter
    def PriorityGroupIdMap(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PriorityGroupIdMap"], value)

    @property
    def PriorityGroupPercentageMap(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Percentage associated to each priority group id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityGroupPercentageMap"])

    @PriorityGroupPercentageMap.setter
    def PriorityGroupPercentageMap(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PriorityGroupPercentageMap"], value)

    @property
    def TcsSupported(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of traffic classes supported by device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcsSupported"])

    @TcsSupported.setter
    def TcsSupported(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcsSupported"], value)

    def update(
        self,
        PriorityGroupIdMap=None,
        PriorityGroupPercentageMap=None,
        TcsSupported=None,
    ):
        # type: (List[int], List[int], int) -> DcbxTlvPgIeee
        """Updates dcbxTlvPgIeee resource on the server.

        Args
        ----
        - PriorityGroupIdMap (list(number)): Priority group ID associated to each priority.
        - PriorityGroupPercentageMap (list(number)): Percentage associated to each priority group id.
        - TcsSupported (number): Number of traffic classes supported by device.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ObjectId=None,
        PriorityGroupIdMap=None,
        PriorityGroupPercentageMap=None,
        TcsSupported=None,
    ):
        # type: (str, List[int], List[int], int) -> DcbxTlvPgIeee
        """Finds and retrieves dcbxTlvPgIeee resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxTlvPgIeee resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxTlvPgIeee resources from the server.

        Args
        ----
        - ObjectId (str): Unique identifier for this object
        - PriorityGroupIdMap (list(number)): Priority group ID associated to each priority.
        - PriorityGroupPercentageMap (list(number)): Percentage associated to each priority group id.
        - TcsSupported (number): Number of traffic classes supported by device.

        Returns
        -------
        - self: This instance with matching dcbxTlvPgIeee resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxTlvPgIeee data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxTlvPgIeee resources from the server available through an iterator or index

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
