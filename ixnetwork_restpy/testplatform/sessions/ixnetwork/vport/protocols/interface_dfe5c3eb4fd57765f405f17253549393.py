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


class Interface(Base):
    """A network interface to be included in this OSPFv3 router.
    The Interface class encapsulates a list of interface resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by the user by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def Area(self):
        """The OSPFv3 area as a 32-bit number.

        Returns:
            number
        """
        return self._get_attribute('area')
    @Area.setter
    def Area(self, value):
        self._set_attribute('area', value)

    @property
    def DeadInterval(self):
        """The number of seconds before declaring a silent router as being down.

        Returns:
            number
        """
        return self._get_attribute('deadInterval')
    @DeadInterval.setter
    def DeadInterval(self, value):
        self._set_attribute('deadInterval', value)

    @property
    def EnableBfdRegistration(self):
        """Enables the BFD registration.

        Returns:
            bool
        """
        return self._get_attribute('enableBfdRegistration')
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute('enableBfdRegistration', value)

    @property
    def EnableFastHello(self):
        """Enables Fast Hello option for OSPF Router

        Returns:
            bool
        """
        return self._get_attribute('enableFastHello')
    @EnableFastHello.setter
    def EnableFastHello(self, value):
        self._set_attribute('enableFastHello', value)

    @property
    def EnableIgnoreDbDescMtu(self):
        """If true, enables the ability for the router to ignore the database described MTU.

        Returns:
            bool
        """
        return self._get_attribute('enableIgnoreDbDescMtu')
    @EnableIgnoreDbDescMtu.setter
    def EnableIgnoreDbDescMtu(self, value):
        self._set_attribute('enableIgnoreDbDescMtu', value)

    @property
    def Enabled(self):
        """Enables the use of the simulated interface.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def HelloInterval(self):
        """The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.

        Returns:
            number
        """
        return self._get_attribute('helloInterval')
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute('helloInterval', value)

    @property
    def HelloMultiplier(self):
        """Indicates the number of Hello Packets transmitted per second

        Returns:
            number
        """
        return self._get_attribute('helloMultiplier')
    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._set_attribute('helloMultiplier', value)

    @property
    def InstanceId(self):
        """Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.

        Returns:
            number
        """
        return self._get_attribute('instanceId')
    @InstanceId.setter
    def InstanceId(self, value):
        self._set_attribute('instanceId', value)

    @property
    def InterfaceIndex(self):
        """The assigned protocol interface ID for this OSPFv3 interface.

        Returns:
            number
        """
        return self._get_attribute('interfaceIndex')
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute('interfaceIndex', value)

    @property
    def InterfaceType(self):
        """Indicates the type of network for the interface.

        Returns:
            str(pointToPoint|broadcast)
        """
        return self._get_attribute('interfaceType')
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute('interfaceType', value)

    @property
    def InterfaceTypes(self):
        """The type of interface to be selected for this OSPFv3 interface.

        Returns:
            str
        """
        return self._get_attribute('interfaceTypes')
    @InterfaceTypes.setter
    def InterfaceTypes(self, value):
        self._set_attribute('interfaceTypes', value)

    @property
    def Interfaces(self):
        """The interfaces that are associated with the selected interface type.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)
        """
        return self._get_attribute('interfaces')
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute('interfaces', value)

    @property
    def LinkMetric(self):
        """The metric for the link connecting the grid with the emulated OSPFv3 router.

        Returns:
            number
        """
        return self._get_attribute('linkMetric')
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute('linkMetric', value)

    @property
    def Priority(self):
        """Indicates the OSPF interface priority

        Returns:
            number
        """
        return self._get_attribute('priority')
    @Priority.setter
    def Priority(self, value):
        self._set_attribute('priority', value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED This is the name of this emulated OSPFv3 interface on this emulated router.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)
        """
        return self._get_attribute('protocolInterface')
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute('protocolInterface', value)

    @property
    def RouterOptions(self):
        """Options related to the interface. Multiple options may be or'd together. (default = 0x13).

        Returns:
            number
        """
        return self._get_attribute('routerOptions')
    @RouterOptions.setter
    def RouterOptions(self, value):
        self._set_attribute('routerOptions', value)

    def update(self, Area=None, DeadInterval=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, Enabled=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, InterfaceIndex=None, InterfaceType=None, InterfaceTypes=None, Interfaces=None, LinkMetric=None, Priority=None, ProtocolInterface=None, RouterOptions=None):
        """Updates a child instance of interface on the server.

        Args:
            Area (number): The OSPFv3 area as a 32-bit number.
            DeadInterval (number): The number of seconds before declaring a silent router as being down.
            EnableBfdRegistration (bool): Enables the BFD registration.
            EnableFastHello (bool): Enables Fast Hello option for OSPF Router
            EnableIgnoreDbDescMtu (bool): If true, enables the ability for the router to ignore the database described MTU.
            Enabled (bool): Enables the use of the simulated interface.
            HelloInterval (number): The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
            HelloMultiplier (number): Indicates the number of Hello Packets transmitted per second
            InstanceId (number): Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
            InterfaceIndex (number): The assigned protocol interface ID for this OSPFv3 interface.
            InterfaceType (str(pointToPoint|broadcast)): Indicates the type of network for the interface.
            InterfaceTypes (str): The type of interface to be selected for this OSPFv3 interface.
            Interfaces (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)): The interfaces that are associated with the selected interface type.
            LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
            Priority (number): Indicates the OSPF interface priority
            ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): This is the name of this emulated OSPFv3 interface on this emulated router.
            RouterOptions (number): Options related to the interface. Multiple options may be or'd together. (default = 0x13).

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Area=None, DeadInterval=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, Enabled=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, InterfaceIndex=None, InterfaceType=None, InterfaceTypes=None, Interfaces=None, LinkMetric=None, Priority=None, ProtocolInterface=None, RouterOptions=None):
        """Adds a new interface node on the server and retrieves it in this instance.

        Args:
            Area (number): The OSPFv3 area as a 32-bit number.
            DeadInterval (number): The number of seconds before declaring a silent router as being down.
            EnableBfdRegistration (bool): Enables the BFD registration.
            EnableFastHello (bool): Enables Fast Hello option for OSPF Router
            EnableIgnoreDbDescMtu (bool): If true, enables the ability for the router to ignore the database described MTU.
            Enabled (bool): Enables the use of the simulated interface.
            HelloInterval (number): The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
            HelloMultiplier (number): Indicates the number of Hello Packets transmitted per second
            InstanceId (number): Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
            InterfaceIndex (number): The assigned protocol interface ID for this OSPFv3 interface.
            InterfaceType (str(pointToPoint|broadcast)): Indicates the type of network for the interface.
            InterfaceTypes (str): The type of interface to be selected for this OSPFv3 interface.
            Interfaces (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)): The interfaces that are associated with the selected interface type.
            LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
            Priority (number): Indicates the OSPF interface priority
            ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): This is the name of this emulated OSPFv3 interface on this emulated router.
            RouterOptions (number): Options related to the interface. Multiple options may be or'd together. (default = 0x13).

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

    def find(self, Area=None, DeadInterval=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, Enabled=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, InterfaceIndex=None, InterfaceType=None, InterfaceTypes=None, Interfaces=None, LinkMetric=None, Priority=None, ProtocolInterface=None, RouterOptions=None):
        """Finds and retrieves interface data from the server.

        All named parameters support regex and can be used to selectively retrieve interface data from the server.
        By default the find method takes no parameters and will retrieve all interface data from the server.

        Args:
            Area (number): The OSPFv3 area as a 32-bit number.
            DeadInterval (number): The number of seconds before declaring a silent router as being down.
            EnableBfdRegistration (bool): Enables the BFD registration.
            EnableFastHello (bool): Enables Fast Hello option for OSPF Router
            EnableIgnoreDbDescMtu (bool): If true, enables the ability for the router to ignore the database described MTU.
            Enabled (bool): Enables the use of the simulated interface.
            HelloInterval (number): The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
            HelloMultiplier (number): Indicates the number of Hello Packets transmitted per second
            InstanceId (number): Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
            InterfaceIndex (number): The assigned protocol interface ID for this OSPFv3 interface.
            InterfaceType (str(pointToPoint|broadcast)): Indicates the type of network for the interface.
            InterfaceTypes (str): The type of interface to be selected for this OSPFv3 interface.
            Interfaces (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)): The interfaces that are associated with the selected interface type.
            LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
            Priority (number): Indicates the OSPF interface priority
            ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): This is the name of this emulated OSPFv3 interface on this emulated router.
            RouterOptions (number): Options related to the interface. Multiple options may be or'd together. (default = 0x13).

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

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Fetches interface accessor Iface list.

            Returns:
                str: NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)
