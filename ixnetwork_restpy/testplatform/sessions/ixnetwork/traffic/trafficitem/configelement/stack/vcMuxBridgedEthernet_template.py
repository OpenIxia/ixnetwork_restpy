from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VcMuxBridgedEthernet(Base):
    __slots__ = ()
    _SDM_NAME = "vcMuxBridgedEthernet"
    _SDM_ATT_MAP = {
        "HeaderPad": "vcMuxBridgedEthernet.header.pad-1",
    }

    def __init__(self, parent, list_op=False):
        super(VcMuxBridgedEthernet, self).__init__(parent, list_op)

    @property
    def HeaderPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderPad"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
