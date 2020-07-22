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
        'EgressPageSize': 'egressPageSize',
        'IsBlocked': 'isBlocked',
        'IsReady': 'isReady',
        'IsReadyTimeout': 'isReadyTimeout',
        'PageSize': 'pageSize',
        'PageValues': 'pageValues',
        'RowCount': 'rowCount',
        'RowValues': 'rowValues',
        'Timestamp': 'timestamp',
        'TotalPages': 'totalPages',
        'TotalRows': 'totalRows',
    }

    def __init__(self, parent):
        super(Page, self).__init__(parent)

    @property
    def Egress(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egress.egress.Egress): An instance of the Egress class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egress.egress import Egress
        return Egress(self)

    @property
    def EgressRxCondition(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egressrxcondition.egressrxcondition.EgressRxCondition): An instance of the EgressRxCondition class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egressrxcondition.egressrxcondition import EgressRxCondition
        return EgressRxCondition(self)._select()

    @property
    def AllowPaging(self):
        """
        Returns
        -------
        - bool: If true, statistics will be displayed in multiple pages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowPaging'])

    @property
    def ColumnCaptions(self):
        """
        Returns
        -------
        - list(str): The statistics column caption.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCaptions'])

    @property
    def ColumnCount(self):
        """
        Returns
        -------
        - number: Displays the particular column number in the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCount'])

    @property
    def CurrentPage(self):
        """
        Returns
        -------
        - number: The current page number being displayed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentPage'])
    @CurrentPage.setter
    def CurrentPage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CurrentPage'], value)

    @property
    def EgressMode(self):
        """
        Returns
        -------
        - str(conditional | paged): Emulates conditional or paged egress tracking view based on selected mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressMode'])
    @EgressMode.setter
    def EgressMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EgressMode'], value)

    @property
    def EgressPageSize(self):
        """
        Returns
        -------
        - number: The current egress page size across all ingress rows. Default = 3
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressPageSize'])
    @EgressPageSize.setter
    def EgressPageSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EgressPageSize'], value)

    @property
    def IsBlocked(self):
        """
        Returns
        -------
        - bool: Is a flag used to fetch the status of view (returns true if the views was blocked by Guard Rail, false otherwise)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsBlocked'])

    @property
    def IsReady(self):
        """
        Returns
        -------
        - bool: If true, the counter is ready to record the statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReady'])

    @property
    def IsReadyTimeout(self):
        """
        Returns
        -------
        - number: The maximum time (in seconds) for the -isReady attribute to wait before it returns false in case the page has no data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReadyTimeout'])
    @IsReadyTimeout.setter
    def IsReadyTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsReadyTimeout'], value)

    @property
    def PageSize(self):
        """
        Returns
        -------
        - number: The number of statistics per page.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PageSize'])
    @PageSize.setter
    def PageSize(self, value):
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
        """
        Returns
        -------
        - number: Describes the date and time of the event.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Timestamp'])

    @property
    def TotalPages(self):
        """
        Returns
        -------
        - number: The total number of statistics pages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalPages'])

    @property
    def TotalRows(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalRows'])

    def update(self, CurrentPage=None, EgressMode=None, EgressPageSize=None, IsReadyTimeout=None, PageSize=None):
        """Updates page resource on the server.

        Args
        ----
        - CurrentPage (number): The current page number being displayed.
        - EgressMode (str(conditional | paged)): Emulates conditional or paged egress tracking view based on selected mode.
        - EgressPageSize (number): The current egress page size across all ingress rows. Default = 3
        - IsReadyTimeout (number): The maximum time (in seconds) for the -isReady attribute to wait before it returns false in case the page has no data.
        - PageSize (number): The number of statistics per page.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
