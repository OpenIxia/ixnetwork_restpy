from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPNVCTypeIPCW(Base):
    __slots__ = ()
    _SDM_NAME = "l2VPNVCTypeIPCW"
    _SDM_ATT_MAP = {
        "ControlWordReserved": "l2VPNVCTypeIPCW.controlWord.reserved-1",
        "ControlWordFlags": "l2VPNVCTypeIPCW.controlWord.flags-2",
        "ControlWordZero": "l2VPNVCTypeIPCW.controlWord.zero-3",
        "ControlWordLength": "l2VPNVCTypeIPCW.controlWord.length-4",
        "ControlWordSequenceNumber": "l2VPNVCTypeIPCW.controlWord.sequenceNumber-5",
    }

    def __init__(self, parent, list_op=False):
        super(L2VPNVCTypeIPCW, self).__init__(parent, list_op)

    @property
    def ControlWordReserved(self):
        """
        Display Name: CW Rsvd
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordReserved"])
        )

    @property
    def ControlWordFlags(self):
        """
        Display Name: CW Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordFlags"])
        )

    @property
    def ControlWordZero(self):
        """
        Display Name: CW FRG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordZero"])
        )

    @property
    def ControlWordLength(self):
        """
        Display Name: CW Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordLength"])
        )

    @property
    def ControlWordSequenceNumber(self):
        """
        Display Name: CW Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordSequenceNumber"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
