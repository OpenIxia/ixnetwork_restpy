# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class SwitchHostRanges(Base):
    """The Swicth Host Ranges window describes the switch Host Ranges and its configuration parameters. This window is available for Switch configuration only. When the user selects a column in the grid view, the entire composite column break-up appears in a split pane. When a user selects a non-composite cell or column in the grid, like, Enable, the Preview pane displays empty cells for all the rows.
    The SwitchHostRanges class encapsulates a list of switchHostRanges resources that is be managed by the user.
    A list of resources can be retrieved from the server using the SwitchHostRanges.find() method.
    The list can be managed by the user by using the SwitchHostRanges.add() and SwitchHostRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchHostRanges'

    def __init__(self, parent):
        super(SwitchHostRanges, self).__init__(parent)

    @property
    def EnableStaticIp(self):
        """If selected, Host Static IPv4 Address is available for change. It indicates if static IP will be configured in simulated Host.

        Returns:
            bool
        """
        return self._get_attribute('enableStaticIp')
    @EnableStaticIp.setter
    def EnableStaticIp(self, value):
        self._set_attribute('enableStaticIp', value)

    @property
    def EnableVlan(self):
        """If selected, Host VLAN ID is available for change. It indicates if VLAN will be configured in Host.

        Returns:
            bool
        """
        return self._get_attribute('enableVlan')
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute('enableVlan', value)

    @property
    def Enabled(self):
        """If selected, the Host Range gets configured in the switch.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def HostMacAddress(self):
        """The MAC Address of the simulated Host. The composite column break-up appears in a split pane on the right.

        Returns:
            str
        """
        return self._get_attribute('hostMacAddress')
    @HostMacAddress.setter
    def HostMacAddress(self, value):
        self._set_attribute('hostMacAddress', value)

    @property
    def HostStaticIpv4Address(self):
        """The static IPv4 Address of the Host. This is available only if Enable Static IP is selected. The composite column break-up appears in a split pane on the right.

        Returns:
            str
        """
        return self._get_attribute('hostStaticIpv4Address')
    @HostStaticIpv4Address.setter
    def HostStaticIpv4Address(self, value):
        self._set_attribute('hostStaticIpv4Address', value)

    @property
    def HostVlanid(self):
        """The VLAN ID of the Host. This is available only if Enable VLAN is selected. The composite column break-up appears in a split pane on the right.

        Returns:
            str
        """
        return self._get_attribute('hostVlanid')
    @HostVlanid.setter
    def HostVlanid(self, value):
        self._set_attribute('hostVlanid', value)

    @property
    def NumberOfHostsPerPort(self):
        """Specify the number of switches to be configured for every switch port.

        Returns:
            number
        """
        return self._get_attribute('numberOfHostsPerPort')
    @NumberOfHostsPerPort.setter
    def NumberOfHostsPerPort(self, value):
        self._set_attribute('numberOfHostsPerPort', value)

    def update(self, EnableStaticIp=None, EnableVlan=None, Enabled=None, HostMacAddress=None, HostStaticIpv4Address=None, HostVlanid=None, NumberOfHostsPerPort=None):
        """Updates a child instance of switchHostRanges on the server.

        Args:
            EnableStaticIp (bool): If selected, Host Static IPv4 Address is available for change. It indicates if static IP will be configured in simulated Host.
            EnableVlan (bool): If selected, Host VLAN ID is available for change. It indicates if VLAN will be configured in Host.
            Enabled (bool): If selected, the Host Range gets configured in the switch.
            HostMacAddress (str): The MAC Address of the simulated Host. The composite column break-up appears in a split pane on the right.
            HostStaticIpv4Address (str): The static IPv4 Address of the Host. This is available only if Enable Static IP is selected. The composite column break-up appears in a split pane on the right.
            HostVlanid (str): The VLAN ID of the Host. This is available only if Enable VLAN is selected. The composite column break-up appears in a split pane on the right.
            NumberOfHostsPerPort (number): Specify the number of switches to be configured for every switch port.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, EnableStaticIp=None, EnableVlan=None, Enabled=None, HostMacAddress=None, HostStaticIpv4Address=None, HostVlanid=None, NumberOfHostsPerPort=None):
        """Adds a new switchHostRanges node on the server and retrieves it in this instance.

        Args:
            EnableStaticIp (bool): If selected, Host Static IPv4 Address is available for change. It indicates if static IP will be configured in simulated Host.
            EnableVlan (bool): If selected, Host VLAN ID is available for change. It indicates if VLAN will be configured in Host.
            Enabled (bool): If selected, the Host Range gets configured in the switch.
            HostMacAddress (str): The MAC Address of the simulated Host. The composite column break-up appears in a split pane on the right.
            HostStaticIpv4Address (str): The static IPv4 Address of the Host. This is available only if Enable Static IP is selected. The composite column break-up appears in a split pane on the right.
            HostVlanid (str): The VLAN ID of the Host. This is available only if Enable VLAN is selected. The composite column break-up appears in a split pane on the right.
            NumberOfHostsPerPort (number): Specify the number of switches to be configured for every switch port.

        Returns:
            self: This instance with all currently retrieved switchHostRanges data using find and the newly added switchHostRanges data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the switchHostRanges data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableStaticIp=None, EnableVlan=None, Enabled=None, HostMacAddress=None, HostStaticIpv4Address=None, HostVlanid=None, NumberOfHostsPerPort=None):
        """Finds and retrieves switchHostRanges data from the server.

        All named parameters support regex and can be used to selectively retrieve switchHostRanges data from the server.
        By default the find method takes no parameters and will retrieve all switchHostRanges data from the server.

        Args:
            EnableStaticIp (bool): If selected, Host Static IPv4 Address is available for change. It indicates if static IP will be configured in simulated Host.
            EnableVlan (bool): If selected, Host VLAN ID is available for change. It indicates if VLAN will be configured in Host.
            Enabled (bool): If selected, the Host Range gets configured in the switch.
            HostMacAddress (str): The MAC Address of the simulated Host. The composite column break-up appears in a split pane on the right.
            HostStaticIpv4Address (str): The static IPv4 Address of the Host. This is available only if Enable Static IP is selected. The composite column break-up appears in a split pane on the right.
            HostVlanid (str): The VLAN ID of the Host. This is available only if Enable VLAN is selected. The composite column break-up appears in a split pane on the right.
            NumberOfHostsPerPort (number): Specify the number of switches to be configured for every switch port.

        Returns:
            self: This instance with matching switchHostRanges data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of switchHostRanges data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the switchHostRanges data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
