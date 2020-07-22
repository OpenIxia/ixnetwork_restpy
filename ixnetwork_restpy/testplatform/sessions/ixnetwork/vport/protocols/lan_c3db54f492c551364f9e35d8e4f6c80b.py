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


class Lan(Base):
    """A set of STP LANs to be included in stpServer.
    The Lan class encapsulates a list of lan resources that are managed by the user.
    A list of resources can be retrieved from the server using the Lan.find() method.
    The list can be managed by using the Lan.add() and Lan.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lan'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'MacAddress': 'macAddress',
        'MacCount': 'macCount',
        'MacIncrement': 'macIncrement',
        'TrafficGroupId': 'trafficGroupId',
        'VlanEnabled': 'vlanEnabled',
        'VlanId': 'vlanId',
        'VlanIncrement': 'vlanIncrement',
    }

    def __init__(self, parent):
        super(Lan, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the STP LAN.
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
        - str: The first 6-byte MAC Address in the range. (default = 00:00:00:00:00:00)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def MacCount(self):
        """
        Returns
        -------
        - number: The number of MAC addresses in the LAN range. The valid range is 1 to 500. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacCount'])
    @MacCount.setter
    def MacCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacCount'], value)

    @property
    def MacIncrement(self):
        """
        Returns
        -------
        - bool: If enabled, a 6-byte increment value will be added for each additional MAC address to create a range of MAC addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacIncrement'])
    @MacIncrement.setter
    def MacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacIncrement'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): References a traffic group identifier as configured by the trafficGroup object.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def VlanEnabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this STP LAN. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanEnabled'])
    @VlanEnabled.setter
    def VlanEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanEnabled'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: The identifier for the first VLAN in the range. Valid range: 1 to 4094.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanIncrement(self):
        """
        Returns
        -------
        - bool: If enabled, an increment value will be added for each additional VLAN to create a range of MAC addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIncrement'])
    @VlanIncrement.setter
    def VlanIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIncrement'], value)

    def update(self, Enabled=None, MacAddress=None, MacCount=None, MacIncrement=None, TrafficGroupId=None, VlanEnabled=None, VlanId=None, VlanIncrement=None):
        """Updates lan resource on the server.

        Args
        ----
        - Enabled (bool): Enables the use of the STP LAN.
        - MacAddress (str): The first 6-byte MAC Address in the range. (default = 00:00:00:00:00:00)
        - MacCount (number): The number of MAC addresses in the LAN range. The valid range is 1 to 500. (default = 1)
        - MacIncrement (bool): If enabled, a 6-byte increment value will be added for each additional MAC address to create a range of MAC addresses.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): References a traffic group identifier as configured by the trafficGroup object.
        - VlanEnabled (bool): Enables the use of this STP LAN. (default = disabled)
        - VlanId (number): The identifier for the first VLAN in the range. Valid range: 1 to 4094.
        - VlanIncrement (bool): If enabled, an increment value will be added for each additional VLAN to create a range of MAC addresses.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, MacAddress=None, MacCount=None, MacIncrement=None, TrafficGroupId=None, VlanEnabled=None, VlanId=None, VlanIncrement=None):
        """Adds a new lan resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the use of the STP LAN.
        - MacAddress (str): The first 6-byte MAC Address in the range. (default = 00:00:00:00:00:00)
        - MacCount (number): The number of MAC addresses in the LAN range. The valid range is 1 to 500. (default = 1)
        - MacIncrement (bool): If enabled, a 6-byte increment value will be added for each additional MAC address to create a range of MAC addresses.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): References a traffic group identifier as configured by the trafficGroup object.
        - VlanEnabled (bool): Enables the use of this STP LAN. (default = disabled)
        - VlanId (number): The identifier for the first VLAN in the range. Valid range: 1 to 4094.
        - VlanIncrement (bool): If enabled, an increment value will be added for each additional VLAN to create a range of MAC addresses.

        Returns
        -------
        - self: This instance with all currently retrieved lan resources using find and the newly added lan resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained lan resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, MacAddress=None, MacCount=None, MacIncrement=None, TrafficGroupId=None, VlanEnabled=None, VlanId=None, VlanIncrement=None):
        """Finds and retrieves lan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lan resources from the server.

        Args
        ----
        - Enabled (bool): Enables the use of the STP LAN.
        - MacAddress (str): The first 6-byte MAC Address in the range. (default = 00:00:00:00:00:00)
        - MacCount (number): The number of MAC addresses in the LAN range. The valid range is 1 to 500. (default = 1)
        - MacIncrement (bool): If enabled, a 6-byte increment value will be added for each additional MAC address to create a range of MAC addresses.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): References a traffic group identifier as configured by the trafficGroup object.
        - VlanEnabled (bool): Enables the use of this STP LAN. (default = disabled)
        - VlanId (number): The identifier for the first VLAN in the range. Valid range: 1 to 4094.
        - VlanIncrement (bool): If enabled, an increment value will be added for each additional VLAN to create a range of MAC addresses.

        Returns
        -------
        - self: This instance with matching lan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
