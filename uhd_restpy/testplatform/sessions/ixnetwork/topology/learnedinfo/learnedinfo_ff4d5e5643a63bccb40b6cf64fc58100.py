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
from typing import List, Any, Union


class LearnedInfo(Base):
    """The main learned information node that contains tables of learned information.
    The LearnedInfo class encapsulates a list of learnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfo'
    _SDM_ATT_MAP = {
        'Id__': '__id__',
        'Columns': 'columns',
        'State': 'state',
        'Type': 'type',
        'Values': 'values',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(LearnedInfo, self).__init__(parent, list_op)

    @property
    def Col(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.col_82c9f692cc4dfbaf274869de8a335e5e.Col): An instance of the Col class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.col_82c9f692cc4dfbaf274869de8a335e5e import Col
        if self._properties.get('Col', None) is not None:
            return self._properties.get('Col')
        else:
            return Col(self)

    @property
    def Table(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.table_5866003f22dc964c958a5bc4c3040ef4.Table): An instance of the Table class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.table_5866003f22dc964c958a5bc4c3040ef4 import Table
        if self._properties.get('Table', None) is not None:
            return self._properties.get('Table')
        else:
            return Table(self)

    @property
    def Id__(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): A unique id for the learned information table
        """
        return self._get_attribute(self._SDM_ATT_MAP['Id__'])

    @property
    def Columns(self):
        # type: () -> List[str]
        """DEPRECATED 
        Returns
        -------
        - list(str): The list of columns in the learned information table
        """
        return self._get_attribute(self._SDM_ATT_MAP['Columns'])

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The state of the learned information query
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def Type(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: The type of learned information
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])

    @property
    def Values(self):
        """DEPRECATED 
        Returns
        -------
        - list(list[str]): A list of rows of learned information values
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])

    def add(self):
        """Adds a new learnedInfo resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved learnedInfo resources using find and the newly added learnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Id__=None, Columns=None, State=None, Type=None, Values=None):
        """Finds and retrieves learnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInfo resources from the server.

        Args
        ----
        - Id__ (list(str)): A unique id for the learned information table
        - Columns (list(str)): The list of columns in the learned information table
        - State (str): The state of the learned information query
        - Type (str): The type of learned information
        - Values (list(list[str])): A list of rows of learned information values

        Returns
        -------
        - self: This instance with matching learnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
