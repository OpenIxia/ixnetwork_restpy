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


class AmtGlobals(Base):
    """Global settings placeholder for AMTPlugin.
    The AmtGlobals class encapsulates a list of amtGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the AmtGlobals.find() method.
    The list can be managed by the user by using the AmtGlobals.add() and AmtGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'amtGlobals'

    def __init__(self, parent):
        super(AmtGlobals, self).__init__(parent)

    @property
    def DiscoveryTimeout(self):
        """Initial time to wait for a response to a Relay Discovery message.

        Returns:
            number
        """
        return self._get_attribute('discoveryTimeout')
    @DiscoveryTimeout.setter
    def DiscoveryTimeout(self, value):
        self._set_attribute('discoveryTimeout', value)

    @property
    def MaxOutstandingSessions(self):
        """This is the point at which AMT Discovery packets will be restricted. AMT Discovery are sent at the configured speed until these are the number of AMT Discovery in progress, without receiving AMT Advertisment messages; at which point new Discovery messages are sent only when other are completed.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingSessions')
    @MaxOutstandingSessions.setter
    def MaxOutstandingSessions(self, value):
        self._set_attribute('maxOutstandingSessions', value)

    @property
    def MaxRelayDiscoveryRetransmissionCount(self):
        """Maximum number of Relay Discovery retransmissions to allow before terminating relay discovery and reporting an error.

        Returns:
            number
        """
        return self._get_attribute('maxRelayDiscoveryRetransmissionCount')
    @MaxRelayDiscoveryRetransmissionCount.setter
    def MaxRelayDiscoveryRetransmissionCount(self, value):
        self._set_attribute('maxRelayDiscoveryRetransmissionCount', value)

    @property
    def MaxRequestRetransmissionCount(self):
        """Maximum number of Request retransmissions to allow before abandoning a relay and restarting relay discovery or reporting an error.

        Returns:
            number
        """
        return self._get_attribute('maxRequestRetransmissionCount')
    @MaxRequestRetransmissionCount.setter
    def MaxRequestRetransmissionCount(self, value):
        self._set_attribute('maxRequestRetransmissionCount', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def RequestTimeout(self):
        """Initial time to wait for a response to a Request message.

        Returns:
            number
        """
        return self._get_attribute('requestTimeout')
    @RequestTimeout.setter
    def RequestTimeout(self, value):
        self._set_attribute('requestTimeout', value)

    @property
    def RetransmissionHolddown(self):
        """Number of seconds to wait in hold-down when the maximum number of retries was reached before trying to retransmit message. Applicable for both Relay Discovery and Request messages.

        Returns:
            number
        """
        return self._get_attribute('retransmissionHolddown')
    @RetransmissionHolddown.setter
    def RetransmissionHolddown(self, value):
        self._set_attribute('retransmissionHolddown', value)

    @property
    def SetupRate(self):
        """Request Rate is the number of AMT Discovery packets to send in each second.

        Returns:
            number
        """
        return self._get_attribute('setupRate')
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute('setupRate', value)

    @property
    def TeardownRate(self):
        """Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.

        Returns:
            number
        """
        return self._get_attribute('teardownRate')
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute('teardownRate', value)

    def update(self, DiscoveryTimeout=None, MaxOutstandingSessions=None, MaxRelayDiscoveryRetransmissionCount=None, MaxRequestRetransmissionCount=None, RequestTimeout=None, RetransmissionHolddown=None, SetupRate=None, TeardownRate=None):
        """Updates a child instance of amtGlobals on the server.

        Args:
            DiscoveryTimeout (number): Initial time to wait for a response to a Relay Discovery message.
            MaxOutstandingSessions (number): This is the point at which AMT Discovery packets will be restricted. AMT Discovery are sent at the configured speed until these are the number of AMT Discovery in progress, without receiving AMT Advertisment messages; at which point new Discovery messages are sent only when other are completed.
            MaxRelayDiscoveryRetransmissionCount (number): Maximum number of Relay Discovery retransmissions to allow before terminating relay discovery and reporting an error.
            MaxRequestRetransmissionCount (number): Maximum number of Request retransmissions to allow before abandoning a relay and restarting relay discovery or reporting an error.
            RequestTimeout (number): Initial time to wait for a response to a Request message.
            RetransmissionHolddown (number): Number of seconds to wait in hold-down when the maximum number of retries was reached before trying to retransmit message. Applicable for both Relay Discovery and Request messages.
            SetupRate (number): Request Rate is the number of AMT Discovery packets to send in each second.
            TeardownRate (number): Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, DiscoveryTimeout=None, MaxOutstandingSessions=None, MaxRelayDiscoveryRetransmissionCount=None, MaxRequestRetransmissionCount=None, RequestTimeout=None, RetransmissionHolddown=None, SetupRate=None, TeardownRate=None):
        """Adds a new amtGlobals node on the server and retrieves it in this instance.

        Args:
            DiscoveryTimeout (number): Initial time to wait for a response to a Relay Discovery message.
            MaxOutstandingSessions (number): This is the point at which AMT Discovery packets will be restricted. AMT Discovery are sent at the configured speed until these are the number of AMT Discovery in progress, without receiving AMT Advertisment messages; at which point new Discovery messages are sent only when other are completed.
            MaxRelayDiscoveryRetransmissionCount (number): Maximum number of Relay Discovery retransmissions to allow before terminating relay discovery and reporting an error.
            MaxRequestRetransmissionCount (number): Maximum number of Request retransmissions to allow before abandoning a relay and restarting relay discovery or reporting an error.
            RequestTimeout (number): Initial time to wait for a response to a Request message.
            RetransmissionHolddown (number): Number of seconds to wait in hold-down when the maximum number of retries was reached before trying to retransmit message. Applicable for both Relay Discovery and Request messages.
            SetupRate (number): Request Rate is the number of AMT Discovery packets to send in each second.
            TeardownRate (number): Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.

        Returns:
            self: This instance with all currently retrieved amtGlobals data using find and the newly added amtGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the amtGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DiscoveryTimeout=None, MaxOutstandingSessions=None, MaxRelayDiscoveryRetransmissionCount=None, MaxRequestRetransmissionCount=None, ObjectId=None, RequestTimeout=None, RetransmissionHolddown=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves amtGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve amtGlobals data from the server.
        By default the find method takes no parameters and will retrieve all amtGlobals data from the server.

        Args:
            DiscoveryTimeout (number): Initial time to wait for a response to a Relay Discovery message.
            MaxOutstandingSessions (number): This is the point at which AMT Discovery packets will be restricted. AMT Discovery are sent at the configured speed until these are the number of AMT Discovery in progress, without receiving AMT Advertisment messages; at which point new Discovery messages are sent only when other are completed.
            MaxRelayDiscoveryRetransmissionCount (number): Maximum number of Relay Discovery retransmissions to allow before terminating relay discovery and reporting an error.
            MaxRequestRetransmissionCount (number): Maximum number of Request retransmissions to allow before abandoning a relay and restarting relay discovery or reporting an error.
            ObjectId (str): Unique identifier for this object
            RequestTimeout (number): Initial time to wait for a response to a Request message.
            RetransmissionHolddown (number): Number of seconds to wait in hold-down when the maximum number of retries was reached before trying to retransmit message. Applicable for both Relay Discovery and Request messages.
            SetupRate (number): Request Rate is the number of AMT Discovery packets to send in each second.
            TeardownRate (number): Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.

        Returns:
            self: This instance with matching amtGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of amtGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the amtGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
