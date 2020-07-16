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


class EnumerationFilter(Base):
    """Enumeration filter specification.
    The EnumerationFilter class encapsulates a list of enumerationFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the EnumerationFilter.find() method.
    The list can be managed by using the EnumerationFilter.add() and EnumerationFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'enumerationFilter'
    _SDM_ATT_MAP = {
        'SortDirection': 'sortDirection',
        'TrackingFilterId': 'trackingFilterId',
    }

    def __init__(self, parent):
        super(EnumerationFilter, self).__init__(parent)

    @property
    def SortDirection(self):
        """
        Returns
        -------
        - str(ascending | descending): Sets the display order of the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortDirection'])
    @SortDirection.setter
    def SortDirection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortDirection'], value)

    @property
    def TrackingFilterId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter): Selected tracking filters from the availableTrackingFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackingFilterId'])
    @TrackingFilterId.setter
    def TrackingFilterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackingFilterId'], value)

    def update(self, SortDirection=None, TrackingFilterId=None):
        """Updates enumerationFilter resource on the server.

        Args
        ----
        - SortDirection (str(ascending | descending)): Sets the display order of the view.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, SortDirection=None, TrackingFilterId=None):
        """Adds a new enumerationFilter resource on the server and adds it to the container.

        Args
        ----
        - SortDirection (str(ascending | descending)): Sets the display order of the view.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.

        Returns
        -------
        - self: This instance with all currently retrieved enumerationFilter resources using find and the newly added enumerationFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained enumerationFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, SortDirection=None, TrackingFilterId=None):
        """Finds and retrieves enumerationFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve enumerationFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all enumerationFilter resources from the server.

        Args
        ----
        - SortDirection (str(ascending | descending)): Sets the display order of the view.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.

        Returns
        -------
        - self: This instance with matching enumerationFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of enumerationFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the enumerationFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
