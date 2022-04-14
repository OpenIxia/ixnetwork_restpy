from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class POPOK(Base):
    __slots__ = ()
    _SDM_NAME = "POP_OK"
    _SDM_ATT_MAP = {
        "RESPONSE_OKResponse Indicator": "POP_OK.RESPONSE_OK.Response Indicator-1",
        "RESPONSE_OKSpace8": "POP_OK.RESPONSE_OK.Space8-2",
        "RESPONSE_OKResponse description": "POP_OK.RESPONSE_OK.Response description-3",
        "RESPONSE_OKCRLF_": "POP_OK.RESPONSE_OK.CRLF_-4",
    }

    def __init__(self, parent, list_op=False):
        super(POPOK, self).__init__(parent, list_op)

    @property
    def RESPONSE_OKResponseIndicator(self):
        """
        Display Name: Response Indicator
        Default Value: 0x2B4F4B
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RESPONSE_OKResponse Indicator"]),
        )

    @property
    def RESPONSE_OKSpace8(self):
        """
        Display Name: Space8
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE_OKSpace8"])
        )

    @property
    def RESPONSE_OKResponsedescription(self):
        """
        Display Name: Response description
        Default Value: 0x31323539206F6374657473
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RESPONSE_OKResponse description"]),
        )

    @property
    def RESPONSE_OKCRLF_(self):
        """
        Display Name: CRLF_
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE_OKCRLF_"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
