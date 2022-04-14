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


class CpdpConvergence(Base):
    """This object fetches the control plane and data plane statistics.
    The CpdpConvergence class encapsulates a required cpdpConvergence resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cpdpConvergence"
    _SDM_ATT_MAP = {
        "DataPlaneJitterWindow": "dataPlaneJitterWindow",
        "DataPlaneThreshold": "dataPlaneThreshold",
        "EnableControlPlaneEvents": "enableControlPlaneEvents",
        "EnableDataPlaneEventsRateMonitor": "enableDataPlaneEventsRateMonitor",
        "Enabled": "enabled",
    }
    _SDM_ENUM_MAP = {
        "dataPlaneJitterWindow": [
            "0",
            "10485760",
            "1310720",
            "167772160",
            "20971520",
            "2621440",
            "335544320",
            "41943040",
            "5242880",
            "671088640",
            "83886080",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(CpdpConvergence, self).__init__(parent, list_op)

    @property
    def DataPlaneJitterWindow(self):
        # type: () -> str
        """
        Returns
        -------
        - str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080): Indicates the number of packets received during a time interval. This is used for calculating the rate on the recieve side.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPlaneJitterWindow"])

    @DataPlaneJitterWindow.setter
    def DataPlaneJitterWindow(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataPlaneJitterWindow"], value)

    @property
    def DataPlaneThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data loss threshold percentage for CP/DP events at the prompt.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPlaneThreshold"])

    @DataPlaneThreshold.setter
    def DataPlaneThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataPlaneThreshold"], value)

    @property
    def EnableControlPlaneEvents(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, fetches control plane event statistics of event name, event start timestamp, and event end timestamp.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableControlPlaneEvents"])

    @EnableControlPlaneEvents.setter
    def EnableControlPlaneEvents(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableControlPlaneEvents"], value)

    @property
    def EnableDataPlaneEventsRateMonitor(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, fetches data plane event rate statistics of DP above Threshold Timestamp, DP below Threshold Timestamp, Ramp Up Convergence, Ramp Down Convergence, CP/DP Convergence, and DP/DP Convergence.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableDataPlaneEventsRateMonitor"]
        )

    @EnableDataPlaneEventsRateMonitor.setter
    def EnableDataPlaneEventsRateMonitor(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableDataPlaneEventsRateMonitor"], value
        )

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, fetches control plane/data plane statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    def update(
        self,
        DataPlaneJitterWindow=None,
        DataPlaneThreshold=None,
        EnableControlPlaneEvents=None,
        EnableDataPlaneEventsRateMonitor=None,
        Enabled=None,
    ):
        # type: (str, int, bool, bool, bool) -> CpdpConvergence
        """Updates cpdpConvergence resource on the server.

        Args
        ----
        - DataPlaneJitterWindow (str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080)): Indicates the number of packets received during a time interval. This is used for calculating the rate on the recieve side.
        - DataPlaneThreshold (number): The data loss threshold percentage for CP/DP events at the prompt.
        - EnableControlPlaneEvents (bool): If enabled, fetches control plane event statistics of event name, event start timestamp, and event end timestamp.
        - EnableDataPlaneEventsRateMonitor (bool): If enabled, fetches data plane event rate statistics of DP above Threshold Timestamp, DP below Threshold Timestamp, Ramp Up Convergence, Ramp Down Convergence, CP/DP Convergence, and DP/DP Convergence.
        - Enabled (bool): If enabled, fetches control plane/data plane statistics.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DataPlaneJitterWindow=None,
        DataPlaneThreshold=None,
        EnableControlPlaneEvents=None,
        EnableDataPlaneEventsRateMonitor=None,
        Enabled=None,
    ):
        # type: (str, int, bool, bool, bool) -> CpdpConvergence
        """Finds and retrieves cpdpConvergence resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cpdpConvergence resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cpdpConvergence resources from the server.

        Args
        ----
        - DataPlaneJitterWindow (str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080)): Indicates the number of packets received during a time interval. This is used for calculating the rate on the recieve side.
        - DataPlaneThreshold (number): The data loss threshold percentage for CP/DP events at the prompt.
        - EnableControlPlaneEvents (bool): If enabled, fetches control plane event statistics of event name, event start timestamp, and event end timestamp.
        - EnableDataPlaneEventsRateMonitor (bool): If enabled, fetches data plane event rate statistics of DP above Threshold Timestamp, DP below Threshold Timestamp, Ramp Up Convergence, Ramp Down Convergence, CP/DP Convergence, and DP/DP Convergence.
        - Enabled (bool): If enabled, fetches control plane/data plane statistics.

        Returns
        -------
        - self: This instance with matching cpdpConvergence resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cpdpConvergence data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cpdpConvergence resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
