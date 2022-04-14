from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VcMuxPPP(Base):
    __slots__ = ()
    _SDM_NAME = "vcMuxPPP"
    _SDM_ATT_MAP = {
        "HeaderPppProtocolType": "vcMuxPPP.header.pppProtocolType-1",
    }

    def __init__(self, parent, list_op=False):
        super(VcMuxPPP, self).__init__(parent, list_op)

    @property
    def HeaderPppProtocolType(self):
        """
        Display Name: PPP Protocol Type
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPppProtocolType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
