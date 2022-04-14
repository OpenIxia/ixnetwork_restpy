from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CiscoFrameRelay(Base):
    __slots__ = ()
    _SDM_NAME = "ciscoFrameRelay"
    _SDM_ATT_MAP = {
        "Address2ByteDlciHiOrderBits": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.dlciHiOrderBits-1",
        "Address2ByteCrBit": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.crBit-2",
        "Address2ByteEa0Bit": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.ea0Bit-3",
        "Address2ByteDlciLoOrderBits": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.dlciLoOrderBits-4",
        "Address2ByteFecnBit": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.fecnBit-5",
        "Address2ByteBecnBit": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.becnBit-6",
        "Address2ByteDeBit": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.deBit-7",
        "Address2ByteEa1Bit": "ciscoFrameRelay.header.frameRelayTag.frameRelay.address.address2Byte.ea1Bit-8",
        "HeaderEtherType": "ciscoFrameRelay.header.etherType-9",
    }

    def __init__(self, parent, list_op=False):
        super(CiscoFrameRelay, self).__init__(parent, list_op)

    @property
    def Address2ByteDlciHiOrderBits(self):
        """
        Display Name: DLCI High Order Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteDlciHiOrderBits"])
        )

    @property
    def Address2ByteCrBit(self):
        """
        Display Name: CR Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteCrBit"])
        )

    @property
    def Address2ByteEa0Bit(self):
        """
        Display Name: EA0 Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteEa0Bit"])
        )

    @property
    def Address2ByteDlciLoOrderBits(self):
        """
        Display Name: DLCI Low Order Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteDlciLoOrderBits"])
        )

    @property
    def Address2ByteFecnBit(self):
        """
        Display Name: FECN Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteFecnBit"])
        )

    @property
    def Address2ByteBecnBit(self):
        """
        Display Name: BECN Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteBecnBit"])
        )

    @property
    def Address2ByteDeBit(self):
        """
        Display Name: DE Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteDeBit"])
        )

    @property
    def Address2ByteEa1Bit(self):
        """
        Display Name: EA1 Bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Address2ByteEa1Bit"])
        )

    @property
    def HeaderEtherType(self):
        """
        Display Name: Ethernet Type
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderEtherType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
