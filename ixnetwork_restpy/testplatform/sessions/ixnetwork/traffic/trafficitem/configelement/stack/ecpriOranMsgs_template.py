from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class EcpriOranMsgs(Base):
    __slots__ = ()
    _SDM_NAME = "ecpriOranMsgs"
    _SDM_ATT_MAP = {
        "CommonheaderProtocolRevision": "ecpriOranMsgs.commonheader.protocolRevision-1",
        "CommonheaderReserved": "ecpriOranMsgs.commonheader.reserved-2",
        "CommonheaderConcatenation": "ecpriOranMsgs.commonheader.concatenation-3",
        "CommonheaderMessageType": "ecpriOranMsgs.commonheader.messageType-4",
        "CommonheaderPayloadSize": "ecpriOranMsgs.commonheader.payloadSize-5",
    }

    def __init__(self, parent, list_op=False):
        super(EcpriOranMsgs, self).__init__(parent, list_op)

    @property
    def CommonheaderProtocolRevision(self):
        """
        Display Name: Protocol Revision
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonheaderProtocolRevision"])
        )

    @property
    def CommonheaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonheaderReserved"])
        )

    @property
    def CommonheaderConcatenation(self):
        """
        Display Name: Concatenation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonheaderConcatenation"])
        )

    @property
    def CommonheaderMessageType(self):
        """
        Display Name: Message Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonheaderMessageType"])
        )

    @property
    def CommonheaderPayloadSize(self):
        """
        Display Name: Payload Size (octets)
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonheaderPayloadSize"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
