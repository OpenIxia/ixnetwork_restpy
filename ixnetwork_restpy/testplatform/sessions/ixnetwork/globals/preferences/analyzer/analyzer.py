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


class Analyzer(Base):
    """
    The Analyzer class encapsulates a required analyzer resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "analyzer"
    _SDM_ATT_MAP = {
        "EnablePacketLatency": "enablePacketLatency",
        "ReleaseHwCaptureOwnership": "releaseHwCaptureOwnership",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Analyzer, self).__init__(parent, list_op)

    @property
    def EnablePacketLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Compute per packet latency for Traffic packets
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePacketLatency"])

    @EnablePacketLatency.setter
    def EnablePacketLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePacketLatency"], value)

    @property
    def ReleaseHwCaptureOwnership(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Release HW Capture ownership when capture stops
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReleaseHwCaptureOwnership"])

    @ReleaseHwCaptureOwnership.setter
    def ReleaseHwCaptureOwnership(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReleaseHwCaptureOwnership"], value)

    def update(self, EnablePacketLatency=None, ReleaseHwCaptureOwnership=None):
        # type: (bool, bool) -> Analyzer
        """Updates analyzer resource on the server.

        Args
        ----
        - EnablePacketLatency (bool): Compute per packet latency for Traffic packets
        - ReleaseHwCaptureOwnership (bool): Release HW Capture ownership when capture stops

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, EnablePacketLatency=None, ReleaseHwCaptureOwnership=None):
        # type: (bool, bool) -> Analyzer
        """Finds and retrieves analyzer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve analyzer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all analyzer resources from the server.

        Args
        ----
        - EnablePacketLatency (bool): Compute per packet latency for Traffic packets
        - ReleaseHwCaptureOwnership (bool): Release HW Capture ownership when capture stops

        Returns
        -------
        - self: This instance with matching analyzer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of analyzer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the analyzer resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
