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


class EgtpS5S8SgwOptions(Base):
    """
    The EgtpS5S8SgwOptions class encapsulates a list of egtpS5S8SgwOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the EgtpS5S8SgwOptions.find() method.
    The list can be managed by the user by using the EgtpS5S8SgwOptions.add() and EgtpS5S8SgwOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpS5S8SgwOptions'

    def __init__(self, parent):
        super(EgtpS5S8SgwOptions, self).__init__(parent)

    @property
    def AlwaysIncludeRecoveryIE(self):
        """Always include recovery IE

        Returns:
            bool
        """
        return self._get_attribute('alwaysIncludeRecoveryIE')
    @AlwaysIncludeRecoveryIE.setter
    def AlwaysIncludeRecoveryIE(self, value):
        self._set_attribute('alwaysIncludeRecoveryIE', value)

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
    def DeleteIdleBearers(self):
        """Delete Idle Bearers

        Returns:
            bool
        """
        return self._get_attribute('deleteIdleBearers')
    @DeleteIdleBearers.setter
    def DeleteIdleBearers(self, value):
        self._set_attribute('deleteIdleBearers', value)

    @property
    def MaxOutstandingReleases(self):
        """- The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

    @property
    def MaxOutstandingRequests(self):
        """- The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)

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
    def PcpuLogLevel(self):
        """PCPU log level

        Returns:
            str
        """
        return self._get_attribute('pcpuLogLevel')
    @PcpuLogLevel.setter
    def PcpuLogLevel(self, value):
        self._set_attribute('pcpuLogLevel', value)

    @property
    def SetupRateInitial(self):
        """- The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def TeardownRateInitial(self):
        """- The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Returns:
            number
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    def update(self, AlwaysIncludeRecoveryIE=None, Associates=None, DeleteIdleBearers=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PcpuLogLevel=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Updates a child instance of egtpS5S8SgwOptions on the server.

        Args:
            AlwaysIncludeRecoveryIE (bool): Always include recovery IE
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            DeleteIdleBearers (bool): Delete Idle Bearers
            MaxOutstandingReleases (number): - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
            MaxOutstandingRequests (number): - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
            OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
            PcpuLogLevel (str): PCPU log level
            SetupRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
            TeardownRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AlwaysIncludeRecoveryIE=None, Associates=None, DeleteIdleBearers=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PcpuLogLevel=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Adds a new egtpS5S8SgwOptions node on the server and retrieves it in this instance.

        Args:
            AlwaysIncludeRecoveryIE (bool): Always include recovery IE
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            DeleteIdleBearers (bool): Delete Idle Bearers
            MaxOutstandingReleases (number): - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
            MaxOutstandingRequests (number): - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
            OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
            PcpuLogLevel (str): PCPU log level
            SetupRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
            TeardownRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Returns:
            self: This instance with all currently retrieved egtpS5S8SgwOptions data using find and the newly added egtpS5S8SgwOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the egtpS5S8SgwOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AlwaysIncludeRecoveryIE=None, Associates=None, DeleteIdleBearers=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, OverrideGlobalRateControls=None, PcpuLogLevel=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Finds and retrieves egtpS5S8SgwOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve egtpS5S8SgwOptions data from the server.
        By default the find method takes no parameters and will retrieve all egtpS5S8SgwOptions data from the server.

        Args:
            AlwaysIncludeRecoveryIE (bool): Always include recovery IE
            Associates (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
            DeleteIdleBearers (bool): Delete Idle Bearers
            MaxOutstandingReleases (number): - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
            MaxOutstandingRequests (number): - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
            ObjectId (str): Unique identifier for this object
            OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
            PcpuLogLevel (str): PCPU log level
            SetupRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
            TeardownRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Returns:
            self: This instance with matching egtpS5S8SgwOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of egtpS5S8SgwOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the egtpS5S8SgwOptions data from the server available through an iterator or index

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
