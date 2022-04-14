from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class StpTCNBPDU(Base):
    __slots__ = ()
    _SDM_NAME = "stpTCNBPDU"
    _SDM_ATT_MAP = {
        "HeaderProtocolIdentifier": "stpTCNBPDU.header.protocolIdentifier-1",
        "HeaderProtocolVersionIdentifier": "stpTCNBPDU.header.protocolVersionIdentifier-2",
        "HeaderBpduType": "stpTCNBPDU.header.bpduType-3",
    }

    def __init__(self, parent, list_op=False):
        super(StpTCNBPDU, self).__init__(parent, list_op)

    @property
    def HeaderProtocolIdentifier(self):
        """
        Display Name: Protocol identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolIdentifier"])
        )

    @property
    def HeaderProtocolVersionIdentifier(self):
        """
        Display Name: Protocol version identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolVersionIdentifier"]),
        )

    @property
    def HeaderBpduType(self):
        """
        Display Name: BPDU type
        Default Value: 0x80
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBpduType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
