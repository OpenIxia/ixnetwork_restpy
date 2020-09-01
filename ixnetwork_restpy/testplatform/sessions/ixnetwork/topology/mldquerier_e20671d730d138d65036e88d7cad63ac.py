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


class MldQuerier(Base):
    """MLD Querier Configuration
    The MldQuerier class encapsulates a list of mldQuerier resources that are managed by the user.
    A list of resources can be retrieved from the server using the MldQuerier.find() method.
    The list can be managed by using the MldQuerier.add() and MldQuerier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mldQuerier'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DiscardLearntInfo': 'discardLearntInfo',
        'Errors': 'errors',
        'GeneralQueryInterval': 'generalQueryInterval',
        'GeneralQueryResponseInterval': 'generalQueryResponseInterval',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'ProxyQuerier': 'proxyQuerier',
        'RobustnessVariable': 'robustnessVariable',
        'RouterAlert': 'routerAlert',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'SpecificQueryResponseInterval': 'specificQueryResponseInterval',
        'SpecificQueryTransmissionCount': 'specificQueryTransmissionCount',
        'StackedLayers': 'stackedLayers',
        'StartupQueryCount': 'startupQueryCount',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SupportElection': 'supportElection',
        'SupportOlderVersionHost': 'supportOlderVersionHost',
        'SupportOlderVersionQuerier': 'supportOlderVersionQuerier',
        'VersionType': 'versionType',
    }

    def __init__(self, parent):
        super(MldQuerier, self).__init__(parent)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        return LearnedInfo(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DiscardLearntInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard Learned Info
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DiscardLearntInfo']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def GeneralQueryInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): General Query Interval in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GeneralQueryInterval']))

    @property
    def GeneralQueryResponseInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): General Query Response Interval in milliseconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GeneralQueryResponseInterval']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ProxyQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Proxy Querier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProxyQuerier']))

    @property
    def RobustnessVariable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Robustness Variable
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RobustnessVariable']))

    @property
    def RouterAlert(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router Alert
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterAlert']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[noIfaceUp | up]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SpecificQueryResponseInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specific Query Response Interval in milliseconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SpecificQueryResponseInterval']))

    @property
    def SpecificQueryTransmissionCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specific Query Transmission Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SpecificQueryTransmissionCount']))

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StartupQueryCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Startup Query Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartupQueryCount']))

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def SupportElection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Election
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportElection']))

    @property
    def SupportOlderVersionHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Older Version Host
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportOlderVersionHost']))

    @property
    def SupportOlderVersionQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Older Version Querier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportOlderVersionQuerier']))

    @property
    def VersionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Version
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VersionType']))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates mldQuerier resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new mldQuerier resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved mldQuerier resources using find and the newly added mldQuerier resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mldQuerier resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves mldQuerier resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mldQuerier resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mldQuerier resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionInfo (list(str[noIfaceUp | up])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching mldQuerier resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mldQuerier data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mldQuerier resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, DiscardLearntInfo=None, GeneralQueryInterval=None, GeneralQueryResponseInterval=None, ProxyQuerier=None, RobustnessVariable=None, RouterAlert=None, SpecificQueryResponseInterval=None, SpecificQueryTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, VersionType=None):
        """Base class infrastructure that gets a list of mldQuerier device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - DiscardLearntInfo (str): optional regex of discardLearntInfo
        - GeneralQueryInterval (str): optional regex of generalQueryInterval
        - GeneralQueryResponseInterval (str): optional regex of generalQueryResponseInterval
        - ProxyQuerier (str): optional regex of proxyQuerier
        - RobustnessVariable (str): optional regex of robustnessVariable
        - RouterAlert (str): optional regex of routerAlert
        - SpecificQueryResponseInterval (str): optional regex of specificQueryResponseInterval
        - SpecificQueryTransmissionCount (str): optional regex of specificQueryTransmissionCount
        - StartupQueryCount (str): optional regex of startupQueryCount
        - SupportElection (str): optional regex of supportElection
        - SupportOlderVersionHost (str): optional regex of supportOlderVersionHost
        - SupportOlderVersionQuerier (str): optional regex of supportOlderVersionQuerier
        - VersionType (str): optional regex of versionType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def ClearAllLearnedInfoInClient(self, *args, **kwargs):
        """Executes the clearAllLearnedInfoInClient operation on the server.

        Clears ALL routes from GUI grid for the selected BGP Peers.

        clearAllLearnedInfoInClient(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfoInClient', payload=payload, response_object=None)

    def GetLearnedInfo(self, *args, **kwargs):
        """Executes the getLearnedInfo operation on the server.

        Gets all the LSPs and Topologies learnt by this MLD Querier.

        getLearnedInfo(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getLearnedInfo', payload=payload, response_object=None)

    def MldGetLearnedInfo(self, *args, **kwargs):
        """Executes the mldGetLearnedInfo operation on the server.

        Get Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldGetLearnedInfo(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldGetLearnedInfo(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldGetLearnedInfo', payload=payload, response_object=None)

    def MldResumePeriodicGenQuery(self, *args, **kwargs):
        """Executes the mldResumePeriodicGenQuery operation on the server.

        Resume Periodic General Query

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldResumePeriodicGenQuery(SessionIndices=list)
        ----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldResumePeriodicGenQuery(SessionIndices=string)
        ------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldResumePeriodicGenQuery', payload=payload, response_object=None)

    def MldSendSpecificQuery(self, *args, **kwargs):
        """Executes the mldSendSpecificQuery operation on the server.

        Send Specific Query

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldSendSpecificQuery(Start_group_address=string, Group_count=number, Start_source_address=string, Source_count=number, Source_increment_step=number)
        ----------------------------------------------------------------------------------------------------------------------------------------------------
        - Start_group_address (str): This parameter requires a start_group_address of type kString
        - Group_count (number): This parameter requires a group_count of type kInteger
        - Start_source_address (str): This parameter requires a start_source_address of type kString
        - Source_count (number): This parameter requires a source_count of type kInteger
        - Source_increment_step (number): This parameter requires a source_increment_step of type kInteger

        mldSendSpecificQuery(Start_group_address=string, Group_count=number, Start_source_address=string, Source_count=number, Source_increment_step=number, SessionIndices=list)
        -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Start_group_address (str): This parameter requires a start_group_address of type kString
        - Group_count (number): This parameter requires a group_count of type kInteger
        - Start_source_address (str): This parameter requires a start_source_address of type kString
        - Source_count (number): This parameter requires a source_count of type kInteger
        - Source_increment_step (number): This parameter requires a source_increment_step of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldSendSpecificQuery(SessionIndices=string, Start_group_address=string, Group_count=number, Start_source_address=string, Source_count=number, Source_increment_step=number)
        ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a start_group_address of type kString
        - Start_group_address (str): This parameter requires a group_count of type kInteger
        - Group_count (number): This parameter requires a start_source_address of type kString
        - Start_source_address (str): This parameter requires a source_count of type kInteger
        - Source_count (number): This parameter requires a source_increment_step of type kInteger
        - Source_increment_step (number): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldSendSpecificQuery', payload=payload, response_object=None)

    def MldStartQuerier(self, *args, **kwargs):
        """Executes the mldStartQuerier operation on the server.

        Start MLD Querier

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldStartQuerier(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldStartQuerier(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldStartQuerier', payload=payload, response_object=None)

    def MldStopPeriodicGenQuery(self, *args, **kwargs):
        """Executes the mldStopPeriodicGenQuery operation on the server.

        Stop Periodic General Query

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldStopPeriodicGenQuery(SessionIndices=list)
        --------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldStopPeriodicGenQuery(SessionIndices=string)
        ----------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldStopPeriodicGenQuery', payload=payload, response_object=None)

    def MldStopQuerier(self, *args, **kwargs):
        """Executes the mldStopQuerier operation on the server.

        Stop MLD Querier

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldStopQuerier(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldStopQuerier(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldStopQuerier', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def ResumePeriodicGenQuery(self, *args, **kwargs):
        """Executes the resumePeriodicGenQuery operation on the server.

        Resume Sending Periodic General Query

        resumePeriodicGenQuery(Arg2=list)list
        -------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumePeriodicGenQuery', payload=payload, response_object=None)

    def SendSpecificQuery(self, *args, **kwargs):
        """Executes the sendSpecificQuery operation on the server.

        Send Specific Query

        sendSpecificQuery(Arg2=list, Arg3=string, Arg4=number, Arg5=string, Arg6=number, Arg7=number)list
        -------------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str): Start Group Address.
        - Arg4 (number): Group Count.
        - Arg5 (str): Start Source Address.
        - Arg6 (number): Source Count.
        - Arg7 (number): Source Increment Step.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendSpecificQuery', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def StartMLD(self, *args, **kwargs):
        """Executes the startMLD operation on the server.

        Start MLD protocol on selected interfaces

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startMLD(SessionIndices=list)
        -----------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        startMLD(SessionIndices=string)
        -------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        startMLD(Arg2=string, Arg3=list)
        --------------------------------
        - Arg2 (str): ID to associate each async action invocation
        - Arg3 (list(number)): List of indices into the group range grid An empty list indicates all instances in the plugin.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startMLD', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def StopMLD(self, *args, **kwargs):
        """Executes the stopMLD operation on the server.

        Stop MLD protocol on selected interfaces

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopMLD(SessionIndices=list)
        ----------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopMLD(SessionIndices=string)
        ------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stopMLD(Arg2=string, Arg3=list)
        -------------------------------
        - Arg2 (str): ID to associate each async action invocation
        - Arg3 (list(number)): List of indices into the group range grid An empty list indicates all instances in the plugin.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopMLD', payload=payload, response_object=None)

    def StopPeriodicGenQuery(self, *args, **kwargs):
        """Executes the stopPeriodicGenQuery operation on the server.

        Stop Sending Periodic General Query

        stopPeriodicGenQuery(Arg2=list)list
        -----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopPeriodicGenQuery', payload=payload, response_object=None)
