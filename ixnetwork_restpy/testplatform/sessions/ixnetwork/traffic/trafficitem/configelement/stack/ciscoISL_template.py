from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CiscoISL(Base):
    __slots__ = ()
    _SDM_NAME = "ciscoISL"
    _SDM_ATT_MAP = {
        "HeaderDstAddress": "ciscoISL.header.dstAddress-1",
        "HeaderFrameType": "ciscoISL.header.frameType-2",
        "HeaderUserBits": "ciscoISL.header.userBits-3",
        "HeaderSrcAddressHi24": "ciscoISL.header.srcAddressHi24-4",
        "HeaderSrcAddressLo24": "ciscoISL.header.srcAddressLo24-5",
        "HeaderLength": "ciscoISL.header.length-6",
        "HeaderSnapLLC": "ciscoISL.header.snapLLC-7",
        "HeaderHiBitsOfSrcAddress": "ciscoISL.header.hiBitsOfSrcAddress-8",
        "HeaderDstVlan": "ciscoISL.header.dstVlan-9",
        "HeaderBpduCDP": "ciscoISL.header.bpduCDP-10",
        "HeaderIndex": "ciscoISL.header.index-11",
        "HeaderReserved": "ciscoISL.header.reserved-12",
    }

    def __init__(self, parent, list_op=False):
        super(CiscoISL, self).__init__(parent, list_op)

    @property
    def HeaderDstAddress(self):
        """
        Display Name: Destination address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstAddress"])
        )

    @property
    def HeaderFrameType(self):
        """
        Display Name: Frame type
        Default Value: 0
        Value Format: decimal
        Available enum values: Ethernet, 0, Token-Ring, 1, FDDI, 2, ATM, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFrameType"])
        )

    @property
    def HeaderUserBits(self):
        """
        Display Name: User defined bits
        Default Value: 0
        Value Format: decimal
        Available enum values: Priority 0 (Normal), 0, Priority 1, 1, Priority 2, 2, Priority 3, 3, Priority 4, 4, Priority 5, 5, Priority 6, 6, Priority 7, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderUserBits"])
        )

    @property
    def HeaderSrcAddressHi24(self):
        """
        Display Name: Source address - high 24 bits
        Default Value: 0x0c
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcAddressHi24"])
        )

    @property
    def HeaderSrcAddressLo24(self):
        """
        Display Name: Source address - low 24 bits
        Default Value: 0x0c
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcAddressLo24"])
        )

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderSnapLLC(self):
        """
        Display Name: SNAP / LLC
        Default Value: 0xAAAA03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSnapLLC"]))

    @property
    def HeaderHiBitsOfSrcAddress(self):
        """
        Display Name: High bits of Source Address
        Default Value: 0x00000C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHiBitsOfSrcAddress"])
        )

    @property
    def HeaderDstVlan(self):
        """
        Display Name: Destination VLAN
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstVlan"]))

    @property
    def HeaderBpduCDP(self):
        """
        Display Name: BPDU and CDP indicator
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderBpduCDP"]))

    @property
    def HeaderIndex(self):
        """
        Display Name: Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderIndex"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved for Token Ring and FDDI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
