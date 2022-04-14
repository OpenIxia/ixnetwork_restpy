from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CN(Base):
    __slots__ = ()
    _SDM_NAME = "CN"
    _SDM_ATT_MAP = {
        "CNCommonHeaderLevelbit1": "CN.CNCommonHeader.levelbit1-1",
        "CNCommonHeaderLevel": "CN.CNCommonHeader.level-2",
    }

    def __init__(self, parent, list_op=False):
        super(CN, self).__init__(parent, list_op)

    @property
    def CNCommonHeaderLevelbit1(self):
        """
        Display Name: Level Bit 1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CNCommonHeaderLevelbit1"])
        )

    @property
    def CNCommonHeaderLevel(self):
        """
        Display Name: Level
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CNCommonHeaderLevel"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
