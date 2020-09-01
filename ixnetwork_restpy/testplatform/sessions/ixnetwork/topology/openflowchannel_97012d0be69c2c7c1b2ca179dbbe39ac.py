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


class OpenFlowChannel(Base):
    """Openflow Controller Channel level Configuration
    The OpenFlowChannel class encapsulates a list of openFlowChannel resources that are managed by the user.
    A list of resources can be retrieved from the server using the OpenFlowChannel.find() method.
    The list can be managed by using the OpenFlowChannel.add() and OpenFlowChannel.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'openFlowChannel'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'CalcFlowRate': 'calcFlowRate',
        'CalcFlowRateWithBarrier': 'calcFlowRateWithBarrier',
        'ConnectedVia': 'connectedVia',
        'ControllerIndex': 'controllerIndex',
        'ControllerName': 'controllerName',
        'Count': 'count',
        'DatapathId': 'datapathId',
        'DatapathIdHex': 'datapathIdHex',
        'DescriptiveName': 'descriptiveName',
        'EnableHelloElement': 'enableHelloElement',
        'Errors': 'errors',
        'FlowTxBurstSize': 'flowTxBurstSize',
        'GroupsPerChannel': 'groupsPerChannel',
        'InterFlowBurstGap': 'interFlowBurstGap',
        'LocalIp': 'localIp',
        'MaxFlowsAtATime': 'maxFlowsAtATime',
        'MetersPerChannel': 'metersPerChannel',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'RemoteIp': 'remoteIp',
        'SendRoleRequest': 'sendRoleRequest',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StartupGenerationId': 'startupGenerationId',
        'StartupRoleRequest': 'startupRoleRequest',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TablesPerChannel': 'tablesPerChannel',
        'UseDatapathID': 'useDatapathID',
    }

    def __init__(self, parent):
        super(OpenFlowChannel, self).__init__(parent)

    @property
    def Groups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.groups_b0203364879843ea921d92b31d3b37a9.Groups): An instance of the Groups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.groups_b0203364879843ea921d92b31d3b37a9 import Groups
        return Groups(self)

    @property
    def Meters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.meters_8b28210732dd4e9a4bab19a7e6241a11.Meters): An instance of the Meters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.meters_8b28210732dd4e9a4bab19a7e6241a11 import Meters
        return Meters(self)

    @property
    def Tables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tables_3d687bbed07969785585da03f7a19e75.Tables): An instance of the Tables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tables_3d687bbed07969785585da03f7a19e75 import Tables
        return Tables(self)

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
    def CalcFlowRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the statistics on the rate of transmission of flows per second by the controller is published.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CalcFlowRate']))

    @property
    def CalcFlowRateWithBarrier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, statistics on the rate of transmission of flows per second by the controller, along with Barrier Request messages is published.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CalcFlowRateWithBarrier']))

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
    def ControllerIndex(self):
        """
        Returns
        -------
        - list(str): Parent Controller Index
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControllerIndex'])

    @property
    def ControllerName(self):
        """
        Returns
        -------
        - str: Parent Controller Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControllerName'])

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DatapathId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Datapath ID of the OF Channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DatapathId']))

    @property
    def DatapathIdHex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Datapath ID in hexadecimal format.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DatapathIdHex']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableHelloElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Controller sends a hello message consisting of an OpenFlow header and a set of variable size hello elements to inform the initial handshake of the connection.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHelloElement']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FlowTxBurstSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the number of Flow transmitting packets that can be sent in a single burst within the time frame specified by the Inter Flow Burst Gap value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlowTxBurstSize']))

    @property
    def GroupsPerChannel(self):
        """
        Returns
        -------
        - number: Number of Groups per Channel
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupsPerChannel'])
    @GroupsPerChannel.setter
    def GroupsPerChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupsPerChannel'], value)

    @property
    def InterFlowBurstGap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the duration (in milliseconds) for which the controller waits between successive flow advertisements.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterFlowBurstGap']))

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - list(str): The local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaxFlowsAtATime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Max Number of Flows Processed at a Time is the size of an internal buffer maintained by the Ixiacontroller, which prevents it from sending more flows than the Openflow switch can consume at a time.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxFlowsAtATime']))

    @property
    def MetersPerChannel(self):
        """
        Returns
        -------
        - number: Number of Meters per Channel
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetersPerChannel'])
    @MetersPerChannel.setter
    def MetersPerChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetersPerChannel'], value)

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
    def RemoteIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the DUT at the other end of the OF Channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIp']))

    @property
    def SendRoleRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the controller sends a Role Request message after the connection is established; to change its role according to the Role Request option selected.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendRoleRequest']))

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
    def StartupGenerationId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 64-bit sequence number field that identifies a given mastership view.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartupGenerationId']))

    @property
    def StartupRoleRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This defines role of the controller.Options include: 1) No Change 2) Equal 3) Master 4) Slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartupRoleRequest']))

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
    def TablesPerChannel(self):
        """
        Returns
        -------
        - number: Number of Tables per Channel
        """
        return self._get_attribute(self._SDM_ATT_MAP['TablesPerChannel'])
    @TablesPerChannel.setter
    def TablesPerChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TablesPerChannel'], value)

    @property
    def UseDatapathID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Datapath ID and IP address are used as the OF Channel identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseDatapathID']))

    def update(self, ConnectedVia=None, GroupsPerChannel=None, MetersPerChannel=None, Multiplier=None, Name=None, StackedLayers=None, TablesPerChannel=None):
        """Updates openFlowChannel resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - GroupsPerChannel (number): Number of Groups per Channel
        - MetersPerChannel (number): Number of Meters per Channel
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TablesPerChannel (number): Number of Tables per Channel

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, GroupsPerChannel=None, MetersPerChannel=None, Multiplier=None, Name=None, StackedLayers=None, TablesPerChannel=None):
        """Adds a new openFlowChannel resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - GroupsPerChannel (number): Number of Groups per Channel
        - MetersPerChannel (number): Number of Meters per Channel
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TablesPerChannel (number): Number of Tables per Channel

        Returns
        -------
        - self: This instance with all currently retrieved openFlowChannel resources using find and the newly added openFlowChannel resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained openFlowChannel resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, ControllerIndex=None, ControllerName=None, Count=None, DescriptiveName=None, Errors=None, GroupsPerChannel=None, LocalIp=None, MetersPerChannel=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TablesPerChannel=None):
        """Finds and retrieves openFlowChannel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openFlowChannel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openFlowChannel resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - ControllerIndex (list(str)): Parent Controller Index
        - ControllerName (str): Parent Controller Name
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - GroupsPerChannel (number): Number of Groups per Channel
        - LocalIp (list(str)): The local IP address of the interface. This field is auto-populated and cannot be changed.
        - MetersPerChannel (number): Number of Meters per Channel
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TablesPerChannel (number): Number of Tables per Channel

        Returns
        -------
        - self: This instance with matching openFlowChannel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openFlowChannel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openFlowChannel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, CalcFlowRate=None, CalcFlowRateWithBarrier=None, DatapathId=None, DatapathIdHex=None, EnableHelloElement=None, FlowTxBurstSize=None, InterFlowBurstGap=None, MaxFlowsAtATime=None, RemoteIp=None, SendRoleRequest=None, StartupGenerationId=None, StartupRoleRequest=None, UseDatapathID=None):
        """Base class infrastructure that gets a list of openFlowChannel device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CalcFlowRate (str): optional regex of calcFlowRate
        - CalcFlowRateWithBarrier (str): optional regex of calcFlowRateWithBarrier
        - DatapathId (str): optional regex of datapathId
        - DatapathIdHex (str): optional regex of datapathIdHex
        - EnableHelloElement (str): optional regex of enableHelloElement
        - FlowTxBurstSize (str): optional regex of flowTxBurstSize
        - InterFlowBurstGap (str): optional regex of interFlowBurstGap
        - MaxFlowsAtATime (str): optional regex of maxFlowsAtATime
        - RemoteIp (str): optional regex of remoteIp
        - SendRoleRequest (str): optional regex of sendRoleRequest
        - StartupGenerationId (str): optional regex of startupGenerationId
        - StartupRoleRequest (str): optional regex of startupRoleRequest
        - UseDatapathID (str): optional regex of useDatapathID

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

    def GetAsynchronousConfiguration(self, *args, **kwargs):
        """Executes the getAsynchronousConfiguration operation on the server.

        Get Asynchronous Configurationr

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getAsynchronousConfiguration(SessionIndices=list)
        -------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getAsynchronousConfiguration(SessionIndices=string)
        ---------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getAsynchronousConfiguration(Arg2=list)list
        -------------------------------------------
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
        return self._execute('getAsynchronousConfiguration', payload=payload, response_object=None)

    def InvokeSendRoleRequest(self, *args, **kwargs):
        """Executes the invokeSendRoleRequest operation on the server.

        Sends a Role Request for selected Channel.

        invokeSendRoleRequest(Arg2=list)list
        ------------------------------------
        - Arg2 (list(number)): List of indices in channel grid
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('invokeSendRoleRequest', payload=payload, response_object=None)

    def PauseEchoReply(self, *args, **kwargs):
        """Executes the pauseEchoReply operation on the server.

        Pause Sending Echo Reply Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pauseEchoReply(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        pauseEchoReply(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        pauseEchoReply(Arg2=list)list
        -----------------------------
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
        return self._execute('pauseEchoReply', payload=payload, response_object=None)

    def PauseEchoRequest(self, *args, **kwargs):
        """Executes the pauseEchoRequest operation on the server.

        Pause Sending Echo Request Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pauseEchoRequest(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        pauseEchoRequest(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        pauseEchoRequest(Arg2=list)list
        -------------------------------
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
        return self._execute('pauseEchoRequest', payload=payload, response_object=None)

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

    def ResumeEchoReply(self, *args, **kwargs):
        """Executes the resumeEchoReply operation on the server.

        Resume Sending Echo Reply Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeEchoReply(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        resumeEchoReply(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        resumeEchoReply(Arg2=list)list
        ------------------------------
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
        return self._execute('resumeEchoReply', payload=payload, response_object=None)

    def ResumeEchoRequest(self, *args, **kwargs):
        """Executes the resumeEchoRequest operation on the server.

        Resume Sending Echo Request Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeEchoRequest(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        resumeEchoRequest(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        resumeEchoRequest(Arg2=list)list
        --------------------------------
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
        return self._execute('resumeEchoRequest', payload=payload, response_object=None)

    def SendBarrierRequest(self, *args, **kwargs):
        """Executes the sendBarrierRequest operation on the server.

        Send Barrier Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendBarrierRequest(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendBarrierRequest(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendBarrierRequest(Arg2=list)list
        ---------------------------------
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
        return self._execute('sendBarrierRequest', payload=payload, response_object=None)

    def SendConfigRequest(self, *args, **kwargs):
        """Executes the sendConfigRequest operation on the server.

        Send Config Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendConfigRequest(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendConfigRequest(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendConfigRequest(Arg2=list)list
        --------------------------------
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
        return self._execute('sendConfigRequest', payload=payload, response_object=None)

    def SendDescriptionStatRequest(self, *args, **kwargs):
        """Executes the sendDescriptionStatRequest operation on the server.

        Send Description Stat Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendDescriptionStatRequest(SessionIndices=list)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendDescriptionStatRequest(SessionIndices=string)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendDescriptionStatRequest(Arg2=list)list
        -----------------------------------------
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
        return self._execute('sendDescriptionStatRequest', payload=payload, response_object=None)

    def SendEchoRequest(self, *args, **kwargs):
        """Executes the sendEchoRequest operation on the server.

        Send Echo Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendEchoRequest(EnableEchoTimeout=bool, EchoTimeoutVal=number)
        --------------------------------------------------------------
        - EnableEchoTimeout (bool): This parameter requires a enableEchoTimeout of type kBool
        - EchoTimeoutVal (number): This parameter requires a echoTimeoutVal of type kInteger

        sendEchoRequest(EnableEchoTimeout=bool, EchoTimeoutVal=number, SessionIndices=list)
        -----------------------------------------------------------------------------------
        - EnableEchoTimeout (bool): This parameter requires a enableEchoTimeout of type kBool
        - EchoTimeoutVal (number): This parameter requires a echoTimeoutVal of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendEchoRequest(SessionIndices=string, EnableEchoTimeout=bool, EchoTimeoutVal=number)
        -------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a enableEchoTimeout of type kBool
        - EnableEchoTimeout (bool): This parameter requires a echoTimeoutVal of type kInteger
        - EchoTimeoutVal (number): This parameter requires a string of session numbers 1-4;6;7-12

        sendEchoRequest(Arg2=list, Arg3=bool, Arg4=number)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (bool): Enable Echo Timeout
        - Arg4 (number): Echo Timeout Value
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendEchoRequest', payload=payload, response_object=None)

    def SendExperimenterMessage(self, *args, **kwargs):
        """Executes the sendExperimenterMessage operation on the server.

        Send Experimenter Message

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendExperimenterMessage(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string)
        -------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString

        sendExperimenterMessage(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, SessionIndices=list)
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendExperimenterMessage(SessionIndices=string, ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string)
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a experimenterDataLength of type kInteger
        - ExperimenterDataLength (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a experimenterData of type kString
        - ExperimenterData (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendExperimenterMessage(Arg2=list, Arg3=number, Arg4=number, Arg5=number, Arg6=string)list
        ------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Experimenter Data Length.
        - Arg4 (number): Experimenter ID.
        - Arg5 (number): Experimenter ID
        - Arg6 (str): Experimenter Data in Hex.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendExperimenterMessage', payload=payload, response_object=None)

    def SendExperimenterStatRequest(self, *args, **kwargs):
        """Executes the sendExperimenterStatRequest operation on the server.

        Send Experimenter Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendExperimenterStatRequest(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string)
        -----------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString

        sendExperimenterStatRequest(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, SessionIndices=list)
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendExperimenterStatRequest(SessionIndices=string, ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string)
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a experimenterDataLength of type kInteger
        - ExperimenterDataLength (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a experimenterData of type kString
        - ExperimenterData (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendExperimenterStatRequest(Arg2=list, Arg3=number, Arg4=number, Arg5=number, Arg6=string)list
        ----------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Experimenter Data Length.
        - Arg4 (number): Experimenter ID.
        - Arg5 (number): Experimenter ID
        - Arg6 (str): Experimenter Data in Hex.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendExperimenterStatRequest', payload=payload, response_object=None)

    def SendFeatureRequest(self, *args, **kwargs):
        """Executes the sendFeatureRequest operation on the server.

        Send Feature Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendFeatureRequest(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendFeatureRequest(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendFeatureRequest(Arg2=list)list
        ---------------------------------
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
        return self._execute('sendFeatureRequest', payload=payload, response_object=None)

    def SendGetQueueConfigRequest(self, *args, **kwargs):
        """Executes the sendGetQueueConfigRequest operation on the server.

        Send Queue Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGetQueueConfigRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null)
        -------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

        sendGetQueueConfigRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list)
        ----------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendGetQueueConfigRequest(SessionIndices=string, OutputPortType=enum, ErrorUnsupportedTypeFormat=null)
        ------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

        sendGetQueueConfigRequest(Arg2=list, Arg3=enum, Arg4=number)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | mANUAL | oFPP_TABLE | oFPP_NONE | oFPP_ANY)): Output Port Type
        - Arg4 (number): Port ID
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendGetQueueConfigRequest', payload=payload, response_object=None)

    def SendGroupDescriptionRequest(self, *args, **kwargs):
        """Executes the sendGroupDescriptionRequest operation on the server.

        Send Group Description Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGroupDescriptionRequest(SessionIndices=list)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendGroupDescriptionRequest(SessionIndices=string)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendGroupDescriptionRequest(Arg2=list)list
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
        return self._execute('sendGroupDescriptionRequest', payload=payload, response_object=None)

    def SendGroupFeaturesRequest(self, *args, **kwargs):
        """Executes the sendGroupFeaturesRequest operation on the server.

        Send Group Features Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGroupFeaturesRequest(SessionIndices=list)
        ---------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendGroupFeaturesRequest(SessionIndices=string)
        -----------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendGroupFeaturesRequest(Arg2=list)list
        ---------------------------------------
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
        return self._execute('sendGroupFeaturesRequest', payload=payload, response_object=None)

    def SendGroupStatsRequest(self, *args, **kwargs):
        """Executes the sendGroupStatsRequest operation on the server.

        Send Group Stats Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGroupStatsRequest(GroupIDType=enum, GroupID=number)
        -------------------------------------------------------
        - GroupIDType (str(enumOpt-Manual | enumOpt-OFPG_ALL | enumOpt-OFPG_ANY)): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
        - GroupID (number): This parameter requires a groupID of type kInteger

        sendGroupStatsRequest(GroupIDType=enum, GroupID=number, SessionIndices=list)
        ----------------------------------------------------------------------------
        - GroupIDType (str(enumOpt-Manual | enumOpt-OFPG_ALL | enumOpt-OFPG_ANY)): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
        - GroupID (number): This parameter requires a groupID of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendGroupStatsRequest(SessionIndices=string, GroupIDType=enum, GroupID=number)
        ------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
        - GroupIDType (str(enumOpt-Manual | enumOpt-OFPG_ALL | enumOpt-OFPG_ANY)): This parameter requires a groupID of type kInteger
        - GroupID (number): This parameter requires a string of session numbers 1-4;6;7-12

        sendGroupStatsRequest(Arg2=list, Arg3=enum, Arg4=number)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPG_ALL | oFPG_ANY | manual)): Group ID Type
        - Arg4 (number): Group ID
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendGroupStatsRequest', payload=payload, response_object=None)

    def SendMeterConfigRequest(self, *args, **kwargs):
        """Executes the sendMeterConfigRequest operation on the server.

        Send Meter Config Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendMeterConfigRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null)
        -------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

        sendMeterConfigRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list)
        ----------------------------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendMeterConfigRequest(SessionIndices=string, MeterIDType=enum, ErrorUnsupportedTypeFormat=null)
        ------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

        sendMeterConfigRequest(Arg2=list, Arg3=enum, Arg4=number)list
        -------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPM_SLOWPATH | oFPM_CONTROLLER | all | manual)): Meter ID Type
        - Arg4 (number): Meter ID
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendMeterConfigRequest', payload=payload, response_object=None)

    def SendMeterFeaturesRequest(self, *args, **kwargs):
        """Executes the sendMeterFeaturesRequest operation on the server.

        Send Meter Features Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendMeterFeaturesRequest(SessionIndices=list)
        ---------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendMeterFeaturesRequest(SessionIndices=string)
        -----------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendMeterFeaturesRequest(Arg2=list)list
        ---------------------------------------
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
        return self._execute('sendMeterFeaturesRequest', payload=payload, response_object=None)

    def SendMeterStatRequest(self, *args, **kwargs):
        """Executes the sendMeterStatRequest operation on the server.

        Send Meter Stat Request to Switch.

        sendMeterStatRequest(Arg2=list, Arg3=enum, Arg4=number)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPM_SLOWPATH | oFPM_CONTROLLER | all | manual)): Meter ID Type
        - Arg4 (number): Meter ID
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendMeterStatRequest', payload=payload, response_object=None)

    def SendMeterStatsRequest(self, *args, **kwargs):
        """Executes the sendMeterStatsRequest operation on the server.

        Send Meter Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendMeterStatsRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null)
        ------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

        sendMeterStatsRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list)
        ---------------------------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendMeterStatsRequest(SessionIndices=string, MeterIDType=enum, ErrorUnsupportedTypeFormat=null)
        -----------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendMeterStatsRequest', payload=payload, response_object=None)

    def SendPortDescription(self, *args, **kwargs):
        """Executes the sendPortDescription operation on the server.

        Send Port Description

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPortDescription(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendPortDescription(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendPortDescription(Arg2=list)list
        ----------------------------------
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
        return self._execute('sendPortDescription', payload=payload, response_object=None)

    def SendPortStatsRequest(self, *args, **kwargs):
        """Executes the sendPortStatsRequest operation on the server.

        Send Port Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPortStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null)
        --------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY | enumOpt-OFPP_NONE)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

        sendPortStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list)
        -----------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY | enumOpt-OFPP_NONE)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendPortStatsRequest(SessionIndices=string, OutputPortType=enum, ErrorUnsupportedTypeFormat=null)
        -------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY | enumOpt-OFPP_NONE)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

        sendPortStatsRequest(Arg2=list, Arg3=enum, Arg4=number)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | mANUAL | oFPP_TABLE | oFPP_NONE | oFPP_ANY)): Output Port Type
        - Arg4 (number): Port ID
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPortStatsRequest', payload=payload, response_object=None)

    def SendQueueStatsRequest(self, *args, **kwargs):
        """Executes the sendQueueStatsRequest operation on the server.

        Send Queue Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendQueueStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, QueueType=enum, ErrorUnsupportedTypeFormat=null)
        ----------------------------------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - QueueType (str(enumOpt-MANUAL | enumOpt-OFPQ_ALL)): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

        sendQueueStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, QueueType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list)
        -------------------------------------------------------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - QueueType (str(enumOpt-MANUAL | enumOpt-OFPQ_ALL)): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendQueueStatsRequest(SessionIndices=string, OutputPortType=enum, ErrorUnsupportedTypeFormat=null, QueueType=enum, ErrorUnsupportedTypeFormat=null)
        ---------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
        - QueueType (str(enumOpt-MANUAL | enumOpt-OFPQ_ALL)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

        sendQueueStatsRequest(Arg2=list, Arg3=enum, Arg4=number, Arg5=enum, Arg6=number)list
        ------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | mANUAL | oFPP_TABLE | oFPP_NONE | oFPP_ANY)): Output Port Type
        - Arg4 (number): Port ID
        - Arg5 (str(oFPQ_ALL | manual)): Queue Type
        - Arg6 (number): Queue ID
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendQueueStatsRequest', payload=payload, response_object=None)

    def SendTableModRequest(self, *args, **kwargs):
        """Executes the sendTableModRequest operation on the server.

        Send Table Mod Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendTableModRequest(TableIdType=enum, TableId=number, ErrorUnsupportedTypeFormat=null)
        --------------------------------------------------------------------------------------
        - TableIdType (str(enumOpt-ALL_TABLE | enumOpt-MANUAL)): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
        - TableId (number): This parameter requires a tableId of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

        sendTableModRequest(TableIdType=enum, TableId=number, ErrorUnsupportedTypeFormat=null, SessionIndices=list)
        -----------------------------------------------------------------------------------------------------------
        - TableIdType (str(enumOpt-ALL_TABLE | enumOpt-MANUAL)): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
        - TableId (number): This parameter requires a tableId of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendTableModRequest(SessionIndices=string, TableIdType=enum, TableId=number, ErrorUnsupportedTypeFormat=null)
        -------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
        - TableIdType (str(enumOpt-ALL_TABLE | enumOpt-MANUAL)): This parameter requires a tableId of type kInteger
        - TableId (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

        sendTableModRequest(Arg2=list, Arg3=enum, Arg4=number, Arg5=number)list
        -----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(aLL_TABLE | manual)): Table ID Type
        - Arg4 (number): Table ID
        - Arg5 (number): Table Config
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendTableModRequest', payload=payload, response_object=None)

    def SendTableStatsRequest(self, *args, **kwargs):
        """Executes the sendTableStatsRequest operation on the server.

        Send Table Stats Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendTableStatsRequest(SessionIndices=list)
        ------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendTableStatsRequest(SessionIndices=string)
        --------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendTableStatsRequest(Arg2=list)list
        ------------------------------------
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
        return self._execute('sendTableStatsRequest', payload=payload, response_object=None)

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

    def StartChannel(self, *args, **kwargs):
        """Executes the startChannel operation on the server.

        Start OpenFlow Channel

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startChannel(SessionIndices=list)
        ---------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        startChannel(SessionIndices=string)
        -----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startChannel', payload=payload, response_object=None)

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

    def StopChannel(self, *args, **kwargs):
        """Executes the stopChannel operation on the server.

        Stop OpenFlow Channel

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopChannel(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopChannel(SessionIndices=string)
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
        return self._execute('stopChannel', payload=payload, response_object=None)
