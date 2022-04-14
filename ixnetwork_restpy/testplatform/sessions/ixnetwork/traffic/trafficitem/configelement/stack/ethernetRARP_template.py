from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class EthernetRARP(Base):
    __slots__ = ()
    _SDM_NAME = "ethernetRARP"
    _SDM_ATT_MAP = {
        "HeaderHwType": "ethernetRARP.header.hwType-1",
        "HeaderProtocolType": "ethernetRARP.header.protocolType-2",
        "HeaderHwAddressLength": "ethernetRARP.header.hwAddressLength-3",
        "HeaderProtocolAddressLength": "ethernetRARP.header.protocolAddressLength-4",
        "HeaderOpCode": "ethernetRARP.header.opCode-5",
        "HeaderSrcHwAddr": "ethernetRARP.header.srcHwAddr-6",
        "HeaderSrcIp": "ethernetRARP.header.srcIp-7",
        "HeaderDstHwAddr": "ethernetRARP.header.dstHwAddr-8",
        "HeaderDstIp": "ethernetRARP.header.dstIp-9",
    }

    def __init__(self, parent, list_op=False):
        super(EthernetRARP, self).__init__(parent, list_op)

    @property
    def HeaderHwType(self):
        """
        Display Name: Hardware Type
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderHwType"]))

    @property
    def HeaderProtocolType(self):
        """
        Display Name: Protocol Type
        Default Value: 0x0800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolType"])
        )

    @property
    def HeaderHwAddressLength(self):
        """
        Display Name: Hardware Address Length
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHwAddressLength"])
        )

    @property
    def HeaderProtocolAddressLength(self):
        """
        Display Name: Protocol Address Length
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocolAddressLength"])
        )

    @property
    def HeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 3
        Value Format: decimal
        Available enum values: 0x0003 Request Reverse, 3, 0x0004 Reply Reverse, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOpCode"]))

    @property
    def HeaderSrcHwAddr(self):
        """
        Display Name: Sender Hardware Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcHwAddr"])
        )

    @property
    def HeaderSrcIp(self):
        """
        Display Name: Sender Protocol Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcIp"]))

    @property
    def HeaderDstHwAddr(self):
        """
        Display Name: Target Hardware Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstHwAddr"])
        )

    @property
    def HeaderDstIp(self):
        """
        Display Name: Target Protocol Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstIp"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
