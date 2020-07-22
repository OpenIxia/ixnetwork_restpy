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


class LearnedRoute(Base):
    """Used to retrieve the list of learned routes from the request learned routes. Each enabled type of route is considered a separate list.
    The LearnedRoute class encapsulates a list of learnedRoute resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedRoute.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedRoute'
    _SDM_ATT_MAP = {
        'Destination': 'destination',
        'Fd': 'fd',
        'HopCount': 'hopCount',
        'Neighbor': 'neighbor',
        'NextHop': 'nextHop',
        'Prefix': 'prefix',
        'Rd': 'rd',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(LearnedRoute, self).__init__(parent)

    @property
    def Destination(self):
        """
        Returns
        -------
        - str: (Read-only) The destination network that was advertised in the learned route of IPv4/IPv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Destination'])

    @property
    def Fd(self):
        """
        Returns
        -------
        - number: (Read-only) The feasible distance. The sum of the Reported Distance and the Link Cost of the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Fd'])

    @property
    def HopCount(self):
        """
        Returns
        -------
        - number: (Read-only) The hop count of the route learned from the neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HopCount'])

    @property
    def Neighbor(self):
        """
        Returns
        -------
        - str: (Read-only) The neighbor from which the route was learned.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: (Read-only) The next hop on the path to the destination contained in the learned route of IPv4/Ipv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])

    @property
    def Prefix(self):
        """
        Returns
        -------
        - number: (Read-only) IP prefix length for the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Prefix'])

    @property
    def Rd(self):
        """
        Returns
        -------
        - number: (Read-only) The reported distance of the route advertised by the neighbor. It is calculated based on bandwidth, load, delay, and reliability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rd'])

    @property
    def Type(self):
        """
        Returns
        -------
        - number: (Read-only) Indicates whether it is an internal or external route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])

    def find(self, Destination=None, Fd=None, HopCount=None, Neighbor=None, NextHop=None, Prefix=None, Rd=None, Type=None):
        """Finds and retrieves learnedRoute resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedRoute resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedRoute resources from the server.

        Args
        ----
        - Destination (str): (Read-only) The destination network that was advertised in the learned route of IPv4/IPv6.
        - Fd (number): (Read-only) The feasible distance. The sum of the Reported Distance and the Link Cost of the interface.
        - HopCount (number): (Read-only) The hop count of the route learned from the neighbor.
        - Neighbor (str): (Read-only) The neighbor from which the route was learned.
        - NextHop (str): (Read-only) The next hop on the path to the destination contained in the learned route of IPv4/Ipv6.
        - Prefix (number): (Read-only) IP prefix length for the route.
        - Rd (number): (Read-only) The reported distance of the route advertised by the neighbor. It is calculated based on bandwidth, load, delay, and reliability.
        - Type (number): (Read-only) Indicates whether it is an internal or external route.

        Returns
        -------
        - self: This instance with matching learnedRoute resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedRoute data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedRoute resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
