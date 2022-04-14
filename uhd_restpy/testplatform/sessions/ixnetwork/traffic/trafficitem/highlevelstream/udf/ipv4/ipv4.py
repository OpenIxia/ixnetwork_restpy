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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Ipv4(Base):
    """This object provides different options for UDF in IPv4 Type.
    The Ipv4 class encapsulates a list of ipv4 resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4'
    _SDM_ATT_MAP = {
        'AvailableWidths': 'availableWidths',
        'BitmaskCount': 'bitmaskCount',
        'InnerLoopIncrementBy': 'innerLoopIncrementBy',
        'InnerLoopLoopCount': 'innerLoopLoopCount',
        'OuterLoopLoopCount': 'outerLoopLoopCount',
        'SkipValues': 'skipValues',
        'StartValue': 'startValue',
        'Width': 'width',
    }
    _SDM_ENUM_MAP = {
        'width': ['32'],
    }

    def __init__(self, parent, list_op=False):
        super(Ipv4, self).__init__(parent, list_op)

    @property
    def AvailableWidths(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Species all the possible widths available for a UDF in particular Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableWidths'])

    @property
    def BitmaskCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of bits to be masked to any integer value between 2 to 32.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BitmaskCount'])
    @BitmaskCount.setter
    def BitmaskCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BitmaskCount'], value)

    @property
    def InnerLoopIncrementBy(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Step Value by which the Inner Loop will be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InnerLoopIncrementBy'])
    @InnerLoopIncrementBy.setter
    def InnerLoopIncrementBy(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InnerLoopIncrementBy'], value)

    @property
    def InnerLoopLoopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the no. of times the inner loop will occur.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InnerLoopLoopCount'])
    @InnerLoopLoopCount.setter
    def InnerLoopLoopCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InnerLoopLoopCount'], value)

    @property
    def OuterLoopLoopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the no. of times the outer loop will occur.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OuterLoopLoopCount'])
    @OuterLoopLoopCount.setter
    def OuterLoopLoopCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['OuterLoopLoopCount'], value)

    @property
    def SkipValues(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Skip Values option is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipValues'])
    @SkipValues.setter
    def SkipValues(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SkipValues'], value)

    @property
    def StartValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the start value of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartValue'])
    @StartValue.setter
    def StartValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartValue'], value)

    @property
    def Width(self):
        # type: () -> str
        """
        Returns
        -------
        - str(32): Specifies the width of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Width'])
    @Width.setter
    def Width(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Width'], value)

    def update(self, BitmaskCount=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, OuterLoopLoopCount=None, SkipValues=None, StartValue=None, Width=None):
        # type: (int, int, int, int, bool, int, str) -> Ipv4
        """Updates ipv4 resource on the server.

        Args
        ----
        - BitmaskCount (number): Specifies the number of bits to be masked to any integer value between 2 to 32.
        - InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
        - InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
        - OuterLoopLoopCount (number): Specifies the no. of times the outer loop will occur.
        - SkipValues (bool): If true, Skip Values option is enabled.
        - StartValue (number): Specifies the start value of the UDF.
        - Width (str(32)): Specifies the width of the UDF.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BitmaskCount=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, OuterLoopLoopCount=None, SkipValues=None, StartValue=None, Width=None):
        # type: (int, int, int, int, bool, int, str) -> Ipv4
        """Adds a new ipv4 resource on the json, only valid with batch add utility

        Args
        ----
        - BitmaskCount (number): Specifies the number of bits to be masked to any integer value between 2 to 32.
        - InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
        - InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
        - OuterLoopLoopCount (number): Specifies the no. of times the outer loop will occur.
        - SkipValues (bool): If true, Skip Values option is enabled.
        - StartValue (number): Specifies the start value of the UDF.
        - Width (str(32)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with all currently retrieved ipv4 resources using find and the newly added ipv4 resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableWidths=None, BitmaskCount=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, OuterLoopLoopCount=None, SkipValues=None, StartValue=None, Width=None):
        # type: (List[str], int, int, int, int, bool, int, str) -> Ipv4
        """Finds and retrieves ipv4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4 resources from the server.

        Args
        ----
        - AvailableWidths (list(str)): Species all the possible widths available for a UDF in particular Type.
        - BitmaskCount (number): Specifies the number of bits to be masked to any integer value between 2 to 32.
        - InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
        - InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
        - OuterLoopLoopCount (number): Specifies the no. of times the outer loop will occur.
        - SkipValues (bool): If true, Skip Values option is enabled.
        - StartValue (number): Specifies the start value of the UDF.
        - Width (str(32)): Specifies the width of the UDF.

        Returns
        -------
        - self: This instance with matching ipv4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
