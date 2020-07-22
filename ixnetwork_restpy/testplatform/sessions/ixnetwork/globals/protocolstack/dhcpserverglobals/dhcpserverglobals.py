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


class DhcpServerGlobals(Base):
    """Global settings placeholder for DHCPServerPlugin.
    The DhcpServerGlobals class encapsulates a list of dhcpServerGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the DhcpServerGlobals.find() method.
    The list can be managed by using the DhcpServerGlobals.add() and DhcpServerGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpServerGlobals'
    _SDM_ATT_MAP = {
        'DefaultLeaseTime': 'defaultLeaseTime',
        'MaxLeaseTime': 'maxLeaseTime',
        'ObjectId': 'objectId',
        'PingCheck': 'pingCheck',
        'PingTimeout': 'pingTimeout',
        'SharedNetwork': 'sharedNetwork',
    }

    def __init__(self, parent):
        super(DhcpServerGlobals, self).__init__(parent)

    @property
    def DefaultLeaseTime(self):
        """
        Returns
        -------
        - number: The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultLeaseTime'])
    @DefaultLeaseTime.setter
    def DefaultLeaseTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DefaultLeaseTime'], value)

    @property
    def MaxLeaseTime(self):
        """
        Returns
        -------
        - number: The maximum Life Time length in seconds that will be assigned to a lease.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxLeaseTime'])
    @MaxLeaseTime.setter
    def MaxLeaseTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxLeaseTime'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PingCheck(self):
        """
        Returns
        -------
        - bool: When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingCheck'])
    @PingCheck.setter
    def PingCheck(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PingCheck'], value)

    @property
    def PingTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PingTimeout'])
    @PingTimeout.setter
    def PingTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PingTimeout'], value)

    @property
    def SharedNetwork(self):
        """
        Returns
        -------
        - bool: When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SharedNetwork'])
    @SharedNetwork.setter
    def SharedNetwork(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SharedNetwork'], value)

    def update(self, DefaultLeaseTime=None, MaxLeaseTime=None, PingCheck=None, PingTimeout=None, SharedNetwork=None):
        """Updates dhcpServerGlobals resource on the server.

        Args
        ----
        - DefaultLeaseTime (number): The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
        - MaxLeaseTime (number): The maximum Life Time length in seconds that will be assigned to a lease.
        - PingCheck (bool): When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
        - PingTimeout (number): The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
        - SharedNetwork (bool): When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DefaultLeaseTime=None, MaxLeaseTime=None, PingCheck=None, PingTimeout=None, SharedNetwork=None):
        """Adds a new dhcpServerGlobals resource on the server and adds it to the container.

        Args
        ----
        - DefaultLeaseTime (number): The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
        - MaxLeaseTime (number): The maximum Life Time length in seconds that will be assigned to a lease.
        - PingCheck (bool): When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
        - PingTimeout (number): The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
        - SharedNetwork (bool): When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpServerGlobals resources using find and the newly added dhcpServerGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpServerGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DefaultLeaseTime=None, MaxLeaseTime=None, ObjectId=None, PingCheck=None, PingTimeout=None, SharedNetwork=None):
        """Finds and retrieves dhcpServerGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpServerGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpServerGlobals resources from the server.

        Args
        ----
        - DefaultLeaseTime (number): The Life Time length in seconds that will be assigned to a leaseif the requesting DHCP Client does not specify a specific expiration time.
        - MaxLeaseTime (number): The maximum Life Time length in seconds that will be assigned to a lease.
        - ObjectId (str): Unique identifier for this object
        - PingCheck (bool): When enabled, the DHCP Server will not assign IP addresses that areresponding to ICMP echo requests (PING) within a certain time period.
        - PingTimeout (number): The number of seconds the DHCP Server will wait for anICMP Echo response before assigning the address.
        - SharedNetwork (bool): When enabled, the DHCP leases are collected into a common pool and assignedto clients as needed. Consider this option when the number of address poolsis large and the interface on which the lease is issued is not important.

        Returns
        -------
        - self: This instance with matching dhcpServerGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpServerGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpServerGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
