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


class Flapping(Base):
    """This object controls route flapping for the route range.
    The Flapping class encapsulates a required flapping resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "flapping"
    _SDM_ATT_MAP = {
        "Delay": "delay",
        "DownTime": "downTime",
        "EnablePartialFlap": "enablePartialFlap",
        "Enabled": "enabled",
        "RoutesToFlapFrom": "routesToFlapFrom",
        "RoutesToFlapTo": "routesToFlapTo",
        "UpTime": "upTime",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Flapping, self).__init__(parent, list_op)

    @property
    def Delay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The setting for a timer that must elapse before a route range is advertised. It allows the user to specify a pause time between the sending of route ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Delay"])

    @Delay.setter
    def Delay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Delay"], value)

    @property
    def DownTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: During flapping, the amount of time during which the routes in the route range are withdrawn/down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownTime"])

    @DownTime.setter
    def DownTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownTime"], value)

    @property
    def EnablePartialFlap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables partial flapping, based on the Flap From and To Route Index settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePartialFlap"])

    @EnablePartialFlap.setter
    def EnablePartialFlap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePartialFlap"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables route flapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def RoutesToFlapFrom(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The index of the first generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesToFlapFrom"])

    @RoutesToFlapFrom.setter
    def RoutesToFlapFrom(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesToFlapFrom"], value)

    @property
    def RoutesToFlapTo(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The index of the last generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesToFlapTo"])

    @RoutesToFlapTo.setter
    def RoutesToFlapTo(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesToFlapTo"], value)

    @property
    def UpTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: During flapping, the amount of time during which the routes in the route range are up.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpTime"])

    @UpTime.setter
    def UpTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpTime"], value)

    def update(
        self,
        Delay=None,
        DownTime=None,
        EnablePartialFlap=None,
        Enabled=None,
        RoutesToFlapFrom=None,
        RoutesToFlapTo=None,
        UpTime=None,
    ):
        # type: (int, int, bool, bool, int, int, int) -> Flapping
        """Updates flapping resource on the server.

        Args
        ----
        - Delay (number): The setting for a timer that must elapse before a route range is advertised. It allows the user to specify a pause time between the sending of route ranges.
        - DownTime (number): During flapping, the amount of time during which the routes in the route range are withdrawn/down.
        - EnablePartialFlap (bool): Enables partial flapping, based on the Flap From and To Route Index settings.
        - Enabled (bool): If true, enables route flapping.
        - RoutesToFlapFrom (number): The index of the first generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
        - RoutesToFlapTo (number): The index of the last generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
        - UpTime (number): During flapping, the amount of time during which the routes in the route range are up.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Delay=None,
        DownTime=None,
        EnablePartialFlap=None,
        Enabled=None,
        RoutesToFlapFrom=None,
        RoutesToFlapTo=None,
        UpTime=None,
    ):
        # type: (int, int, bool, bool, int, int, int) -> Flapping
        """Finds and retrieves flapping resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flapping resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flapping resources from the server.

        Args
        ----
        - Delay (number): The setting for a timer that must elapse before a route range is advertised. It allows the user to specify a pause time between the sending of route ranges.
        - DownTime (number): During flapping, the amount of time during which the routes in the route range are withdrawn/down.
        - EnablePartialFlap (bool): Enables partial flapping, based on the Flap From and To Route Index settings.
        - Enabled (bool): If true, enables route flapping.
        - RoutesToFlapFrom (number): The index of the first generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
        - RoutesToFlapTo (number): The index of the last generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
        - UpTime (number): During flapping, the amount of time during which the routes in the route range are up.

        Returns
        -------
        - self: This instance with matching flapping resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flapping data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flapping resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
