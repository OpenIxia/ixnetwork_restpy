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


class TableModificationTriggerAttributes(Base):
    """To modify the table config property, right click on any row in the grid, and select Table Modification Trigger. The Table Modification Trigger dialog appears.
    The TableModificationTriggerAttributes class encapsulates a required tableModificationTriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "tableModificationTriggerAttributes"
    _SDM_ATT_MAP = {
        "AllTables": "allTables",
        "Config": "config",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TableModificationTriggerAttributes, self).__init__(parent, list_op)

    @property
    def AllTables(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: To apply the change to all tables.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AllTables"])

    @AllTables.setter
    def AllTables(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AllTables"], value)

    @property
    def Config(self):
        # type: () -> int
        """
        Returns
        -------
        - number: 2.Type the value of the Config.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Config"])

    @Config.setter
    def Config(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Config"], value)

    def update(self, AllTables=None, Config=None):
        # type: (bool, int) -> TableModificationTriggerAttributes
        """Updates tableModificationTriggerAttributes resource on the server.

        Args
        ----
        - AllTables (bool): To apply the change to all tables.
        - Config (number): 2.Type the value of the Config.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AllTables=None, Config=None):
        # type: (bool, int) -> TableModificationTriggerAttributes
        """Finds and retrieves tableModificationTriggerAttributes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tableModificationTriggerAttributes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tableModificationTriggerAttributes resources from the server.

        Args
        ----
        - AllTables (bool): To apply the change to all tables.
        - Config (number): 2.Type the value of the Config.

        Returns
        -------
        - self: This instance with matching tableModificationTriggerAttributes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tableModificationTriggerAttributes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tableModificationTriggerAttributes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
