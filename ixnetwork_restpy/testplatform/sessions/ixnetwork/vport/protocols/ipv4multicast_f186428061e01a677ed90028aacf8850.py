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


class Ipv4Multicast(Base):
    """Learned information for IPv4 Multicast routes.
    The Ipv4Multicast class encapsulates a list of ipv4Multicast resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4Multicast.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ipv4Multicast"
    _SDM_ATT_MAP = {
        "AsPath": "asPath",
        "BlockOffset": "blockOffset",
        "BlockSize": "blockSize",
        "ControlWordEnabled": "controlWordEnabled",
        "IpPrefix": "ipPrefix",
        "LabelBase": "labelBase",
        "LocalPreference": "localPreference",
        "MaxLabel": "maxLabel",
        "MultiExitDiscriminator": "multiExitDiscriminator",
        "Neighbor": "neighbor",
        "NextHop": "nextHop",
        "OriginType": "originType",
        "PrefixLength": "prefixLength",
        "RouteDistinguisher": "routeDistinguisher",
        "SeqDeliveryEnabled": "seqDeliveryEnabled",
        "SiteId": "siteId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ipv4Multicast, self).__init__(parent, list_op)

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
    def BlockOffset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The label block offset (VBO) is the value used to help define this specific label block uniquely as a subset of all of the possible labels.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BlockOffset"])

    @property
    def BlockSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The size of the label block, in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BlockSize"])

    @property
    def ControlWordEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the route label uses a control word, as part of the extended community information. (One of the control flags.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlWordEnabled"])

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
    def LabelBase(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first label to be assigned to the FEC.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LabelBase"])

    @property
    def LocalPreference(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the value of the local preference attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPreference"])

    @property
    def MaxLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The last label to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxLabel"])

    @property
    def MultiExitDiscriminator(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A metric field of the route file.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MultiExitDiscriminator"])

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
    def OriginType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: An indication of where the route entry originated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginType"])

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
        - str: The route distinguisher for the route, for use with IPv4 and IPv6 MPLS VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisher"])

    @property
    def SeqDeliveryEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if sequential delivery is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SeqDeliveryEnabled"])

    @property
    def SiteId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The site ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SiteId"])

    def add(self):
        """Adds a new ipv4Multicast resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved ipv4Multicast resources using find and the newly added ipv4Multicast resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AsPath=None,
        BlockOffset=None,
        BlockSize=None,
        ControlWordEnabled=None,
        IpPrefix=None,
        LabelBase=None,
        LocalPreference=None,
        MaxLabel=None,
        MultiExitDiscriminator=None,
        Neighbor=None,
        NextHop=None,
        OriginType=None,
        PrefixLength=None,
        RouteDistinguisher=None,
        SeqDeliveryEnabled=None,
        SiteId=None,
    ):
        # type: (str, int, int, bool, str, int, int, int, int, str, str, str, int, str, bool, int) -> Ipv4Multicast
        """Finds and retrieves ipv4Multicast resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4Multicast resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4Multicast resources from the server.

        Args
        ----
        - AsPath (str): Indicates the local IP address of the BGP router.
        - BlockOffset (number): The label block offset (VBO) is the value used to help define this specific label block uniquely as a subset of all of the possible labels.
        - BlockSize (number): The size of the label block, in bytes.
        - ControlWordEnabled (bool): If true, the route label uses a control word, as part of the extended community information. (One of the control flags.)
        - IpPrefix (str): The route IP prefix.
        - LabelBase (number): The first label to be assigned to the FEC.
        - LocalPreference (number): Indicates the value of the local preference attribute.
        - MaxLabel (number): The last label to use.
        - MultiExitDiscriminator (number): A metric field of the route file.
        - Neighbor (str): The descriptive identifier for the BGP neighbor.
        - NextHop (str): A 4-octet IP address which indicates the next hop.
        - OriginType (str): An indication of where the route entry originated.
        - PrefixLength (number): The length of the route IP prefix, in bytes.
        - RouteDistinguisher (str): The route distinguisher for the route, for use with IPv4 and IPv6 MPLS VPN address types.
        - SeqDeliveryEnabled (bool): Indicates if sequential delivery is enabled.
        - SiteId (number): The site ID.

        Returns
        -------
        - self: This instance with matching ipv4Multicast resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4Multicast data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4Multicast resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
