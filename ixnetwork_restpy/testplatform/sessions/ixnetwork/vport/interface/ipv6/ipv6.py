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


class Ipv6(Base):
    """Controls the general IPv6 interface properties.
    The Ipv6 class encapsulates a list of ipv6 resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ipv6.find() method.
    The list can be managed by using the Ipv6.add() and Ipv6.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv6'
    _SDM_ATT_MAP = {
        'Gateway': 'gateway',
        'Ip': 'ip',
        'PrefixLength': 'prefixLength',
        'TargetLinkLayerAddressOption': 'targetLinkLayerAddressOption',
        'TrafficClass': 'trafficClass',
    }

    def __init__(self, parent):
        super(Ipv6, self).__init__(parent)

    @property
    def Gateway(self):
        """
        Returns
        -------
        - str: The IPv6 address of the Gateway to the network,typically an interface on the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gateway'])
    @Gateway.setter
    def Gateway(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gateway'], value)

    @property
    def Ip(self):
        """
        Returns
        -------
        - str: The 128-bit IPv6 address assigned to this unconnected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ip'])
    @Ip.setter
    def Ip(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ip'], value)

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: A learned/allocated IPv4 address prefix length (mask) for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])
    @PrefixLength.setter
    def PrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixLength'], value)

    @property
    def TargetLinkLayerAddressOption(self):
        """
        Returns
        -------
        - bool: Tentative Source Link-Layer Address Options for IPv6 Neighbour Discovery. Upon reception of a Tentative Source Link-Layer Address Option in a Neighbour Solicitation for which the receiver has the Target Address configured, a node checks to see if there is a neighbour cache entry with conflicting link-layer address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetLinkLayerAddressOption'])
    @TargetLinkLayerAddressOption.setter
    def TargetLinkLayerAddressOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetLinkLayerAddressOption'], value)

    @property
    def TrafficClass(self):
        """
        Returns
        -------
        - str: This value ,1 byte long, configures the Traffic Class in the IPv6 header for our IPv6 Neighbour Discovery messages. The default value is 0x00 but the user can modify it to any value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficClass'])
    @TrafficClass.setter
    def TrafficClass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficClass'], value)

    def update(self, Gateway=None, Ip=None, PrefixLength=None, TargetLinkLayerAddressOption=None, TrafficClass=None):
        """Updates ipv6 resource on the server.

        Args
        ----
        - Gateway (str): The IPv6 address of the Gateway to the network,typically an interface on the DUT.
        - Ip (str): The 128-bit IPv6 address assigned to this unconnected interface.
        - PrefixLength (number): A learned/allocated IPv4 address prefix length (mask) for this interface.
        - TargetLinkLayerAddressOption (bool): Tentative Source Link-Layer Address Options for IPv6 Neighbour Discovery. Upon reception of a Tentative Source Link-Layer Address Option in a Neighbour Solicitation for which the receiver has the Target Address configured, a node checks to see if there is a neighbour cache entry with conflicting link-layer address.
        - TrafficClass (str): This value ,1 byte long, configures the Traffic Class in the IPv6 header for our IPv6 Neighbour Discovery messages. The default value is 0x00 but the user can modify it to any value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Gateway=None, Ip=None, PrefixLength=None, TargetLinkLayerAddressOption=None, TrafficClass=None):
        """Adds a new ipv6 resource on the server and adds it to the container.

        Args
        ----
        - Gateway (str): The IPv6 address of the Gateway to the network,typically an interface on the DUT.
        - Ip (str): The 128-bit IPv6 address assigned to this unconnected interface.
        - PrefixLength (number): A learned/allocated IPv4 address prefix length (mask) for this interface.
        - TargetLinkLayerAddressOption (bool): Tentative Source Link-Layer Address Options for IPv6 Neighbour Discovery. Upon reception of a Tentative Source Link-Layer Address Option in a Neighbour Solicitation for which the receiver has the Target Address configured, a node checks to see if there is a neighbour cache entry with conflicting link-layer address.
        - TrafficClass (str): This value ,1 byte long, configures the Traffic Class in the IPv6 header for our IPv6 Neighbour Discovery messages. The default value is 0x00 but the user can modify it to any value.

        Returns
        -------
        - self: This instance with all currently retrieved ipv6 resources using find and the newly added ipv6 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ipv6 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Gateway=None, Ip=None, PrefixLength=None, TargetLinkLayerAddressOption=None, TrafficClass=None):
        """Finds and retrieves ipv6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv6 resources from the server.

        Args
        ----
        - Gateway (str): The IPv6 address of the Gateway to the network,typically an interface on the DUT.
        - Ip (str): The 128-bit IPv6 address assigned to this unconnected interface.
        - PrefixLength (number): A learned/allocated IPv4 address prefix length (mask) for this interface.
        - TargetLinkLayerAddressOption (bool): Tentative Source Link-Layer Address Options for IPv6 Neighbour Discovery. Upon reception of a Tentative Source Link-Layer Address Option in a Neighbour Solicitation for which the receiver has the Target Address configured, a node checks to see if there is a neighbour cache entry with conflicting link-layer address.
        - TrafficClass (str): This value ,1 byte long, configures the Traffic Class in the IPv6 header for our IPv6 Neighbour Discovery messages. The default value is 0x00 but the user can modify it to any value.

        Returns
        -------
        - self: This instance with matching ipv6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv6 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
