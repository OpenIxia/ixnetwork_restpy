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


class Column(Base):
    """This object specifies column properties of an UDF table.
    The Column class encapsulates a list of column resources that are managed by the user.
    A list of resources can be retrieved from the server using the Column.find() method.
    The list can be managed by using the Column.add() and Column.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'column'
    _SDM_ATT_MAP = {
        'Format': 'format',
        'Offset': 'offset',
        'Size': 'size',
        'Values': 'values',
    }

    def __init__(self, parent):
        super(Column, self).__init__(parent)

    @property
    def Format(self):
        """
        Returns
        -------
        - str(ascii | binary | custom | decimal | hex | ipv4 | ipv6 | mac): The format of the Table UDF list (column).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Format'])
    @Format.setter
    def Format(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Format'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: The offset value, in bytes, of the Table UDF list (column).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    @property
    def Size(self):
        """
        Returns
        -------
        - number: The size, in bytes, of the Table UDF list (column).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Size'])
    @Size.setter
    def Size(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Size'], value)

    @property
    def Values(self):
        """
        Returns
        -------
        - list(str): The value of the table UDF column.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])
    @Values.setter
    def Values(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Values'], value)

    def update(self, Format=None, Offset=None, Size=None, Values=None):
        """Updates column resource on the server.

        Args
        ----
        - Format (str(ascii | binary | custom | decimal | hex | ipv4 | ipv6 | mac)): The format of the Table UDF list (column).
        - Offset (number): The offset value, in bytes, of the Table UDF list (column).
        - Size (number): The size, in bytes, of the Table UDF list (column).
        - Values (list(str)): The value of the table UDF column.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Format=None, Offset=None, Size=None, Values=None):
        """Adds a new column resource on the server and adds it to the container.

        Args
        ----
        - Format (str(ascii | binary | custom | decimal | hex | ipv4 | ipv6 | mac)): The format of the Table UDF list (column).
        - Offset (number): The offset value, in bytes, of the Table UDF list (column).
        - Size (number): The size, in bytes, of the Table UDF list (column).
        - Values (list(str)): The value of the table UDF column.

        Returns
        -------
        - self: This instance with all currently retrieved column resources using find and the newly added column resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained column resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Format=None, Offset=None, Size=None, Values=None):
        """Finds and retrieves column resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve column resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all column resources from the server.

        Args
        ----
        - Format (str(ascii | binary | custom | decimal | hex | ipv4 | ipv6 | mac)): The format of the Table UDF list (column).
        - Offset (number): The offset value, in bytes, of the Table UDF list (column).
        - Size (number): The size, in bytes, of the Table UDF list (column).
        - Values (list(str)): The value of the table UDF column.

        Returns
        -------
        - self: This instance with matching column resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of column data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the column resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
