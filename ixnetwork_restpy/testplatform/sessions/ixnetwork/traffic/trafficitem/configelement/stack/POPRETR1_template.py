from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class POPRETR1(Base):
    __slots__ = ()
    _SDM_NAME = "POP_RETR_1"
    _SDM_ATT_MAP = {
        "REQUESTXRequest command": "POP_RETR_1.REQUESTX.Request command-1",
        "REQUESTXSpace7": "POP_RETR_1.REQUESTX.Space7-2",
        "REQUESTXRequest parameter": "POP_RETR_1.REQUESTX.Request parameter-3",
        "REQUESTXCRLFxx": "POP_RETR_1.REQUESTX.CRLFxx-4",
    }

    def __init__(self, parent, list_op=False):
        super(POPRETR1, self).__init__(parent, list_op)

    @property
    def REQUESTXRequestcommand(self):
        """
        Display Name: Request command
        Default Value: 0x52455452
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTXRequest command"])
        )

    @property
    def REQUESTXSpace7(self):
        """
        Display Name: Space7
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTXSpace7"])
        )

    @property
    def REQUESTXRequestparameter(self):
        """
        Display Name: Request parameter
        Default Value: 0x31
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTXRequest parameter"])
        )

    @property
    def REQUESTXCRLFxx(self):
        """
        Display Name: CRLFxx
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTXCRLFxx"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
