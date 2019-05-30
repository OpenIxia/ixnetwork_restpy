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


class BgpEpePeerLinkList(Base):
	"""The BgpEpePeerLinkList class encapsulates a required bgpEpePeerLinkList node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the BgpEpePeerLinkList property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'bgpEpePeerLinkList'

	def __init__(self, parent):
		super(BgpEpePeerLinkList, self).__init__(parent)

	@property
	def TlvProfile(self):
		"""An instance of the TlvProfile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile.TlvProfile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile import TlvProfile
		return TlvProfile(self)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def BBit(self):
		"""B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bBit')

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
	def EnableLinkAddress(self):
		"""Enable Link Addresses

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLinkAddress')

	@property
	def EnableLinkIdentifier(self):
		"""Enable Link Identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLinkIdentifier')

	@property
	def EnablePeerAdjSid(self):
		"""Enable Peer-Adj-SID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enablePeerAdjSid')

	@property
	def LBit(self):
		"""L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lBit')

	@property
	def LinkAddressType(self):
		"""Link Address Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkAddressType')

	@property
	def LinkLocalIdentifier(self):
		"""Link Local Identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkLocalIdentifier')

	@property
	def LinkNumber(self):
		"""EPE Link Number For Reference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkNumber')

	@property
	def LinkRemoteIdentifier(self):
		"""Link Remote Identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkRemoteIdentifier')

	@property
	def LocalIpv4LinkAddress(self):
		"""Local IPv4 Link Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localIpv4LinkAddress')

	@property
	def LocalIpv6LinkAddress(self):
		"""Local IPv6 Link Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localIpv6LinkAddress')

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
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pBit')

	@property
	def PeerName(self):
		"""Peer Name For Reference

		Returns:
			list(str)
		"""
		return self._get_attribute('peerName')

	@property
	def RemoteIpv4LinkAddress(self):
		"""Remote IPv4 Link Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteIpv4LinkAddress')

	@property
	def RemoteIpv6LinkAddress(self):
		"""Remote IPv6 Link Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteIpv6LinkAddress')

	@property
	def Reserved(self):
		"""Reserved

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reserved')

	@property
	def RsvdBits(self):
		"""Reserved for future use and MUST be zero when originated and ignored when received

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rsvdBits')

	@property
	def SidIndex(self):
		"""Local Label for Peer-Adj

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sidIndex')

	@property
	def SidIndexValue(self):
		"""If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sidIndexValue')

	@property
	def VBit(self):
		"""V-Flag: Value flag. If set, then the SID carries a label value.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vBit')

	@property
	def Weight(self):
		"""Weight of the SID for the purpose of load balancing

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('weight')

	def update(self, Name=None):
		"""Updates a child instance of bgpEpePeerLinkList on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def get_device_ids(self, PortNames=None, Active=None, BBit=None, EnableLinkAddress=None, EnableLinkIdentifier=None, EnablePeerAdjSid=None, LBit=None, LinkAddressType=None, LinkLocalIdentifier=None, LinkNumber=None, LinkRemoteIdentifier=None, LocalIpv4LinkAddress=None, LocalIpv6LinkAddress=None, PBit=None, RemoteIpv4LinkAddress=None, RemoteIpv6LinkAddress=None, Reserved=None, RsvdBits=None, SidIndex=None, SidIndexValue=None, VBit=None, Weight=None):
		"""Base class infrastructure that gets a list of bgpEpePeerLinkList device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			BBit (str): optional regex of bBit
			EnableLinkAddress (str): optional regex of enableLinkAddress
			EnableLinkIdentifier (str): optional regex of enableLinkIdentifier
			EnablePeerAdjSid (str): optional regex of enablePeerAdjSid
			LBit (str): optional regex of lBit
			LinkAddressType (str): optional regex of linkAddressType
			LinkLocalIdentifier (str): optional regex of linkLocalIdentifier
			LinkNumber (str): optional regex of linkNumber
			LinkRemoteIdentifier (str): optional regex of linkRemoteIdentifier
			LocalIpv4LinkAddress (str): optional regex of localIpv4LinkAddress
			LocalIpv6LinkAddress (str): optional regex of localIpv6LinkAddress
			PBit (str): optional regex of pBit
			RemoteIpv4LinkAddress (str): optional regex of remoteIpv4LinkAddress
			RemoteIpv6LinkAddress (str): optional regex of remoteIpv6LinkAddress
			Reserved (str): optional regex of reserved
			RsvdBits (str): optional regex of rsvdBits
			SidIndex (str): optional regex of sidIndex
			SidIndexValue (str): optional regex of sidIndexValue
			VBit (str): optional regex of vBit
			Weight (str): optional regex of weight

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
