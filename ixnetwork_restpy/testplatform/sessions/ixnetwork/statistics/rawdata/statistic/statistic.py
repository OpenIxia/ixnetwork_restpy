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


class Statistic(Base):
    """Raw data statistics parameters.
    The Statistic class encapsulates a list of statistic resources that are managed by the system.
    A list of resources can be retrieved from the server using the Statistic.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "statistic"
    _SDM_ATT_MAP = {
        "Caption": "caption",
        "Enabled": "enabled",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Statistic, self).__init__(parent, list_op)

    @property
    def Caption(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Stats Caption.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Caption"])

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enabled stats for Raw Data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    def update(self, Enabled=None):
        # type: (bool) -> Statistic
        """Updates statistic resource on the server.

        Args
        ----
        - Enabled (bool): Enabled stats for Raw Data.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None):
        # type: (bool) -> Statistic
        """Adds a new statistic resource on the json, only valid with batch add utility

        Args
        ----
        - Enabled (bool): Enabled stats for Raw Data.

        Returns
        -------
        - self: This instance with all currently retrieved statistic resources using find and the newly added statistic resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Caption=None, Enabled=None):
        # type: (str, bool) -> Statistic
        """Finds and retrieves statistic resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statistic resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statistic resources from the server.

        Args
        ----
        - Caption (str): Stats Caption.
        - Enabled (bool): Enabled stats for Raw Data.

        Returns
        -------
        - self: This instance with matching statistic resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of statistic data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the statistic resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
