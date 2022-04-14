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
    """DEPRECATED
    The Statistic class encapsulates a list of statistic resources that are managed by the user.
    A list of resources can be retrieved from the server using the Statistic.find() method.
    The list can be managed by using the Statistic.add() and Statistic.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "statistic"
    _SDM_ATT_MAP = {
        "Enable": "enable",
        "Name": "name",
        "Notes": "notes",
        "Operator": "operator",
        "Unit": "unit",
        "Value": "value",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Statistic, self).__init__(parent, list_op)

    @property
    def Enable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable monitoring for the current statistic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enable"])

    @Enable.setter
    def Enable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enable"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the statistic that is being monitored.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @property
    def Notes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Additional notes that explain what is being monitored for this statistic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Notes"])

    @property
    def Operator(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The operator that is being used to compare the actual value of the statistic with the configured threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Operator"])

    @property
    def Unit(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The measurement unit being used for this statistic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Unit"])

    @property
    def Value(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The threshold for the current statistic. Exceeding this value will trigger a warning if monitoring is enabled for this statistic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Value"])

    @Value.setter
    def Value(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Value"], value)

    def update(self, Enable=None, Value=None):
        # type: (bool, int) -> Statistic
        """Updates statistic resource on the server.

        Args
        ----
        - Enable (bool): Enable/Disable monitoring for the current statistic.
        - Value (number): The threshold for the current statistic. Exceeding this value will trigger a warning if monitoring is enabled for this statistic.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enable=None, Value=None):
        # type: (bool, int) -> Statistic
        """Adds a new statistic resource on the server and adds it to the container.

        Args
        ----
        - Enable (bool): Enable/Disable monitoring for the current statistic.
        - Value (number): The threshold for the current statistic. Exceeding this value will trigger a warning if monitoring is enabled for this statistic.

        Returns
        -------
        - self: This instance with all currently retrieved statistic resources using find and the newly added statistic resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained statistic resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self, Enable=None, Name=None, Notes=None, Operator=None, Unit=None, Value=None
    ):
        # type: (bool, str, str, str, str, int) -> Statistic
        """Finds and retrieves statistic resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statistic resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statistic resources from the server.

        Args
        ----
        - Enable (bool): Enable/Disable monitoring for the current statistic.
        - Name (str): The name of the statistic that is being monitored.
        - Notes (str): Additional notes that explain what is being monitored for this statistic.
        - Operator (str): The operator that is being used to compare the actual value of the statistic with the configured threshold.
        - Unit (str): The measurement unit being used for this statistic.
        - Value (number): The threshold for the current statistic. Exceeding this value will trigger a warning if monitoring is enabled for this statistic.

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
