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


class Dhcpv6PdClientOptions(Base):
    """Portgroup settings placeholder for DHCPv6PDClientPlugin.
    The Dhcpv6PdClientOptions class encapsulates a list of dhcpv6PdClientOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6PdClientOptions.find() method.
    The list can be managed by the user by using the Dhcpv6PdClientOptions.add() and Dhcpv6PdClientOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6PdClientOptions'

    def __init__(self, parent):
        super(Dhcpv6PdClientOptions, self).__init__(parent)

    @property
    def Associates(self):
        """The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])
        """
        return self._get_attribute('associates')
    @Associates.setter
    def Associates(self, value):
        self._set_attribute('associates', value)

    @property
    def MaxOutstandingReleases(self):
        """This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

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
    def OverrideGlobalSetupRate(self):
        """If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.

        Returns:
            bool
        """
        return self._get_attribute('overrideGlobalSetupRate')
    @OverrideGlobalSetupRate.setter
    def OverrideGlobalSetupRate(self, value):
        self._set_attribute('overrideGlobalSetupRate', value)

    @property
    def OverrideGlobalTeardownRate(self):
        """If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.

        Returns:
            bool
        """
        return self._get_attribute('overrideGlobalTeardownRate')
    @OverrideGlobalTeardownRate.setter
    def OverrideGlobalTeardownRate(self, value):
        self._set_attribute('overrideGlobalTeardownRate', value)

    @property
    def SetupRateIncrement(self):
        """This value represents the increment value for setup rate.This value is applied every second and can be negative.

        Returns:
            number
        """
        return self._get_attribute('setupRateIncrement')
    @SetupRateIncrement.setter
    def SetupRateIncrement(self, value):
        self._set_attribute('setupRateIncrement', value)

    @property
    def SetupRateInitial(self):
        """Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def SetupRateMax(self):
        """This value represents the final value for setup rate.The setup rate will not change after this value is reached.

        Returns:
            number
        """
        return self._get_attribute('setupRateMax')
    @SetupRateMax.setter
    def SetupRateMax(self, value):
        self._set_attribute('setupRateMax', value)

    @property
    def TeardownRateIncrement(self):
        """This value represents the increment value for teardown rate.This value is applied every second and can be negative.

        Returns:
            number
        """
        return self._get_attribute('teardownRateIncrement')
    @TeardownRateIncrement.setter
    def TeardownRateIncrement(self, value):
        self._set_attribute('teardownRateIncrement', value)

    @property
    def TeardownRateInitial(self):
        """Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.

        Returns:
            number
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    @property
    def TeardownRateMax(self):
        """This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.

        Returns:
            number
        """
        return self._get_attribute('teardownRateMax')
    @TeardownRateMax.setter
    def TeardownRateMax(self, value):
        self._set_attribute('teardownRateMax', value)

    def update(self, Associates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalSetupRate=None, OverrideGlobalTeardownRate=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None):
        """Updates a child instance of dhcpv6PdClientOptions on the server.

        Args:
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            MaxOutstandingReleases (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.
            OverrideGlobalTeardownRate (bool): If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.
            SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
            TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
            TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
            TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Associates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalSetupRate=None, OverrideGlobalTeardownRate=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None):
        """Adds a new dhcpv6PdClientOptions node on the server and retrieves it in this instance.

        Args:
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            MaxOutstandingReleases (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.
            OverrideGlobalTeardownRate (bool): If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.
            SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
            TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
            TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
            TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.

        Returns:
            self: This instance with all currently retrieved dhcpv6PdClientOptions data using find and the newly added dhcpv6PdClientOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpv6PdClientOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Associates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, OverrideGlobalSetupRate=None, OverrideGlobalTeardownRate=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None):
        """Finds and retrieves dhcpv6PdClientOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpv6PdClientOptions data from the server.
        By default the find method takes no parameters and will retrieve all dhcpv6PdClientOptions data from the server.

        Args:
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            MaxOutstandingReleases (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            MaxOutstandingRequests (number): This is the point at which requests will be restricted. Requests are sent at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            ObjectId (str): Unique identifier for this object
            OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.
            OverrideGlobalTeardownRate (bool): If true then all the rate settings defined at Session levelwill be overriden by rate settings defined on this PortGroup.
            SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
            TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
            TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
            TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.

        Returns:
            self: This instance with matching dhcpv6PdClientOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpv6PdClientOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpv6PdClientOptions data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
