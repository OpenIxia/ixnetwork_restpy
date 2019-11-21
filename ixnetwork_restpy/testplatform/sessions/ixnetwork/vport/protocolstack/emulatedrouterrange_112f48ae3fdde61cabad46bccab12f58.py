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


class EmulatedRouterRange(Base):
	"""Emulated Router range. Provides ability to have multiple IPs with same MAC address 
        (just like it would appear behind a router).
	The EmulatedRouterRange class encapsulates a required emulatedRouterRange resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'emulatedRouterRange'

	def __init__(self, parent):
		super(EmulatedRouterRange, self).__init__(parent)

	@property
	def AutoCountEnabled(self):
		"""If set, IP address count will be automatically adjusted based on other plugins

		Returns:
			bool
		"""
		return self._get_attribute('autoCountEnabled')
	@AutoCountEnabled.setter
	def AutoCountEnabled(self, value):
		self._set_attribute('autoCountEnabled', value)

	@property
	def AutoMacGeneration(self):
		"""If set, MAC addresses will be auto-generated based on IP

		Returns:
			bool
		"""
		return self._get_attribute('autoMacGeneration')
	@AutoMacGeneration.setter
	def AutoMacGeneration(self, value):
		self._set_attribute('autoMacGeneration', value)

	@property
	def Count(self):
		"""The total number of addresses to be created for the range.

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def EnableGatewayArp(self):
		"""Deprecated property, please use Static IP globals instead.

		Returns:
			bool
		"""
		return self._get_attribute('enableGatewayArp')
	@EnableGatewayArp.setter
	def EnableGatewayArp(self, value):
		self._set_attribute('enableGatewayArp', value)

	@property
	def Enabled(self):
		"""Disabled ranges won't be configured nor validated.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def GatewayAddress(self):
		"""Defines the gateway to be associated with all the addresses created in the range.

		Returns:
			str
		"""
		return self._get_attribute('gatewayAddress')
	@GatewayAddress.setter
	def GatewayAddress(self, value):
		self._set_attribute('gatewayAddress', value)

	@property
	def GatewayIncrement(self):
		"""Defines the gateway step size to be used in the association with the addresses created in the range.

		Returns:
			str
		"""
		return self._get_attribute('gatewayIncrement')
	@GatewayIncrement.setter
	def GatewayIncrement(self, value):
		self._set_attribute('gatewayIncrement', value)

	@property
	def GatewayIncrementMode(self):
		"""Defines the gateway step size to be used in the association with the addresses created in the range.

		Returns:
			str
		"""
		return self._get_attribute('gatewayIncrementMode')
	@GatewayIncrementMode.setter
	def GatewayIncrementMode(self, value):
		self._set_attribute('gatewayIncrementMode', value)

	@property
	def IncrementBy(self):
		"""Defines the increment to be used for enumerating all the addresses in the range.

		Returns:
			str
		"""
		return self._get_attribute('incrementBy')
	@IncrementBy.setter
	def IncrementBy(self, value):
		self._set_attribute('incrementBy', value)

	@property
	def IpAddress(self):
		"""Defines the base address to be used for enumerating all the addresses in the range.

		Returns:
			str
		"""
		return self._get_attribute('ipAddress')
	@IpAddress.setter
	def IpAddress(self, value):
		self._set_attribute('ipAddress', value)

	@property
	def IpType(self):
		"""Defines the version of IP address style to be used for describing the range.

		Returns:
			str
		"""
		return self._get_attribute('ipType')
	@IpType.setter
	def IpType(self, value):
		self._set_attribute('ipType', value)

	@property
	def Mss(self):
		"""The Maximum Segment Size, defines the maximum length of the data. TCP MSS = MTU - TCP header size - IP header size. Theoretically, this value can be as large as 65495, but such a large value is never used. For traditional Ethernet the maximum value for MSS is 1460 = 1500-40. With Jumbo Frame support, the maximum value is 9460 = 9500-40.

		Returns:
			number
		"""
		return self._get_attribute('mss')
	@Mss.setter
	def Mss(self, value):
		self._set_attribute('mss', value)

	@property
	def Name(self):
		"""Name of range

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def Prefix(self):
		"""Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.

		Returns:
			number
		"""
		return self._get_attribute('prefix')
	@Prefix.setter
	def Prefix(self, value):
		self._set_attribute('prefix', value)

	def update(self, AutoCountEnabled=None, AutoMacGeneration=None, Count=None, EnableGatewayArp=None, Enabled=None, GatewayAddress=None, GatewayIncrement=None, GatewayIncrementMode=None, IncrementBy=None, IpAddress=None, IpType=None, Mss=None, Name=None, Prefix=None):
		"""Updates a child instance of emulatedRouterRange on the server.

		Args:
			AutoCountEnabled (bool): If set, IP address count will be automatically adjusted based on other plugins
			AutoMacGeneration (bool): If set, MAC addresses will be auto-generated based on IP
			Count (number): The total number of addresses to be created for the range.
			EnableGatewayArp (bool): Deprecated property, please use Static IP globals instead.
			Enabled (bool): Disabled ranges won't be configured nor validated.
			GatewayAddress (str): Defines the gateway to be associated with all the addresses created in the range.
			GatewayIncrement (str): Defines the gateway step size to be used in the association with the addresses created in the range.
			GatewayIncrementMode (str): Defines the gateway step size to be used in the association with the addresses created in the range.
			IncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
			IpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
			IpType (str): Defines the version of IP address style to be used for describing the range.
			Mss (number): The Maximum Segment Size, defines the maximum length of the data. TCP MSS = MTU - TCP header size - IP header size. Theoretically, this value can be as large as 65495, but such a large value is never used. For traditional Ethernet the maximum value for MSS is 1460 = 1500-40. With Jumbo Frame support, the maximum value is 9460 = 9500-40.
			Name (str): Name of range
			Prefix (number): Defines the length (in bits) of the mask to be used in conjunction with all the addresses created in the range. e.g., a prefix of 24 = 255.255.255.0 for IPv4.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

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
