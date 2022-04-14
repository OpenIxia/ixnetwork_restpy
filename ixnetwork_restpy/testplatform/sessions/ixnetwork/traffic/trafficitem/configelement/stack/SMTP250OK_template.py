from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SMTP250OK(Base):
    __slots__ = ()
    _SDM_NAME = "SMTP_250_OK"
    _SDM_ATT_MAP = {
        "Response_Response Code": "SMTP_250_OK.Response_.Response Code-1",
        "Response_Space11": "SMTP_250_OK.Response_.Space11-2",
        "Response_Response parameter": "SMTP_250_OK.Response_.Response parameter-3",
        "Response_CRLF11": "SMTP_250_OK.Response_.CRLF11-4",
    }

    def __init__(self, parent, list_op=False):
        super(SMTP250OK, self).__init__(parent, list_op)

    @property
    def Response_ResponseCode(self):
        """
        Display Name: Response Code
        Default Value: 0x323530
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Response_Response Code"])
        )

    @property
    def Response_Space11(self):
        """
        Display Name: Space11
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Response_Space11"])
        )

    @property
    def Response_Responseparameter(self):
        """
        Display Name: Response parameter
        Default Value: 0x4F4B
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Response_Response parameter"])
        )

    @property
    def Response_CRLF11(self):
        """
        Display Name: CRLF11
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Response_CRLF11"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
