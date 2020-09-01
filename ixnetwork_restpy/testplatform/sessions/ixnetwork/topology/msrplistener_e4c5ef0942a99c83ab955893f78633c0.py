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


class MsrpListener(Base):
    """MSRP Listener level Configuration
    The MsrpListener class encapsulates a list of msrpListener resources that are managed by the user.
    A list of resources can be retrieved from the server using the MsrpListener.find() method.
    The list can be managed by using the MsrpListener.add() and MsrpListener.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'msrpListener'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseAs': 'advertiseAs',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DeclareUnsolicitedVlan': 'declareUnsolicitedVlan',
        'DescriptiveName': 'descriptiveName',
        'Errors': 'errors',
        'JoinTimer': 'joinTimer',
        'LeaveAllTimer': 'leaveAllTimer',
        'LeaveTimer': 'leaveTimer',
        'ListenerDomainCount': 'listenerDomainCount',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'ProtocolVersion': 'protocolVersion',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StartVlanId': 'startVlanId',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SubscribeAll': 'subscribeAll',
        'SubscribedStreamCount': 'subscribedStreamCount',
        'VlanCount': 'vlanCount',
    }

    def __init__(self, parent):
        super(MsrpListener, self).__init__(parent)

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
    def MsrpListenerDomains(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistenerdomains_f2fe387dee9561ca08fc00cc9bf60ef4.MsrpListenerDomains): An instance of the MsrpListenerDomains class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistenerdomains_f2fe387dee9561ca08fc00cc9bf60ef4 import MsrpListenerDomains
        return MsrpListenerDomains(self)._select()

    @property
    def SubscribedStreams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.subscribedstreams_b01da202c4f5221aa9094d86a288d1bd.SubscribedStreams): An instance of the SubscribedStreams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.subscribedstreams_b01da202c4f5221aa9094d86a288d1bd import SubscribedStreams
        return SubscribedStreams(self)._select()

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
    def AdvertiseAs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Attribute Advertise As Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseAs']))

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
    def DeclareUnsolicitedVlan(self):
        """
        Returns
        -------
        - bool: Declare VLAN membership of configured VLAN range using MVRP even before learning any streams
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeclareUnsolicitedVlan'])
    @DeclareUnsolicitedVlan.setter
    def DeclareUnsolicitedVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeclareUnsolicitedVlan'], value)

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def JoinTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MRP Join Timer in miliseconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JoinTimer']))

    @property
    def LeaveAllTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MRP Leave All timer in milisecond
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LeaveAllTimer']))

    @property
    def LeaveTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MRP Leave Timer in milisecond
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LeaveTimer']))

    @property
    def ListenerDomainCount(self):
        """
        Returns
        -------
        - number: Domain Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['ListenerDomainCount'])
    @ListenerDomainCount.setter
    def ListenerDomainCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ListenerDomainCount'], value)

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
    def ProtocolVersion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MRP protocol version
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProtocolVersion']))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

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
    def StartVlanId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start VLAN ID of VLAN range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartVlanId']))

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
    def SubscribeAll(self):
        """
        Returns
        -------
        - bool: Send MSRP Listener Ready for all streams advertised in recieved MSRP Talker Advertise
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubscribeAll'])
    @SubscribeAll.setter
    def SubscribeAll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubscribeAll'], value)

    @property
    def SubscribedStreamCount(self):
        """
        Returns
        -------
        - number: Count of streams Listener want to listen
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubscribedStreamCount'])
    @SubscribedStreamCount.setter
    def SubscribedStreamCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubscribedStreamCount'], value)

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN count of VLAN range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanCount']))

    def update(self, ConnectedVia=None, DeclareUnsolicitedVlan=None, ListenerDomainCount=None, Multiplier=None, Name=None, StackedLayers=None, SubscribeAll=None, SubscribedStreamCount=None):
        """Updates msrpListener resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - DeclareUnsolicitedVlan (bool): Declare VLAN membership of configured VLAN range using MVRP even before learning any streams
        - ListenerDomainCount (number): Domain Count
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - SubscribeAll (bool): Send MSRP Listener Ready for all streams advertised in recieved MSRP Talker Advertise
        - SubscribedStreamCount (number): Count of streams Listener want to listen

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, DeclareUnsolicitedVlan=None, ListenerDomainCount=None, Multiplier=None, Name=None, StackedLayers=None, SubscribeAll=None, SubscribedStreamCount=None):
        """Adds a new msrpListener resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - DeclareUnsolicitedVlan (bool): Declare VLAN membership of configured VLAN range using MVRP even before learning any streams
        - ListenerDomainCount (number): Domain Count
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - SubscribeAll (bool): Send MSRP Listener Ready for all streams advertised in recieved MSRP Talker Advertise
        - SubscribedStreamCount (number): Count of streams Listener want to listen

        Returns
        -------
        - self: This instance with all currently retrieved msrpListener resources using find and the newly added msrpListener resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained msrpListener resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DeclareUnsolicitedVlan=None, DescriptiveName=None, Errors=None, ListenerDomainCount=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, SubscribeAll=None, SubscribedStreamCount=None):
        """Finds and retrieves msrpListener resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve msrpListener resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all msrpListener resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DeclareUnsolicitedVlan (bool): Declare VLAN membership of configured VLAN range using MVRP even before learning any streams
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - ListenerDomainCount (number): Domain Count
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - SubscribeAll (bool): Send MSRP Listener Ready for all streams advertised in recieved MSRP Talker Advertise
        - SubscribedStreamCount (number): Count of streams Listener want to listen

        Returns
        -------
        - self: This instance with matching msrpListener resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of msrpListener data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the msrpListener resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseAs=None, JoinTimer=None, LeaveAllTimer=None, LeaveTimer=None, ProtocolVersion=None, StartVlanId=None, VlanCount=None):
        """Base class infrastructure that gets a list of msrpListener device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseAs (str): optional regex of advertiseAs
        - JoinTimer (str): optional regex of joinTimer
        - LeaveAllTimer (str): optional regex of leaveAllTimer
        - LeaveTimer (str): optional regex of leaveTimer
        - ProtocolVersion (str): optional regex of protocolVersion
        - StartVlanId (str): optional regex of startVlanId
        - VlanCount (str): optional regex of vlanCount

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

    def ClearListenerDatabasesInClient(self, *args, **kwargs):
        """Executes the clearListenerDatabasesInClient operation on the server.

        Clears ALL databases learnt by this MSRP Listener.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearListenerDatabasesInClient(SessionIndices=list)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        clearListenerDatabasesInClient(SessionIndices=string)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        clearListenerDatabasesInClient(Arg2=list)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearListenerDatabasesInClient', payload=payload, response_object=None)

    def GetListenerDatabases(self, *args, **kwargs):
        """Executes the getListenerDatabases operation on the server.

        Gets All databases learnt by this MSRP Listener

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getListenerDatabases(SessionIndices=list)
        -----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getListenerDatabases(SessionIndices=string)
        -------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getListenerDatabases(Arg2=list)list
        -----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getListenerDatabases', payload=payload, response_object=None)

    def GetMsrpListenerDomainDatabase(self, *args, **kwargs):
        """Executes the getMsrpListenerDomainDatabase operation on the server.

        Gets Listener Domain Database Information learnt by this Msrp Listener

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getMsrpListenerDomainDatabase(SessionIndices=list)
        --------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getMsrpListenerDomainDatabase(SessionIndices=string)
        ----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getMsrpListenerDomainDatabase(Arg2=list)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getMsrpListenerDomainDatabase', payload=payload, response_object=None)

    def GetMsrpListenerStreamDatabase(self, *args, **kwargs):
        """Executes the getMsrpListenerStreamDatabase operation on the server.

        Gets Listener Stream Database Information learnt by this Msrp Listener.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getMsrpListenerStreamDatabase(SessionIndices=list)
        --------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getMsrpListenerStreamDatabase(SessionIndices=string)
        ----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getMsrpListenerStreamDatabase(Arg2=list)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getMsrpListenerStreamDatabase', payload=payload, response_object=None)

    def GetMsrpListenerVlanDatabase(self, *args, **kwargs):
        """Executes the getMsrpListenerVlanDatabase operation on the server.

        Gets Listener VLAN Database Information learnt by this Msrp Listener

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getMsrpListenerVlanDatabase(SessionIndices=list)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getMsrpListenerVlanDatabase(SessionIndices=string)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getMsrpListenerVlanDatabase(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getMsrpListenerVlanDatabase', payload=payload, response_object=None)

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
