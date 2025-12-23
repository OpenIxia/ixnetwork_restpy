from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsRudRodSRequest(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsRudRodSRequest"
    _SDM_ATT_MAP = {
        "RudRequestType": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.type-1",
        "RudRequestNextHdr": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.nextHdr-2",
        "RudRequestReserved": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.reserved-3",
        "RudRequestRetransmit": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.retransmit-4",
        "RudRequestAckRequest": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.ackRequest-5",
        "SynFlag0SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag0.synFlag-6",
        "SynFlag0Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag0.reserved1-7",
        "SynFlag0ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag0.clearPsnOffset-8",
        "SynFlag0PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag0.pktSeqNo-9",
        "SynFlag0Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag0.spdcid-10",
        "SynFlag0DpdcidValue": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag0.dpdcidValue-11",
        "SynFlag1SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.synFlag-12",
        "SynFlag1Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.reserved1-13",
        "SynFlag1ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.clearPsnOffset-14",
        "SynFlag1PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.pktSeqNo-15",
        "SynFlag1Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.spdcid-16",
        "SynFlag1PdcInfo": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.pdcInfo-17",
        "SynFlag1PdcOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequest.synRequestFlag.synFlag1.pdcOffset-18",
        "RodRequestType": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.type-19",
        "RodRequestNextHdr": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.nextHdr-20",
        "RodRequestReserved": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.reserved-21",
        "RodRequestRetransmit": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.retransmit-22",
        "RodRequestAckRequest": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.ackRequest-23",
        "SynrequestflagSynFlag0SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag0.synFlag-24",
        "SynrequestflagSynFlag0Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag0.reserved1-25",
        "SynrequestflagSynFlag0ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag0.clearPsnOffset-26",
        "SynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag0.pktSeqNo-27",
        "SynrequestflagSynFlag0Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag0.spdcid-28",
        "SynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag0.dpdcidValue-29",
        "SynrequestflagSynFlag1SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.synFlag-30",
        "SynrequestflagSynFlag1Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.reserved1-31",
        "SynrequestflagSynFlag1ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.clearPsnOffset-32",
        "SynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.pktSeqNo-33",
        "SynrequestflagSynFlag1Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.spdcid-34",
        "SynrequestflagSynFlag1PdcInfo": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.pdcInfo-35",
        "SynrequestflagSynFlag1PdcOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequest.synRequestFlag.synFlag1.pdcOffset-36",
        "RudRequestWithCCType": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.type-37",
        "RudRequestWithCCNextHdr": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.nextHdr-38",
        "RudRequestWithCCReserved": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.reserved-39",
        "RudRequestWithCCRetransmit": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.retransmit-40",
        "RudRequestWithCCAckRequest": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.ackRequest-41",
        "RudrequestwithccSynrequestflagSynFlag0SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.synFlag-42",
        "RudrequestwithccSynrequestflagSynFlag0Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.reserved1-43",
        "RudrequestwithccSynrequestflagSynFlag0ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.clearPsnOffset-44",
        "RudrequestwithccSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.pktSeqNo-45",
        "RudrequestwithccSynrequestflagSynFlag0Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.spdcid-46",
        "RudrequestwithccSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.dpdcidValue-47",
        "RequestCCStateCccId": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.requestCCState.cccId-48",
        "RequestCCStateCreditTarget": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag0.requestCCState.creditTarget-49",
        "RudrequestwithccSynrequestflagSynFlag1SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.synFlag-50",
        "RudrequestwithccSynrequestflagSynFlag1Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.reserved1-51",
        "RudrequestwithccSynrequestflagSynFlag1ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.clearPsnOffset-52",
        "RudrequestwithccSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.pktSeqNo-53",
        "RudrequestwithccSynrequestflagSynFlag1Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.spdcid-54",
        "RudrequestwithccSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.pdcInfo-55",
        "RudrequestwithccSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.pdcOffset-56",
        "Synflag1RequestCCStateCccId": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.requestCCState.cccId-57",
        "Synflag1RequestCCStateCreditTarget": "uetPdsRudRodSRequest.header.requestHeaderType.rudRequestWithCC.synRequestFlag.synFlag1.requestCCState.creditTarget-58",
        "RodRequestCCType": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.type-59",
        "RodRequestCCNextHdr": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.nextHdr-60",
        "RodRequestCCReserved": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.reserved-61",
        "RodRequestCCRetransmit": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.retransmit-62",
        "RodRequestCCAckRequest": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.ackRequest-63",
        "RodrequestccSynrequestflagSynFlag0SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.synFlag-64",
        "RodrequestccSynrequestflagSynFlag0Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.reserved1-65",
        "RodrequestccSynrequestflagSynFlag0ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.clearPsnOffset-66",
        "RodrequestccSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.pktSeqNo-67",
        "RodrequestccSynrequestflagSynFlag0Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.spdcid-68",
        "RodrequestccSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.dpdcidValue-69",
        "Synflag0RequestCCStateCccId": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.requestCCState.cccId-70",
        "Synflag0RequestCCStateCreditTarget": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag0.requestCCState.creditTarget-71",
        "RodrequestccSynrequestflagSynFlag1SynFlag": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.synFlag-72",
        "RodrequestccSynrequestflagSynFlag1Reserved1": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.reserved1-73",
        "RodrequestccSynrequestflagSynFlag1ClearPsnOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.clearPsnOffset-74",
        "RodrequestccSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.pktSeqNo-75",
        "RodrequestccSynrequestflagSynFlag1Spdcid": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.spdcid-76",
        "RodrequestccSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.pdcInfo-77",
        "RodrequestccSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.pdcOffset-78",
        "SynrequestflagSynflag1RequestCCStateCccId": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.requestCCState.cccId-79",
        "SynrequestflagSynflag1RequestCCStateCreditTarget": "uetPdsRudRodSRequest.header.requestHeaderType.rodRequestCC.synRequestFlag.synFlag1.requestCCState.creditTarget-80",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsRudRodSRequest, self).__init__(parent, list_op)

    @property
    def RudRequestType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        Available enum values: RUD_REQ, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestType"])
        )

    @property
    def RudRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestNextHdr"])
        )

    @property
    def RudRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestReserved"])
        )

    @property
    def RudRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestRetransmit"])
        )

    @property
    def RudRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestAckRequest"])
        )

    @property
    def SynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0SynFlag"])
        )

    @property
    def SynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0Reserved1"])
        )

    @property
    def SynFlag0ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0ClearPsnOffset"])
        )

    @property
    def SynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0PktSeqNo"])
        )

    @property
    def SynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0Spdcid"])
        )

    @property
    def SynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0DpdcidValue"])
        )

    @property
    def SynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1SynFlag"])
        )

    @property
    def SynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1Reserved1"])
        )

    @property
    def SynFlag1ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1ClearPsnOffset"])
        )

    @property
    def SynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PktSeqNo"])
        )

    @property
    def SynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1Spdcid"])
        )

    @property
    def SynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PdcInfo"])
        )

    @property
    def SynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PdcOffset"])
        )

    @property
    def RodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestType"])
        )

    @property
    def RodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestNextHdr"])
        )

    @property
    def RodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestReserved"])
        )

    @property
    def RodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestRetransmit"])
        )

    @property
    def RodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestAckRequest"])
        )

    @property
    def SynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0SynFlag"]),
        )

    @property
    def SynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0Reserved1"]),
        )

    @property
    def SynrequestflagSynFlag0ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag0ClearPsnOffset"]
            ),
        )

    @property
    def SynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0PktSeqNo"]),
        )

    @property
    def SynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0Spdcid"])
        )

    @property
    def SynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0DpdcidValue"]),
        )

    @property
    def SynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1SynFlag"]),
        )

    @property
    def SynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1Reserved1"]),
        )

    @property
    def SynrequestflagSynFlag1ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag1ClearPsnOffset"]
            ),
        )

    @property
    def SynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1PktSeqNo"]),
        )

    @property
    def SynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1Spdcid"])
        )

    @property
    def SynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1PdcInfo"]),
        )

    @property
    def SynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1PdcOffset"]),
        )

    @property
    def RudRequestWithCCType(self):
        """
        Display Name: Type
        Default Value: 13
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestWithCCType"])
        )

    @property
    def RudRequestWithCCNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestWithCCNextHdr"])
        )

    @property
    def RudRequestWithCCReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestWithCCReserved"])
        )

    @property
    def RudRequestWithCCRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestWithCCRetransmit"])
        )

    @property
    def RudRequestWithCCAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRequestWithCCAckRequest"])
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag0ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "RudrequestwithccSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestCCStateCccId"])
        )

    @property
    def RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestCCStateCreditTarget"])
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "RudrequestwithccSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def RudrequestwithccSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrequestwithccSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def Synflag1RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Synflag1RequestCCStateCccId"])
        )

    @property
    def Synflag1RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Synflag1RequestCCStateCreditTarget"]
            ),
        )

    @property
    def RodRequestCCType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestCCType"])
        )

    @property
    def RodRequestCCNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestCCNextHdr"])
        )

    @property
    def RodRequestCCReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestCCReserved"])
        )

    @property
    def RodRequestCCRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestCCRetransmit"])
        )

    @property
    def RodRequestCCAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RodRequestCCAckRequest"])
        )

    @property
    def RodrequestccSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag0ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag0ClearPsnOffset"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def Synflag0RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Synflag0RequestCCStateCccId"])
        )

    @property
    def Synflag0RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Synflag0RequestCCStateCreditTarget"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1ClearPsnOffset"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def RodrequestccSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RodrequestccSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def SynrequestflagSynflag1RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynflag1RequestCCStateCccId"]
            ),
        )

    @property
    def SynrequestflagSynflag1RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynflag1RequestCCStateCreditTarget"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
