from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Vxlan(Base):
    __slots__ = ()
    _SDM_NAME = 'vxlan'
    _SDM_ATT_MAP = {
        'Flags': 'vxlan.header.flags-1',
        'Reserved': 'vxlan.header.reserved-2',
        'Vni': 'vxlan.header.vni-3',
        'Reserved8': 'vxlan.header.reserved8-4',
    }

    def __init__(self, parent, list_op=False):
        super(Vxlan, self).__init__(parent, list_op)

    @property
    def Flags(self):
        """
        Display Name: Flags
        Default Value: 0x08
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Vni(self):
        """
        Display Name: VNI
        Default Value: 1234
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vni']))

    @property
    def Reserved8(self):
        """
        Display Name: Reserved8
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved8']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
