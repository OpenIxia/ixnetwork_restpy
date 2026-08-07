from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SueAFHGEN1(Base):
    __slots__ = ()
    _SDM_NAME = "sueAFHGEN1"
    _SDM_ATT_MAP = {
        "DestXPUDestXPUId_16Bit": "sueAFHGEN1.afhGen1.destMac0to15Bits.destXPU.destXPUId_16Bit-1",
        "OpaqueOpaque_16Bit": "sueAFHGEN1.afhGen1.destMac0to15Bits.opaque.opaque_16Bit-2",
        "AfhGen1Opaque1_16Bit": "sueAFHGEN1.afhGen1.opaque1_16Bit-3",
        "AfhGen1Opaque2_16Bit": "sueAFHGEN1.afhGen1.opaque2_16Bit-4",
        "SrcXPUIdSrcXPUId_16Bit": "sueAFHGEN1.afhGen1.srcMac0to15Bits.srcXPUId.srcXPUId_16Bit-5",
        "OpaqueOpaque_16Bit": "sueAFHGEN1.afhGen1.srcMac0to15Bits.opaque.opaque_16Bit-6",
        "AfhGen1Opaque3_16Bit": "sueAFHGEN1.afhGen1.opaque3_16Bit-7",
        "AfhGen1Opaque4_16Bit": "sueAFHGEN1.afhGen1.opaque4_16Bit-8",
        "EnableVLANTpid": "sueAFHGEN1.afhGen1.enableVLAN.tpid-9",
        "EnableVLANOpcp": "sueAFHGEN1.afhGen1.enableVLAN.opcp-10",
        "EnableVLANOcfi": "sueAFHGEN1.afhGen1.enableVLAN.ocfi-11",
        "EnableVLANOvid": "sueAFHGEN1.afhGen1.enableVLAN.ovid-12",
        "AfhGen1EtherType": "sueAFHGEN1.afhGen1.etherType-13",
        "2ByteShimArFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.arFlag-14",
        "2ByteShimFFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.fFlag-15",
        "2ByteShimCFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.cFlag-16",
        "2ByteShimCmnFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.cmnFlag-17",
        "2ByteShimTtl": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.ttl-18",
        "2ByteShimDscp": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.dscp-19",
        "2ByteShimEcn": "sueAFHGEN1.afhGen1.enableShim.shimHeader.2ByteShim.ecn-20",
        "3ByteShimArFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.arFlag-21",
        "3ByteShimFFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.fFlag-22",
        "3ByteShimCFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.cFlag-23",
        "3ByteShimCmnFlag": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.cmnFlag-24",
        "3ByteShimTtl": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.ttl-25",
        "3ByteShimDscp": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.dscp-26",
        "3ByteShimEcn": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.ecn-27",
        "3ByteShimFlowLabel": "sueAFHGEN1.afhGen1.enableShim.shimHeader.3ByteShim.flowLabel-28",
    }

    def __init__(self, parent, list_op=False):
        super(SueAFHGEN1, self).__init__(parent, list_op)

    @property
    def DestXPUDestXPUId_16Bit(self):
        """
        Display Name: Destination XPU ID (16 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestXPUDestXPUId_16Bit"])
        )

    @property
    def OpaqueOpaque_16Bit(self):
        """
        Display Name: Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque_16Bit"])
        )

    @property
    def AfhGen1Opaque1_16Bit(self):
        """
        Display Name: Dest Mac[16:31] : Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen1Opaque1_16Bit"])
        )

    @property
    def AfhGen1Opaque2_16Bit(self):
        """
        Display Name: Dest Mac[32:47] : Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen1Opaque2_16Bit"])
        )

    @property
    def SrcXPUIdSrcXPUId_16Bit(self):
        """
        Display Name: Source XPU ID (16 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcXPUIdSrcXPUId_16Bit"])
        )

    @property
    def OpaqueOpaque_16Bit(self):
        """
        Display Name: Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OpaqueOpaque_16Bit"])
        )

    @property
    def AfhGen1Opaque3_16Bit(self):
        """
        Display Name: Source Mac[16:31] : Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen1Opaque3_16Bit"])
        )

    @property
    def AfhGen1Opaque4_16Bit(self):
        """
        Display Name: Source Mac[32:47] : Opaque (16 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen1Opaque4_16Bit"])
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
    def AfhGen1EtherType(self):
        """
        Display Name: EtherType
        Default Value: 0xFFF1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AfhGen1EtherType"])
        )

    @property
    def _2ByteShimArFlag(self):
        """
        Display Name: AR-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimArFlag"])
        )

    @property
    def _2ByteShimFFlag(self):
        """
        Display Name: F-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimFFlag"])
        )

    @property
    def _2ByteShimCFlag(self):
        """
        Display Name: C-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimCFlag"])
        )

    @property
    def _2ByteShimCmnFlag(self):
        """
        Display Name: CMN-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimCmnFlag"])
        )

    @property
    def _2ByteShimTtl(self):
        """
        Display Name: TTL (4 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimTtl"]))

    @property
    def _2ByteShimDscp(self):
        """
        Display Name: DSCP (6 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimDscp"]))

    @property
    def _2ByteShimEcn(self):
        """
        Display Name: ECN (2 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["2ByteShimEcn"]))

    @property
    def _3ByteShimArFlag(self):
        """
        Display Name: AR-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimArFlag"])
        )

    @property
    def _3ByteShimFFlag(self):
        """
        Display Name: F-Flag
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimFFlag"])
        )

    @property
    def _3ByteShimCFlag(self):
        """
        Display Name: C-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimCFlag"])
        )

    @property
    def _3ByteShimCmnFlag(self):
        """
        Display Name: CMN-Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimCmnFlag"])
        )

    @property
    def _3ByteShimTtl(self):
        """
        Display Name: TTL (4 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimTtl"]))

    @property
    def _3ByteShimDscp(self):
        """
        Display Name: DSCP (6 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimDscp"]))

    @property
    def _3ByteShimEcn(self):
        """
        Display Name: ECN (2 Bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimEcn"]))

    @property
    def _3ByteShimFlowLabel(self):
        """
        Display Name: Flow Label (8 Bits)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["3ByteShimFlowLabel"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
