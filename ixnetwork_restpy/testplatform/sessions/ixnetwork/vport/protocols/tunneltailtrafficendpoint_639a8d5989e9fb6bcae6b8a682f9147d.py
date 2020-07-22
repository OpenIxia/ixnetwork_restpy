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


class TunnelTailTrafficEndPoint(Base):
    """The tunnelTailTrafficEndpoint configures the IP addresses to be used in the Destination IP field in traffic to be sent over the LSPs terminating on this Tail Range.
    The TunnelTailTrafficEndPoint class encapsulates a list of tunnelTailTrafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the TunnelTailTrafficEndPoint.find() method.
    The list can be managed by using the TunnelTailTrafficEndPoint.add() and TunnelTailTrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'tunnelTailTrafficEndPoint'
    _SDM_ATT_MAP = {
        'EndPointType': 'endPointType',
        'IpCount': 'ipCount',
        'IpStart': 'ipStart',
    }

    def __init__(self, parent):
        super(TunnelTailTrafficEndPoint, self).__init__(parent)

    @property
    def EndPointType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6 | 17 | 18): Indicates the end point type. One of IPv4 or IPv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndPointType'])
    @EndPointType.setter
    def EndPointType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EndPointType'], value)

    @property
    def IpCount(self):
        """
        Returns
        -------
        - number: This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
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
        - str: The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStart'])
    @IpStart.setter
    def IpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStart'], value)

    def update(self, EndPointType=None, IpCount=None, IpStart=None):
        """Updates tunnelTailTrafficEndPoint resource on the server.

        Args
        ----
        - EndPointType (str(ipv4 | ipv6 | 17 | 18)): Indicates the end point type. One of IPv4 or IPv6.
        - IpCount (number): This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
        - IpStart (str): The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EndPointType=None, IpCount=None, IpStart=None):
        """Adds a new tunnelTailTrafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - EndPointType (str(ipv4 | ipv6 | 17 | 18)): Indicates the end point type. One of IPv4 or IPv6.
        - IpCount (number): This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
        - IpStart (str): The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

        Returns
        -------
        - self: This instance with all currently retrieved tunnelTailTrafficEndPoint resources using find and the newly added tunnelTailTrafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained tunnelTailTrafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EndPointType=None, IpCount=None, IpStart=None):
        """Finds and retrieves tunnelTailTrafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tunnelTailTrafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tunnelTailTrafficEndPoint resources from the server.

        Args
        ----
        - EndPointType (str(ipv4 | ipv6 | 17 | 18)): Indicates the end point type. One of IPv4 or IPv6.
        - IpCount (number): This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
        - IpStart (str): The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

        Returns
        -------
        - self: This instance with matching tunnelTailTrafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tunnelTailTrafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tunnelTailTrafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
