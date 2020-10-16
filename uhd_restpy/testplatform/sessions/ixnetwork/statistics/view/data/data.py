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
        'EgressPageSize': 'egressPageSize',
        'IsBlocked': 'isBlocked',
        'IsReady': 'isReady',
        'PageSize': 'pageSize',
        'PageValues': 'pageValues',
        'RowCount': 'rowCount',
        'RowValues': 'rowValues',
        'Timestamp': 'timestamp',
        'TotalPages': 'totalPages',
        'TotalRows': 'totalRows',
    }

    def __init__(self, parent):
        super(Data, self).__init__(parent)

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
        return EgressRxCondition(self)._select()

    @property
    def AllowPaging(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowPaging'])

    @property
    def ColumnCaptions(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCaptions'])

    @property
    def ColumnCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ColumnCount'])

    @property
    def CurrentPage(self):
        """
        Returns
        -------
        - number: 
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
        - str(conditional | paged): 
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
        - number: 
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
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsBlocked'])

    @property
    def IsReady(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReady'])

    @property
    def PageSize(self):
        """
        Returns
        -------
        - number: 
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
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Timestamp'])

    @property
    def TotalPages(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalPages'])

    @property
    def TotalRows(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalRows'])

    def update(self, CurrentPage=None, EgressMode=None, EgressPageSize=None, PageSize=None):
        """Updates data resource on the server.

        Args
        ----
        - CurrentPage (number): 
        - EgressMode (str(conditional | paged)): 
        - EgressPageSize (number): 
        - PageSize (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
