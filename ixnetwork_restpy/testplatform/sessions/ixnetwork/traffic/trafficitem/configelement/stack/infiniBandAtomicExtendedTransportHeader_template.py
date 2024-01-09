from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InfiniBandAtomicExtendedTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "infiniBandAtomicExtendedTransportHeader"
    _SDM_ATT_MAP = {
        "HeaderVirtualAddr": "infiniBandAtomicExtendedTransportHeader.header.virtualAddr-1",
        "HeaderRKey": "infiniBandAtomicExtendedTransportHeader.header.rKey-2",
        "HeaderDmaLength": "infiniBandAtomicExtendedTransportHeader.header.dmaLength-3",
        "HeaderSwapOrAddData": "infiniBandAtomicExtendedTransportHeader.header.swapOrAddData-4",
        "HeaderCmpDt": "infiniBandAtomicExtendedTransportHeader.header.cmpDt-5",
    }

    def __init__(self, parent, list_op=False):
        super(InfiniBandAtomicExtendedTransportHeader, self).__init__(parent, list_op)

    @property
    def HeaderVirtualAddr(self):
        """
        Display Name: Virtual Address (VA)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderVirtualAddr"])
        )

    @property
    def HeaderRKey(self):
        """
        Display Name: R Key
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderRKey"]))

    @property
    def HeaderDmaLength(self):
        """
        Display Name: DMA Lenght
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDmaLength"])
        )

    @property
    def HeaderSwapOrAddData(self):
        """
        Display Name: SWAP (or ADD) DATA (SWAPDT)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSwapOrAddData"])
        )

    @property
    def HeaderCmpDt(self):
        """
        Display Name: Compare Data (CmpDT)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCmpDt"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
