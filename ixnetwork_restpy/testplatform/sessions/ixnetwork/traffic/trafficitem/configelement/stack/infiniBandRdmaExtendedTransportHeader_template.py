from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InfiniBandRdmaExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "infiniBandRdmaExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "RdmaExtensionHeaderVirtualAddr": "infiniBandRdmaExtendedTransportHeader.rdmaExtensionHeader.virtualAddr-1",
        "RdmaExtensionHeaderRemoteKey": "infiniBandRdmaExtendedTransportHeader.rdmaExtensionHeader.remoteKey-2",
        "RdmaExtensionHeaderDmaLength": "infiniBandRdmaExtendedTransportHeader.rdmaExtensionHeader.dmaLength-3",
    }

    def __init__(self, parent, list_op=False):
        super(InfiniBandRdmaExtendedTransportHeader, self).__init__(parent, list_op)

    @property
    def RdmaExtensionHeaderVirtualAddr(self):
        """
        Display Name: Virtual Address (VA)
        Default Value: 0xFFFFFFFFFFFFFFFF
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RdmaExtensionHeaderVirtualAddr"]),
        )

    @property
    def RdmaExtensionHeaderRemoteKey(self):
        """
        Display Name: Remote Key
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RdmaExtensionHeaderRemoteKey"])
        )

    @property
    def RdmaExtensionHeaderDmaLength(self):
        """
        Display Name: DMA Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RdmaExtensionHeaderDmaLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
