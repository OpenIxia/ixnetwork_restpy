from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SueAFHGEN2Normal(Base):
    __slots__ = ()
    _SDM_NAME = "sueAFHGEN2Normal"
    _SDM_ATT_MAP = {
        "FlagsVFlag": "sueAFHGEN2Normal.afhGen2Normal.flags.vFlag-1",
        "FlagsWFlag": "sueAFHGEN2Normal.afhGen2Normal.flags.wFlag-2",
        "FlagsReservedFlag1": "sueAFHGEN2Normal.afhGen2Normal.flags.reservedFlag1-3",
        "FlagsReservedFlag2": "sueAFHGEN2Normal.afhGen2Normal.flags.reservedFlag2-4",
        "FlagsZFlag": "sueAFHGEN2Normal.afhGen2Normal.flags.zFlag-5",
        "FlagsYFlag": "sueAFHGEN2Normal.afhGen2Normal.flags.yFlag-6",
        "FlagsXFlag": "sueAFHGEN2Normal.afhGen2Normal.flags.xFlag-7",
        "FlagsMFlag": "sueAFHGEN2Normal.afhGen2Normal.flags.mFlag-8",
        "HopLimitAndEntropyHopLimit": "sueAFHGEN2Normal.afhGen2Normal.destMac8to15Bits.hopLimitAndEntropy.hopLimit-9",
        "HopLimitAndEntropyEntropySpare_4Bit": "sueAFHGEN2Normal.afhGen2Normal.destMac8to15Bits.hopLimitAndEntropy.entropySpare_4Bit-10",
        "OpaqueOpaque_8Bit": "sueAFHGEN2Normal.afhGen2Normal.destMac8to15Bits.opaque.opaque_8Bit-11",
        "DestXPUIdDestXPUId_32Bit": "sueAFHGEN2Normal.afhGen2Normal.destMac16to47Bits.destXPUId.destXPUId_32Bit-12",
        "OpaqueOpaque1_16Bit": "sueAFHGEN2Normal.afhGen2Normal.destMac16to47Bits.opaque.opaque1_16Bit-13",
        "OpaqueOpaque2_16Bit": "sueAFHGEN2Normal.afhGen2Normal.destMac16to47Bits.opaque.opaque2_16Bit-14",
        "TrafficClassDscp": "sueAFHGEN2Normal.afhGen2Normal.srcMac0to7Bits.trafficClass.dscp-15",
        "TrafficClassEcn": "sueAFHGEN2Normal.afhGen2Normal.srcMac0to7Bits.trafficClass.ecn-16",
        "OpaqueOpaque_8Bit": "sueAFHGEN2Normal.afhGen2Normal.srcMac0to7Bits.opaque.opaque_8Bit-17",
        "EntropySpareEntropySpare_8Bit": "sueAFHGEN2Normal.afhGen2Normal.srcMac8to15Bits.entropySpare.entropySpare_8Bit-18",
        "OpaqueOpaque_8Bit": "sueAFHGEN2Normal.afhGen2Normal.srcMac8to15Bits.opaque.opaque_8Bit-19",
        "SourceXPUIdSourceXPUId_32Bit": "sueAFHGEN2Normal.afhGen2Normal.srcMac16to47Bits.sourceXPUId.sourceXPUId_32Bit-20",
        "OpaqueOpaque1_16Bit": "sueAFHGEN2Normal.afhGen2Normal.srcMac16to47Bits.opaque.opaque1_16Bit-21",
        "OpaqueOpaque2_16Bit": "sueAFHGEN2Normal.afhGen2Normal.srcMac16to47Bits.opaque.opaque2_16Bit-22",
        "EnableVLANTpid": "sueAFHGEN2Normal.afhGen2Normal.enableVLAN.tpid-23",
        "EnableVLANOpcp": "sueAFHGEN2Normal.afhGen2Normal.enableVLAN.opcp-24",
        "EnableVLANOcfi": "sueAFHGEN2Normal.afhGen2Normal.enableVLAN.ocfi-25",
        "EnableVLANOvid": "sueAFHGEN2Normal.afhGen2Normal.enableVLAN.ovid-26",
        "AfhGen2NormalEtherType": "sueAFHGEN2Normal.afhGen2Normal.etherType-27",
    }

    def __init__(self, parent, list_op=False):
        super(SueAFHGEN2Normal, self).__init__(parent, list_op)

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
        Default Value: 0
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
    def HopLimitAndEntropyHopLimit(self):
        """
        Display Name: Hop Limit (4 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HopLimitAndEntropyHopLimit"])
        )

    @property
    def HopLimitAndEntropyEntropySpare_4Bit(self):
        """
        Display Name: Entropy Spare (4 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HopLimitAndEntropyEntropySpare_4Bit"]
            ),
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
    def DestXPUIdDestXPUId_32Bit(self):
        """
        Display Name: Destination XPU Id (32 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestXPUIdDestXPUId_32Bit"])
        )

    @property
    def OpaqueOpaque1_16Bit(self):
        """
        Display Name: Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque1_16Bit"])
        )

    @property
    def OpaqueOpaque2_16Bit(self):
        """
        Display Name: Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque2_16Bit"])
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
    def EntropySpareEntropySpare_8Bit(self):
        """
        Display Name: Entropy Spare (8 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EntropySpareEntropySpare_8Bit"]),
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
    def SourceXPUIdSourceXPUId_32Bit(self):
        """
        Display Name: Source XPU Id (32 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceXPUIdSourceXPUId_32Bit"])
        )

    @property
    def OpaqueOpaque1_16Bit(self):
        """
        Display Name: Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque1_16Bit"])
        )

    @property
    def OpaqueOpaque2_16Bit(self):
        """
        Display Name: Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque2_16Bit"])
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
    def AfhGen2NormalEtherType(self):
        """
        Display Name: EtherType
        Default Value: 0xFFF3
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen2NormalEtherType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
