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


class LosLof(Base):
    """DEPRECATED Emulates loss of signal or loss of framing on the link.
    The LosLof class encapsulates a required losLof resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "losLof"
    _SDM_ATT_MAP = {
        "Duration": "duration",
        "IsBurst": "isBurst",
        "State": "state",
        "Type": "type",
        "Units": "units",
    }
    _SDM_ENUM_MAP = {
        "state": ["started", "stopped"],
        "type": ["lof", "los"],
        "units": [
            "kMicroseconds",
            "kMilliseconds",
            "kSeconds",
            "microseconds",
            "milliseconds",
            "seconds",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(LosLof, self).__init__(parent, list_op)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The burst duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Duration"])

    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Duration"], value)

    @property
    def IsBurst(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, loss of signal or loss of frame will be enabled for the specified duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsBurst"])

    @IsBurst.setter
    def IsBurst(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsBurst"], value)

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str(started | stopped): Gets the loss of signal or loss of framing state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["State"])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(lof | los): Selects loss of signal or loss of framing.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    @property
    def Units(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kMicroseconds | kMilliseconds | kSeconds | microseconds | milliseconds | seconds): Burst duration units.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Units"])

    @Units.setter
    def Units(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Units"], value)

    def update(self, Duration=None, IsBurst=None, Type=None, Units=None):
        # type: (int, bool, str, str) -> LosLof
        """Updates losLof resource on the server.

        Args
        ----
        - Duration (number): The burst duration.
        - IsBurst (bool): If true, loss of signal or loss of frame will be enabled for the specified duration.
        - Type (str(lof | los)): Selects loss of signal or loss of framing.
        - Units (str(kMicroseconds | kMilliseconds | kSeconds | microseconds | milliseconds | seconds)): Burst duration units.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Duration=None, IsBurst=None, State=None, Type=None, Units=None):
        # type: (int, bool, str, str, str) -> LosLof
        """Finds and retrieves losLof resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve losLof resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all losLof resources from the server.

        Args
        ----
        - Duration (number): The burst duration.
        - IsBurst (bool): If true, loss of signal or loss of frame will be enabled for the specified duration.
        - State (str(started | stopped)): Gets the loss of signal or loss of framing state.
        - Type (str(lof | los)): Selects loss of signal or loss of framing.
        - Units (str(kMicroseconds | kMilliseconds | kSeconds | microseconds | milliseconds | seconds)): Burst duration units.

        Returns
        -------
        - self: This instance with matching losLof resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of losLof data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the losLof resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the impairments defined by user (traffic will be impaired).

        DEPRECATED start(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the impairments defined by user (traffic will pass unimpaired).

        DEPRECATED stop(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)
