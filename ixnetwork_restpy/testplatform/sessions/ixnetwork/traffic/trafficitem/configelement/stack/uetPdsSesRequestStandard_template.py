from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsSesRequestStandard(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsSesRequestStandard"
    _SDM_ATT_MAP = {
        "RudRodRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.type-1",
        "RudRodRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.nextHdr-2",
        "RudRodRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.reserved-3",
        "RudRodRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.retransmit-4",
        "RudRodRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.ackRequest-5",
        "SynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.synFlag-6",
        "SynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.reserved1-7",
        "SynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.clearPsnOffset-8",
        "SynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.pktSeqNo-9",
        "SynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.spdcid-10",
        "SynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.dpdcidValue-11",
        "SynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.synFlag-12",
        "SynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.reserved1-13",
        "SynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.clearPsnOffset-14",
        "SynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pktSeqNo-15",
        "SynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.spdcid-16",
        "SynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcInfo-17",
        "SynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcOffset-18",
        "SesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.reserved1-19",
        "SesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.opCode-20",
        "SesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.version-21",
        "SesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.deliveryComplete-22",
        "SesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.initiatorError-23",
        "SesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.relative-24",
        "SesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.headerDataPresent-25",
        "SesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.endOfMsg-26",
        "SesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.startOfMsg-27",
        "SesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.messageId-28",
        "SesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.riGeneration-29",
        "SesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.jobId-30",
        "SesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.Reserved2-31",
        "SesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.pidOnFEP-32",
        "SesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.Reserved3-33",
        "SesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.resourceIndex-34",
        "SesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.bufferOffset-35",
        "SesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.initiatorId-36",
        "SesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.matchBits-37",
        "SesHeaderHeaderData": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.headerData-38",
        "SesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequest.sesHeader.requestLength-39",
        "PdsheaderRudRodRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.type-40",
        "PdsheaderRudRodRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.nextHdr-41",
        "PdsheaderRudRodRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.reserved-42",
        "PdsheaderRudRodRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.retransmit-43",
        "PdsheaderRudRodRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.ackRequest-44",
        "SynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.synFlag-45",
        "SynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.reserved1-46",
        "SynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.clearPsnOffset-47",
        "SynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.pktSeqNo-48",
        "SynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.spdcid-49",
        "SynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.dpdcidValue-50",
        "SynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.synFlag-51",
        "SynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.reserved1-52",
        "SynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.clearPsnOffset-53",
        "SynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pktSeqNo-54",
        "SynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.spdcid-55",
        "SynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcInfo-56",
        "SynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcOffset-57",
        "Seswritesom0rudrodrequestSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.reserved1-58",
        "Seswritesom0rudrodrequestSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.opCode-59",
        "Seswritesom0rudrodrequestSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.version-60",
        "Seswritesom0rudrodrequestSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.deliveryComplete-61",
        "Seswritesom0rudrodrequestSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.initiatorError-62",
        "Seswritesom0rudrodrequestSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.relative-63",
        "Seswritesom0rudrodrequestSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.headerDataPresent-64",
        "Seswritesom0rudrodrequestSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.endOfMsg-65",
        "Seswritesom0rudrodrequestSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.startOfMsg-66",
        "Seswritesom0rudrodrequestSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.messageId-67",
        "Seswritesom0rudrodrequestSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.riGeneration-68",
        "Seswritesom0rudrodrequestSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.jobId-69",
        "Seswritesom0rudrodrequestSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.Reserved2-70",
        "Seswritesom0rudrodrequestSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.pidOnFEP-71",
        "Seswritesom0rudrodrequestSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.Reserved3-72",
        "Seswritesom0rudrodrequestSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.resourceIndex-73",
        "Seswritesom0rudrodrequestSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.bufferOffset-74",
        "Seswritesom0rudrodrequestSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.initiatorId-75",
        "Seswritesom0rudrodrequestSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.matchBits-76",
        "SesHeaderReserved4": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.Reserved4-77",
        "SesHeaderPayloadLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.payloadLength-78",
        "SesHeaderMessageOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.messageOffset-79",
        "Seswritesom0rudrodrequestSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequest.sesHeader.requestLength-80",
        "Sesreadsom1rudrodrequestPdsheaderRudRodRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.type-81",
        "Sesreadsom1rudrodrequestPdsheaderRudRodRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.nextHdr-82",
        "Sesreadsom1rudrodrequestPdsheaderRudRodRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.reserved-83",
        "Sesreadsom1rudrodrequestPdsheaderRudRodRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.retransmit-84",
        "Sesreadsom1rudrodrequestPdsheaderRudRodRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.ackRequest-85",
        "RudrodrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.synFlag-86",
        "RudrodrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.reserved1-87",
        "RudrodrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.clearPsnOffset-88",
        "RudrodrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.pktSeqNo-89",
        "RudrodrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.spdcid-90",
        "RudrodrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.dpdcidValue-91",
        "RudrodrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.synFlag-92",
        "RudrodrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.reserved1-93",
        "RudrodrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.clearPsnOffset-94",
        "RudrodrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pktSeqNo-95",
        "RudrodrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.spdcid-96",
        "RudrodrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcInfo-97",
        "RudrodrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcOffset-98",
        "Sesreadsom1rudrodrequestSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.reserved1-99",
        "Sesreadsom1rudrodrequestSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.opCode-100",
        "Sesreadsom1rudrodrequestSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.version-101",
        "Sesreadsom1rudrodrequestSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.deliveryComplete-102",
        "Sesreadsom1rudrodrequestSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.initiatorError-103",
        "Sesreadsom1rudrodrequestSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.relative-104",
        "Sesreadsom1rudrodrequestSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.headerDataPresent-105",
        "Sesreadsom1rudrodrequestSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.endOfMsg-106",
        "Sesreadsom1rudrodrequestSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.startOfMsg-107",
        "Sesreadsom1rudrodrequestSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.messageId-108",
        "Sesreadsom1rudrodrequestSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.riGeneration-109",
        "Sesreadsom1rudrodrequestSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.jobId-110",
        "Sesreadsom1rudrodrequestSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.Reserved2-111",
        "Sesreadsom1rudrodrequestSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.pidOnFEP-112",
        "Sesreadsom1rudrodrequestSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.Reserved3-113",
        "Sesreadsom1rudrodrequestSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.resourceIndex-114",
        "Sesreadsom1rudrodrequestSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.bufferOffset-115",
        "Sesreadsom1rudrodrequestSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.initiatorId-116",
        "Sesreadsom1rudrodrequestSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.matchBits-117",
        "Sesreadsom1rudrodrequestSesHeaderHeaderData": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.headerData-118",
        "Sesreadsom1rudrodrequestSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequest.sesHeader.requestLength-119",
        "Sesreadsom0rudrodrequestPdsheaderRudRodRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.type-120",
        "Sesreadsom0rudrodrequestPdsheaderRudRodRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.nextHdr-121",
        "Sesreadsom0rudrodrequestPdsheaderRudRodRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.reserved-122",
        "Sesreadsom0rudrodrequestPdsheaderRudRodRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.retransmit-123",
        "Sesreadsom0rudrodrequestPdsheaderRudRodRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.ackRequest-124",
        "PdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.synFlag-125",
        "PdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.reserved1-126",
        "PdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.clearPsnOffset-127",
        "PdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.pktSeqNo-128",
        "PdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.spdcid-129",
        "PdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.dpdcidValue-130",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.synFlag-131",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.reserved1-132",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.clearPsnOffset-133",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pktSeqNo-134",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.spdcid-135",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcInfo-136",
        "PdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcOffset-137",
        "Sesreadsom0rudrodrequestSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.reserved1-138",
        "Sesreadsom0rudrodrequestSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.opCode-139",
        "Sesreadsom0rudrodrequestSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.version-140",
        "Sesreadsom0rudrodrequestSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.deliveryComplete-141",
        "Sesreadsom0rudrodrequestSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.initiatorError-142",
        "Sesreadsom0rudrodrequestSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.relative-143",
        "Sesreadsom0rudrodrequestSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.headerDataPresent-144",
        "Sesreadsom0rudrodrequestSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.endOfMsg-145",
        "Sesreadsom0rudrodrequestSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.startOfMsg-146",
        "Sesreadsom0rudrodrequestSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.messageId-147",
        "Sesreadsom0rudrodrequestSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.riGeneration-148",
        "Sesreadsom0rudrodrequestSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.jobId-149",
        "Sesreadsom0rudrodrequestSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.Reserved2-150",
        "Sesreadsom0rudrodrequestSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.pidOnFEP-151",
        "Sesreadsom0rudrodrequestSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.Reserved3-152",
        "Sesreadsom0rudrodrequestSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.resourceIndex-153",
        "Sesreadsom0rudrodrequestSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.bufferOffset-154",
        "Sesreadsom0rudrodrequestSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.initiatorId-155",
        "Sesreadsom0rudrodrequestSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.matchBits-156",
        "Sesreadsom0rudrodrequestSesHeaderReserved4": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.Reserved4-157",
        "Sesreadsom0rudrodrequestSesHeaderPayloadLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.payloadLength-158",
        "Sesreadsom0rudrodrequestSesHeaderMessageOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.messageOffset-159",
        "Sesreadsom0rudrodrequestSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequest.sesHeader.requestLength-160",
        "Sessendsom1rudrodrequestPdsheaderRudRodRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.type-161",
        "Sessendsom1rudrodrequestPdsheaderRudRodRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.nextHdr-162",
        "Sessendsom1rudrodrequestPdsheaderRudRodRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.reserved-163",
        "Sessendsom1rudrodrequestPdsheaderRudRodRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.retransmit-164",
        "Sessendsom1rudrodrequestPdsheaderRudRodRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.ackRequest-165",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.synFlag-166",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.reserved1-167",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.clearPsnOffset-168",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.pktSeqNo-169",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.spdcid-170",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.dpdcidValue-171",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.synFlag-172",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.reserved1-173",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.clearPsnOffset-174",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pktSeqNo-175",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.spdcid-176",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcInfo-177",
        "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcOffset-178",
        "Sessendsom1rudrodrequestSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.reserved1-179",
        "Sessendsom1rudrodrequestSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.opCode-180",
        "Sessendsom1rudrodrequestSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.version-181",
        "Sessendsom1rudrodrequestSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.deliveryComplete-182",
        "Sessendsom1rudrodrequestSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.initiatorError-183",
        "Sessendsom1rudrodrequestSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.relative-184",
        "Sessendsom1rudrodrequestSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.headerDataPresent-185",
        "Sessendsom1rudrodrequestSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.endOfMsg-186",
        "Sessendsom1rudrodrequestSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.startOfMsg-187",
        "Sessendsom1rudrodrequestSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.messageId-188",
        "Sessendsom1rudrodrequestSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.riGeneration-189",
        "Sessendsom1rudrodrequestSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.jobId-190",
        "Sessendsom1rudrodrequestSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.Reserved2-191",
        "Sessendsom1rudrodrequestSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.pidOnFEP-192",
        "Sessendsom1rudrodrequestSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.Reserved3-193",
        "Sessendsom1rudrodrequestSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.resourceIndex-194",
        "Sessendsom1rudrodrequestSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.bufferOffset-195",
        "Sessendsom1rudrodrequestSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.initiatorId-196",
        "Sessendsom1rudrodrequestSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.matchBits-197",
        "Sessendsom1rudrodrequestSesHeaderHeaderData": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.headerData-198",
        "Sessendsom1rudrodrequestSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequest.sesHeader.requestLength-199",
        "Sessendsom0rudrodrequestPdsheaderRudRodRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.type-200",
        "Sessendsom0rudrodrequestPdsheaderRudRodRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.nextHdr-201",
        "Sessendsom0rudrodrequestPdsheaderRudRodRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.reserved-202",
        "Sessendsom0rudrodrequestPdsheaderRudRodRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.retransmit-203",
        "Sessendsom0rudrodrequestPdsheaderRudRodRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.ackRequest-204",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.synFlag-205",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.reserved1-206",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.clearPsnOffset-207",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.pktSeqNo-208",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.spdcid-209",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag0.dpdcidValue-210",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.synFlag-211",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.reserved1-212",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.clearPsnOffset-213",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pktSeqNo-214",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.spdcid-215",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcInfo-216",
        "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.pdsHeader.rudRodRequest.synRequestFlag.synFlag1.pdcOffset-217",
        "Sessendsom0rudrodrequestSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.reserved1-218",
        "Sessendsom0rudrodrequestSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.opCode-219",
        "Sessendsom0rudrodrequestSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.version-220",
        "Sessendsom0rudrodrequestSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.deliveryComplete-221",
        "Sessendsom0rudrodrequestSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.initiatorError-222",
        "Sessendsom0rudrodrequestSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.relative-223",
        "Sessendsom0rudrodrequestSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.headerDataPresent-224",
        "Sessendsom0rudrodrequestSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.endOfMsg-225",
        "Sessendsom0rudrodrequestSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.startOfMsg-226",
        "Sessendsom0rudrodrequestSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.messageId-227",
        "Sessendsom0rudrodrequestSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.riGeneration-228",
        "Sessendsom0rudrodrequestSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.jobId-229",
        "Sessendsom0rudrodrequestSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.Reserved2-230",
        "Sessendsom0rudrodrequestSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.pidOnFEP-231",
        "Sessendsom0rudrodrequestSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.Reserved3-232",
        "Sessendsom0rudrodrequestSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.resourceIndex-233",
        "Sessendsom0rudrodrequestSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.bufferOffset-234",
        "Sessendsom0rudrodrequestSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.initiatorId-235",
        "Sessendsom0rudrodrequestSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.matchBits-236",
        "Sessendsom0rudrodrequestSesHeaderReserved4": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.Reserved4-237",
        "Sessendsom0rudrodrequestSesHeaderPayloadLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.payloadLength-238",
        "Sessendsom0rudrodrequestSesHeaderMessageOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.messageOffset-239",
        "Sessendsom0rudrodrequestSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequest.sesHeader.requestLength-240",
        "RudRodCCRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.type-241",
        "RudRodCCRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.nextHdr-242",
        "RudRodCCRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.reserved-243",
        "RudRodCCRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.retransmit-244",
        "RudRodCCRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.ackRequest-245",
        "RudrodccrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.synFlag-246",
        "RudrodccrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.reserved1-247",
        "RudrodccrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.clearPsnOffset-248",
        "RudrodccrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.pktSeqNo-249",
        "RudrodccrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.spdcid-250",
        "RudrodccrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.dpdcidValue-251",
        "RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.cccId-252",
        "RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.creditTarget-253",
        "RudrodccrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.synFlag-254",
        "RudrodccrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.reserved1-255",
        "RudrodccrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.clearPsnOffset-256",
        "RudrodccrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pktSeqNo-257",
        "RudrodccrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.spdcid-258",
        "RudrodccrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcInfo-259",
        "RudrodccrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcOffset-260",
        "Synflag1RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.cccId-261",
        "Synflag1RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.creditTarget-262",
        "Seswritesom1rudrodrequestccSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.reserved1-263",
        "Seswritesom1rudrodrequestccSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.opCode-264",
        "Seswritesom1rudrodrequestccSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.version-265",
        "Seswritesom1rudrodrequestccSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.deliveryComplete-266",
        "Seswritesom1rudrodrequestccSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.initiatorError-267",
        "Seswritesom1rudrodrequestccSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.relative-268",
        "Seswritesom1rudrodrequestccSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.headerDataPresent-269",
        "Seswritesom1rudrodrequestccSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.endOfMsg-270",
        "Seswritesom1rudrodrequestccSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.startOfMsg-271",
        "Seswritesom1rudrodrequestccSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.messageId-272",
        "Seswritesom1rudrodrequestccSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.riGeneration-273",
        "Seswritesom1rudrodrequestccSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.jobId-274",
        "Seswritesom1rudrodrequestccSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.Reserved2-275",
        "Seswritesom1rudrodrequestccSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.pidOnFEP-276",
        "Seswritesom1rudrodrequestccSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.Reserved3-277",
        "Seswritesom1rudrodrequestccSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.resourceIndex-278",
        "Seswritesom1rudrodrequestccSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.bufferOffset-279",
        "Seswritesom1rudrodrequestccSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.initiatorId-280",
        "Seswritesom1rudrodrequestccSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.matchBits-281",
        "Seswritesom1rudrodrequestccSesHeaderHeaderData": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.headerData-282",
        "Seswritesom1rudrodrequestccSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom1RudRodRequestCC.sesHeader.requestLength-283",
        "PdsheaderRudRodCCRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.type-284",
        "PdsheaderRudRodCCRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.nextHdr-285",
        "PdsheaderRudRodCCRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.reserved-286",
        "PdsheaderRudRodCCRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.retransmit-287",
        "PdsheaderRudRodCCRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.ackRequest-288",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.synFlag-289",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.reserved1-290",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.clearPsnOffset-291",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.pktSeqNo-292",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.spdcid-293",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.dpdcidValue-294",
        "Synflag0RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.cccId-295",
        "Synflag0RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.creditTarget-296",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.synFlag-297",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.reserved1-298",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.clearPsnOffset-299",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pktSeqNo-300",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.spdcid-301",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcInfo-302",
        "PdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcOffset-303",
        "SynrequestflagSynflag1RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.cccId-304",
        "SynrequestflagSynflag1RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.creditTarget-305",
        "Seswritesom0rudrodrequestccSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.reserved1-306",
        "Seswritesom0rudrodrequestccSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.opCode-307",
        "Seswritesom0rudrodrequestccSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.version-308",
        "Seswritesom0rudrodrequestccSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.deliveryComplete-309",
        "Seswritesom0rudrodrequestccSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.initiatorError-310",
        "Seswritesom0rudrodrequestccSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.relative-311",
        "Seswritesom0rudrodrequestccSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.headerDataPresent-312",
        "Seswritesom0rudrodrequestccSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.endOfMsg-313",
        "Seswritesom0rudrodrequestccSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.startOfMsg-314",
        "Seswritesom0rudrodrequestccSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.messageId-315",
        "Seswritesom0rudrodrequestccSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.riGeneration-316",
        "Seswritesom0rudrodrequestccSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.jobId-317",
        "Seswritesom0rudrodrequestccSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.Reserved2-318",
        "Seswritesom0rudrodrequestccSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.pidOnFEP-319",
        "Seswritesom0rudrodrequestccSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.Reserved3-320",
        "Seswritesom0rudrodrequestccSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.resourceIndex-321",
        "Seswritesom0rudrodrequestccSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.bufferOffset-322",
        "Seswritesom0rudrodrequestccSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.initiatorId-323",
        "Seswritesom0rudrodrequestccSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.matchBits-324",
        "Seswritesom0rudrodrequestccSesHeaderReserved4": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.Reserved4-325",
        "Seswritesom0rudrodrequestccSesHeaderPayloadLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.payloadLength-326",
        "Seswritesom0rudrodrequestccSesHeaderMessageOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.messageOffset-327",
        "Seswritesom0rudrodrequestccSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesWriteSom0RudRodRequestCC.sesHeader.requestLength-328",
        "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.type-329",
        "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.nextHdr-330",
        "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.reserved-331",
        "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.retransmit-332",
        "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.ackRequest-333",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.synFlag-334",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.reserved1-335",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.clearPsnOffset-336",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.pktSeqNo-337",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.spdcid-338",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.dpdcidValue-339",
        "SynrequestflagSynflag0RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.cccId-340",
        "SynrequestflagSynflag0RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.creditTarget-341",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.synFlag-342",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.reserved1-343",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.clearPsnOffset-344",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pktSeqNo-345",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.spdcid-346",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcInfo-347",
        "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcOffset-348",
        "RudrodccrequestSynrequestflagSynflag1RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.cccId-349",
        "RudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.creditTarget-350",
        "Sesreadsom1rudrodrequestccSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.reserved1-351",
        "Sesreadsom1rudrodrequestccSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.opCode-352",
        "Sesreadsom1rudrodrequestccSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.version-353",
        "Sesreadsom1rudrodrequestccSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.deliveryComplete-354",
        "Sesreadsom1rudrodrequestccSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.initiatorError-355",
        "Sesreadsom1rudrodrequestccSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.relative-356",
        "Sesreadsom1rudrodrequestccSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.headerDataPresent-357",
        "Sesreadsom1rudrodrequestccSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.endOfMsg-358",
        "Sesreadsom1rudrodrequestccSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.startOfMsg-359",
        "Sesreadsom1rudrodrequestccSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.messageId-360",
        "Sesreadsom1rudrodrequestccSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.riGeneration-361",
        "Sesreadsom1rudrodrequestccSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.jobId-362",
        "Sesreadsom1rudrodrequestccSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.Reserved2-363",
        "Sesreadsom1rudrodrequestccSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.pidOnFEP-364",
        "Sesreadsom1rudrodrequestccSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.Reserved3-365",
        "Sesreadsom1rudrodrequestccSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.resourceIndex-366",
        "Sesreadsom1rudrodrequestccSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.bufferOffset-367",
        "Sesreadsom1rudrodrequestccSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.initiatorId-368",
        "Sesreadsom1rudrodrequestccSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.matchBits-369",
        "Sesreadsom1rudrodrequestccSesHeaderHeaderData": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.headerData-370",
        "Sesreadsom1rudrodrequestccSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom1RudRodRequestCC.sesHeader.requestLength-371",
        "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.type-372",
        "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.nextHdr-373",
        "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.reserved-374",
        "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.retransmit-375",
        "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.ackRequest-376",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.synFlag-377",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.reserved1-378",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.clearPsnOffset-379",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.pktSeqNo-380",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.spdcid-381",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.dpdcidValue-382",
        "RudrodccrequestSynrequestflagSynflag0RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.cccId-383",
        "RudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.creditTarget-384",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.synFlag-385",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.reserved1-386",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.clearPsnOffset-387",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pktSeqNo-388",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.spdcid-389",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcInfo-390",
        "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcOffset-391",
        "PdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.cccId-392",
        "PdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.creditTarget-393",
        "Sesreadsom0rudrodrequestccSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.reserved1-394",
        "Sesreadsom0rudrodrequestccSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.opCode-395",
        "Sesreadsom0rudrodrequestccSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.version-396",
        "Sesreadsom0rudrodrequestccSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.deliveryComplete-397",
        "Sesreadsom0rudrodrequestccSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.initiatorError-398",
        "Sesreadsom0rudrodrequestccSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.relative-399",
        "Sesreadsom0rudrodrequestccSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.headerDataPresent-400",
        "Sesreadsom0rudrodrequestccSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.endOfMsg-401",
        "Sesreadsom0rudrodrequestccSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.startOfMsg-402",
        "Sesreadsom0rudrodrequestccSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.messageId-403",
        "Sesreadsom0rudrodrequestccSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.riGeneration-404",
        "Sesreadsom0rudrodrequestccSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.jobId-405",
        "Sesreadsom0rudrodrequestccSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.Reserved2-406",
        "Sesreadsom0rudrodrequestccSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.pidOnFEP-407",
        "Sesreadsom0rudrodrequestccSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.Reserved3-408",
        "Sesreadsom0rudrodrequestccSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.resourceIndex-409",
        "Sesreadsom0rudrodrequestccSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.bufferOffset-410",
        "Sesreadsom0rudrodrequestccSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.initiatorId-411",
        "Sesreadsom0rudrodrequestccSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.matchBits-412",
        "Sesreadsom0rudrodrequestccSesHeaderReserved4": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.Reserved4-413",
        "Sesreadsom0rudrodrequestccSesHeaderPayloadLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.payloadLength-414",
        "Sesreadsom0rudrodrequestccSesHeaderMessageOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.messageOffset-415",
        "Sesreadsom0rudrodrequestccSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesReadSom0RudRodRequestCC.sesHeader.requestLength-416",
        "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.type-417",
        "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.nextHdr-418",
        "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.reserved-419",
        "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.retransmit-420",
        "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.ackRequest-421",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.synFlag-422",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.reserved1-423",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.clearPsnOffset-424",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.pktSeqNo-425",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.spdcid-426",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.dpdcidValue-427",
        "PdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.cccId-428",
        "PdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.creditTarget-429",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.synFlag-430",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.reserved1-431",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.clearPsnOffset-432",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pktSeqNo-433",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.spdcid-434",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcInfo-435",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcOffset-436",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.cccId-437",
        "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.creditTarget-438",
        "Sessendsom1rudrodrequestccSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.reserved1-439",
        "Sessendsom1rudrodrequestccSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.opCode-440",
        "Sessendsom1rudrodrequestccSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.version-441",
        "Sessendsom1rudrodrequestccSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.deliveryComplete-442",
        "Sessendsom1rudrodrequestccSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.initiatorError-443",
        "Sessendsom1rudrodrequestccSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.relative-444",
        "Sessendsom1rudrodrequestccSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.headerDataPresent-445",
        "Sessendsom1rudrodrequestccSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.endOfMsg-446",
        "Sessendsom1rudrodrequestccSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.startOfMsg-447",
        "Sessendsom1rudrodrequestccSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.messageId-448",
        "Sessendsom1rudrodrequestccSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.riGeneration-449",
        "Sessendsom1rudrodrequestccSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.jobId-450",
        "Sessendsom1rudrodrequestccSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.Reserved2-451",
        "Sessendsom1rudrodrequestccSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.pidOnFEP-452",
        "Sessendsom1rudrodrequestccSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.Reserved3-453",
        "Sessendsom1rudrodrequestccSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.resourceIndex-454",
        "Sessendsom1rudrodrequestccSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.bufferOffset-455",
        "Sessendsom1rudrodrequestccSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.initiatorId-456",
        "Sessendsom1rudrodrequestccSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.matchBits-457",
        "Sessendsom1rudrodrequestccSesHeaderHeaderData": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.headerData-458",
        "Sessendsom1rudrodrequestccSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom1RudRodRequestCC.sesHeader.requestLength-459",
        "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestType": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.type-460",
        "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestNextHdr": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.nextHdr-461",
        "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestReserved": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.reserved-462",
        "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestRetransmit": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.retransmit-463",
        "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestAckRequest": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.ackRequest-464",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.synFlag-465",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.reserved1-466",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.clearPsnOffset-467",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.pktSeqNo-468",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.spdcid-469",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.dpdcidValue-470",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.cccId-471",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag0.requestCCState.creditTarget-472",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.synFlag-473",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.reserved1-474",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.clearPsnOffset-475",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pktSeqNo-476",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.spdcid-477",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcInfo-478",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.pdcOffset-479",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.cccId-480",
        "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.pdsHeader.rudRodCCRequest.synRequestFlag.synFlag1.requestCCState.creditTarget-481",
        "Sessendsom0rudrodrequestccSesHeaderReserved1": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.reserved1-482",
        "Sessendsom0rudrodrequestccSesHeaderOpCode": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.opCode-483",
        "Sessendsom0rudrodrequestccSesHeaderVersion": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.version-484",
        "Sessendsom0rudrodrequestccSesHeaderDeliveryComplete": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.deliveryComplete-485",
        "Sessendsom0rudrodrequestccSesHeaderInitiatorError": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.initiatorError-486",
        "Sessendsom0rudrodrequestccSesHeaderRelative": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.relative-487",
        "Sessendsom0rudrodrequestccSesHeaderHeaderDataPresent": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.headerDataPresent-488",
        "Sessendsom0rudrodrequestccSesHeaderEndOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.endOfMsg-489",
        "Sessendsom0rudrodrequestccSesHeaderStartOfMsg": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.startOfMsg-490",
        "Sessendsom0rudrodrequestccSesHeaderMessageId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.messageId-491",
        "Sessendsom0rudrodrequestccSesHeaderRiGeneration": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.riGeneration-492",
        "Sessendsom0rudrodrequestccSesHeaderJobId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.jobId-493",
        "Sessendsom0rudrodrequestccSesHeaderReserved2": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.Reserved2-494",
        "Sessendsom0rudrodrequestccSesHeaderPidOnFEP": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.pidOnFEP-495",
        "Sessendsom0rudrodrequestccSesHeaderReserved3": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.Reserved3-496",
        "Sessendsom0rudrodrequestccSesHeaderResourceIndex": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.resourceIndex-497",
        "Sessendsom0rudrodrequestccSesHeaderBufferOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.bufferOffset-498",
        "Sessendsom0rudrodrequestccSesHeaderInitiatorId": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.initiatorId-499",
        "Sessendsom0rudrodrequestccSesHeaderMatchBits": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.matchBits-500",
        "Sessendsom0rudrodrequestccSesHeaderReserved4": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.Reserved4-501",
        "Sessendsom0rudrodrequestccSesHeaderPayloadLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.payloadLength-502",
        "Sessendsom0rudrodrequestccSesHeaderMessageOffset": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.messageOffset-503",
        "Sessendsom0rudrodrequestccSesHeaderRequestLength": "uetPdsSesRequestStandard.header.requestHeaderType.sesSendSom0RudRodRequestCC.sesHeader.requestLength-504",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsSesRequestStandard, self).__init__(parent, list_op)

    @property
    def RudRodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: RUD_REQ, 2, ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodRequestType"])
        )

    @property
    def RudRodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodRequestNextHdr"])
        )

    @property
    def RudRodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodRequestReserved"])
        )

    @property
    def RudRodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodRequestRetransmit"])
        )

    @property
    def RudRodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodRequestAckRequest"])
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
    def SesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderReserved1"])
        )

    @property
    def SesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_WRITE, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderOpCode"])
        )

    @property
    def SesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderVersion"])
        )

    @property
    def SesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderDeliveryComplete"])
        )

    @property
    def SesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderInitiatorError"])
        )

    @property
    def SesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderRelative"])
        )

    @property
    def SesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderHeaderDataPresent"])
        )

    @property
    def SesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderEndOfMsg"])
        )

    @property
    def SesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderStartOfMsg"])
        )

    @property
    def SesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderMessageId"])
        )

    @property
    def SesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderRiGeneration"])
        )

    @property
    def SesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderJobId"])
        )

    @property
    def SesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderReserved2"])
        )

    @property
    def SesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderPidOnFEP"])
        )

    @property
    def SesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderReserved3"])
        )

    @property
    def SesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderResourceIndex"])
        )

    @property
    def SesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderBufferOffset"])
        )

    @property
    def SesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderInitiatorId"])
        )

    @property
    def SesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderMatchBits"])
        )

    @property
    def SesHeaderHeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderHeaderData"])
        )

    @property
    def SesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderRequestLength"])
        )

    @property
    def PdsheaderRudRodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: RUD_REQ, 2, ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodRequestType"])
        )

    @property
    def PdsheaderRudRodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodRequestNextHdr"]),
        )

    @property
    def PdsheaderRudRodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodRequestReserved"]),
        )

    @property
    def PdsheaderRudRodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodRequestRetransmit"]),
        )

    @property
    def PdsheaderRudRodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodRequestAckRequest"]),
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
    def Seswritesom0rudrodrequestSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderReserved1"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_WRITE, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderOpCode"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderVersion"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderInitiatorError"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderRelative"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderHeaderDataPresent"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderMessageId"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderRiGeneration"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderJobId"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderReserved2"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderReserved3"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderResourceIndex"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderBufferOffset"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderInitiatorId"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderMatchBits"]
            ),
        )

    @property
    def SesHeaderReserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderReserved4"])
        )

    @property
    def SesHeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderPayloadLength"])
        )

    @property
    def SesHeaderMessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesHeaderMessageOffset"])
        )

    @property
    def Seswritesom0rudrodrequestSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestSesHeaderRequestLength"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestPdsheaderRudRodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: RUD_REQ, 2, ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestPdsheaderRudRodRequestType"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestPdsheaderRudRodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestPdsheaderRudRodRequestNextHdr"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestPdsheaderRudRodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestPdsheaderRudRodRequestReserved"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestPdsheaderRudRodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestPdsheaderRudRodRequestRetransmit"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestPdsheaderRudRodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestPdsheaderRudRodRequestAckRequest"
                ]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag0ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag0ClearPsnOffset"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1ClearPsnOffset"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def RudrodrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodrequestSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderReserved1"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 2
        Value Format: decimal
        Available enum values: UET_READ, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderOpCode"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderVersion"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderRelative"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderHeaderDataPresent"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderMessageId"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderJobId"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderReserved2"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderReserved3"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderMatchBits"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderHeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderHeaderData"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestSesHeaderRequestLength"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestPdsheaderRudRodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: RUD_REQ, 2, ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestPdsheaderRudRodRequestType"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestPdsheaderRudRodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestPdsheaderRudRodRequestNextHdr"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestPdsheaderRudRodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestPdsheaderRudRodRequestReserved"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestPdsheaderRudRodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestPdsheaderRudRodRequestRetransmit"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestPdsheaderRudRodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestPdsheaderRudRodRequestAckRequest"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset(self):
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
                    "PdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset(self):
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
                    "PdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def PdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderReserved1"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 2
        Value Format: decimal
        Available enum values: UET_READ, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderOpCode"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderVersion"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderRelative"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderHeaderDataPresent"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderMessageId"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderJobId"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderReserved2"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderReserved3"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderMatchBits"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderReserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderReserved4"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderPayloadLength"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderMessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderMessageOffset"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestSesHeaderRequestLength"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudRodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: RUD_REQ, 2, ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestPdsheaderRudRodRequestType"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudRodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudRodRequestNextHdr"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudRodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudRodRequestReserved"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudRodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudRodRequestRetransmit"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudRodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudRodRequestAckRequest"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue(
        self,
    ):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo(
        self,
    ):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset(
        self,
    ):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderReserved1"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 5
        Value Format: decimal
        Available enum values: UET_SEND, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderOpCode"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderVersion"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderRelative"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderHeaderDataPresent"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderMessageId"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderJobId"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderReserved2"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderReserved3"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderMatchBits"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderHeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderHeaderData"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestSesHeaderRequestLength"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudRodRequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        Available enum values: RUD_REQ, 2, ROD_REQ, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestPdsheaderRudRodRequestType"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudRodRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudRodRequestNextHdr"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudRodRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudRodRequestReserved"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudRodRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudRodRequestRetransmit"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudRodRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudRodRequestAckRequest"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue(
        self,
    ):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo(
        self,
    ):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset(
        self,
    ):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestPdsheaderRudrodrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderReserved1"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 5
        Value Format: decimal
        Available enum values: UET_SEND, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderOpCode"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderVersion"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderRelative"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderHeaderDataPresent"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderMessageId"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderJobId"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderReserved2"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderReserved3"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderMatchBits"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderReserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderReserved4"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderPayloadLength"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderMessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderMessageOffset"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestSesHeaderRequestLength"]
            ),
        )

    @property
    def RudRodCCRequestType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13, ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodCCRequestType"])
        )

    @property
    def RudRodCCRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodCCRequestNextHdr"])
        )

    @property
    def RudRodCCRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodCCRequestReserved"])
        )

    @property
    def RudRodCCRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodCCRequestRetransmit"])
        )

    @property
    def RudRodCCRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudRodCCRequestAckRequest"])
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag0ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag0ClearPsnOffset"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag0DpdcidValue"]
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
    def RudrodccrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag1ClearPsnOffset(self):
        """
        Display Name: Clear PSN Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1ClearPsnOffset"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RudrodccrequestSynrequestflagSynFlag1PdcOffset"]
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
    def Seswritesom1rudrodrequestccSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderReserved1"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_WRITE, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderOpCode"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderVersion"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Seswritesom1rudrodrequestccSesHeaderDeliveryComplete"
                ]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderInitiatorError"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderRelative"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Seswritesom1rudrodrequestccSesHeaderHeaderDataPresent"
                ]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderMessageId"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderRiGeneration"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderJobId"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderReserved2"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderReserved3"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderResourceIndex"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderBufferOffset"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderInitiatorId"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderMatchBits"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderHeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderHeaderData"]
            ),
        )

    @property
    def Seswritesom1rudrodrequestccSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom1rudrodrequestccSesHeaderRequestLength"]
            ),
        )

    @property
    def PdsheaderRudRodCCRequestType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13, ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodCCRequestType"])
        )

    @property
    def PdsheaderRudRodCCRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodCCRequestNextHdr"]),
        )

    @property
    def PdsheaderRudRodCCRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PdsheaderRudRodCCRequestReserved"]),
        )

    @property
    def PdsheaderRudRodCCRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudRodCCRequestRetransmit"]
            ),
        )

    @property
    def PdsheaderRudRodCCRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PdsheaderRudRodCCRequestAckRequest"]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset(self):
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
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue"
                ]
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
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset(self):
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
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset"
                ]
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

    @property
    def Seswritesom0rudrodrequestccSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderReserved1"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_WRITE, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderOpCode"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderVersion"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Seswritesom0rudrodrequestccSesHeaderDeliveryComplete"
                ]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderInitiatorError"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderRelative"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Seswritesom0rudrodrequestccSesHeaderHeaderDataPresent"
                ]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderMessageId"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderRiGeneration"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderJobId"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderReserved2"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderReserved3"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderResourceIndex"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderBufferOffset"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderInitiatorId"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderMatchBits"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderReserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderReserved4"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderPayloadLength"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderMessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderMessageOffset"]
            ),
        )

    @property
    def Seswritesom0rudrodrequestccSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Seswritesom0rudrodrequestccSesHeaderRequestLength"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13, ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestType"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestNextHdr"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestReserved"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestRetransmit"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudRodCCRequestAckRequest"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset(
        self,
    ):
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
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue(
        self,
    ):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def SynrequestflagSynflag0RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynflag0RequestCCStateCccId"]
            ),
        )

    @property
    def SynrequestflagSynflag0RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynflag0RequestCCStateCreditTarget"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset(
        self,
    ):
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
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo(
        self,
    ):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset(
        self,
    ):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynflag1RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "RudrodccrequestSynrequestflagSynflag1RequestCCStateCccId"
                ]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "RudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderReserved1"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 2
        Value Format: decimal
        Available enum values: UET_READ, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderOpCode"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderVersion"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderRelative"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom1rudrodrequestccSesHeaderHeaderDataPresent"
                ]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderMessageId"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderJobId"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderReserved2"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderReserved3"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderMatchBits"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderHeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderHeaderData"]
            ),
        )

    @property
    def Sesreadsom1rudrodrequestccSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom1rudrodrequestccSesHeaderRequestLength"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13, ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestType"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestNextHdr"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestReserved"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestRetransmit"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudRodCCRequestAckRequest"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset(
        self,
    ):
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
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue(
        self,
    ):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynflag0RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "RudrodccrequestSynrequestflagSynflag0RequestCCStateCccId"
                ]
            ),
        )

    @property
    def RudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "RudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset(
        self,
    ):
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
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo(
        self,
    ):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset(
        self,
    ):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderReserved1"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 2
        Value Format: decimal
        Available enum values: UET_READ, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderOpCode"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderVersion"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderRelative"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sesreadsom0rudrodrequestccSesHeaderHeaderDataPresent"
                ]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderMessageId"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderJobId"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderReserved2"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderReserved3"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderMatchBits"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderReserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderReserved4"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderPayloadLength"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderMessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderMessageOffset"]
            ),
        )

    @property
    def Sesreadsom0rudrodrequestccSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sesreadsom0rudrodrequestccSesHeaderRequestLength"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13, ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestType"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestNextHdr"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestReserved"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestRetransmit"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudRodCCRequestAckRequest"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue(
        self,
    ):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCccId(self):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCccId"
                ]
            ),
        )

    @property
    def PdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget(self):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo(
        self,
    ):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset(
        self,
    ):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId(
        self,
    ):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget(
        self,
    ):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderReserved1"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 5
        Value Format: decimal
        Available enum values: UET_SEND, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderOpCode"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderVersion"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderRelative"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom1rudrodrequestccSesHeaderHeaderDataPresent"
                ]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderMessageId"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderJobId"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderReserved2"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderReserved3"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderMatchBits"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderHeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderHeaderData"]
            ),
        )

    @property
    def Sessendsom1rudrodrequestccSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom1rudrodrequestccSesHeaderRequestLength"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestType(self):
        """
        Display Name: Type
        Default Value: 14
        Value Format: decimal
        Available enum values: RUD_CC_REQ, 13, ROD_CC_REQ, 14
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestType"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestNextHdr"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestReserved"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestRetransmit"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudRodCCRequestAckRequest"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue(
        self,
    ):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCccId(
        self,
    ):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCccId"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget(
        self,
    ):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag0RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag(
        self,
    ):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1(
        self,
    ):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset(
        self,
    ):
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
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1ClearPsnOffset"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo(
        self,
    ):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid(
        self,
    ):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo(
        self,
    ):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset(
        self,
    ):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId(
        self,
    ):
        """
        Display Name: CCC Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCccId"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget(
        self,
    ):
        """
        Display Name: Credit Target
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccPdsheaderRudrodccrequestSynrequestflagSynflag1RequestCCStateCreditTarget"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderReserved1"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderOpCode(self):
        """
        Display Name: Op Code
        Default Value: 5
        Value Format: decimal
        Available enum values: UET_SEND, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderOpCode"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderVersion"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderDeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderDeliveryComplete"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderInitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderInitiatorError"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderRelative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderRelative"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderHeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Sessendsom0rudrodrequestccSesHeaderHeaderDataPresent"
                ]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderEndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderEndOfMsg"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderStartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderStartOfMsg"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderMessageId"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderRiGeneration"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderJobId"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderReserved2"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderPidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderPidOnFEP"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderReserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderReserved3"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderResourceIndex"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderBufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderBufferOffset"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderInitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderInitiatorId"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderMatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderMatchBits"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderReserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderReserved4"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderPayloadLength"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderMessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderMessageOffset"]
            ),
        )

    @property
    def Sessendsom0rudrodrequestccSesHeaderRequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sessendsom0rudrodrequestccSesHeaderRequestLength"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
