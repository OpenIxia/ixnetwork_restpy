from uhd_restpy.base import Base
from uhd_restpy.files import Files


class EthernetNoFCS(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernetNoFCS'
    _SDM_ATT_MAP = {
        'HeaderDestinationAddress': 'ethernetNoFCS.header.destinationAddress-1',
        'HeaderSourceAddress': 'ethernetNoFCS.header.sourceAddress-2',
        'HeaderEtherType': 'ethernetNoFCS.header.etherType-3',
    }

    def __init__(self, parent, list_op=False):
        super(EthernetNoFCS, self).__init__(parent, list_op)

    @property
    def HeaderDestinationAddress(self):
        """
        Display Name: Destination MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDestinationAddress']))

    @property
    def HeaderSourceAddress(self):
        """
        Display Name: Source MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderSourceAddress']))

    @property
    def HeaderEtherType(self):
        """
        Display Name: Ethernet-Type
        Default Value: 0xFFFF
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderEtherType']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
