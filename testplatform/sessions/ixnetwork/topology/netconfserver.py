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


class NetconfServer(Base):
	"""The NetconfServer class encapsulates a user managed netconfServer node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the NetconfServer property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'netconfServer'

	def __init__(self, parent):
		super(NetconfServer, self).__init__(parent)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def CapabilitiesBase1Dot0(self):
		"""Whether base1.0 support should be advertised in Capabilities.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesBase1Dot0')

	@property
	def CapabilitiesBase1Dot1(self):
		"""Whether base1.1 support should be advertised in Capabilities.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesBase1Dot1')

	@property
	def CapabilitiesCandidate(self):
		"""Whether supports capability candidate to make changes into an intermediate candidate database. Normally this is preferred over writable-running.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesCandidate')

	@property
	def CapabilitiesConfirmedCommit(self):
		"""Whether supports capability confirmed-commit to specify ability to commit a group of commands or none as a batch.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesConfirmedCommit')

	@property
	def CapabilitiesInterleave(self):
		"""Whether supports capability interleave to interleave notifications and responses.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesInterleave')

	@property
	def CapabilitiesNotification(self):
		"""Whether supports capability notification to aynchronously send notifications to Netconf client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesNotification')

	@property
	def CapabilitiesRollbackOnError(self):
		"""Whether supports capability rollback to rollback partial changes make changes on detection of error during validate or commit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesRollbackOnError')

	@property
	def CapabilitiesStartup(self):
		"""Whether supports capability startup to make changes in config persistent on device restart.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesStartup')

	@property
	def CapabilitiesUrl(self):
		"""Whether supports capability url to specify netconf commands using url.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesUrl')

	@property
	def CapabilitiesValidate(self):
		"""Whether supports capability validate to specify ability to validate a netconf command prior to commit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesValidate')

	@property
	def CapabilitiesWritableRunning(self):
		"""Whether supports capability writable-running to directly modify running config.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesWritableRunning')

	@property
	def CapabilitiesXpath(self):
		"""Whether supports capability xpath to specify netconf commands and filters using xpath extensions.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitiesXpath')

	@property
	def ClientIpv4Address(self):
		"""Specify the IPv4 address of the Netconf Client which will connect with this Server.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('clientIpv4Address')

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
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DecryptedCapture(self):
		"""This specifies whether SSH packets for this session will be captured and stored on client in decrypted form. Note that this is not linked to IxNetwork control or data capture which will capture the packets in encrypted format only. The Decrypted Capture can be viewed by either doing right-click on a client where this option is enabled and doing Get Decrypted Capture ( allowed on 5 servers at a time ; each of the captures will be opened in a new Wireshark pop-up) OR by stopping the server and then directly opening it from the configured Output Directory from inside the current run folder/capture. This option can be enabled even when a session is already up in which case the capture will be started from that point of time.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('decryptedCapture')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def ErrorInfo(self):
		"""Contains protocol or data-model-specific error content.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('errorInfo')

	@property
	def ErrorPercentage(self):
		"""The percentage of requests whose response will be errors

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('errorPercentage')

	@property
	def ErrorSeverity(self):
		"""Contains a string identifying the error severity, as determined by the device.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('errorSeverity')

	@property
	def ErrorTag(self):
		"""Contains a string identifying the error condition.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('errorTag')

	@property
	def ErrorType(self):
		"""Defines the conceptual layer that the error occurred.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('errorType')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def GetConfigReplyXML(self):
		"""File containing the response to a <get-config> request.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('getConfigReplyXML')

	@property
	def IncludeErrorInfo(self):
		"""This specifies whether 'error-info' element should be included in rpc error messages.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeErrorInfo')

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
	def NetconfSessionState(self):
		"""Shows the current state of the Netconf SSH Session. None - Not started. Authenticated - The SSH session has been authenticated by the server using user/password or Key-based authentication. Channel Opened- SSH session is established and SSH Channel has been opened on which data will be sent. Subsystem Requested- Netconf Subsystem has been requested on top of SSH channel. Ready - The SSH session is in Ready state and waiting for Netconf data to be exchanged. Note that this does not mean that NETCONF is in Up state. That is reached only after Netconf Capabilities are negotiated and there is at least one matching Netconf version (1.0 or 1.1) supported on both client and server. Multiple connections - The server has multiple connections

		Returns:
			list(str[authenticated|channelOpened|multipleConnections|none|ready|subsystemRequested])
		"""
		return self._get_attribute('netconfSessionState')

	@property
	def OutputDirectory(self):
		"""Location of Directory in Client where the decrypted capture(if enabled) will be stored.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('outputDirectory')

	@property
	def Password(self):
		"""Password for Username/Password mode.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('password')

	@property
	def PortNumber(self):
		"""The TCP Port Number the Netconf Server is listening on to which to connect.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('portNumber')

	@property
	def PublicKeyDirectory(self):
		"""Directory containing public key file for this session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('publicKeyDirectory')

	@property
	def PublicKeyFileName(self):
		"""File containing public key (e.g. generated using ssh_keygen). For multiple server rows and assymetric public key filenames( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('publicKeyFileName')

	@property
	def ResponseXMLDirectory(self):
		"""Directory where Reply XMLs for <get-config> operations are present

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('responseXMLDirectory')

	@property
	def SendOkResponse(self):
		"""This specifies whether <ok> element should be sent in <rpc-reply> in response to <get-config> requests. If this is unchecked, custom reply based on <get-config> response xml will be sent out

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendOkResponse')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SshAuthenticationMechanism(self):
		"""The authentication mechanism for connecting to Netconf Client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sshAuthenticationMechanism')

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
	def UserName(self):
		"""Username for Username/Password mode and Username for Key-Based authentication mode if applicable.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('userName')

	def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Updates a child instance of netconfServer on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Adds a new netconfServer node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved netconfServer data using find and the newly added netconfServer data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the netconfServer data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, NetconfSessionState=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves netconfServer data from the server.

		All named parameters support regex and can be used to selectively retrieve netconfServer data from the server.
		By default the find method takes no parameters and will retrieve all netconfServer data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetconfSessionState (list(str[authenticated|channelOpened|multipleConnections|none|ready|subsystemRequested])): Shows the current state of the Netconf SSH Session. None - Not started. Authenticated - The SSH session has been authenticated by the server using user/password or Key-based authentication. Channel Opened- SSH session is established and SSH Channel has been opened on which data will be sent. Subsystem Requested- Netconf Subsystem has been requested on top of SSH channel. Ready - The SSH session is in Ready state and waiting for Netconf data to be exchanged. Note that this does not mean that NETCONF is in Up state. That is reached only after Netconf Capabilities are negotiated and there is at least one matching Netconf version (1.0 or 1.1) supported on both client and server. Multiple connections - The server has multiple connections
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching netconfServer data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of netconfServer data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the netconfServer data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, CapabilitiesBase1Dot0=None, CapabilitiesBase1Dot1=None, CapabilitiesCandidate=None, CapabilitiesConfirmedCommit=None, CapabilitiesInterleave=None, CapabilitiesNotification=None, CapabilitiesRollbackOnError=None, CapabilitiesStartup=None, CapabilitiesUrl=None, CapabilitiesValidate=None, CapabilitiesWritableRunning=None, CapabilitiesXpath=None, ClientIpv4Address=None, DecryptedCapture=None, ErrorInfo=None, ErrorPercentage=None, ErrorSeverity=None, ErrorTag=None, ErrorType=None, GetConfigReplyXML=None, IncludeErrorInfo=None, OutputDirectory=None, Password=None, PortNumber=None, PublicKeyDirectory=None, PublicKeyFileName=None, ResponseXMLDirectory=None, SendOkResponse=None, SshAuthenticationMechanism=None, UserName=None):
		"""Base class infrastructure that gets a list of netconfServer device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			CapabilitiesBase1Dot0 (str): optional regex of capabilitiesBase1Dot0
			CapabilitiesBase1Dot1 (str): optional regex of capabilitiesBase1Dot1
			CapabilitiesCandidate (str): optional regex of capabilitiesCandidate
			CapabilitiesConfirmedCommit (str): optional regex of capabilitiesConfirmedCommit
			CapabilitiesInterleave (str): optional regex of capabilitiesInterleave
			CapabilitiesNotification (str): optional regex of capabilitiesNotification
			CapabilitiesRollbackOnError (str): optional regex of capabilitiesRollbackOnError
			CapabilitiesStartup (str): optional regex of capabilitiesStartup
			CapabilitiesUrl (str): optional regex of capabilitiesUrl
			CapabilitiesValidate (str): optional regex of capabilitiesValidate
			CapabilitiesWritableRunning (str): optional regex of capabilitiesWritableRunning
			CapabilitiesXpath (str): optional regex of capabilitiesXpath
			ClientIpv4Address (str): optional regex of clientIpv4Address
			DecryptedCapture (str): optional regex of decryptedCapture
			ErrorInfo (str): optional regex of errorInfo
			ErrorPercentage (str): optional regex of errorPercentage
			ErrorSeverity (str): optional regex of errorSeverity
			ErrorTag (str): optional regex of errorTag
			ErrorType (str): optional regex of errorType
			GetConfigReplyXML (str): optional regex of getConfigReplyXML
			IncludeErrorInfo (str): optional regex of includeErrorInfo
			OutputDirectory (str): optional regex of outputDirectory
			Password (str): optional regex of password
			PortNumber (str): optional regex of portNumber
			PublicKeyDirectory (str): optional regex of publicKeyDirectory
			PublicKeyFileName (str): optional regex of publicKeyFileName
			ResponseXMLDirectory (str): optional regex of responseXMLDirectory
			SendOkResponse (str): optional regex of sendOkResponse
			SshAuthenticationMechanism (str): optional regex of sshAuthenticationMechanism
			UserName (str): optional regex of userName

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

	def GetDecryptedCapture(self, *args, **kwargs):
		"""Executes the getDecryptedCapture operation on the server.

		If Enable Capture is enabled, this will fetch and open the decrypted capture for selected sessions.

		getDecryptedCapture(Arg2:list, Arg3:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group.
				args[1] is Arg3 (number): The TCP Port number of the server connection for which the capture file is to be fetched. Enter 0 for the first server connection

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getDecryptedCapture', payload=payload, response_object=None)

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

	def ResumeRPCReply(self, *args, **kwargs):
		"""Executes the resumeRPCReply operation on the server.

		Resume sending responses to RPC requests.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		resumeRPCReply()

		resumeRPCReply(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		resumeRPCReply(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		resumeRPCReply(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumeRPCReply', payload=payload, response_object=None)

	def SendRPCReplyWithWrongCharacterCount(self, *args, **kwargs):
		"""Executes the sendRPCReplyWithWrongCharacterCount operation on the server.

		The response to the next RPC request will be sent with wrong message Id.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendRPCReplyWithWrongCharacterCount()

		sendRPCReplyWithWrongCharacterCount(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendRPCReplyWithWrongCharacterCount(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendRPCReplyWithWrongCharacterCount(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendRPCReplyWithWrongCharacterCount', payload=payload, response_object=None)

	def SendRPCReplyWithWrongMessageId(self, *args, **kwargs):
		"""Executes the sendRPCReplyWithWrongMessageId operation on the server.

		The response to the next RPC request will be sent with wrong message Id.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendRPCReplyWithWrongMessageId()

		sendRPCReplyWithWrongMessageId(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendRPCReplyWithWrongMessageId(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		sendRPCReplyWithWrongMessageId(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendRPCReplyWithWrongMessageId', payload=payload, response_object=None)

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

	def StopRPCReplyDropOutstandingRequests(self, *args, **kwargs):
		"""Executes the stopRPCReplyDropOutstandingRequests operation on the server.

		Stop sending replies to rpc requests. Drop the outstanding requests so that when Resume RPC Reply is triggered, responses will not be sent for these requests.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopRPCReplyDropOutstandingRequests()

		stopRPCReplyDropOutstandingRequests(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stopRPCReplyDropOutstandingRequests(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		stopRPCReplyDropOutstandingRequests(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopRPCReplyDropOutstandingRequests', payload=payload, response_object=None)

	def StopRPCReplyStoreOutstandingRequests(self, *args, **kwargs):
		"""Executes the stopRPCReplyStoreOutstandingRequests operation on the server.

		Stop sending replies to rpc requests. Store the outstanding requests so that when Resume RPC Reply is triggered, responses will be sent for these requests.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopRPCReplyStoreOutstandingRequests()

		stopRPCReplyStoreOutstandingRequests(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stopRPCReplyStoreOutstandingRequests(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		stopRPCReplyStoreOutstandingRequests(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopRPCReplyStoreOutstandingRequests', payload=payload, response_object=None)
