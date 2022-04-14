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


class NestedCounter(Base):
    """This object provides different options for UDF in Nested Counter Type.
    The NestedCounter class encapsulates a list of nestedCounter resources that are managed by the system.
    A list of resources can be retrieved from the server using the NestedCounter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "nestedCounter"
    _SDM_ATT_MAP = {
        "AvailableWidths": "availableWidths",
        "BitOffset": "bitOffset",
        "InnerLoopIncrementBy": "innerLoopIncrementBy",
        "InnerLoopLoopCount": "innerLoopLoopCount",
        "InnerLoopRepeatValue": "innerLoopRepeatValue",
        "OuterLoopIncrementBy": "outerLoopIncrementBy",
        "OuterLoopLoopCount": "outerLoopLoopCount",
        "StartValue": "startValue",
        "Width": "width",
    }
    _SDM_ENUM_MAP = {
        "width": [
            "1",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "2",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "3",
            "30",
            "31",
            "32",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(NestedCounter, self).__init__(parent, list_op)

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
    def BitOffset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitOffset"])

    @BitOffset.setter
    def BitOffset(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitOffset"], value)

    @property
    def InnerLoopIncrementBy(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Step Value by which the Inner Loop will be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerLoopIncrementBy"])

    @InnerLoopIncrementBy.setter
    def InnerLoopIncrementBy(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerLoopIncrementBy"], value)

    @property
    def InnerLoopLoopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the no. of times the inner loop will occur.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerLoopLoopCount"])

    @InnerLoopLoopCount.setter
    def InnerLoopLoopCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerLoopLoopCount"], value)

    @property
    def InnerLoopRepeatValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of times the UDF Value will be repeated in inner loop.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InnerLoopRepeatValue"])

    @InnerLoopRepeatValue.setter
    def InnerLoopRepeatValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InnerLoopRepeatValue"], value)

    @property
    def OuterLoopIncrementBy(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Step Value by which the outer loop will be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OuterLoopIncrementBy"])

    @OuterLoopIncrementBy.setter
    def OuterLoopIncrementBy(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OuterLoopIncrementBy"], value)

    @property
    def OuterLoopLoopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of times the outer loop will occur.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OuterLoopLoopCount"])

    @OuterLoopLoopCount.setter
    def OuterLoopLoopCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OuterLoopLoopCount"], value)

    @property
    def StartValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Start Value of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartValue"])

    @StartValue.setter
    def StartValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartValue"], value)

    @property
    def Width(self):
        # type: () -> str
        """
        Returns
        -------
        - str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9): Specifies the width of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Width"])

    @Width.setter
    def Width(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Width"], value)

    def update(
        self,
        BitOffset=None,
        InnerLoopIncrementBy=None,
        InnerLoopLoopCount=None,
        InnerLoopRepeatValue=None,
        OuterLoopIncrementBy=None,
        OuterLoopLoopCount=None,
        StartValue=None,
        Width=None,
    ):
        # type: (int, int, int, int, int, int, int, str) -> NestedCounter
        """Updates nestedCounter resource on the server.

        Args
        ----
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
        - InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
        - InnerLoopRepeatValue (number): Specifies the number of times the UDF Value will be repeated in inner loop.
        - OuterLoopIncrementBy (number): Specifies the Step Value by which the outer loop will be incremented.
        - OuterLoopLoopCount (number): Specifies the number of times the outer loop will occur.
        - StartValue (number): Specifies the Start Value of the UDF.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BitOffset=None,
        InnerLoopIncrementBy=None,
        InnerLoopLoopCount=None,
        InnerLoopRepeatValue=None,
        OuterLoopIncrementBy=None,
        OuterLoopLoopCount=None,
        StartValue=None,
        Width=None,
    ):
        # type: (int, int, int, int, int, int, int, str) -> NestedCounter
        """Adds a new nestedCounter resource on the json, only valid with batch add utility

        Args
        ----
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
        - InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
        - InnerLoopRepeatValue (number): Specifies the number of times the UDF Value will be repeated in inner loop.
        - OuterLoopIncrementBy (number): Specifies the Step Value by which the outer loop will be incremented.
        - OuterLoopLoopCount (number): Specifies the number of times the outer loop will occur.
        - StartValue (number): Specifies the Start Value of the UDF.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with all currently retrieved nestedCounter resources using find and the newly added nestedCounter resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableWidths=None,
        BitOffset=None,
        InnerLoopIncrementBy=None,
        InnerLoopLoopCount=None,
        InnerLoopRepeatValue=None,
        OuterLoopIncrementBy=None,
        OuterLoopLoopCount=None,
        StartValue=None,
        Width=None,
    ):
        # type: (List[str], int, int, int, int, int, int, int, str) -> NestedCounter
        """Finds and retrieves nestedCounter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve nestedCounter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all nestedCounter resources from the server.

        Args
        ----
        - AvailableWidths (list(str)): Species all the possible widths available for a UDF in particular Type.
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
        - InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
        - InnerLoopRepeatValue (number): Specifies the number of times the UDF Value will be repeated in inner loop.
        - OuterLoopIncrementBy (number): Specifies the Step Value by which the outer loop will be incremented.
        - OuterLoopLoopCount (number): Specifies the number of times the outer loop will occur.
        - StartValue (number): Specifies the Start Value of the UDF.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with matching nestedCounter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of nestedCounter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the nestedCounter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
