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


class RoceV2TestConfig(Base):
    """RoCEv2 Test Configuration
    The RoceV2TestConfig class encapsulates a list of roceV2TestConfig resources that are managed by the system.
    A list of resources can be retrieved from the server using the RoceV2TestConfig.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "roceV2TestConfig"
    _SDM_ATT_MAP = {
        "LatencyMode": "latencyMode",
        "SupportReordering": "supportReordering",
    }
    _SDM_ENUM_MAP = {
        "latencyMode": ["cutThrough", "forwardingDelay", "mef", "storeForward"],
    }

    def __init__(self, parent, list_op=False):
        super(RoceV2TestConfig, self).__init__(parent, list_op)

    @property
    def LatencyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | forwardingDelay | mef | storeForward): Latency mode for 2arm traffic
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyMode"])

    @LatencyMode.setter
    def LatencyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyMode"], value)

    @property
    def SupportReordering(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable frame reordering
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportReordering"])

    @SupportReordering.setter
    def SupportReordering(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportReordering"], value)

    def update(self, LatencyMode=None, SupportReordering=None):
        # type: (str, bool) -> RoceV2TestConfig
        """Updates roceV2TestConfig resource on the server.

        Args
        ----
        - LatencyMode (str(cutThrough | forwardingDelay | mef | storeForward)): Latency mode for 2arm traffic
        - SupportReordering (bool): Enable frame reordering

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, LatencyMode=None, SupportReordering=None):
        # type: (str, bool) -> RoceV2TestConfig
        """Adds a new roceV2TestConfig resource on the json, only valid with batch add utility

        Args
        ----
        - LatencyMode (str(cutThrough | forwardingDelay | mef | storeForward)): Latency mode for 2arm traffic
        - SupportReordering (bool): Enable frame reordering

        Returns
        -------
        - self: This instance with all currently retrieved roceV2TestConfig resources using find and the newly added roceV2TestConfig resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, LatencyMode=None, SupportReordering=None):
        # type: (str, bool) -> RoceV2TestConfig
        """Finds and retrieves roceV2TestConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve roceV2TestConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all roceV2TestConfig resources from the server.

        Args
        ----
        - LatencyMode (str(cutThrough | forwardingDelay | mef | storeForward)): Latency mode for 2arm traffic
        - SupportReordering (bool): Enable frame reordering

        Returns
        -------
        - self: This instance with matching roceV2TestConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of roceV2TestConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the roceV2TestConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
