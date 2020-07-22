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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MacRanges(Base):
    """This object contains the MAC range configuration.
    The MacRanges class encapsulates a list of macRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the MacRanges.find() method.
    The list can be managed by using the MacRanges.add() and MacRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macRanges'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Enabled': 'enabled',
        'MacAddress': 'macAddress',
        'Step': 'step',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(MacRanges, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of times to increment in this MAC range, starting with the address set in macAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the MAC range is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - str: The MAC address of the first entry in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - str: The amount to increment each MAC address in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): Assigns a traffic group to the MAC range. The traffic group must be previously configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, Count=None, Enabled=None, MacAddress=None, Step=None, TrafficGroupId=None):
        """Updates macRanges resource on the server.

        Args
        ----
        - Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
        - Enabled (bool): If true, the MAC range is enabled.
        - MacAddress (str): The MAC address of the first entry in the range.
        - Step (str): The amount to increment each MAC address in the range.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, Enabled=None, MacAddress=None, Step=None, TrafficGroupId=None):
        """Adds a new macRanges resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
        - Enabled (bool): If true, the MAC range is enabled.
        - MacAddress (str): The MAC address of the first entry in the range.
        - Step (str): The amount to increment each MAC address in the range.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.

        Returns
        -------
        - self: This instance with all currently retrieved macRanges resources using find and the newly added macRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Enabled=None, MacAddress=None, Step=None, TrafficGroupId=None):
        """Finds and retrieves macRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macRanges resources from the server.

        Args
        ----
        - Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
        - Enabled (bool): If true, the MAC range is enabled.
        - MacAddress (str): The MAC address of the first entry in the range.
        - Step (str): The amount to increment each MAC address in the range.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.

        Returns
        -------
        - self: This instance with matching macRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
