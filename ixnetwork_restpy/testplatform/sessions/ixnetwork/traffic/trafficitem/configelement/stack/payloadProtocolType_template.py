from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PayloadProtocolType(Base):
    __slots__ = ()
    _SDM_NAME = "payloadProtocolType"
    _SDM_ATT_MAP = {
        "HeaderPayloadProtocolId": "payloadProtocolType.header.payloadProtocolId-1",
    }

    def __init__(self, parent, list_op=False):
        super(PayloadProtocolType, self).__init__(parent, list_op)

    @property
    def HeaderPayloadProtocolId(self):
        """
        Display Name: Payload Protocol Id (EtherType)
        Default Value: 0xffff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPayloadProtocolId"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
