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


class Static(Base):
	"""This object controls the static configuration of ports.
	The Static class encapsulates a required static resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'static'

	def __init__(self, parent):
		super(Static, self).__init__(parent)

	@property
	def Atm(self):
		"""An instance of the Atm class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atm_j0l3byb3rvy29scy9zdgf0awmvyxrt.Atm)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atm_j0l3byb3rvy29scy9zdgf0awmvyxrt import Atm
		return Atm(self)

	@property
	def Fr(self):
		"""An instance of the Fr class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fr_3j0l3byb3rvy29scy9zdgf0awmvzni.Fr)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fr_3j0l3byb3rvy29scy9zdgf0awmvzni import Fr
		return Fr(self)

	@property
	def InterfaceGroup(self):
		"""An instance of the InterfaceGroup class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacegroup_y9zdgf0awmvaw50zxjmywnlr3jvdxa.InterfaceGroup)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacegroup_y9zdgf0awmvaw50zxjmywnlr3jvdxa import InterfaceGroup
		return InterfaceGroup(self)

	@property
	def Ip(self):
		"""An instance of the Ip class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ip_3j0l3byb3rvy29scy9zdgf0awmvaxa.Ip)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ip_3j0l3byb3rvy29scy9zdgf0awmvaxa import Ip
		return Ip(self)

	@property
	def Lan(self):
		"""An instance of the Lan class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_j0l3byb3rvy29scy9zdgf0awmvbgfu.Lan)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_j0l3byb3rvy29scy9zdgf0awmvbgfu import Lan
		return Lan(self)
