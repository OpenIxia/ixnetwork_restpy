from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsRudRodCP(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsRudRodCP"
    _SDM_ATT_MAP = {
        "NoOPType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.type-1",
        "NoOPControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.controlType-2",
        "NoOPReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.reserved-3",
        "NoOPIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.isRod-4",
        "NoOPRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.retransmit-5",
        "NoOPAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.ackRequest-6",
        "SynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.synFlag-7",
        "SynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.reserved1-8",
        "SynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.probeOpaque-9",
        "SynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.pktSeqNo-10",
        "SynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.spdcid-11",
        "SynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.dpdcidValue-12",
        "SynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag0.payload-13",
        "SynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.synFlag-14",
        "SynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.reserved1-15",
        "SynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.probeOpaque-16",
        "SynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.pktSeqNo-17",
        "SynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.spdcid-18",
        "SynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.pdcInfo-19",
        "SynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.pdcOffset-20",
        "SynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.noOP.synRequestFlag.synFlag1.payload-21",
        "AckRequestType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.type-22",
        "AckRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.controlType-23",
        "AckRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.reserved-24",
        "AckRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.isRod-25",
        "AckRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.retransmit-26",
        "AckRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.ackRequest-27",
        "SynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.synFlag-28",
        "SynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.reserved1-29",
        "SynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.probeOpaque-30",
        "SynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.pktSeqNo-31",
        "SynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.spdcid-32",
        "SynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.dpdcidValue-33",
        "SynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.payload-34",
        "SynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.synFlag-35",
        "SynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.reserved1-36",
        "SynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.probeOpaque-37",
        "SynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.pktSeqNo-38",
        "SynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.spdcid-39",
        "SynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.pdcInfo-40",
        "SynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.pdcOffset-41",
        "SynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.payload-42",
        "ClearCommandType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.type-43",
        "ClearCommandControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.controlType-44",
        "ClearCommandReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.reserved-45",
        "ClearCommandIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.isRod-46",
        "ClearCommandRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.retransmit-47",
        "ClearCommandAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.ackRequest-48",
        "ClearcommandSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.synFlag-49",
        "ClearcommandSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.reserved1-50",
        "ClearcommandSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.probeOpaque-51",
        "ClearcommandSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.pktSeqNo-52",
        "ClearcommandSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.spdcid-53",
        "ClearcommandSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.dpdcidValue-54",
        "ClearcommandSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.payload-55",
        "ClearcommandSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.synFlag-56",
        "ClearcommandSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.reserved1-57",
        "ClearcommandSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.probeOpaque-58",
        "ClearcommandSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.pktSeqNo-59",
        "ClearcommandSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.spdcid-60",
        "ClearcommandSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.pdcInfo-61",
        "ClearcommandSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.pdcOffset-62",
        "ClearcommandSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.payload-63",
        "ClearRequestType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.type-64",
        "ClearRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.controlType-65",
        "ClearRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.reserved-66",
        "ClearRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.isRod-67",
        "ClearRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.retransmit-68",
        "ClearRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.ackRequest-69",
        "ClearrequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.synFlag-70",
        "ClearrequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.reserved1-71",
        "ClearrequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.probeOpaque-72",
        "ClearrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.pktSeqNo-73",
        "ClearrequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.spdcid-74",
        "ClearrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.dpdcidValue-75",
        "ClearrequestSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.payload-76",
        "ClearrequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.synFlag-77",
        "ClearrequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.reserved1-78",
        "ClearrequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.probeOpaque-79",
        "ClearrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.pktSeqNo-80",
        "ClearrequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.spdcid-81",
        "ClearrequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.pdcInfo-82",
        "ClearrequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.pdcOffset-83",
        "ClearrequestSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.payload-84",
        "CloseCommandType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.type-85",
        "CloseCommandControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.controlType-86",
        "CloseCommandReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.reserved-87",
        "CloseCommandIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.isRod-88",
        "CloseCommandRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.retransmit-89",
        "CloseCommandAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.ackRequest-90",
        "ClosecommandSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.synFlag-91",
        "ClosecommandSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.reserved1-92",
        "ClosecommandSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.probeOpaque-93",
        "ClosecommandSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.pktSeqNo-94",
        "ClosecommandSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.spdcid-95",
        "ClosecommandSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.dpdcidValue-96",
        "ClosecommandSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.payload-97",
        "ClosecommandSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.synFlag-98",
        "ClosecommandSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.reserved1-99",
        "ClosecommandSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.probeOpaque-100",
        "ClosecommandSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.pktSeqNo-101",
        "ClosecommandSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.spdcid-102",
        "ClosecommandSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.pdcInfo-103",
        "ClosecommandSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.pdcOffset-104",
        "ClosecommandSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.payload-105",
        "CloseRequestType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.type-106",
        "CloseRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.controlType-107",
        "CloseRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.reserved-108",
        "CloseRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.isRod-109",
        "CloseRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.retransmit-110",
        "CloseRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.ackRequest-111",
        "CloserequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.synFlag-112",
        "CloserequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.reserved1-113",
        "CloserequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.probeOpaque-114",
        "CloserequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.pktSeqNo-115",
        "CloserequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.spdcid-116",
        "CloserequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.dpdcidValue-117",
        "CloserequestSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.payload-118",
        "CloserequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.synFlag-119",
        "CloserequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.reserved1-120",
        "CloserequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.probeOpaque-121",
        "CloserequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.pktSeqNo-122",
        "CloserequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.spdcid-123",
        "CloserequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.pdcInfo-124",
        "CloserequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.pdcOffset-125",
        "CloserequestSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.payload-126",
        "ProbeType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.type-127",
        "ProbeControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.controlType-128",
        "ProbeReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.reserved-129",
        "ProbeIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.isRod-130",
        "ProbeRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.retransmit-131",
        "ProbeAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.ackRequest-132",
        "ProbeSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.synFlag-133",
        "ProbeSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.reserved1-134",
        "ProbeSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.probeOpaque-135",
        "ProbeSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.pktSeqNo-136",
        "ProbeSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.spdcid-137",
        "ProbeSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.dpdcidValue-138",
        "ProbeSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag0.payload-139",
        "ProbeSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.synFlag-140",
        "ProbeSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.reserved1-141",
        "ProbeSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.probeOpaque-142",
        "ProbeSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.pktSeqNo-143",
        "ProbeSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.spdcid-144",
        "ProbeSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.pdcInfo-145",
        "ProbeSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.pdcOffset-146",
        "ProbeSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.probe.synRequestFlag.synFlag1.payload-147",
        "CreditType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.type-148",
        "CreditControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.controlType-149",
        "CreditReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.reserved-150",
        "CreditIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.isRod-151",
        "CreditRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.retransmit-152",
        "CreditAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.ackRequest-153",
        "CreditSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.synFlag-154",
        "CreditSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.reserved1-155",
        "CreditSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.probeOpaque-156",
        "CreditSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.pktSeqNo-157",
        "CreditSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.spdcid-158",
        "CreditSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.dpdcidValue-159",
        "SynFlag0PayloadCredit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.payloadCredit-160",
        "SynFlag0PayloadReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag0.payloadReserved-161",
        "CreditSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.synFlag-162",
        "CreditSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.reserved1-163",
        "CreditSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.probeOpaque-164",
        "CreditSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.pktSeqNo-165",
        "CreditSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.spdcid-166",
        "CreditSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.pdcInfo-167",
        "CreditSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.pdcOffset-168",
        "SynFlag1PayloadCredit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.payloadCredit-169",
        "SynFlag1PayloadReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.credit.synRequestFlag.synFlag1.payloadReserved-170",
        "CreditRequestType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.type-171",
        "CreditRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.controlType-172",
        "CreditRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.reserved-173",
        "CreditRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.isRod-174",
        "CreditRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.retransmit-175",
        "CreditRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.ackRequest-176",
        "CreditrequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.synFlag-177",
        "CreditrequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.reserved1-178",
        "CreditrequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.probeOpaque-179",
        "CreditrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.pktSeqNo-180",
        "CreditrequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.spdcid-181",
        "CreditrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.dpdcidValue-182",
        "SynFlag0PayloadCCCID": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.payloadCCCID-183",
        "SynFlag0PayloadCreditTarget": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.payloadCreditTarget-184",
        "CreditrequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.synFlag-185",
        "CreditrequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.reserved1-186",
        "CreditrequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.probeOpaque-187",
        "CreditrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.pktSeqNo-188",
        "CreditrequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.spdcid-189",
        "CreditrequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.pdcInfo-190",
        "CreditrequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.pdcOffset-191",
        "SynFlag1PayloadCCCID": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.payloadCCCID-192",
        "SynFlag1PayloadCreditTarget": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.payloadCreditTarget-193",
        "NegotiationType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.type-194",
        "NegotiationControlType": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.controlType-195",
        "NegotiationReserved": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.reserved-196",
        "NegotiationIsRod": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.isRod-197",
        "NegotiationRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.retransmit-198",
        "NegotiationAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.ackRequest-199",
        "NegotiationSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.synFlag-200",
        "NegotiationSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.reserved1-201",
        "NegotiationSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.probeOpaque-202",
        "NegotiationSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.pktSeqNo-203",
        "NegotiationSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.spdcid-204",
        "NegotiationSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.dpdcidValue-205",
        "NegotiationSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag0.payload-206",
        "NegotiationSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.synFlag-207",
        "NegotiationSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.reserved1-208",
        "NegotiationSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.probeOpaque-209",
        "NegotiationSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.pktSeqNo-210",
        "NegotiationSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.spdcid-211",
        "NegotiationSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.pdcInfo-212",
        "NegotiationSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.pdcOffset-213",
        "NegotiationSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rudControlPacket.controlType.negotiation.synRequestFlag.synFlag1.payload-214",
        "ControltypeNoOPType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.type-215",
        "ControltypeNoOPControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.controlType-216",
        "ControltypeNoOPReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.reserved-217",
        "ControltypeNoOPIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.isRod-218",
        "ControltypeNoOPRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.retransmit-219",
        "ControltypeNoOPAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.ackRequest-220",
        "NoopSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.synFlag-221",
        "NoopSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.reserved1-222",
        "NoopSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.probeOpaque-223",
        "NoopSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.pktSeqNo-224",
        "NoopSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.spdcid-225",
        "NoopSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.dpdcidValue-226",
        "NoopSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag0.payload-227",
        "NoopSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.synFlag-228",
        "NoopSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.reserved1-229",
        "NoopSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.probeOpaque-230",
        "NoopSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.pktSeqNo-231",
        "NoopSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.spdcid-232",
        "NoopSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.pdcInfo-233",
        "NoopSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.pdcOffset-234",
        "NoopSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.noOP.synRequestFlag.synFlag1.payload-235",
        "ControltypeAckRequestType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.type-236",
        "ControltypeAckRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.controlType-237",
        "ControltypeAckRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.reserved-238",
        "ControltypeAckRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.isRod-239",
        "ControltypeAckRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.retransmit-240",
        "ControltypeAckRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.ackRequest-241",
        "AckrequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.synFlag-242",
        "AckrequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.reserved1-243",
        "AckrequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.probeOpaque-244",
        "AckrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.pktSeqNo-245",
        "AckrequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.spdcid-246",
        "AckrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.dpdcidValue-247",
        "AckrequestSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag0.payload-248",
        "AckrequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.synFlag-249",
        "AckrequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.reserved1-250",
        "AckrequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.probeOpaque-251",
        "AckrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.pktSeqNo-252",
        "AckrequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.spdcid-253",
        "AckrequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.pdcInfo-254",
        "AckrequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.pdcOffset-255",
        "AckrequestSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.ackRequest.synRequestFlag.synFlag1.payload-256",
        "ControltypeClearCommandType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.type-257",
        "ControltypeClearCommandControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.controlType-258",
        "ControltypeClearCommandReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.reserved-259",
        "ControltypeClearCommandIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.isRod-260",
        "ControltypeClearCommandRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.retransmit-261",
        "ControltypeClearCommandAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.ackRequest-262",
        "ControltypeClearcommandSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.synFlag-263",
        "ControltypeClearcommandSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.reserved1-264",
        "ControltypeClearcommandSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.probeOpaque-265",
        "ControltypeClearcommandSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.pktSeqNo-266",
        "ControltypeClearcommandSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.spdcid-267",
        "ControltypeClearcommandSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.dpdcidValue-268",
        "ControltypeClearcommandSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag0.payload-269",
        "ControltypeClearcommandSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.synFlag-270",
        "ControltypeClearcommandSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.reserved1-271",
        "ControltypeClearcommandSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.probeOpaque-272",
        "ControltypeClearcommandSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.pktSeqNo-273",
        "ControltypeClearcommandSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.spdcid-274",
        "ControltypeClearcommandSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.pdcInfo-275",
        "ControltypeClearcommandSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.pdcOffset-276",
        "ControltypeClearcommandSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearCommand.synRequestFlag.synFlag1.payload-277",
        "ControltypeClearRequestType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.type-278",
        "ControltypeClearRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.controlType-279",
        "ControltypeClearRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.reserved-280",
        "ControltypeClearRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.isRod-281",
        "ControltypeClearRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.retransmit-282",
        "ControltypeClearRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.ackRequest-283",
        "ControltypeClearrequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.synFlag-284",
        "ControltypeClearrequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.reserved1-285",
        "ControltypeClearrequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.probeOpaque-286",
        "ControltypeClearrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.pktSeqNo-287",
        "ControltypeClearrequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.spdcid-288",
        "ControltypeClearrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.dpdcidValue-289",
        "ControltypeClearrequestSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag0.payload-290",
        "ControltypeClearrequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.synFlag-291",
        "ControltypeClearrequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.reserved1-292",
        "ControltypeClearrequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.probeOpaque-293",
        "ControltypeClearrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.pktSeqNo-294",
        "ControltypeClearrequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.spdcid-295",
        "ControltypeClearrequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.pdcInfo-296",
        "ControltypeClearrequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.pdcOffset-297",
        "ControltypeClearrequestSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.clearRequest.synRequestFlag.synFlag1.payload-298",
        "ControltypeCloseCommandType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.type-299",
        "ControltypeCloseCommandControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.controlType-300",
        "ControltypeCloseCommandReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.reserved-301",
        "ControltypeCloseCommandIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.isRod-302",
        "ControltypeCloseCommandRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.retransmit-303",
        "ControltypeCloseCommandAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.ackRequest-304",
        "ControltypeClosecommandSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.synFlag-305",
        "ControltypeClosecommandSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.reserved1-306",
        "ControltypeClosecommandSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.probeOpaque-307",
        "ControltypeClosecommandSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.pktSeqNo-308",
        "ControltypeClosecommandSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.spdcid-309",
        "ControltypeClosecommandSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.dpdcidValue-310",
        "ControltypeClosecommandSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag0.payload-311",
        "ControltypeClosecommandSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.synFlag-312",
        "ControltypeClosecommandSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.reserved1-313",
        "ControltypeClosecommandSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.probeOpaque-314",
        "ControltypeClosecommandSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.pktSeqNo-315",
        "ControltypeClosecommandSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.spdcid-316",
        "ControltypeClosecommandSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.pdcInfo-317",
        "ControltypeClosecommandSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.pdcOffset-318",
        "ControltypeClosecommandSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeCommand.synRequestFlag.synFlag1.payload-319",
        "ControltypeCloseRequestType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.type-320",
        "ControltypeCloseRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.controlType-321",
        "ControltypeCloseRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.reserved-322",
        "ControltypeCloseRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.isRod-323",
        "ControltypeCloseRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.retransmit-324",
        "ControltypeCloseRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.ackRequest-325",
        "ControltypeCloserequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.synFlag-326",
        "ControltypeCloserequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.reserved1-327",
        "ControltypeCloserequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.probeOpaque-328",
        "ControltypeCloserequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.pktSeqNo-329",
        "ControltypeCloserequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.spdcid-330",
        "ControltypeCloserequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.dpdcidValue-331",
        "ControltypeCloserequestSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag0.payload-332",
        "ControltypeCloserequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.synFlag-333",
        "ControltypeCloserequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.reserved1-334",
        "ControltypeCloserequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.probeOpaque-335",
        "ControltypeCloserequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.pktSeqNo-336",
        "ControltypeCloserequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.spdcid-337",
        "ControltypeCloserequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.pdcInfo-338",
        "ControltypeCloserequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.pdcOffset-339",
        "ControltypeCloserequestSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.closeRequest.synRequestFlag.synFlag1.payload-340",
        "ControltypeProbeType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.type-341",
        "ControltypeProbeControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.controlType-342",
        "ControltypeProbeReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.reserved-343",
        "ControltypeProbeIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.isRod-344",
        "ControltypeProbeRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.retransmit-345",
        "ControltypeProbeAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.ackRequest-346",
        "ControltypeProbeSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.synFlag-347",
        "ControltypeProbeSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.reserved1-348",
        "ControltypeProbeSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.probeOpaque-349",
        "ControltypeProbeSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.pktSeqNo-350",
        "ControltypeProbeSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.spdcid-351",
        "ControltypeProbeSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.dpdcidValue-352",
        "ControltypeProbeSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag0.payload-353",
        "ControltypeProbeSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.synFlag-354",
        "ControltypeProbeSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.reserved1-355",
        "ControltypeProbeSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.probeOpaque-356",
        "ControltypeProbeSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.pktSeqNo-357",
        "ControltypeProbeSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.spdcid-358",
        "ControltypeProbeSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.pdcInfo-359",
        "ControltypeProbeSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.pdcOffset-360",
        "ControltypeProbeSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.probe.synRequestFlag.synFlag1.payload-361",
        "ControltypeCreditType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.type-362",
        "ControltypeCreditControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.controlType-363",
        "ControltypeCreditReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.reserved-364",
        "ControltypeCreditIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.isRod-365",
        "ControltypeCreditRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.retransmit-366",
        "ControltypeCreditAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.ackRequest-367",
        "ControltypeCreditSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.synFlag-368",
        "ControltypeCreditSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.reserved1-369",
        "ControltypeCreditSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.probeOpaque-370",
        "ControltypeCreditSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.pktSeqNo-371",
        "ControltypeCreditSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.spdcid-372",
        "ControltypeCreditSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.dpdcidValue-373",
        "SynrequestflagSynFlag0PayloadCredit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.payloadCredit-374",
        "SynrequestflagSynFlag0PayloadReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag0.payloadReserved-375",
        "ControltypeCreditSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.synFlag-376",
        "ControltypeCreditSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.reserved1-377",
        "ControltypeCreditSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.probeOpaque-378",
        "ControltypeCreditSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.pktSeqNo-379",
        "ControltypeCreditSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.spdcid-380",
        "ControltypeCreditSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.pdcInfo-381",
        "ControltypeCreditSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.pdcOffset-382",
        "SynrequestflagSynFlag1PayloadCredit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.payloadCredit-383",
        "SynrequestflagSynFlag1PayloadReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.credit.synRequestFlag.synFlag1.payloadReserved-384",
        "ControltypeCreditRequestType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.type-385",
        "ControltypeCreditRequestControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.controlType-386",
        "ControltypeCreditRequestReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.reserved-387",
        "ControltypeCreditRequestIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.isRod-388",
        "ControltypeCreditRequestRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.retransmit-389",
        "ControltypeCreditRequestAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.ackRequest-390",
        "ControltypeCreditrequestSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.synFlag-391",
        "ControltypeCreditrequestSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.reserved1-392",
        "ControltypeCreditrequestSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.probeOpaque-393",
        "ControltypeCreditrequestSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.pktSeqNo-394",
        "ControltypeCreditrequestSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.spdcid-395",
        "ControltypeCreditrequestSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.dpdcidValue-396",
        "SynrequestflagSynFlag0PayloadCCCID": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.payloadCCCID-397",
        "SynrequestflagSynFlag0PayloadCreditTarget": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag0.payloadCreditTarget-398",
        "ControltypeCreditrequestSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.synFlag-399",
        "ControltypeCreditrequestSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.reserved1-400",
        "ControltypeCreditrequestSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.probeOpaque-401",
        "ControltypeCreditrequestSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.pktSeqNo-402",
        "ControltypeCreditrequestSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.spdcid-403",
        "ControltypeCreditrequestSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.pdcInfo-404",
        "ControltypeCreditrequestSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.pdcOffset-405",
        "SynrequestflagSynFlag1PayloadCCCID": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.payloadCCCID-406",
        "SynrequestflagSynFlag1PayloadCreditTarget": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.creditRequest.synRequestFlag.synFlag1.payloadCreditTarget-407",
        "ControltypeNegotiationType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.type-408",
        "ControltypeNegotiationControlType": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.controlType-409",
        "ControltypeNegotiationReserved": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.reserved-410",
        "ControltypeNegotiationIsRod": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.isRod-411",
        "ControltypeNegotiationRetransmit": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.retransmit-412",
        "ControltypeNegotiationAckRequest": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.ackRequest-413",
        "ControltypeNegotiationSynrequestflagSynFlag0SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.synFlag-414",
        "ControltypeNegotiationSynrequestflagSynFlag0Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.reserved1-415",
        "ControltypeNegotiationSynrequestflagSynFlag0ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.probeOpaque-416",
        "ControltypeNegotiationSynrequestflagSynFlag0PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.pktSeqNo-417",
        "ControltypeNegotiationSynrequestflagSynFlag0Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.spdcid-418",
        "ControltypeNegotiationSynrequestflagSynFlag0DpdcidValue": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.dpdcidValue-419",
        "ControltypeNegotiationSynrequestflagSynFlag0Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag0.payload-420",
        "ControltypeNegotiationSynrequestflagSynFlag1SynFlag": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.synFlag-421",
        "ControltypeNegotiationSynrequestflagSynFlag1Reserved1": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.reserved1-422",
        "ControltypeNegotiationSynrequestflagSynFlag1ProbeOpaque": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.probeOpaque-423",
        "ControltypeNegotiationSynrequestflagSynFlag1PktSeqNo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.pktSeqNo-424",
        "ControltypeNegotiationSynrequestflagSynFlag1Spdcid": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.spdcid-425",
        "ControltypeNegotiationSynrequestflagSynFlag1PdcInfo": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.pdcInfo-426",
        "ControltypeNegotiationSynrequestflagSynFlag1PdcOffset": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.pdcOffset-427",
        "ControltypeNegotiationSynrequestflagSynFlag1Payload": "uetPdsRudRodCP.header.cpHeaderType.rodControlPacket.controlType.negotiation.synRequestFlag.synFlag1.payload-428",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsRudRodCP, self).__init__(parent, list_op)

    @property
    def NoOPType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NoOPType"]))

    @property
    def NoOPControlType(self):
        """
        Display Name: Control Type
        Default Value: 0
        Value Format: decimal
        Available enum values: NO_OP, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoOPControlType"])
        )

    @property
    def NoOPReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NoOPReserved"]))

    @property
    def NoOPIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NoOPIsRod"]))

    @property
    def NoOPRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoOPRetransmit"])
        )

    @property
    def NoOPAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoOPAckRequest"])
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
    def SynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0ProbeOpaque"])
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
    def SynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0Payload"])
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
    def SynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1ProbeOpaque"])
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
    def SynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1Payload"])
        )

    @property
    def AckRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckRequestType"])
        )

    @property
    def AckRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 1
        Value Format: decimal
        Available enum values: ACK_REQUEST, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckRequestControlType"])
        )

    @property
    def AckRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckRequestReserved"])
        )

    @property
    def AckRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckRequestIsRod"])
        )

    @property
    def AckRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckRequestRetransmit"])
        )

    @property
    def AckRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AckRequestAckRequest"])
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
    def SynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0ProbeOpaque"]),
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
    def SynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (message_id)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag0Payload"]),
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
    def SynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1ProbeOpaque"]),
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
    def SynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (message_id)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SynrequestflagSynFlag1Payload"]),
        )

    @property
    def ClearCommandType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearCommandType"])
        )

    @property
    def ClearCommandControlType(self):
        """
        Display Name: Control Type
        Default Value: 2
        Value Format: decimal
        Available enum values: CLEAR_COMMAND, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearCommandControlType"])
        )

    @property
    def ClearCommandReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearCommandReserved"])
        )

    @property
    def ClearCommandIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearCommandIsRod"])
        )

    @property
    def ClearCommandRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearCommandRetransmit"])
        )

    @property
    def ClearCommandAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearCommandAckRequest"])
        )

    @property
    def ClearcommandSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (CLEAR_PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def ClearcommandSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (CLEAR_PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearcommandSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def ClearRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearRequestType"])
        )

    @property
    def ClearRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 3
        Value Format: decimal
        Available enum values: CLEAR_REQUEST, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearRequestControlType"])
        )

    @property
    def ClearRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearRequestReserved"])
        )

    @property
    def ClearRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearRequestIsRod"])
        )

    @property
    def ClearRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearRequestRetransmit"])
        )

    @property
    def ClearRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClearRequestAckRequest"])
        )

    @property
    def ClearrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def ClearrequestSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClearrequestSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def CloseCommandType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseCommandType"])
        )

    @property
    def CloseCommandControlType(self):
        """
        Display Name: Control Type
        Default Value: 4
        Value Format: decimal
        Available enum values: CLOSE_COMMAND, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseCommandControlType"])
        )

    @property
    def CloseCommandReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseCommandReserved"])
        )

    @property
    def CloseCommandIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseCommandIsRod"])
        )

    @property
    def CloseCommandRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseCommandRetransmit"])
        )

    @property
    def CloseCommandAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseCommandAckRequest"])
        )

    @property
    def ClosecommandSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def ClosecommandSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ClosecommandSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def CloseRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseRequestType"])
        )

    @property
    def CloseRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 5
        Value Format: decimal
        Available enum values: CLOSE_REQUEST, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseRequestControlType"])
        )

    @property
    def CloseRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseRequestReserved"])
        )

    @property
    def CloseRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseRequestIsRod"])
        )

    @property
    def CloseRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseRequestRetransmit"])
        )

    @property
    def CloseRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CloseRequestAckRequest"])
        )

    @property
    def CloserequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def CloserequestSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CloserequestSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def ProbeType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProbeType"]))

    @property
    def ProbeControlType(self):
        """
        Display Name: Control Type
        Default Value: 6
        Value Format: decimal
        Available enum values: PROBE, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProbeControlType"])
        )

    @property
    def ProbeReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProbeReserved"]))

    @property
    def ProbeIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProbeIsRod"]))

    @property
    def ProbeRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProbeRetransmit"])
        )

    @property
    def ProbeAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProbeAckRequest"])
        )

    @property
    def ProbeSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0Spdcid"]),
        )

    @property
    def ProbeSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (SACK bitmap base PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1Spdcid"]),
        )

    @property
    def ProbeSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def ProbeSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (SACK bitmap base PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProbeSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def CreditType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CreditType"]))

    @property
    def CreditControlType(self):
        """
        Display Name: Control Type
        Default Value: 7
        Value Format: decimal
        Available enum values: CREDIT, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditControlType"])
        )

    @property
    def CreditReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditReserved"])
        )

    @property
    def CreditIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CreditIsRod"]))

    @property
    def CreditRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRetransmit"])
        )

    @property
    def CreditAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditAckRequest"])
        )

    @property
    def CreditSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def SynFlag0PayloadCredit(self):
        """
        Display Name: Payload (credit - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0PayloadCredit"])
        )

    @property
    def SynFlag0PayloadReserved(self):
        """
        Display Name: Payload (reserved - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0PayloadReserved"])
        )

    @property
    def CreditSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def CreditSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def SynFlag1PayloadCredit(self):
        """
        Display Name: Payload (credit - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PayloadCredit"])
        )

    @property
    def SynFlag1PayloadReserved(self):
        """
        Display Name: Payload (reserved - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PayloadReserved"])
        )

    @property
    def CreditRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRequestType"])
        )

    @property
    def CreditRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 8
        Value Format: decimal
        Available enum values: CREDIT REQUEST, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRequestControlType"])
        )

    @property
    def CreditRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRequestReserved"])
        )

    @property
    def CreditRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRequestIsRod"])
        )

    @property
    def CreditRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRequestRetransmit"])
        )

    @property
    def CreditRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CreditRequestAckRequest"])
        )

    @property
    def CreditrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def SynFlag0PayloadCCCID(self):
        """
        Display Name: Payload (ccc_id - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0PayloadCCCID"])
        )

    @property
    def SynFlag0PayloadCreditTarget(self):
        """
        Display Name: Payload (credit_target - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag0PayloadCreditTarget"])
        )

    @property
    def CreditrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def CreditrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CreditrequestSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def SynFlag1PayloadCCCID(self):
        """
        Display Name: Payload (ccc_id - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PayloadCCCID"])
        )

    @property
    def SynFlag1PayloadCreditTarget(self):
        """
        Display Name: Payload (credit_target - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynFlag1PayloadCreditTarget"])
        )

    @property
    def NegotiationType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NegotiationType"])
        )

    @property
    def NegotiationControlType(self):
        """
        Display Name: Control Type
        Default Value: 9
        Value Format: decimal
        Available enum values: NEGOTIATION, 9
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NegotiationControlType"])
        )

    @property
    def NegotiationReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NegotiationReserved"])
        )

    @property
    def NegotiationIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NegotiationIsRod"])
        )

    @property
    def NegotiationRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NegotiationRetransmit"])
        )

    @property
    def NegotiationAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NegotiationAckRequest"])
        )

    @property
    def NegotiationSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def NegotiationSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NegotiationSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def ControltypeNoOPType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNoOPType"])
        )

    @property
    def ControltypeNoOPControlType(self):
        """
        Display Name: Control Type
        Default Value: 0
        Value Format: decimal
        Available enum values: NO_OP, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNoOPControlType"])
        )

    @property
    def ControltypeNoOPReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNoOPReserved"])
        )

    @property
    def ControltypeNoOPIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNoOPIsRod"])
        )

    @property
    def ControltypeNoOPRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNoOPRetransmit"])
        )

    @property
    def ControltypeNoOPAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNoOPAckRequest"])
        )

    @property
    def NoopSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0SynFlag"]),
        )

    @property
    def NoopSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0Spdcid"]),
        )

    @property
    def NoopSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag0Payload"]),
        )

    @property
    def NoopSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1SynFlag"]),
        )

    @property
    def NoopSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1Spdcid"]),
        )

    @property
    def NoopSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1PdcInfo"]),
        )

    @property
    def NoopSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def NoopSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoopSynrequestflagSynFlag1Payload"]),
        )

    @property
    def ControltypeAckRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeAckRequestType"])
        )

    @property
    def ControltypeAckRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 1
        Value Format: decimal
        Available enum values: ACK_REQUEST, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeAckRequestControlType"]),
        )

    @property
    def ControltypeAckRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeAckRequestReserved"]),
        )

    @property
    def ControltypeAckRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeAckRequestIsRod"])
        )

    @property
    def ControltypeAckRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeAckRequestRetransmit"]),
        )

    @property
    def ControltypeAckRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeAckRequestAckRequest"]),
        )

    @property
    def AckrequestSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (message_id)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def AckrequestSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (message_id)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AckrequestSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def ControltypeClearCommandType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeClearCommandType"])
        )

    @property
    def ControltypeClearCommandControlType(self):
        """
        Display Name: Control Type
        Default Value: 2
        Value Format: decimal
        Available enum values: CLEAR_COMMAND, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClearCommandControlType"]
            ),
        )

    @property
    def ControltypeClearCommandReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeClearCommandReserved"]),
        )

    @property
    def ControltypeClearCommandIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeClearCommandIsRod"])
        )

    @property
    def ControltypeClearCommandRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeClearCommandRetransmit"]),
        )

    @property
    def ControltypeClearCommandAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeClearCommandAckRequest"]),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0SynFlag(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0Reserved1(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearcommandSynrequestflagSynFlag0ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0PktSeqNo(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClearcommandSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0DpdcidValue(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (CLEAR_PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearcommandSynrequestflagSynFlag0Payload"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1SynFlag(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1Reserved1(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearcommandSynrequestflagSynFlag1ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1PktSeqNo(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClearcommandSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1PdcInfo(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1PdcOffset(self):
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
                    "ControltypeClearcommandSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def ControltypeClearcommandSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (CLEAR_PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearcommandSynrequestflagSynFlag1Payload"
                ]
            ),
        )

    @property
    def ControltypeClearRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeClearRequestType"])
        )

    @property
    def ControltypeClearRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 3
        Value Format: decimal
        Available enum values: CLEAR_REQUEST, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClearRequestControlType"]
            ),
        )

    @property
    def ControltypeClearRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeClearRequestReserved"]),
        )

    @property
    def ControltypeClearRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeClearRequestIsRod"])
        )

    @property
    def ControltypeClearRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeClearRequestRetransmit"]),
        )

    @property
    def ControltypeClearRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeClearRequestAckRequest"]),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0SynFlag(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0Reserved1(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearrequestSynrequestflagSynFlag0ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0PktSeqNo(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClearrequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0DpdcidValue(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearrequestSynrequestflagSynFlag0Payload"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1SynFlag(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1Reserved1(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearrequestSynrequestflagSynFlag1ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1PktSeqNo(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClearrequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1PdcInfo(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1PdcOffset(self):
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
                    "ControltypeClearrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def ControltypeClearrequestSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClearrequestSynrequestflagSynFlag1Payload"
                ]
            ),
        )

    @property
    def ControltypeCloseCommandType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseCommandType"])
        )

    @property
    def ControltypeCloseCommandControlType(self):
        """
        Display Name: Control Type
        Default Value: 4
        Value Format: decimal
        Available enum values: CLOSE_COMMAND, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCloseCommandControlType"]
            ),
        )

    @property
    def ControltypeCloseCommandReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseCommandReserved"]),
        )

    @property
    def ControltypeCloseCommandIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseCommandIsRod"])
        )

    @property
    def ControltypeCloseCommandRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseCommandRetransmit"]),
        )

    @property
    def ControltypeCloseCommandAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseCommandAckRequest"]),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0SynFlag(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0Reserved1(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClosecommandSynrequestflagSynFlag0ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0PktSeqNo(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClosecommandSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0DpdcidValue(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClosecommandSynrequestflagSynFlag0Payload"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1SynFlag(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1Reserved1(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClosecommandSynrequestflagSynFlag1ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1PktSeqNo(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeClosecommandSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1PdcInfo(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1PdcOffset(self):
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
                    "ControltypeClosecommandSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def ControltypeClosecommandSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeClosecommandSynrequestflagSynFlag1Payload"
                ]
            ),
        )

    @property
    def ControltypeCloseRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseRequestType"])
        )

    @property
    def ControltypeCloseRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 5
        Value Format: decimal
        Available enum values: CLOSE_REQUEST, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCloseRequestControlType"]
            ),
        )

    @property
    def ControltypeCloseRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseRequestReserved"]),
        )

    @property
    def ControltypeCloseRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseRequestIsRod"])
        )

    @property
    def ControltypeCloseRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseRequestRetransmit"]),
        )

    @property
    def ControltypeCloseRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCloseRequestAckRequest"]),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0SynFlag(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0Reserved1(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeCloserequestSynrequestflagSynFlag0ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0PktSeqNo(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCloserequestSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0DpdcidValue(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeCloserequestSynrequestflagSynFlag0Payload"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1SynFlag(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1Reserved1(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeCloserequestSynrequestflagSynFlag1ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1PktSeqNo(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCloserequestSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1PdcInfo(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1PdcOffset(self):
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
                    "ControltypeCloserequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def ControltypeCloserequestSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeCloserequestSynrequestflagSynFlag1Payload"
                ]
            ),
        )

    @property
    def ControltypeProbeType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeProbeType"])
        )

    @property
    def ControltypeProbeControlType(self):
        """
        Display Name: Control Type
        Default Value: 6
        Value Format: decimal
        Available enum values: PROBE, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeProbeControlType"])
        )

    @property
    def ControltypeProbeReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeProbeReserved"])
        )

    @property
    def ControltypeProbeIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeProbeIsRod"])
        )

    @property
    def ControltypeProbeRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeProbeRetransmit"])
        )

    @property
    def ControltypeProbeAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeProbeAckRequest"])
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload (SACK bitmap base PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def ControltypeProbeSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload (SACK bitmap base PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeProbeSynrequestflagSynFlag1Payload"]
            ),
        )

    @property
    def ControltypeCreditType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditType"])
        )

    @property
    def ControltypeCreditControlType(self):
        """
        Display Name: Control Type
        Default Value: 7
        Value Format: decimal
        Available enum values: CREDIT, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditControlType"])
        )

    @property
    def ControltypeCreditReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditReserved"])
        )

    @property
    def ControltypeCreditIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditIsRod"])
        )

    @property
    def ControltypeCreditRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditRetransmit"])
        )

    @property
    def ControltypeCreditAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditAckRequest"])
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag0Reserved1(self):
        """
        Display Name: Reserved1 Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag0Reserved1"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag0ProbeOpaque"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag0PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag0PktSeqNo"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag0DpdcidValue(self):
        """
        Display Name: DPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag0DpdcidValue"]
            ),
        )

    @property
    def SynrequestflagSynFlag0PayloadCredit(self):
        """
        Display Name: Payload (credit - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag0PayloadCredit"]
            ),
        )

    @property
    def SynrequestflagSynFlag0PayloadReserved(self):
        """
        Display Name: Payload (reserved - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag0PayloadReserved"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1Reserved1(self):
        """
        Display Name: Reserved1 Flag(2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1Reserved1"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1ProbeOpaque"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1PktSeqNo(self):
        """
        Display Name: Pkt Seq No
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1PktSeqNo"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ControltypeCreditSynrequestflagSynFlag1PdcOffset(self):
        """
        Display Name: PDC Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditSynrequestflagSynFlag1PdcOffset"]
            ),
        )

    @property
    def SynrequestflagSynFlag1PayloadCredit(self):
        """
        Display Name: Payload (credit - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag1PayloadCredit"]
            ),
        )

    @property
    def SynrequestflagSynFlag1PayloadReserved(self):
        """
        Display Name: Payload (reserved - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag1PayloadReserved"]
            ),
        )

    @property
    def ControltypeCreditRequestType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditRequestType"])
        )

    @property
    def ControltypeCreditRequestControlType(self):
        """
        Display Name: Control Type
        Default Value: 8
        Value Format: decimal
        Available enum values: CREDIT REQUEST, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditRequestControlType"]
            ),
        )

    @property
    def ControltypeCreditRequestReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditRequestReserved"]),
        )

    @property
    def ControltypeCreditRequestIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeCreditRequestIsRod"]),
        )

    @property
    def ControltypeCreditRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditRequestRetransmit"]
            ),
        )

    @property
    def ControltypeCreditRequestAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeCreditRequestAckRequest"]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag0SynFlag(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag0SynFlag"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag0Reserved1(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeCreditrequestSynrequestflagSynFlag0ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag0PktSeqNo(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag0Spdcid(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag0Spdcid"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag0DpdcidValue(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def SynrequestflagSynFlag0PayloadCCCID(self):
        """
        Display Name: Payload (ccc_id - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag0PayloadCCCID"]
            ),
        )

    @property
    def SynrequestflagSynFlag0PayloadCreditTarget(self):
        """
        Display Name: Payload (credit_target - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag0PayloadCreditTarget"]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1SynFlag(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag1SynFlag"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1Reserved1(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeCreditrequestSynrequestflagSynFlag1ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1PktSeqNo(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1Spdcid(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag1Spdcid"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1PdcInfo(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag1PdcInfo"
                ]
            ),
        )

    @property
    def ControltypeCreditrequestSynrequestflagSynFlag1PdcOffset(self):
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
                    "ControltypeCreditrequestSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def SynrequestflagSynFlag1PayloadCCCID(self):
        """
        Display Name: Payload (ccc_id - 8bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag1PayloadCCCID"]
            ),
        )

    @property
    def SynrequestflagSynFlag1PayloadCreditTarget(self):
        """
        Display Name: Payload (credit_target - 24bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SynrequestflagSynFlag1PayloadCreditTarget"]
            ),
        )

    @property
    def ControltypeNegotiationType(self):
        """
        Display Name: Type
        Default Value: 11
        Value Format: decimal
        Available enum values: CONTROL_PACKET, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNegotiationType"])
        )

    @property
    def ControltypeNegotiationControlType(self):
        """
        Display Name: Control Type
        Default Value: 9
        Value Format: decimal
        Available enum values: NEGOTIATION, 9
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeNegotiationControlType"]),
        )

    @property
    def ControltypeNegotiationReserved(self):
        """
        Display Name: Reserved Flag (1-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeNegotiationReserved"]),
        )

    @property
    def ControltypeNegotiationIsRod(self):
        """
        Display Name: isRod (1-bits)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControltypeNegotiationIsRod"])
        )

    @property
    def ControltypeNegotiationRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeNegotiationRetransmit"]),
        )

    @property
    def ControltypeNegotiationAckRequest(self):
        """
        Display Name: Ack Request Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ControltypeNegotiationAckRequest"]),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag0SynFlag"]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0Reserved1(self):
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
                    "ControltypeNegotiationSynrequestflagSynFlag0Reserved1"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeNegotiationSynrequestflagSynFlag0ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0PktSeqNo(self):
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
                    "ControltypeNegotiationSynrequestflagSynFlag0PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag0Spdcid"]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0DpdcidValue(self):
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
                    "ControltypeNegotiationSynrequestflagSynFlag0DpdcidValue"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag0Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag0Payload"]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1SynFlag(self):
        """
        Display Name: Syn Flag (1-bit)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag1SynFlag"]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1Reserved1(self):
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
                    "ControltypeNegotiationSynrequestflagSynFlag1Reserved1"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1ProbeOpaque(self):
        """
        Display Name: Probe Opaque
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControltypeNegotiationSynrequestflagSynFlag1ProbeOpaque"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1PktSeqNo(self):
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
                    "ControltypeNegotiationSynrequestflagSynFlag1PktSeqNo"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1Spdcid(self):
        """
        Display Name: SPDCID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag1Spdcid"]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1PdcInfo(self):
        """
        Display Name: PDC Info
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag1PdcInfo"]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1PdcOffset(self):
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
                    "ControltypeNegotiationSynrequestflagSynFlag1PdcOffset"
                ]
            ),
        )

    @property
    def ControltypeNegotiationSynrequestflagSynFlag1Payload(self):
        """
        Display Name: Payload
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControltypeNegotiationSynrequestflagSynFlag1Payload"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
