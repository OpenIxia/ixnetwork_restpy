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


class Dhcpv6ClientGlobals(Base):
    """Global settings placeholder for DHCPPlugin.
    The Dhcpv6ClientGlobals class encapsulates a list of dhcpv6ClientGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6ClientGlobals.find() method.
    The list can be managed by the user by using the Dhcpv6ClientGlobals.add() and Dhcpv6ClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6ClientGlobals'

    def __init__(self, parent):
        super(Dhcpv6ClientGlobals, self).__init__(parent)

    @property
    def Dhcp6InfMaxRc(self):
        """The maximum information-request retry attempts.

        Returns:
            number
        """
        return self._get_attribute('dhcp6InfMaxRc')
    @Dhcp6InfMaxRc.setter
    def Dhcp6InfMaxRc(self, value):
        self._set_attribute('dhcp6InfMaxRc', value)

    @property
    def Dhcp6InfMaxRt(self):
        """RFC 3315 maximum information-request timeout value, in seconds.

        Returns:
            number
        """
        return self._get_attribute('dhcp6InfMaxRt')
    @Dhcp6InfMaxRt.setter
    def Dhcp6InfMaxRt(self, value):
        self._set_attribute('dhcp6InfMaxRt', value)

    @property
    def Dhcp6InfTimeout(self):
        """RFC 3315 Initial information-request timeout, in seconds.

        Returns:
            number
        """
        return self._get_attribute('dhcp6InfTimeout')
    @Dhcp6InfTimeout.setter
    def Dhcp6InfTimeout(self, value):
        self._set_attribute('dhcp6InfTimeout', value)

    @property
    def MaxOutstandingRequests(self):
        """This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def SetupRateIncrement(self):
        """This value represents the increment value for setup rate. This value is applied every second and can be negative.

        Returns:
            number
        """
        return self._get_attribute('setupRateIncrement')
    @SetupRateIncrement.setter
    def SetupRateIncrement(self, value):
        self._set_attribute('setupRateIncrement', value)

    @property
    def SetupRateInitial(self):
        """Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def SetupRateMax(self):
        """This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Returns:
            number
        """
        return self._get_attribute('setupRateMax')
    @SetupRateMax.setter
    def SetupRateMax(self, value):
        self._set_attribute('setupRateMax', value)

    def update(self, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, MaxOutstandingRequests=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None):
        """Updates a child instance of dhcpv6ClientGlobals on the server.

        Args:
            Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
            Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
            Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
            MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            SetupRateIncrement (number): This value represents the increment value for setup rate. This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, MaxOutstandingRequests=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None):
        """Adds a new dhcpv6ClientGlobals node on the server and retrieves it in this instance.

        Args:
            Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
            Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
            Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
            MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            SetupRateIncrement (number): This value represents the increment value for setup rate. This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Returns:
            self: This instance with all currently retrieved dhcpv6ClientGlobals data using find and the newly added dhcpv6ClientGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpv6ClientGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, MaxOutstandingRequests=None, ObjectId=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None):
        """Finds and retrieves dhcpv6ClientGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpv6ClientGlobals data from the server.
        By default the find method takes no parameters and will retrieve all dhcpv6ClientGlobals data from the server.

        Args:
            Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
            Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
            Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
            MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            ObjectId (str): Unique identifier for this object
            SetupRateIncrement (number): This value represents the increment value for setup rate. This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Returns:
            self: This instance with matching dhcpv6ClientGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpv6ClientGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpv6ClientGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
