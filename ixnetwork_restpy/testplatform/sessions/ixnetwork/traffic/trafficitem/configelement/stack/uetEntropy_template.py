from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetEntropy(Base):
    __slots__ = ()
    _SDM_NAME = "uetEntropy"
    _SDM_ATT_MAP = {
        "EntropyHeaderEntropy": "uetEntropy.entropyHeader.entropy-1",
        "EntropyHeaderReserved": "uetEntropy.entropyHeader.Reserved-2",
    }

    def __init__(self, parent, list_op=False):
        super(UetEntropy, self).__init__(parent, list_op)

    @property
    def EntropyHeaderEntropy(self):
        """
        Display Name: Entropy
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EntropyHeaderEntropy"])
        )

    @property
    def EntropyHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EntropyHeaderReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
