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


class Dcc(Base):
    """The Layer 1 Configuration is being configured for a POS port and DCC is selected as the Payload Type.
    The Dcc class encapsulates a required dcc resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dcc"
    _SDM_ATT_MAP = {
        "AvailableSpeeds": "availableSpeeds",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "Crc": "crc",
        "OverheadByte": "overheadByte",
        "SelectedSpeeds": "selectedSpeeds",
        "TimeFill": "timeFill",
    }
    _SDM_ENUM_MAP = {
        "crc": ["crc16", "crc32"],
        "overheadByte": ["loh", "soh"],
        "timeFill": ["flag7E", "markIdle"],
    }

    def __init__(self, parent, list_op=False):
        super(Dcc, self).__init__(parent, list_op)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def CanModifySpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanModifySpeed"])

    @property
    def CanSetMultipleSpeeds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanSetMultipleSpeeds"])

    @property
    def Crc(self):
        # type: () -> str
        """
        Returns
        -------
        - str(crc16 | crc32): Choose the type of Cyclic Redundancy Check to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Crc"])

    @Crc.setter
    def Crc(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Crc"], value)

    @property
    def OverheadByte(self):
        # type: () -> str
        """
        Returns
        -------
        - str(loh | soh): Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverheadByte"])

    @OverheadByte.setter
    def OverheadByte(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverheadByte"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def TimeFill(self):
        # type: () -> str
        """
        Returns
        -------
        - str(flag7E | markIdle): Choose the type of bytes used to fill the gaps between DCC frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimeFill"])

    @TimeFill.setter
    def TimeFill(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimeFill"], value)

    def update(self, Crc=None, OverheadByte=None, SelectedSpeeds=None, TimeFill=None):
        # type: (str, str, List[str], str) -> Dcc
        """Updates dcc resource on the server.

        Args
        ----
        - Crc (str(crc16 | crc32)): Choose the type of Cyclic Redundancy Check to be used.
        - OverheadByte (str(loh | soh)): Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TimeFill (str(flag7E | markIdle)): Choose the type of bytes used to fill the gaps between DCC frames.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableSpeeds=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        Crc=None,
        OverheadByte=None,
        SelectedSpeeds=None,
        TimeFill=None,
    ):
        # type: (List[str], bool, bool, str, str, List[str], str) -> Dcc
        """Finds and retrieves dcc resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcc resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcc resources from the server.

        Args
        ----
        - AvailableSpeeds (list(str[])): Which speeds are available for the current media and AN settings.
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - Crc (str(crc16 | crc32)): Choose the type of Cyclic Redundancy Check to be used.
        - OverheadByte (str(loh | soh)): Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TimeFill (str(flag7E | markIdle)): Choose the type of bytes used to fill the gaps between DCC frames.

        Returns
        -------
        - self: This instance with matching dcc resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcc data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcc resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
