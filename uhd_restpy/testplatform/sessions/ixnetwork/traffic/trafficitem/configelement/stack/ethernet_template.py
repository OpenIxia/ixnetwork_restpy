from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Ethernet(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernet'
    _SDM_ATT_MAP = {
        'DestinationAddress': 'ethernet.header.destinationAddress-1',
        'SourceAddress': 'ethernet.header.sourceAddress-2',
        'EtherType': 'ethernet.header.etherType-3',
        'PfcQueue': 'ethernet.header.pfcQueue-4',
    }

    def __init__(self, parent, list_op=False):
        super(Ethernet, self).__init__(parent, list_op)

    @property
    def DestinationAddress(self):
        """
        Display Name: Destination MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationAddress']))

    @property
    def SourceAddress(self):
        """
        Display Name: Source MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddress']))

    @property
    def EtherType(self):
        """
        Display Name: Ethernet-Type
        Default Value: 0xFFFF
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EtherType']))

    @property
    def PfcQueue(self):
        """
        Display Name: PFC Queue
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PfcQueue']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
