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


class AdvancedCVFilters(Base):
    """Sets the advanced filter for a custom view. Note- To change the filter on an existing view, you must first disable it.
    The AdvancedCVFilters class encapsulates a list of advancedCVFilters resources that are managed by the user.
    A list of resources can be retrieved from the server using the AdvancedCVFilters.find() method.
    The list can be managed by using the AdvancedCVFilters.add() and AdvancedCVFilters.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'advancedCVFilters'
    _SDM_ATT_MAP = {
        'AvailableFilterOptions': 'availableFilterOptions',
        'AvailableGroupingOptions': 'availableGroupingOptions',
        'Caption': 'caption',
        'Expression': 'expression',
        'Grouping': 'grouping',
        'Protocol': 'protocol',
        'SortingStats': 'sortingStats',
    }

    def __init__(self, parent):
        super(AdvancedCVFilters, self).__init__(parent)

    @property
    def AvailableFilterOptions(self):
        """
        Returns
        -------
        - str: Returns a list of all the statistics and the operations available for filtering. Note- A protocol and a grouping must be set in order for this to work.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableFilterOptions'])

    @property
    def AvailableGroupingOptions(self):
        """
        Returns
        -------
        - str: Returns all the grouping options available. Note - A protocol must be set in order for this to work.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableGroupingOptions'])

    @property
    def Caption(self):
        """
        Returns
        -------
        - str: Sets a name for the filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Caption'])
    @Caption.setter
    def Caption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Caption'], value)

    @property
    def Expression(self):
        """
        Returns
        -------
        - str: Specifies the filter body. This is a string that must have the specific format. This can be empty or no filter.The available operations and statistics can be obtained from availableFilterOptions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Expression'])
    @Expression.setter
    def Expression(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Expression'], value)

    @property
    def Grouping(self):
        """
        Returns
        -------
        - str: Sets a grouping for the filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Grouping'])
    @Grouping.setter
    def Grouping(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Grouping'], value)

    @property
    def Protocol(self):
        """
        Returns
        -------
        - str: Sets a protocol for the filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Protocol'])
    @Protocol.setter
    def Protocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Protocol'], value)

    @property
    def SortingStats(self):
        """
        Returns
        -------
        - str: Specifies the list of statistics by which the view is sorted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortingStats'])
    @SortingStats.setter
    def SortingStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortingStats'], value)

    def update(self, Caption=None, Expression=None, Grouping=None, Protocol=None, SortingStats=None):
        """Updates advancedCVFilters resource on the server.

        Args
        ----
        - Caption (str): Sets a name for the filter.
        - Expression (str): Specifies the filter body. This is a string that must have the specific format. This can be empty or no filter.The available operations and statistics can be obtained from availableFilterOptions.
        - Grouping (str): Sets a grouping for the filter.
        - Protocol (str): Sets a protocol for the filter.
        - SortingStats (str): Specifies the list of statistics by which the view is sorted.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Caption=None, Expression=None, Grouping=None, Protocol=None, SortingStats=None):
        """Adds a new advancedCVFilters resource on the server and adds it to the container.

        Args
        ----
        - Caption (str): Sets a name for the filter.
        - Expression (str): Specifies the filter body. This is a string that must have the specific format. This can be empty or no filter.The available operations and statistics can be obtained from availableFilterOptions.
        - Grouping (str): Sets a grouping for the filter.
        - Protocol (str): Sets a protocol for the filter.
        - SortingStats (str): Specifies the list of statistics by which the view is sorted.

        Returns
        -------
        - self: This instance with all currently retrieved advancedCVFilters resources using find and the newly added advancedCVFilters resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained advancedCVFilters resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AvailableFilterOptions=None, AvailableGroupingOptions=None, Caption=None, Expression=None, Grouping=None, Protocol=None, SortingStats=None):
        """Finds and retrieves advancedCVFilters resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve advancedCVFilters resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all advancedCVFilters resources from the server.

        Args
        ----
        - AvailableFilterOptions (str): Returns a list of all the statistics and the operations available for filtering. Note- A protocol and a grouping must be set in order for this to work.
        - AvailableGroupingOptions (str): Returns all the grouping options available. Note - A protocol must be set in order for this to work.
        - Caption (str): Sets a name for the filter.
        - Expression (str): Specifies the filter body. This is a string that must have the specific format. This can be empty or no filter.The available operations and statistics can be obtained from availableFilterOptions.
        - Grouping (str): Sets a grouping for the filter.
        - Protocol (str): Sets a protocol for the filter.
        - SortingStats (str): Specifies the list of statistics by which the view is sorted.

        Returns
        -------
        - self: This instance with matching advancedCVFilters resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of advancedCVFilters data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the advancedCVFilters resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
