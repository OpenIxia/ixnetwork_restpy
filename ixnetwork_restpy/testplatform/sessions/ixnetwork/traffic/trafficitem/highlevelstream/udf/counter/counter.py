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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files
from typing import List, Any, Union


class Counter(Base):
    """This object provides different options for UDF in Counter Type.
    The Counter class encapsulates a list of counter resources that are managed by the system.
    A list of resources can be retrieved from the server using the Counter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'counter'
    _SDM_ATT_MAP = {
        'AvailableWidths': 'availableWidths',
        'BitOffset': 'bitOffset',
        'Count': 'count',
        'Direction': 'direction',
        'StartValue': 'startValue',
        'StepValue': 'stepValue',
        'Width': 'width',
    }
    _SDM_ENUM_MAP = {
        'direction': ['decrement', 'increment'],
        'width': ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '4', '5', '6', '7', '8', '9'],
    }

    def __init__(self, parent, list_op=False):
        super(Counter, self).__init__(parent, list_op)

    @property
    def AvailableWidths(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Contains all the possible widths available for a UDF in particular Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableWidths'])

    @property
    def BitOffset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BitOffset'])
    @BitOffset.setter
    def BitOffset(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BitOffset'], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the repeat count for the UDF. After the elapse of this count, UDF will again start from the Start Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Direction(self):
        # type: () -> str
        """
        Returns
        -------
        - str(decrement | increment): Specifies if the UDF value will be incremented or decremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Direction'])
    @Direction.setter
    def Direction(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Direction'], value)

    @property
    def StartValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Start Value of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartValue'])
    @StartValue.setter
    def StartValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartValue'], value)

    @property
    def StepValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Step Value by which the UDF value will be incremented or decremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepValue'])
    @StepValue.setter
    def StepValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepValue'], value)

    @property
    def Width(self):
        # type: () -> str
        """
        Returns
        -------
        - str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9): Specifies the width of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Width'])
    @Width.setter
    def Width(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Width'], value)

    def update(self, BitOffset=None, Count=None, Direction=None, StartValue=None, StepValue=None, Width=None):
        # type: (int, int, str, int, int, str) -> Counter
        """Updates counter resource on the server.

        Args
        ----
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - Count (number): Specifies the repeat count for the UDF. After the elapse of this count, UDF will again start from the Start Value.
        - Direction (str(decrement | increment)): Specifies if the UDF value will be incremented or decremented.
        - StartValue (number): Specifies the Start Value of the UDF.
        - StepValue (number): Specifies the Step Value by which the UDF value will be incremented or decremented.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BitOffset=None, Count=None, Direction=None, StartValue=None, StepValue=None, Width=None):
        # type: (int, int, str, int, int, str) -> Counter
        """Adds a new counter resource on the json, only valid with config assistant

        Args
        ----
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - Count (number): Specifies the repeat count for the UDF. After the elapse of this count, UDF will again start from the Start Value.
        - Direction (str(decrement | increment)): Specifies if the UDF value will be incremented or decremented.
        - StartValue (number): Specifies the Start Value of the UDF.
        - StepValue (number): Specifies the Step Value by which the UDF value will be incremented or decremented.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with all currently retrieved counter resources using find and the newly added counter resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableWidths=None, BitOffset=None, Count=None, Direction=None, StartValue=None, StepValue=None, Width=None):
        # type: (List[str], int, int, str, int, int, str) -> Counter
        """Finds and retrieves counter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve counter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all counter resources from the server.

        Args
        ----
        - AvailableWidths (list(str)): Contains all the possible widths available for a UDF in particular Type.
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - Count (number): Specifies the repeat count for the UDF. After the elapse of this count, UDF will again start from the Start Value.
        - Direction (str(decrement | increment)): Specifies if the UDF value will be incremented or decremented.
        - StartValue (number): Specifies the Start Value of the UDF.
        - StepValue (number): Specifies the Step Value by which the UDF value will be incremented or decremented.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with matching counter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of counter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the counter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
