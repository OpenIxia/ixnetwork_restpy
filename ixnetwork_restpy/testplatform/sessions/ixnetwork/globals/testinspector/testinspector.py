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


class TestInspector(Base):
    """DEPRECATED
    The TestInspector class encapsulates a required testInspector resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testInspector"
    _SDM_ATT_MAP = {
        "EnableTestInspector": "enableTestInspector",
        "PollingInterval": "pollingInterval",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TestInspector, self).__init__(parent, list_op)

    @property
    def Statistic(self):
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.testinspector.statistic.statistic.Statistic): An instance of the Statistic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.testinspector.statistic.statistic import (
            Statistic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Statistic", None) is not None:
                return self._properties.get("Statistic")
        return Statistic(self)

    @property
    def EnableTestInspector(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable Test Inspector
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTestInspector"])

    @EnableTestInspector.setter
    def EnableTestInspector(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTestInspector"], value)

    @property
    def PollingInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Polling Interval
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollingInterval"])

    @PollingInterval.setter
    def PollingInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollingInterval"], value)

    def update(self, EnableTestInspector=None, PollingInterval=None):
        # type: (bool, int) -> TestInspector
        """Updates testInspector resource on the server.

        Args
        ----
        - EnableTestInspector (bool): Enable/Disable Test Inspector
        - PollingInterval (number): Polling Interval

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, EnableTestInspector=None, PollingInterval=None):
        # type: (bool, int) -> TestInspector
        """Finds and retrieves testInspector resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testInspector resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testInspector resources from the server.

        Args
        ----
        - EnableTestInspector (bool): Enable/Disable Test Inspector
        - PollingInterval (number): Polling Interval

        Returns
        -------
        - self: This instance with matching testInspector resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testInspector data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testInspector resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
