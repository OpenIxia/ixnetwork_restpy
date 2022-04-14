from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PppoESession(Base):
    __slots__ = ()
    _SDM_NAME = "pppoESession"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pppoESession.header.header.version-1",
        "HeaderType": "pppoESession.header.header.type-2",
        "HeaderCode": "pppoESession.header.header.code-3",
        "HeaderSessionID": "pppoESession.header.header.sessionID-4",
        "HeaderPayloadLength": "pppoESession.header.header.payloadLength-5",
        "HeaderProtocolID": "pppoESession.header.protocolID-6",
    }

    def __init__(self, parent, list_op=False):
        super(PppoESession, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: PPPoE protocol version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderType(self):
        """
        Display Name: PPPoE type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderCode(self):
        """
        Display Name: PPPoE code
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCode"]))

    @property
    def HeaderSessionID(self):
        """
        Display Name: PPPoE session ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSessionID"])
        )

    @property
    def HeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPayloadLength"])
        )

    @property
    def HeaderProtocolID(self):
        """
        Display Name: PPP Protocol-ID
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolID"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
