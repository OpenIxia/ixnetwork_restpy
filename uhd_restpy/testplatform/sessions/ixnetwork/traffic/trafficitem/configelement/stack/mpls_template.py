from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Mpls(Base):
    __slots__ = ()
    _SDM_NAME = 'mpls'
    _SDM_ATT_MAP = {
        'LabelValue': 'mpls.label.value-1',
        'LabelExperimental': 'mpls.label.experimental-2',
        'LabelBottomOfStack': 'mpls.label.bottomOfStack-3',
        'LabelTtl': 'mpls.label.ttl-4',
        'LabelTracker': 'mpls.label.tracker-5',
    }

    def __init__(self, parent, list_op=False):
        super(Mpls, self).__init__(parent, list_op)

    @property
    def LabelValue(self):
        """
        Display Name: Label Value
        Default Value: 16
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelValue']))

    @property
    def LabelExperimental(self):
        """
        Display Name: MPLS Exp
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelExperimental']))

    @property
    def LabelBottomOfStack(self):
        """
        Display Name: Bottom of Stack Bit
        Default Value: 1
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelBottomOfStack']))

    @property
    def LabelTtl(self):
        """
        Display Name: Time To Live
        Default Value: 64
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelTtl']))

    @property
    def LabelTracker(self):
        """
        Display Name: Label Tracker
        Default Value: 0x0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelTracker']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
