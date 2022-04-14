from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MpegtsPayload(Base):
    __slots__ = ()
    _SDM_NAME = "mpegtsPayload"
    _SDM_ATT_MAP = {
        "PayloadLength": "mpegtsPayload.payload.length-1",
        "PayloadDataPayload": "mpegtsPayload.payload.dataPayload-2",
    }

    def __init__(self, parent, list_op=False):
        super(MpegtsPayload, self).__init__(parent, list_op)

    @property
    def PayloadLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PayloadLength"]))

    @property
    def PayloadDataPayload(self):
        """
        Display Name: Data Payload
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PayloadDataPayload"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
