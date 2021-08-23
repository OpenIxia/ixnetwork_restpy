from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Udp(Base):
    __slots__ = ()
    _SDM_NAME = 'udp'
    _SDM_ATT_MAP = {
        'SrcPort': 'udp.header.srcPort-1',
        'DstPort': 'udp.header.dstPort-2',
        'Length': 'udp.header.length-3',
        'Checksum': 'udp.header.checksum-4',
    }

    def __init__(self, parent, list_op=False):
        super(Udp, self).__init__(parent, list_op)

    @property
    def SrcPort(self):
        """
        Display Name: UDP-Source-Port
        Default Value: 63
        Value Format: decimal
        Available enum values: Default, 63, DHCP, 68, DHCPv6, 546, LDP, 646, Mobile IP, 434, RIPng, 521, RIP, 520, RTP, 30000, NTP, 123
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcPort']))

    @property
    def DstPort(self):
        """
        Display Name: UDP-Dest-Port
        Default Value: 63
        Value Format: decimal
        Available enum values: Default, 63, DHCP, 67, DHCPv6, 547, BFD, 3784, L2TP, 1701, Mobile IP, 434, RIPng, 521, RIP, 520, RTP, 40392, NTP, 123
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DstPort']))

    @property
    def Length(self):
        """
        Display Name: UDP-Length
        Default Value: 8
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def Checksum(self):
        """
        Display Name: UDP-Checksum
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
