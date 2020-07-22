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


class LearnedInformation(Base):
    """Holds lists of all of the learned route information. Each of the enabled types of routes is logically considered as a separate list.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInformation'
    _SDM_ATT_MAP = {
        'EvpnEthernetAdRouteCount': 'evpnEthernetAdRouteCount',
        'EvpnEthernetSegmentRouteCount': 'evpnEthernetSegmentRouteCount',
        'EvpnMacRouteCount': 'evpnMacRouteCount',
        'EvpnMulticastRouteCount': 'evpnMulticastRouteCount',
    }

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def AdVpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_5dde8265ff1ecdeb96de20b298f80538.AdVpls): An instance of the AdVpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_5dde8265ff1ecdeb96de20b298f80538 import AdVpls
        return AdVpls(self)

    @property
    def EvpnEthernetAd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_12dab0dc2864617054af263fc2b58155.EvpnEthernetAd): An instance of the EvpnEthernetAd class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_12dab0dc2864617054af263fc2b58155 import EvpnEthernetAd
        return EvpnEthernetAd(self)

    @property
    def EvpnEthernetSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_40ee843e162d38e5cb7726bfd833049f.EvpnEthernetSegment): An instance of the EvpnEthernetSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_40ee843e162d38e5cb7726bfd833049f import EvpnEthernetSegment
        return EvpnEthernetSegment(self)

    @property
    def EvpnMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_86150b3c69e43c37b03253f974aaf4e9.EvpnMac): An instance of the EvpnMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_86150b3c69e43c37b03253f974aaf4e9 import EvpnMac
        return EvpnMac(self)

    @property
    def EvpnMulticast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_2332f2753b59728e071685b055054c3a.EvpnMulticast): An instance of the EvpnMulticast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_2332f2753b59728e071685b055054c3a import EvpnMulticast
        return EvpnMulticast(self)

    @property
    def IpV4MulticastMplsVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_80de293cc7b2808bdf53a0e093cca30e.IpV4MulticastMplsVpn): An instance of the IpV4MulticastMplsVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_80de293cc7b2808bdf53a0e093cca30e import IpV4MulticastMplsVpn
        return IpV4MulticastMplsVpn(self)

    @property
    def IpV6MulticastMplsVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_d5defc40d2603c5ae259d96b20899427.IpV6MulticastMplsVpn): An instance of the IpV6MulticastMplsVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_d5defc40d2603c5ae259d96b20899427 import IpV6MulticastMplsVpn
        return IpV6MulticastMplsVpn(self)

    @property
    def Ipv4Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_fc7ec4c3d8c03e9cbb20f32806a31040.Ipv4Multicast): An instance of the Ipv4Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_fc7ec4c3d8c03e9cbb20f32806a31040 import Ipv4Multicast
        return Ipv4Multicast(self)

    @property
    def Ipv4MulticastVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_edb2c16f7b63fa9484b778f711c90fa2.Ipv4MulticastVpn): An instance of the Ipv4MulticastVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_edb2c16f7b63fa9484b778f711c90fa2 import Ipv4MulticastVpn
        return Ipv4MulticastVpn(self)

    @property
    def Ipv4Unicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_46145dc1db04f9b8ca284ae1b1f97d4c.Ipv4Unicast): An instance of the Ipv4Unicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_46145dc1db04f9b8ca284ae1b1f97d4c import Ipv4Unicast
        return Ipv4Unicast(self)

    @property
    def Ipv4mpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_ae3d2a891e54132a528702b808875d79.Ipv4mpls): An instance of the Ipv4mpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_ae3d2a891e54132a528702b808875d79 import Ipv4mpls
        return Ipv4mpls(self)

    @property
    def Ipv4vpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_19861e78349cda1e107027a3485bd143.Ipv4vpn): An instance of the Ipv4vpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_19861e78349cda1e107027a3485bd143 import Ipv4vpn
        return Ipv4vpn(self)

    @property
    def Ipv6Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_79b74a6b4570ecc06dd366389f4cadb2.Ipv6Multicast): An instance of the Ipv6Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_79b74a6b4570ecc06dd366389f4cadb2 import Ipv6Multicast
        return Ipv6Multicast(self)

    @property
    def Ipv6MulticastVpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_d39213c0e17a3d42693ad10771afee20.Ipv6MulticastVpn): An instance of the Ipv6MulticastVpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_d39213c0e17a3d42693ad10771afee20 import Ipv6MulticastVpn
        return Ipv6MulticastVpn(self)

    @property
    def Ipv6Unicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_8e6edd93af91708fbdeecf6b152d6dfa.Ipv6Unicast): An instance of the Ipv6Unicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_8e6edd93af91708fbdeecf6b152d6dfa import Ipv6Unicast
        return Ipv6Unicast(self)

    @property
    def Ipv6mpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_1b76569d6340a83ced4933d8b353a1f9.Ipv6mpls): An instance of the Ipv6mpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_1b76569d6340a83ced4933d8b353a1f9 import Ipv6mpls
        return Ipv6mpls(self)

    @property
    def Ipv6vpn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_9888e5f551d28846a488a4ecd661dc33.Ipv6vpn): An instance of the Ipv6vpn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_9888e5f551d28846a488a4ecd661dc33 import Ipv6vpn
        return Ipv6vpn(self)

    @property
    def Vpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_384184902812cb49d38ba3ad35e491ea.Vpls): An instance of the Vpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_384184902812cb49d38ba3ad35e491ea import Vpls
        return Vpls(self)

    @property
    def EvpnEthernetAdRouteCount(self):
        """
        Returns
        -------
        - number: (read only) Number of AD-Routes learned and shown in A-D route learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnEthernetAdRouteCount'])

    @property
    def EvpnEthernetSegmentRouteCount(self):
        """
        Returns
        -------
        - number: (read only) Number of Ethernet Segment routes learned and shown in ethernet segment route learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnEthernetSegmentRouteCount'])

    @property
    def EvpnMacRouteCount(self):
        """
        Returns
        -------
        - number: (read only) Number of Macs learned and shown in mac learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnMacRouteCount'])

    @property
    def EvpnMulticastRouteCount(self):
        """
        Returns
        -------
        - number: (read only) Number of RDs learned and shown in evpn multicast learned info table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnMulticastRouteCount'])
