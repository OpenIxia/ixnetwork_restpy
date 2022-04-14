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


class SwitchFlow131TriggerAttributes(Base):
    """This object allows to configure the switch Flow 131 Trigger Attributes.
    The SwitchFlow131TriggerAttributes class encapsulates a required switchFlow131TriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "switchFlow131TriggerAttributes"
    _SDM_ATT_MAP = {
        "OutGroup": "outGroup",
        "OutGroupInputMode": "outGroupInputMode",
        "OutPort": "outPort",
        "OutPortInputMode": "outPortInputMode",
        "TableId": "tableId",
        "TableIdInputMode": "tableIdInputMode",
    }
    _SDM_ENUM_MAP = {
        "outGroupInputMode": ["allGroups", "anyGroup", "outGroupCustom"],
        "outPortInputMode": [
            "ofppInPort",
            "ofppNormal",
            "ofppFlood",
            "ofppAll",
            "ofppController",
            "ofppLocal",
            "ofppAny",
            "outPortCustom",
        ],
        "tableIdInputMode": ["allTables", "emergency", "custom"],
    }

    def __init__(self, parent, list_op=False):
        super(SwitchFlow131TriggerAttributes, self).__init__(parent, list_op)

    @property
    def OutGroup(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the out group value. It requires matching entries to include this as an output group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutGroup"])

    @OutGroup.setter
    def OutGroup(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutGroup"], value)

    @property
    def OutGroupInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allGroups | anyGroup | outGroupCustom): This describes the input mode of the out group value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutGroupInputMode"])

    @OutGroupInputMode.setter
    def OutGroupInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutGroupInputMode"], value)

    @property
    def OutPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the out port value. It requires matching entries to include this as an output port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutPort"])

    @OutPort.setter
    def OutPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutPort"], value)

    @property
    def OutPortInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom): This describes the input mode of the out port value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutPortInputMode"])

    @OutPortInputMode.setter
    def OutPortInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutPortInputMode"], value)

    @property
    def TableId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This describes the table identifier. It indicates the next table in the packet processing pipeline.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableId"])

    @TableId.setter
    def TableId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableId"], value)

    @property
    def TableIdInputMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allTables | emergency | custom): This describes the input mode of the Table Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableIdInputMode"])

    @TableIdInputMode.setter
    def TableIdInputMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableIdInputMode"], value)

    def update(
        self,
        OutGroup=None,
        OutGroupInputMode=None,
        OutPort=None,
        OutPortInputMode=None,
        TableId=None,
        TableIdInputMode=None,
    ):
        # type: (int, str, int, str, int, str) -> SwitchFlow131TriggerAttributes
        """Updates switchFlow131TriggerAttributes resource on the server.

        Args
        ----
        - OutGroup (number): This describes the out group value. It requires matching entries to include this as an output group.
        - OutGroupInputMode (str(allGroups | anyGroup | outGroupCustom)): This describes the input mode of the out group value.
        - OutPort (number): This describes the out port value. It requires matching entries to include this as an output port.
        - OutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom)): This describes the input mode of the out port value.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | custom)): This describes the input mode of the Table Identifier.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        OutGroup=None,
        OutGroupInputMode=None,
        OutPort=None,
        OutPortInputMode=None,
        TableId=None,
        TableIdInputMode=None,
    ):
        # type: (int, str, int, str, int, str) -> SwitchFlow131TriggerAttributes
        """Finds and retrieves switchFlow131TriggerAttributes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchFlow131TriggerAttributes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchFlow131TriggerAttributes resources from the server.

        Args
        ----
        - OutGroup (number): This describes the out group value. It requires matching entries to include this as an output group.
        - OutGroupInputMode (str(allGroups | anyGroup | outGroupCustom)): This describes the input mode of the out group value.
        - OutPort (number): This describes the out port value. It requires matching entries to include this as an output port.
        - OutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom)): This describes the input mode of the out port value.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | custom)): This describes the input mode of the Table Identifier.

        Returns
        -------
        - self: This instance with matching switchFlow131TriggerAttributes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchFlow131TriggerAttributes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchFlow131TriggerAttributes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
