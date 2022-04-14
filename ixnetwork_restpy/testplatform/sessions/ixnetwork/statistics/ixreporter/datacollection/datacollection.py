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


class DataCollection(Base):
    """DEPRECATED Specifies the collection of data.
    The DataCollection class encapsulates a required dataCollection resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dataCollection"
    _SDM_ATT_MAP = {
        "Enable": "Enable",
        "LastRunId": "LastRunId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DataCollection, self).__init__(parent, list_op)

    @property
    def Enable(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If set to true, enables collection of data
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enable"])

    @Enable.setter
    def Enable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enable"], value)

    @property
    def LastRunId(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Specifies the identifier for last run.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastRunId"])

    def update(self, Enable=None):
        # type: (bool) -> DataCollection
        """Updates dataCollection resource on the server.

        Args
        ----
        - Enable (bool): If set to true, enables collection of data

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enable=None, LastRunId=None):
        # type: (bool, int) -> DataCollection
        """Finds and retrieves dataCollection resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dataCollection resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dataCollection resources from the server.

        Args
        ----
        - Enable (bool): If set to true, enables collection of data
        - LastRunId (number): Specifies the identifier for last run.

        Returns
        -------
        - self: This instance with matching dataCollection resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dataCollection data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dataCollection resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
