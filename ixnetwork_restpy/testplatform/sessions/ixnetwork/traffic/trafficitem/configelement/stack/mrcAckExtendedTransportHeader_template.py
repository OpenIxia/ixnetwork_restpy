from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcAckExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcAckExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "AckExtTransportHeaderSyndrome": "mrcAckExtendedTransportHeader.ackExtTransportHeader.syndrome-1",
        "AckExtTransportHeaderMsn": "mrcAckExtendedTransportHeader.ackExtTransportHeader.msn-2",
    }

    def __init__(self, parent, list_op=False):
        super(MrcAckExtendedTransportHeader, self).__init__(parent, list_op)

    @property
    def AckExtTransportHeaderSyndrome(self):
        """
        Display Name: Syndrome
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AckExtTransportHeaderSyndrome"]),
        )

    @property
    def AckExtTransportHeaderMsn(self):
        """
        Display Name: Message Sequence Number (MSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckExtTransportHeaderMsn"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
