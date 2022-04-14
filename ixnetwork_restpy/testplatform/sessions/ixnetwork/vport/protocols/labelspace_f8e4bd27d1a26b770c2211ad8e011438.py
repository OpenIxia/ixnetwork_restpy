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


class LabelSpace(Base):
    """This object configures the labels for the route range.
    The LabelSpace class encapsulates a required labelSpace resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "labelSpace"
    _SDM_ATT_MAP = {
        "End": "end",
        "LabelId": "labelId",
        "Mode": "mode",
        "Start": "start",
        "Step": "step",
    }
    _SDM_ENUM_MAP = {
        "mode": ["fixedLabel", "incrementLabel"],
    }

    def __init__(self, parent, list_op=False):
        super(LabelSpace, self).__init__(parent, list_op)

    @property
    def End(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The last label value available in the label space (range).
        """
        return self._get_attribute(self._SDM_ATT_MAP["End"])

    @End.setter
    def End(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["End"], value)

    @property
    def LabelId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier for the label space.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LabelId"])

    @LabelId.setter
    def LabelId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LabelId"], value)

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixedLabel | incrementLabel): Sets the Label mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

    @property
    def Start(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first label value available in the label space (range). The default is 16.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Start"])

    @Start.setter
    def Start(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Start"], value)

    @property
    def Step(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value to add for creating each additional label value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Step"])

    @Step.setter
    def Step(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Step"], value)

    def update(self, End=None, LabelId=None, Mode=None, Start=None, Step=None):
        # type: (int, int, str, int, int) -> LabelSpace
        """Updates labelSpace resource on the server.

        Args
        ----
        - End (number): The last label value available in the label space (range).
        - LabelId (number): The identifier for the label space.
        - Mode (str(fixedLabel | incrementLabel)): Sets the Label mode.
        - Start (number): The first label value available in the label space (range). The default is 16.
        - Step (number): The value to add for creating each additional label value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, End=None, LabelId=None, Mode=None, Start=None, Step=None):
        # type: (int, int, str, int, int) -> LabelSpace
        """Finds and retrieves labelSpace resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve labelSpace resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all labelSpace resources from the server.

        Args
        ----
        - End (number): The last label value available in the label space (range).
        - LabelId (number): The identifier for the label space.
        - Mode (str(fixedLabel | incrementLabel)): Sets the Label mode.
        - Start (number): The first label value available in the label space (range). The default is 16.
        - Step (number): The value to add for creating each additional label value.

        Returns
        -------
        - self: This instance with matching labelSpace resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of labelSpace data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the labelSpace resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
