# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def AdVpls(self):
        """An instance of the AdVpls class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_24592f3e13bed965e6c23f1c1b2d9641.AdVpls)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advpls_24592f3e13bed965e6c23f1c1b2d9641 import AdVpls
        return AdVpls(self)

    @property
    def EvpnEthernetAd(self):
        """An instance of the EvpnEthernetAd class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_620d04816cff72733b13b22794af5724.EvpnEthernetAd)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetad_620d04816cff72733b13b22794af5724 import EvpnEthernetAd
        return EvpnEthernetAd(self)

    @property
    def EvpnEthernetSegment(self):
        """An instance of the EvpnEthernetSegment class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_dc24d661eb63bbfbbc2c2b7249d1a96a.EvpnEthernetSegment)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnethernetsegment_dc24d661eb63bbfbbc2c2b7249d1a96a import EvpnEthernetSegment
        return EvpnEthernetSegment(self)

    @property
    def EvpnMac(self):
        """An instance of the EvpnMac class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_c7187502f1b62ee807c6bb1e864edefd.EvpnMac)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmac_c7187502f1b62ee807c6bb1e864edefd import EvpnMac
        return EvpnMac(self)

    @property
    def EvpnMulticast(self):
        """An instance of the EvpnMulticast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_1252232f190ef0e26a6d428eadbbaab8.EvpnMulticast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evpnmulticast_1252232f190ef0e26a6d428eadbbaab8 import EvpnMulticast
        return EvpnMulticast(self)

    @property
    def IpV4MulticastMplsVpn(self):
        """An instance of the IpV4MulticastMplsVpn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_fab0c052e74f6d5e193305dc18ea58f9.IpV4MulticastMplsVpn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastmplsvpn_fab0c052e74f6d5e193305dc18ea58f9 import IpV4MulticastMplsVpn
        return IpV4MulticastMplsVpn(self)

    @property
    def IpV6MulticastMplsVpn(self):
        """An instance of the IpV6MulticastMplsVpn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_4b83ce3555acb00aaaef9637348e6b19.IpV6MulticastMplsVpn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastmplsvpn_4b83ce3555acb00aaaef9637348e6b19 import IpV6MulticastMplsVpn
        return IpV6MulticastMplsVpn(self)

    @property
    def Ipv4Multicast(self):
        """An instance of the Ipv4Multicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_7a578a8ce4efd91613a77ff427b81f53.Ipv4Multicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_7a578a8ce4efd91613a77ff427b81f53 import Ipv4Multicast
        return Ipv4Multicast(self)

    @property
    def Ipv4MulticastVpn(self):
        """An instance of the Ipv4MulticastVpn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_ed84d15019e0b55d116ad84be2201a9e.Ipv4MulticastVpn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicastvpn_ed84d15019e0b55d116ad84be2201a9e import Ipv4MulticastVpn
        return Ipv4MulticastVpn(self)

    @property
    def Ipv4Unicast(self):
        """An instance of the Ipv4Unicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_8b02f5c7be8e28e024512019c7aca9c7.Ipv4Unicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicast_8b02f5c7be8e28e024512019c7aca9c7 import Ipv4Unicast
        return Ipv4Unicast(self)

    @property
    def Ipv4mpls(self):
        """An instance of the Ipv4mpls class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_38cd8307167c2ee5b1d76a8a7c4f85e6.Ipv4mpls)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4mpls_38cd8307167c2ee5b1d76a8a7c4f85e6 import Ipv4mpls
        return Ipv4mpls(self)

    @property
    def Ipv4vpn(self):
        """An instance of the Ipv4vpn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_99be8e57b1f9f300c15f4a41f5c0fbda.Ipv4vpn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4vpn_99be8e57b1f9f300c15f4a41f5c0fbda import Ipv4vpn
        return Ipv4vpn(self)

    @property
    def Ipv6Multicast(self):
        """An instance of the Ipv6Multicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_c4cc1fe4866696a0336e4d2068a5105e.Ipv6Multicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_c4cc1fe4866696a0336e4d2068a5105e import Ipv6Multicast
        return Ipv6Multicast(self)

    @property
    def Ipv6MulticastVpn(self):
        """An instance of the Ipv6MulticastVpn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_6da75fb0a9d4cf39cb9591b80083f588.Ipv6MulticastVpn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicastvpn_6da75fb0a9d4cf39cb9591b80083f588 import Ipv6MulticastVpn
        return Ipv6MulticastVpn(self)

    @property
    def Ipv6Unicast(self):
        """An instance of the Ipv6Unicast class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_adb27ca68bdbf91d629e9bab028eca36.Ipv6Unicast)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6unicast_adb27ca68bdbf91d629e9bab028eca36 import Ipv6Unicast
        return Ipv6Unicast(self)

    @property
    def Ipv6mpls(self):
        """An instance of the Ipv6mpls class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_bb7568d2fc7b0603c0c57720586c8071.Ipv6mpls)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6mpls_bb7568d2fc7b0603c0c57720586c8071 import Ipv6mpls
        return Ipv6mpls(self)

    @property
    def Ipv6vpn(self):
        """An instance of the Ipv6vpn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_d07854455f68d7b5a195849304394708.Ipv6vpn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6vpn_d07854455f68d7b5a195849304394708 import Ipv6vpn
        return Ipv6vpn(self)

    @property
    def Vpls(self):
        """An instance of the Vpls class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_846d0f2f14f6ec80f05341b71fa82746.Vpls)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpls_846d0f2f14f6ec80f05341b71fa82746 import Vpls
        return Vpls(self)

    @property
    def EvpnEthernetAdRouteCount(self):
        """(read only) Number of AD-Routes learned and shown in A-D route learned info table.

        Returns:
            number
        """
        return self._get_attribute('evpnEthernetAdRouteCount')

    @property
    def EvpnEthernetSegmentRouteCount(self):
        """(read only) Number of Ethernet Segment routes learned and shown in ethernet segment route learned info table.

        Returns:
            number
        """
        return self._get_attribute('evpnEthernetSegmentRouteCount')

    @property
    def EvpnMacRouteCount(self):
        """(read only) Number of Macs learned and shown in mac learned info table.

        Returns:
            number
        """
        return self._get_attribute('evpnMacRouteCount')

    @property
    def EvpnMulticastRouteCount(self):
        """(read only) Number of RDs learned and shown in evpn multicast learned info table.

        Returns:
            number
        """
        return self._get_attribute('evpnMulticastRouteCount')
