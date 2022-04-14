from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPNFrameRelay(Base):
    __slots__ = ()
    _SDM_NAME = "l2VPNFrameRelay"
    _SDM_ATT_MAP = {
        "HeaderControlWord": "l2VPNFrameRelay.header.controlWord-1",
    }

    def __init__(self, parent, list_op=False):
        super(L2VPNFrameRelay, self).__init__(parent, list_op)

    @property
    def HeaderControlWord(self):
        """
        Display Name: FR IP CW
        Default Value: 0x03cc
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderControlWord"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
