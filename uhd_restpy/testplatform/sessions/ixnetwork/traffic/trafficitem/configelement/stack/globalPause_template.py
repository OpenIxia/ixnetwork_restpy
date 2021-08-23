from uhd_restpy.base import Base
from uhd_restpy.files import Files


class GlobalPause(Base):
    __slots__ = ()
    _SDM_NAME = 'globalPause'
    _SDM_ATT_MAP = {
        'HeaderDstAddress': 'globalPause.header.header.dstAddress-1',
        'HeaderSrcAddress': 'globalPause.header.header.srcAddress-2',
        'HeaderEthertype': 'globalPause.header.header.ethertype-3',
        'MacControlControlOpcode': 'globalPause.header.macControl.controlOpcode-4',
        'MacControlPfcQueue0': 'globalPause.header.macControl.pfcQueue0-5',
    }

    def __init__(self, parent, list_op=False):
        super(GlobalPause, self).__init__(parent, list_op)

    @property
    def HeaderDstAddress(self):
        """
        Display Name: Destination address
        Default Value: 01:80:C2:00:00:01
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDstAddress']))

    @property
    def HeaderSrcAddress(self):
        """
        Display Name: Source address
        Default Value: 00:00:AA:00:00:01
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderSrcAddress']))

    @property
    def HeaderEthertype(self):
        """
        Display Name: Ethertype
        Default Value: 0x8808
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderEthertype']))

    @property
    def MacControlControlOpcode(self):
        """
        Display Name: Control opcode
        Default Value: 0x0001
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacControlControlOpcode']))

    @property
    def MacControlPfcQueue0(self):
        """
        Display Name: PAUSE Quanta
        Default Value: 0xFFFF
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacControlPfcQueue0']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
