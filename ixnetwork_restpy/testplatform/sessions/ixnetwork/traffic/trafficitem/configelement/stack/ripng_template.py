from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ripng(Base):
    __slots__ = ()
    _SDM_NAME = "ripng"
    _SDM_ATT_MAP = {
        "Command": "ripng.header.ripngHeader.command-1",
        "Version": "ripng.header.ripngHeader.version-2",
        "MustBeZero": "ripng.header.ripngHeader.mustBeZero-3",
        "RteIpv6Prefix": "ripng.header.routeTableEntries.routingTableEntryType.rte.ipv6Prefix-4",
        "RteRouteTag": "ripng.header.routeTableEntries.routingTableEntryType.rte.routeTag-5",
        "RtePrefixLength": "ripng.header.routeTableEntries.routingTableEntryType.rte.prefixLength-6",
        "RteMetric": "ripng.header.routeTableEntries.routingTableEntryType.rte.metric-7",
        "NextHopRTEIpv6NexthopPrefix": "ripng.header.routeTableEntries.routingTableEntryType.nextHopRTE.ipv6NexthopPrefix-8",
        "NextHopRTEMustBeZero": "ripng.header.routeTableEntries.routingTableEntryType.nextHopRTE.mustBeZero-9",
        "RoutingtableentrytypeNextHopRTEMustBeZero": "ripng.header.routeTableEntries.routingTableEntryType.nextHopRTE.mustBeZero-10",
        "NextHopRTEUnused": "ripng.header.routeTableEntries.routingTableEntryType.nextHopRTE.unused-11",
    }

    def __init__(self, parent, list_op=False):
        super(Ripng, self).__init__(parent, list_op)

    @property
    def Command(self):
        """
        Display Name: Command
        Default Value: 1
        Value Format: decimal
        Available enum values: Request, 1, Response, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Command"]))

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def MustBeZero(self):
        """
        Display Name: Must be zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MustBeZero"]))

    @property
    def RteIpv6Prefix(self):
        """
        Display Name: IPv6 prefix
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RteIpv6Prefix"]))

    @property
    def RteRouteTag(self):
        """
        Display Name: Route tag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RteRouteTag"]))

    @property
    def RtePrefixLength(self):
        """
        Display Name: Prefix length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtePrefixLength"])
        )

    @property
    def RteMetric(self):
        """
        Display Name: Metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RteMetric"]))

    @property
    def NextHopRTEIpv6NexthopPrefix(self):
        """
        Display Name: IPv6 nexthop prefix
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopRTEIpv6NexthopPrefix"])
        )

    @property
    def NextHopRTEMustBeZero(self):
        """
        Display Name: Must be zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopRTEMustBeZero"])
        )

    @property
    def RoutingtableentrytypeNextHopRTEMustBeZero(self):
        """
        Display Name: Must be zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtableentrytypeNextHopRTEMustBeZero"]
            ),
        )

    @property
    def NextHopRTEUnused(self):
        """
        Display Name: Unused
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopRTEUnused"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
