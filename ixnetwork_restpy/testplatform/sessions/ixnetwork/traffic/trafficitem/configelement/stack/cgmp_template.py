from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Cgmp(Base):
    __slots__ = ()
    _SDM_NAME = "cgmp"
    _SDM_ATT_MAP = {
        "Version": "cgmp.header.version-1",
        "Type": "cgmp.header.type-2",
        "Reserved": "cgmp.header.reserved-3",
        "Count": "cgmp.header.count-4",
        "AddressSetGroupDestinationAddress": "cgmp.header.addressSet.groupDestinationAddress-5",
        "AddressSetUnicastSourceAddress": "cgmp.header.addressSet.unicastSourceAddress-6",
    }

    def __init__(self, parent, list_op=False):
        super(Cgmp, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        Available enum values: Join, 0, Leave, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved"]))

    @property
    def Count(self):
        """
        Display Name: Count
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Count"]))

    @property
    def AddressSetGroupDestinationAddress(self):
        """
        Display Name: Group Destination Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AddressSetGroupDestinationAddress"]),
        )

    @property
    def AddressSetUnicastSourceAddress(self):
        """
        Display Name: Unicast Source Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AddressSetUnicastSourceAddress"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
