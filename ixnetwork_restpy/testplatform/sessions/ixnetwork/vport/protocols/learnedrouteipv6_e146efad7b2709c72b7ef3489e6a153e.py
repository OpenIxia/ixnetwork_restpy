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


class LearnedRouteIpv6(Base):
    """NOT DEFINED
    The LearnedRouteIpv6 class encapsulates a list of learnedRouteIpv6 resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedRouteIpv6.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "learnedRouteIpv6"
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
        super(LearnedRouteIpv6, self).__init__(parent, list_op)

    @property
    def AsPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsPath"])

    @property
    def BlockOffset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BlockOffset"])

    @property
    def BlockSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BlockSize"])

    @property
    def ControlWordEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlWordEnabled"])

    @property
    def IpPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpPrefix"])

    @property
    def LabelBase(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LabelBase"])

    @property
    def LocalPreference(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPreference"])

    @property
    def MaxLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxLabel"])

    @property
    def MultiExitDiscriminator(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MultiExitDiscriminator"])

    @property
    def Neighbor(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Neighbor"])

    @property
    def NextHop(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHop"])

    @property
    def OriginType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginType"])

    @property
    def PrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrefixLength"])

    @property
    def RouteDistinguisher(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisher"])

    @property
    def SeqDeliveryEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SeqDeliveryEnabled"])

    @property
    def SiteId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SiteId"])

    def add(self):
        """Adds a new learnedRouteIpv6 resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved learnedRouteIpv6 resources using find and the newly added learnedRouteIpv6 resources available through an iterator or index

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
        # type: (str, int, int, bool, str, int, int, int, int, str, str, str, int, str, bool, int) -> LearnedRouteIpv6
        """Finds and retrieves learnedRouteIpv6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedRouteIpv6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedRouteIpv6 resources from the server.

        Args
        ----
        - AsPath (str): NOT DEFINED
        - BlockOffset (number): NOT DEFINED
        - BlockSize (number): NOT DEFINED
        - ControlWordEnabled (bool): NOT DEFINED
        - IpPrefix (str): NOT DEFINED
        - LabelBase (number): NOT DEFINED
        - LocalPreference (number): NOT DEFINED
        - MaxLabel (number): NOT DEFINED
        - MultiExitDiscriminator (number): NOT DEFINED
        - Neighbor (str): NOT DEFINED
        - NextHop (str): NOT DEFINED
        - OriginType (str): NOT DEFINED
        - PrefixLength (number): NOT DEFINED
        - RouteDistinguisher (str): NOT DEFINED
        - SeqDeliveryEnabled (bool): NOT DEFINED
        - SiteId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching learnedRouteIpv6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedRouteIpv6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedRouteIpv6 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
