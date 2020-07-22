# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
    """List of interfaces that can be configured on ports. Multiple protocol interfaces can be configured for Ixia ports that support this capability, with the number of protocol interfaces being dependent on the amount of memory available on the Ixia port.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'Enabled': 'enabled',
        'Eui64Id': 'eui64Id',
        'Mtu': 'mtu',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def Atm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.atm.atm.Atm): An instance of the Atm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.atm.atm import Atm
        return Atm(self)._select()

    @property
    def DhcpV4DiscoveredInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4discoveredinfo.dhcpv4discoveredinfo.DhcpV4DiscoveredInfo): An instance of the DhcpV4DiscoveredInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4discoveredinfo.dhcpv4discoveredinfo import DhcpV4DiscoveredInfo
        return DhcpV4DiscoveredInfo(self)._select()

    @property
    def DhcpV4Properties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4properties.dhcpv4properties.DhcpV4Properties): An instance of the DhcpV4Properties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv4properties.dhcpv4properties import DhcpV4Properties
        return DhcpV4Properties(self)._select()

    @property
    def DhcpV6DiscoveredInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6discoveredinfo.dhcpv6discoveredinfo.DhcpV6DiscoveredInfo): An instance of the DhcpV6DiscoveredInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6discoveredinfo.dhcpv6discoveredinfo import DhcpV6DiscoveredInfo
        return DhcpV6DiscoveredInfo(self)._select()

    @property
    def DhcpV6Properties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6properties.dhcpv6properties.DhcpV6Properties): An instance of the DhcpV6Properties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.dhcpv6properties.dhcpv6properties import DhcpV6Properties
        return DhcpV6Properties(self)._select()

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ethernet.ethernet.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ethernet.ethernet import Ethernet
        return Ethernet(self)._select()

    @property
    def Gre(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.gre.gre.Gre): An instance of the Gre class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.gre.gre import Gre
        return Gre(self)._select()

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv4.ipv4.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv4.ipv4 import Ipv4
        return Ipv4(self)

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv6.ipv6.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.ipv6.ipv6 import Ipv6
        return Ipv6(self)

    @property
    def Unconnected(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.unconnected.unconnected.Unconnected): An instance of the Unconnected class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.unconnected.unconnected import Unconnected
        return Unconnected(self)._select()

    @property
    def Vlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.vlan.vlan.Vlan): An instance of the Vlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.interface.vlan.vlan import Vlan
        return Vlan(self)._select()

    @property
    def Description(self):
        """
        Returns
        -------
        - str: The identifier for the port including card and port numbers, and the port type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the selected protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Eui64Id(self):
        """
        Returns
        -------
        - str: This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Eui64Id'])
    @Eui64Id.setter
    def Eui64Id(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Eui64Id'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: The maximum transmission unit for the interfaces created with this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(default | gre | routed): The identifier or 'tag' for this DHCP option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, Description=None, Enabled=None, Eui64Id=None, Mtu=None, Type=None):
        """Updates interface resource on the server.

        Args
        ----
        - Description (str): The identifier for the port including card and port numbers, and the port type.
        - Enabled (bool): Enables the selected protocol interface.
        - Eui64Id (str): This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
        - Mtu (number): The maximum transmission unit for the interfaces created with this range.
        - Type (str(default | gre | routed)): The identifier or 'tag' for this DHCP option.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, Enabled=None, Eui64Id=None, Mtu=None, Type=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - Description (str): The identifier for the port including card and port numbers, and the port type.
        - Enabled (bool): Enables the selected protocol interface.
        - Eui64Id (str): This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
        - Mtu (number): The maximum transmission unit for the interfaces created with this range.
        - Type (str(default | gre | routed)): The identifier or 'tag' for this DHCP option.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Description=None, Enabled=None, Eui64Id=None, Mtu=None, Type=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - Description (str): The identifier for the port including card and port numbers, and the port type.
        - Enabled (bool): Enables the selected protocol interface.
        - Eui64Id (str): This is the 64-bit IEEE Modified EUI ID value for the Interface Identifier portion of the IPv6 address.
        - Mtu (number): The maximum transmission unit for the interfaces created with this range.
        - Type (str(default | gre | routed)): The identifier or 'tag' for this DHCP option.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SendArp(self):
        """Executes the sendArp operation on the server.

        Sends an ARP to an interface or group of interfaces.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendArp', payload=payload, response_object=None)

    def SendArpAndNS(self):
        """Executes the sendArpAndNS operation on the server.

        Send ARP and neighbor solicitation to an interface or group of interfaces.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendArpAndNS', payload=payload, response_object=None)

    def SendNs(self):
        """Executes the sendNs operation on the server.

        Sends NS to an interface or group of interfaces.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendNs', payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Sends a ping to a port or group of ports.

        sendPing(Arg2=string)string
        ---------------------------
        - Arg2 (str): IP address for which ping is send.
        - Returns str: Returns reply from the IP for which ping has been send.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPing', payload=payload, response_object=None)

    def SendRs(self):
        """Executes the sendRs operation on the server.

        Sends router solicitation to an interface or group of interfaces.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendRs', payload=payload, response_object=None)
