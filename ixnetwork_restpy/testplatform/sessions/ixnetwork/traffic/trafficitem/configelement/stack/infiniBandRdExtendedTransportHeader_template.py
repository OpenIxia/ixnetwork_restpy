from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InfiniBandRdExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "infiniBandRdExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "InfiniBandRdExtendedTransportHeaderReserve": "infiniBandRdExtendedTransportHeader.infiniBandRdExtendedTransportHeader.reserve-1",
        "InfiniBandRdExtendedTransportHeaderEeContext": "infiniBandRdExtendedTransportHeader.infiniBandRdExtendedTransportHeader.eeContext-2",
    }

    def __init__(self, parent, list_op=False):
        super(InfiniBandRdExtendedTransportHeader, self).__init__(parent, list_op)

    @property
    def InfiniBandRdExtendedTransportHeaderReserve(self):
        """
        Display Name: Reserve
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["InfiniBandRdExtendedTransportHeaderReserve"]
            ),
        )

    @property
    def InfiniBandRdExtendedTransportHeaderEeContext(self):
        """
        Display Name: End-to-End (EE) Context
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["InfiniBandRdExtendedTransportHeaderEeContext"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
