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


class AppselMatch(Base):
    """
    The AppselMatch class encapsulates a list of appselMatch resources that are managed by the system.
    A list of resources can be retrieved from the server using the AppselMatch.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "appselMatch"
    _SDM_ATT_MAP = {
        "AppSel": "appSel",
        "Link": "link",
        "ModuleHostElectricalIfName": "moduleHostElectricalIfName",
        "ModuleHostLaneCount": "moduleHostLaneCount",
        "ModuleHostLaneGroup": "moduleHostLaneGroup",
        "Note": "note",
        "PortFanouts": "portFanouts",
        "PortLaneCount": "portLaneCount",
        "PortMode": "portMode",
        "PortModulation": "portModulation",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AppselMatch, self).__init__(parent, list_op)

    @property
    def AppSel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: App Sel Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AppSel"])

    @property
    def Link(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Link: Y- yes, N- No or M- maybe for this match.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Link"])

    @property
    def ModuleHostElectricalIfName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The module specified industry standard host electrical interface string.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleHostElectricalIfName"])

    @property
    def ModuleHostLaneCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The module specified host lane count for this appsel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleHostLaneCount"])

    @property
    def ModuleHostLaneGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The number of fanouts/lane groups supported by the module host side for this appsel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleHostLaneGroup"])

    @property
    def Note(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A string describing if this AppSel is a good match for the RG speed mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Note"])

    @property
    def PortFanouts(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Number of fanouts available for the current port speed mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortFanouts"])

    @property
    def PortLaneCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The total number of lanes on host port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortLaneCount"])

    @property
    def PortMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Port speed mode for which automatic appsel match this entry is.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortMode"])

    @property
    def PortModulation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: String indicating the modulation of speed mode(PAM4, NRZ).
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortModulation"])

    def add(self):
        """Adds a new appselMatch resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved appselMatch resources using find and the newly added appselMatch resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AppSel=None,
        Link=None,
        ModuleHostElectricalIfName=None,
        ModuleHostLaneCount=None,
        ModuleHostLaneGroup=None,
        Note=None,
        PortFanouts=None,
        PortLaneCount=None,
        PortMode=None,
        PortModulation=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str) -> AppselMatch
        """Finds and retrieves appselMatch resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve appselMatch resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all appselMatch resources from the server.

        Args
        ----
        - AppSel (str): App Sel Id.
        - Link (str): Link: Y- yes, N- No or M- maybe for this match.
        - ModuleHostElectricalIfName (str): The module specified industry standard host electrical interface string.
        - ModuleHostLaneCount (str): The module specified host lane count for this appsel.
        - ModuleHostLaneGroup (str): The number of fanouts/lane groups supported by the module host side for this appsel.
        - Note (str): A string describing if this AppSel is a good match for the RG speed mode.
        - PortFanouts (str): Number of fanouts available for the current port speed mode.
        - PortLaneCount (str): The total number of lanes on host port.
        - PortMode (str): Port speed mode for which automatic appsel match this entry is.
        - PortModulation (str): String indicating the modulation of speed mode(PAM4, NRZ).

        Returns
        -------
        - self: This instance with matching appselMatch resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of appselMatch data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the appselMatch resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
