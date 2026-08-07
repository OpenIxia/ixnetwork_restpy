from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcRdmaExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcRdmaExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "RdmaExtendedTransportHeaderVirtualAddr": "mrcRdmaExtendedTransportHeader.rdmaExtendedTransportHeader.virtualAddr-1",
        "RdmaExtendedTransportHeaderRemoteKey": "mrcRdmaExtendedTransportHeader.rdmaExtendedTransportHeader.remoteKey-2",
        "RdmaExtendedTransportHeaderDmaLength": "mrcRdmaExtendedTransportHeader.rdmaExtendedTransportHeader.dmaLength-3",
    }

    def __init__(self, parent, list_op=False):
        super(MrcRdmaExtendedTransportHeader, self).__init__(parent, list_op)

    @property
    def RdmaExtendedTransportHeaderVirtualAddr(self):
        """
        Display Name: Virtual Address
        Default Value: 0xFFFFFFFFFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RdmaExtendedTransportHeaderVirtualAddr"]
            ),
        )

    @property
    def RdmaExtendedTransportHeaderRemoteKey(self):
        """
        Display Name: Remote Key
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RdmaExtendedTransportHeaderRemoteKey"]
            ),
        )

    @property
    def RdmaExtendedTransportHeaderDmaLength(self):
        """
        Display Name: DMA Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RdmaExtendedTransportHeaderDmaLength"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
