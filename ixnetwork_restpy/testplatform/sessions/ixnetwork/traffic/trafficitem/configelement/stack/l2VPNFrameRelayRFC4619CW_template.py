from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPNFrameRelayRFC4619CW(Base):
    __slots__ = ()
    _SDM_NAME = "l2VPNFrameRelayRFC4619CW"
    _SDM_ATT_MAP = {
        "ControlWordReserved": "l2VPNFrameRelayRFC4619CW.controlWord.reserved-1",
        "ControlWordFbit": "l2VPNFrameRelayRFC4619CW.controlWord.fbit-2",
        "ControlWordBbit": "l2VPNFrameRelayRFC4619CW.controlWord.bbit-3",
        "ControlWordDbit": "l2VPNFrameRelayRFC4619CW.controlWord.dbit-4",
        "ControlWordCbit": "l2VPNFrameRelayRFC4619CW.controlWord.cbit-5",
        "ControlWordZero": "l2VPNFrameRelayRFC4619CW.controlWord.zero-6",
        "ControlWordLength": "l2VPNFrameRelayRFC4619CW.controlWord.length-7",
        "ControlWordSequenceNumber": "l2VPNFrameRelayRFC4619CW.controlWord.sequenceNumber-8",
    }

    def __init__(self, parent, list_op=False):
        super(L2VPNFrameRelayRFC4619CW, self).__init__(parent, list_op)

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
    def ControlWordFbit(self):
        """
        Display Name: CW F Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordFbit"])
        )

    @property
    def ControlWordBbit(self):
        """
        Display Name: CW B Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordBbit"])
        )

    @property
    def ControlWordDbit(self):
        """
        Display Name: CW D Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordDbit"])
        )

    @property
    def ControlWordCbit(self):
        """
        Display Name: CW C Bit
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
