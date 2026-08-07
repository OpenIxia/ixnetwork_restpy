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


class TxCtlOSDelay(Base):
    """
    The TxCtlOSDelay class encapsulates a required txCtlOSDelay resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "txCtlOSDelay"
    _SDM_ATT_MAP = {
        "DelayNs": "delayNs",
        "TestState": "testState",
        "TestStatus": "testStatus",
    }
    _SDM_ENUM_MAP = {
        "testState": ["notRunning", "running", "stopping", "error"],
    }

    def __init__(self, parent, list_op=False):
        super(TxCtlOSDelay, self).__init__(parent, list_op)

    @property
    def DelayNs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Extra delay (in nanoseconds) added before each transmitted CtlOS frame. Range: [0, 10237].
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayNs"])

    @DelayNs.setter
    def DelayNs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayNs"], value)

    @property
    def TestState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notRunning | running | stopping | error): Current execution state of the impairment test (Not Running / Running / Stopping / Error).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestState"])

    @property
    def TestStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Status of the impairment test's last/current run (e.g., Started, Stopped, error details).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestStatus"])

    def update(self, DelayNs=None):
        # type: (int) -> TxCtlOSDelay
        """Updates txCtlOSDelay resource on the server.

        Args
        ----
        - DelayNs (number): Extra delay (in nanoseconds) added before each transmitted CtlOS frame. Range: [0, 10237].

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, DelayNs=None, TestState=None, TestStatus=None):
        # type: (int, str, str) -> TxCtlOSDelay
        """Finds and retrieves txCtlOSDelay resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve txCtlOSDelay resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all txCtlOSDelay resources from the server.

        Args
        ----
        - DelayNs (number): Extra delay (in nanoseconds) added before each transmitted CtlOS frame. Range: [0, 10237].
        - TestState (str(notRunning | running | stopping | error)): Current execution state of the impairment test (Not Running / Running / Stopping / Error).
        - TestStatus (str): Status of the impairment test's last/current run (e.g., Started, Stopped, error details).

        Returns
        -------
        - self: This instance with matching txCtlOSDelay resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of txCtlOSDelay data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the txCtlOSDelay resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
