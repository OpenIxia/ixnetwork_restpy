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


class NetworkGroup(Base):
    """Describes a set of network clouds with similar configuration

        and the same multiplicity for devices behind.
    The NetworkGroup class encapsulates a list of networkGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkGroup.find() method.
    The list can be managed by using the NetworkGroup.add() and NetworkGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "networkGroup"
    _SDM_ATT_MAP = {
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Enabled": "enabled",
        "Multiplier": "multiplier",
        "Name": "name",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(NetworkGroup, self).__init__(parent, list_op)

    @property
    def BgpIPRouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty_3dbf4edca5d6573869a4ee79cda6644b.BgpIPRouteProperty): An instance of the BgpIPRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty_3dbf4edca5d6573869a4ee79cda6644b import (
            BgpIPRouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIPRouteProperty", None) is not None:
                return self._properties.get("BgpIPRouteProperty")
        return BgpIPRouteProperty(self)

    @property
    def BgpL3VpnRouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty_e2aee0650e29dba83e26da419c8f5f5d.BgpL3VpnRouteProperty): An instance of the BgpL3VpnRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty_e2aee0650e29dba83e26da419c8f5f5d import (
            BgpL3VpnRouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpL3VpnRouteProperty", None) is not None:
                return self._properties.get("BgpL3VpnRouteProperty")
        return BgpL3VpnRouteProperty(self)

    @property
    def BgpMVpnReceiverSitesIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4_279b1194a64614140f00d08a876cb61b.BgpMVpnReceiverSitesIpv4): An instance of the BgpMVpnReceiverSitesIpv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4_279b1194a64614140f00d08a876cb61b import (
            BgpMVpnReceiverSitesIpv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpMVpnReceiverSitesIpv4", None) is not None:
                return self._properties.get("BgpMVpnReceiverSitesIpv4")
        return BgpMVpnReceiverSitesIpv4(self)

    @property
    def BgpMVpnReceiverSitesIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6_49c886be42acc1f3fc70df1023ccb0bd.BgpMVpnReceiverSitesIpv6): An instance of the BgpMVpnReceiverSitesIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6_49c886be42acc1f3fc70df1023ccb0bd import (
            BgpMVpnReceiverSitesIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpMVpnReceiverSitesIpv6", None) is not None:
                return self._properties.get("BgpMVpnReceiverSitesIpv6")
        return BgpMVpnReceiverSitesIpv6(self)

    @property
    def BgpMVpnSenderSiteSpmsiV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitespmsiv4_4b13597607a662131f4202b2be10d840.BgpMVpnSenderSiteSpmsiV4): An instance of the BgpMVpnSenderSiteSpmsiV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitespmsiv4_4b13597607a662131f4202b2be10d840 import (
            BgpMVpnSenderSiteSpmsiV4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpMVpnSenderSiteSpmsiV4", None) is not None:
                return self._properties.get("BgpMVpnSenderSiteSpmsiV4")
        return BgpMVpnSenderSiteSpmsiV4(self)

    @property
    def BgpMVpnSenderSiteSpmsiV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitespmsiv6_2952dbb55deecb9e4187a6b85fc7807e.BgpMVpnSenderSiteSpmsiV6): An instance of the BgpMVpnSenderSiteSpmsiV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitespmsiv6_2952dbb55deecb9e4187a6b85fc7807e import (
            BgpMVpnSenderSiteSpmsiV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpMVpnSenderSiteSpmsiV6", None) is not None:
                return self._properties.get("BgpMVpnSenderSiteSpmsiV6")
        return BgpMVpnSenderSiteSpmsiV6(self)

    @property
    def BgpMVpnSenderSitesIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4_83c1dffccb6359eeaa27efcb24b1e2a2.BgpMVpnSenderSitesIpv4): An instance of the BgpMVpnSenderSitesIpv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4_83c1dffccb6359eeaa27efcb24b1e2a2 import (
            BgpMVpnSenderSitesIpv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpMVpnSenderSitesIpv4", None) is not None:
                return self._properties.get("BgpMVpnSenderSitesIpv4")
        return BgpMVpnSenderSitesIpv4(self)

    @property
    def BgpMVpnSenderSitesIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6_432522ec6a3a94bf0469071086aef3c0.BgpMVpnSenderSitesIpv6): An instance of the BgpMVpnSenderSitesIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6_432522ec6a3a94bf0469071086aef3c0 import (
            BgpMVpnSenderSitesIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpMVpnSenderSitesIpv6", None) is not None:
                return self._properties.get("BgpMVpnSenderSitesIpv6")
        return BgpMVpnSenderSitesIpv6(self)

    @property
    def BgpV6IPRouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty_a52cfd647078952e2675a9fcb67c5b8c.BgpV6IPRouteProperty): An instance of the BgpV6IPRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty_a52cfd647078952e2675a9fcb67c5b8c import (
            BgpV6IPRouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpV6IPRouteProperty", None) is not None:
                return self._properties.get("BgpV6IPRouteProperty")
        return BgpV6IPRouteProperty(self)

    @property
    def BgpV6L3VpnRouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty_31ec3d51dd542be8b59cdd94b98698df.BgpV6L3VpnRouteProperty): An instance of the BgpV6L3VpnRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty_31ec3d51dd542be8b59cdd94b98698df import (
            BgpV6L3VpnRouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpV6L3VpnRouteProperty", None) is not None:
                return self._properties.get("BgpV6L3VpnRouteProperty")
        return BgpV6L3VpnRouteProperty(self)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_ecb45bfaef4008cb27346c98c45748b2.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_ecb45bfaef4008cb27346c98c45748b2 import (
            CMacProperties,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CMacProperties", None) is not None:
                return self._properties.get("CMacProperties")
        return CMacProperties(self)

    @property
    def DeviceGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09.DeviceGroup): An instance of the DeviceGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09 import (
            DeviceGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DeviceGroup", None) is not None:
                return self._properties.get("DeviceGroup")
        return DeviceGroup(self)

    @property
    def DslPools(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dslpools_d9b929e10c822a015fb7026b5bad393a.DslPools): An instance of the DslPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dslpools_d9b929e10c822a015fb7026b5bad393a import (
            DslPools,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DslPools", None) is not None:
                return self._properties.get("DslPools")
        return DslPools(self)

    @property
    def ECpriReRadioChannelsOrUsers(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprireradiochannelsorusers_d1f6861b47ba784e3298939a333f12b9.ECpriReRadioChannelsOrUsers): An instance of the ECpriReRadioChannelsOrUsers class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprireradiochannelsorusers_d1f6861b47ba784e3298939a333f12b9 import (
            ECpriReRadioChannelsOrUsers,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ECpriReRadioChannelsOrUsers", None) is not None:
                return self._properties.get("ECpriReRadioChannelsOrUsers")
        return ECpriReRadioChannelsOrUsers(self)

    @property
    def ECpriRecRadioChannelsOrUsers(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirecradiochannelsorusers_5814e34000b9bdc960142e49f7af3c67.ECpriRecRadioChannelsOrUsers): An instance of the ECpriRecRadioChannelsOrUsers class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirecradiochannelsorusers_5814e34000b9bdc960142e49f7af3c67 import (
            ECpriRecRadioChannelsOrUsers,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ECpriRecRadioChannelsOrUsers", None) is not None:
                return self._properties.get("ECpriRecRadioChannelsOrUsers")
        return ECpriRecRadioChannelsOrUsers(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_f9fe868ed341d666199597001888e18d.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_f9fe868ed341d666199597001888e18d import (
            EvpnIPv4PrefixRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnIPv4PrefixRange", None) is not None:
                return self._properties.get("EvpnIPv4PrefixRange")
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_907e82e321deae422b0ee1ed0f82f2f3.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_907e82e321deae422b0ee1ed0f82f2f3 import (
            EvpnIPv6PrefixRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnIPv6PrefixRange", None) is not None:
                return self._properties.get("EvpnIPv6PrefixRange")
        return EvpnIPv6PrefixRange(self)

    @property
    def GRIBIIpv4Entry(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.gribiipv4entry_ed5330eae91aea3aecb945c3eda32ad4.GRIBIIpv4Entry): An instance of the GRIBIIpv4Entry class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.gribiipv4entry_ed5330eae91aea3aecb945c3eda32ad4 import (
            GRIBIIpv4Entry,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GRIBIIpv4Entry", None) is not None:
                return self._properties.get("GRIBIIpv4Entry")
        return GRIBIIpv4Entry(self)

    @property
    def Ipv4PrefixPools(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools_2d6f2aedde61c058965d4e1b21741352.Ipv4PrefixPools): An instance of the Ipv4PrefixPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools_2d6f2aedde61c058965d4e1b21741352 import (
            Ipv4PrefixPools,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4PrefixPools", None) is not None:
                return self._properties.get("Ipv4PrefixPools")
        return Ipv4PrefixPools(self)

    @property
    def Ipv6PrefixPools(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools_f83aba85ff769655b348dc60ddcb30f2.Ipv6PrefixPools): An instance of the Ipv6PrefixPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools_f83aba85ff769655b348dc60ddcb30f2 import (
            Ipv6PrefixPools,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6PrefixPools", None) is not None:
                return self._properties.get("Ipv6PrefixPools")
        return Ipv6PrefixPools(self)

    @property
    def IsisL3RouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3routeproperty_efc01a54a3fe800787fededcdef1b6c7.IsisL3RouteProperty): An instance of the IsisL3RouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3routeproperty_efc01a54a3fe800787fededcdef1b6c7 import (
            IsisL3RouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisL3RouteProperty", None) is not None:
                return self._properties.get("IsisL3RouteProperty")
        return IsisL3RouteProperty(self)

    @property
    def IsisSpbMacCloudConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig_791b0bf61c8f6877cabfa2621478ab8a.IsisSpbMacCloudConfig): An instance of the IsisSpbMacCloudConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig_791b0bf61c8f6877cabfa2621478ab8a import (
            IsisSpbMacCloudConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSpbMacCloudConfig", None) is not None:
                return self._properties.get("IsisSpbMacCloudConfig")
        return IsisSpbMacCloudConfig(self)

    @property
    def IsisTrillUCastMacConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig_a91c5b3e28b2bee04ff08d2e22fad1e2.IsisTrillUCastMacConfig): An instance of the IsisTrillUCastMacConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig_a91c5b3e28b2bee04ff08d2e22fad1e2 import (
            IsisTrillUCastMacConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisTrillUCastMacConfig", None) is not None:
                return self._properties.get("IsisTrillUCastMacConfig")
        return IsisTrillUCastMacConfig(self)

    @property
    def LdpFECProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpfecproperty_9d07999903dc2acadf9a2f44f8a94399.LdpFECProperty): An instance of the LdpFECProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpfecproperty_9d07999903dc2acadf9a2f44f8a94399 import (
            LdpFECProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpFECProperty", None) is not None:
                return self._properties.get("LdpFECProperty")
        return LdpFECProperty(self)

    @property
    def LdpIpv6FECProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpipv6fecproperty_408cfe80a37623da202d7739fba9b830.LdpIpv6FECProperty): An instance of the LdpIpv6FECProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpipv6fecproperty_408cfe80a37623da202d7739fba9b830 import (
            LdpIpv6FECProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpIpv6FECProperty", None) is not None:
                return self._properties.get("LdpIpv6FECProperty")
        return LdpIpv6FECProperty(self)

    @property
    def MacPools(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macpools_414597218f17eaa9c882bf703e2d0bdd.MacPools): An instance of the MacPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macpools_414597218f17eaa9c882bf703e2d0bdd import (
            MacPools,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MacPools", None) is not None:
                return self._properties.get("MacPools")
        return MacPools(self)

    @property
    def NetworkGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup_4a63874e791827c3a0361c2d201dbc0c.NetworkGroup): An instance of the NetworkGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup_4a63874e791827c3a0361c2d201dbc0c import (
            NetworkGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetworkGroup", None) is not None:
                return self._properties.get("NetworkGroup")
        return NetworkGroup(self)

    @property
    def NetworkRangeInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo_cbb1e7fa358c353ee8fd62246a36a824.NetworkRangeInfo): An instance of the NetworkRangeInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo_cbb1e7fa358c353ee8fd62246a36a824 import (
            NetworkRangeInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetworkRangeInfo", None) is not None:
                return self._properties.get("NetworkRangeInfo")
        return NetworkRangeInfo(self)

    @property
    def NetworkTopology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology_8aeb1c02ce88d0f4f656681df998fe83.NetworkTopology): An instance of the NetworkTopology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology_8aeb1c02ce88d0f4f656681df998fe83 import (
            NetworkTopology,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetworkTopology", None) is not None:
                return self._properties.get("NetworkTopology")
        return NetworkTopology(self)

    @property
    def OspfRouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfrouteproperty_d69371739e1874a63feb0c8493c3f052.OspfRouteProperty): An instance of the OspfRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfrouteproperty_d69371739e1874a63feb0c8493c3f052 import (
            OspfRouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OspfRouteProperty", None) is not None:
                return self._properties.get("OspfRouteProperty")
        return OspfRouteProperty(self)

    @property
    def Ospfv3RouteProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty_daf6d024b6ece255d2d043618b13bae5.Ospfv3RouteProperty): An instance of the Ospfv3RouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty_daf6d024b6ece255d2d043618b13bae5 import (
            Ospfv3RouteProperty,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospfv3RouteProperty", None) is not None:
                return self._properties.get("Ospfv3RouteProperty")
        return Ospfv3RouteProperty(self)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def Enabled(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables/disables device.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Enabled"]))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of device instances per parent device instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    def update(self, Multiplier=None, Name=None):
        # type: (int, str) -> NetworkGroup
        """Updates networkGroup resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Multiplier=None, Name=None):
        # type: (int, str) -> NetworkGroup
        """Adds a new networkGroup resource on the server and adds it to the container.

        Args
        ----
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved networkGroup resources using find and the newly added networkGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained networkGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Multiplier=None, Name=None):
        # type: (int, str, int, str) -> NetworkGroup
        """Finds and retrieves networkGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkGroup resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching networkGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of networkGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Enabled=None):
        """Base class infrastructure that gets a list of networkGroup device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Enabled (str): optional regex of enabled

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
