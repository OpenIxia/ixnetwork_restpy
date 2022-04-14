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


class RxRateLimit(Base):
    """Limit receive bandwidth, by dropping incoming packets which exceed the limit.
    The RxRateLimit class encapsulates a required rxRateLimit resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rxRateLimit"
    _SDM_ATT_MAP = {
        "BufferSizeEnabled": "bufferSizeEnabled",
        "BufferSizeUnits": "bufferSizeUnits",
        "BufferSizeValue": "bufferSizeValue",
        "Enabled": "enabled",
        "Units": "units",
        "Value": "value",
    }
    _SDM_ENUM_MAP = {
        "bufferSizeUnits": ["kilobytes", "kKilobytes", "kMegabytes", "megabytes"],
        "units": [
            "kilobitsPerSecond",
            "kKilobitsPerSecond",
            "kMegabitsPerSecond",
            "megabitsPerSecond",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(RxRateLimit, self).__init__(parent, list_op)

    @property
    def BufferSizeEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Allows user to specify a custom buffer size. Default false
        """
        return self._get_attribute(self._SDM_ATT_MAP["BufferSizeEnabled"])

    @BufferSizeEnabled.setter
    def BufferSizeEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BufferSizeEnabled"], value)

    @property
    def BufferSizeUnits(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kilobytes | kKilobytes | kMegabytes | megabytes): Units (Kilobytes, Megabytes). Default: Kilobytes
        """
        return self._get_attribute(self._SDM_ATT_MAP["BufferSizeUnits"])

    @BufferSizeUnits.setter
    def BufferSizeUnits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BufferSizeUnits"], value)

    @property
    def BufferSizeValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Burst tolerance buffer size. Default value is 32 KB
        """
        return self._get_attribute(self._SDM_ATT_MAP["BufferSizeValue"])

    @BufferSizeValue.setter
    def BufferSizeValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BufferSizeValue"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable or disable the receive rate limit impairment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Units(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kilobitsPerSecond | kKilobitsPerSecond | kMegabitsPerSecond | megabitsPerSecond): Specify the units for the receive rate limit value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Units"])

    @Units.setter
    def Units(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Units"], value)

    @property
    def Value(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the value of the receive rate limit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Value"])

    @Value.setter
    def Value(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Value"], value)

    def update(
        self,
        BufferSizeEnabled=None,
        BufferSizeUnits=None,
        BufferSizeValue=None,
        Enabled=None,
        Units=None,
        Value=None,
    ):
        # type: (bool, str, int, bool, str, int) -> RxRateLimit
        """Updates rxRateLimit resource on the server.

        Args
        ----
        - BufferSizeEnabled (bool): Allows user to specify a custom buffer size. Default false
        - BufferSizeUnits (str(kilobytes | kKilobytes | kMegabytes | megabytes)): Units (Kilobytes, Megabytes). Default: Kilobytes
        - BufferSizeValue (number): Burst tolerance buffer size. Default value is 32 KB
        - Enabled (bool): Enable or disable the receive rate limit impairment.
        - Units (str(kilobitsPerSecond | kKilobitsPerSecond | kMegabitsPerSecond | megabitsPerSecond)): Specify the units for the receive rate limit value.
        - Value (number): Specify the value of the receive rate limit.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BufferSizeEnabled=None,
        BufferSizeUnits=None,
        BufferSizeValue=None,
        Enabled=None,
        Units=None,
        Value=None,
    ):
        # type: (bool, str, int, bool, str, int) -> RxRateLimit
        """Finds and retrieves rxRateLimit resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rxRateLimit resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rxRateLimit resources from the server.

        Args
        ----
        - BufferSizeEnabled (bool): Allows user to specify a custom buffer size. Default false
        - BufferSizeUnits (str(kilobytes | kKilobytes | kMegabytes | megabytes)): Units (Kilobytes, Megabytes). Default: Kilobytes
        - BufferSizeValue (number): Burst tolerance buffer size. Default value is 32 KB
        - Enabled (bool): Enable or disable the receive rate limit impairment.
        - Units (str(kilobitsPerSecond | kKilobitsPerSecond | kMegabitsPerSecond | megabitsPerSecond)): Specify the units for the receive rate limit value.
        - Value (number): Specify the value of the receive rate limit.

        Returns
        -------
        - self: This instance with matching rxRateLimit resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rxRateLimit data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rxRateLimit resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
