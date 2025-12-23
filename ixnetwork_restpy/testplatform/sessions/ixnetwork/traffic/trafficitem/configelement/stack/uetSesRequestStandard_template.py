from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetSesRequestStandard(Base):
    __slots__ = ()
    _SDM_NAME = "uetSesRequestStandard"
    _SDM_ATT_MAP = {
        "SesRequestWithSom1Reserved1": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.reserved1-1",
        "SesRequestWithSom1OpCode": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.opCode-2",
        "SesRequestWithSom1Version": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.version-3",
        "SesRequestWithSom1DeliveryComplete": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.deliveryComplete-4",
        "SesRequestWithSom1InitiatorError": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.initiatorError-5",
        "SesRequestWithSom1Relative": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.relative-6",
        "SesRequestWithSom1HeaderDataPresent": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.headerDataPresent-7",
        "SesRequestWithSom1EndOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.endOfMsg-8",
        "SesRequestWithSom1StartOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.startOfMsg-9",
        "SesRequestWithSom1MessageId": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.messageId-10",
        "SesRequestWithSom1RiGeneration": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.riGeneration-11",
        "SesRequestWithSom1JobId": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.jobId-12",
        "SesRequestWithSom1Reserved2": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.Reserved2-13",
        "SesRequestWithSom1PidOnFEP": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.pidOnFEP-14",
        "SesRequestWithSom1Reserved3": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.Reserved3-15",
        "SesRequestWithSom1ResourceIndex": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.resourceIndex-16",
        "SesRequestWithSom1BufferOffset": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.bufferOffset-17",
        "SesRequestWithSom1InitiatorId": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.initiatorId-18",
        "SesRequestWithSom1MatchBits": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.matchBits-19",
        "SesRequestWithSom1HeaderData": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.headerData-20",
        "SesRequestWithSom1RequestLength": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom1.requestLength-21",
        "SesRequestWithSom0Reserved1": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.reserved1-22",
        "SesRequestWithSom0OpCode": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.opCode-23",
        "SesRequestWithSom0Version": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.version-24",
        "SesRequestWithSom0DeliveryComplete": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.deliveryComplete-25",
        "SesRequestWithSom0InitiatorError": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.initiatorError-26",
        "SesRequestWithSom0Relative": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.relative-27",
        "SesRequestWithSom0HeaderDataPresent": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.headerDataPresent-28",
        "SesRequestWithSom0EndOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.endOfMsg-29",
        "SesRequestWithSom0StartOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.startOfMsg-30",
        "SesRequestWithSom0MessageId": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.messageId-31",
        "SesRequestWithSom0RiGeneration": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.riGeneration-32",
        "SesRequestWithSom0JobId": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.jobId-33",
        "SesRequestWithSom0Reserved2": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.Reserved2-34",
        "SesRequestWithSom0PidOnFEP": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.pidOnFEP-35",
        "SesRequestWithSom0Reserved3": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.Reserved3-36",
        "SesRequestWithSom0ResourceIndex": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.resourceIndex-37",
        "SesRequestWithSom0BufferOffset": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.bufferOffset-38",
        "SesRequestWithSom0InitiatorId": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.initiatorId-39",
        "SesRequestWithSom0MatchBits": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.matchBits-40",
        "SesRequestWithSom0Reserved4": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.Reserved4-41",
        "SesRequestWithSom0PayloadLength": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.payloadLength-42",
        "SesRequestWithSom0MessageOffset": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.messageOffset-43",
        "SesRequestWithSom0RequestLength": "uetSesRequestStandard.header.sesOpCodeType.uetWrite.standardHeaderFormatType.sesRequestWithSom0.requestLength-44",
        "StandardheaderformattypeSesRequestWithSom1Reserved1": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.reserved1-45",
        "StandardheaderformattypeSesRequestWithSom1OpCode": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.opCode-46",
        "StandardheaderformattypeSesRequestWithSom1Version": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.version-47",
        "StandardheaderformattypeSesRequestWithSom1DeliveryComplete": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.deliveryComplete-48",
        "StandardheaderformattypeSesRequestWithSom1InitiatorError": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.initiatorError-49",
        "StandardheaderformattypeSesRequestWithSom1Relative": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.relative-50",
        "StandardheaderformattypeSesRequestWithSom1HeaderDataPresent": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.headerDataPresent-51",
        "StandardheaderformattypeSesRequestWithSom1EndOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.endOfMsg-52",
        "StandardheaderformattypeSesRequestWithSom1StartOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.startOfMsg-53",
        "StandardheaderformattypeSesRequestWithSom1MessageId": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.messageId-54",
        "StandardheaderformattypeSesRequestWithSom1RiGeneration": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.riGeneration-55",
        "StandardheaderformattypeSesRequestWithSom1JobId": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.jobId-56",
        "StandardheaderformattypeSesRequestWithSom1Reserved2": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.Reserved2-57",
        "StandardheaderformattypeSesRequestWithSom1PidOnFEP": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.pidOnFEP-58",
        "StandardheaderformattypeSesRequestWithSom1Reserved3": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.Reserved3-59",
        "StandardheaderformattypeSesRequestWithSom1ResourceIndex": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.resourceIndex-60",
        "StandardheaderformattypeSesRequestWithSom1BufferOffset": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.bufferOffset-61",
        "StandardheaderformattypeSesRequestWithSom1InitiatorId": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.initiatorId-62",
        "StandardheaderformattypeSesRequestWithSom1MatchBits": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.matchBits-63",
        "StandardheaderformattypeSesRequestWithSom1HeaderData": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.headerData-64",
        "StandardheaderformattypeSesRequestWithSom1RequestLength": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom1.requestLength-65",
        "StandardheaderformattypeSesRequestWithSom0Reserved1": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.reserved1-66",
        "StandardheaderformattypeSesRequestWithSom0OpCode": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.opCode-67",
        "StandardheaderformattypeSesRequestWithSom0Version": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.version-68",
        "StandardheaderformattypeSesRequestWithSom0DeliveryComplete": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.deliveryComplete-69",
        "StandardheaderformattypeSesRequestWithSom0InitiatorError": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.initiatorError-70",
        "StandardheaderformattypeSesRequestWithSom0Relative": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.relative-71",
        "StandardheaderformattypeSesRequestWithSom0HeaderDataPresent": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.headerDataPresent-72",
        "StandardheaderformattypeSesRequestWithSom0EndOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.endOfMsg-73",
        "StandardheaderformattypeSesRequestWithSom0StartOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.startOfMsg-74",
        "StandardheaderformattypeSesRequestWithSom0MessageId": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.messageId-75",
        "StandardheaderformattypeSesRequestWithSom0RiGeneration": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.riGeneration-76",
        "StandardheaderformattypeSesRequestWithSom0JobId": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.jobId-77",
        "StandardheaderformattypeSesRequestWithSom0Reserved2": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.Reserved2-78",
        "StandardheaderformattypeSesRequestWithSom0PidOnFEP": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.pidOnFEP-79",
        "StandardheaderformattypeSesRequestWithSom0Reserved3": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.Reserved3-80",
        "StandardheaderformattypeSesRequestWithSom0ResourceIndex": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.resourceIndex-81",
        "StandardheaderformattypeSesRequestWithSom0BufferOffset": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.bufferOffset-82",
        "StandardheaderformattypeSesRequestWithSom0InitiatorId": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.initiatorId-83",
        "StandardheaderformattypeSesRequestWithSom0MatchBits": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.matchBits-84",
        "StandardheaderformattypeSesRequestWithSom0Reserved4": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.Reserved4-85",
        "StandardheaderformattypeSesRequestWithSom0PayloadLength": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.payloadLength-86",
        "StandardheaderformattypeSesRequestWithSom0MessageOffset": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.messageOffset-87",
        "StandardheaderformattypeSesRequestWithSom0RequestLength": "uetSesRequestStandard.header.sesOpCodeType.uetRead.standardHeaderFormatType.sesRequestWithSom0.requestLength-88",
        "UetsendStandardheaderformattypeSesRequestWithSom1Reserved1": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.reserved1-89",
        "UetsendStandardheaderformattypeSesRequestWithSom1OpCode": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.opCode-90",
        "UetsendStandardheaderformattypeSesRequestWithSom1Version": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.version-91",
        "UetsendStandardheaderformattypeSesRequestWithSom1DeliveryComplete": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.deliveryComplete-92",
        "UetsendStandardheaderformattypeSesRequestWithSom1InitiatorError": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.initiatorError-93",
        "UetsendStandardheaderformattypeSesRequestWithSom1Relative": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.relative-94",
        "UetsendStandardheaderformattypeSesRequestWithSom1HeaderDataPresent": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.headerDataPresent-95",
        "UetsendStandardheaderformattypeSesRequestWithSom1EndOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.endOfMsg-96",
        "UetsendStandardheaderformattypeSesRequestWithSom1StartOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.startOfMsg-97",
        "UetsendStandardheaderformattypeSesRequestWithSom1MessageId": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.messageId-98",
        "UetsendStandardheaderformattypeSesRequestWithSom1RiGeneration": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.riGeneration-99",
        "UetsendStandardheaderformattypeSesRequestWithSom1JobId": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.jobId-100",
        "UetsendStandardheaderformattypeSesRequestWithSom1Reserved2": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.Reserved2-101",
        "UetsendStandardheaderformattypeSesRequestWithSom1PidOnFEP": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.pidOnFEP-102",
        "UetsendStandardheaderformattypeSesRequestWithSom1Reserved3": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.Reserved3-103",
        "UetsendStandardheaderformattypeSesRequestWithSom1ResourceIndex": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.resourceIndex-104",
        "UetsendStandardheaderformattypeSesRequestWithSom1BufferOffset": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.bufferOffset-105",
        "UetsendStandardheaderformattypeSesRequestWithSom1InitiatorId": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.initiatorId-106",
        "UetsendStandardheaderformattypeSesRequestWithSom1MatchBits": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.matchBits-107",
        "UetsendStandardheaderformattypeSesRequestWithSom1HeaderData": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.headerData-108",
        "UetsendStandardheaderformattypeSesRequestWithSom1RequestLength": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom1.requestLength-109",
        "UetsendStandardheaderformattypeSesRequestWithSom0Reserved1": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.reserved1-110",
        "UetsendStandardheaderformattypeSesRequestWithSom0OpCode": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.opCode-111",
        "UetsendStandardheaderformattypeSesRequestWithSom0Version": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.version-112",
        "UetsendStandardheaderformattypeSesRequestWithSom0DeliveryComplete": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.deliveryComplete-113",
        "UetsendStandardheaderformattypeSesRequestWithSom0InitiatorError": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.initiatorError-114",
        "UetsendStandardheaderformattypeSesRequestWithSom0Relative": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.relative-115",
        "UetsendStandardheaderformattypeSesRequestWithSom0HeaderDataPresent": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.headerDataPresent-116",
        "UetsendStandardheaderformattypeSesRequestWithSom0EndOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.endOfMsg-117",
        "UetsendStandardheaderformattypeSesRequestWithSom0StartOfMsg": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.startOfMsg-118",
        "UetsendStandardheaderformattypeSesRequestWithSom0MessageId": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.messageId-119",
        "UetsendStandardheaderformattypeSesRequestWithSom0RiGeneration": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.riGeneration-120",
        "UetsendStandardheaderformattypeSesRequestWithSom0JobId": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.jobId-121",
        "UetsendStandardheaderformattypeSesRequestWithSom0Reserved2": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.Reserved2-122",
        "UetsendStandardheaderformattypeSesRequestWithSom0PidOnFEP": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.pidOnFEP-123",
        "UetsendStandardheaderformattypeSesRequestWithSom0Reserved3": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.Reserved3-124",
        "UetsendStandardheaderformattypeSesRequestWithSom0ResourceIndex": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.resourceIndex-125",
        "UetsendStandardheaderformattypeSesRequestWithSom0BufferOffset": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.bufferOffset-126",
        "UetsendStandardheaderformattypeSesRequestWithSom0InitiatorId": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.initiatorId-127",
        "UetsendStandardheaderformattypeSesRequestWithSom0MatchBits": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.matchBits-128",
        "UetsendStandardheaderformattypeSesRequestWithSom0Reserved4": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.Reserved4-129",
        "UetsendStandardheaderformattypeSesRequestWithSom0PayloadLength": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.payloadLength-130",
        "UetsendStandardheaderformattypeSesRequestWithSom0MessageOffset": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.messageOffset-131",
        "UetsendStandardheaderformattypeSesRequestWithSom0RequestLength": "uetSesRequestStandard.header.sesOpCodeType.uetSend.standardHeaderFormatType.sesRequestWithSom0.requestLength-132",
    }

    def __init__(self, parent, list_op=False):
        super(UetSesRequestStandard, self).__init__(parent, list_op)

    @property
    def SesRequestWithSom1Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1Reserved1"])
        )

    @property
    def SesRequestWithSom1OpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_WRITE, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1OpCode"])
        )

    @property
    def SesRequestWithSom1Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1Version"])
        )

    @property
    def SesRequestWithSom1DeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SesRequestWithSom1DeliveryComplete"]
            ),
        )

    @property
    def SesRequestWithSom1InitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1InitiatorError"]),
        )

    @property
    def SesRequestWithSom1Relative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1Relative"])
        )

    @property
    def SesRequestWithSom1HeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SesRequestWithSom1HeaderDataPresent"]
            ),
        )

    @property
    def SesRequestWithSom1EndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1EndOfMsg"])
        )

    @property
    def SesRequestWithSom1StartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1StartOfMsg"])
        )

    @property
    def SesRequestWithSom1MessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1MessageId"])
        )

    @property
    def SesRequestWithSom1RiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1RiGeneration"]),
        )

    @property
    def SesRequestWithSom1JobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1JobId"])
        )

    @property
    def SesRequestWithSom1Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1Reserved2"])
        )

    @property
    def SesRequestWithSom1PidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1PidOnFEP"])
        )

    @property
    def SesRequestWithSom1Reserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1Reserved3"])
        )

    @property
    def SesRequestWithSom1ResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1ResourceIndex"]),
        )

    @property
    def SesRequestWithSom1BufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1BufferOffset"]),
        )

    @property
    def SesRequestWithSom1InitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1InitiatorId"]),
        )

    @property
    def SesRequestWithSom1MatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1MatchBits"])
        )

    @property
    def SesRequestWithSom1HeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1HeaderData"])
        )

    @property
    def SesRequestWithSom1RequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom1RequestLength"]),
        )

    @property
    def SesRequestWithSom0Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0Reserved1"])
        )

    @property
    def SesRequestWithSom0OpCode(self):
        """
        Display Name: Op Code
        Default Value: 1
        Value Format: decimal
        Available enum values: UET_WRITE, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0OpCode"])
        )

    @property
    def SesRequestWithSom0Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0Version"])
        )

    @property
    def SesRequestWithSom0DeliveryComplete(self):
        """
        Display Name: Delivery Complete
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SesRequestWithSom0DeliveryComplete"]
            ),
        )

    @property
    def SesRequestWithSom0InitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0InitiatorError"]),
        )

    @property
    def SesRequestWithSom0Relative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0Relative"])
        )

    @property
    def SesRequestWithSom0HeaderDataPresent(self):
        """
        Display Name: Header Data Present
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SesRequestWithSom0HeaderDataPresent"]
            ),
        )

    @property
    def SesRequestWithSom0EndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0EndOfMsg"])
        )

    @property
    def SesRequestWithSom0StartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0StartOfMsg"])
        )

    @property
    def SesRequestWithSom0MessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0MessageId"])
        )

    @property
    def SesRequestWithSom0RiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0RiGeneration"]),
        )

    @property
    def SesRequestWithSom0JobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0JobId"])
        )

    @property
    def SesRequestWithSom0Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0Reserved2"])
        )

    @property
    def SesRequestWithSom0PidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0PidOnFEP"])
        )

    @property
    def SesRequestWithSom0Reserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0Reserved3"])
        )

    @property
    def SesRequestWithSom0ResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0ResourceIndex"]),
        )

    @property
    def SesRequestWithSom0BufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0BufferOffset"]),
        )

    @property
    def SesRequestWithSom0InitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0InitiatorId"]),
        )

    @property
    def SesRequestWithSom0MatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0MatchBits"])
        )

    @property
    def SesRequestWithSom0Reserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0Reserved4"])
        )

    @property
    def SesRequestWithSom0PayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0PayloadLength"]),
        )

    @property
    def SesRequestWithSom0MessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0MessageOffset"]),
        )

    @property
    def SesRequestWithSom0RequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SesRequestWithSom0RequestLength"]),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1Reserved1"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1OpCode(self):
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
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1OpCode"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1Version"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1DeliveryComplete(self):
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
                    "StandardheaderformattypeSesRequestWithSom1DeliveryComplete"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1InitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1InitiatorError"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1Relative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1Relative"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1HeaderDataPresent(self):
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
                    "StandardheaderformattypeSesRequestWithSom1HeaderDataPresent"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1EndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1EndOfMsg"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1StartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1StartOfMsg"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1MessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1MessageId"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1RiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1RiGeneration"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1JobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1JobId"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1Reserved2"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1PidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1PidOnFEP"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1Reserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1Reserved3"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1ResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1ResourceIndex"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1BufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1BufferOffset"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1InitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1InitiatorId"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1MatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom1MatchBits"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1HeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1HeaderData"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom1RequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom1RequestLength"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0Reserved1"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0OpCode(self):
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
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0OpCode"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0Version"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0DeliveryComplete(self):
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
                    "StandardheaderformattypeSesRequestWithSom0DeliveryComplete"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0InitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0InitiatorError"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0Relative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0Relative"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0HeaderDataPresent(self):
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
                    "StandardheaderformattypeSesRequestWithSom0HeaderDataPresent"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0EndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0EndOfMsg"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0StartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0StartOfMsg"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0MessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0MessageId"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0RiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0RiGeneration"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0JobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0JobId"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0Reserved2"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0PidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0PidOnFEP"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0Reserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0Reserved3"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0ResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0ResourceIndex"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0BufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0BufferOffset"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0InitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0InitiatorId"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0MatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0MatchBits"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0Reserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StandardheaderformattypeSesRequestWithSom0Reserved4"]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0PayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0PayloadLength"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0MessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0MessageOffset"
                ]
            ),
        )

    @property
    def StandardheaderformattypeSesRequestWithSom0RequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "StandardheaderformattypeSesRequestWithSom0RequestLength"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1Reserved1"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1OpCode(self):
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
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1OpCode"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1Version"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1DeliveryComplete(self):
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
                    "UetsendStandardheaderformattypeSesRequestWithSom1DeliveryComplete"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1InitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1InitiatorError"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1Relative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1Relative"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1HeaderDataPresent(self):
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
                    "UetsendStandardheaderformattypeSesRequestWithSom1HeaderDataPresent"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1EndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1EndOfMsg"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1StartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1StartOfMsg"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1MessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1MessageId"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1RiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1RiGeneration"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1JobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1JobId"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1Reserved2"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1PidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1PidOnFEP"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1Reserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1Reserved3"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1ResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1ResourceIndex"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1BufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1BufferOffset"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1InitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1InitiatorId"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1MatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1MatchBits"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1HeaderData(self):
        """
        Display Name: Header Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1HeaderData"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom1RequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom1RequestLength"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0Reserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0Reserved1"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0OpCode(self):
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
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0OpCode"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0Version"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0DeliveryComplete(self):
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
                    "UetsendStandardheaderformattypeSesRequestWithSom0DeliveryComplete"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0InitiatorError(self):
        """
        Display Name: Initiator Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0InitiatorError"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0Relative(self):
        """
        Display Name: Relative
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0Relative"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0HeaderDataPresent(self):
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
                    "UetsendStandardheaderformattypeSesRequestWithSom0HeaderDataPresent"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0EndOfMsg(self):
        """
        Display Name: End Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0EndOfMsg"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0StartOfMsg(self):
        """
        Display Name: Start Of Msg
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0StartOfMsg"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0MessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0MessageId"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0RiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0RiGeneration"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0JobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0JobId"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0Reserved2"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0PidOnFEP(self):
        """
        Display Name: PID on FEP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0PidOnFEP"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0Reserved3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0Reserved3"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0ResourceIndex(self):
        """
        Display Name: Resource Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0ResourceIndex"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0BufferOffset(self):
        """
        Display Name: Buffer Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0BufferOffset"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0InitiatorId(self):
        """
        Display Name: Initiator Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0InitiatorId"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0MatchBits(self):
        """
        Display Name: Match Bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0MatchBits"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0Reserved4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0Reserved4"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0PayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0PayloadLength"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0MessageOffset(self):
        """
        Display Name: Message Offset
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0MessageOffset"
                ]
            ),
        )

    @property
    def UetsendStandardheaderformattypeSesRequestWithSom0RequestLength(self):
        """
        Display Name: Request Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "UetsendStandardheaderformattypeSesRequestWithSom0RequestLength"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
