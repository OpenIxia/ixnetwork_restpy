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


class SwitchPorts(Base):
	"""This object allows to define the attributes for the physical Switch Ports.
	The SwitchPorts class encapsulates a list of switchPorts resources that is be managed by the user.
	A list of resources can be retrieved from the server using the SwitchPorts.find() method.
	The list can be managed by the user by using the SwitchPorts.add() and SwitchPorts.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'switchPorts'

	def __init__(self, parent):
		super(SwitchPorts, self).__init__(parent)

	@property
	def AdvertisedFeatures(self):
		"""An instance of the AdvertisedFeatures class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_3j0cy9hzhzlcnrpc2vkrmvhdhvyzxm.AdvertisedFeatures)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advertisedfeatures_3j0cy9hzhzlcnrpc2vkrmvhdhvyzxm import AdvertisedFeatures
		return AdvertisedFeatures(self)._select()

	@property
	def Config(self):
		"""An instance of the Config class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_m5lbc9zd2l0y2hqb3j0cy9jb25mawc.Config)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.config_m5lbc9zd2l0y2hqb3j0cy9jb25mawc import Config
		return Config(self)._select()

	@property
	def CurrentFeatures(self):
		"""An instance of the CurrentFeatures class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_2hqb3j0cy9jdxjyzw50rmvhdhvyzxm.CurrentFeatures)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.currentfeatures_2hqb3j0cy9jdxjyzw50rmvhdhvyzxm import CurrentFeatures
		return CurrentFeatures(self)._select()

	@property
	def PeerAdvertisedFeatures(self):
		"""An instance of the PeerAdvertisedFeatures class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_9wzwvyqwr2zxj0axnlzezlyxr1cmvz.PeerAdvertisedFeatures)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.peeradvertisedfeatures_9wzwvyqwr2zxj0axnlzezlyxr1cmvz import PeerAdvertisedFeatures
		return PeerAdvertisedFeatures(self)._select()

	@property
	def State(self):
		"""An instance of the State class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_bm5lbc9zd2l0y2hqb3j0cy9zdgf0zq.State)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.state_bm5lbc9zd2l0y2hqb3j0cy9zdgf0zq import State
		return State(self)._select()

	@property
	def SupportedFeatures(self):
		"""An instance of the SupportedFeatures class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_b3j0cy9zdxbwb3j0zwrgzwf0dxjlcw.SupportedFeatures)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedfeatures_b3j0cy9zdxbwb3j0zwrgzwf0dxjlcw import SupportedFeatures
		return SupportedFeatures(self)._select()

	@property
	def SwitchPortQueues(self):
		"""An instance of the SwitchPortQueues class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_hqb3j0cy9zd2l0y2hqb3j0uxvldwvz.SwitchPortQueues)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchportqueues_hqb3j0cy9zd2l0y2hqb3j0uxvldwvz import SwitchPortQueues
		return SwitchPortQueues(self)

	@property
	def Enabled(self):
		"""If true, the ports in the selected port range are added to the switch.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def EthernetAddress(self):
		"""Indicates the hardware address of the ports in the port range.

		Returns:
			str
		"""
		return self._get_attribute('ethernetAddress')
	@EthernetAddress.setter
	def EthernetAddress(self, value):
		self._set_attribute('ethernetAddress', value)

	@property
	def NumberOfPorts(self):
		"""Specifies the number of ports in a port range.

		Returns:
			number
		"""
		return self._get_attribute('numberOfPorts')
	@NumberOfPorts.setter
	def NumberOfPorts(self, value):
		self._set_attribute('numberOfPorts', value)

	@property
	def PortName(self):
		"""Indicates the name for the switch port interface.

		Returns:
			str
		"""
		return self._get_attribute('portName')
	@PortName.setter
	def PortName(self, value):
		self._set_attribute('portName', value)

	@property
	def PortNumber(self):
		"""Indicates a value that the datapath associates with a physical port.

		Returns:
			str
		"""
		return self._get_attribute('portNumber')
	@PortNumber.setter
	def PortNumber(self, value):
		self._set_attribute('portNumber', value)

	def update(self, Enabled=None, EthernetAddress=None, NumberOfPorts=None, PortName=None, PortNumber=None):
		"""Updates a child instance of switchPorts on the server.

		Args:
			Enabled (bool): If true, the ports in the selected port range are added to the switch.
			EthernetAddress (str): Indicates the hardware address of the ports in the port range.
			NumberOfPorts (number): Specifies the number of ports in a port range.
			PortName (str): Indicates the name for the switch port interface.
			PortNumber (str): Indicates a value that the datapath associates with a physical port.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Enabled=None, EthernetAddress=None, NumberOfPorts=None, PortName=None, PortNumber=None):
		"""Adds a new switchPorts node on the server and retrieves it in this instance.

		Args:
			Enabled (bool): If true, the ports in the selected port range are added to the switch.
			EthernetAddress (str): Indicates the hardware address of the ports in the port range.
			NumberOfPorts (number): Specifies the number of ports in a port range.
			PortName (str): Indicates the name for the switch port interface.
			PortNumber (str): Indicates a value that the datapath associates with a physical port.

		Returns:
			self: This instance with all currently retrieved switchPorts data using find and the newly added switchPorts data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the switchPorts data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Enabled=None, EthernetAddress=None, NumberOfPorts=None, PortName=None, PortNumber=None):
		"""Finds and retrieves switchPorts data from the server.

		All named parameters support regex and can be used to selectively retrieve switchPorts data from the server.
		By default the find method takes no parameters and will retrieve all switchPorts data from the server.

		Args:
			Enabled (bool): If true, the ports in the selected port range are added to the switch.
			EthernetAddress (str): Indicates the hardware address of the ports in the port range.
			NumberOfPorts (number): Specifies the number of ports in a port range.
			PortName (str): Indicates the name for the switch port interface.
			PortNumber (str): Indicates a value that the datapath associates with a physical port.

		Returns:
			self: This instance with matching switchPorts data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of switchPorts data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the switchPorts data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def SimulatePortUpDown(self):
		"""Executes the simulatePortUpDown operation on the server.

		Exec to simulate port up and down.

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('simulatePortUpDown', payload=payload, response_object=None)
