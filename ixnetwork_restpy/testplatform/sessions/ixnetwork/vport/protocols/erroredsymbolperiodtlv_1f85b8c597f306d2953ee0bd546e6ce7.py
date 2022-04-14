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


class ErroredSymbolPeriodTlv(Base):
    """
    The ErroredSymbolPeriodTlv class encapsulates a required erroredSymbolPeriodTlv resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "erroredSymbolPeriodTlv"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "Symbols": "symbols",
        "Threshold": "threshold",
        "Window": "window",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ErroredSymbolPeriodTlv, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Symbols(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Symbols"])

    @Symbols.setter
    def Symbols(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Symbols"], value)

    @property
    def Threshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Threshold"])

    @Threshold.setter
    def Threshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Threshold"], value)

    @property
    def Window(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Window"])

    @Window.setter
    def Window(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Window"], value)

    def update(self, Enabled=None, Symbols=None, Threshold=None, Window=None):
        # type: (bool, int, int, int) -> ErroredSymbolPeriodTlv
        """Updates erroredSymbolPeriodTlv resource on the server.

        Args
        ----
        - Enabled (bool):
        - Symbols (number):
        - Threshold (number):
        - Window (number):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None, Symbols=None, Threshold=None, Window=None):
        # type: (bool, int, int, int) -> ErroredSymbolPeriodTlv
        """Finds and retrieves erroredSymbolPeriodTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve erroredSymbolPeriodTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all erroredSymbolPeriodTlv resources from the server.

        Args
        ----
        - Enabled (bool):
        - Symbols (number):
        - Threshold (number):
        - Window (number):

        Returns
        -------
        - self: This instance with matching erroredSymbolPeriodTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of erroredSymbolPeriodTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the erroredSymbolPeriodTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
