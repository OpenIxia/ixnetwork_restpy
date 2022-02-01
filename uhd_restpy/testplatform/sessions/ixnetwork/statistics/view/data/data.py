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


class Data(Base):
    """
    The Data class encapsulates a required data resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'data'
    _SDM_ATT_MAP = {
        'AllowPaging': 'allowPaging',
        'ColumnCaptions': 'columnCaptions',
        'ColumnCount': 'columnCount',
        'CurrentPage': 'currentPage',
        'EgressMode': 'egressMode',
        'EgressOption': 'egressOption',
        'EgressPageSize': 'egressPageSize',
        'IsBlocked': 'isBlocked',
        'IsReady': 'isReady',
        'LastPageSize': 'lastPageSize',
        'PageSize': 'pageSize',
        'PageValues': 'pageValues',
        'RowCount': 'rowCount',
        'RowValues': 'rowValues',
        'Timestamp': 'timestamp',
        'TotalPages': 'totalPages',
        'TotalRows': 'totalRows',
    }
    _SDM_ENUM_MAP = {
        'egressMode': ['conditional', 'paged'],
        'egressOption': ['rowsWithNoPackets', 'rowsWithPackets', 'showAll'],
    }

    def __init__(self, parent, list_op=False):
        super(Data, self).__init__(parent, list_op)

    @property
    def Egress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.data.egress.egress.Egress): An instance of the Egress class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.data.egress.egress import Egress
        if len(self._object_properties) > 0:
            if self._properties.get('Egress', None) is not None:
                return self._properties.get('Egress')
        return Egress(self)

    @property
    def EgressRxCondition(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.data.egressrxcondition.egressrxcondition.EgressRxCondition): An instance of the EgressRxCondition class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.data.egressrxcondition.egressrxcondition import EgressRxCondition
        if len(self._object_properties) > 0:
            if self._properties.get('EgressRxCondition', None) is not None:
                return self._properties.get('EgressRxCondition')
        return EgressRxCondition(self)._select()

    @property
    def AllowPaging(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowPaging'])

    @property
    def ColumnCaptions(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCaptions'])

    @property
    def ColumnCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCount'])

    @property
    def CurrentPage(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentPage'])
    @CurrentPage.setter
    def CurrentPage(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CurrentPage'], value)

    @property
    def EgressMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(conditional | paged): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressMode'])
    @EgressMode.setter
    def EgressMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EgressMode'], value)

    @property
    def EgressOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(rowsWithNoPackets | rowsWithPackets | showAll): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressOption'])
    @EgressOption.setter
    def EgressOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EgressOption'], value)

    @property
    def EgressPageSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressPageSize'])
    @EgressPageSize.setter
    def EgressPageSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EgressPageSize'], value)

    @property
    def IsBlocked(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsBlocked'])

    @property
    def IsReady(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReady'])

    @property
    def LastPageSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastPageSize'])

    @property
    def PageSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PageSize'])
    @PageSize.setter
    def PageSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PageSize'], value)

    @property
    def PageValues(self):
        """
        Returns
        -------
        - list(list[list[str]]): Returns the values in the current page. The ingress row is grouped with its corresponding egress rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['PageValues'])

    @property
    def RowCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowCount'])

    @property
    def RowValues(self):
        """DEPRECATED 
        Returns
        -------
        - dict(arg1:list[list[list[str]]]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowValues'])

    @property
    def Timestamp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Timestamp'])

    @property
    def TotalPages(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalPages'])

    @property
    def TotalRows(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalRows'])

    def update(self, CurrentPage=None, EgressMode=None, EgressOption=None, EgressPageSize=None, PageSize=None):
        # type: (int, str, str, int, int) -> Data
        """Updates data resource on the server.

        Args
        ----
        - CurrentPage (number): 
        - EgressMode (str(conditional | paged)): 
        - EgressOption (str(rowsWithNoPackets | rowsWithPackets | showAll)): 
        - EgressPageSize (number): 
        - PageSize (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AllowPaging=None, ColumnCaptions=None, ColumnCount=None, CurrentPage=None, EgressMode=None, EgressOption=None, EgressPageSize=None, IsBlocked=None, IsReady=None, LastPageSize=None, PageSize=None, PageValues=None, RowCount=None, RowValues=None, Timestamp=None, TotalPages=None, TotalRows=None):
        """Finds and retrieves data resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve data resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all data resources from the server.

        Args
        ----
        - AllowPaging (bool): 
        - ColumnCaptions (list(str)): 
        - ColumnCount (number): 
        - CurrentPage (number): 
        - EgressMode (str(conditional | paged)): 
        - EgressOption (str(rowsWithNoPackets | rowsWithPackets | showAll)): 
        - EgressPageSize (number): 
        - IsBlocked (bool): 
        - IsReady (bool): 
        - LastPageSize (number): 
        - PageSize (number): 
        - PageValues (list(list[list[str]])): Returns the values in the current page. The ingress row is grouped with its corresponding egress rows
        - RowCount (number): 
        - RowValues (dict(arg1:list[list[list[str]]])): 
        - Timestamp (number): 
        - TotalPages (number): 
        - TotalRows (number): 

        Returns
        -------
        - self: This instance with matching data resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of data data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the data resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
