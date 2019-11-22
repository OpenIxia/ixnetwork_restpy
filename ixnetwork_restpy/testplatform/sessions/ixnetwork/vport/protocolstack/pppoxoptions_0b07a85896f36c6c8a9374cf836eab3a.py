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


class PppoxOptions(Base):
    """Portgroup settings container for PppoxPlugin.
    The PppoxOptions class encapsulates a list of pppoxOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the PppoxOptions.find() method.
    The list can be managed by the user by using the PppoxOptions.add() and PppoxOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'pppoxOptions'

    def __init__(self, parent):
        super(PppoxOptions, self).__init__(parent)

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
    def EnablePerSessionStatGeneration(self):
        """OBSOLETE

        Returns:
            bool
        """
        return self._get_attribute('enablePerSessionStatGeneration')
    @EnablePerSessionStatGeneration.setter
    def EnablePerSessionStatGeneration(self, value):
        self._set_attribute('enablePerSessionStatGeneration', value)

    @property
    def FilterDataPlaneBeforeL7(self):
        """DEPRECATED Don't enable filters letting data plane traffic through to the port before a status-dump with enable-layer7=yes. When checked, should improve performance for stateless tests.

        Returns:
            bool
        """
        return self._get_attribute('filterDataPlaneBeforeL7')
    @FilterDataPlaneBeforeL7.setter
    def FilterDataPlaneBeforeL7(self, value):
        self._set_attribute('filterDataPlaneBeforeL7', value)

    @property
    def Ipv6GlobalAddressMode(self):
        """Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces

        Returns:
            str
        """
        return self._get_attribute('ipv6GlobalAddressMode')
    @Ipv6GlobalAddressMode.setter
    def Ipv6GlobalAddressMode(self, value):
        self._set_attribute('ipv6GlobalAddressMode', value)

    @property
    def MaxOutstandingReleases(self):
        """This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

    @property
    def MaxOutstandingRequests(self):
        """Max. no. of sessions outstanding while new sessions are being setup

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
    def OverrideGlobalRateControls(self):
        """If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

        Returns:
            bool
        """
        return self._get_attribute('overrideGlobalRateControls')
    @OverrideGlobalRateControls.setter
    def OverrideGlobalRateControls(self, value):
        self._set_attribute('overrideGlobalRateControls', value)

    @property
    def PerSessionStatFilePrefix(self):
        """OBSOLETE

        Returns:
            str
        """
        return self._get_attribute('perSessionStatFilePrefix')
    @PerSessionStatFilePrefix.setter
    def PerSessionStatFilePrefix(self, value):
        self._set_attribute('perSessionStatFilePrefix', value)

    @property
    def RaTimeout(self):
        """Router Advertisment RX timeout period (in seconds).

        Returns:
            number
        """
        return self._get_attribute('raTimeout')
    @RaTimeout.setter
    def RaTimeout(self, value):
        self._set_attribute('raTimeout', value)

    @property
    def ReConnectOnLinkUp(self):
        """Renegotiate the PPP session when the link goes down and up.

        Returns:
            bool
        """
        return self._get_attribute('reConnectOnLinkUp')
    @ReConnectOnLinkUp.setter
    def ReConnectOnLinkUp(self, value):
        self._set_attribute('reConnectOnLinkUp', value)

    @property
    def Role(self):
        """Functional Role for protocol stack, client or server

        Returns:
            str
        """
        return self._get_attribute('role')
    @Role.setter
    def Role(self, value):
        self._set_attribute('role', value)

    @property
    def SetupRateInitial(self):
        """Rate (per sec), for session setup

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def TeardownRateInitial(self):
        """The rate per sec for destroying sessions

        Returns:
            number
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    @property
    def UseWaitForCompletionTimeout(self):
        """Enables configuration of session setup timeout period by the user.

        Returns:
            bool
        """
        return self._get_attribute('useWaitForCompletionTimeout')
    @UseWaitForCompletionTimeout.setter
    def UseWaitForCompletionTimeout(self, value):
        self._set_attribute('useWaitForCompletionTimeout', value)

    @property
    def WaitForCompletionTimeout(self):
        """Session setup timeout period.

        Returns:
            number
        """
        return self._get_attribute('waitForCompletionTimeout')
    @WaitForCompletionTimeout.setter
    def WaitForCompletionTimeout(self, value):
        self._set_attribute('waitForCompletionTimeout', value)

    @property
    def WaitingTimeUntilReconnect(self):
        """Time to wait until reconnect

        Returns:
            number
        """
        return self._get_attribute('waitingTimeUntilReconnect')
    @WaitingTimeUntilReconnect.setter
    def WaitingTimeUntilReconnect(self, value):
        self._set_attribute('waitingTimeUntilReconnect', value)

    def update(self, Associates=None, EnablePerSessionStatGeneration=None, FilterDataPlaneBeforeL7=None, Ipv6GlobalAddressMode=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PerSessionStatFilePrefix=None, RaTimeout=None, ReConnectOnLinkUp=None, Role=None, SetupRateInitial=None, TeardownRateInitial=None, UseWaitForCompletionTimeout=None, WaitForCompletionTimeout=None, WaitingTimeUntilReconnect=None):
        """Updates a child instance of pppoxOptions on the server.

        Args:
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            EnablePerSessionStatGeneration (bool): OBSOLETE
            FilterDataPlaneBeforeL7 (bool): Don't enable filters letting data plane traffic through to the port before a status-dump with enable-layer7=yes. When checked, should improve performance for stateless tests.
            Ipv6GlobalAddressMode (str): Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
            MaxOutstandingReleases (number): This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
            MaxOutstandingRequests (number): Max. no. of sessions outstanding while new sessions are being setup
            OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
            PerSessionStatFilePrefix (str): OBSOLETE
            RaTimeout (number): Router Advertisment RX timeout period (in seconds).
            ReConnectOnLinkUp (bool): Renegotiate the PPP session when the link goes down and up.
            Role (str): Functional Role for protocol stack, client or server
            SetupRateInitial (number): Rate (per sec), for session setup
            TeardownRateInitial (number): The rate per sec for destroying sessions
            UseWaitForCompletionTimeout (bool): Enables configuration of session setup timeout period by the user.
            WaitForCompletionTimeout (number): Session setup timeout period.
            WaitingTimeUntilReconnect (number): Time to wait until reconnect

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Associates=None, EnablePerSessionStatGeneration=None, FilterDataPlaneBeforeL7=None, Ipv6GlobalAddressMode=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PerSessionStatFilePrefix=None, RaTimeout=None, ReConnectOnLinkUp=None, Role=None, SetupRateInitial=None, TeardownRateInitial=None, UseWaitForCompletionTimeout=None, WaitForCompletionTimeout=None, WaitingTimeUntilReconnect=None):
        """Adds a new pppoxOptions node on the server and retrieves it in this instance.

        Args:
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            EnablePerSessionStatGeneration (bool): OBSOLETE
            FilterDataPlaneBeforeL7 (bool): Don't enable filters letting data plane traffic through to the port before a status-dump with enable-layer7=yes. When checked, should improve performance for stateless tests.
            Ipv6GlobalAddressMode (str): Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
            MaxOutstandingReleases (number): This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
            MaxOutstandingRequests (number): Max. no. of sessions outstanding while new sessions are being setup
            OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
            PerSessionStatFilePrefix (str): OBSOLETE
            RaTimeout (number): Router Advertisment RX timeout period (in seconds).
            ReConnectOnLinkUp (bool): Renegotiate the PPP session when the link goes down and up.
            Role (str): Functional Role for protocol stack, client or server
            SetupRateInitial (number): Rate (per sec), for session setup
            TeardownRateInitial (number): The rate per sec for destroying sessions
            UseWaitForCompletionTimeout (bool): Enables configuration of session setup timeout period by the user.
            WaitForCompletionTimeout (number): Session setup timeout period.
            WaitingTimeUntilReconnect (number): Time to wait until reconnect

        Returns:
            self: This instance with all currently retrieved pppoxOptions data using find and the newly added pppoxOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the pppoxOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Associates=None, EnablePerSessionStatGeneration=None, FilterDataPlaneBeforeL7=None, Ipv6GlobalAddressMode=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, OverrideGlobalRateControls=None, PerSessionStatFilePrefix=None, RaTimeout=None, ReConnectOnLinkUp=None, Role=None, SetupRateInitial=None, TeardownRateInitial=None, UseWaitForCompletionTimeout=None, WaitForCompletionTimeout=None, WaitingTimeUntilReconnect=None):
        """Finds and retrieves pppoxOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve pppoxOptions data from the server.
        By default the find method takes no parameters and will retrieve all pppoxOptions data from the server.

        Args:
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            EnablePerSessionStatGeneration (bool): OBSOLETE
            FilterDataPlaneBeforeL7 (bool): Don't enable filters letting data plane traffic through to the port before a status-dump with enable-layer7=yes. When checked, should improve performance for stateless tests.
            Ipv6GlobalAddressMode (str): Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
            MaxOutstandingReleases (number): This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
            MaxOutstandingRequests (number): Max. no. of sessions outstanding while new sessions are being setup
            ObjectId (str): Unique identifier for this object
            OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
            PerSessionStatFilePrefix (str): OBSOLETE
            RaTimeout (number): Router Advertisment RX timeout period (in seconds).
            ReConnectOnLinkUp (bool): Renegotiate the PPP session when the link goes down and up.
            Role (str): Functional Role for protocol stack, client or server
            SetupRateInitial (number): Rate (per sec), for session setup
            TeardownRateInitial (number): The rate per sec for destroying sessions
            UseWaitForCompletionTimeout (bool): Enables configuration of session setup timeout period by the user.
            WaitForCompletionTimeout (number): Session setup timeout period.
            WaitingTimeUntilReconnect (number): Time to wait until reconnect

        Returns:
            self: This instance with matching pppoxOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of pppoxOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the pppoxOptions data from the server available through an iterator or index

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
