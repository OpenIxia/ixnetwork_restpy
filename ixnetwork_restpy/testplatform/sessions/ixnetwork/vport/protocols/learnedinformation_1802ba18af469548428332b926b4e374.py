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


class LearnedInformation(Base):
    """Holds lists of all of the learned route information. Each of the enabled types of routes is logically considered as a separate list.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnedInformation"
    _SDM_ATT_MAP = {
        "EvpnEthernetAdRouteCount": "evpnEthernetAdRouteCount",
        "EvpnEthernetSegmentRouteCount": "evpnEthernetSegmentRouteCount",
        "EvpnMacRouteCount": "evpnMacRouteCount",
        "EvpnMulticastRouteCount": "evpnMulticastRouteCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedInformation, self).__init__(parent, list_op)

    @property
    def AdVpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_ccea4561ace0189882bb546c9cfa5f9e.AdVpls): An instance of the AdVpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_ccea4561ace0189882bb546c9cfa5f9e import (
            AdVpls,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AdVpls", None) is not None:
                return self._properties.get("AdVpls")
        return AdVpls(self)

    @property
    def EvpnEthernetAd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_382be6f7368ead1bc83dbc2883056278.EvpnEthernetAd): An instance of the EvpnEthernetAd class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_382be6f7368ead1bc83dbc2883056278 import (
            EvpnEthernetAd,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnEthernetAd", None) is not None:
                return self._properties.get("EvpnEthernetAd")
        return EvpnEthernetAd(self)

    @property
    def EvpnEthernetSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_677e4911564b087e7599980ffdd2625c.EvpnEthernetSegment): An instance of the EvpnEthernetSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_677e4911564b087e7599980ffdd2625c import (
            EvpnEthernetSegment,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnEthernetSegment", None) is not None:
                return self._properties.get("EvpnEthernetSegment")
        return EvpnEthernetSegment(self)

    @property
    def EvpnMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_227e9aab660a89fa37cb22fcbbf5fd8e.EvpnMac): An instance of the EvpnMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_227e9aab660a89fa37cb22fcbbf5fd8e import (
            EvpnMac,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnMac", None) is not None:
                return self._properties.get("EvpnMac")
        return EvpnMac(self)

    @property
    def EvpnMulticast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_dd530fe640f92b02fcec585230a1eb38.EvpnMulticast): An instance of the EvpnMulticast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_dd530fe640f92b02fcec585230a1eb38 import (
            EvpnMulticast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnMulticast", None) is not None:
                return self._properties.get("EvpnMulticast")
        return EvpnMulticast(self)

    @property
    def IpV4MulticastMplsVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_0e7ecf09417f1445669838c0c124e95d.IpV4MulticastMplsVpn): An instance of the IpV4MulticastMplsVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_0e7ecf09417f1445669838c0c124e95d import (
            IpV4MulticastMplsVpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpV4MulticastMplsVpn", None) is not None:
                return self._properties.get("IpV4MulticastMplsVpn")
        return IpV4MulticastMplsVpn(self)

    @property
    def IpV6MulticastMplsVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_37320011249b7b5eb6ac8e28261e14e9.IpV6MulticastMplsVpn): An instance of the IpV6MulticastMplsVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_37320011249b7b5eb6ac8e28261e14e9 import (
            IpV6MulticastMplsVpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpV6MulticastMplsVpn", None) is not None:
                return self._properties.get("IpV6MulticastMplsVpn")
        return IpV6MulticastMplsVpn(self)

    @property
    def Ipv4Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_f186428061e01a677ed90028aacf8850.Ipv4Multicast): An instance of the Ipv4Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_f186428061e01a677ed90028aacf8850 import (
            Ipv4Multicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4Multicast", None) is not None:
                return self._properties.get("Ipv4Multicast")
        return Ipv4Multicast(self)

    @property
    def Ipv4MulticastVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_2838bda5d3294192ebb739b43ae2920d.Ipv4MulticastVpn): An instance of the Ipv4MulticastVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_2838bda5d3294192ebb739b43ae2920d import (
            Ipv4MulticastVpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4MulticastVpn", None) is not None:
                return self._properties.get("Ipv4MulticastVpn")
        return Ipv4MulticastVpn(self)

    @property
    def Ipv4Unicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_84eb965edee4a3a92f8039684a927d29.Ipv4Unicast): An instance of the Ipv4Unicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_84eb965edee4a3a92f8039684a927d29 import (
            Ipv4Unicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4Unicast", None) is not None:
                return self._properties.get("Ipv4Unicast")
        return Ipv4Unicast(self)

    @property
    def Ipv4mpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_9d02231b6863fbed9e16d0466d0d5ad2.Ipv4mpls): An instance of the Ipv4mpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_9d02231b6863fbed9e16d0466d0d5ad2 import (
            Ipv4mpls,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4mpls", None) is not None:
                return self._properties.get("Ipv4mpls")
        return Ipv4mpls(self)

    @property
    def Ipv4vpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_deef183a882ebd6379f7ba509e5fe8f8.Ipv4vpn): An instance of the Ipv4vpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_deef183a882ebd6379f7ba509e5fe8f8 import (
            Ipv4vpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4vpn", None) is not None:
                return self._properties.get("Ipv4vpn")
        return Ipv4vpn(self)

    @property
    def Ipv6Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_07d4602699a2d5dce022feb7ce147d82.Ipv6Multicast): An instance of the Ipv6Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_07d4602699a2d5dce022feb7ce147d82 import (
            Ipv6Multicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Multicast", None) is not None:
                return self._properties.get("Ipv6Multicast")
        return Ipv6Multicast(self)

    @property
    def Ipv6MulticastVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_70c6fcfd3abd5d2f628ad42b275cbff8.Ipv6MulticastVpn): An instance of the Ipv6MulticastVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_70c6fcfd3abd5d2f628ad42b275cbff8 import (
            Ipv6MulticastVpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6MulticastVpn", None) is not None:
                return self._properties.get("Ipv6MulticastVpn")
        return Ipv6MulticastVpn(self)

    @property
    def Ipv6Unicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_570794df9cdc49c5fe62856ad97cafb6.Ipv6Unicast): An instance of the Ipv6Unicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_570794df9cdc49c5fe62856ad97cafb6 import (
            Ipv6Unicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Unicast", None) is not None:
                return self._properties.get("Ipv6Unicast")
        return Ipv6Unicast(self)

    @property
    def Ipv6mpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_a344b5c14be52b80b9d7e6c64c6cdf76.Ipv6mpls): An instance of the Ipv6mpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_a344b5c14be52b80b9d7e6c64c6cdf76 import (
            Ipv6mpls,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6mpls", None) is not None:
                return self._properties.get("Ipv6mpls")
        return Ipv6mpls(self)

    @property
    def Ipv6vpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_5e78c44f75f6a204a00bb97a7a781443.Ipv6vpn): An instance of the Ipv6vpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_5e78c44f75f6a204a00bb97a7a781443 import (
            Ipv6vpn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6vpn", None) is not None:
                return self._properties.get("Ipv6vpn")
        return Ipv6vpn(self)

    @property
    def Vpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_e484acf8ddac1ab77d2c368869618883.Vpls): An instance of the Vpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_e484acf8ddac1ab77d2c368869618883 import (
            Vpls,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vpls", None) is not None:
                return self._properties.get("Vpls")
        return Vpls(self)

    @property
    def EvpnEthernetAdRouteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) Number of AD-Routes learned and shown in A-D route learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EvpnEthernetAdRouteCount"])

    @property
    def EvpnEthernetSegmentRouteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) Number of Ethernet Segment routes learned and shown in ethernet segment route learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EvpnEthernetSegmentRouteCount"])

    @property
    def EvpnMacRouteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) Number of Macs learned and shown in mac learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EvpnMacRouteCount"])

    @property
    def EvpnMulticastRouteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) Number of RDs learned and shown in evpn multicast learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EvpnMulticastRouteCount"])

    def find(
        self,
        EvpnEthernetAdRouteCount=None,
        EvpnEthernetSegmentRouteCount=None,
        EvpnMacRouteCount=None,
        EvpnMulticastRouteCount=None,
    ):
        # type: (int, int, int, int) -> LearnedInformation
        """Finds and retrieves learnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInformation resources from the server.

        Args
        ----
        - EvpnEthernetAdRouteCount (number): (read only) Number of AD-Routes learned and shown in A-D route learned info table.
        - EvpnEthernetSegmentRouteCount (number): (read only) Number of Ethernet Segment routes learned and shown in ethernet segment route learned info table.
        - EvpnMacRouteCount (number): (read only) Number of Macs learned and shown in mac learned info table.
        - EvpnMulticastRouteCount (number): (read only) Number of RDs learned and shown in evpn multicast learned info table.

        Returns
        -------
        - self: This instance with matching learnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
