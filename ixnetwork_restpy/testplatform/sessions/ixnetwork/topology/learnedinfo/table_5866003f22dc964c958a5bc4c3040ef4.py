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


class Table(Base):
    """The node where learned information is grouped into tables or columns and rows.
    The Table class encapsulates a list of table resources that are managed by the system.
    A list of resources can be retrieved from the server using the Table.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'table'
    _SDM_ATT_MAP = {
        'Actions': 'actions',
        'Columns': 'columns',
        'RowCount': 'rowCount',
        'Type': 'type',
        'Values': 'values',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Table, self).__init__(parent, list_op)

    @property
    def Col(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.col_82c9f692cc4dfbaf274869de8a335e5e.Col): An instance of the Col class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.col_82c9f692cc4dfbaf274869de8a335e5e import Col
        if self._properties.get('Col', None) is not None:
            return self._properties.get('Col')
        else:
            return Col(self)

    @property
    def Actions(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The list of actions allowed on the learned information table
        """
        return self._get_attribute(self._SDM_ATT_MAP['Actions'])

    @property
    def Columns(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The list of columns in the learned information table
        """
        return self._get_attribute(self._SDM_ATT_MAP['Columns'])

    @property
    def RowCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of rows in the learned information table
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowCount'])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Description of the learned information type
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])

    @property
    def Values(self):
        """
        Returns
        -------
        - list(list[str]): A list of rows of learned information values
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])

    def add(self):
        """Adds a new table resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved table resources using find and the newly added table resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Actions=None, Columns=None, RowCount=None, Type=None, Values=None):
        """Finds and retrieves table resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve table resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all table resources from the server.

        Args
        ----
        - Actions (list(str)): The list of actions allowed on the learned information table
        - Columns (list(str)): The list of columns in the learned information table
        - RowCount (number): Number of rows in the learned information table
        - Type (str): Description of the learned information type
        - Values (list(list[str])): A list of rows of learned information values

        Returns
        -------
        - self: This instance with matching table resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of table data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the table resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
