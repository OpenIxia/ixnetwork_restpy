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


class Timestamp(Base):
    """This node contains Timestamp settings.
    The Timestamp class encapsulates a required timestamp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "timestamp"
    _SDM_ATT_MAP = {
        "TimestampPrecision": "timestampPrecision",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Timestamp, self).__init__(parent, list_op)

    @property
    def TimestampPrecision(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the statistics display values with decimals ranging from 0 to 9.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimestampPrecision"])

    @TimestampPrecision.setter
    def TimestampPrecision(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimestampPrecision"], value)

    def update(self, TimestampPrecision=None):
        # type: (int) -> Timestamp
        """Updates timestamp resource on the server.

        Args
        ----
        - TimestampPrecision (number): The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the statistics display values with decimals ranging from 0 to 9.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, TimestampPrecision=None):
        # type: (int) -> Timestamp
        """Finds and retrieves timestamp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve timestamp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all timestamp resources from the server.

        Args
        ----
        - TimestampPrecision (number): The timestamp precision allows you to change the timestamp precision from microseconds to nanoseconds for specific StatViewer statistics and features. The timestamp precision can be set to have the statistics display values with decimals ranging from 0 to 9.

        Returns
        -------
        - self: This instance with matching timestamp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of timestamp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the timestamp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
