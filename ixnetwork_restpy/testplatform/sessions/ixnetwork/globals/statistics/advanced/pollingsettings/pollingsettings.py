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


class PollingSettings(Base):
    """This node contains the polling settings.
    The PollingSettings class encapsulates a required pollingSettings resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pollingSettings"
    _SDM_ATT_MAP = {
        "ForcePollValue": "forcePollValue",
        "MinimumRefreshIntervalForOnDemandViews": "minimumRefreshIntervalForOnDemandViews",
        "PollInterval": "pollInterval",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PollingSettings, self).__init__(parent, list_op)

    @property
    def ForcePollValue(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When set to True, it will force set the poll value
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForcePollValue"])

    @ForcePollValue.setter
    def ForcePollValue(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForcePollValue"], value)

    @property
    def MinimumRefreshIntervalForOnDemandViews(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum Refresh Interval for Next Gen On-Demand Views
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["MinimumRefreshIntervalForOnDemandViews"]
        )

    @MinimumRefreshIntervalForOnDemandViews.setter
    def MinimumRefreshIntervalForOnDemandViews(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["MinimumRefreshIntervalForOnDemandViews"], value
        )

    @property
    def PollInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds). Note: The above settings will only be applied by saving the configuration and restarting the application! (Exception: The NextGen views are not affected by this change.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollInterval"])

    @PollInterval.setter
    def PollInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollInterval"], value)

    def update(
        self,
        ForcePollValue=None,
        MinimumRefreshIntervalForOnDemandViews=None,
        PollInterval=None,
    ):
        # type: (bool, int, int) -> PollingSettings
        """Updates pollingSettings resource on the server.

        Args
        ----
        - ForcePollValue (bool): When set to True, it will force set the poll value
        - MinimumRefreshIntervalForOnDemandViews (number): Minimum Refresh Interval for Next Gen On-Demand Views
        - PollInterval (number): The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds). Note: The above settings will only be applied by saving the configuration and restarting the application! (Exception: The NextGen views are not affected by this change.)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ForcePollValue=None,
        MinimumRefreshIntervalForOnDemandViews=None,
        PollInterval=None,
    ):
        # type: (bool, int, int) -> PollingSettings
        """Finds and retrieves pollingSettings resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pollingSettings resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pollingSettings resources from the server.

        Args
        ----
        - ForcePollValue (bool): When set to True, it will force set the poll value
        - MinimumRefreshIntervalForOnDemandViews (number): Minimum Refresh Interval for Next Gen On-Demand Views
        - PollInterval (number): The multiplier used with the frequency (2 seconds), to set the time interval between polling events. The default is 1 (1 times 2 seconds = 2 seconds). Note: The above settings will only be applied by saving the configuration and restarting the application! (Exception: The NextGen views are not affected by this change.)

        Returns
        -------
        - self: This instance with matching pollingSettings resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pollingSettings data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pollingSettings resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
