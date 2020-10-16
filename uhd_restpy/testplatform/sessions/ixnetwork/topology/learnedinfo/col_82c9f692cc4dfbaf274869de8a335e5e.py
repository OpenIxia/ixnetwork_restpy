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


class Col(Base):
    """DEPRECATED A column view of learned information.
    The Col class encapsulates a list of col resources that are managed by the system.
    A list of resources can be retrieved from the server using the Col.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'col'
    _SDM_ATT_MAP = {
        'Value': 'value',
    }

    def __init__(self, parent):
        super(Col, self).__init__(parent)

    @property
    def CellTable(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.celltable_bef6632b895c626cc7174eb89a76162c.CellTable): An instance of the CellTable class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.celltable_bef6632b895c626cc7174eb89a76162c import CellTable
        return CellTable(self)

    @property
    def Row(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.row_dbafc34e8c4bf46a4ac7b647400c39d3.Row): An instance of the Row class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.row_dbafc34e8c4bf46a4ac7b647400c39d3 import Row
        return Row(self)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: A learned information value
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])

    def find(self, Value=None):
        """Finds and retrieves col resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve col resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all col resources from the server.

        Args
        ----
        - Value (str): A learned information value

        Returns
        -------
        - self: This instance with matching col resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of col data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the col resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
