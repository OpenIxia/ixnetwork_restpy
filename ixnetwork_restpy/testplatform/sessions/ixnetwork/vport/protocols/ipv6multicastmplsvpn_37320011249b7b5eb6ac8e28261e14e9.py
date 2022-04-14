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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class IpV6MulticastMplsVpn(Base):
    """This object allows to configure the IPv6 Multicast MplsVpn.
    The IpV6MulticastMplsVpn class encapsulates a list of ipV6MulticastMplsVpn resources that are managed by the system.
    A list of resources can be retrieved from the server using the IpV6MulticastMplsVpn.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ipV6MulticastMplsVpn"
    _SDM_ATT_MAP = {
        "AsPath": "asPath",
        "IpPrefix": "ipPrefix",
        "Label": "label",
        "Neighbor": "neighbor",
        "NextHop": "nextHop",
        "PrefixLength": "prefixLength",
        "RouteDistinguisher": "routeDistinguisher",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IpV6MulticastMplsVpn, self).__init__(parent, list_op)

    @property
    def AsPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the local IP address of the BGP router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsPath"])

    @property
    def IpPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The route IP prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpPrefix"])

    @property
    def Label(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Label"])

    @property
    def Neighbor(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The descriptive identifier for the BGP neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Neighbor"])

    @property
    def NextHop(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A 4-octet IP address which indicates the next hop.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHop"])

    @property
    def PrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The length of the route IP prefix, in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrefixLength"])

    @property
    def RouteDistinguisher(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The route distinguisher for the route, for use with IPv6 MPLS VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisher"])

    def add(self):
        """Adds a new ipV6MulticastMplsVpn resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved ipV6MulticastMplsVpn resources using find and the newly added ipV6MulticastMplsVpn resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AsPath=None,
        IpPrefix=None,
        Label=None,
        Neighbor=None,
        NextHop=None,
        PrefixLength=None,
        RouteDistinguisher=None,
    ):
        # type: (str, str, int, str, str, int, str) -> IpV6MulticastMplsVpn
        """Finds and retrieves ipV6MulticastMplsVpn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipV6MulticastMplsVpn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipV6MulticastMplsVpn resources from the server.

        Args
        ----
        - AsPath (str): Indicates the local IP address of the BGP router.
        - IpPrefix (str): The route IP prefix.
        - Label (number): NOT DEFINED
        - Neighbor (str): The descriptive identifier for the BGP neighbor.
        - NextHop (str): A 4-octet IP address which indicates the next hop.
        - PrefixLength (number): The length of the route IP prefix, in bytes.
        - RouteDistinguisher (str): The route distinguisher for the route, for use with IPv6 MPLS VPN address types.

        Returns
        -------
        - self: This instance with matching ipV6MulticastMplsVpn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipV6MulticastMplsVpn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipV6MulticastMplsVpn resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
