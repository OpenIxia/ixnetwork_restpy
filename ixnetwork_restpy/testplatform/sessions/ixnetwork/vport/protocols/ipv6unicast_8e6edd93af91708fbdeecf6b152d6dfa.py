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


class Ipv6Unicast(Base):
    """Learned information for IPv6 Unicast routes.
    The Ipv6Unicast class encapsulates a list of ipv6Unicast resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv6Unicast.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv6Unicast'
    _SDM_ATT_MAP = {
        'AsPath': 'asPath',
        'Community': 'community',
        'IpPrefix': 'ipPrefix',
        'LocalPreference': 'localPreference',
        'MultiExitDiscriminator': 'multiExitDiscriminator',
        'Neighbor': 'neighbor',
        'NextHop': 'nextHop',
        'OriginType': 'originType',
        'PrefixLength': 'prefixLength',
    }

    def __init__(self, parent):
        super(Ipv6Unicast, self).__init__(parent)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - str: Indicates the local IP address of the BGP router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPath'])

    @property
    def Community(self):
        """
        Returns
        -------
        - str: The BGP Community attribute to be added to the BGP entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Community'])

    @property
    def IpPrefix(self):
        """
        Returns
        -------
        - str: The route IP prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpPrefix'])

    @property
    def LocalPreference(self):
        """
        Returns
        -------
        - number: Indicates the value of the local preference attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPreference'])

    @property
    def MultiExitDiscriminator(self):
        """
        Returns
        -------
        - number: A metric field of the route file.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MultiExitDiscriminator'])

    @property
    def Neighbor(self):
        """
        Returns
        -------
        - str: The descriptive identifier for the BGP neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: A 4-octet IP address which indicates the next hop.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])

    @property
    def OriginType(self):
        """
        Returns
        -------
        - str: An indication of where the route entry originated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginType'])

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: The length of the route IP prefix, in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])

    def find(self, AsPath=None, Community=None, IpPrefix=None, LocalPreference=None, MultiExitDiscriminator=None, Neighbor=None, NextHop=None, OriginType=None, PrefixLength=None):
        """Finds and retrieves ipv6Unicast resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv6Unicast resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv6Unicast resources from the server.

        Args
        ----
        - AsPath (str): Indicates the local IP address of the BGP router.
        - Community (str): The BGP Community attribute to be added to the BGP entry.
        - IpPrefix (str): The route IP prefix.
        - LocalPreference (number): Indicates the value of the local preference attribute.
        - MultiExitDiscriminator (number): A metric field of the route file.
        - Neighbor (str): The descriptive identifier for the BGP neighbor.
        - NextHop (str): A 4-octet IP address which indicates the next hop.
        - OriginType (str): An indication of where the route entry originated.
        - PrefixLength (number): The length of the route IP prefix, in bytes.

        Returns
        -------
        - self: This instance with matching ipv6Unicast resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv6Unicast data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv6Unicast resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
