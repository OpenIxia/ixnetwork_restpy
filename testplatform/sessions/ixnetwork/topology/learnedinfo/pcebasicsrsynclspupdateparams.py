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


class PceBasicSrSyncLspUpdateParams(Base):
	"""The PceBasicSrSyncLspUpdateParams class encapsulates a system managed pceBasicSrSyncLspUpdateParams node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the PceBasicSrSyncLspUpdateParams property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'pceBasicSrSyncLspUpdateParams'

	def __init__(self, parent):
		super(PceBasicSrSyncLspUpdateParams, self).__init__(parent)

	@property
	def PceUpdateSrEroSubObjectList(self):
		"""An instance of the PceUpdateSrEroSubObjectList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrerosubobjectlist.PceUpdateSrEroSubObjectList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrerosubobjectlist import PceUpdateSrEroSubObjectList
		return PceUpdateSrEroSubObjectList(self)

	@property
	def PceUpdateSrMetricSubObjectList(self):
		"""An instance of the PceUpdateSrMetricSubObjectList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrmetricsubobjectlist.PceUpdateSrMetricSubObjectList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrmetricsubobjectlist import PceUpdateSrMetricSubObjectList
		return PceUpdateSrMetricSubObjectList(self)

	@property
	def Bandwidth(self):
		"""Bandwidth (bps)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

	@property
	def BindingType(self):
		"""Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label. Default value is 20bit MPLS Label.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bindingType')

	@property
	def Bos(self):
		"""This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bos')

	@property
	def ConfigureBandwidth(self):
		"""Configure Bandwidth

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureBandwidth')

	@property
	def ConfigureEro(self):
		"""Configure ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureEro')

	@property
	def ConfigureLsp(self):
		"""Configure LSP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureLsp')

	@property
	def ConfigureLspa(self):
		"""Configure LSPA

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureLspa')

	@property
	def ConfigureMetric(self):
		"""Configure Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureMetric')

	@property
	def ExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def HoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

	@property
	def IncludeAll(self):
		"""Include All

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAll')

	@property
	def IncludeAny(self):
		"""Include Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAny')

	@property
	def IncludeSrp(self):
		"""Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSrp')

	@property
	def IncludeSymbolicPathName(self):
		"""Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSymbolicPathName')

	@property
	def IncludeTEPathBindingTLV(self):
		"""Indicates if TE-PATH-BINDING TLV is to be included in PCUpate trigger message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeTEPathBindingTLV')

	@property
	def LocalProtection(self):
		"""Local Protection

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtection')

	@property
	def MplsLabel(self):
		"""This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mplsLabel')

	@property
	def NumberOfEroSubObjects(self):
		"""Value that indicates the number of ERO Sub Objects to be configured.

		Returns:
			number
		"""
		return self._get_attribute('numberOfEroSubObjects')
	@NumberOfEroSubObjects.setter
	def NumberOfEroSubObjects(self, value):
		self._set_attribute('numberOfEroSubObjects', value)

	@property
	def NumberOfMetricSubObjects(self):
		"""Value that indicates the number of Metric Objects to be configured.

		Returns:
			number
		"""
		return self._get_attribute('numberOfMetricSubObjects')
	@NumberOfMetricSubObjects.setter
	def NumberOfMetricSubObjects(self, value):
		self._set_attribute('numberOfMetricSubObjects', value)

	@property
	def OverrideSrpId(self):
		"""Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('overrideSrpId')

	@property
	def PceTriggersChoiceList(self):
		"""Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pceTriggersChoiceList')

	@property
	def SendEmptyTLV(self):
		"""If enabled all fields after Binding Type will be grayed out.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendEmptyTLV')

	@property
	def SetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SrpId(self):
		"""The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srpId')

	@property
	def Tc(self):
		"""This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tc')

	@property
	def Ttl(self):
		"""This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ttl')

	def update(self, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None):
		"""Updates a child instance of pceBasicSrSyncLspUpdateParams on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None):
		"""Finds and retrieves pceBasicSrSyncLspUpdateParams data from the server.

		All named parameters support regex and can be used to selectively retrieve pceBasicSrSyncLspUpdateParams data from the server.
		By default the find method takes no parameters and will retrieve all pceBasicSrSyncLspUpdateParams data from the server.

		Args:
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.

		Returns:
			self: This instance with matching pceBasicSrSyncLspUpdateParams data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of pceBasicSrSyncLspUpdateParams data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the pceBasicSrSyncLspUpdateParams data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Bandwidth=None, BindingType=None, Bos=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeSrp=None, IncludeSymbolicPathName=None, IncludeTEPathBindingTLV=None, LocalProtection=None, MplsLabel=None, OverrideSrpId=None, PceTriggersChoiceList=None, SendEmptyTLV=None, SetupPriority=None, SrpId=None, Tc=None, Ttl=None):
		"""Base class infrastructure that gets a list of pceBasicSrSyncLspUpdateParams device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Bandwidth (str): optional regex of bandwidth
			BindingType (str): optional regex of bindingType
			Bos (str): optional regex of bos
			ConfigureBandwidth (str): optional regex of configureBandwidth
			ConfigureEro (str): optional regex of configureEro
			ConfigureLsp (str): optional regex of configureLsp
			ConfigureLspa (str): optional regex of configureLspa
			ConfigureMetric (str): optional regex of configureMetric
			ExcludeAny (str): optional regex of excludeAny
			HoldingPriority (str): optional regex of holdingPriority
			IncludeAll (str): optional regex of includeAll
			IncludeAny (str): optional regex of includeAny
			IncludeSrp (str): optional regex of includeSrp
			IncludeSymbolicPathName (str): optional regex of includeSymbolicPathName
			IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
			LocalProtection (str): optional regex of localProtection
			MplsLabel (str): optional regex of mplsLabel
			OverrideSrpId (str): optional regex of overrideSrpId
			PceTriggersChoiceList (str): optional regex of pceTriggersChoiceList
			SendEmptyTLV (str): optional regex of sendEmptyTLV
			SetupPriority (str): optional regex of setupPriority
			SrpId (str): optional regex of srpId
			Tc (str): optional regex of tc
			Ttl (str): optional regex of ttl

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

	def SendPcUpdate(self, *args, **kwargs):
		"""Executes the sendPcUpdate operation on the server.

		Counts property changes created by the user.

		sendPcUpdate(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendPcUpdate', payload=payload, response_object=None)
