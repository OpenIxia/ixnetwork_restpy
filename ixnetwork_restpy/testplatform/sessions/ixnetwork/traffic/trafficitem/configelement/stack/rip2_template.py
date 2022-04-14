from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rip2(Base):
    __slots__ = ()
    _SDM_NAME = "rip2"
    _SDM_ATT_MAP = {
        "Command": "rip2.header.rip2Header.command-1",
        "Version": "rip2.header.rip2Header.version-2",
        "Unused": "rip2.header.rip2Header.unused-3",
        "AuthenticationEntryAddressFamilyIdentifier": "rip2.header.authenticationEntry.addressFamilyIdentifier-4",
        "AuthenticationEntryAuthenticationType": "rip2.header.authenticationEntry.authenticationType-5",
        "AuthenticationEntryAuthentication": "rip2.header.authenticationEntry.authentication-6",
        "RoutingTableEntryAddressFamilyIdentifier": "rip2.header.routingTableEntry.addressFamilyIdentifier-7",
        "RoutingTableEntryRouteTag": "rip2.header.routingTableEntry.routeTag-8",
        "RoutingTableEntryIpv4Address": "rip2.header.routingTableEntry.ipv4Address-9",
        "RoutingTableEntrySubnetMask": "rip2.header.routingTableEntry.subnetMask-10",
        "RoutingTableEntryNextHop": "rip2.header.routingTableEntry.nextHop-11",
        "RoutingTableEntryMetric": "rip2.header.routingTableEntry.metric-12",
    }

    def __init__(self, parent, list_op=False):
        super(Rip2, self).__init__(parent, list_op)

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
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Unused"]))

    @property
    def AuthenticationEntryAddressFamilyIdentifier(self):
        """
        Display Name: Address Family Identifier
        Default Value: 0xffff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AuthenticationEntryAddressFamilyIdentifier"]
            ),
        )

    @property
    def AuthenticationEntryAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AuthenticationEntryAuthenticationType"]
            ),
        )

    @property
    def AuthenticationEntryAuthentication(self):
        """
        Display Name: Authentication
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticationEntryAuthentication"]),
        )

    @property
    def RoutingTableEntryAddressFamilyIdentifier(self):
        """
        Display Name: Address Family Identifier
        Default Value: 2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingTableEntryAddressFamilyIdentifier"]
            ),
        )

    @property
    def RoutingTableEntryRouteTag(self):
        """
        Display Name: Route tag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryRouteTag"])
        )

    @property
    def RoutingTableEntryIpv4Address(self):
        """
        Display Name: IPv4 address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryIpv4Address"])
        )

    @property
    def RoutingTableEntrySubnetMask(self):
        """
        Display Name: Subnet mask
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntrySubnetMask"])
        )

    @property
    def RoutingTableEntryNextHop(self):
        """
        Display Name: Next hop
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryNextHop"])
        )

    @property
    def RoutingTableEntryMetric(self):
        """
        Display Name: Metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryMetric"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
