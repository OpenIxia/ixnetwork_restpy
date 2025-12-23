from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsRudRodAck(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsRudRodAck"
    _SDM_ATT_MAP = {
        "RudRodAckType": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.type-1",
        "RudRodAckNextHdr": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.nextHdr-2",
        "RudRodAckReserved": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.reserved-3",
        "RudRodAckMFlag": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.mFlag-4",
        "RudRodAckRetransmit": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.retransmit-5",
        "RudRodAckProbe": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.probe-6",
        "RudRodAckRequest": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.request-7",
        "RudRodAckReserved1": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.reserved1-8",
        "RudRodAckPsnOffsetProbeOpaque": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.psnOffsetProbeOpaque-9",
        "RudRodAckCackPsn": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.cackPsn-10",
        "RudRodAckSpdcid": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.spdcid-11",
        "RudRodAckDpdcidValue": "uetPdsRudRodAck.header.ackHeaderType.rudRodAck.dpdcidValue-12",
        "RudRodAckCCType": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.type-13",
        "RudRodAckCCNextHdr": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.nextHdr-14",
        "RudRodAckCCReserved": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.reserved-15",
        "RudRodAckCCMFlag": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.mFlag-16",
        "RudRodAckCCRetransmit": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.retransmit-17",
        "RudRodAckCCProbe": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.probe-18",
        "RudRodAckCCRequest": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.request-19",
        "RudRodAckCCReserved1": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.reserved1-20",
        "RudRodAckCCPsnOffsetProbeOpaque": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.psnOffsetProbeOpaque-21",
        "RudRodAckCCCackPsn": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.cackPsn-22",
        "RudRodAckCCSpdcid": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.spdcid-23",
        "RudRodAckCCDpdcidValue": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.dpdcidValue-24",
        "RudRodAckCCCcType": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.ccType-25",
        "RudRodAckCCCcFlags": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.ccFlags-26",
        "RudRodAckCCMaxPsnRange": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.maxPsnRange-27",
        "RudRodAckCCSackPSNOffset": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.sackPSNOffset-28",
        "RudRodAckCCSackBitmap": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.sackBitmap-29",
        "RudRodAckCCAckCCState": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCC.ackCCState-30",
        "RudRodAckCCXType": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.type-31",
        "RudRodAckCCXNextHdr": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.nextHdr-32",
        "RudRodAckCCXReserved": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.reserved-33",
        "RudRodAckCCXMFlag": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.mFlag-34",
        "RudRodAckCCXRetransmit": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.retransmit-35",
        "RudRodAckCCXProbe": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.probe-36",
        "RudRodAckCCXRequest": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.request-37",
        "RudRodAckCCXReserved1": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.reserved1-38",
        "RudRodAckCCXPsnOffsetProbeOpaque": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.psnOffsetProbeOpaque-39",
        "RudRodAckCCXCackPsn": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.cackPsn-40",
        "RudRodAckCCXSpdcid": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.spdcid-41",
        "RudRodAckCCXDpdcidValue": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.dpdcidValue-42",
        "RudRodAckCCXCcxType": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.ccxType-43",
        "RudRodAckCCXCcFlags": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.ccFlags-44",
        "RudRodAckCCXMaxPsnRange": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.maxPsnRange-45",
        "RudRodAckCCXSackPSNOffset": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.sackPSNOffset-46",
        "RudRodAckCCXSackBitmap": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.sackBitmap-47",
        "RudRodAckCCXAckCCXState": "uetPdsRudRodAck.header.ackHeaderType.rudRodAckCCX.ackCCXState-48",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsRudRodAck, self).__init__(parent, list_op)

    @property
    def RudRodAckType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        Available enum values: RUD_ROD_ACK, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckType"]))

    @property
    def RudRodAckNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 4
        Value Format: decimal
        Available enum values: UET_HDR_RESPONSE, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckNextHdr"])
        )

    @property
    def RudRodAckReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckReserved"])
        )

    @property
    def RudRodAckMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckMFlag"])
        )

    @property
    def RudRodAckRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckRetransmit"])
        )

    @property
    def RudRodAckProbe(self):
        """
        Display Name: Probe Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckProbe"])
        )

    @property
    def RudRodAckRequest(self):
        """
        Display Name: Request
        Default Value: 0
        Value Format: decimal
        Available enum values: NO_REQUEST, 0, REQ_CLEAR, 1, REQ_CLOSE, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckRequest"])
        )

    @property
    def RudRodAckReserved1(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckReserved1"])
        )

    @property
    def RudRodAckPsnOffsetProbeOpaque(self):
        """
        Display Name: Psn_Offset/Probe_Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RudRodAckPsnOffsetProbeOpaque"]),
        )

    @property
    def RudRodAckCackPsn(self):
        """
        Display Name: CACK_PSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCackPsn"])
        )

    @property
    def RudRodAckSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckSpdcid"])
        )

    @property
    def RudRodAckDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckDpdcidValue"])
        )

    @property
    def RudRodAckCCType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        Available enum values: RUD_ROD_ACK_CC, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCType"])
        )

    @property
    def RudRodAckCCNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 4
        Value Format: decimal
        Available enum values: UET_HDR_RESPONSE, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCNextHdr"])
        )

    @property
    def RudRodAckCCReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCReserved"])
        )

    @property
    def RudRodAckCCMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCMFlag"])
        )

    @property
    def RudRodAckCCRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCRetransmit"])
        )

    @property
    def RudRodAckCCProbe(self):
        """
        Display Name: Probe Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCProbe"])
        )

    @property
    def RudRodAckCCRequest(self):
        """
        Display Name: Request
        Default Value: 0
        Value Format: decimal
        Available enum values: NO_REQUEST, 0, REQ_CLEAR, 1, REQ_CLOSE, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCRequest"])
        )

    @property
    def RudRodAckCCReserved1(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCReserved1"])
        )

    @property
    def RudRodAckCCPsnOffsetProbeOpaque(self):
        """
        Display Name: Psn_Offset/Probe_Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCPsnOffsetProbeOpaque"]),
        )

    @property
    def RudRodAckCCCackPsn(self):
        """
        Display Name: CACK_PSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCCackPsn"])
        )

    @property
    def RudRodAckCCSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCSpdcid"])
        )

    @property
    def RudRodAckCCDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCDpdcidValue"])
        )

    @property
    def RudRodAckCCCcType(self):
        """
        Display Name: CC Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCCcType"])
        )

    @property
    def RudRodAckCCCcFlags(self):
        """
        Display Name: CC Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCCcFlags"])
        )

    @property
    def RudRodAckCCMaxPsnRange(self):
        """
        Display Name: Max PSN Range
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCMaxPsnRange"])
        )

    @property
    def RudRodAckCCSackPSNOffset(self):
        """
        Display Name: SACK PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCSackPSNOffset"])
        )

    @property
    def RudRodAckCCSackBitmap(self):
        """
        Display Name: SACK Bitmap (64-bit)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCSackBitmap"])
        )

    @property
    def RudRodAckCCAckCCState(self):
        """
        Display Name: ACK CC State (64-bit)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCAckCCState"])
        )

    @property
    def RudRodAckCCXType(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        Available enum values: RUD_ROD_ACK_CCX, 9
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXType"])
        )

    @property
    def RudRodAckCCXNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 4
        Value Format: decimal
        Available enum values: UET_HDR_RESPONSE, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXNextHdr"])
        )

    @property
    def RudRodAckCCXReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXReserved"])
        )

    @property
    def RudRodAckCCXMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXMFlag"])
        )

    @property
    def RudRodAckCCXRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXRetransmit"])
        )

    @property
    def RudRodAckCCXProbe(self):
        """
        Display Name: Probe Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXProbe"])
        )

    @property
    def RudRodAckCCXRequest(self):
        """
        Display Name: Request
        Default Value: 0
        Value Format: decimal
        Available enum values: NO_REQUEST, 0, REQ_CLEAR, 1, REQ_CLOSE, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXRequest"])
        )

    @property
    def RudRodAckCCXReserved1(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXReserved1"])
        )

    @property
    def RudRodAckCCXPsnOffsetProbeOpaque(self):
        """
        Display Name: Psn_Offset/Probe_Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXPsnOffsetProbeOpaque"]),
        )

    @property
    def RudRodAckCCXCackPsn(self):
        """
        Display Name: CACK_PSN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXCackPsn"])
        )

    @property
    def RudRodAckCCXSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXSpdcid"])
        )

    @property
    def RudRodAckCCXDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXDpdcidValue"])
        )

    @property
    def RudRodAckCCXCcxType(self):
        """
        Display Name: CCX Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXCcxType"])
        )

    @property
    def RudRodAckCCXCcFlags(self):
        """
        Display Name: CC Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXCcFlags"])
        )

    @property
    def RudRodAckCCXMaxPsnRange(self):
        """
        Display Name: Max PSN Range
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXMaxPsnRange"])
        )

    @property
    def RudRodAckCCXSackPSNOffset(self):
        """
        Display Name: SACK PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXSackPSNOffset"])
        )

    @property
    def RudRodAckCCXSackBitmap(self):
        """
        Display Name: SACK Bitmap (64-bit)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXSackBitmap"])
        )

    @property
    def RudRodAckCCXAckCCXState(self):
        """
        Display Name: ACK CCX State (128-bit)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodAckCCXAckCCXState"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
