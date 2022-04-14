from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Snap(Base):
    __slots__ = ()
    _SDM_NAME = "snap"
    _SDM_ATT_MAP = {
        "SnapOUI": "snap.snapHeader.snapOUI-1",
        "SnapPID": "snap.snapHeader.snapPID-2",
    }

    def __init__(self, parent, list_op=False):
        super(Snap, self).__init__(parent, list_op)

    @property
    def SnapOUI(self):
        """
        Display Name: SNAP OUI (Organizationally Unique Id)
        Default Value: 0x00000C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SnapOUI"]))

    @property
    def SnapPID(self):
        """
        Display Name: SNAP PID
        Default Value: 0x0800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SnapPID"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
