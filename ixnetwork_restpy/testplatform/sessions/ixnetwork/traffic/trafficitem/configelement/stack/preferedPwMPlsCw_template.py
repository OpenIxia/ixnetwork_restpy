from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PreferedPwMPlsCw(Base):
    __slots__ = ()
    _SDM_NAME = "preferedPwMPlsCw"
    _SDM_ATT_MAP = {
        "ControlWordReserved": "preferedPwMPlsCw.controlWord.reserved-1",
        "ControlWordFlags": "preferedPwMPlsCw.controlWord.flags-2",
        "ControlWordFrg": "preferedPwMPlsCw.controlWord.frg-3",
        "ControlWordLength": "preferedPwMPlsCw.controlWord.length-4",
        "ControlWordSequenceNumber": "preferedPwMPlsCw.controlWord.sequenceNumber-5",
    }

    def __init__(self, parent, list_op=False):
        super(PreferedPwMPlsCw, self).__init__(parent, list_op)

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
    def ControlWordFrg(self):
        """
        Display Name: CW FRG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlWordFrg"])
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
