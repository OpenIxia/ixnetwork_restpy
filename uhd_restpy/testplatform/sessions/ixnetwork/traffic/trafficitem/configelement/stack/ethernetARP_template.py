from uhd_restpy.base import Base
from uhd_restpy.files import Files


class EthernetARP(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernetARP'
    _SDM_ATT_MAP = {
        'HeaderHardwareType': 'ethernetARP.header.hardwareType-1',
        'HeaderProtocolType': 'ethernetARP.header.protocolType-2',
        'HeaderHardwareAddressLength': 'ethernetARP.header.hardwareAddressLength-3',
        'HeaderProtocolAddressLength': 'ethernetARP.header.protocolAddressLength-4',
        'HeaderOpCode': 'ethernetARP.header.opCode-5',
        'HeaderSrcHardwareAddress': 'ethernetARP.header.srcHardwareAddress-6',
        'HeaderSrcIP': 'ethernetARP.header.srcIP-7',
        'HeaderDstHardwareAddress': 'ethernetARP.header.dstHardwareAddress-8',
        'HeaderDstIP': 'ethernetARP.header.dstIP-9',
    }

    def __init__(self, parent, list_op=False):
        super(EthernetARP, self).__init__(parent, list_op)

    @property
    def HeaderHardwareType(self):
        """
        Display Name: Hardware Type
        Default Value: 0x0001
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderHardwareType']))

    @property
    def HeaderProtocolType(self):
        """
        Display Name: Protocol Type
        Default Value: 0x0800
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderProtocolType']))

    @property
    def HeaderHardwareAddressLength(self):
        """
        Display Name: Hardware Address Length
        Default Value: 0x06
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderHardwareAddressLength']))

    @property
    def HeaderProtocolAddressLength(self):
        """
        Display Name: Protocol Address Length
        Default Value: 0x04
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderProtocolAddressLength']))

    @property
    def HeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: 0x0000 Unknown, 0, 0x0001 Request, 1, 0x0002 Reply, 2, 0x0003 Request Reverse, 3, 0x0004 Reply Reverse, 4
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderOpCode']))

    @property
    def HeaderSrcHardwareAddress(self):
        """
        Display Name: Sender Hardware Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderSrcHardwareAddress']))

    @property
    def HeaderSrcIP(self):
        """
        Display Name: Sender Protocol Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderSrcIP']))

    @property
    def HeaderDstHardwareAddress(self):
        """
        Display Name: Target Hardware Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDstHardwareAddress']))

    @property
    def HeaderDstIP(self):
        """
        Display Name: Target Protocol Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDstIP']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
