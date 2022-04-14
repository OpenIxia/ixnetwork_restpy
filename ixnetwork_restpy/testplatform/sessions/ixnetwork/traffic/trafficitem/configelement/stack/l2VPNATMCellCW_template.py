from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPNATMCellCW(Base):
    __slots__ = ()
    _SDM_NAME = "l2VPNATMCellCW"
    _SDM_ATT_MAP = {
        "ControlWordReserved": "l2VPNATMCellCW.controlWord.reserved-1",
        "ControlWordTbit": "l2VPNATMCellCW.controlWord.tbit-2",
        "ControlWordEbit": "l2VPNATMCellCW.controlWord.ebit-3",
        "ControlWordLbit": "l2VPNATMCellCW.controlWord.lbit-4",
        "ControlWordCbit": "l2VPNATMCellCW.controlWord.cbit-5",
        "ControlWordZero": "l2VPNATMCellCW.controlWord.zero-6",
        "ControlWordLength": "l2VPNATMCellCW.controlWord.length-7",
        "ControlWordSequenceNumber": "l2VPNATMCellCW.controlWord.sequenceNumber-8",
    }

    def __init__(self, parent, list_op=False):
        super(L2VPNATMCellCW, self).__init__(parent, list_op)

    @property
    def ControlWordReserved(self):
        """
        Display Name: CW RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordReserved"])
        )

    @property
    def ControlWordTbit(self):
        """
        Display Name: CW T Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordTbit"])
        )

    @property
    def ControlWordEbit(self):
        """
        Display Name: CW E bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordEbit"])
        )

    @property
    def ControlWordLbit(self):
        """
        Display Name: CW L bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordLbit"])
        )

    @property
    def ControlWordCbit(self):
        """
        Display Name: CW C bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordCbit"])
        )

    @property
    def ControlWordZero(self):
        """
        Display Name: CW Zero
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
