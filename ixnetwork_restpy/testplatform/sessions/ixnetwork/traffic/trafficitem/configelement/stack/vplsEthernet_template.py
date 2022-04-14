from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VplsEthernet(Base):
    __slots__ = ()
    _SDM_NAME = "vplsEthernet"
    _SDM_ATT_MAP = {
        "PweControlWordZero": "vplsEthernet.pweControlWord.zero-1",
        "PweControlWordReserved": "vplsEthernet.pweControlWord.reserved-2",
        "PweControlWordSequenceNumber": "vplsEthernet.pweControlWord.sequenceNumber-3",
    }

    def __init__(self, parent, list_op=False):
        super(VplsEthernet, self).__init__(parent, list_op)

    @property
    def PweControlWordZero(self):
        """
        Display Name: CW Zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PweControlWordZero"])
        )

    @property
    def PweControlWordReserved(self):
        """
        Display Name: CW Rsvd
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PweControlWordReserved"])
        )

    @property
    def PweControlWordSequenceNumber(self):
        """
        Display Name: CW Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PweControlWordSequenceNumber"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
