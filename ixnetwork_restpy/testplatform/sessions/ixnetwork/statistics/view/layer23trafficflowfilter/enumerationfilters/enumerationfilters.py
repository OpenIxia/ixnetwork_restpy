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


class EnumerationFilters(Base):
    """Contains list of all the enumeration filters (tracking options) available which can be enabled for the custom view.
    The EnumerationFilters class encapsulates a list of enumerationFilters resources that are managed by the system.
    A list of resources can be retrieved from the server using the EnumerationFilters.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "enumerationFilters"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "Name": "name",
        "SortDirection": "sortDirection",
        "TrackingFilterId": "trackingFilterId",
    }
    _SDM_ENUM_MAP = {
        "sortDirection": ["ascending", "descending"],
    }

    def __init__(self, parent, list_op=False):
        super(EnumerationFilters, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Value determining whether the filter is selected or not
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Selected enumeration filters from the tracking Filter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @property
    def SortDirection(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ascending | descending):
        """
        return self._get_attribute(self._SDM_ATT_MAP["SortDirection"])

    @SortDirection.setter
    def SortDirection(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SortDirection"], value)

    @property
    def TrackingFilterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The reference id of available tracking filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrackingFilterId"])

    def update(self, Enabled=None, SortDirection=None):
        # type: (bool, str) -> EnumerationFilters
        """Updates enumerationFilters resource on the server.

        Args
        ----
        - Enabled (bool): Value determining whether the filter is selected or not
        - SortDirection (str(ascending | descending)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, SortDirection=None):
        # type: (bool, str) -> EnumerationFilters
        """Adds a new enumerationFilters resource on the json, only valid with batch add utility

        Args
        ----
        - Enabled (bool): Value determining whether the filter is selected or not
        - SortDirection (str(ascending | descending)):

        Returns
        -------
        - self: This instance with all currently retrieved enumerationFilters resources using find and the newly added enumerationFilters resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None, Name=None, SortDirection=None, TrackingFilterId=None):
        # type: (bool, str, str, str) -> EnumerationFilters
        """Finds and retrieves enumerationFilters resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve enumerationFilters resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all enumerationFilters resources from the server.

        Args
        ----
        - Enabled (bool): Value determining whether the filter is selected or not
        - Name (str): Selected enumeration filters from the tracking Filter list.
        - SortDirection (str(ascending | descending)):
        - TrackingFilterId (str): The reference id of available tracking filter.

        Returns
        -------
        - self: This instance with matching enumerationFilters resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of enumerationFilters data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the enumerationFilters resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
