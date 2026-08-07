from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SueAFHGEN2Compressed(Base):
    __slots__ = ()
    _SDM_NAME = "sueAFHGEN2Compressed"
    _SDM_ATT_MAP = {
        "FlagsVFlag": "sueAFHGEN2Compressed.afhGen2Compressed.flags.vFlag-1",
        "FlagsWFlag": "sueAFHGEN2Compressed.afhGen2Compressed.flags.wFlag-2",
        "FlagsReservedFlag1": "sueAFHGEN2Compressed.afhGen2Compressed.flags.reservedFlag1-3",
        "FlagsReservedFlag2": "sueAFHGEN2Compressed.afhGen2Compressed.flags.reservedFlag2-4",
        "FlagsZFlag": "sueAFHGEN2Compressed.afhGen2Compressed.flags.zFlag-5",
        "FlagsYFlag": "sueAFHGEN2Compressed.afhGen2Compressed.flags.yFlag-6",
        "FlagsXFlag": "sueAFHGEN2Compressed.afhGen2Compressed.flags.xFlag-7",
        "FlagsMFlag": "sueAFHGEN2Compressed.afhGen2Compressed.flags.mFlag-8",
        "AfhGen2CompressedOpaque1_8Bit": "sueAFHGEN2Compressed.afhGen2Compressed.opaque1_8Bit-9",
        "AfhGen2CompressedOpaque1_16Bit": "sueAFHGEN2Compressed.afhGen2Compressed.opaque1_16Bit-10",
        "AfhGen2CompressedDestXPUId_16Bit": "sueAFHGEN2Compressed.afhGen2Compressed.destXPUId_16Bit-11",
        "TrafficClassDscp": "sueAFHGEN2Compressed.afhGen2Compressed.srcMac0to7Bits.trafficClass.dscp-12",
        "TrafficClassEcn": "sueAFHGEN2Compressed.afhGen2Compressed.srcMac0to7Bits.trafficClass.ecn-13",
        "OpaqueOpaque_8Bit": "sueAFHGEN2Compressed.afhGen2Compressed.srcMac0to7Bits.opaque.opaque_8Bit-14",
        "AfhGen2CompressedOpaque2_8Bit": "sueAFHGEN2Compressed.afhGen2Compressed.opaque2_8Bit-15",
        "AfhGen2CompressedOpaque2_16Bit": "sueAFHGEN2Compressed.afhGen2Compressed.opaque2_16Bit-16",
        "AfhGen2CompressedSourceXPUId_16Bit": "sueAFHGEN2Compressed.afhGen2Compressed.sourceXPUId_16Bit-17",
        "EnableVLANTpid": "sueAFHGEN2Compressed.afhGen2Compressed.enableVLAN.tpid-18",
        "EnableVLANOpcp": "sueAFHGEN2Compressed.afhGen2Compressed.enableVLAN.opcp-19",
        "EnableVLANOcfi": "sueAFHGEN2Compressed.afhGen2Compressed.enableVLAN.ocfi-20",
        "EnableVLANOvid": "sueAFHGEN2Compressed.afhGen2Compressed.enableVLAN.ovid-21",
        "AfhGen2CompressedEtherType": "sueAFHGEN2Compressed.afhGen2Compressed.etherType-22",
    }

    def __init__(self, parent, list_op=False):
        super(SueAFHGEN2Compressed, self).__init__(parent, list_op)

    @property
    def FlagsVFlag(self):
        """
        Display Name: V(Version)
        Default Value: 0
        Value Format: decimal
        Available enum values: Current Version, 0, Future, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsVFlag"]))

    @property
    def FlagsWFlag(self):
        """
        Display Name: W(Format)
        Default Value: 1
        Value Format: decimal
        Available enum values: Normal Format, 0, Compressed Format, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsWFlag"]))

    @property
    def FlagsReservedFlag1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReservedFlag1"])
        )

    @property
    def FlagsReservedFlag2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReservedFlag2"])
        )

    @property
    def FlagsZFlag(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsZFlag"]))

    @property
    def FlagsYFlag(self):
        """
        Display Name: Y
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsYFlag"]))

    @property
    def FlagsXFlag(self):
        """
        Display Name: X
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsXFlag"]))

    @property
    def FlagsMFlag(self):
        """
        Display Name: M(Multicast)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsMFlag"]))

    @property
    def AfhGen2CompressedOpaque1_8Bit(self):
        """
        Display Name: Dest Mac[8:15] : Opaque (8 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfhGen2CompressedOpaque1_8Bit"]),
        )

    @property
    def AfhGen2CompressedOpaque1_16Bit(self):
        """
        Display Name: Dest Mac[16:31] : Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfhGen2CompressedOpaque1_16Bit"]),
        )

    @property
    def AfhGen2CompressedDestXPUId_16Bit(self):
        """
        Display Name: Dest Mac[32:47] : Dest XPU Id (16 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfhGen2CompressedDestXPUId_16Bit"]),
        )

    @property
    def TrafficClassDscp(self):
        """
        Display Name: DSCP (6 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrafficClassDscp"])
        )

    @property
    def TrafficClassEcn(self):
        """
        Display Name: ECN (2 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrafficClassEcn"])
        )

    @property
    def OpaqueOpaque_8Bit(self):
        """
        Display Name: Opaque (8 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque_8Bit"])
        )

    @property
    def AfhGen2CompressedOpaque2_8Bit(self):
        """
        Display Name: Source Mac[8:15] : Opaque (8 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfhGen2CompressedOpaque2_8Bit"]),
        )

    @property
    def AfhGen2CompressedOpaque2_16Bit(self):
        """
        Display Name: Source Mac[16:31] : Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfhGen2CompressedOpaque2_16Bit"]),
        )

    @property
    def AfhGen2CompressedSourceXPUId_16Bit(self):
        """
        Display Name: Source Mac[32-47] : Source XPU Id (16 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AfhGen2CompressedSourceXPUId_16Bit"]
            ),
        )

    @property
    def EnableVLANTpid(self):
        """
        Display Name: TPID
        Default Value: 0x8100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVLANTpid"])
        )

    @property
    def EnableVLANOpcp(self):
        """
        Display Name: OPCP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVLANOpcp"])
        )

    @property
    def EnableVLANOcfi(self):
        """
        Display Name: OCFI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVLANOcfi"])
        )

    @property
    def EnableVLANOvid(self):
        """
        Display Name: OVID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVLANOvid"])
        )

    @property
    def AfhGen2CompressedEtherType(self):
        """
        Display Name: EtherType
        Default Value: 0xFFF2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen2CompressedEtherType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
