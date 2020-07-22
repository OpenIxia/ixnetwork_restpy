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
    """A network interface to be included in this OSPFv3 router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'Area': 'area',
        'DeadInterval': 'deadInterval',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableFastHello': 'enableFastHello',
        'EnableIgnoreDbDescMtu': 'enableIgnoreDbDescMtu',
        'Enabled': 'enabled',
        'HelloInterval': 'helloInterval',
        'HelloMultiplier': 'helloMultiplier',
        'InstanceId': 'instanceId',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceType': 'interfaceType',
        'InterfaceTypes': 'interfaceTypes',
        'Interfaces': 'interfaces',
        'LinkMetric': 'linkMetric',
        'Priority': 'priority',
        'ProtocolInterface': 'protocolInterface',
        'RouterOptions': 'routerOptions',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def Area(self):
        """
        Returns
        -------
        - number: The OSPFv3 area as a 32-bit number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Area'])
    @Area.setter
    def Area(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Area'], value)

    @property
    def DeadInterval(self):
        """
        Returns
        -------
        - number: The number of seconds before declaring a silent router as being down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeadInterval'])
    @DeadInterval.setter
    def DeadInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeadInterval'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: Enables the BFD registration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def EnableFastHello(self):
        """
        Returns
        -------
        - bool: Enables Fast Hello option for OSPF Router
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastHello'])
    @EnableFastHello.setter
    def EnableFastHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastHello'], value)

    @property
    def EnableIgnoreDbDescMtu(self):
        """
        Returns
        -------
        - bool: If true, enables the ability for the router to ignore the database described MTU.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIgnoreDbDescMtu'])
    @EnableIgnoreDbDescMtu.setter
    def EnableIgnoreDbDescMtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIgnoreDbDescMtu'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the simulated interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def HelloMultiplier(self):
        """
        Returns
        -------
        - number: Indicates the number of Hello Packets transmitted per second
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloMultiplier'])
    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloMultiplier'], value)

    @property
    def InstanceId(self):
        """
        Returns
        -------
        - number: Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstanceId'])
    @InstanceId.setter
    def InstanceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstanceId'], value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this OSPFv3 interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIndex'])
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIndex'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast): Indicates the type of network for the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def InterfaceTypes(self):
        """
        Returns
        -------
        - str: The type of interface to be selected for this OSPFv3 interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceTypes'])
    @InterfaceTypes.setter
    def InterfaceTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceTypes'], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: The metric for the link connecting the grid with the emulated OSPFv3 router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMetric'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: Indicates the OSPF interface priority
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): This is the name of this emulated OSPFv3 interface on this emulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def RouterOptions(self):
        """
        Returns
        -------
        - number: Options related to the interface. Multiple options may be or'd together. (default = 0x13).
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterOptions'])
    @RouterOptions.setter
    def RouterOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterOptions'], value)

    def update(self, Area=None, DeadInterval=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, Enabled=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, InterfaceIndex=None, InterfaceType=None, InterfaceTypes=None, Interfaces=None, LinkMetric=None, Priority=None, ProtocolInterface=None, RouterOptions=None):
        """Updates interface resource on the server.

        Args
        ----
        - Area (number): The OSPFv3 area as a 32-bit number.
        - DeadInterval (number): The number of seconds before declaring a silent router as being down.
        - EnableBfdRegistration (bool): Enables the BFD registration.
        - EnableFastHello (bool): Enables Fast Hello option for OSPF Router
        - EnableIgnoreDbDescMtu (bool): If true, enables the ability for the router to ignore the database described MTU.
        - Enabled (bool): Enables the use of the simulated interface.
        - HelloInterval (number): The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
        - HelloMultiplier (number): Indicates the number of Hello Packets transmitted per second
        - InstanceId (number): Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
        - InterfaceIndex (number): The assigned protocol interface ID for this OSPFv3 interface.
        - InterfaceType (str(pointToPoint | broadcast)): Indicates the type of network for the interface.
        - InterfaceTypes (str): The type of interface to be selected for this OSPFv3 interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
        - Priority (number): Indicates the OSPF interface priority
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This is the name of this emulated OSPFv3 interface on this emulated router.
        - RouterOptions (number): Options related to the interface. Multiple options may be or'd together. (default = 0x13).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Area=None, DeadInterval=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, Enabled=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, InterfaceIndex=None, InterfaceType=None, InterfaceTypes=None, Interfaces=None, LinkMetric=None, Priority=None, ProtocolInterface=None, RouterOptions=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - Area (number): The OSPFv3 area as a 32-bit number.
        - DeadInterval (number): The number of seconds before declaring a silent router as being down.
        - EnableBfdRegistration (bool): Enables the BFD registration.
        - EnableFastHello (bool): Enables Fast Hello option for OSPF Router
        - EnableIgnoreDbDescMtu (bool): If true, enables the ability for the router to ignore the database described MTU.
        - Enabled (bool): Enables the use of the simulated interface.
        - HelloInterval (number): The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
        - HelloMultiplier (number): Indicates the number of Hello Packets transmitted per second
        - InstanceId (number): Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
        - InterfaceIndex (number): The assigned protocol interface ID for this OSPFv3 interface.
        - InterfaceType (str(pointToPoint | broadcast)): Indicates the type of network for the interface.
        - InterfaceTypes (str): The type of interface to be selected for this OSPFv3 interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
        - Priority (number): Indicates the OSPF interface priority
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This is the name of this emulated OSPFv3 interface on this emulated router.
        - RouterOptions (number): Options related to the interface. Multiple options may be or'd together. (default = 0x13).

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

    def find(self, Area=None, DeadInterval=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, Enabled=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, InterfaceIndex=None, InterfaceType=None, InterfaceTypes=None, Interfaces=None, LinkMetric=None, Priority=None, ProtocolInterface=None, RouterOptions=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - Area (number): The OSPFv3 area as a 32-bit number.
        - DeadInterval (number): The number of seconds before declaring a silent router as being down.
        - EnableBfdRegistration (bool): Enables the BFD registration.
        - EnableFastHello (bool): Enables Fast Hello option for OSPF Router
        - EnableIgnoreDbDescMtu (bool): If true, enables the ability for the router to ignore the database described MTU.
        - Enabled (bool): Enables the use of the simulated interface.
        - HelloInterval (number): The number of seconds between Hello packets sent by a router. The Ixia state machine sends Hello packets at this interval for this interface.
        - HelloMultiplier (number): Indicates the number of Hello Packets transmitted per second
        - InstanceId (number): Has local link significance only. It allows multiple instances of the OSPFv3 protocol to be run simultaneously over the same link.
        - InterfaceIndex (number): The assigned protocol interface ID for this OSPFv3 interface.
        - InterfaceType (str(pointToPoint | broadcast)): Indicates the type of network for the interface.
        - InterfaceTypes (str): The type of interface to be selected for this OSPFv3 interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
        - Priority (number): Indicates the OSPF interface priority
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This is the name of this emulated OSPFv3 interface on this emulated router.
        - RouterOptions (number): Options related to the interface. Multiple options may be or'd together. (default = 0x13).

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

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Fetches interface accessor Iface list.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)
