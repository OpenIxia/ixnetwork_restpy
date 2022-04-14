from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LlcSNAP(Base):
    __slots__ = ()
    _SDM_NAME = "llcSNAP"
    _SDM_ATT_MAP = {
        "SnapHeaderDsap": "llcSNAP.snapHeader.dsap-1",
        "SnapHeaderSsap": "llcSNAP.snapHeader.ssap-2",
        "SnapHeaderControlField": "llcSNAP.snapHeader.controlField-3",
        "SnapHeaderSnapOUI": "llcSNAP.snapHeader.snapOUI-4",
        "SnapHeaderSnapPID": "llcSNAP.snapHeader.snapPID-5",
    }

    def __init__(self, parent, list_op=False):
        super(LlcSNAP, self).__init__(parent, list_op)

    @property
    def SnapHeaderDsap(self):
        """
        Display Name: DSAP
        Default Value: 0xAA
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SnapHeaderDsap"])
        )

    @property
    def SnapHeaderSsap(self):
        """
        Display Name: SSAP
        Default Value: 0xAA
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SnapHeaderSsap"])
        )

    @property
    def SnapHeaderControlField(self):
        """
        Display Name: Control field
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SnapHeaderControlField"])
        )

    @property
    def SnapHeaderSnapOUI(self):
        """
        Display Name: SNAP OUI (Organizationally Unique Id)
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SnapHeaderSnapOUI"])
        )

    @property
    def SnapHeaderSnapPID(self):
        """
        Display Name: SNAP PID
        Default Value: 0x0800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SnapHeaderSnapPID"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
