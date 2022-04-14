from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class EndMark(Base):
    __slots__ = ()
    _SDM_NAME = "endMark"
    _SDM_ATT_MAP = {
        "HeaderEndMark": "endMark.header.endMark-1",
    }

    def __init__(self, parent, list_op=False):
        super(EndMark, self).__init__(parent, list_op)

    @property
    def HeaderEndMark(self):
        """
        Display Name: End Mark
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderEndMark"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
