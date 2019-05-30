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


class Interface(Base):
	"""The Interface class encapsulates a user managed interface node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Interface property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'interface'

	def __init__(self, parent):
		super(Interface, self).__init__(parent)

	@property
	def Atm(self):
		"""An instance of the Atm class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.atm.atm.Atm)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.atm.atm import Atm
		return Atm(self)._select()

	@property
	def DhcpV4DiscoveredInfo(self):
		"""An instance of the DhcpV4DiscoveredInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4discoveredinfo.dhcpv4discoveredinfo.DhcpV4DiscoveredInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4discoveredinfo.dhcpv4discoveredinfo import DhcpV4DiscoveredInfo
		return DhcpV4DiscoveredInfo(self)._select()

	@property
	def DhcpV4Properties(self):
		"""An instance of the DhcpV4Properties class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4properties.dhcpv4properties.DhcpV4Properties)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4properties.dhcpv4properties import DhcpV4Properties
		return DhcpV4Properties(self)._select()

	@property
	def DhcpV6DiscoveredInfo(self):
		"""An instance of the DhcpV6DiscoveredInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6discoveredinfo.dhcpv6discoveredinfo.DhcpV6DiscoveredInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6discoveredinfo.dhcpv6discoveredinfo import DhcpV6DiscoveredInfo
		return DhcpV6DiscoveredInfo(self)._select()

	@property
	def DhcpV6Properties(self):
		"""An instance of the DhcpV6Properties class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6properties.dhcpv6properties.DhcpV6Properties)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6properties.dhcpv6properties import DhcpV6Properties
		return DhcpV6Properties(self)._select()

	@property
	def Ethernet(self):
		"""An instance of the Ethernet class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ethernet.ethernet.Ethernet)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ethernet.ethernet import Ethernet
		return Ethernet(self)._select()

	@property
	def Gre(self):
		"""An instance of the Gre class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.gre.gre.Gre)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.gre.gre import Gre
		return Gre(self)._select()

	@property
	def Ipv4(self):
		"""An instance of the Ipv4 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv4.ipv4.Ipv4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv4.ipv4 import Ipv4
		return Ipv4(self)

	@property
	def Ipv6(self):
		"""An instance of the Ipv6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv6.ipv6.Ipv6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv6.ipv6 import Ipv6
		return Ipv6(self)

	@property
	def Unconnected(self):
		"""An instance of the Unconnected class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.unconnected.unconnected.Unconnected)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.unconnected.unconnected import Unconnected
		return Unconnected(self)._select()

	@property
	def Vlan(self):
		"""An instance of the Vlan class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.vlan.vlan.Vlan)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.vlan.vlan import Vlan
		return Vlan(self)._select()

	@property
	def Description(self):
		"""The identifier for the port including card and port numbers, and the port type.

		Returns:
			str
		"""
		return self._get_attribute('description')
	@Description.setter
	def Description(self, value):
		self._set_attribute('description', value)

	@property
	def Enabled(self):
		"""Enables the selected protocol interface.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Eui64Id(self):
		"""This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.

		Returns:
			str
		"""
		return self._get_attribute('eui64Id')
	@Eui64Id.setter
	def Eui64Id(self, value):
		self._set_attribute('eui64Id', value)

	@property
	def Mtu(self):
		"""The maximum transmission unit for the interfaces created with this range.

		Returns:
			number
		"""
		return self._get_attribute('mtu')
	@Mtu.setter
	def Mtu(self, value):
		self._set_attribute('mtu', value)

	@property
	def Type(self):
		"""The identifier or 'tag' for this DHCP option.

		Returns:
			str(default|gre|routed)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	def update(self, Description=None, Enabled=None, Eui64Id=None, Mtu=None, Type=None):
		"""Updates a child instance of interface on the server.

		Args:
			Description (str): The identifier for the port including card and port numbers, and the port type.
			Enabled (bool): Enables the selected protocol interface.
			Eui64Id (str): This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
			Mtu (number): The maximum transmission unit for the interfaces created with this range.
			Type (str(default|gre|routed)): The identifier or 'tag' for this DHCP option.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Description=None, Enabled=None, Eui64Id=None, Mtu=None, Type=None):
		"""Adds a new interface node on the server and retrieves it in this instance.

		Args:
			Description (str): The identifier for the port including card and port numbers, and the port type.
			Enabled (bool): Enables the selected protocol interface.
			Eui64Id (str): This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
			Mtu (number): The maximum transmission unit for the interfaces created with this range.
			Type (str(default|gre|routed)): The identifier or 'tag' for this DHCP option.

		Returns:
			self: This instance with all currently retrieved interface data using find and the newly added interface data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the interface data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Description=None, Enabled=None, Eui64Id=None, Mtu=None, Type=None):
		"""Finds and retrieves interface data from the server.

		All named parameters support regex and can be used to selectively retrieve interface data from the server.
		By default the find method takes no parameters and will retrieve all interface data from the server.

		Args:
			Description (str): The identifier for the port including card and port numbers, and the port type.
			Enabled (bool): Enables the selected protocol interface.
			Eui64Id (str): This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
			Mtu (number): The maximum transmission unit for the interfaces created with this range.
			Type (str(default|gre|routed)): The identifier or 'tag' for this DHCP option.

		Returns:
			self: This instance with matching interface data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of interface data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the interface data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def SendArp(self):
		"""Executes the sendArp operation on the server.

		Sends an ARP to an interface or group of interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('sendArp', payload=payload, response_object=None)

	def SendArpAndNS(self):
		"""Executes the sendArpAndNS operation on the server.

		Send ARP and neighbor solicitation to an interface or group of interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('sendArpAndNS', payload=payload, response_object=None)

	def SendNs(self):
		"""Executes the sendNs operation on the server.

		Sends NS to an interface or group of interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('sendNs', payload=payload, response_object=None)

	def SendPing(self, *args, **kwargs):
		"""Executes the sendPing operation on the server.

		Sends a ping to a port or group of ports.

		sendPing(Arg2:string)string
			Args:
				args[0] is Arg2 (str): IP address for which ping is send.

			Returns:
				str: Returns reply from the IP for which ping has been send.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendPing', payload=payload, response_object=None)

	def SendRs(self):
		"""Executes the sendRs operation on the server.

		Sends router solicitation to an interface or group of interfaces.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('sendRs', payload=payload, response_object=None)
