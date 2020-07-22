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
    """The EIGRP interface holds the information related to a single interface on the simulated router. Interfaces are added into the EIGRP router interface list using the EIGRP router add interface object. In addition, learned LSAs from the DUT are made available through this object.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'Bandwidth': 'bandwidth',
        'Delay': 'delay',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'Enabled': 'enabled',
        'HelloInterval': 'helloInterval',
        'HoldTime': 'holdTime',
        'InterfaceId': 'interfaceId',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'Load': 'load',
        'MaxTlvPerPacket': 'maxTlvPerPacket',
        'Mtu': 'mtu',
        'Reliability': 'reliability',
        'SplitHorizon': 'splitHorizon',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - number: The minimum amount of bandwidth available on this link, in Kbps. The valid range is 1 to 4294967295. (default = 10,000 Kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Bandwidth'])
    @Bandwidth.setter
    def Bandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Bandwidth'], value)

    @property
    def Delay(self):
        """
        Returns
        -------
        - number: The total of delays on the path to the route/network, in microseconds. The valid range is 0 to 4294967295. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Delay'])
    @Delay.setter
    def Delay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Delay'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: Indicates if a BFD session is to be created to the EIGRP peer IP address once the EIGRP session is established. This allows EIGRP to use BFD to maintain IPv4 connectivity the EIGRP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the EIGRP interface. (default = disabled)
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
        - number: The time interval between Hello packets sent over the interface, in seconds. (default = 5 seconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def HoldTime(self):
        """
        Returns
        -------
        - number: The amount of time starting from the reception of a HELLO from a neighbor until the moment when the neighbor is to be dropped if no further HELLO is received from it, in seconds. (default = 15 seconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP['HoldTime'])
    @HoldTime.setter
    def HoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HoldTime'], value)

    @property
    def InterfaceId(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The local ID associated with the interface, which is unique per router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this EIGRP interface.
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
        - str: The type of interface to be selected for this EIGRP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

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
    def Load(self):
        """
        Returns
        -------
        - number: The amount of load on the link. The valid range is 0 to 255. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Load'])
    @Load.setter
    def Load(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Load'], value)

    @property
    def MaxTlvPerPacket(self):
        """
        Returns
        -------
        - number: The maximum number of TLVs that will be packed into a single Update packet, taking MTU into consideration. The valid range is 0-255. A value of 0 means that maximum possible packing will be used, which depends on the MTU of the link. (default = 30)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxTlvPerPacket'])
    @MaxTlvPerPacket.setter
    def MaxTlvPerPacket(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxTlvPerPacket'], value)

    @property
    def Mtu(self):
        """DEPRECATED 
        Returns
        -------
        - number: The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def Reliability(self):
        """
        Returns
        -------
        - number: The reliability factor. The valid range is 0 to 255. (default =255, which means 100% reliable)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reliability'])
    @Reliability.setter
    def Reliability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Reliability'], value)

    @property
    def SplitHorizon(self):
        """
        Returns
        -------
        - bool: Split Horizon is a method for omitting routes learned from a neighbor in update messages to that same neighbor. This enables or disables poison reverse.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SplitHorizon'])
    @SplitHorizon.setter
    def SplitHorizon(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SplitHorizon'], value)

    def update(self, Bandwidth=None, Delay=None, EnableBfdRegistration=None, Enabled=None, HelloInterval=None, HoldTime=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, Load=None, MaxTlvPerPacket=None, Mtu=None, Reliability=None, SplitHorizon=None):
        """Updates interface resource on the server.

        Args
        ----
        - Bandwidth (number): The minimum amount of bandwidth available on this link, in Kbps. The valid range is 1 to 4294967295. (default = 10,000 Kbps)
        - Delay (number): The total of delays on the path to the route/network, in microseconds. The valid range is 0 to 4294967295. (default = 0)
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the EIGRP peer IP address once the EIGRP session is established. This allows EIGRP to use BFD to maintain IPv4 connectivity the EIGRP peer.
        - Enabled (bool): Enables the EIGRP interface. (default = disabled)
        - HelloInterval (number): The time interval between Hello packets sent over the interface, in seconds. (default = 5 seconds)
        - HoldTime (number): The amount of time starting from the reception of a HELLO from a neighbor until the moment when the neighbor is to be dropped if no further HELLO is received from it, in seconds. (default = 15 seconds)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The local ID associated with the interface, which is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this EIGRP interface.
        - InterfaceType (str): The type of interface to be selected for this EIGRP interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - Load (number): The amount of load on the link. The valid range is 0 to 255. (default = 0)
        - MaxTlvPerPacket (number): The maximum number of TLVs that will be packed into a single Update packet, taking MTU into consideration. The valid range is 0-255. A value of 0 means that maximum possible packing will be used, which depends on the MTU of the link. (default = 30)
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - Reliability (number): The reliability factor. The valid range is 0 to 255. (default =255, which means 100% reliable)
        - SplitHorizon (bool): Split Horizon is a method for omitting routes learned from a neighbor in update messages to that same neighbor. This enables or disables poison reverse.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Bandwidth=None, Delay=None, EnableBfdRegistration=None, Enabled=None, HelloInterval=None, HoldTime=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, Load=None, MaxTlvPerPacket=None, Mtu=None, Reliability=None, SplitHorizon=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - Bandwidth (number): The minimum amount of bandwidth available on this link, in Kbps. The valid range is 1 to 4294967295. (default = 10,000 Kbps)
        - Delay (number): The total of delays on the path to the route/network, in microseconds. The valid range is 0 to 4294967295. (default = 0)
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the EIGRP peer IP address once the EIGRP session is established. This allows EIGRP to use BFD to maintain IPv4 connectivity the EIGRP peer.
        - Enabled (bool): Enables the EIGRP interface. (default = disabled)
        - HelloInterval (number): The time interval between Hello packets sent over the interface, in seconds. (default = 5 seconds)
        - HoldTime (number): The amount of time starting from the reception of a HELLO from a neighbor until the moment when the neighbor is to be dropped if no further HELLO is received from it, in seconds. (default = 15 seconds)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The local ID associated with the interface, which is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this EIGRP interface.
        - InterfaceType (str): The type of interface to be selected for this EIGRP interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - Load (number): The amount of load on the link. The valid range is 0 to 255. (default = 0)
        - MaxTlvPerPacket (number): The maximum number of TLVs that will be packed into a single Update packet, taking MTU into consideration. The valid range is 0-255. A value of 0 means that maximum possible packing will be used, which depends on the MTU of the link. (default = 30)
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - Reliability (number): The reliability factor. The valid range is 0 to 255. (default =255, which means 100% reliable)
        - SplitHorizon (bool): Split Horizon is a method for omitting routes learned from a neighbor in update messages to that same neighbor. This enables or disables poison reverse.

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

    def find(self, Bandwidth=None, Delay=None, EnableBfdRegistration=None, Enabled=None, HelloInterval=None, HoldTime=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, Load=None, MaxTlvPerPacket=None, Mtu=None, Reliability=None, SplitHorizon=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - Bandwidth (number): The minimum amount of bandwidth available on this link, in Kbps. The valid range is 1 to 4294967295. (default = 10,000 Kbps)
        - Delay (number): The total of delays on the path to the route/network, in microseconds. The valid range is 0 to 4294967295. (default = 0)
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the EIGRP peer IP address once the EIGRP session is established. This allows EIGRP to use BFD to maintain IPv4 connectivity the EIGRP peer.
        - Enabled (bool): Enables the EIGRP interface. (default = disabled)
        - HelloInterval (number): The time interval between Hello packets sent over the interface, in seconds. (default = 5 seconds)
        - HoldTime (number): The amount of time starting from the reception of a HELLO from a neighbor until the moment when the neighbor is to be dropped if no further HELLO is received from it, in seconds. (default = 15 seconds)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The local ID associated with the interface, which is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this EIGRP interface.
        - InterfaceType (str): The type of interface to be selected for this EIGRP interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - Load (number): The amount of load on the link. The valid range is 0 to 255. (default = 0)
        - MaxTlvPerPacket (number): The maximum number of TLVs that will be packed into a single Update packet, taking MTU into consideration. The valid range is 0-255. A value of 0 means that maximum possible packing will be used, which depends on the MTU of the link. (default = 30)
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - Reliability (number): The reliability factor. The valid range is 0 to 255. (default =255, which means 100% reliable)
        - SplitHorizon (bool): Split Horizon is a method for omitting routes learned from a neighbor in update messages to that same neighbor. This enables or disables poison reverse.

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

        Gets the interface accesor Iface list.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)
