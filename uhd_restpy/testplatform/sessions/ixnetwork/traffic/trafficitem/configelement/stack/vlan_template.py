from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Vlan(Base):
    __slots__ = ()
    _SDM_NAME = 'vlan'
    _SDM_ATT_MAP = {
        'VlanTagVlanUserPriority': 'vlan.header.vlanTag.vlanUserPriority-1',
        'VlanTagCfi': 'vlan.header.vlanTag.cfi-2',
        'VlanTagVlanID': 'vlan.header.vlanTag.vlanID-3',
        'ProtocolID': 'vlan.header.protocolID-4',
    }

    def __init__(self, parent, list_op=False):
        super(Vlan, self).__init__(parent, list_op)

    @property
    def VlanTagVlanUserPriority(self):
        """
        Display Name: VLAN Priority
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTagVlanUserPriority']))

    @property
    def VlanTagCfi(self):
        """
        Display Name: Canonical Format Indicator
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTagCfi']))

    @property
    def VlanTagVlanID(self):
        """
        Display Name: VLAN-ID
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTagVlanID']))

    @property
    def ProtocolID(self):
        """
        Display Name: Protocol-ID
        Default Value: 0xffff
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProtocolID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
