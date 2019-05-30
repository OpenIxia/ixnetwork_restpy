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


class PccGroup(Base):
	"""The PccGroup class encapsulates a user managed pccGroup node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the PccGroup property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'pccGroup'

	def __init__(self, parent):
		super(PccGroup, self).__init__(parent)

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
	def LearnedInfoUpdate(self):
		"""An instance of the LearnedInfoUpdate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate.LearnedInfoUpdate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate import LearnedInfoUpdate
		return LearnedInfoUpdate(self)

	@property
	def PcReplyLspParameters(self):
		"""An instance of the PcReplyLspParameters class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcreplylspparameters.PcReplyLspParameters)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcreplylspparameters import PcReplyLspParameters
		return PcReplyLspParameters(self)._select()

	@property
	def PcRequestMatchCriteria(self):
		"""An instance of the PcRequestMatchCriteria class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcrequestmatchcriteria.PcRequestMatchCriteria)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcrequestmatchcriteria import PcRequestMatchCriteria
		return PcRequestMatchCriteria(self)._select()

	@property
	def PceInitiateLSPParameters(self):
		"""An instance of the PceInitiateLSPParameters class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatelspparameters.PceInitiateLSPParameters)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatelspparameters import PceInitiateLSPParameters
		return PceInitiateLSPParameters(self)._select()

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Authentication(self):
		"""The type of cryptographic authentication to be used on this link interface

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authentication')

	@property
	def BurstInterval(self):
		"""Interval in milisecond in which desired rate of messages needs to be maintained.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('burstInterval')

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
	def DeadInterval(self):
		"""This is the time interval, after the expiration of which, a PCEP peer declares the session down if no PCEP message has been received.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('deadInterval')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def KeepaliveInterval(self):
		"""Frequency/Time Interval of sending PCEP messages to keep the session active.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('keepaliveInterval')

	@property
	def MD5Key(self):
		"""A value to be used as the secret MD5 Key.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mD5Key')

	@property
	def MaxInitiatedLspPerInterval(self):
		"""Maximum number of messages can be sent per interval.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxInitiatedLspPerInterval')

	@property
	def MaxLspsPerPcInitiate(self):
		"""Controls the maximum number of LSPs that can be present in a PCInitiate message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxLspsPerPcInitiate')

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
	def PcReplyLspsPerPcc(self):
		"""Controls the maximum number of PCE LSPs that can be send as PATH Response.

		Returns:
			number
		"""
		return self._get_attribute('pcReplyLspsPerPcc')
	@PcReplyLspsPerPcc.setter
	def PcReplyLspsPerPcc(self, value):
		self._set_attribute('pcReplyLspsPerPcc', value)

	@property
	def PccIpv4Address(self):
		"""IPv4 address of the PCC. This column is greyed out in case of PCEv6.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pccIpv4Address')

	@property
	def PceInitiatedLspsPerPcc(self):
		"""Controls the maximum number of PCE LSPs that can be Initiated per PCC.

		Returns:
			number
		"""
		return self._get_attribute('pceInitiatedLspsPerPcc')
	@PceInitiatedLspsPerPcc.setter
	def PceInitiatedLspsPerPcc(self, value):
		self._set_attribute('pceInitiatedLspsPerPcc', value)

	@property
	def PcePpagTLVType(self):
		"""PPAG TLV Type specifies PCE's capability of interpreting this type of PPAG TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pcePpagTLVType')

	@property
	def RateControl(self):
		"""The rate control is an optional feature associated with PCE initiated LSP.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rateControl')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SrPceCapability(self):
		"""The SR PCE Capability TLV is an optional TLV associated with the OPEN Object to exchange SR capability of PCEP speakers.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srPceCapability')

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

	def update(self, ConnectedVia=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PceInitiatedLspsPerPcc=None, StackedLayers=None):
		"""Updates a child instance of pccGroup on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
			PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PceInitiatedLspsPerPcc=None, StackedLayers=None):
		"""Adds a new pccGroup node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
			PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved pccGroup data using find and the newly added pccGroup data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the pccGroup data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PceInitiatedLspsPerPcc=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves pccGroup data from the server.

		All named parameters support regex and can be used to selectively retrieve pccGroup data from the server.
		By default the find method takes no parameters and will retrieve all pccGroup data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
			PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching pccGroup data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of pccGroup data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the pccGroup data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, Authentication=None, BurstInterval=None, DeadInterval=None, KeepaliveInterval=None, MD5Key=None, MaxInitiatedLspPerInterval=None, MaxLspsPerPcInitiate=None, PccIpv4Address=None, PcePpagTLVType=None, RateControl=None, SrPceCapability=None):
		"""Base class infrastructure that gets a list of pccGroup device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			Authentication (str): optional regex of authentication
			BurstInterval (str): optional regex of burstInterval
			DeadInterval (str): optional regex of deadInterval
			KeepaliveInterval (str): optional regex of keepaliveInterval
			MD5Key (str): optional regex of mD5Key
			MaxInitiatedLspPerInterval (str): optional regex of maxInitiatedLspPerInterval
			MaxLspsPerPcInitiate (str): optional regex of maxLspsPerPcInitiate
			PccIpv4Address (str): optional regex of pccIpv4Address
			PcePpagTLVType (str): optional regex of pcePpagTLVType
			RateControl (str): optional regex of rateControl
			SrPceCapability (str): optional regex of srPceCapability

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def ClearPceAllLearnedInfo(self, *args, **kwargs):
		"""Executes the clearPceAllLearnedInfo operation on the server.

		Clears ALL Learned LSP Information By PCC Device.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		clearPceAllLearnedInfo()

		clearPceAllLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		clearPceAllLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		clearPceAllLearnedInfo(Arg2:list)list
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
		return self._execute('clearPceAllLearnedInfo', payload=payload, response_object=None)

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

	def GetPceBasicAllRsvpLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicAllRsvpLspLearnedInfo operation on the server.

		Gets Basic Information about All RSVP LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicAllRsvpLspLearnedInfo()

		getPceBasicAllRsvpLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicAllRsvpLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicAllRsvpLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicAllRsvpLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicAllSrLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicAllSrLspLearnedInfo operation on the server.

		Gets Basic Information about All SR LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicAllSrLspLearnedInfo()

		getPceBasicAllSrLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicAllSrLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicAllSrLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicAllSrLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicRsvpPccRequestedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicRsvpPccRequestedLspLearnedInfo operation on the server.

		Gets Basic Information about RSVP-TE PCC Requested LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicRsvpPccRequestedLspLearnedInfo()

		getPceBasicRsvpPccRequestedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicRsvpPccRequestedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicRsvpPccRequestedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicRsvpPccRequestedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicRsvpPccSyncLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicRsvpPccSyncLspLearnedInfo operation on the server.

		Gets Basic Information about RSVP-TE PCC Sync/Report LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicRsvpPccSyncLspLearnedInfo()

		getPceBasicRsvpPccSyncLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicRsvpPccSyncLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicRsvpPccSyncLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicRsvpPccSyncLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicRsvpPceInitiatedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicRsvpPceInitiatedLspLearnedInfo operation on the server.

		Gets Basic Information about RSVP-TE PCE Initiated LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicRsvpPceInitiatedLspLearnedInfo()

		getPceBasicRsvpPceInitiatedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicRsvpPceInitiatedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicRsvpPceInitiatedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicRsvpPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicSrPccRequestedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicSrPccRequestedLspLearnedInfo operation on the server.

		Gets Basic Information about SR-TE PCC Requested LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicSrPccRequestedLspLearnedInfo()

		getPceBasicSrPccRequestedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicSrPccRequestedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicSrPccRequestedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicSrPccRequestedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicSrPccSyncLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicSrPccSyncLspLearnedInfo operation on the server.

		Gets Basic Information about SR-TE PCC Sync/Report LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicSrPccSyncLspLearnedInfo()

		getPceBasicSrPccSyncLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicSrPccSyncLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicSrPccSyncLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicSrPccSyncLspLearnedInfo', payload=payload, response_object=None)

	def GetPceBasicSrPceInitiatedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceBasicSrPceInitiatedLspLearnedInfo operation on the server.

		Gets Basic Information about SR-TE PCE Initiated LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceBasicSrPceInitiatedLspLearnedInfo()

		getPceBasicSrPceInitiatedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceBasicSrPceInitiatedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceBasicSrPceInitiatedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceBasicSrPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedAllRsvpLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedAllRsvpLspLearnedInfo operation on the server.

		Gets Detailed Information about All RSVP LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedAllRsvpLspLearnedInfo()

		getPceDetailedAllRsvpLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedAllRsvpLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedAllRsvpLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedAllRsvpLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedAllSrLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedAllSrLspLearnedInfo operation on the server.

		Gets Detailed Information about All SR LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedAllSrLspLearnedInfo()

		getPceDetailedAllSrLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedAllSrLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedAllSrLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedAllSrLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedRsvpPccRequestedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedRsvpPccRequestedLspLearnedInfo operation on the server.

		Gets Detailed Information about RSVP-TE PCC Requested LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedRsvpPccRequestedLspLearnedInfo()

		getPceDetailedRsvpPccRequestedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedRsvpPccRequestedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedRsvpPccRequestedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedRsvpPccRequestedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedRsvpPccSyncLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedRsvpPccSyncLspLearnedInfo operation on the server.

		Gets Detailed Information about RSVP-TE PCC Sync/Report LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedRsvpPccSyncLspLearnedInfo()

		getPceDetailedRsvpPccSyncLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedRsvpPccSyncLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedRsvpPccSyncLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedRsvpPccSyncLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedRsvpPceInitiatedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedRsvpPceInitiatedLspLearnedInfo operation on the server.

		Gets Detailed Information about RSVP-TE PCE Initiated LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedRsvpPceInitiatedLspLearnedInfo()

		getPceDetailedRsvpPceInitiatedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedRsvpPceInitiatedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedRsvpPceInitiatedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedRsvpPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedSrPccRequestedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedSrPccRequestedLspLearnedInfo operation on the server.

		Gets Detailed Information about SR-TE PCC Requested LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedSrPccRequestedLspLearnedInfo()

		getPceDetailedSrPccRequestedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedSrPccRequestedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedSrPccRequestedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedSrPccRequestedLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedSrPccSyncLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedSrPccSyncLspLearnedInfo operation on the server.

		Gets Detailed Information about SR-TE PCC Sync/Report LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedSrPccSyncLspLearnedInfo()

		getPceDetailedSrPccSyncLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedSrPccSyncLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedSrPccSyncLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedSrPccSyncLspLearnedInfo', payload=payload, response_object=None)

	def GetPceDetailedSrPceInitiatedLspLearnedInfo(self, *args, **kwargs):
		"""Executes the getPceDetailedSrPceInitiatedLspLearnedInfo operation on the server.

		Gets Detailed Information about SR-TE PCE Initiated LSPs learnt by this PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getPceDetailedSrPceInitiatedLspLearnedInfo()

		getPceDetailedSrPceInitiatedLspLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getPceDetailedSrPceInitiatedLspLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getPceDetailedSrPceInitiatedLspLearnedInfo(Arg2:list)list
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
		return self._execute('getPceDetailedSrPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

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
