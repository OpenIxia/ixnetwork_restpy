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


class NetTopologyGrid(Base):
    """grid topology
    The NetTopologyGrid class encapsulates a list of netTopologyGrid resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetTopologyGrid.find() method.
    The list can be managed by using the NetTopologyGrid.add() and NetTopologyGrid.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'netTopologyGrid'
    _SDM_ATT_MAP = {
        'Columns': 'columns',
        'IncludeEntryPoint': 'includeEntryPoint',
        'LinkMultiplier': 'linkMultiplier',
        'Rows': 'rows',
    }

    def __init__(self, parent):
        super(NetTopologyGrid, self).__init__(parent)

    @property
    def Columns(self):
        """
        Returns
        -------
        - number: number of columns
        """
        return self._get_attribute(self._SDM_ATT_MAP['Columns'])
    @Columns.setter
    def Columns(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Columns'], value)

    @property
    def IncludeEntryPoint(self):
        """
        Returns
        -------
        - bool: if true, entry node belongs to ring topology, otherwise it is outside of ring
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeEntryPoint'])
    @IncludeEntryPoint.setter
    def IncludeEntryPoint(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeEntryPoint'], value)

    @property
    def LinkMultiplier(self):
        """
        Returns
        -------
        - number: number of links between two nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMultiplier'])
    @LinkMultiplier.setter
    def LinkMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMultiplier'], value)

    @property
    def Rows(self):
        """
        Returns
        -------
        - number: number of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rows'])
    @Rows.setter
    def Rows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rows'], value)

    def update(self, Columns=None, IncludeEntryPoint=None, LinkMultiplier=None, Rows=None):
        """Updates netTopologyGrid resource on the server.

        Args
        ----
        - Columns (number): number of columns
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Rows (number): number of rows

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Columns=None, IncludeEntryPoint=None, LinkMultiplier=None, Rows=None):
        """Adds a new netTopologyGrid resource on the server and adds it to the container.

        Args
        ----
        - Columns (number): number of columns
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Rows (number): number of rows

        Returns
        -------
        - self: This instance with all currently retrieved netTopologyGrid resources using find and the newly added netTopologyGrid resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netTopologyGrid resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Columns=None, IncludeEntryPoint=None, LinkMultiplier=None, Rows=None):
        """Finds and retrieves netTopologyGrid resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netTopologyGrid resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netTopologyGrid resources from the server.

        Args
        ----
        - Columns (number): number of columns
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Rows (number): number of rows

        Returns
        -------
        - self: This instance with matching netTopologyGrid resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netTopologyGrid data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netTopologyGrid resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
