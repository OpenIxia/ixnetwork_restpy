from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcMessageExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcMessageExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "MessageExtendedTransportHeaderRqmsn": "mrcMessageExtendedTransportHeader.messageExtendedTransportHeader.rqmsn-1",
        "MessageExtendedTransportHeaderMsn": "mrcMessageExtendedTransportHeader.messageExtendedTransportHeader.msn-2",
    }

    def __init__(self, parent, list_op=False):
        super(MrcMessageExtendedTransportHeader, self).__init__(parent, list_op)

    @property
    def MessageExtendedTransportHeaderRqmsn(self):
        """
        Display Name: Receive Queue MSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageExtendedTransportHeaderRqmsn"]
            ),
        )

    @property
    def MessageExtendedTransportHeaderMsn(self):
        """
        Display Name: Requestor MSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MessageExtendedTransportHeaderMsn"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
