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


class Duplicate(Base):
    """Duplicate packets.
    The Duplicate class encapsulates a required duplicate resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "duplicate"
    _SDM_ATT_MAP = {
        "ClusterSize": "clusterSize",
        "DuplicateCount": "duplicateCount",
        "Enabled": "enabled",
        "PercentRate": "percentRate",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Duplicate, self).__init__(parent, list_op)

    @property
    def ClusterSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of packets to duplicate on each occurrence.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClusterSize"])

    @ClusterSize.setter
    def ClusterSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClusterSize"], value)

    @property
    def DuplicateCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of times to duplicate each packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DuplicateCount"])

    @DuplicateCount.setter
    def DuplicateCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DuplicateCount"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, periodically duplicate received packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def PercentRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: How often to duplicate packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PercentRate"])

    @PercentRate.setter
    def PercentRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PercentRate"], value)

    def update(
        self, ClusterSize=None, DuplicateCount=None, Enabled=None, PercentRate=None
    ):
        # type: (int, int, bool, int) -> Duplicate
        """Updates duplicate resource on the server.

        Args
        ----
        - ClusterSize (number): Number of packets to duplicate on each occurrence.
        - DuplicateCount (number): Number of times to duplicate each packet.
        - Enabled (bool): If true, periodically duplicate received packets.
        - PercentRate (number): How often to duplicate packets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, ClusterSize=None, DuplicateCount=None, Enabled=None, PercentRate=None
    ):
        # type: (int, int, bool, int) -> Duplicate
        """Finds and retrieves duplicate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve duplicate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all duplicate resources from the server.

        Args
        ----
        - ClusterSize (number): Number of packets to duplicate on each occurrence.
        - DuplicateCount (number): Number of times to duplicate each packet.
        - Enabled (bool): If true, periodically duplicate received packets.
        - PercentRate (number): How often to duplicate packets.

        Returns
        -------
        - self: This instance with matching duplicate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of duplicate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the duplicate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
