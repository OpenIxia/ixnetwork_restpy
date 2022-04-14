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


class ValueList(Base):
    """This object specifies the value list properties.
    The ValueList class encapsulates a list of valueList resources that are managed by the system.
    A list of resources can be retrieved from the server using the ValueList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "valueList"
    _SDM_ATT_MAP = {
        "AvailableWidths": "availableWidths",
        "StartValueList": "startValueList",
        "Width": "width",
    }
    _SDM_ENUM_MAP = {
        "width": ["16", "24", "32", "8"],
    }

    def __init__(self, parent, list_op=False):
        super(ValueList, self).__init__(parent, list_op)

    @property
    def AvailableWidths(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Species all the possible widths available for a UDF in particular Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableWidths"])

    @property
    def StartValueList(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Specifies the starting value for a particular UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartValueList"])

    @StartValueList.setter
    def StartValueList(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartValueList"], value)

    @property
    def Width(self):
        # type: () -> str
        """
        Returns
        -------
        - str(16 | 24 | 32 | 8): Specifies the width of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Width"])

    @Width.setter
    def Width(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Width"], value)

    def update(self, StartValueList=None, Width=None):
        # type: (List[int], str) -> ValueList
        """Updates valueList resource on the server.

        Args
        ----
        - StartValueList (list(number)): Specifies the starting value for a particular UDF.
        - Width (str(16 | 24 | 32 | 8)): Specifies the width of the UDF.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, StartValueList=None, Width=None):
        # type: (List[int], str) -> ValueList
        """Adds a new valueList resource on the json, only valid with batch add utility

        Args
        ----
        - StartValueList (list(number)): Specifies the starting value for a particular UDF.
        - Width (str(16 | 24 | 32 | 8)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with all currently retrieved valueList resources using find and the newly added valueList resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableWidths=None, StartValueList=None, Width=None):
        # type: (List[str], List[int], str) -> ValueList
        """Finds and retrieves valueList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve valueList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all valueList resources from the server.

        Args
        ----
        - AvailableWidths (list(str)): Species all the possible widths available for a UDF in particular Type.
        - StartValueList (list(number)): Specifies the starting value for a particular UDF.
        - Width (str(16 | 24 | 32 | 8)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with matching valueList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of valueList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the valueList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
