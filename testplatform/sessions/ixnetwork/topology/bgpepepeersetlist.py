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


class BgpEpePeerSetList(Base):
	"""The BgpEpePeerSetList class encapsulates a system managed bgpEpePeerSetList node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the BgpEpePeerSetList property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'bgpEpePeerSetList'

	def __init__(self, parent):
		super(BgpEpePeerSetList, self).__init__(parent)

	@property
	def BBit(self):
		"""B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.

		Returns:
			bool
		"""
		return self._get_attribute('bBit')
	@BBit.setter
	def BBit(self, value):
		self._set_attribute('bBit', value)

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
	def LBit(self):
		"""L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.

		Returns:
			bool
		"""
		return self._get_attribute('lBit')
	@LBit.setter
	def LBit(self, value):
		self._set_attribute('lBit', value)

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
	def PBit(self):
		"""P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap

		Returns:
			bool
		"""
		return self._get_attribute('pBit')
	@PBit.setter
	def PBit(self, value):
		self._set_attribute('pBit', value)

	@property
	def Reserved(self):
		"""Reserved

		Returns:
			number
		"""
		return self._get_attribute('reserved')
	@Reserved.setter
	def Reserved(self, value):
		self._set_attribute('reserved', value)

	@property
	def RsvdBits(self):
		"""Reserved for future use and MUST be zero when originated and ignored when received

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rsvdBits')

	@property
	def SidIndex(self):
		"""Local Label for Peer-Set

		Returns:
			str(index|sid)
		"""
		return self._get_attribute('sidIndex')
	@SidIndex.setter
	def SidIndex(self, value):
		self._set_attribute('sidIndex', value)

	@property
	def SidIndexValue(self):
		"""If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295

		Returns:
			number
		"""
		return self._get_attribute('sidIndexValue')
	@SidIndexValue.setter
	def SidIndexValue(self, value):
		self._set_attribute('sidIndexValue', value)

	@property
	def VBit(self):
		"""V-Flag: Value flag. If set, then the SID carries a label value.

		Returns:
			bool
		"""
		return self._get_attribute('vBit')
	@VBit.setter
	def VBit(self, value):
		self._set_attribute('vBit', value)

	@property
	def Weight(self):
		"""Weight of SID for the purpose of load balancing

		Returns:
			number
		"""
		return self._get_attribute('weight')
	@Weight.setter
	def Weight(self, value):
		self._set_attribute('weight', value)

	def update(self, BBit=None, LBit=None, Name=None, PBit=None, Reserved=None, SidIndex=None, SidIndexValue=None, VBit=None, Weight=None):
		"""Updates a child instance of bgpEpePeerSetList on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			BBit (bool): B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
			LBit (bool): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PBit (bool): P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
			Reserved (number): Reserved
			SidIndex (str(index|sid)): Local Label for Peer-Set
			SidIndexValue (number): If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
			VBit (bool): V-Flag: Value flag. If set, then the SID carries a label value.
			Weight (number): Weight of SID for the purpose of load balancing

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, BBit=None, Count=None, DescriptiveName=None, LBit=None, Name=None, PBit=None, Reserved=None, SidIndex=None, SidIndexValue=None, VBit=None, Weight=None):
		"""Finds and retrieves bgpEpePeerSetList data from the server.

		All named parameters support regex and can be used to selectively retrieve bgpEpePeerSetList data from the server.
		By default the find method takes no parameters and will retrieve all bgpEpePeerSetList data from the server.

		Args:
			BBit (bool): B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LBit (bool): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PBit (bool): P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
			Reserved (number): Reserved
			SidIndex (str(index|sid)): Local Label for Peer-Set
			SidIndexValue (number): If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
			VBit (bool): V-Flag: Value flag. If set, then the SID carries a label value.
			Weight (number): Weight of SID for the purpose of load balancing

		Returns:
			self: This instance with matching bgpEpePeerSetList data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bgpEpePeerSetList data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bgpEpePeerSetList data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, RsvdBits=None):
		"""Base class infrastructure that gets a list of bgpEpePeerSetList device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			RsvdBits (str): optional regex of rsvdBits

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
