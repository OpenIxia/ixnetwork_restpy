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


class RsvpteIf(Base):
	"""The RsvpteIf class encapsulates a user managed rsvpteIf node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the RsvpteIf property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'rsvpteIf'

	def __init__(self, parent):
		super(RsvpteIf, self).__init__(parent)

	@property
	def LearnedInfo(self):
		"""An instance of the LearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
		return LearnedInfo(self)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def ActualRestartTime(self):
		"""Actual Restart Time (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actualRestartTime')

	@property
	def AdvertisedRestartTime(self):
		"""Advertised Restart Time (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertisedRestartTime')

	@property
	def AuthenticationAlgorithm(self):
		"""Authentication Algorithm

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authenticationAlgorithm')

	@property
	def AuthenticationKeyForReceivedPackets(self):
		"""Authentication Key for Received Packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authenticationKeyForReceivedPackets')

	@property
	def AuthenticationKeyForSentPackets(self):
		"""Authentication Key for Sent Packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authenticationKeyForSentPackets')

	@property
	def AuthenticationKeyIdentifier(self):
		"""Authentication Key Identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authenticationKeyIdentifier')

	@property
	def AutoGenerateAuthenticationKeyIdentifier(self):
		"""Auto Generate Authentication Key Identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('autoGenerateAuthenticationKeyIdentifier')

	@property
	def BundleMessageThresholdTime(self):
		"""Bundle Message Threshold Time (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bundleMessageThresholdTime')

	@property
	def CheckIntegrityForReceivedPackets(self):
		"""Check Integrity for Received Packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('checkIntegrityForReceivedPackets')

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
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DutIp(self):
		"""DUT IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dutIp')

	@property
	def EnableBfdRegistration(self):
		"""Enable BFD Registration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBfdRegistration')

	@property
	def EnableBundleMessageSending(self):
		"""Enable Bundle Message Sending

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBundleMessageSending')

	@property
	def EnableBundleMessageThresholdTimer(self):
		"""Enable Bundle Message Threshold Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBundleMessageThresholdTimer')

	@property
	def EnableGracefulRestartHelperMode(self):
		"""Enable Helper-Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGracefulRestartHelperMode')

	@property
	def EnableGracefulRestartRestartingMode(self):
		"""Enable Restarting-Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGracefulRestartRestartingMode')

	@property
	def EnableHelloExtension(self):
		"""Enable Hello Extension

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableHelloExtension')

	@property
	def EnableRefreshReduction(self):
		"""Enable Refresh Reduction

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableRefreshReduction')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def GenerateSequenceNumberBasedOnRealTime(self):
		"""Generate Sequence Number Based on Real Time

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('generateSequenceNumberBasedOnRealTime')

	@property
	def HandshakeRequired(self):
		"""Handshake Required

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('handshakeRequired')

	@property
	def HelloInterval(self):
		"""Hello Interval (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('helloInterval')

	@property
	def HelloTimeoutMultiplier(self):
		"""Hello Timeout Multiplier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('helloTimeoutMultiplier')

	@property
	def InitialSequenceNumber(self):
		"""Initial Sequence Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('initialSequenceNumber')

	@property
	def LabelReqRefCount(self):
		"""Number of Label Req in RSVP-TE DG

		Returns:
			number
		"""
		return self._get_attribute('labelReqRefCount')
	@LabelReqRefCount.setter
	def LabelReqRefCount(self, value):
		self._set_attribute('labelReqRefCount', value)

	@property
	def LabelSpaceEnd(self):
		"""Label Space End

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelSpaceEnd')

	@property
	def LabelSpaceStart(self):
		"""Label Space Start

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelSpaceStart')

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
	def NumberOfRestarts(self):
		"""Number of Restarts

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numberOfRestarts')

	@property
	def OurIp(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('ourIp')

	@property
	def RecoveryTime(self):
		"""Recovery Time (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('recoveryTime')

	@property
	def RestartStartTime(self):
		"""Restart Start Time (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('restartStartTime')

	@property
	def RestartUpTime(self):
		"""Restart Up Time (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('restartUpTime')

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
	def SummaryRefreshInterval(self):
		"""Summary Refresh Interval (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('summaryRefreshInterval')

	@property
	def UseSameAuthenticationKeyForPeer(self):
		"""Use Same Authentication Key for Peer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useSameAuthenticationKeyForPeer')

	@property
	def UsingGatewayIp(self):
		"""Using Gateway IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('usingGatewayIp')

	def update(self, ConnectedVia=None, LabelReqRefCount=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Updates a child instance of rsvpteIf on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, LabelReqRefCount=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Adds a new rsvpteIf node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved rsvpteIf data using find and the newly added rsvpteIf data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the rsvpteIf data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LabelReqRefCount=None, Multiplier=None, Name=None, OurIp=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves rsvpteIf data from the server.

		All named parameters support regex and can be used to selectively retrieve rsvpteIf data from the server.
		By default the find method takes no parameters and will retrieve all rsvpteIf data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OurIp (list(str)): Local IP
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching rsvpteIf data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of rsvpteIf data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the rsvpteIf data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, ActualRestartTime=None, AdvertisedRestartTime=None, AuthenticationAlgorithm=None, AuthenticationKeyForReceivedPackets=None, AuthenticationKeyForSentPackets=None, AuthenticationKeyIdentifier=None, AutoGenerateAuthenticationKeyIdentifier=None, BundleMessageThresholdTime=None, CheckIntegrityForReceivedPackets=None, DutIp=None, EnableBfdRegistration=None, EnableBundleMessageSending=None, EnableBundleMessageThresholdTimer=None, EnableGracefulRestartHelperMode=None, EnableGracefulRestartRestartingMode=None, EnableHelloExtension=None, EnableRefreshReduction=None, GenerateSequenceNumberBasedOnRealTime=None, HandshakeRequired=None, HelloInterval=None, HelloTimeoutMultiplier=None, InitialSequenceNumber=None, LabelSpaceEnd=None, LabelSpaceStart=None, NumberOfRestarts=None, RecoveryTime=None, RestartStartTime=None, RestartUpTime=None, SummaryRefreshInterval=None, UseSameAuthenticationKeyForPeer=None, UsingGatewayIp=None):
		"""Base class infrastructure that gets a list of rsvpteIf device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			ActualRestartTime (str): optional regex of actualRestartTime
			AdvertisedRestartTime (str): optional regex of advertisedRestartTime
			AuthenticationAlgorithm (str): optional regex of authenticationAlgorithm
			AuthenticationKeyForReceivedPackets (str): optional regex of authenticationKeyForReceivedPackets
			AuthenticationKeyForSentPackets (str): optional regex of authenticationKeyForSentPackets
			AuthenticationKeyIdentifier (str): optional regex of authenticationKeyIdentifier
			AutoGenerateAuthenticationKeyIdentifier (str): optional regex of autoGenerateAuthenticationKeyIdentifier
			BundleMessageThresholdTime (str): optional regex of bundleMessageThresholdTime
			CheckIntegrityForReceivedPackets (str): optional regex of checkIntegrityForReceivedPackets
			DutIp (str): optional regex of dutIp
			EnableBfdRegistration (str): optional regex of enableBfdRegistration
			EnableBundleMessageSending (str): optional regex of enableBundleMessageSending
			EnableBundleMessageThresholdTimer (str): optional regex of enableBundleMessageThresholdTimer
			EnableGracefulRestartHelperMode (str): optional regex of enableGracefulRestartHelperMode
			EnableGracefulRestartRestartingMode (str): optional regex of enableGracefulRestartRestartingMode
			EnableHelloExtension (str): optional regex of enableHelloExtension
			EnableRefreshReduction (str): optional regex of enableRefreshReduction
			GenerateSequenceNumberBasedOnRealTime (str): optional regex of generateSequenceNumberBasedOnRealTime
			HandshakeRequired (str): optional regex of handshakeRequired
			HelloInterval (str): optional regex of helloInterval
			HelloTimeoutMultiplier (str): optional regex of helloTimeoutMultiplier
			InitialSequenceNumber (str): optional regex of initialSequenceNumber
			LabelSpaceEnd (str): optional regex of labelSpaceEnd
			LabelSpaceStart (str): optional regex of labelSpaceStart
			NumberOfRestarts (str): optional regex of numberOfRestarts
			RecoveryTime (str): optional regex of recoveryTime
			RestartStartTime (str): optional regex of restartStartTime
			RestartUpTime (str): optional regex of restartUpTime
			SummaryRefreshInterval (str): optional regex of summaryRefreshInterval
			UseSameAuthenticationKeyForPeer (str): optional regex of useSameAuthenticationKeyForPeer
			UsingGatewayIp (str): optional regex of usingGatewayIp

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

	def GetLearnedInfo(self, *args, **kwargs):
		"""Executes the getLearnedInfo operation on the server.

		Get Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getLearnedInfo()

		getLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getLearnedInfo(Arg2:list)list
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
		return self._execute('getLearnedInfo', payload=payload, response_object=None)

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

	def RestartNeighbor(self, *args, **kwargs):
		"""Executes the restartNeighbor operation on the server.

		Restart Neighbor

		restartNeighbor(Arg2:list)list
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
		return self._execute('restartNeighbor', payload=payload, response_object=None)

	def RsvpRestartNeighbor(self, *args, **kwargs):
		"""Executes the rsvpRestartNeighbor operation on the server.

		Gracefully restart selected Neighbors

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		rsvpRestartNeighbor()

		rsvpRestartNeighbor(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		rsvpRestartNeighbor(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rsvpRestartNeighbor', payload=payload, response_object=None)

	def RsvpResumeHello(self, *args, **kwargs):
		"""Executes the rsvpResumeHello operation on the server.

		Resume sending Hello messages from selected Neighbors

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		rsvpResumeHello()

		rsvpResumeHello(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		rsvpResumeHello(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rsvpResumeHello', payload=payload, response_object=None)

	def RsvpStartSRefresh(self, *args, **kwargs):
		"""Executes the rsvpStartSRefresh operation on the server.

		Start sending SRefresh messages from selected Neighbors

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		rsvpStartSRefresh()

		rsvpStartSRefresh(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		rsvpStartSRefresh(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rsvpStartSRefresh', payload=payload, response_object=None)

	def RsvpStopHello(self, *args, **kwargs):
		"""Executes the rsvpStopHello operation on the server.

		Stop sending Hello messages from selected Neighbors

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		rsvpStopHello()

		rsvpStopHello(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		rsvpStopHello(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rsvpStopHello', payload=payload, response_object=None)

	def RsvpStopSRefresh(self, *args, **kwargs):
		"""Executes the rsvpStopSRefresh operation on the server.

		Stop sending SRefresh messages from selected Neighbors

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		rsvpStopSRefresh()

		rsvpStopSRefresh(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		rsvpStopSRefresh(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rsvpStopSRefresh', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Activate/Enable selected Neighbor Pairs

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

	def StartHello(self, *args, **kwargs):
		"""Executes the startHello operation on the server.

		Start Hello

		startHello(Arg2:list)list
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
		return self._execute('startHello', payload=payload, response_object=None)

	def StartSRefresh(self, *args, **kwargs):
		"""Executes the startSRefresh operation on the server.

		Start SRefresh

		startSRefresh(Arg2:list)list
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
		return self._execute('startSRefresh', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Deactivate/Disable selected Neighbor Pairs

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

	def StopHello(self, *args, **kwargs):
		"""Executes the stopHello operation on the server.

		Stop Hello

		stopHello(Arg2:list)list
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
		return self._execute('stopHello', payload=payload, response_object=None)

	def StopSRefresh(self, *args, **kwargs):
		"""Executes the stopSRefresh operation on the server.

		Stop SRefresh

		stopSRefresh(Arg2:list)list
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
		return self._execute('stopSRefresh', payload=payload, response_object=None)
