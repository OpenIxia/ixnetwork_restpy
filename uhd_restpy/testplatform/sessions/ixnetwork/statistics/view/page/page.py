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


class Page(Base):
    """DEPRECATED The root page for statistics view.
    The Page class encapsulates a required page resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'page'
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
        'IsReadyTimeout': 'isReadyTimeout',
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
        super(Page, self).__init__(parent, list_op)

    @property
    def Egress(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egress.egress.Egress): An instance of the Egress class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egress.egress import Egress
        if len(self._object_properties) > 0:
            if self._properties.get('Egress', None) is not None:
                return self._properties.get('Egress')
        return Egress(self)

    @property
    def EgressRxCondition(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egressrxcondition.egressrxcondition.EgressRxCondition): An instance of the EgressRxCondition class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egressrxcondition.egressrxcondition import EgressRxCondition
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
        - bool: If true, statistics will be displayed in multiple pages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowPaging'])

    @property
    def ColumnCaptions(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The statistics column caption.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCaptions'])

    @property
    def ColumnCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Displays the particular column number in the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCount'])

    @property
    def CurrentPage(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The current page number being displayed.
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
        - str(conditional | paged): Emulates conditional or paged egress tracking view based on selected mode.
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
        - number: The current egress page size across all ingress rows. Default = 3
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
        - bool: Is a flag used to fetch the status of view (returns true if the views was blocked by Guard Rail, false otherwise)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsBlocked'])

    @property
    def IsReady(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the counter is ready to record the statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReady'])

    @property
    def IsReadyTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum time (in seconds) for the -isReady attribute to wait before it returns false in case the page has no data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReadyTimeout'])
    @IsReadyTimeout.setter
    def IsReadyTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsReadyTimeout'], value)

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
        - number: The number of statistics per page.
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
        - number: Displays the particular row number in the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowCount'])

    @property
    def RowValues(self):
        """DEPRECATED 
        Returns
        -------
        - dict(arg1:list[list[list[str]]]): All statistics values in a row.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowValues'])

    @property
    def Timestamp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Describes the date and time of the event.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Timestamp'])

    @property
    def TotalPages(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The total number of statistics pages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalPages'])

    @property
    def TotalRows(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalRows'])

    def update(self, CurrentPage=None, EgressMode=None, EgressOption=None, EgressPageSize=None, IsReadyTimeout=None, PageSize=None):
        # type: (int, str, str, int, int, int) -> Page
        """Updates page resource on the server.

        Args
        ----
        - CurrentPage (number): The current page number being displayed.
        - EgressMode (str(conditional | paged)): Emulates conditional or paged egress tracking view based on selected mode.
        - EgressOption (str(rowsWithNoPackets | rowsWithPackets | showAll)): 
        - EgressPageSize (number): The current egress page size across all ingress rows. Default = 3
        - IsReadyTimeout (number): The maximum time (in seconds) for the -isReady attribute to wait before it returns false in case the page has no data.
        - PageSize (number): The number of statistics per page.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AllowPaging=None, ColumnCaptions=None, ColumnCount=None, CurrentPage=None, EgressMode=None, EgressOption=None, EgressPageSize=None, IsBlocked=None, IsReady=None, IsReadyTimeout=None, LastPageSize=None, PageSize=None, PageValues=None, RowCount=None, RowValues=None, Timestamp=None, TotalPages=None, TotalRows=None):
        """Finds and retrieves page resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve page resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all page resources from the server.

        Args
        ----
        - AllowPaging (bool): If true, statistics will be displayed in multiple pages.
        - ColumnCaptions (list(str)): The statistics column caption.
        - ColumnCount (number): Displays the particular column number in the view.
        - CurrentPage (number): The current page number being displayed.
        - EgressMode (str(conditional | paged)): Emulates conditional or paged egress tracking view based on selected mode.
        - EgressOption (str(rowsWithNoPackets | rowsWithPackets | showAll)): 
        - EgressPageSize (number): The current egress page size across all ingress rows. Default = 3
        - IsBlocked (bool): Is a flag used to fetch the status of view (returns true if the views was blocked by Guard Rail, false otherwise)
        - IsReady (bool): If true, the counter is ready to record the statistics.
        - IsReadyTimeout (number): The maximum time (in seconds) for the -isReady attribute to wait before it returns false in case the page has no data.
        - LastPageSize (number): 
        - PageSize (number): The number of statistics per page.
        - PageValues (list(list[list[str]])): Returns the values in the current page. The ingress row is grouped with its corresponding egress rows
        - RowCount (number): Displays the particular row number in the view.
        - RowValues (dict(arg1:list[list[list[str]]])): All statistics values in a row.
        - Timestamp (number): Describes the date and time of the event.
        - TotalPages (number): The total number of statistics pages.
        - TotalRows (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching page resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of page data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the page resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
