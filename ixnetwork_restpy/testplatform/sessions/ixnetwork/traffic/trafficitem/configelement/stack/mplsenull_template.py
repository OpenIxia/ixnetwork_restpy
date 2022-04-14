from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mplsenull(Base):
    __slots__ = ()
    _SDM_NAME = "mpls_enull"
    _SDM_ATT_MAP = {
        "LabelValue": "mpls_enull.label.value-1",
        "LabelExperimental": "mpls_enull.label.experimental-2",
        "LabelBottomOfStack": "mpls_enull.label.bottomOfStack-3",
        "LabelTtl": "mpls_enull.label.ttl-4",
    }

    def __init__(self, parent, list_op=False):
        super(Mplsenull, self).__init__(parent, list_op)

    @property
    def LabelValue(self):
        """
        Display Name: Label Value
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LabelValue"]))

    @property
    def LabelExperimental(self):
        """
        Display Name: MPLS Exp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelExperimental"])
        )

    @property
    def LabelBottomOfStack(self):
        """
        Display Name: Bottom of Stack Bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelBottomOfStack"])
        )

    @property
    def LabelTtl(self):
        """
        Display Name: Time To Live
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LabelTtl"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
