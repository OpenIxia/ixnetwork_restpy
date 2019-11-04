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


class Protocols(Base):
	"""Allows the user to select a set of protocols that are enabled for a newly added port.
	The Protocols class encapsulates a list of protocols resources that is managed by the system.
	A list of resources can be retrieved from the server using the Protocols.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'protocols'

	def __init__(self, parent):
		super(Protocols, self).__init__(parent)

	@property
	def Arp(self):
		"""An instance of the Arp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_l3zwb3j0l3byb3rvy29scy9hcna.Arp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_l3zwb3j0l3byb3rvy29scy9hcna import Arp
		return Arp(self)

	@property
	def Bfd(self):
		"""An instance of the Bfd class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_l3zwb3j0l3byb3rvy29scy9izmq.Bfd)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_l3zwb3j0l3byb3rvy29scy9izmq import Bfd
		return Bfd(self)._select()

	@property
	def Bgp(self):
		"""An instance of the Bgp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_l3zwb3j0l3byb3rvy29scy9iz3a.Bgp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_l3zwb3j0l3byb3rvy29scy9iz3a import Bgp
		return Bgp(self)._select()

	@property
	def Cfm(self):
		"""An instance of the Cfm class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_l3zwb3j0l3byb3rvy29scy9jzm0.Cfm)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_l3zwb3j0l3byb3rvy29scy9jzm0 import Cfm
		return Cfm(self)._select()

	@property
	def Eigrp(self):
		"""An instance of the Eigrp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_l3zwb3j0l3byb3rvy29scy9lawdyca.Eigrp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_l3zwb3j0l3byb3rvy29scy9lawdyca import Eigrp
		return Eigrp(self)._select()

	@property
	def Elmi(self):
		"""An instance of the Elmi class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_l3zwb3j0l3byb3rvy29scy9lbg1p.Elmi)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_l3zwb3j0l3byb3rvy29scy9lbg1p import Elmi
		return Elmi(self)._select()

	@property
	def Igmp(self):
		"""An instance of the Igmp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_l3zwb3j0l3byb3rvy29scy9pz21w.Igmp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_l3zwb3j0l3byb3rvy29scy9pz21w import Igmp
		return Igmp(self)._select()

	@property
	def Isis(self):
		"""An instance of the Isis class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_l3zwb3j0l3byb3rvy29scy9pc2lz.Isis)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_l3zwb3j0l3byb3rvy29scy9pc2lz import Isis
		return Isis(self)._select()

	@property
	def Lacp(self):
		"""An instance of the Lacp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_l3zwb3j0l3byb3rvy29scy9sywnw.Lacp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_l3zwb3j0l3byb3rvy29scy9sywnw import Lacp
		return Lacp(self)._select()

	@property
	def Ldp(self):
		"""An instance of the Ldp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_l3zwb3j0l3byb3rvy29scy9szha.Ldp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_l3zwb3j0l3byb3rvy29scy9szha import Ldp
		return Ldp(self)._select()

	@property
	def LinkOam(self):
		"""An instance of the LinkOam class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_zwb3j0l3byb3rvy29scy9saw5rt2ft.LinkOam)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_zwb3j0l3byb3rvy29scy9saw5rt2ft import LinkOam
		return LinkOam(self)._select()

	@property
	def Lisp(self):
		"""An instance of the Lisp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_l3zwb3j0l3byb3rvy29scy9saxnw.Lisp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_l3zwb3j0l3byb3rvy29scy9saxnw import Lisp
		return Lisp(self)._select()

	@property
	def Mld(self):
		"""An instance of the Mld class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_l3zwb3j0l3byb3rvy29scy9tbgq.Mld)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_l3zwb3j0l3byb3rvy29scy9tbgq import Mld
		return Mld(self)._select()

	@property
	def MplsOam(self):
		"""An instance of the MplsOam class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_zwb3j0l3byb3rvy29scy9tcgxzt2ft.MplsOam)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_zwb3j0l3byb3rvy29scy9tcgxzt2ft import MplsOam
		return MplsOam(self)._select()

	@property
	def MplsTp(self):
		"""An instance of the MplsTp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_3zwb3j0l3byb3rvy29scy9tcgxzvha.MplsTp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_3zwb3j0l3byb3rvy29scy9tcgxzvha import MplsTp
		return MplsTp(self)._select()

	@property
	def OpenFlow(self):
		"""An instance of the OpenFlow class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_b3j0l3byb3rvy29scy9vcgvurmxvdw.OpenFlow)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_b3j0l3byb3rvy29scy9vcgvurmxvdw import OpenFlow
		return OpenFlow(self)._select()

	@property
	def Ospf(self):
		"""An instance of the Ospf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_l3zwb3j0l3byb3rvy29scy9vc3bm.Ospf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_l3zwb3j0l3byb3rvy29scy9vc3bm import Ospf
		return Ospf(self)._select()

	@property
	def OspfV3(self):
		"""An instance of the OspfV3 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_3zwb3j0l3byb3rvy29scy9vc3bmvjm.OspfV3)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_3zwb3j0l3byb3rvy29scy9vc3bmvjm import OspfV3
		return OspfV3(self)._select()

	@property
	def Pimsm(self):
		"""An instance of the Pimsm class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_l3zwb3j0l3byb3rvy29scy9waw1zbq.Pimsm)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_l3zwb3j0l3byb3rvy29scy9waw1zbq import Pimsm
		return Pimsm(self)._select()

	@property
	def Ping(self):
		"""An instance of the Ping class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_l3zwb3j0l3byb3rvy29scy9waw5n.Ping)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_l3zwb3j0l3byb3rvy29scy9waw5n import Ping
		return Ping(self)

	@property
	def Rip(self):
		"""An instance of the Rip class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_l3zwb3j0l3byb3rvy29scy9yaxa.Rip)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_l3zwb3j0l3byb3rvy29scy9yaxa import Rip
		return Rip(self)._select()

	@property
	def Ripng(self):
		"""An instance of the Ripng class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_l3zwb3j0l3byb3rvy29scy9yaxbuzw.Ripng)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_l3zwb3j0l3byb3rvy29scy9yaxbuzw import Ripng
		return Ripng(self)._select()

	@property
	def Rsvp(self):
		"""An instance of the Rsvp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_l3zwb3j0l3byb3rvy29scy9yc3zw.Rsvp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_l3zwb3j0l3byb3rvy29scy9yc3zw import Rsvp
		return Rsvp(self)._select()

	@property
	def Static(self):
		"""An instance of the Static class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_3zwb3j0l3byb3rvy29scy9zdgf0awm.Static)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_3zwb3j0l3byb3rvy29scy9zdgf0awm import Static
		return Static(self)._select()

	@property
	def Stp(self):
		"""An instance of the Stp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_l3zwb3j0l3byb3rvy29scy9zdha.Stp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_l3zwb3j0l3byb3rvy29scy9zdha import Stp
		return Stp(self)._select()

	@property
	def ProtocolMaxNodeCount(self):
		"""Shows maximum number of node.

		Returns:
			number
		"""
		return self._get_attribute('protocolMaxNodeCount')

	def find(self, ProtocolMaxNodeCount=None):
		"""Finds and retrieves protocols data from the server.

		All named parameters support regex and can be used to selectively retrieve protocols data from the server.
		By default the find method takes no parameters and will retrieve all protocols data from the server.

		Args:
			ProtocolMaxNodeCount (number): Shows maximum number of node.

		Returns:
			self: This instance with matching protocols data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of protocols data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the protocols data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
