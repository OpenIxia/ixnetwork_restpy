from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FrameRelay(Base):
    __slots__ = ()
    _SDM_NAME = "frameRelay"
    _SDM_ATT_MAP = {
        "Address2ByteDlciHiOrderBits": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.dlciHiOrderBits-1",
        "Address2ByteCrBit": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.crBit-2",
        "Address2ByteEa0Bit": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.ea0Bit-3",
        "Address2ByteDlciLoOrderBits": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.dlciLoOrderBits-4",
        "Address2ByteFecnBit": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.fecnBit-5",
        "Address2ByteBecnBit": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.becnBit-6",
        "Address2ByteDeBit": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.deBit-7",
        "Address2ByteEa1Bit": "frameRelay.header.frameRelayTag.frameRelay.address.address2Byte.ea1Bit-8",
        "HeaderControl": "frameRelay.header.control-9",
        "PaddingPad": "frameRelay.header.padding.pad-10",
        "HeaderNlpid": "frameRelay.header.nlpid-11",
    }

    def __init__(self, parent, list_op=False):
        super(FrameRelay, self).__init__(parent, list_op)

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
    def HeaderControl(self):
        """
        Display Name: Control
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderControl"]))

    @property
    def PaddingPad(self):
        """
        Display Name: Pad
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PaddingPad"]))

    @property
    def HeaderNlpid(self):
        """
        Display Name: NLPID
        Default Value: 0xCC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderNlpid"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
