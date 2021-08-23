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


class AvailableTrafficItemFilter(Base):
    """List of traffic items available for filtering.
    The AvailableTrafficItemFilter class encapsulates a list of availableTrafficItemFilter resources that are managed by the system.
    A list of resources can be retrieved from the server using the AvailableTrafficItemFilter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'availableTrafficItemFilter'
    _SDM_ATT_MAP = {
        'Constraints': 'constraints',
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(AvailableTrafficItemFilter, self).__init__(parent, list_op)

    @property
    def Constraints(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Lists down the constraints associated with the available traffic item filter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Constraints'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Displays the name of the traffic item filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    def add(self):
        """Adds a new availableTrafficItemFilter resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved availableTrafficItemFilter resources using find and the newly added availableTrafficItemFilter resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Constraints=None, Name=None):
        # type: (List[str], str) -> AvailableTrafficItemFilter
        """Finds and retrieves availableTrafficItemFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve availableTrafficItemFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all availableTrafficItemFilter resources from the server.

        Args
        ----
        - Constraints (list(str)): Lists down the constraints associated with the available traffic item filter list.
        - Name (str): Displays the name of the traffic item filter.

        Returns
        -------
        - self: This instance with matching availableTrafficItemFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of availableTrafficItemFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the availableTrafficItemFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
