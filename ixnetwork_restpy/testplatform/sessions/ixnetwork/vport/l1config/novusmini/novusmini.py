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


class Novusmini(Base):
    """
    The Novusmini class encapsulates a required novusmini resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "novusmini"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AutoNegotiateSpeed": "autoNegotiateSpeed",
        "AvailableSpeeds": "availableSpeeds",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "Loopback": "loopback",
        "Mtu": "mtu",
        "NegotiatePrimarySecondary": "negotiatePrimarySecondary",
        "PrimarySecondaryMode": "primarySecondaryMode",
        "SelectedSpeeds": "selectedSpeeds",
        "Speed": "speed",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "primarySecondaryMode": ["primary", "secondary"],
        "speed": ["speed1000", "speed100fd", "speed10fd", "speed10hd", "speed2.5g"],
    }

    def __init__(self, parent, list_op=False):
        super(Novusmini, self).__init__(parent, list_op)

    @property
    def AutoInstrumentation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoInstrumentation"])

    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoInstrumentation"], value)

    @property
    def AutoNegotiateSpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, allows auto-negotiation between ports for speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoNegotiateSpeed"])

    @AutoNegotiateSpeed.setter
    def AutoNegotiateSpeed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoNegotiateSpeed"], value)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed1000 | speed2.5g]): Which speeds are available for the current media and AN settings.
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
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopback"])

    @property
    def Mtu(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mtu"])

    @Mtu.setter
    def Mtu(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mtu"], value)

    @property
    def NegotiatePrimarySecondary(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatePrimarySecondary"])

    @NegotiatePrimarySecondary.setter
    def NegotiatePrimarySecondary(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NegotiatePrimarySecondary"], value)

    @property
    def PrimarySecondaryMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(primary | secondary):
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrimarySecondaryMode"])

    @PrimarySecondaryMode.setter
    def PrimarySecondaryMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrimarySecondaryMode"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed1000 | speed2.5g]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed1000 | speed100fd | speed10fd | speed10hd | speed2.5g): Select one of the enums to set the speed of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Speed"])

    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Speed"], value)

    def update(
        self,
        AutoInstrumentation=None,
        AutoNegotiateSpeed=None,
        Mtu=None,
        NegotiatePrimarySecondary=None,
        PrimarySecondaryMode=None,
        SelectedSpeeds=None,
        Speed=None,
    ):
        # type: (str, bool, int, bool, str, List[str], str) -> Novusmini
        """Updates novusmini resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiateSpeed (bool): If enabled, allows auto-negotiation between ports for speed.
        - Mtu (number):
        - NegotiatePrimarySecondary (bool):
        - PrimarySecondaryMode (str(primary | secondary)):
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed1000 | speed2.5g])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed1000 | speed100fd | speed10fd | speed10hd | speed2.5g)): Select one of the enums to set the speed of the port.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AutoNegotiateSpeed=None,
        AvailableSpeeds=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        Loopback=None,
        Mtu=None,
        NegotiatePrimarySecondary=None,
        PrimarySecondaryMode=None,
        SelectedSpeeds=None,
        Speed=None,
    ):
        # type: (str, bool, List[str], bool, bool, bool, int, bool, str, List[str], str) -> Novusmini
        """Finds and retrieves novusmini resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve novusmini resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all novusmini resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiateSpeed (bool): If enabled, allows auto-negotiation between ports for speed.
        - AvailableSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed1000 | speed2.5g])): Which speeds are available for the current media and AN settings.
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - Mtu (number):
        - NegotiatePrimarySecondary (bool):
        - PrimarySecondaryMode (str(primary | secondary)):
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed1000 | speed2.5g])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed1000 | speed100fd | speed10fd | speed10hd | speed2.5g)): Select one of the enums to set the speed of the port.

        Returns
        -------
        - self: This instance with matching novusmini resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of novusmini data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the novusmini resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
