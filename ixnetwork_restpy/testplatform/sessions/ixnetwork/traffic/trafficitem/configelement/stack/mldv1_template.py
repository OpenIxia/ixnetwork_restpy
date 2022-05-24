from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mldv1(Base):
    __slots__ = ()
    _SDM_NAME = "mldv1 "
    _SDM_ATT_MAP = {
        "Type": "mldv1 .header.type-1",
        "Code": "mldv1 .header.code-2",
        "Mldv1Checksum": "mldv1 .header.mldv1Checksum-3",
        "MaximumResponseDelayValue": "mldv1 .header.maximumResponseDelay.value-4",
        "MaximumResponseDelayValue": "mldv1 .header.maximumResponseDelay.value-5",
        "MaximumResponseDelayValue": "mldv1 .header.maximumResponseDelay.value-6",
        "Reserved": "mldv1 .header.reserved-7",
        "MulticastAddress": "mldv1 .header.multicastAddress-8",
    }

    def __init__(self, parent, list_op=False):
        super(Mldv1, self).__init__(parent, list_op)

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 130
        Value Format: decimal
        Available enum values: Query, 130, Report, 131, Done, 132
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def Code(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Code"]))

    @property
    def Mldv1Checksum(self):
        """
        Display Name: MLDv1 checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mldv1Checksum"]))

    @property
    def MaximumResponseDelayValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumResponseDelayValue"])
        )

    @property
    def MaximumResponseDelayValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumResponseDelayValue"])
        )

    @property
    def MaximumResponseDelayValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumResponseDelayValue"])
        )

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
    def MulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastAddress"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
