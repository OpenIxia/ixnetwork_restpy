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


class AdvancedFilter(Base):
    """Allows you to configure an advanced filter for drill down views.
    The AdvancedFilter class encapsulates a list of advancedFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the AdvancedFilter.find() method.
    The list can be managed by using the AdvancedFilter.add() and AdvancedFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'advancedFilter'
    _SDM_ATT_MAP = {
        'Expression': 'expression',
        'Name': 'name',
        'SortingStats': 'sortingStats',
        'TrackingFilterId': 'trackingFilterId',
    }

    def __init__(self, parent):
        super(AdvancedFilter, self).__init__(parent)

    @property
    def Expression(self):
        """
        Returns
        -------
        - str: Specifies the filter body. This is a string that must have a specific format.This can be empty (no filter). The available operations and statistics can be obtained from availableAdvancedFilterOptions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Expression'])
    @Expression.setter
    def Expression(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Expression'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Specifies the filter name. It must be unique per view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def SortingStats(self):
        """
        Returns
        -------
        - str: Specifies the list of statistics by which the view will be sorted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortingStats'])
    @SortingStats.setter
    def SortingStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortingStats'], value)

    @property
    def TrackingFilterId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters): Gets the id of the filter, which is used to add the filter to a view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackingFilterId'])
    @TrackingFilterId.setter
    def TrackingFilterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackingFilterId'], value)

    def update(self, Expression=None, Name=None, SortingStats=None, TrackingFilterId=None):
        """Updates advancedFilter resource on the server.

        Args
        ----
        - Expression (str): Specifies the filter body. This is a string that must have a specific format.This can be empty (no filter). The available operations and statistics can be obtained from availableAdvancedFilterOptions.
        - Name (str): Specifies the filter name. It must be unique per view.
        - SortingStats (str): Specifies the list of statistics by which the view will be sorted.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Gets the id of the filter, which is used to add the filter to a view.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Expression=None, Name=None, SortingStats=None, TrackingFilterId=None):
        """Adds a new advancedFilter resource on the server and adds it to the container.

        Args
        ----
        - Expression (str): Specifies the filter body. This is a string that must have a specific format.This can be empty (no filter). The available operations and statistics can be obtained from availableAdvancedFilterOptions.
        - Name (str): Specifies the filter name. It must be unique per view.
        - SortingStats (str): Specifies the list of statistics by which the view will be sorted.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Gets the id of the filter, which is used to add the filter to a view.

        Returns
        -------
        - self: This instance with all currently retrieved advancedFilter resources using find and the newly added advancedFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained advancedFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Expression=None, Name=None, SortingStats=None, TrackingFilterId=None):
        """Finds and retrieves advancedFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve advancedFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all advancedFilter resources from the server.

        Args
        ----
        - Expression (str): Specifies the filter body. This is a string that must have a specific format.This can be empty (no filter). The available operations and statistics can be obtained from availableAdvancedFilterOptions.
        - Name (str): Specifies the filter name. It must be unique per view.
        - SortingStats (str): Specifies the list of statistics by which the view will be sorted.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Gets the id of the filter, which is used to add the filter to a view.

        Returns
        -------
        - self: This instance with matching advancedFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of advancedFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the advancedFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
