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


class TunnelHeadTrafficEndPoint(Base):
    """The tunnelHeadTrafficEndPoint helps to configure the IP addresses to be used in the Source IP field in traffic to be sent over the LSPs originating from this Head Range.
    The TunnelHeadTrafficEndPoint class encapsulates a list of tunnelHeadTrafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the TunnelHeadTrafficEndPoint.find() method.
    The list can be managed by using the TunnelHeadTrafficEndPoint.add() and TunnelHeadTrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'tunnelHeadTrafficEndPoint'
    _SDM_ATT_MAP = {
        'EndPointType': 'endPointType',
        'InsertExplicitTrafficItem': 'insertExplicitTrafficItem',
        'InsertIpv6ExplicitNull': 'insertIpv6ExplicitNull',
        'IpCount': 'ipCount',
        'IpStart': 'ipStart',
    }

    def __init__(self, parent):
        super(TunnelHeadTrafficEndPoint, self).__init__(parent)

    @property
    def EndPointType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6 | 17 | 18): IPv4/IPv6 address. It has the same values as of IP Type for traffic item in parent Tail Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndPointType'])
    @EndPointType.setter
    def EndPointType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EndPointType'], value)

    @property
    def InsertExplicitTrafficItem(self):
        """DEPRECATED 
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InsertExplicitTrafficItem'])
    @InsertExplicitTrafficItem.setter
    def InsertExplicitTrafficItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InsertExplicitTrafficItem'], value)

    @property
    def InsertIpv6ExplicitNull(self):
        """
        Returns
        -------
        - bool: This causes an IPv6 Explicit NULL to be inserted as the innermost label in addition to learned label when trying to generate IPv6 traffic over the IPv4 LSP. The purpose of this is to route the traffic to the IPv6 Protocol Stack at the egress for routing towards the IPv6 destination.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InsertIpv6ExplicitNull'])
    @InsertIpv6ExplicitNull.setter
    def InsertIpv6ExplicitNull(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InsertIpv6ExplicitNull'], value)

    @property
    def IpCount(self):
        """
        Returns
        -------
        - number: Allows value greater than or equal to Tunnel Head IP Count (1 by default). This can be used to simulate traffic from multiple source endpoints to be sent over the LSPs originated from the Head Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpCount'])
    @IpCount.setter
    def IpCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpCount'], value)

    @property
    def IpStart(self):
        """
        Returns
        -------
        - str: The Source IP address, one of IPv4 or IPv6, to be used for traffic to be sent over LSPs from the Head End Point.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStart'])
    @IpStart.setter
    def IpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStart'], value)

    def update(self, EndPointType=None, InsertExplicitTrafficItem=None, InsertIpv6ExplicitNull=None, IpCount=None, IpStart=None):
        """Updates tunnelHeadTrafficEndPoint resource on the server.

        Args
        ----
        - EndPointType (str(ipv4 | ipv6 | 17 | 18)): IPv4/IPv6 address. It has the same values as of IP Type for traffic item in parent Tail Range.
        - InsertExplicitTrafficItem (bool): NOT DEFINED
        - InsertIpv6ExplicitNull (bool): This causes an IPv6 Explicit NULL to be inserted as the innermost label in addition to learned label when trying to generate IPv6 traffic over the IPv4 LSP. The purpose of this is to route the traffic to the IPv6 Protocol Stack at the egress for routing towards the IPv6 destination.
        - IpCount (number): Allows value greater than or equal to Tunnel Head IP Count (1 by default). This can be used to simulate traffic from multiple source endpoints to be sent over the LSPs originated from the Head Range.
        - IpStart (str): The Source IP address, one of IPv4 or IPv6, to be used for traffic to be sent over LSPs from the Head End Point.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EndPointType=None, InsertExplicitTrafficItem=None, InsertIpv6ExplicitNull=None, IpCount=None, IpStart=None):
        """Adds a new tunnelHeadTrafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - EndPointType (str(ipv4 | ipv6 | 17 | 18)): IPv4/IPv6 address. It has the same values as of IP Type for traffic item in parent Tail Range.
        - InsertExplicitTrafficItem (bool): NOT DEFINED
        - InsertIpv6ExplicitNull (bool): This causes an IPv6 Explicit NULL to be inserted as the innermost label in addition to learned label when trying to generate IPv6 traffic over the IPv4 LSP. The purpose of this is to route the traffic to the IPv6 Protocol Stack at the egress for routing towards the IPv6 destination.
        - IpCount (number): Allows value greater than or equal to Tunnel Head IP Count (1 by default). This can be used to simulate traffic from multiple source endpoints to be sent over the LSPs originated from the Head Range.
        - IpStart (str): The Source IP address, one of IPv4 or IPv6, to be used for traffic to be sent over LSPs from the Head End Point.

        Returns
        -------
        - self: This instance with all currently retrieved tunnelHeadTrafficEndPoint resources using find and the newly added tunnelHeadTrafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained tunnelHeadTrafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EndPointType=None, InsertExplicitTrafficItem=None, InsertIpv6ExplicitNull=None, IpCount=None, IpStart=None):
        """Finds and retrieves tunnelHeadTrafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tunnelHeadTrafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tunnelHeadTrafficEndPoint resources from the server.

        Args
        ----
        - EndPointType (str(ipv4 | ipv6 | 17 | 18)): IPv4/IPv6 address. It has the same values as of IP Type for traffic item in parent Tail Range.
        - InsertExplicitTrafficItem (bool): NOT DEFINED
        - InsertIpv6ExplicitNull (bool): This causes an IPv6 Explicit NULL to be inserted as the innermost label in addition to learned label when trying to generate IPv6 traffic over the IPv4 LSP. The purpose of this is to route the traffic to the IPv6 Protocol Stack at the egress for routing towards the IPv6 destination.
        - IpCount (number): Allows value greater than or equal to Tunnel Head IP Count (1 by default). This can be used to simulate traffic from multiple source endpoints to be sent over the LSPs originated from the Head Range.
        - IpStart (str): The Source IP address, one of IPv4 or IPv6, to be used for traffic to be sent over LSPs from the Head End Point.

        Returns
        -------
        - self: This instance with matching tunnelHeadTrafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tunnelHeadTrafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tunnelHeadTrafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
