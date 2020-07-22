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


class EgtpS5S8SgwOptions(Base):
    """
    The EgtpS5S8SgwOptions class encapsulates a list of egtpS5S8SgwOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the EgtpS5S8SgwOptions.find() method.
    The list can be managed by using the EgtpS5S8SgwOptions.add() and EgtpS5S8SgwOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpS5S8SgwOptions'
    _SDM_ATT_MAP = {
        'AlwaysIncludeRecoveryIE': 'alwaysIncludeRecoveryIE',
        'Associates': 'associates',
        'DeleteIdleBearers': 'deleteIdleBearers',
        'MaxOutstandingReleases': 'maxOutstandingReleases',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'ObjectId': 'objectId',
        'OverrideGlobalRateControls': 'overrideGlobalRateControls',
        'PcpuLogLevel': 'pcpuLogLevel',
        'SetupRateInitial': 'setupRateInitial',
        'TeardownRateInitial': 'teardownRateInitial',
    }

    def __init__(self, parent):
        super(EgtpS5S8SgwOptions, self).__init__(parent)

    @property
    def AlwaysIncludeRecoveryIE(self):
        """
        Returns
        -------
        - bool: Always include recovery IE
        """
        return self._get_attribute(self._SDM_ATT_MAP['AlwaysIncludeRecoveryIE'])
    @AlwaysIncludeRecoveryIE.setter
    def AlwaysIncludeRecoveryIE(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AlwaysIncludeRecoveryIE'], value)

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
    def DeleteIdleBearers(self):
        """
        Returns
        -------
        - bool: Delete Idle Bearers
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeleteIdleBearers'])
    @DeleteIdleBearers.setter
    def DeleteIdleBearers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeleteIdleBearers'], value)

    @property
    def MaxOutstandingReleases(self):
        """
        Returns
        -------
        - number: - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
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
        - number: - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
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
    def PcpuLogLevel(self):
        """
        Returns
        -------
        - str: PCPU log level
        """
        return self._get_attribute(self._SDM_ATT_MAP['PcpuLogLevel'])
    @PcpuLogLevel.setter
    def PcpuLogLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PcpuLogLevel'], value)

    @property
    def SetupRateInitial(self):
        """
        Returns
        -------
        - number: - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
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
        - number: - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRateInitial'])
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRateInitial'], value)

    def update(self, AlwaysIncludeRecoveryIE=None, Associates=None, DeleteIdleBearers=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PcpuLogLevel=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Updates egtpS5S8SgwOptions resource on the server.

        Args
        ----
        - AlwaysIncludeRecoveryIE (bool): Always include recovery IE
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - DeleteIdleBearers (bool): Delete Idle Bearers
        - MaxOutstandingReleases (number): - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
        - MaxOutstandingRequests (number): - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
        - OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - PcpuLogLevel (str): PCPU log level
        - SetupRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
        - TeardownRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AlwaysIncludeRecoveryIE=None, Associates=None, DeleteIdleBearers=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, OverrideGlobalRateControls=None, PcpuLogLevel=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Adds a new egtpS5S8SgwOptions resource on the server and adds it to the container.

        Args
        ----
        - AlwaysIncludeRecoveryIE (bool): Always include recovery IE
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - DeleteIdleBearers (bool): Delete Idle Bearers
        - MaxOutstandingReleases (number): - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
        - MaxOutstandingRequests (number): - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
        - OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - PcpuLogLevel (str): PCPU log level
        - SetupRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
        - TeardownRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Returns
        -------
        - self: This instance with all currently retrieved egtpS5S8SgwOptions resources using find and the newly added egtpS5S8SgwOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained egtpS5S8SgwOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AlwaysIncludeRecoveryIE=None, Associates=None, DeleteIdleBearers=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, OverrideGlobalRateControls=None, PcpuLogLevel=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Finds and retrieves egtpS5S8SgwOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egtpS5S8SgwOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egtpS5S8SgwOptions resources from the server.

        Args
        ----
        - AlwaysIncludeRecoveryIE (bool): Always include recovery IE
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - DeleteIdleBearers (bool): Delete Idle Bearers
        - MaxOutstandingReleases (number): - The maximum amount of in progress procedures. If this limit is reached, no new releases shall be started, for all procedures covered. Release rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop
        - MaxOutstandingRequests (number): - The maximum amount of in progress procedures. If this limit is reached, no new initiations shall be started, for all procedures covered. Initiation rate will be resumed when the amount of outstanding procedures to be completed drops below the max outstanding value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalRateControls (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - PcpuLogLevel (str): PCPU log level
        - SetupRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Attach (create session) o Bearer Resource Command for start o HSS updates o All handover types o Enter Idle (S1 Release procedure) o Exit Idle (UE/Network triggered service request)
        - TeardownRateInitial (number): - The maximum procedure initiation rate, cumulative of multiple procedures. The rate of initiation of all procedures, at any given time, shall not exceed this value - Includes the following procedures: o Detach o Delete Bearer Command o Bearer Resource Command for stop

        Returns
        -------
        - self: This instance with matching egtpS5S8SgwOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egtpS5S8SgwOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egtpS5S8SgwOptions resources from the server available through an iterator or index

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
