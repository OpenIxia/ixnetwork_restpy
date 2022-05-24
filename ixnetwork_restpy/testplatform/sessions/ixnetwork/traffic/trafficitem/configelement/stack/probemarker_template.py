from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Probemarker(Base):
    __slots__ = ()
    _SDM_NAME = "probemarker"
    _SDM_ATT_MAP = {
        "HeaderPm": "probemarker.header.pm-1",
    }

    def __init__(self, parent, list_op=False):
        super(Probemarker, self).__init__(parent, list_op)

    @property
    def HeaderPm(self):
        """
        Display Name: INT Probe Marker
        Default Value: 0xFFFFFFFFFFFFFFF9
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderPm"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
