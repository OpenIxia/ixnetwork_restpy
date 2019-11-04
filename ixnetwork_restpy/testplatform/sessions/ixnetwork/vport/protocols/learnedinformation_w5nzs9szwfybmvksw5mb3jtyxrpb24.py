# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class LearnedInformation(Base):
	"""Holds lists of all of the learned route information. Each of the enabled types of routes is logically considered as a separate list.
	The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'learnedInformation'

	def __init__(self, parent):
		super(LearnedInformation, self).__init__(parent)

	@property
	def AdVpls(self):
		"""An instance of the AdVpls class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_fybmvksw5mb3jtyxrpb24vywrwcgxz.AdVpls)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_fybmvksw5mb3jtyxrpb24vywrwcgxz import AdVpls
		return AdVpls(self)

	@property
	def EvpnEthernetAd(self):
		"""An instance of the EvpnEthernetAd class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_3jtyxrpb24vzxzwbkv0agvybmv0qwq.EvpnEthernetAd)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_3jtyxrpb24vzxzwbkv0agvybmv0qwq import EvpnEthernetAd
		return EvpnEthernetAd(self)

	@property
	def EvpnEthernetSegment(self):
		"""An instance of the EvpnEthernetSegment class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_b24vzxzwbkv0agvybmv0u2vnbwvuda.EvpnEthernetSegment)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_b24vzxzwbkv0agvybmv0u2vnbwvuda import EvpnEthernetSegment
		return EvpnEthernetSegment(self)

	@property
	def EvpnMac(self):
		"""An instance of the EvpnMac class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_bmvksw5mb3jtyxrpb24vzxzwbk1hyw.EvpnMac)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_bmvksw5mb3jtyxrpb24vzxzwbk1hyw import EvpnMac
		return EvpnMac(self)

	@property
	def EvpnMulticast(self):
		"""An instance of the EvpnMulticast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_b3jtyxrpb24vzxzwbk11bhrpy2fzda.EvpnMulticast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_b3jtyxrpb24vzxzwbk11bhrpy2fzda import EvpnMulticast
		return EvpnMulticast(self)

	@property
	def IpV4MulticastMplsVpn(self):
		"""An instance of the IpV4MulticastMplsVpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_24vaxbwne11bhrpy2fzde1wbhnwcg4.IpV4MulticastMplsVpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_24vaxbwne11bhrpy2fzde1wbhnwcg4 import IpV4MulticastMplsVpn
		return IpV4MulticastMplsVpn(self)

	@property
	def IpV6MulticastMplsVpn(self):
		"""An instance of the IpV6MulticastMplsVpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_24vaxbwnk11bhrpy2fzde1wbhnwcg4.IpV6MulticastMplsVpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_24vaxbwnk11bhrpy2fzde1wbhnwcg4 import IpV6MulticastMplsVpn
		return IpV6MulticastMplsVpn(self)

	@property
	def Ipv4Multicast(self):
		"""An instance of the Ipv4Multicast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_b3jtyxrpb24vaxb2ne11bhrpy2fzda.Ipv4Multicast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_b3jtyxrpb24vaxb2ne11bhrpy2fzda import Ipv4Multicast
		return Ipv4Multicast(self)

	@property
	def Ipv4MulticastVpn(self):
		"""An instance of the Ipv4MulticastVpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_yxrpb24vaxb2ne11bhrpy2fzdfzwbg.Ipv4MulticastVpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_yxrpb24vaxb2ne11bhrpy2fzdfzwbg import Ipv4MulticastVpn
		return Ipv4MulticastVpn(self)

	@property
	def Ipv4Unicast(self):
		"""An instance of the Ipv4Unicast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_w5mb3jtyxrpb24vaxb2nfvuawnhc3q.Ipv4Unicast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_w5mb3jtyxrpb24vaxb2nfvuawnhc3q import Ipv4Unicast
		return Ipv4Unicast(self)

	@property
	def Ipv4mpls(self):
		"""An instance of the Ipv4mpls class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_mvksw5mb3jtyxrpb24vaxb2ng1wbhm.Ipv4mpls)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_mvksw5mb3jtyxrpb24vaxb2ng1wbhm import Ipv4mpls
		return Ipv4mpls(self)

	@property
	def Ipv4vpn(self):
		"""An instance of the Ipv4vpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_bmvksw5mb3jtyxrpb24vaxb2nhzwbg.Ipv4vpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_bmvksw5mb3jtyxrpb24vaxb2nhzwbg import Ipv4vpn
		return Ipv4vpn(self)

	@property
	def Ipv6Multicast(self):
		"""An instance of the Ipv6Multicast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_b3jtyxrpb24vaxb2nk11bhrpy2fzda.Ipv6Multicast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_b3jtyxrpb24vaxb2nk11bhrpy2fzda import Ipv6Multicast
		return Ipv6Multicast(self)

	@property
	def Ipv6MulticastVpn(self):
		"""An instance of the Ipv6MulticastVpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_yxrpb24vaxb2nk11bhrpy2fzdfzwbg.Ipv6MulticastVpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_yxrpb24vaxb2nk11bhrpy2fzdfzwbg import Ipv6MulticastVpn
		return Ipv6MulticastVpn(self)

	@property
	def Ipv6Unicast(self):
		"""An instance of the Ipv6Unicast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_w5mb3jtyxrpb24vaxb2nlvuawnhc3q.Ipv6Unicast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_w5mb3jtyxrpb24vaxb2nlvuawnhc3q import Ipv6Unicast
		return Ipv6Unicast(self)

	@property
	def Ipv6mpls(self):
		"""An instance of the Ipv6mpls class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_mvksw5mb3jtyxrpb24vaxb2nm1wbhm.Ipv6mpls)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_mvksw5mb3jtyxrpb24vaxb2nm1wbhm import Ipv6mpls
		return Ipv6mpls(self)

	@property
	def Ipv6vpn(self):
		"""An instance of the Ipv6vpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_bmvksw5mb3jtyxrpb24vaxb2nnzwbg.Ipv6vpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_bmvksw5mb3jtyxrpb24vaxb2nnzwbg import Ipv6vpn
		return Ipv6vpn(self)

	@property
	def Vpls(self):
		"""An instance of the Vpls class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_zwfybmvksw5mb3jtyxrpb24vdnbscw.Vpls)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_zwfybmvksw5mb3jtyxrpb24vdnbscw import Vpls
		return Vpls(self)

	@property
	def EvpnEthernetAdRouteCount(self):
		"""(read only) Number of AD-Routes learned and shown in A-D route learned info table.

		Returns:
			number
		"""
		return self._get_attribute('evpnEthernetAdRouteCount')

	@property
	def EvpnEthernetSegmentRouteCount(self):
		"""(read only) Number of Ethernet Segment routes learned and shown in ethernet segment route learned info table.

		Returns:
			number
		"""
		return self._get_attribute('evpnEthernetSegmentRouteCount')

	@property
	def EvpnMacRouteCount(self):
		"""(read only) Number of Macs learned and shown in mac learned info table.

		Returns:
			number
		"""
		return self._get_attribute('evpnMacRouteCount')

	@property
	def EvpnMulticastRouteCount(self):
		"""(read only) Number of RDs learned and shown in evpn multicast learned info table.

		Returns:
			number
		"""
		return self._get_attribute('evpnMulticastRouteCount')
