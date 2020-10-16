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


class ValueList(Base):
    """This object specifies the value list properties.
    The ValueList class encapsulates a list of valueList resources that are managed by the system.
    A list of resources can be retrieved from the server using the ValueList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'valueList'
    _SDM_ATT_MAP = {
        'AvailableWidths': 'availableWidths',
        'StartValueList': 'startValueList',
        'Width': 'width',
    }

    def __init__(self, parent):
        super(ValueList, self).__init__(parent)

    @property
    def AvailableWidths(self):
        """
        Returns
        -------
        - list(str): Species all the possible widths available for a UDF in particular Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableWidths'])

    @property
    def StartValueList(self):
        """
        Returns
        -------
        - list(number): Specifies the starting value for a particular UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartValueList'])
    @StartValueList.setter
    def StartValueList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartValueList'], value)

    @property
    def Width(self):
        """
        Returns
        -------
        - str(16 | 24 | 32 | 8): Specifies the width of the UDF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Width'])
    @Width.setter
    def Width(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Width'], value)

    def update(self, StartValueList=None, Width=None):
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

    def find(self, AvailableWidths=None, StartValueList=None, Width=None):
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
