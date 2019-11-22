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


class DhcpServerGlobals(Base):
    """Global settings placeholder for DHCPServerPlugin.
    The DhcpServerGlobals class encapsulates a list of dhcpServerGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the DhcpServerGlobals.find() method.
    The list can be managed by the user by using the DhcpServerGlobals.add() and DhcpServerGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpServerGlobals'

    def __init__(self, parent):
        super(DhcpServerGlobals, self).__init__(parent)

    @property
    def DefaultLeaseTime(self):
        """The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.

        Returns:
            number
        """
        return self._get_attribute('defaultLeaseTime')
    @DefaultLeaseTime.setter
    def DefaultLeaseTime(self, value):
        self._set_attribute('defaultLeaseTime', value)

    @property
    def MaxLeaseTime(self):
        """The maximum Life Time length in seconds that will be assigned to a lease.

        Returns:
            number
        """
        return self._get_attribute('maxLeaseTime')
    @MaxLeaseTime.setter
    def MaxLeaseTime(self, value):
        self._set_attribute('maxLeaseTime', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PingCheck(self):
        """When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.

        Returns:
            bool
        """
        return self._get_attribute('pingCheck')
    @PingCheck.setter
    def PingCheck(self, value):
        self._set_attribute('pingCheck', value)

    @property
    def PingTimeout(self):
        """The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.

        Returns:
            number
        """
        return self._get_attribute('pingTimeout')
    @PingTimeout.setter
    def PingTimeout(self, value):
        self._set_attribute('pingTimeout', value)

    @property
    def SharedNetwork(self):
        """When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Returns:
            bool
        """
        return self._get_attribute('sharedNetwork')
    @SharedNetwork.setter
    def SharedNetwork(self, value):
        self._set_attribute('sharedNetwork', value)

    def update(self, DefaultLeaseTime=None, MaxLeaseTime=None, PingCheck=None, PingTimeout=None, SharedNetwork=None):
        """Updates a child instance of dhcpServerGlobals on the server.

        Args:
            DefaultLeaseTime (number): The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
            MaxLeaseTime (number): The maximum Life Time length in seconds that will be assigned to a lease.
            PingCheck (bool): When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
            PingTimeout (number): The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
            SharedNetwork (bool): When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, DefaultLeaseTime=None, MaxLeaseTime=None, PingCheck=None, PingTimeout=None, SharedNetwork=None):
        """Adds a new dhcpServerGlobals node on the server and retrieves it in this instance.

        Args:
            DefaultLeaseTime (number): The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
            MaxLeaseTime (number): The maximum Life Time length in seconds that will be assigned to a lease.
            PingCheck (bool): When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
            PingTimeout (number): The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
            SharedNetwork (bool): When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Returns:
            self: This instance with all currently retrieved dhcpServerGlobals data using find and the newly added dhcpServerGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpServerGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DefaultLeaseTime=None, MaxLeaseTime=None, ObjectId=None, PingCheck=None, PingTimeout=None, SharedNetwork=None):
        """Finds and retrieves dhcpServerGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpServerGlobals data from the server.
        By default the find method takes no parameters and will retrieve all dhcpServerGlobals data from the server.

        Args:
            DefaultLeaseTime (number): The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
            MaxLeaseTime (number): The maximum Life Time length in seconds that will be assigned to a lease.
            ObjectId (str): Unique identifier for this object
            PingCheck (bool): When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
            PingTimeout (number): The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
            SharedNetwork (bool): When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Returns:
            self: This instance with matching dhcpServerGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpServerGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpServerGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
