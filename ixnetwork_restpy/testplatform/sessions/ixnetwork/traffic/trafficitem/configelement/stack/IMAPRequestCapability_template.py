from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IMAPRequestCapability(Base):
    __slots__ = ()
    _SDM_NAME = "IMAP_Request_Capability"
    _SDM_ATT_MAP = {
        "REQUESTRequest Tag": "IMAP_Request_Capability.REQUEST.Request Tag-1",
        "REQUESTSP": "IMAP_Request_Capability.REQUEST.SP-2",
        "REQUESTRequest": "IMAP_Request_Capability.REQUEST.Request-3",
        "REQUESTCRLF": "IMAP_Request_Capability.REQUEST.CRLF-4",
    }

    def __init__(self, parent, list_op=False):
        super(IMAPRequestCapability, self).__init__(parent, list_op)

    @property
    def REQUESTRequestTag(self):
        """
        Display Name: Request Tag
        Default Value: 0x6130303030
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTRequest Tag"])
        )

    @property
    def REQUESTSP(self):
        """
        Display Name: SP
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["REQUESTSP"]))

    @property
    def REQUESTRequest(self):
        """
        Display Name: Request
        Default Value: 0x4341504142494C495459
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTRequest"])
        )

    @property
    def REQUESTCRLF(self):
        """
        Display Name: CRLF
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["REQUESTCRLF"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
