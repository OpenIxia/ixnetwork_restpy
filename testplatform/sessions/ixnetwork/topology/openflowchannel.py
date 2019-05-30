# Copyright 1997 - 2018 by IXIA Keysight
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
	"""The OpenFlowChannel class encapsulates a user managed openFlowChannel node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the OpenFlowChannel property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'openFlowChannel'

	def __init__(self, parent):
		super(OpenFlowChannel, self).__init__(parent)

	@property
	def Groups(self):
		"""An instance of the Groups class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.groups.Groups)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.groups import Groups
		return Groups(self)

	@property
	def Meters(self):
		"""An instance of the Meters class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.meters.Meters)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.meters import Meters
		return Meters(self)

	@property
	def Tables(self):
		"""An instance of the Tables class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tables.Tables)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tables import Tables
		return Tables(self)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def CalcFlowRate(self):
		"""If selected, the statistics on the rate of transmission of flows per second by the controller is published.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('calcFlowRate')

	@property
	def CalcFlowRateWithBarrier(self):
		"""If selected, statistics on the rate of transmission of flows per second by the controller, along with Barrier Request messages is published.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('calcFlowRateWithBarrier')

	@property
	def ConnectedVia(self):
		"""List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('connectedVia')
	@ConnectedVia.setter
	def ConnectedVia(self, value):
		self._set_attribute('connectedVia', value)

	@property
	def ControllerIndex(self):
		"""Parent Controller Index

		Returns:
			list(str)
		"""
		return self._get_attribute('controllerIndex')

	@property
	def ControllerName(self):
		"""Parent Controller Name

		Returns:
			str
		"""
		return self._get_attribute('controllerName')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DatapathId(self):
		"""The Datapath ID of the OF Channel.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('datapathId')

	@property
	def DatapathIdHex(self):
		"""The Datapath ID in hexadecimal format.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('datapathIdHex')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableHelloElement(self):
		"""If selected, the Controller sends a hello message consisting of an OpenFlow header and a set of variable size hello elements to inform the initial handshake of the connection.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableHelloElement')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def FlowTxBurstSize(self):
		"""Specify the number of Flow transmitting packets that can be sent in a single burst within the time frame specified by the Inter Flow Burst Gap value.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flowTxBurstSize')

	@property
	def GroupsPerChannel(self):
		"""Number of Groups per Channel

		Returns:
			number
		"""
		return self._get_attribute('groupsPerChannel')
	@GroupsPerChannel.setter
	def GroupsPerChannel(self, value):
		self._set_attribute('groupsPerChannel', value)

	@property
	def InterFlowBurstGap(self):
		"""Specify the duration (in milliseconds) for which the controller waits between successive flow advertisements.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interFlowBurstGap')

	@property
	def LocalIp(self):
		"""The local IP address of the interface. This field is auto-populated and cannot be changed.

		Returns:
			list(str)
		"""
		return self._get_attribute('localIp')

	@property
	def MaxFlowsAtATime(self):
		"""The Max Number of Flows Processed at a Time is the size of an internal buffer maintained by the Ixiacontroller, which prevents it from sending more flows than the Openflow switch can consume at a time.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxFlowsAtATime')

	@property
	def MetersPerChannel(self):
		"""Number of Meters per Channel

		Returns:
			number
		"""
		return self._get_attribute('metersPerChannel')
	@MetersPerChannel.setter
	def MetersPerChannel(self, value):
		self._set_attribute('metersPerChannel', value)

	@property
	def Multiplier(self):
		"""Number of layer instances per parent instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def RemoteIp(self):
		"""The IP address of the DUT at the other end of the OF Channel.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteIp')

	@property
	def SendRoleRequest(self):
		"""If selected, the controller sends a Role Request message after the connection is established; to change its role according to the Role Request option selected.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendRoleRequest')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def StackedLayers(self):
		"""List of secondary (many to one) child layer protocols

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('stackedLayers')
	@StackedLayers.setter
	def StackedLayers(self, value):
		self._set_attribute('stackedLayers', value)

	@property
	def StartupGenerationId(self):
		"""A 64-bit sequence number field that identifies a given mastership view.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('startupGenerationId')

	@property
	def StartupRoleRequest(self):
		"""This defines role of the controller.Options include: 1) No Change 2) Equal 3) Master 4) Slave

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('startupRoleRequest')

	@property
	def StateCounts(self):
		"""A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

		Returns:
			dict(total:number,notStarted:number,down:number,up:number)
		"""
		return self._get_attribute('stateCounts')

	@property
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	@property
	def TablesPerChannel(self):
		"""Number of Tables per Channel

		Returns:
			number
		"""
		return self._get_attribute('tablesPerChannel')
	@TablesPerChannel.setter
	def TablesPerChannel(self, value):
		self._set_attribute('tablesPerChannel', value)

	@property
	def UseDatapathID(self):
		"""If selected, the Datapath ID and IP address are used as the OF Channel identifier.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useDatapathID')

	def update(self, ConnectedVia=None, GroupsPerChannel=None, MetersPerChannel=None, Multiplier=None, Name=None, StackedLayers=None, TablesPerChannel=None):
		"""Updates a child instance of openFlowChannel on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			GroupsPerChannel (number): Number of Groups per Channel
			MetersPerChannel (number): Number of Meters per Channel
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			TablesPerChannel (number): Number of Tables per Channel

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, GroupsPerChannel=None, MetersPerChannel=None, Multiplier=None, Name=None, StackedLayers=None, TablesPerChannel=None):
		"""Adds a new openFlowChannel node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			GroupsPerChannel (number): Number of Groups per Channel
			MetersPerChannel (number): Number of Meters per Channel
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			TablesPerChannel (number): Number of Tables per Channel

		Returns:
			self: This instance with all currently retrieved openFlowChannel data using find and the newly added openFlowChannel data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the openFlowChannel data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, ControllerIndex=None, ControllerName=None, Count=None, DescriptiveName=None, Errors=None, GroupsPerChannel=None, LocalIp=None, MetersPerChannel=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TablesPerChannel=None):
		"""Finds and retrieves openFlowChannel data from the server.

		All named parameters support regex and can be used to selectively retrieve openFlowChannel data from the server.
		By default the find method takes no parameters and will retrieve all openFlowChannel data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ControllerIndex (list(str)): Parent Controller Index
			ControllerName (str): Parent Controller Name
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			GroupsPerChannel (number): Number of Groups per Channel
			LocalIp (list(str)): The local IP address of the interface. This field is auto-populated and cannot be changed.
			MetersPerChannel (number): Number of Meters per Channel
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TablesPerChannel (number): Number of Tables per Channel

		Returns:
			self: This instance with matching openFlowChannel data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of openFlowChannel data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the openFlowChannel data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, CalcFlowRate=None, CalcFlowRateWithBarrier=None, DatapathId=None, DatapathIdHex=None, EnableHelloElement=None, FlowTxBurstSize=None, InterFlowBurstGap=None, MaxFlowsAtATime=None, RemoteIp=None, SendRoleRequest=None, StartupGenerationId=None, StartupRoleRequest=None, UseDatapathID=None):
		"""Base class infrastructure that gets a list of openFlowChannel device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			CalcFlowRate (str): optional regex of calcFlowRate
			CalcFlowRateWithBarrier (str): optional regex of calcFlowRateWithBarrier
			DatapathId (str): optional regex of datapathId
			DatapathIdHex (str): optional regex of datapathIdHex
			EnableHelloElement (str): optional regex of enableHelloElement
			FlowTxBurstSize (str): optional regex of flowTxBurstSize
			InterFlowBurstGap (str): optional regex of interFlowBurstGap
			MaxFlowsAtATime (str): optional regex of maxFlowsAtATime
			RemoteIp (str): optional regex of remoteIp
			SendRoleRequest (str): optional regex of sendRoleRequest
			StartupGenerationId (str): optional regex of startupGenerationId
			StartupRoleRequest (str): optional regex of startupRoleRequest
			UseDatapathID (str): optional regex of useDatapathID

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		fetchAndUpdateConfigFromCloud(Mode:string)
			Args:
				args[0] is Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

	def GetAsynchronousConfiguration(self, *args, **kwargs):
		"""Executes the getAsynchronousConfiguration operation on the server.

		Get Asynchronous Configurationr

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getAsynchronousConfiguration()

		getAsynchronousConfiguration(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getAsynchronousConfiguration(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getAsynchronousConfiguration(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getAsynchronousConfiguration', payload=payload, response_object=None)

	def InvokeSendRoleRequest(self, *args, **kwargs):
		"""Executes the invokeSendRoleRequest operation on the server.

		Sends a Role Request for selected Channel.

		invokeSendRoleRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices in channel grid

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('invokeSendRoleRequest', payload=payload, response_object=None)

	def PauseEchoReply(self, *args, **kwargs):
		"""Executes the pauseEchoReply operation on the server.

		Pause Sending Echo Reply Messages

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		pauseEchoReply()

		pauseEchoReply(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		pauseEchoReply(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		pauseEchoReply(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('pauseEchoReply', payload=payload, response_object=None)

	def PauseEchoRequest(self, *args, **kwargs):
		"""Executes the pauseEchoRequest operation on the server.

		Pause Sending Echo Request Messages

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		pauseEchoRequest()

		pauseEchoRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		pauseEchoRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		pauseEchoRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('pauseEchoRequest', payload=payload, response_object=None)

	def RestartDown(self, *args, **kwargs):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		restartDown()

		restartDown(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		restartDown(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('restartDown', payload=payload, response_object=None)

	def ResumeEchoReply(self, *args, **kwargs):
		"""Executes the resumeEchoReply operation on the server.

		Resume Sending Echo Reply Messages

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		resumeEchoReply()

		resumeEchoReply(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		resumeEchoReply(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		resumeEchoReply(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumeEchoReply', payload=payload, response_object=None)

	def ResumeEchoRequest(self, *args, **kwargs):
		"""Executes the resumeEchoRequest operation on the server.

		Resume Sending Echo Request Messages

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		resumeEchoRequest()

		resumeEchoRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		resumeEchoRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		resumeEchoRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumeEchoRequest', payload=payload, response_object=None)

	def SendBarrierRequest(self, *args, **kwargs):
		"""Executes the sendBarrierRequest operation on the server.

		Send Barrier Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendBarrierRequest()

		sendBarrierRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendBarrierRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendBarrierRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendBarrierRequest', payload=payload, response_object=None)

	def SendConfigRequest(self, *args, **kwargs):
		"""Executes the sendConfigRequest operation on the server.

		Send Config Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendConfigRequest()

		sendConfigRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendConfigRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendConfigRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendConfigRequest', payload=payload, response_object=None)

	def SendDescriptionStatRequest(self, *args, **kwargs):
		"""Executes the sendDescriptionStatRequest operation on the server.

		Send Description Stat Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendDescriptionStatRequest()

		sendDescriptionStatRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendDescriptionStatRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendDescriptionStatRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendDescriptionStatRequest', payload=payload, response_object=None)

	def SendEchoRequest(self, *args, **kwargs):
		"""Executes the sendEchoRequest operation on the server.

		Send Echo Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendEchoRequest(EnableEchoTimeout:bool, EchoTimeoutVal:number)
			Args:
				args[0] is EnableEchoTimeout (bool): This parameter requires a enableEchoTimeout of type kBool
				args[1] is EchoTimeoutVal (number): This parameter requires a echoTimeoutVal of type kInteger

		sendEchoRequest(EnableEchoTimeout:bool, EchoTimeoutVal:number, SessionIndices:list)
			Args:
				args[0] is EnableEchoTimeout (bool): This parameter requires a enableEchoTimeout of type kBool
				args[1] is EchoTimeoutVal (number): This parameter requires a echoTimeoutVal of type kInteger
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendEchoRequest(SessionIndices:string, EnableEchoTimeout:bool, EchoTimeoutVal:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a enableEchoTimeout of type kBool
				args[1] is EnableEchoTimeout (bool): This parameter requires a echoTimeoutVal of type kInteger
				args[2] is EchoTimeoutVal (number): This parameter requires a string of session numbers 1-4;6;7-12

		sendEchoRequest(Arg2:list, Arg3:bool, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (bool): Enable Echo Timeout
				args[2] is Arg4 (number): Echo Timeout Value

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendEchoRequest', payload=payload, response_object=None)

	def SendExperimenterMessage(self, *args, **kwargs):
		"""Executes the sendExperimenterMessage operation on the server.

		Send Experimenter Message

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendExperimenterMessage(ExperimenterDataLength:number, ErrorUnsupportedTypeFormat:null, ErrorUnsupportedTypeFormat:null, ExperimenterData:string)
			Args:
				args[0] is ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ExperimenterData (str): This parameter requires a experimenterData of type kString

		sendExperimenterMessage(ExperimenterDataLength:number, ErrorUnsupportedTypeFormat:null, ErrorUnsupportedTypeFormat:null, ExperimenterData:string, SessionIndices:list)
			Args:
				args[0] is ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ExperimenterData (str): This parameter requires a experimenterData of type kString
				args[4] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendExperimenterMessage(SessionIndices:string, ExperimenterDataLength:number, ErrorUnsupportedTypeFormat:null, ErrorUnsupportedTypeFormat:null, ExperimenterData:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a experimenterDataLength of type kInteger
				args[1] is ExperimenterDataLength (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ErrorUnsupportedTypeFormat (null): This parameter requires a experimenterData of type kString
				args[4] is ExperimenterData (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendExperimenterMessage(Arg2:list, Arg3:number, Arg4:number, Arg5:number, Arg6:string)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (number): Experimenter Data Length.
				args[2] is Arg4 (number): Experimenter ID.
				args[3] is Arg5 (number): Experimenter ID
				args[4] is Arg6 (str): Experimenter Data in Hex.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendExperimenterMessage', payload=payload, response_object=None)

	def SendExperimenterStatRequest(self, *args, **kwargs):
		"""Executes the sendExperimenterStatRequest operation on the server.

		Send Experimenter Stats Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendExperimenterStatRequest(ExperimenterDataLength:number, ErrorUnsupportedTypeFormat:null, ErrorUnsupportedTypeFormat:null, ExperimenterData:string)
			Args:
				args[0] is ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ExperimenterData (str): This parameter requires a experimenterData of type kString

		sendExperimenterStatRequest(ExperimenterDataLength:number, ErrorUnsupportedTypeFormat:null, ErrorUnsupportedTypeFormat:null, ExperimenterData:string, SessionIndices:list)
			Args:
				args[0] is ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ExperimenterData (str): This parameter requires a experimenterData of type kString
				args[4] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendExperimenterStatRequest(SessionIndices:string, ExperimenterDataLength:number, ErrorUnsupportedTypeFormat:null, ErrorUnsupportedTypeFormat:null, ExperimenterData:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a experimenterDataLength of type kInteger
				args[1] is ExperimenterDataLength (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ErrorUnsupportedTypeFormat (null): This parameter requires a experimenterData of type kString
				args[4] is ExperimenterData (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendExperimenterStatRequest(Arg2:list, Arg3:number, Arg4:number, Arg5:number, Arg6:string)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (number): Experimenter Data Length.
				args[2] is Arg4 (number): Experimenter ID.
				args[3] is Arg5 (number): Experimenter ID
				args[4] is Arg6 (str): Experimenter Data in Hex.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendExperimenterStatRequest', payload=payload, response_object=None)

	def SendFeatureRequest(self, *args, **kwargs):
		"""Executes the sendFeatureRequest operation on the server.

		Send Feature Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendFeatureRequest()

		sendFeatureRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendFeatureRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendFeatureRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendFeatureRequest', payload=payload, response_object=None)

	def SendGetQueueConfigRequest(self, *args, **kwargs):
		"""Executes the sendGetQueueConfigRequest operation on the server.

		Send Queue Stats Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendGetQueueConfigRequest(OutputPortType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

		sendGetQueueConfigRequest(OutputPortType:enum, ErrorUnsupportedTypeFormat:null, SessionIndices:list)
			Args:
				args[0] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendGetQueueConfigRequest(SessionIndices:string, OutputPortType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
				args[1] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

		sendGetQueueConfigRequest(Arg2:list, Arg3:enum, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(mANUAL|oFPP_ALL|oFPP_ANY|oFPP_CONTROLLER|oFPP_FLOOD|oFPP_IN_PORT|oFPP_LOCAL|oFPP_NONE|oFPP_NORMAL|oFPP_TABLE)): Output Port Type
				args[2] is Arg4 (number): Port ID

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendGetQueueConfigRequest', payload=payload, response_object=None)

	def SendGroupDescriptionRequest(self, *args, **kwargs):
		"""Executes the sendGroupDescriptionRequest operation on the server.

		Send Group Description Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendGroupDescriptionRequest()

		sendGroupDescriptionRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendGroupDescriptionRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendGroupDescriptionRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendGroupDescriptionRequest', payload=payload, response_object=None)

	def SendGroupFeaturesRequest(self, *args, **kwargs):
		"""Executes the sendGroupFeaturesRequest operation on the server.

		Send Group Features Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendGroupFeaturesRequest()

		sendGroupFeaturesRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendGroupFeaturesRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendGroupFeaturesRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendGroupFeaturesRequest', payload=payload, response_object=None)

	def SendGroupStatsRequest(self, *args, **kwargs):
		"""Executes the sendGroupStatsRequest operation on the server.

		Send Group Stats Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendGroupStatsRequest(GroupIDType:enum, GroupID:number)
			Args:
				args[0] is GroupIDType (str(enumOpt-Manual|enumOpt-OFPG_ALL|enumOpt-OFPG_ANY)): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
				args[1] is GroupID (number): This parameter requires a groupID of type kInteger

		sendGroupStatsRequest(GroupIDType:enum, GroupID:number, SessionIndices:list)
			Args:
				args[0] is GroupIDType (str(enumOpt-Manual|enumOpt-OFPG_ALL|enumOpt-OFPG_ANY)): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
				args[1] is GroupID (number): This parameter requires a groupID of type kInteger
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendGroupStatsRequest(SessionIndices:string, GroupIDType:enum, GroupID:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
				args[1] is GroupIDType (str(enumOpt-Manual|enumOpt-OFPG_ALL|enumOpt-OFPG_ANY)): This parameter requires a groupID of type kInteger
				args[2] is GroupID (number): This parameter requires a string of session numbers 1-4;6;7-12

		sendGroupStatsRequest(Arg2:list, Arg3:enum, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(manual|oFPG_ALL|oFPG_ANY)): Group ID Type
				args[2] is Arg4 (number): Group ID

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendGroupStatsRequest', payload=payload, response_object=None)

	def SendMeterConfigRequest(self, *args, **kwargs):
		"""Executes the sendMeterConfigRequest operation on the server.

		Send Meter Config Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendMeterConfigRequest(MeterIDType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is MeterIDType (str(enumOpt-ALL|enumOpt-MANUAL|enumOpt-OFPM_CONTROLLER|enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

		sendMeterConfigRequest(MeterIDType:enum, ErrorUnsupportedTypeFormat:null, SessionIndices:list)
			Args:
				args[0] is MeterIDType (str(enumOpt-ALL|enumOpt-MANUAL|enumOpt-OFPM_CONTROLLER|enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendMeterConfigRequest(SessionIndices:string, MeterIDType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is SessionIndices (str): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
				args[1] is MeterIDType (str(enumOpt-ALL|enumOpt-MANUAL|enumOpt-OFPM_CONTROLLER|enumOpt-OFPM_SLOWPATH)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

		sendMeterConfigRequest(Arg2:list, Arg3:enum, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(all|manual|oFPM_CONTROLLER|oFPM_SLOWPATH)): Meter ID Type
				args[2] is Arg4 (number): Meter ID

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendMeterConfigRequest', payload=payload, response_object=None)

	def SendMeterFeaturesRequest(self, *args, **kwargs):
		"""Executes the sendMeterFeaturesRequest operation on the server.

		Send Meter Features Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendMeterFeaturesRequest()

		sendMeterFeaturesRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendMeterFeaturesRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendMeterFeaturesRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendMeterFeaturesRequest', payload=payload, response_object=None)

	def SendMeterStatRequest(self, *args, **kwargs):
		"""Executes the sendMeterStatRequest operation on the server.

		Send Meter Stat Request to Switch.

		sendMeterStatRequest(Arg2:list, Arg3:enum, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(all|manual|oFPM_CONTROLLER|oFPM_SLOWPATH)): Meter ID Type
				args[2] is Arg4 (number): Meter ID

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendMeterStatRequest', payload=payload, response_object=None)

	def SendMeterStatsRequest(self, *args, **kwargs):
		"""Executes the sendMeterStatsRequest operation on the server.

		Send Meter Stats Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendMeterStatsRequest(MeterIDType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is MeterIDType (str(enumOpt-ALL|enumOpt-MANUAL|enumOpt-OFPM_CONTROLLER|enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

		sendMeterStatsRequest(MeterIDType:enum, ErrorUnsupportedTypeFormat:null, SessionIndices:list)
			Args:
				args[0] is MeterIDType (str(enumOpt-ALL|enumOpt-MANUAL|enumOpt-OFPM_CONTROLLER|enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendMeterStatsRequest(SessionIndices:string, MeterIDType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is SessionIndices (str): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
				args[1] is MeterIDType (str(enumOpt-ALL|enumOpt-MANUAL|enumOpt-OFPM_CONTROLLER|enumOpt-OFPM_SLOWPATH)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendMeterStatsRequest', payload=payload, response_object=None)

	def SendPortDescription(self, *args, **kwargs):
		"""Executes the sendPortDescription operation on the server.

		Send Port Description

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendPortDescription()

		sendPortDescription(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendPortDescription(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendPortDescription(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendPortDescription', payload=payload, response_object=None)

	def SendPortStatsRequest(self, *args, **kwargs):
		"""Executes the sendPortStatsRequest operation on the server.

		Send Port Stats Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendPortStatsRequest(OutputPortType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY|enumOpt-OFPP_NONE)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

		sendPortStatsRequest(OutputPortType:enum, ErrorUnsupportedTypeFormat:null, SessionIndices:list)
			Args:
				args[0] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY|enumOpt-OFPP_NONE)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendPortStatsRequest(SessionIndices:string, OutputPortType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
				args[1] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY|enumOpt-OFPP_NONE)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

		sendPortStatsRequest(Arg2:list, Arg3:enum, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(mANUAL|oFPP_ALL|oFPP_ANY|oFPP_CONTROLLER|oFPP_FLOOD|oFPP_IN_PORT|oFPP_LOCAL|oFPP_NONE|oFPP_NORMAL|oFPP_TABLE)): Output Port Type
				args[2] is Arg4 (number): Port ID

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendPortStatsRequest', payload=payload, response_object=None)

	def SendQueueStatsRequest(self, *args, **kwargs):
		"""Executes the sendQueueStatsRequest operation on the server.

		Send Queue Stats Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendQueueStatsRequest(OutputPortType:enum, ErrorUnsupportedTypeFormat:null, QueueType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is QueueType (str(enumOpt-MANUAL|enumOpt-OFPQ_ALL)): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
				args[3] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

		sendQueueStatsRequest(OutputPortType:enum, ErrorUnsupportedTypeFormat:null, QueueType:enum, ErrorUnsupportedTypeFormat:null, SessionIndices:list)
			Args:
				args[0] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
				args[1] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is QueueType (str(enumOpt-MANUAL|enumOpt-OFPQ_ALL)): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
				args[3] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[4] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendQueueStatsRequest(SessionIndices:string, OutputPortType:enum, ErrorUnsupportedTypeFormat:null, QueueType:enum, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
				args[1] is OutputPortType (str(enumOpt-MANUAL|enumOpt-OFPP_ANY)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
				args[3] is QueueType (str(enumOpt-MANUAL|enumOpt-OFPQ_ALL)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[4] is ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

		sendQueueStatsRequest(Arg2:list, Arg3:enum, Arg4:number, Arg5:enum, Arg6:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(mANUAL|oFPP_ALL|oFPP_ANY|oFPP_CONTROLLER|oFPP_FLOOD|oFPP_IN_PORT|oFPP_LOCAL|oFPP_NONE|oFPP_NORMAL|oFPP_TABLE)): Output Port Type
				args[2] is Arg4 (number): Port ID
				args[3] is Arg5 (str(manual|oFPQ_ALL)): Queue Type
				args[4] is Arg6 (number): Queue ID

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendQueueStatsRequest', payload=payload, response_object=None)

	def SendTableModRequest(self, *args, **kwargs):
		"""Executes the sendTableModRequest operation on the server.

		Send Table Mod Request

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendTableModRequest(TableIdType:enum, TableId:number, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is TableIdType (str(enumOpt-ALL_TABLE|enumOpt-MANUAL)): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
				args[1] is TableId (number): This parameter requires a tableId of type kInteger
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid

		sendTableModRequest(TableIdType:enum, TableId:number, ErrorUnsupportedTypeFormat:null, SessionIndices:list)
			Args:
				args[0] is TableIdType (str(enumOpt-ALL_TABLE|enumOpt-MANUAL)): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
				args[1] is TableId (number): This parameter requires a tableId of type kInteger
				args[2] is ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendTableModRequest(SessionIndices:string, TableIdType:enum, TableId:number, ErrorUnsupportedTypeFormat:null)
			Args:
				args[0] is SessionIndices (str): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
				args[1] is TableIdType (str(enumOpt-ALL_TABLE|enumOpt-MANUAL)): This parameter requires a tableId of type kInteger
				args[2] is TableId (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
				args[3] is ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12

		sendTableModRequest(Arg2:list, Arg3:enum, Arg4:number, Arg5:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(aLL_TABLE|manual)): Table ID Type
				args[2] is Arg4 (number): Table ID
				args[3] is Arg5 (number): Table Config

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendTableModRequest', payload=payload, response_object=None)

	def SendTableStatsRequest(self, *args, **kwargs):
		"""Executes the sendTableStatsRequest operation on the server.

		Send Table Stats Request to Switch

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendTableStatsRequest()

		sendTableStatsRequest(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendTableStatsRequest(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendTableStatsRequest(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendTableStatsRequest', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start selected protocols.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def StartChannel(self, *args, **kwargs):
		"""Executes the startChannel operation on the server.

		Start OpenFlow Channel

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		startChannel()

		startChannel(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		startChannel(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('startChannel', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)

	def StopChannel(self, *args, **kwargs):
		"""Executes the stopChannel operation on the server.

		Stop OpenFlow Channel

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopChannel()

		stopChannel(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stopChannel(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopChannel', payload=payload, response_object=None)
