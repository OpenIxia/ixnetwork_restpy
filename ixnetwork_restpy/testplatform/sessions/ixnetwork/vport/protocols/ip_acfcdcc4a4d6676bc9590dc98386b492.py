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


class Ip(Base):
    """This object holds the list of statically-configured IP addresses for the port.
    The Ip class encapsulates a list of ip resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ip.find() method.
    The list can be managed by using the Ip.add() and Ip.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ip'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Enabled': 'enabled',
        'IpStart': 'ipStart',
        'IpType': 'ipType',
        'Mask': 'mask',
        'ProtocolInterface': 'protocolInterface',
        'Step': 'step',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Ip, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The total number of addresses to create for this range of IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this IP address entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IpStart(self):
        """
        Returns
        -------
        - str: The first IP address in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStart'])
    @IpStart.setter
    def IpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStart'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): The Internet Protocol (IP version).
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def Mask(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mask'])
    @Mask.setter
    def Mask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mask'], value)

    @property
    def ProtocolInterface(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): There may be multiple interfaces listed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: The increment value to be used for each additional address, to create a range of IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

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

    def update(self, Count=None, Enabled=None, IpStart=None, IpType=None, Mask=None, ProtocolInterface=None, Step=None, TrafficGroupId=None):
        """Updates ip resource on the server.

        Args
        ----
        - Count (number): The total number of addresses to create for this range of IP addresses.
        - Enabled (bool): Enables this IP address entry.
        - IpStart (str): The first IP address in the range.
        - IpType (str(ipv4 | ipv6)): The Internet Protocol (IP version).
        - Mask (number): The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): There may be multiple interfaces listed.
        - Step (number): The increment value to be used for each additional address, to create a range of IP addresses.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, Enabled=None, IpStart=None, IpType=None, Mask=None, ProtocolInterface=None, Step=None, TrafficGroupId=None):
        """Adds a new ip resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The total number of addresses to create for this range of IP addresses.
        - Enabled (bool): Enables this IP address entry.
        - IpStart (str): The first IP address in the range.
        - IpType (str(ipv4 | ipv6)): The Internet Protocol (IP version).
        - Mask (number): The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): There may be multiple interfaces listed.
        - Step (number): The increment value to be used for each additional address, to create a range of IP addresses.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with all currently retrieved ip resources using find and the newly added ip resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ip resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Enabled=None, IpStart=None, IpType=None, Mask=None, ProtocolInterface=None, Step=None, TrafficGroupId=None):
        """Finds and retrieves ip resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ip resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ip resources from the server.

        Args
        ----
        - Count (number): The total number of addresses to create for this range of IP addresses.
        - Enabled (bool): Enables this IP address entry.
        - IpStart (str): The first IP address in the range.
        - IpType (str(ipv4 | ipv6)): The Internet Protocol (IP version).
        - Mask (number): The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): There may be multiple interfaces listed.
        - Step (number): The increment value to be used for each additional address, to create a range of IP addresses.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with matching ip resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ip data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ip resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
