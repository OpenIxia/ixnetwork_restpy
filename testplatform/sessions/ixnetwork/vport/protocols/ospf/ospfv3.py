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


class OspfV3(Base):
	"""The OspfV3 class encapsulates a required ospfV3 node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the OspfV3 property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'ospfV3'

	def __init__(self, parent):
		super(OspfV3, self).__init__(parent)

	@property
	def Router(self):
		"""An instance of the Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf.router.Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf.router import Router
		return Router(self)

	@property
	def EnableDrOrBdr(self):
		"""Enables the OSPF Router to participate in DR/BDR election process

		Returns:
			bool
		"""
		return self._get_attribute('enableDrOrBdr')
	@EnableDrOrBdr.setter
	def EnableDrOrBdr(self, value):
		self._set_attribute('enableDrOrBdr', value)

	@property
	def Enabled(self):
		"""Enables this emulated OSPFv3 router.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def RunningState(self):
		"""The current state of the OSPFv6 router.

		Returns:
			str(unknown|stopped|stopping|starting|started)
		"""
		return self._get_attribute('runningState')

	def update(self, EnableDrOrBdr=None, Enabled=None):
		"""Updates a child instance of ospfV3 on the server.

		Args:
			EnableDrOrBdr (bool): Enables the OSPF Router to participate in DR/BDR election process
			Enabled (bool): Enables this emulated OSPFv3 router.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def GracefulRouterRestart(self, *args, **kwargs):
		"""Executes the gracefulRouterRestart operation on the server.

		NOT DEFINED

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		gracefulRouterRestart(Arg2:list)string
			Args:
				args[0] is Arg2 (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=router])): NOT DEFINED

			Returns:
				str: NOT DEFINED

		gracefulRouterRestart(Arg2:list, Arg3:number, Arg4:enum, Arg5:number)string
			Args:
				args[0] is Arg2 (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=router])): NOT DEFINED
				args[1] is Arg3 (number): NOT DEFINED
				args[2] is Arg4 (str(softwareReloadOrUpgrade|softwareRestart|switchToRedundantControlProcessor|unknown)): NOT DEFINED
				args[3] is Arg5 (number): NOT DEFINED

			Returns:
				str: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('gracefulRouterRestart', payload=payload, response_object=None)

	def Start(self):
		"""Executes the start operation on the server.

		Starts the OSPFv3 protocol on a port or group of ports simultaneously.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the OSPFv3 protocol on a port or group of ports simultaneously.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
