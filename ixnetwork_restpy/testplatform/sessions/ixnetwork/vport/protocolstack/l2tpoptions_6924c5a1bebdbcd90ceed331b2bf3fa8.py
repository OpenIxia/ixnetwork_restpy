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


class L2tpOptions(Base):
    """Portgroup settings container for L2TPPlugin.
    The L2tpOptions class encapsulates a list of l2tpOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2tpOptions.find() method.
    The list can be managed by using the L2tpOptions.add() and L2tpOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2tpOptions'
    _SDM_ATT_MAP = {
        'Associates': 'associates',
        'EnablePerSessionStatGeneration': 'enablePerSessionStatGeneration',
        'Ipv6GlobalAddressMode': 'ipv6GlobalAddressMode',
        'MaxOutstandingReleases': 'maxOutstandingReleases',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'ObjectId': 'objectId',
        'OverrideGlobalRateControls': 'overrideGlobalRateControls',
        'PerSessionStatFilePrefix': 'perSessionStatFilePrefix',
        'RaTimeout': 'raTimeout',
        'Role': 'role',
        'SetupRateInitial': 'setupRateInitial',
        'TeardownRateInitial': 'teardownRateInitial',
        'UseWaitForCompletionTimeout': 'useWaitForCompletionTimeout',
        'WaitForCompletionTimeout': 'waitForCompletionTimeout',
    }

    def __init__(self, parent):
        super(L2tpOptions, self).__init__(parent)

    @property
    def Associates(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack]): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Associates'])
    @Associates.setter
    def Associates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Associates'], value)

    @property
    def EnablePerSessionStatGeneration(self):
        """
        Returns
        -------
        - bool: OBSOLETE
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePerSessionStatGeneration'])
    @EnablePerSessionStatGeneration.setter
    def EnablePerSessionStatGeneration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePerSessionStatGeneration'], value)

    @property
    def Ipv6GlobalAddressMode(self):
        """
        Returns
        -------
        - str: Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6GlobalAddressMode'])
    @Ipv6GlobalAddressMode.setter
    def Ipv6GlobalAddressMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6GlobalAddressMode'], value)

    @property
    def MaxOutstandingReleases(self):
        """
        Returns
        -------
        - number: This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingReleases'])
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingReleases'], value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: Max. no. of sessions outstanding while new sessions are being setup
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
    def OverrideGlobalRateControls(self):
        """
        Returns
        -------
        - bool: If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideGlobalRateControls'])
    @OverrideGlobalRateControls.setter
    def OverrideGlobalRateControls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideGlobalRateControls'], value)

    @property
    def PerSessionStatFilePrefix(self):
        """
        Returns
        -------
        - str: OBSOLETE
        """
        return self._get_attribute(self._SDM_ATT_MAP['PerSessionStatFilePrefix'])
    @PerSessionStatFilePrefix.setter
    def PerSessionStatFilePrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PerSessionStatFilePrefix'], value)

    @property
    def RaTimeout(self):
        """
        Returns
        -------
        - number: Router Advertisment RX timeout period (in seconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP['RaTimeout'])
    @RaTimeout.setter
    def RaTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RaTimeout'], value)

    @property
    def Role(self):
        """
        Returns
        -------
        - str: Role for L2TP element, access concentrator (LAC) or network server (LNS).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Role'])
    @Role.setter
    def Role(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Role'], value)

    @property
    def SetupRateInitial(self):
        """
        Returns
        -------
        - number: Rate (per sec), for session setup
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateInitial'])
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateInitial'], value)

    @property
    def TeardownRateInitial(self):
        """
        Returns
        -------
        - number: The rate per sec for destroying sessions
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRateInitial'])
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRateInitial'], value)

    @property
    def UseWaitForCompletionTimeout(self):
        """
        Returns
        -------
        - bool: Enables configuration of session setup timeout period by the user.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseWaitForCompletionTimeout'])
    @UseWaitForCompletionTimeout.setter
    def UseWaitForCompletionTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseWaitForCompletionTimeout'], value)

    @property
    def WaitForCompletionTimeout(self):
        """
        Returns
        -------
        - number: Session setup timeout period.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitForCompletionTimeout'])
    @WaitForCompletionTimeout.setter
    def WaitForCompletionTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WaitForCompletionTimeout'], value)

    def update(self, Associates=None, EnablePerSessionStatGeneration=None, Ipv6GlobalAddressMode=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PerSessionStatFilePrefix=None, RaTimeout=None, Role=None, SetupRateInitial=None, TeardownRateInitial=None, UseWaitForCompletionTimeout=None, WaitForCompletionTimeout=None):
        """Updates l2tpOptions resource on the server.

        Args
        ----
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - EnablePerSessionStatGeneration (bool): OBSOLETE
        - Ipv6GlobalAddressMode (str): Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
        - MaxOutstandingReleases (number): This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
        - MaxOutstandingRequests (number): Max. no. of sessions outstanding while new sessions are being setup
        - OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - PerSessionStatFilePrefix (str): OBSOLETE
        - RaTimeout (number): Router Advertisment RX timeout period (in seconds).
        - Role (str): Role for L2TP element, access concentrator (LAC) or network server (LNS).
        - SetupRateInitial (number): Rate (per sec), for session setup
        - TeardownRateInitial (number): The rate per sec for destroying sessions
        - UseWaitForCompletionTimeout (bool): Enables configuration of session setup timeout period by the user.
        - WaitForCompletionTimeout (number): Session setup timeout period.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Associates=None, EnablePerSessionStatGeneration=None, Ipv6GlobalAddressMode=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PerSessionStatFilePrefix=None, RaTimeout=None, Role=None, SetupRateInitial=None, TeardownRateInitial=None, UseWaitForCompletionTimeout=None, WaitForCompletionTimeout=None):
        """Adds a new l2tpOptions resource on the server and adds it to the container.

        Args
        ----
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - EnablePerSessionStatGeneration (bool): OBSOLETE
        - Ipv6GlobalAddressMode (str): Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
        - MaxOutstandingReleases (number): This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
        - MaxOutstandingRequests (number): Max. no. of sessions outstanding while new sessions are being setup
        - OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - PerSessionStatFilePrefix (str): OBSOLETE
        - RaTimeout (number): Router Advertisment RX timeout period (in seconds).
        - Role (str): Role for L2TP element, access concentrator (LAC) or network server (LNS).
        - SetupRateInitial (number): Rate (per sec), for session setup
        - TeardownRateInitial (number): The rate per sec for destroying sessions
        - UseWaitForCompletionTimeout (bool): Enables configuration of session setup timeout period by the user.
        - WaitForCompletionTimeout (number): Session setup timeout period.

        Returns
        -------
        - self: This instance with all currently retrieved l2tpOptions resources using find and the newly added l2tpOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l2tpOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Associates=None, EnablePerSessionStatGeneration=None, Ipv6GlobalAddressMode=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, OverrideGlobalRateControls=None, PerSessionStatFilePrefix=None, RaTimeout=None, Role=None, SetupRateInitial=None, TeardownRateInitial=None, UseWaitForCompletionTimeout=None, WaitForCompletionTimeout=None):
        """Finds and retrieves l2tpOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2tpOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2tpOptions resources from the server.

        Args
        ----
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - EnablePerSessionStatGeneration (bool): OBSOLETE
        - Ipv6GlobalAddressMode (str): Selects protocol used to set IPv6 global interfaces on PPP/L2TP interfaces
        - MaxOutstandingReleases (number): This is the point at which session teardown will be restricted. Sessions are torn down at the configured speed until there are this number of sessions in disconnecting stage, at which point additional sessions are torn down only when others get fully disconnected.
        - MaxOutstandingRequests (number): Max. no. of sessions outstanding while new sessions are being setup
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - PerSessionStatFilePrefix (str): OBSOLETE
        - RaTimeout (number): Router Advertisment RX timeout period (in seconds).
        - Role (str): Role for L2TP element, access concentrator (LAC) or network server (LNS).
        - SetupRateInitial (number): Rate (per sec), for session setup
        - TeardownRateInitial (number): The rate per sec for destroying sessions
        - UseWaitForCompletionTimeout (bool): Enables configuration of session setup timeout period by the user.
        - WaitForCompletionTimeout (number): Session setup timeout period.

        Returns
        -------
        - self: This instance with matching l2tpOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2tpOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2tpOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
