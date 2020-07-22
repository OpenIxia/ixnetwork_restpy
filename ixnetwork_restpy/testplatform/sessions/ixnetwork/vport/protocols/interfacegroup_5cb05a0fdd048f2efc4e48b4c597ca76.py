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


class InterfaceGroup(Base):
    """This object holds a list of groups of Protocol Interfaces for the port.
    The InterfaceGroup class encapsulates a list of interfaceGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the InterfaceGroup.find() method.
    The list can be managed by using the InterfaceGroup.add() and InterfaceGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interfaceGroup'
    _SDM_ATT_MAP = {
        'AtmEncapsulation': 'atmEncapsulation',
        'Description': 'description',
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'Ip': 'ip',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(InterfaceGroup, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_faaa2d08d26f7832da652eac34e9b38d.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_faaa2d08d26f7832da652eac34e9b38d import Interface
        return Interface(self)

    @property
    def AtmEncapsulation(self):
        """
        Returns
        -------
        - str(vcMuxIpv4Routed | vcMuxIpv6Routed | vcMuxBridgedEth802p3WithFcs | vcMuxBridgedEth802p3WithOutFcs | llcRoutedAal5Snap | llcBridgedEthernetWithFcs | llcBridgedEthernetWithoutFcs): The type of ATM encapsulation used for the Protocol Interfaces in this Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AtmEncapsulation'])
    @AtmEncapsulation.setter
    def AtmEncapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AtmEncapsulation'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A brief description of the Interface Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - bool: Enables the use of VLANs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVlan'])
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVlan'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this Interface Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Ip(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): The IP version being used for the Protocol Interfaces in this Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ip'])
    @Ip.setter
    def Ip(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ip'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, AtmEncapsulation=None, Description=None, EnableVlan=None, Enabled=None, Ip=None, TrafficGroupId=None):
        """Updates interfaceGroup resource on the server.

        Args
        ----
        - AtmEncapsulation (str(vcMuxIpv4Routed | vcMuxIpv6Routed | vcMuxBridgedEth802p3WithFcs | vcMuxBridgedEth802p3WithOutFcs | llcRoutedAal5Snap | llcBridgedEthernetWithFcs | llcBridgedEthernetWithoutFcs)): The type of ATM encapsulation used for the Protocol Interfaces in this Group.
        - Description (str): A brief description of the Interface Group.
        - EnableVlan (bool): Enables the use of VLANs.
        - Enabled (bool): Enables this Interface Group.
        - Ip (str(ipv4 | ipv6)): The IP version being used for the Protocol Interfaces in this Group.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AtmEncapsulation=None, Description=None, EnableVlan=None, Enabled=None, Ip=None, TrafficGroupId=None):
        """Adds a new interfaceGroup resource on the server and adds it to the container.

        Args
        ----
        - AtmEncapsulation (str(vcMuxIpv4Routed | vcMuxIpv6Routed | vcMuxBridgedEth802p3WithFcs | vcMuxBridgedEth802p3WithOutFcs | llcRoutedAal5Snap | llcBridgedEthernetWithFcs | llcBridgedEthernetWithoutFcs)): The type of ATM encapsulation used for the Protocol Interfaces in this Group.
        - Description (str): A brief description of the Interface Group.
        - EnableVlan (bool): Enables the use of VLANs.
        - Enabled (bool): Enables this Interface Group.
        - Ip (str(ipv4 | ipv6)): The IP version being used for the Protocol Interfaces in this Group.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with all currently retrieved interfaceGroup resources using find and the newly added interfaceGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interfaceGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AtmEncapsulation=None, Description=None, EnableVlan=None, Enabled=None, Ip=None, TrafficGroupId=None):
        """Finds and retrieves interfaceGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interfaceGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interfaceGroup resources from the server.

        Args
        ----
        - AtmEncapsulation (str(vcMuxIpv4Routed | vcMuxIpv6Routed | vcMuxBridgedEth802p3WithFcs | vcMuxBridgedEth802p3WithOutFcs | llcRoutedAal5Snap | llcBridgedEthernetWithFcs | llcBridgedEthernetWithoutFcs)): The type of ATM encapsulation used for the Protocol Interfaces in this Group.
        - Description (str): A brief description of the Interface Group.
        - EnableVlan (bool): Enables the use of VLANs.
        - Enabled (bool): Enables this Interface Group.
        - Ip (str(ipv4 | ipv6)): The IP version being used for the Protocol Interfaces in this Group.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with matching interfaceGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interfaceGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interfaceGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
