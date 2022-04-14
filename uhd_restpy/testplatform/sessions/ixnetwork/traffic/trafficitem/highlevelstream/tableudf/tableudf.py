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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class TableUdf(Base):
    """This object specifies the UDF table properties.
    The TableUdf class encapsulates a list of tableUdf resources that are managed by the system.
    A list of resources can be retrieved from the server using the TableUdf.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tableUdf'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(TableUdf, self).__init__(parent, list_op)

    @property
    def Column(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column.Column): An instance of the Column class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column import Column
        if len(self._object_properties) > 0:
            if self._properties.get('Column', None) is not None:
                return self._properties.get('Column')
        return Column(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, enables the UDF table for this flow group if it is supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    def update(self, Enabled=None):
        # type: (bool) -> TableUdf
        """Updates tableUdf resource on the server.

        Args
        ----
        - Enabled (bool): If enabled, enables the UDF table for this flow group if it is supported.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None):
        # type: (bool) -> TableUdf
        """Adds a new tableUdf resource on the json, only valid with batch add utility

        Args
        ----
        - Enabled (bool): If enabled, enables the UDF table for this flow group if it is supported.

        Returns
        -------
        - self: This instance with all currently retrieved tableUdf resources using find and the newly added tableUdf resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None):
        # type: (bool) -> TableUdf
        """Finds and retrieves tableUdf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tableUdf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tableUdf resources from the server.

        Args
        ----
        - Enabled (bool): If enabled, enables the UDF table for this flow group if it is supported.

        Returns
        -------
        - self: This instance with matching tableUdf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tableUdf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tableUdf resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
