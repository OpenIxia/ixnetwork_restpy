from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Jpeg2000VideoFormat(Base):
    __slots__ = ()
    _SDM_NAME = "jpeg2000VideoFormat"
    _SDM_ATT_MAP = {
        "Jpeg2000PayloadHeaderType": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.type-1",
        "Jpeg2000PayloadHeaderMainHeaderFlag": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.mainHeaderFlag-2",
        "Jpeg2000PayloadHeaderMhId": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.mhId-3",
        "Jpeg2000PayloadHeaderTileFieldInvalidationFlag": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.tileFieldInvalidationFlag-4",
        "Jpeg2000PayloadHeaderPriority": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.priority-5",
        "Jpeg2000PayloadHeaderTileNumber": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.tileNumber-6",
        "Jpeg2000PayloadHeaderReservedField": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.reservedField-7",
        "Jpeg2000PayloadHeaderFragmentOffset": "jpeg2000VideoFormat.header.jpeg2000PayloadHeader.fragmentOffset-8",
        "Jpeg2000PayloadPacketizationUnit1": "jpeg2000VideoFormat.header.jpeg2000Payload.packetizationUnit1-9",
        "Jpeg2000PayloadPacketizationUnit2": "jpeg2000VideoFormat.header.jpeg2000Payload.packetizationUnit2-10",
    }

    def __init__(self, parent, list_op=False):
        super(Jpeg2000VideoFormat, self).__init__(parent, list_op)

    @property
    def Jpeg2000PayloadHeaderType(self):
        """
        Display Name: TP
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Jpeg2000PayloadHeaderType"])
        )

    @property
    def Jpeg2000PayloadHeaderMainHeaderFlag(self):
        """
        Display Name: MHF
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Jpeg2000PayloadHeaderMainHeaderFlag"]
            ),
        )

    @property
    def Jpeg2000PayloadHeaderMhId(self):
        """
        Display Name: MH Id
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Jpeg2000PayloadHeaderMhId"])
        )

    @property
    def Jpeg2000PayloadHeaderTileFieldInvalidationFlag(self):
        """
        Display Name: T
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Jpeg2000PayloadHeaderTileFieldInvalidationFlag"]
            ),
        )

    @property
    def Jpeg2000PayloadHeaderPriority(self):
        """
        Display Name: Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Jpeg2000PayloadHeaderPriority"]),
        )

    @property
    def Jpeg2000PayloadHeaderTileNumber(self):
        """
        Display Name: Tile Number
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Jpeg2000PayloadHeaderTileNumber"]),
        )

    @property
    def Jpeg2000PayloadHeaderReservedField(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Jpeg2000PayloadHeaderReservedField"]
            ),
        )

    @property
    def Jpeg2000PayloadHeaderFragmentOffset(self):
        """
        Display Name: Fragment offset
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Jpeg2000PayloadHeaderFragmentOffset"]
            ),
        )

    @property
    def Jpeg2000PayloadPacketizationUnit1(self):
        """
        Display Name: Packetization Unit 1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Jpeg2000PayloadPacketizationUnit1"]),
        )

    @property
    def Jpeg2000PayloadPacketizationUnit2(self):
        """
        Display Name: Packetization Unit 2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Jpeg2000PayloadPacketizationUnit2"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
