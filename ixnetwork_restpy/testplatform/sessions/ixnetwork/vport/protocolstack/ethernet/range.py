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


class Range(Base):
	"""The Range class encapsulates a user managed range node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Range property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'range'

	def __init__(self, parent):
		super(Range, self).__init__(parent)

	@property
	def Dot1xRange(self):
		"""An instance of the Dot1xRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.dot1xrange.Dot1xRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.dot1xrange import Dot1xRange
		return Dot1xRange(self)

	@property
	def EsmcRange(self):
		"""An instance of the EsmcRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.esmcrange.EsmcRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.esmcrange import EsmcRange
		return EsmcRange(self)

	@property
	def MacRange(self):
		"""An instance of the MacRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.macrange.MacRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.macrange import MacRange
		return MacRange(self)._select()

	@property
	def PtpRangeOverMac(self):
		"""An instance of the PtpRangeOverMac class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ptprangeovermac.PtpRangeOverMac)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ptprangeovermac import PtpRangeOverMac
		return PtpRangeOverMac(self)

	@property
	def VicClientRange(self):
		"""An instance of the VicClientRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.vicclientrange.VicClientRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.vicclientrange import VicClientRange
		return VicClientRange(self)

	@property
	def VlanRange(self):
		"""An instance of the VlanRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.vlanrange.VlanRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.vlanrange import VlanRange
		return VlanRange(self)._select()

	def add(self):
		"""Adds a new range node on the server and retrieves it in this instance.

		Returns:
			self: This instance with all currently retrieved range data using find and the newly added range data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the range data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self):
		"""Finds and retrieves range data from the server.

		All named parameters support regex and can be used to selectively retrieve range data from the server.
		By default the find method takes no parameters and will retrieve all range data from the server.

		Returns:
			self: This instance with matching range data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of range data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the range data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def CustomProtocolStack(self, *args, **kwargs):
		"""Executes the customProtocolStack operation on the server.

		Create custom protocol stack under /vport/protocolStack

		customProtocolStack(Arg2:list, Arg3:enum)
			Args:
				args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
				args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('customProtocolStack', payload=payload, response_object=None)

	def DisableProtocolStack(self, *args, **kwargs):
		"""Executes the disableProtocolStack operation on the server.

		Disable a protocol under protocolStack using the class name

		disableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to disable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disableProtocolStack', payload=payload, response_object=None)

	def EnableProtocolStack(self, *args, **kwargs):
		"""Executes the enableProtocolStack operation on the server.

		Enable a protocol under protocolStack using the class name

		enableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to enable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableProtocolStack', payload=payload, response_object=None)
