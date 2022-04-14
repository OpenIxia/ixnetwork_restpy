from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rip1(Base):
    __slots__ = ()
    _SDM_NAME = "rip1"
    _SDM_ATT_MAP = {
        "Command": "rip1.header.rip1Header.command-1",
        "Version": "rip1.header.rip1Header.version-2",
        "Unused1": "rip1.header.rip1Header.unused1-3",
        "RoutingTableEntryAddressFamilyIdentifier": "rip1.header.routingTableEntry.addressFamilyIdentifier-4",
        "RoutingTableEntryUnused2": "rip1.header.routingTableEntry.unused2-5",
        "RoutingTableEntryIpv4Address": "rip1.header.routingTableEntry.ipv4Address-6",
        "RoutingTableEntryUnused3": "rip1.header.routingTableEntry.unused3-7",
        "RoutingTableEntryUnused4": "rip1.header.routingTableEntry.unused4-8",
        "RoutingTableEntryMetric": "rip1.header.routingTableEntry.metric-9",
    }

    def __init__(self, parent, list_op=False):
        super(Rip1, self).__init__(parent, list_op)

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
    def Unused1(self):
        """
        Display Name: Unused1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Unused1"]))

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
    def RoutingTableEntryUnused2(self):
        """
        Display Name: Unused2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryUnused2"])
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
    def RoutingTableEntryUnused3(self):
        """
        Display Name: Unused3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryUnused3"])
        )

    @property
    def RoutingTableEntryUnused4(self):
        """
        Display Name: Unused4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTableEntryUnused4"])
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
