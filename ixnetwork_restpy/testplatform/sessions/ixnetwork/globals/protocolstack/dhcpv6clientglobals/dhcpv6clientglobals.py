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


class Dhcpv6ClientGlobals(Base):
    """Global settings placeholder for DHCPPlugin.
    The Dhcpv6ClientGlobals class encapsulates a list of dhcpv6ClientGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6ClientGlobals.find() method.
    The list can be managed by using the Dhcpv6ClientGlobals.add() and Dhcpv6ClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6ClientGlobals'
    _SDM_ATT_MAP = {
        'Dhcp6InfMaxRc': 'dhcp6InfMaxRc',
        'Dhcp6InfMaxRt': 'dhcp6InfMaxRt',
        'Dhcp6InfTimeout': 'dhcp6InfTimeout',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'ObjectId': 'objectId',
        'SetupRateIncrement': 'setupRateIncrement',
        'SetupRateInitial': 'setupRateInitial',
        'SetupRateMax': 'setupRateMax',
    }

    def __init__(self, parent):
        super(Dhcpv6ClientGlobals, self).__init__(parent)

    @property
    def Dhcp6InfMaxRc(self):
        """
        Returns
        -------
        - number: The maximum information-request retry attempts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRc'])
    @Dhcp6InfMaxRc.setter
    def Dhcp6InfMaxRc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRc'], value)

    @property
    def Dhcp6InfMaxRt(self):
        """
        Returns
        -------
        - number: RFC 3315 maximum information-request timeout value, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRt'])
    @Dhcp6InfMaxRt.setter
    def Dhcp6InfMaxRt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRt'], value)

    @property
    def Dhcp6InfTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial information-request timeout, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfTimeout'])
    @Dhcp6InfTimeout.setter
    def Dhcp6InfTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6InfTimeout'], value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'])
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SetupRateIncrement(self):
        """
        Returns
        -------
        - number: This value represents the increment value for setup rate. This value is applied every second and can be negative.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateIncrement'])
    @SetupRateIncrement.setter
    def SetupRateIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateIncrement'], value)

    @property
    def SetupRateInitial(self):
        """
        Returns
        -------
        - number: Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateInitial'])
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateInitial'], value)

    @property
    def SetupRateMax(self):
        """
        Returns
        -------
        - number: This value represents the final value for setup rate. The setup rate will not change after this value is reached.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateMax'])
    @SetupRateMax.setter
    def SetupRateMax(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateMax'], value)

    def update(self, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, MaxOutstandingRequests=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None):
        """Updates dhcpv6ClientGlobals resource on the server.

        Args
        ----
        - Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
        - Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
        - Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
        - MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        - SetupRateIncrement (number): This value represents the increment value for setup rate. This value is applied every second and can be negative.
        - SetupRateInitial (number): Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
        - SetupRateMax (number): This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, MaxOutstandingRequests=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None):
        """Adds a new dhcpv6ClientGlobals resource on the server and adds it to the container.

        Args
        ----
        - Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
        - Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
        - Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
        - MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        - SetupRateIncrement (number): This value represents the increment value for setup rate. This value is applied every second and can be negative.
        - SetupRateInitial (number): Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
        - SetupRateMax (number): This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpv6ClientGlobals resources using find and the newly added dhcpv6ClientGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpv6ClientGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, MaxOutstandingRequests=None, ObjectId=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None):
        """Finds and retrieves dhcpv6ClientGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv6ClientGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv6ClientGlobals resources from the server.

        Args
        ----
        - Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
        - Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
        - Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
        - MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        - ObjectId (str): Unique identifier for this object
        - SetupRateIncrement (number): This value represents the increment value for setup rate. This value is applied every second and can be negative.
        - SetupRateInitial (number): Setup rate is the number of clients to start in each second. This value represents the initial value for setup rate.
        - SetupRateMax (number): This value represents the final value for setup rate. The setup rate will not change after this value is reached.

        Returns
        -------
        - self: This instance with matching dhcpv6ClientGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv6ClientGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv6ClientGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
