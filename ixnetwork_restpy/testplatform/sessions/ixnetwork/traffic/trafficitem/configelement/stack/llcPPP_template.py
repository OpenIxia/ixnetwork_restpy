from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LlcPPP(Base):
    __slots__ = ()
    _SDM_NAME = "llcPPP"
    _SDM_ATT_MAP = {
        "LlcPPPHheaderLlcHeader": "llcPPP.llcPPPHheader.llcHeader-1",
        "LlcPPPHheaderNlpid": "llcPPP.llcPPPHheader.nlpid-2",
        "LlcPPPHheaderPid": "llcPPP.llcPPPHheader.pid-3",
    }

    def __init__(self, parent, list_op=False):
        super(LlcPPP, self).__init__(parent, list_op)

    @property
    def LlcPPPHheaderLlcHeader(self):
        """
        Display Name: Logical Link Control(LLC) Header
        Default Value: 0xfefe03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LlcPPPHheaderLlcHeader"])
        )

    @property
    def LlcPPPHheaderNlpid(self):
        """
        Display Name: NLPID
        Default Value: 0xCF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LlcPPPHheaderNlpid"])
        )

    @property
    def LlcPPPHheaderPid(self):
        """
        Display Name: Protocol ID (PID)
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LlcPPPHheaderPid"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
