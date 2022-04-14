from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SourcePacketHeader(Base):
    __slots__ = ()
    _SDM_NAME = "sourcePacketHeader"
    _SDM_ATT_MAP = {
        "HeaderReserved": "sourcePacketHeader.header.reserved-1",
        "HeaderCycleCount": "sourcePacketHeader.header.cycleCount-2",
        "HeaderCycleOffset": "sourcePacketHeader.header.cycleOffset-3",
        "HeaderTSP": "sourcePacketHeader.header.tSP-4",
    }

    def __init__(self, parent, list_op=False):
        super(SourcePacketHeader, self).__init__(parent, list_op)

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderCycleCount(self):
        """
        Display Name: Cycle Count
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCycleCount"])
        )

    @property
    def HeaderCycleOffset(self):
        """
        Display Name: Cycle Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCycleOffset"])
        )

    @property
    def HeaderTSP(self):
        """
        Display Name: Transport Stream Packet
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderTSP"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
