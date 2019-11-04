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
	"""The ISISL2/L3 Learned Information option fetches and shows the information learned by ISIS.
	The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'learnedInformation'

	def __init__(self, parent):
		super(LearnedInformation, self).__init__(parent)

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
	def Ipv4Prefixes(self):
		"""An instance of the Ipv4Prefixes class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_5mb3jtyxrpb24vaxb2nfbyzwzpegvz.Ipv4Prefixes)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_5mb3jtyxrpb24vaxb2nfbyzwzpegvz import Ipv4Prefixes
		return Ipv4Prefixes(self)

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
	def Ipv6Prefixes(self):
		"""An instance of the Ipv6Prefixes class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_5mb3jtyxrpb24vaxb2nlbyzwzpegvz.Ipv6Prefixes)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_5mb3jtyxrpb24vaxb2nlbyzwzpegvz import Ipv6Prefixes
		return Ipv6Prefixes(self)

	@property
	def MacMulticast(self):
		"""An instance of the MacMulticast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_5mb3jtyxrpb24vbwfjtxvsdgljyxn0.MacMulticast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_5mb3jtyxrpb24vbwfjtxvsdgljyxn0 import MacMulticast
		return MacMulticast(self)

	@property
	def RBridges(self):
		"""An instance of the RBridges class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_mvksw5mb3jtyxrpb24vckjyawrnzxm.RBridges)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_mvksw5mb3jtyxrpb24vckjyawrnzxm import RBridges
		return RBridges(self)

	@property
	def SpbRbridges(self):
		"""An instance of the SpbRbridges class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_w5mb3jtyxrpb24vc3biumjyawrnzxm.SpbRbridges)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_w5mb3jtyxrpb24vc3biumjyawrnzxm import SpbRbridges
		return SpbRbridges(self)

	@property
	def TrillMacUnicast(self):
		"""An instance of the TrillMacUnicast class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_jtyxrpb24vdhjpbgxnywnvbmljyxn0.TrillMacUnicast)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_jtyxrpb24vdhjpbgxnywnvbmljyxn0 import TrillMacUnicast
		return TrillMacUnicast(self)

	@property
	def TrillOamPing(self):
		"""An instance of the TrillOamPing class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_5mb3jtyxrpb24vdhjpbgxpyw1qaw5n.TrillOamPing)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_5mb3jtyxrpb24vdhjpbgxpyw1qaw5n import TrillOamPing
		return TrillOamPing(self)
