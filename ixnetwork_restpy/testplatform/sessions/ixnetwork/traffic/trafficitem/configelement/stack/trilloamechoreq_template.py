from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Trilloamechoreq(Base):
    __slots__ = ()
    _SDM_NAME = "trill_oam_echo_req"
    _SDM_ATT_MAP = {
        "HeaderSpid": "trill_oam_echo_req.header.spid-1",
        "HeaderSequence": "trill_oam_echo_req.header.sequence-2",
    }

    def __init__(self, parent, list_op=False):
        super(Trilloamechoreq, self).__init__(parent, list_op)

    @property
    def HeaderSpid(self):
        """
        Display Name: SPID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSpid"]))

    @property
    def HeaderSequence(self):
        """
        Display Name: Sequence Number
        Default Value: 0x0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSequence"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
