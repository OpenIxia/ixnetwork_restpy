from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Aal5(Base):
    __slots__ = ()
    _SDM_NAME = "aal5"
    _SDM_ATT_MAP = {
        "AtmL2HeaderVpi": "aal5.atmL2Header.atmL2Header.vpi-1",
        "AtmL2HeaderVci": "aal5.atmL2Header.atmL2Header.vci-2",
    }

    def __init__(self, parent, list_op=False):
        super(Aal5, self).__init__(parent, list_op)

    @property
    def AtmL2HeaderVpi(self):
        """
        Display Name: Vpi
        Default Value: 0x0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmL2HeaderVpi"])
        )

    @property
    def AtmL2HeaderVci(self):
        """
        Display Name: Vci
        Default Value: 0x0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmL2HeaderVci"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
