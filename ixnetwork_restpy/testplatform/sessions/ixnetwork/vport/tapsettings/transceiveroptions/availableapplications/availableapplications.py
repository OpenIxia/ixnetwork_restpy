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


class AvailableApplications(Base):
    """
    The AvailableApplications class encapsulates a list of availableApplications resources that are managed by the system.
    A list of resources can be retrieved from the server using the AvailableApplications.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "availableApplications"
    _SDM_ATT_MAP = {
        "AppSel": "appSel",
        "HostElectricalIfID": "hostElectricalIfID",
        "HostElectricalIfName": "hostElectricalIfName",
        "HostLaneCount": "hostLaneCount",
        "HostLaneGroup": "hostLaneGroup",
        "HostLaneSpeed": "hostLaneSpeed",
        "HostModulation": "hostModulation",
        "MediaIfID": "mediaIfID",
        "MediaIfName": "mediaIfName",
        "MediaLaneCount": "mediaLaneCount",
        "MediaLaneGroup": "mediaLaneGroup",
        "MediaLaneSpeed": "mediaLaneSpeed",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AvailableApplications, self).__init__(parent, list_op)

    @property
    def AppSel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Appsel Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AppSel"])

    @property
    def HostElectricalIfID(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The industry standard electrical interface id in hex.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostElectricalIfID"])

    @property
    def HostElectricalIfName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The industry standard host electrical interface string.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostElectricalIfName"])

    @property
    def HostLaneCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The module specified host lane count for this appsel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostLaneCount"])

    @property
    def HostLaneGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The group of lanes in a data path.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostLaneGroup"])

    @property
    def HostLaneSpeed(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The per lane speed as defined for the industry standard interface(G bit/s).
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostLaneSpeed"])

    @property
    def HostModulation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The string indicating the modulation(PAM4/NRZ).
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostModulation"])

    @property
    def MediaIfID(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The industry standard media interface id in hex.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaIfID"])

    @property
    def MediaIfName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The industry standard media interface name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaIfName"])

    @property
    def MediaLaneCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The module specified media lane count for this appsel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaLaneCount"])

    @property
    def MediaLaneGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The group of lanes in a data path.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaLaneGroup"])

    @property
    def MediaLaneSpeed(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The per lane speed as defined for the industry standard interface(G bit/s).
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaLaneSpeed"])

    def add(self):
        """Adds a new availableApplications resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved availableApplications resources using find and the newly added availableApplications resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AppSel=None,
        HostElectricalIfID=None,
        HostElectricalIfName=None,
        HostLaneCount=None,
        HostLaneGroup=None,
        HostLaneSpeed=None,
        HostModulation=None,
        MediaIfID=None,
        MediaIfName=None,
        MediaLaneCount=None,
        MediaLaneGroup=None,
        MediaLaneSpeed=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str, str, str) -> AvailableApplications
        """Finds and retrieves availableApplications resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve availableApplications resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all availableApplications resources from the server.

        Args
        ----
        - AppSel (str): Appsel Id.
        - HostElectricalIfID (str): The industry standard electrical interface id in hex.
        - HostElectricalIfName (str): The industry standard host electrical interface string.
        - HostLaneCount (str): The module specified host lane count for this appsel.
        - HostLaneGroup (str): The group of lanes in a data path.
        - HostLaneSpeed (str): The per lane speed as defined for the industry standard interface(G bit/s).
        - HostModulation (str): The string indicating the modulation(PAM4/NRZ).
        - MediaIfID (str): The industry standard media interface id in hex.
        - MediaIfName (str): The industry standard media interface name.
        - MediaLaneCount (str): The module specified media lane count for this appsel.
        - MediaLaneGroup (str): The group of lanes in a data path.
        - MediaLaneSpeed (str): The per lane speed as defined for the industry standard interface(G bit/s).

        Returns
        -------
        - self: This instance with matching availableApplications resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of availableApplications data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the availableApplications resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
