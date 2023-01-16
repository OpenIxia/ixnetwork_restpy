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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Egress(Base):
    """
    The Egress class encapsulates a list of egress resources that are managed by the system.
    A list of resources can be retrieved from the server using the Egress.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "egress"
    _SDM_ATT_MAP = {
        "CommitEgressPage": "commitEgressPage",
        "CurrentPage": "currentPage",
        "RowCount": "rowCount",
        "TotalPages": "totalPages",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Egress, self).__init__(parent, list_op)

    @property
    def FlowCondition(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.data.egress.flowcondition.flowcondition.FlowCondition): An instance of the FlowCondition class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.data.egress.flowcondition.flowcondition import (
            FlowCondition,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlowCondition", None) is not None:
                return self._properties.get("FlowCondition")
        return FlowCondition(self)

    @property
    def CommitEgressPage(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Attribute used to commit egress paging from script.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CommitEgressPage"])

    @CommitEgressPage.setter
    def CommitEgressPage(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CommitEgressPage"], value)

    @property
    def CurrentPage(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The current page number being displayed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentPage"])

    @CurrentPage.setter
    def CurrentPage(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CurrentPage"], value)

    @property
    def RowCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Displays the particular row number in the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowCount"])

    @property
    def TotalPages(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The total number of statistics pages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TotalPages"])

    def update(self, CommitEgressPage=None, CurrentPage=None):
        # type: (bool, int) -> Egress
        """Updates egress resource on the server.

        Args
        ----
        - CommitEgressPage (bool): Attribute used to commit egress paging from script.
        - CurrentPage (number): The current page number being displayed.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CommitEgressPage=None, CurrentPage=None):
        # type: (bool, int) -> Egress
        """Adds a new egress resource on the json, only valid with batch add utility

        Args
        ----
        - CommitEgressPage (bool): Attribute used to commit egress paging from script.
        - CurrentPage (number): The current page number being displayed.

        Returns
        -------
        - self: This instance with all currently retrieved egress resources using find and the newly added egress resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, CommitEgressPage=None, CurrentPage=None, RowCount=None, TotalPages=None
    ):
        # type: (bool, int, int, int) -> Egress
        """Finds and retrieves egress resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egress resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egress resources from the server.

        Args
        ----
        - CommitEgressPage (bool): Attribute used to commit egress paging from script.
        - CurrentPage (number): The current page number being displayed.
        - RowCount (number): Displays the particular row number in the view.
        - TotalPages (number): The total number of statistics pages.

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
