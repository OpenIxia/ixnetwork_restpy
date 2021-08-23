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


class AvailableAdvancedFilterOptions(Base):
    """Provides a list of all the statistics and the filtering options for the current view.
    The AvailableAdvancedFilterOptions class encapsulates a list of availableAdvancedFilterOptions resources that are managed by the system.
    A list of resources can be retrieved from the server using the AvailableAdvancedFilterOptions.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'availableAdvancedFilterOptions'
    _SDM_ATT_MAP = {
        'Operators': 'operators',
        'Stat': 'stat',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(AvailableAdvancedFilterOptions, self).__init__(parent, list_op)

    @property
    def Operators(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Returns the operators list for a filter option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Operators'])

    @property
    def Stat(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Returns the statistic name for a filter option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Stat'])

    def add(self):
        """Adds a new availableAdvancedFilterOptions resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved availableAdvancedFilterOptions resources using find and the newly added availableAdvancedFilterOptions resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Operators=None, Stat=None):
        # type: (str, str) -> AvailableAdvancedFilterOptions
        """Finds and retrieves availableAdvancedFilterOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve availableAdvancedFilterOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all availableAdvancedFilterOptions resources from the server.

        Args
        ----
        - Operators (str): Returns the operators list for a filter option.
        - Stat (str): Returns the statistic name for a filter option.

        Returns
        -------
        - self: This instance with matching availableAdvancedFilterOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of availableAdvancedFilterOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the availableAdvancedFilterOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
