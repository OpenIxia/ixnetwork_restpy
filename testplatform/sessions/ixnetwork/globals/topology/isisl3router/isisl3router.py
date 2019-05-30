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


class IsisL3Router(Base):
	"""The IsisL3Router class encapsulates a system managed isisL3Router node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the IsisL3Router property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'isisL3Router'

	def __init__(self, parent):
		super(IsisL3Router, self).__init__(parent)

	@property
	def StartRate(self):
		"""An instance of the StartRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.startrate.startrate.StartRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.startrate.startrate import StartRate
		return StartRate(self)._select()

	@property
	def StopRate(self):
		"""An instance of the StopRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.stoprate.stoprate.StopRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.stoprate.stoprate import StopRate
		return StopRate(self)._select()

	@property
	def BIERInfoSubTLVType(self):
		"""BIER Info Sub-TLV Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bIERInfoSubTLVType')

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
	def LinkMsdSubTlvType(self):
		"""This specifies the type of Link MSD sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkMsdSubTlvType')

	@property
	def MaxEndDMsdType(self):
		"""This specifies the type of Max End D MSD

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxEndDMsdType')

	@property
	def MaxEndPopMsdType(self):
		"""This specifies the type of Max End Pop MSD

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxEndPopMsdType')

	@property
	def MaxSegmentsLeftMsdType(self):
		"""This specifies the type of Max Segments Left MSD

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxSegmentsLeftMsdType')

	@property
	def MaxTEncapMsdType(self):
		"""This specifies the type of Max T Encap MSD

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxTEncapMsdType')

	@property
	def MaxTInsertMsdType(self):
		"""This specifies the type of Max T Insert MSD

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxTInsertMsdType')

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
	def NoOfLSPsOrMgroupPDUsPerInterval(self):
		"""LSPs/MGROUP-PDUs per Interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('noOfLSPsOrMgroupPDUsPerInterval')

	@property
	def NodeMsdSubTlvType(self):
		"""This specifies the type of Node MSD sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nodeMsdSubTlvType')

	@property
	def RateControlInterval(self):
		"""Rate Control Interval (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rateControlInterval')

	@property
	def RowNames(self):
		"""Name of rows

		Returns:
			list(str)
		"""
		return self._get_attribute('rowNames')

	@property
	def SendP2PHellosToUnicastMAC(self):
		"""Send P2P Hellos To Unicast MAC

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendP2PHellosToUnicastMAC')

	@property
	def SrDraftExtension(self):
		"""This refers to the TLV structure of SRGB as per the Segment Routing draft version

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srDraftExtension')

	@property
	def SrlbSubTlvType(self):
		"""This specifies the type of Segment Routing Local Block sub tlv, suggested value is 22.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srlbSubTlvType')

	@property
	def SrmsPreferenceSubTlvType(self):
		"""This specifies the type of SRMS Preference sub tlv, suggested value is 23.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srmsPreferenceSubTlvType')

	@property
	def Srv6AdjSIDSubTlvType(self):
		"""This specifies the type of SRv6 Adjacency-SID sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6AdjSIDSubTlvType')

	@property
	def Srv6CapabilitiesSubTlvType(self):
		"""This specifies the type of SRv6 Capabilities sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6CapabilitiesSubTlvType')

	@property
	def Srv6EndSidSubTlvType(self):
		"""This specifies the type of SRv6 End SID sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6EndSidSubTlvType')

	@property
	def Srv6EndXSidSubTlvType(self):
		"""This specifies the type of SRv6 End.X SID sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6EndXSidSubTlvType')

	@property
	def Srv6LANAdjSIDSubTlvType(self):
		"""This specifies the type of SRv6 LAN Adjacency-SID sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6LANAdjSIDSubTlvType')

	@property
	def Srv6LanEndXSidSubTlvType(self):
		"""This specifies the type of SRv6 LAN End.X SID sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6LanEndXSidSubTlvType')

	@property
	def Srv6NodeSIDTlvType(self):
		"""This specifies the type of SRv6 Node SID TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6NodeSIDTlvType')

	@property
	def Srv6SidLocatorTlvType(self):
		"""SRv6 SID Locator Tlv Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLocatorTlvType')

	def update(self, Name=None):
		"""Updates a child instance of isisL3Router on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
		"""Finds and retrieves isisL3Router data from the server.

		All named parameters support regex and can be used to selectively retrieve isisL3Router data from the server.
		By default the find method takes no parameters and will retrieve all isisL3Router data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RowNames (list(str)): Name of rows

		Returns:
			self: This instance with matching isisL3Router data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of isisL3Router data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the isisL3Router data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, BIERInfoSubTLVType=None, LinkMsdSubTlvType=None, MaxEndDMsdType=None, MaxEndPopMsdType=None, MaxSegmentsLeftMsdType=None, MaxTEncapMsdType=None, MaxTInsertMsdType=None, NoOfLSPsOrMgroupPDUsPerInterval=None, NodeMsdSubTlvType=None, RateControlInterval=None, SendP2PHellosToUnicastMAC=None, SrDraftExtension=None, SrlbSubTlvType=None, SrmsPreferenceSubTlvType=None, Srv6AdjSIDSubTlvType=None, Srv6CapabilitiesSubTlvType=None, Srv6EndSidSubTlvType=None, Srv6EndXSidSubTlvType=None, Srv6LANAdjSIDSubTlvType=None, Srv6LanEndXSidSubTlvType=None, Srv6NodeSIDTlvType=None, Srv6SidLocatorTlvType=None):
		"""Base class infrastructure that gets a list of isisL3Router device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			BIERInfoSubTLVType (str): optional regex of bIERInfoSubTLVType
			LinkMsdSubTlvType (str): optional regex of linkMsdSubTlvType
			MaxEndDMsdType (str): optional regex of maxEndDMsdType
			MaxEndPopMsdType (str): optional regex of maxEndPopMsdType
			MaxSegmentsLeftMsdType (str): optional regex of maxSegmentsLeftMsdType
			MaxTEncapMsdType (str): optional regex of maxTEncapMsdType
			MaxTInsertMsdType (str): optional regex of maxTInsertMsdType
			NoOfLSPsOrMgroupPDUsPerInterval (str): optional regex of noOfLSPsOrMgroupPDUsPerInterval
			NodeMsdSubTlvType (str): optional regex of nodeMsdSubTlvType
			RateControlInterval (str): optional regex of rateControlInterval
			SendP2PHellosToUnicastMAC (str): optional regex of sendP2PHellosToUnicastMAC
			SrDraftExtension (str): optional regex of srDraftExtension
			SrlbSubTlvType (str): optional regex of srlbSubTlvType
			SrmsPreferenceSubTlvType (str): optional regex of srmsPreferenceSubTlvType
			Srv6AdjSIDSubTlvType (str): optional regex of srv6AdjSIDSubTlvType
			Srv6CapabilitiesSubTlvType (str): optional regex of srv6CapabilitiesSubTlvType
			Srv6EndSidSubTlvType (str): optional regex of srv6EndSidSubTlvType
			Srv6EndXSidSubTlvType (str): optional regex of srv6EndXSidSubTlvType
			Srv6LANAdjSIDSubTlvType (str): optional regex of srv6LANAdjSIDSubTlvType
			Srv6LanEndXSidSubTlvType (str): optional regex of srv6LanEndXSidSubTlvType
			Srv6NodeSIDTlvType (str): optional regex of srv6NodeSIDTlvType
			Srv6SidLocatorTlvType (str): optional regex of srv6SidLocatorTlvType

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
