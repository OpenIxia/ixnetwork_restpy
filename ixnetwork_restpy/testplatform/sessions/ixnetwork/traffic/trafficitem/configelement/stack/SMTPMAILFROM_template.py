from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SMTPMAILFROM(Base):
    __slots__ = ()
    _SDM_NAME = "SMTP_MAIL_FROM"
    _SDM_ATT_MAP = {
        "Request_MAIL_FROMField0": "SMTP_MAIL_FROM.Request_MAIL_FROM.field0-1",
        "Request_MAIL_FROMSpace10": "SMTP_MAIL_FROM.Request_MAIL_FROM.Space10-2",
        "Request_MAIL_FROMRequest_FROM": "SMTP_MAIL_FROM.Request_MAIL_FROM.Request_FROM-3",
        "Request_MAIL_FROMCRLF__": "SMTP_MAIL_FROM.Request_MAIL_FROM.CRLF__-4",
    }

    def __init__(self, parent, list_op=False):
        super(SMTPMAILFROM, self).__init__(parent, list_op)

    @property
    def Request_MAIL_FROMField0(self):
        """
        Display Name: Command_MAIL
        Default Value: 0x4D41494C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Request_MAIL_FROMField0"])
        )

    @property
    def Request_MAIL_FROMSpace10(self):
        """
        Display Name: Space10
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Request_MAIL_FROMSpace10"])
        )

    @property
    def Request_MAIL_FROMRequest_FROM(self):
        """
        Display Name: Request_FROM
        Default Value: 0x46524F4D3A203C6775727061727461704070617472696F74732E696E3E
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Request_MAIL_FROMRequest_FROM"]),
        )

    @property
    def Request_MAIL_FROMCRLF__(self):
        """
        Display Name: CRLF__
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Request_MAIL_FROMCRLF__"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
