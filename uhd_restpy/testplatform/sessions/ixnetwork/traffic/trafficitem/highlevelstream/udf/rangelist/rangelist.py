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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class RangeList(Base):
    """This object provides different options for UDF in Range list Type.
    The RangeList class encapsulates a list of rangeList resources that are managed by the system.
    A list of resources can be retrieved from the server using the RangeList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'rangeList'
    _SDM_ATT_MAP = {
        'AvailableWidths': 'availableWidths',
        'BitOffset': 'bitOffset',
        'StartValueCountStepList': 'startValueCountStepList',
        'Width': 'width',
    }

    def __init__(self, parent):
        super(RangeList, self).__init__(parent)

    @property
    def AvailableWidths(self):
        """
        Returns
        -------
        - list(str): Species all the possible widths available for a UDF in particular Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableWidths'])

    @property
    def BitOffset(self):
        """
        Returns
        -------
        - number: Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BitOffset'])
    @BitOffset.setter
    def BitOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BitOffset'], value)

    @property
    def StartValueCountStepList(self):
        """
        Returns
        -------
        - list(number): Specifies the Start Value, Count and Step Value of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartValueCountStepList'])
    @StartValueCountStepList.setter
    def StartValueCountStepList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartValueCountStepList'], value)

    @property
    def Width(self):
        """
        Returns
        -------
        - str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9): Specifies the width of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Width'])
    @Width.setter
    def Width(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Width'], value)

    def update(self, BitOffset=None, StartValueCountStepList=None, Width=None):
        """Updates rangeList resource on the server.

        Args
        ----
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - StartValueCountStepList (list(number)): Specifies the Start Value, Count and Step Value of the UDF.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableWidths=None, BitOffset=None, StartValueCountStepList=None, Width=None):
        """Finds and retrieves rangeList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rangeList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rangeList resources from the server.

        Args
        ----
        - AvailableWidths (list(str)): Species all the possible widths available for a UDF in particular Type.
        - BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
        - StartValueCountStepList (list(number)): Specifies the Start Value, Count and Step Value of the UDF.
        - Width (str(1 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 2 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 3 | 30 | 31 | 32 | 4 | 5 | 6 | 7 | 8 | 9)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with matching rangeList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rangeList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rangeList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
