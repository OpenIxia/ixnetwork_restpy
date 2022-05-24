from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Pppnohdlc(Base):
    __slots__ = ()
    _SDM_NAME = "ppp_no_hdlc"
    _SDM_ATT_MAP = {
        "HeaderProtocolType": "ppp_no_hdlc.header.protocolType-1",
    }

    def __init__(self, parent, list_op=False):
        super(Pppnohdlc, self).__init__(parent, list_op)

    @property
    def HeaderProtocolType(self):
        """
        Display Name: PPP Protocol Type
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
