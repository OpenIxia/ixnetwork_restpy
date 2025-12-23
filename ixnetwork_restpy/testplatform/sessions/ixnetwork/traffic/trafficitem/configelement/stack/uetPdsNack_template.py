from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsNack(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsNack"
    _SDM_ATT_MAP = {
        "RudRodNackType": "uetPdsNack.header.nackHeaderType.rudRodNack.type-1",
        "RudRodNackNextHdr": "uetPdsNack.header.nackHeaderType.rudRodNack.nextHdr-2",
        "RudRodNackReserved": "uetPdsNack.header.nackHeaderType.rudRodNack.reserved-3",
        "RudRodNackMFlag": "uetPdsNack.header.nackHeaderType.rudRodNack.mFlag-4",
        "RudRodNackRetransmit": "uetPdsNack.header.nackHeaderType.rudRodNack.retransmit-5",
        "RudRodNackNackType": "uetPdsNack.header.nackHeaderType.rudRodNack.nackType-6",
        "RudRodNackReserved1": "uetPdsNack.header.nackHeaderType.rudRodNack.reserved1-7",
        "RudRodNackNackCode": "uetPdsNack.header.nackHeaderType.rudRodNack.nackCode-8",
        "RudRodNackVendorCode": "uetPdsNack.header.nackHeaderType.rudRodNack.vendorCode-9",
        "RudRodNackNackPsnPktId": "uetPdsNack.header.nackHeaderType.rudRodNack.nackPsnPktId-10",
        "RudRodNackSpdcid": "uetPdsNack.header.nackHeaderType.rudRodNack.spdcid-11",
        "RudRodNackDpdcidValue": "uetPdsNack.header.nackHeaderType.rudRodNack.dpdcidValue-12",
        "RudRodNackPayload": "uetPdsNack.header.nackHeaderType.rudRodNack.payload-13",
        "RudiNackType": "uetPdsNack.header.nackHeaderType.rudiNack.type-14",
        "RudiNackNextHdr": "uetPdsNack.header.nackHeaderType.rudiNack.nextHdr-15",
        "RudiNackReserved": "uetPdsNack.header.nackHeaderType.rudiNack.reserved-16",
        "RudiNackMFlag": "uetPdsNack.header.nackHeaderType.rudiNack.mFlag-17",
        "RudiNackRetransmit": "uetPdsNack.header.nackHeaderType.rudiNack.retransmit-18",
        "RudiNackNackType": "uetPdsNack.header.nackHeaderType.rudiNack.nackType-19",
        "RudiNackReserved1": "uetPdsNack.header.nackHeaderType.rudiNack.reserved1-20",
        "RudiNackNackCode": "uetPdsNack.header.nackHeaderType.rudiNack.nackCode-21",
        "RudiNackVendorCode": "uetPdsNack.header.nackHeaderType.rudiNack.vendorCode-22",
        "RudiNackNackPsnPktId": "uetPdsNack.header.nackHeaderType.rudiNack.nackPsnPktId-23",
        "RudiNackSpdcid": "uetPdsNack.header.nackHeaderType.rudiNack.spdcid-24",
        "RudiNackDpdcidValue": "uetPdsNack.header.nackHeaderType.rudiNack.dpdcidValue-25",
        "RudiNackPayload": "uetPdsNack.header.nackHeaderType.rudiNack.payload-26",
        "RudRodNackCCXType": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.type-27",
        "RudRodNackCCXNextHdr": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.nextHdr-28",
        "RudRodNackCCXReserved": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.reserved-29",
        "RudRodNackCCXMFlag": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.mFlag-30",
        "RudRodNackCCXRetransmit": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.retransmit-31",
        "RudRodNackCCXNackType": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.nackType-32",
        "RudRodNackCCXReserved1": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.reserved1-33",
        "RudRodNackCCXNackCode": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.nackCode-34",
        "RudRodNackCCXVendorCode": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.vendorCode-35",
        "RudRodNackCCXNackPsnPktId": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.nackPsnPktId-36",
        "RudRodNackCCXSpdcid": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.spdcid-37",
        "RudRodNackCCXDpdcidValue": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.dpdcidValue-38",
        "RudRodNackCCXPayload": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.payload-39",
        "RudRodNackCCXNccxType": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.nccxType-40",
        "RudRodNackCCXNackCCXState": "uetPdsNack.header.nackHeaderType.rudRodNackCCX.nackCCXState-41",
        "RudiNackCCXType": "uetPdsNack.header.nackHeaderType.rudiNackCCX.type-42",
        "RudiNackCCXNextHdr": "uetPdsNack.header.nackHeaderType.rudiNackCCX.nextHdr-43",
        "RudiNackCCXReserved": "uetPdsNack.header.nackHeaderType.rudiNackCCX.reserved-44",
        "RudiNackCCXMFlag": "uetPdsNack.header.nackHeaderType.rudiNackCCX.mFlag-45",
        "RudiNackCCXRetransmit": "uetPdsNack.header.nackHeaderType.rudiNackCCX.retransmit-46",
        "RudiNackCCXNackType": "uetPdsNack.header.nackHeaderType.rudiNackCCX.nackType-47",
        "RudiNackCCXReserved1": "uetPdsNack.header.nackHeaderType.rudiNackCCX.reserved1-48",
        "RudiNackCCXNackCode": "uetPdsNack.header.nackHeaderType.rudiNackCCX.nackCode-49",
        "RudiNackCCXVendorCode": "uetPdsNack.header.nackHeaderType.rudiNackCCX.vendorCode-50",
        "RudiNackCCXNackPsnPktId": "uetPdsNack.header.nackHeaderType.rudiNackCCX.nackPsnPktId-51",
        "RudiNackCCXSpdcid": "uetPdsNack.header.nackHeaderType.rudiNackCCX.spdcid-52",
        "RudiNackCCXDpdcidValue": "uetPdsNack.header.nackHeaderType.rudiNackCCX.dpdcidValue-53",
        "RudiNackCCXPayload": "uetPdsNack.header.nackHeaderType.rudiNackCCX.payload-54",
        "RudiNackCCXNccxType": "uetPdsNack.header.nackHeaderType.rudiNackCCX.nccxType-55",
        "RudiNackCCXNackCCXState": "uetPdsNack.header.nackHeaderType.rudiNackCCX.nackCCXState-56",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsNack, self).__init__(parent, list_op)

    @property
    def RudRodNackType(self):
        """
        Display Name: Type
        Default Value: 10
        Value Format: decimal
        Available enum values: NACK, 10
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackType"])
        )

    @property
    def RudRodNackNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_HDR_NONE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackNextHdr"])
        )

    @property
    def RudRodNackReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackReserved"])
        )

    @property
    def RudRodNackMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackMFlag"])
        )

    @property
    def RudRodNackRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackRetransmit"])
        )

    @property
    def RudRodNackNackType(self):
        """
        Display Name: Nack Type (1-bit)
        Default Value: 0
        Value Format: decimal
        Available enum values: RUD_ROD_NACK, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackNackType"])
        )

    @property
    def RudRodNackReserved1(self):
        """
        Display Name: Reserved (3-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackReserved1"])
        )

    @property
    def RudRodNackNackCode(self):
        """
        Display Name: Nack Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_TRIMMED, 1, UET_TRIMMED_LASTHOP, 2, UET_TRIMMED_ACK, 3, UET_NO_PDC_AVAIL, 4, UET_NO_CCC_AVAIL, 5, UET_NO_BITMAP, 6, UET_NO_PKT_BUFFER, 7, UET_NO_GTD_DEL_AVAIL, 8, UET_NO_SES_MSG_AVAIL, 9, UET_NO_RESOURCE, 10, UET_PSN_OOR_WINDOW, 11, RESERVED, 12, UET_ROD_OOO, 13, UET_INV_DPDCID, 14, UET_PDC_HDR_MISMATCH, 15, UET_CLOSING, 16, UET_CLOSING_IN_ERR, 17, UET_PKT_NOT_RCVD, 18, UET_GTD_RESP_UNAVAIL, 19, UET_ACK_WITH_DATA, 20, UET_INVALID_SYN, 21, UET_PDC_MODE_MISMATCH, 22, UET_NEW_START_PSN, 23, UET_RCVD_SES_PROCG, 24, UET_UNEXP_EVENT, 25, UET_RCVR_INFER_LOSS, 26, RESERVED, 27, RESERVED, 252, UET_EXP_NACK_NORMAL, 253, UET_EXP_NACK_ERR, 254, UET_EXP_NACK_FATAL, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackNackCode"])
        )

    @property
    def RudRodNackVendorCode(self):
        """
        Display Name: Vendor Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackVendorCode"])
        )

    @property
    def RudRodNackNackPsnPktId(self):
        """
        Display Name: NACK_PSN / NACK_PKT_ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackNackPsnPktId"])
        )

    @property
    def RudRodNackSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackSpdcid"])
        )

    @property
    def RudRodNackDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackDpdcidValue"])
        )

    @property
    def RudRodNackPayload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackPayload"])
        )

    @property
    def RudiNackType(self):
        """
        Display Name: Type
        Default Value: 10
        Value Format: decimal
        Available enum values: NACK, 10
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RudiNackType"]))

    @property
    def RudiNackNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_HDR_NONE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackNextHdr"])
        )

    @property
    def RudiNackReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackReserved"])
        )

    @property
    def RudiNackMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RudiNackMFlag"]))

    @property
    def RudiNackRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackRetransmit"])
        )

    @property
    def RudiNackNackType(self):
        """
        Display Name: Nack Type (1-bit)
        Default Value: 1
        Value Format: decimal
        Available enum values: RUDI_NACK, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackNackType"])
        )

    @property
    def RudiNackReserved1(self):
        """
        Display Name: Reserved (3-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackReserved1"])
        )

    @property
    def RudiNackNackCode(self):
        """
        Display Name: Nack Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_TRIMMED, 1, UET_TRIMMED_LASTHOP, 2, UET_TRIMMED_ACK, 3, UET_NO_PDC_AVAIL, 4, UET_NO_CCC_AVAIL, 5, UET_NO_BITMAP, 6, UET_NO_PKT_BUFFER, 7, UET_NO_GTD_DEL_AVAIL, 8, UET_NO_SES_MSG_AVAIL, 9, UET_NO_RESOURCE, 10, UET_PSN_OOR_WINDOW, 11, RESERVED, 12, UET_ROD_OOO, 13, UET_INV_DPDCID, 14, UET_PDC_HDR_MISMATCH, 15, UET_CLOSING, 16, UET_CLOSING_IN_ERR, 17, UET_PKT_NOT_RCVD, 18, UET_GTD_RESP_UNAVAIL, 19, UET_ACK_WITH_DATA, 20, UET_INVALID_SYN, 21, UET_PDC_MODE_MISMATCH, 22, UET_NEW_START_PSN, 23, UET_RCVD_SES_PROCG, 24, UET_UNEXP_EVENT, 25, UET_RCVR_INFER_LOSS, 26, RESERVED, 27, RESERVED, 252, UET_EXP_NACK_NORMAL, 253, UET_EXP_NACK_ERR, 254, UET_EXP_NACK_FATAL, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackNackCode"])
        )

    @property
    def RudiNackVendorCode(self):
        """
        Display Name: Vendor Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackVendorCode"])
        )

    @property
    def RudiNackNackPsnPktId(self):
        """
        Display Name: NACK_PSN / NACK_PKT_ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackNackPsnPktId"])
        )

    @property
    def RudiNackSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackSpdcid"])
        )

    @property
    def RudiNackDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackDpdcidValue"])
        )

    @property
    def RudiNackPayload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackPayload"])
        )

    @property
    def RudRodNackCCXType(self):
        """
        Display Name: Type
        Default Value: 12
        Value Format: decimal
        Available enum values: NACK_CCX, 12
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXType"])
        )

    @property
    def RudRodNackCCXNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_HDR_NONE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXNextHdr"])
        )

    @property
    def RudRodNackCCXReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXReserved"])
        )

    @property
    def RudRodNackCCXMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXMFlag"])
        )

    @property
    def RudRodNackCCXRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXRetransmit"])
        )

    @property
    def RudRodNackCCXNackType(self):
        """
        Display Name: Nack Type (1-bit)
        Default Value: 0
        Value Format: decimal
        Available enum values: RUD_ROD_NACK_CCX, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXNackType"])
        )

    @property
    def RudRodNackCCXReserved1(self):
        """
        Display Name: Reserved (3-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXReserved1"])
        )

    @property
    def RudRodNackCCXNackCode(self):
        """
        Display Name: Nack Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_TRIMMED, 1, UET_TRIMMED_LASTHOP, 2, UET_TRIMMED_ACK, 3, UET_NO_PDC_AVAIL, 4, UET_NO_CCC_AVAIL, 5, UET_NO_BITMAP, 6, UET_NO_PKT_BUFFER, 7, UET_NO_GTD_DEL_AVAIL, 8, UET_NO_SES_MSG_AVAIL, 9, UET_NO_RESOURCE, 10, UET_PSN_OOR_WINDOW, 11, RESERVED, 12, UET_ROD_OOO, 13, UET_INV_DPDCID, 14, UET_PDC_HDR_MISMATCH, 15, UET_CLOSING, 16, UET_CLOSING_IN_ERR, 17, UET_PKT_NOT_RCVD, 18, UET_GTD_RESP_UNAVAIL, 19, UET_ACK_WITH_DATA, 20, UET_INVALID_SYN, 21, UET_PDC_MODE_MISMATCH, 22, UET_NEW_START_PSN, 23, UET_RCVD_SES_PROCG, 24, UET_UNEXP_EVENT, 25, UET_RCVR_INFER_LOSS, 26, RESERVED, 27, RESERVED, 252, UET_EXP_NACK_NORMAL, 253, UET_EXP_NACK_ERR, 254, UET_EXP_NACK_FATAL, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXNackCode"])
        )

    @property
    def RudRodNackCCXVendorCode(self):
        """
        Display Name: Vendor Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXVendorCode"])
        )

    @property
    def RudRodNackCCXNackPsnPktId(self):
        """
        Display Name: NACK_PSN / NACK_PKT_ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXNackPsnPktId"])
        )

    @property
    def RudRodNackCCXSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXSpdcid"])
        )

    @property
    def RudRodNackCCXDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXDpdcidValue"])
        )

    @property
    def RudRodNackCCXPayload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXPayload"])
        )

    @property
    def RudRodNackCCXNccxType(self):
        """
        Display Name: Nccx Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXNccxType"])
        )

    @property
    def RudRodNackCCXNackCCXState(self):
        """
        Display Name: NACK CCX State (124-bit)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodNackCCXNackCCXState"])
        )

    @property
    def RudiNackCCXType(self):
        """
        Display Name: Type
        Default Value: 12
        Value Format: decimal
        Available enum values: NACK_CCX, 12
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXType"])
        )

    @property
    def RudiNackCCXNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_HDR_NONE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXNextHdr"])
        )

    @property
    def RudiNackCCXReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXReserved"])
        )

    @property
    def RudiNackCCXMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXMFlag"])
        )

    @property
    def RudiNackCCXRetransmit(self):
        """
        Display Name: Retranmsit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXRetransmit"])
        )

    @property
    def RudiNackCCXNackType(self):
        """
        Display Name: Nack Type (1-bit)
        Default Value: 1
        Value Format: decimal
        Available enum values: RUDI_NACK_CCX, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXNackType"])
        )

    @property
    def RudiNackCCXReserved1(self):
        """
        Display Name: Reserved (3-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXReserved1"])
        )

    @property
    def RudiNackCCXNackCode(self):
        """
        Display Name: Nack Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_TRIMMED, 1, UET_TRIMMED_LASTHOP, 2, UET_TRIMMED_ACK, 3, UET_NO_PDC_AVAIL, 4, UET_NO_CCC_AVAIL, 5, UET_NO_BITMAP, 6, UET_NO_PKT_BUFFER, 7, UET_NO_GTD_DEL_AVAIL, 8, UET_NO_SES_MSG_AVAIL, 9, UET_NO_RESOURCE, 10, UET_PSN_OOR_WINDOW, 11, RESERVED, 12, UET_ROD_OOO, 13, UET_INV_DPDCID, 14, UET_PDC_HDR_MISMATCH, 15, UET_CLOSING, 16, UET_CLOSING_IN_ERR, 17, UET_PKT_NOT_RCVD, 18, UET_GTD_RESP_UNAVAIL, 19, UET_ACK_WITH_DATA, 20, UET_INVALID_SYN, 21, UET_PDC_MODE_MISMATCH, 22, UET_NEW_START_PSN, 23, UET_RCVD_SES_PROCG, 24, UET_UNEXP_EVENT, 25, UET_RCVR_INFER_LOSS, 26, RESERVED, 27, RESERVED, 252, UET_EXP_NACK_NORMAL, 253, UET_EXP_NACK_ERR, 254, UET_EXP_NACK_FATAL, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXNackCode"])
        )

    @property
    def RudiNackCCXVendorCode(self):
        """
        Display Name: Vendor Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXVendorCode"])
        )

    @property
    def RudiNackCCXNackPsnPktId(self):
        """
        Display Name: NACK_PSN / NACK_PKT_ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXNackPsnPktId"])
        )

    @property
    def RudiNackCCXSpdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXSpdcid"])
        )

    @property
    def RudiNackCCXDpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXDpdcidValue"])
        )

    @property
    def RudiNackCCXPayload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXPayload"])
        )

    @property
    def RudiNackCCXNccxType(self):
        """
        Display Name: Nccx Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXNccxType"])
        )

    @property
    def RudiNackCCXNackCCXState(self):
        """
        Display Name: NACK CCX State (124-bit)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiNackCCXNackCCXState"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
