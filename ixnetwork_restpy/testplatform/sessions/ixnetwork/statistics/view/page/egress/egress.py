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


class Egress(Base):
    """DEPRECATED SV settings for egress traking display. (fixed list, based on number of ingress rows)
    The Egress class encapsulates a list of egress resources that are managed by the system.
    A list of resources can be retrieved from the server using the Egress.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'egress'
    _SDM_ATT_MAP = {
        'CommitEgressPage': 'commitEgressPage',
        'CurrentPage': 'currentPage',
        'RowCount': 'rowCount',
        'TotalPages': 'totalPages',
    }

    def __init__(self, parent):
        super(Egress, self).__init__(parent)

    @property
    def FlowCondition(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egress.flowcondition.flowcondition.FlowCondition): An instance of the FlowCondition class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.egress.flowcondition.flowcondition import FlowCondition
        return FlowCondition(self)

    @property
    def CommitEgressPage(self):
        """
        Returns
        -------
        - bool: Attribute used to commit egress paging from TCL
        """
        return self._get_attribute(self._SDM_ATT_MAP['CommitEgressPage'])
    @CommitEgressPage.setter
    def CommitEgressPage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CommitEgressPage'], value)

    @property
    def CurrentPage(self):
        """
        Returns
        -------
        - number: Determines the current egress page for the indicated ingress page.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentPage'])
    @CurrentPage.setter
    def CurrentPage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CurrentPage'], value)

    @property
    def RowCount(self):
        """
        Returns
        -------
        - number: Displays the particular row number in the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowCount'])

    @property
    def TotalPages(self):
        """
        Returns
        -------
        - number: The total number of egress pages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalPages'])

    def update(self, CommitEgressPage=None, CurrentPage=None):
        """Updates egress resource on the server.

        Args
        ----
        - CommitEgressPage (bool): Attribute used to commit egress paging from TCL
        - CurrentPage (number): Determines the current egress page for the indicated ingress page.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CommitEgressPage=None, CurrentPage=None, RowCount=None, TotalPages=None):
        """Finds and retrieves egress resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egress resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egress resources from the server.

        Args
        ----
        - CommitEgressPage (bool): Attribute used to commit egress paging from TCL
        - CurrentPage (number): Determines the current egress page for the indicated ingress page.
        - RowCount (number): Displays the particular row number in the view.
        - TotalPages (number): The total number of egress pages.

        Returns
        -------
        - self: This instance with matching egress resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egress data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egress resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
