from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OamCCM(Base):
    __slots__ = ()
    _SDM_NAME = "oamCCM"
    _SDM_ATT_MAP = {
        "OamCCMMessegeMdLevel": "oamCCM.header.oamPacketType.oamCCMMessege.mdLevel-1",
        "OamCCMMessegeVersion": "oamCCM.header.oamPacketType.oamCCMMessege.version-2",
        "OamCCMMessegeOpCode": "oamCCM.header.oamPacketType.oamCCMMessege.opCode-3",
        "FlagsRdiField": "oamCCM.header.oamPacketType.oamCCMMessege.flags.rdiField-4",
        "FlagsReserved": "oamCCM.header.oamPacketType.oamCCMMessege.flags.reserved-5",
        "FlagsCcmInterval": "oamCCM.header.oamPacketType.oamCCMMessege.flags.ccmInterval-6",
        "OamCCMMessegeFirstTLVOffset": "oamCCM.header.oamPacketType.oamCCMMessege.firstTLVOffset-7",
        "OamCCMMessegeTransactionIdentifier": "oamCCM.header.oamPacketType.oamCCMMessege.transactionIdentifier-8",
        "OamCCMMessegeMaintenanceEndPointIdentifier": "oamCCM.header.oamPacketType.oamCCMMessege.maintenanceEndPointIdentifier-9",
        "OamCCMMessegeMaintenanceDomainNameFormat": "oamCCM.header.oamPacketType.oamCCMMessege.maintenanceDomainNameFormat-10",
        "OamCCMMessegeMaintenanceDomainNameLength": "oamCCM.header.oamPacketType.oamCCMMessege.maintenanceDomainNameLength-11",
        "OamCCMMessegeMaintenanceDomainName": "oamCCM.header.oamPacketType.oamCCMMessege.maintenanceDomainName-12",
        "OamCCMMessegeShortMANameFormat": "oamCCM.header.oamPacketType.oamCCMMessege.shortMANameFormat-13",
        "OamCCMMessegeShortMANameLength": "oamCCM.header.oamPacketType.oamCCMMessege.shortMANameLength-14",
        "OamCCMMessegeShortMAName": "oamCCM.header.oamPacketType.oamCCMMessege.shortMAName-15",
        "OrganisationSpecificTLVTlvType": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.organisationSpecificTLV.tlvType-16",
        "OrganisationSpecificTLVTlvLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.organisationSpecificTLV.tlvLength-17",
        "OrganisationSpecificTLVOui": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.organisationSpecificTLV.oui-18",
        "OrganisationSpecificTLVSubType": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.organisationSpecificTLV.subType-19",
        "ValueFieldsValueLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.valueLength-20",
        "ValueFieldsValue": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.value-21",
        "PortIDTLVTlvType": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.tlvType-22",
        "PortIDTLVTlvLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.tlvLength-23",
        "PortIDTLVChassisIDLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.chassisIDLength-24",
        "PortIDTLVChassisIDSubtypeField": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.chassisIDSubtypeField-25",
        "PortIDTLVVariableChassisIDLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.variableChassisIDLength-26",
        "PortIDTLVChassisID": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.chassisID-27",
        "PortIDTLVPortIDLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.portIDLength-28",
        "PortIDTLVPortIDSubtypeField": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.portIDSubtypeField-29",
        "PortIDTLVVariablePortIDLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.variablePortIDLength-30",
        "PortIDTLVPortID": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.portID-31",
        "PortIDTLVManagementAddressLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.managementAddressLength-32",
        "PortIDTLVManagementAddress": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.portIDTLV.managementAddress-33",
        "MacStatusTLVTlvCode": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.macStatusTLV.tlvCode-34",
        "MacStatusTLVTlvLength": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.macStatusTLV.tlvLength-35",
        "MacStatusTLVPortStatus": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.macStatusTLV.portStatus-36",
        "TlvHeaderEndTLVCode": "oamCCM.header.oamPacketType.oamCCMMessege.tlvHeader.tlvHeader.endTLVCode-37",
        "OamLoopbackMessegeReplyMdLevel": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.mdLevel-38",
        "OamLoopbackMessegeReplyVersion": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.version-39",
        "OamLoopbackMessegeReplyOpCode": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.opCode-40",
        "OamLoopbackMessegeReplyFlags": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.flags-41",
        "OamLoopbackMessegeReplyFirstTLVOffset": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.firstTLVOffset-42",
        "OamLoopbackMessegeReplyTransactionIdentifier": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.transactionIdentifier-43",
        "TlvheaderOrganisationSpecificTLVTlvType": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.organisationSpecificTLV.tlvType-44",
        "TlvheaderOrganisationSpecificTLVTlvLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.organisationSpecificTLV.tlvLength-45",
        "TlvheaderOrganisationSpecificTLVOui": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.organisationSpecificTLV.oui-46",
        "TlvheaderOrganisationSpecificTLVSubType": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.organisationSpecificTLV.subType-47",
        "OrganisationspecifictlvValueFieldsValueLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.valueLength-48",
        "OrganisationspecifictlvValueFieldsValue": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.value-49",
        "TlvheaderPortIDTLVTlvType": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.tlvType-50",
        "TlvheaderPortIDTLVTlvLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.tlvLength-51",
        "TlvheaderPortIDTLVChassisIDLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.chassisIDLength-52",
        "TlvheaderPortIDTLVChassisIDSubtypeField": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.chassisIDSubtypeField-53",
        "TlvheaderPortIDTLVVariableChassisIDLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.variableChassisIDLength-54",
        "TlvheaderPortIDTLVChassisID": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.chassisID-55",
        "TlvheaderPortIDTLVPortIDLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.portIDLength-56",
        "TlvheaderPortIDTLVPortIDSubtypeField": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.portIDSubtypeField-57",
        "TlvheaderPortIDTLVVariablePortIDLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.variablePortIDLength-58",
        "TlvheaderPortIDTLVPortID": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.portID-59",
        "TlvheaderPortIDTLVManagementAddressLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.managementAddressLength-60",
        "TlvheaderPortIDTLVManagementAddress": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.portIDTLV.managementAddress-61",
        "DataTLVTlvCode": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.dataTLV.tlvCode-62",
        "DataTLVTlvLength": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.dataTLV.tlvLength-63",
        "DataTLVData": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.dataTLV.data-64",
        "TlvheaderTlvHeaderEndTLVCode": "oamCCM.header.oamPacketType.oamLoopbackMessegeReply.tlvHeader.tlvHeader.endTLVCode-65",
        "OamLinkTraceMessegeMdLevel": "oamCCM.header.oamPacketType.oamLinkTraceMessege.mdLevel-66",
        "OamLinkTraceMessegeVersion": "oamCCM.header.oamPacketType.oamLinkTraceMessege.version-67",
        "OamLinkTraceMessegeOpCode": "oamCCM.header.oamPacketType.oamLinkTraceMessege.opCode-68",
        "FlagsHwonlyField": "oamCCM.header.oamPacketType.oamLinkTraceMessege.flags.hwonlyField-69",
        "OamlinktracemessegeFlagsReserved": "oamCCM.header.oamPacketType.oamLinkTraceMessege.flags.reserved-70",
        "OamLinkTraceMessegeFirstTLVOffset": "oamCCM.header.oamPacketType.oamLinkTraceMessege.firstTLVOffset-71",
        "OamLinkTraceMessegeTransactionIdentifier": "oamCCM.header.oamPacketType.oamLinkTraceMessege.transactionIdentifier-72",
        "OamLinkTraceMessegeLtmTTL": "oamCCM.header.oamPacketType.oamLinkTraceMessege.ltmTTL-73",
        "OamLinkTraceMessegeOriginalAddress": "oamCCM.header.oamPacketType.oamLinkTraceMessege.originalAddress-74",
        "OamLinkTraceMessegeTargetAddress": "oamCCM.header.oamPacketType.oamLinkTraceMessege.targetAddress-75",
        "TlvheaderTlvheaderOrganisationSpecificTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.organisationSpecificTLV.tlvType-76",
        "TlvheaderTlvheaderOrganisationSpecificTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.organisationSpecificTLV.tlvLength-77",
        "TlvheaderTlvheaderOrganisationSpecificTLVOui": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.organisationSpecificTLV.oui-78",
        "TlvheaderTlvheaderOrganisationSpecificTLVSubType": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.organisationSpecificTLV.subType-79",
        "TlvheaderOrganisationspecifictlvValueFieldsValueLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.valueLength-80",
        "TlvheaderOrganisationspecifictlvValueFieldsValue": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.value-81",
        "TlvheaderTlvheaderPortIDTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.tlvType-82",
        "TlvheaderTlvheaderPortIDTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.tlvLength-83",
        "TlvheaderTlvheaderPortIDTLVChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.chassisIDLength-84",
        "TlvheaderTlvheaderPortIDTLVChassisIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.chassisIDSubtypeField-85",
        "TlvheaderTlvheaderPortIDTLVVariableChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.variableChassisIDLength-86",
        "TlvheaderTlvheaderPortIDTLVChassisID": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.chassisID-87",
        "TlvheaderTlvheaderPortIDTLVPortIDLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.portIDLength-88",
        "TlvheaderTlvheaderPortIDTLVPortIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.portIDSubtypeField-89",
        "TlvheaderTlvheaderPortIDTLVVariablePortIDLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.variablePortIDLength-90",
        "TlvheaderTlvheaderPortIDTLVPortID": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.portID-91",
        "TlvheaderTlvheaderPortIDTLVManagementAddressLength": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.managementAddressLength-92",
        "TlvheaderTlvheaderPortIDTLVManagementAddress": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.portIDTLV.managementAddress-93",
        "OamlinktracemessegeTlvheaderTlvHeaderEndTLVCode": "oamCCM.header.oamPacketType.oamLinkTraceMessege.tlvHeader.tlvHeader.endTLVCode-94",
        "OamLinkTraceReplyMdLevel": "oamCCM.header.oamPacketType.oamLinkTraceReply.mdLevel-95",
        "OamLinkTraceReplyVersion": "oamCCM.header.oamPacketType.oamLinkTraceReply.version-96",
        "OamLinkTraceReplyOpCode": "oamCCM.header.oamPacketType.oamLinkTraceReply.opCode-97",
        "FlagsFwdYesField": "oamCCM.header.oamPacketType.oamLinkTraceReply.flags.fwdYesField-98",
        "OamlinktracereplyFlagsReserved": "oamCCM.header.oamPacketType.oamLinkTraceReply.flags.reserved-99",
        "OamLinkTraceReplyFirstTLVOffset": "oamCCM.header.oamPacketType.oamLinkTraceReply.firstTLVOffset-100",
        "OamLinkTraceReplyTransactionIdentifier": "oamCCM.header.oamPacketType.oamLinkTraceReply.transactionIdentifier-101",
        "OamLinkTraceReplyReplyTTL": "oamCCM.header.oamPacketType.oamLinkTraceReply.replyTTL-102",
        "OamLinkTraceReplyRelayAction": "oamCCM.header.oamPacketType.oamLinkTraceReply.relayAction-103",
        "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.organisationSpecificTLV.tlvType-104",
        "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.organisationSpecificTLV.tlvLength-105",
        "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVOui": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.organisationSpecificTLV.oui-106",
        "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVSubType": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.organisationSpecificTLV.subType-107",
        "TlvheaderTlvheaderOrganisationspecifictlvValueFieldsValueLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.valueLength-108",
        "TlvheaderTlvheaderOrganisationspecifictlvValueFieldsValue": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.organisationSpecificTLV.valueFields.value-109",
        "ReplyInformationTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.tlvType-110",
        "ReplyInformationTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.tlvLength-111",
        "ReplyInformationTLVReplyChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.replyChassisIDLength-112",
        "ChassisInfoReplyChassisIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.chassisInfo.replyChassisIDSubtypeField-113",
        "ChassisInfoVariableChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.chassisInfo.variableChassisIDLength-114",
        "ChassisInfoReplyChassisID": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.chassisInfo.replyChassisID-115",
        "ReplyInformationTLVReplyManagementAddressLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.replyManagementAddressLength-116",
        "ReplyInformationTLVReplyManagementAddress": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyInformationTLV.replyManagementAddress-117",
        "ReplyIngressTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.tlvType-118",
        "ReplyIngressTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.tlvLength-119",
        "ReplyIngressTLVIngressAction": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.ingressAction-120",
        "ReplyIngressTLVIngressMacAddress": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.ingressMacAddress-121",
        "IngressPortIDInfoIngressPortIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.ingressPortIDInfo.ingressPortIDLength-122",
        "IngressPortIDInfoIngressPortIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.ingressPortIDInfo.ingressPortIDSubtypeField-123",
        "IngressPortIDInfoVariableChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.ingressPortIDInfo.variableChassisIDLength-124",
        "IngressPortIDInfoIngressPortID": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyIngressTLV.ingressPortIDInfo.ingressPortID-125",
        "ReplyEgressTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.tlvType-126",
        "ReplyEgressTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.tlvLength-127",
        "ReplyEgressTLVEgressAction": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.egressAction-128",
        "ReplyEgressTLVEgressMacAddress": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.egressMacAddress-129",
        "EgressPortIDInfoEgressPortIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.egressPortIDInfo.egressPortIDLength-130",
        "EgressPortIDInfoEgressPortIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.egressPortIDInfo.egressPortIDSubtypeField-131",
        "EgressPortIDInfoVariableChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.egressPortIDInfo.variableChassisIDLength-132",
        "EgressPortIDInfoEgressPortID": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.replyEgressTLV.egressPortIDInfo.egressPortID-133",
        "NextHopIdentifierTLVTlvType": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.tlvType-134",
        "NextHopIdentifierTLVTlvLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.tlvLength-135",
        "NextHopIdentifierTLVChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.chassisIDLength-136",
        "NextHopIdentifierTLVChassisIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.chassisIDSubtypeField-137",
        "NextHopIdentifierTLVVariableChassisIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.variableChassisIDLength-138",
        "NextHopIdentifierTLVChassisID": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.chassisID-139",
        "NextHopIdentifierTLVPortIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.portIDLength-140",
        "NextHopIdentifierTLVPortIDSubtypeField": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.portIDSubtypeField-141",
        "NextHopIdentifierTLVVariablePortIDLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.variablePortIDLength-142",
        "NextHopIdentifierTLVPortID": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.portID-143",
        "NextHopIdentifierTLVManagementAddressLength": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.managementAddressLength-144",
        "NextHopIdentifierTLVManagementAddress": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.nextHopIdentifierTLV.managementAddress-145",
        "OamlinktracereplyTlvheaderTlvHeaderEndTLVCode": "oamCCM.header.oamPacketType.oamLinkTraceReply.tlvHeader.tlvHeader.endTLVCode-146",
    }

    def __init__(self, parent, list_op=False):
        super(OamCCM, self).__init__(parent, list_op)

    @property
    def OamCCMMessegeMdLevel(self):
        """
        Display Name: MD Level
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeMdLevel"])
        )

    @property
    def OamCCMMessegeVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeVersion"])
        )

    @property
    def OamCCMMessegeOpCode(self):
        """
        Display Name: OpCode
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeOpCode"])
        )

    @property
    def FlagsRdiField(self):
        """
        Display Name: RDI Field
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsRdiField"]))

    @property
    def FlagsReserved(self):
        """
        Display Name: Reserved
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved"]))

    @property
    def FlagsCcmInterval(self):
        """
        Display Name: CCM Interval
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsCcmInterval"])
        )

    @property
    def OamCCMMessegeFirstTLVOffset(self):
        """
        Display Name: First TLV Offset
        Default Value: 0x46
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeFirstTLVOffset"])
        )

    @property
    def OamCCMMessegeTransactionIdentifier(self):
        """
        Display Name: Transaction Identifier
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamCCMMessegeTransactionIdentifier"]
            ),
        )

    @property
    def OamCCMMessegeMaintenanceEndPointIdentifier(self):
        """
        Display Name: Maintenance End Point Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamCCMMessegeMaintenanceEndPointIdentifier"]
            ),
        )

    @property
    def OamCCMMessegeMaintenanceDomainNameFormat(self):
        """
        Display Name: Maintenance Domain name Format
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamCCMMessegeMaintenanceDomainNameFormat"]
            ),
        )

    @property
    def OamCCMMessegeMaintenanceDomainNameLength(self):
        """
        Display Name: Maintenance Domain name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamCCMMessegeMaintenanceDomainNameLength"]
            ),
        )

    @property
    def OamCCMMessegeMaintenanceDomainName(self):
        """
        Display Name: Maintenance Domain name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamCCMMessegeMaintenanceDomainName"]
            ),
        )

    @property
    def OamCCMMessegeShortMANameFormat(self):
        """
        Display Name: Short MA Name Format
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeShortMANameFormat"]),
        )

    @property
    def OamCCMMessegeShortMANameLength(self):
        """
        Display Name: Short MA Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeShortMANameLength"]),
        )

    @property
    def OamCCMMessegeShortMAName(self):
        """
        Display Name: Short MA Name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamCCMMessegeShortMAName"])
        )

    @property
    def OrganisationSpecificTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganisationSpecificTLVTlvType"]),
        )

    @property
    def OrganisationSpecificTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganisationSpecificTLVTlvLength"]),
        )

    @property
    def OrganisationSpecificTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OrganisationSpecificTLVOui"])
        )

    @property
    def OrganisationSpecificTLVSubType(self):
        """
        Display Name: Sub-Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OrganisationSpecificTLVSubType"]),
        )

    @property
    def ValueFieldsValueLength(self):
        """
        Display Name: Value length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsValueLength"])
        )

    @property
    def ValueFieldsValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsValue"])
        )

    @property
    def PortIDTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVTlvType"])
        )

    @property
    def PortIDTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVTlvLength"])
        )

    @property
    def PortIDTLVChassisIDLength(self):
        """
        Display Name: Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVChassisIDLength"])
        )

    @property
    def PortIDTLVChassisIDSubtypeField(self):
        """
        Display Name: Chassis ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortIDTLVChassisIDSubtypeField"]),
        )

    @property
    def PortIDTLVVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortIDTLVVariableChassisIDLength"]),
        )

    @property
    def PortIDTLVChassisID(self):
        """
        Display Name: Chassis ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVChassisID"])
        )

    @property
    def PortIDTLVPortIDLength(self):
        """
        Display Name: Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVPortIDLength"])
        )

    @property
    def PortIDTLVPortIDSubtypeField(self):
        """
        Display Name: Port ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVPortIDSubtypeField"])
        )

    @property
    def PortIDTLVVariablePortIDLength(self):
        """
        Display Name: Variable Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortIDTLVVariablePortIDLength"]),
        )

    @property
    def PortIDTLVPortID(self):
        """
        Display Name: Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVPortID"])
        )

    @property
    def PortIDTLVManagementAddressLength(self):
        """
        Display Name: Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortIDTLVManagementAddressLength"]),
        )

    @property
    def PortIDTLVManagementAddress(self):
        """
        Display Name: Management Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIDTLVManagementAddress"])
        )

    @property
    def MacStatusTLVTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacStatusTLVTlvCode"])
        )

    @property
    def MacStatusTLVTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacStatusTLVTlvLength"])
        )

    @property
    def MacStatusTLVPortStatus(self):
        """
        Display Name: Port Status
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacStatusTLVPortStatus"])
        )

    @property
    def TlvHeaderEndTLVCode(self):
        """
        Display Name: End TLV code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvHeaderEndTLVCode"])
        )

    @property
    def OamLoopbackMessegeReplyMdLevel(self):
        """
        Display Name: MD Level
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamLoopbackMessegeReplyMdLevel"]),
        )

    @property
    def OamLoopbackMessegeReplyVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamLoopbackMessegeReplyVersion"]),
        )

    @property
    def OamLoopbackMessegeReplyOpCode(self):
        """
        Display Name: OpCode
        Default Value: 2
        Value Format: decimal
        Available enum values: LBM, 2, LBR, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamLoopbackMessegeReplyOpCode"]),
        )

    @property
    def OamLoopbackMessegeReplyFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLoopbackMessegeReplyFlags"])
        )

    @property
    def OamLoopbackMessegeReplyFirstTLVOffset(self):
        """
        Display Name: First TLV Offset
        Default Value: 0x4
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamLoopbackMessegeReplyFirstTLVOffset"]
            ),
        )

    @property
    def OamLoopbackMessegeReplyTransactionIdentifier(self):
        """
        Display Name: Transaction Identifier
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamLoopbackMessegeReplyTransactionIdentifier"]
            ),
        )

    @property
    def TlvheaderOrganisationSpecificTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderOrganisationSpecificTLVTlvType"]
            ),
        )

    @property
    def TlvheaderOrganisationSpecificTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderOrganisationSpecificTLVTlvLength"]
            ),
        )

    @property
    def TlvheaderOrganisationSpecificTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderOrganisationSpecificTLVOui"]
            ),
        )

    @property
    def TlvheaderOrganisationSpecificTLVSubType(self):
        """
        Display Name: Sub-Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderOrganisationSpecificTLVSubType"]
            ),
        )

    @property
    def OrganisationspecifictlvValueFieldsValueLength(self):
        """
        Display Name: Value length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OrganisationspecifictlvValueFieldsValueLength"]
            ),
        )

    @property
    def OrganisationspecifictlvValueFieldsValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OrganisationspecifictlvValueFieldsValue"]
            ),
        )

    @property
    def TlvheaderPortIDTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvheaderPortIDTLVTlvType"])
        )

    @property
    def TlvheaderPortIDTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvheaderPortIDTLVTlvLength"])
        )

    @property
    def TlvheaderPortIDTLVChassisIDLength(self):
        """
        Display Name: Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvheaderPortIDTLVChassisIDLength"]),
        )

    @property
    def TlvheaderPortIDTLVChassisIDSubtypeField(self):
        """
        Display Name: Chassis ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderPortIDTLVChassisIDSubtypeField"]
            ),
        )

    @property
    def TlvheaderPortIDTLVVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderPortIDTLVVariableChassisIDLength"]
            ),
        )

    @property
    def TlvheaderPortIDTLVChassisID(self):
        """
        Display Name: Chassis ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvheaderPortIDTLVChassisID"])
        )

    @property
    def TlvheaderPortIDTLVPortIDLength(self):
        """
        Display Name: Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvheaderPortIDTLVPortIDLength"]),
        )

    @property
    def TlvheaderPortIDTLVPortIDSubtypeField(self):
        """
        Display Name: Port ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderPortIDTLVPortIDSubtypeField"]
            ),
        )

    @property
    def TlvheaderPortIDTLVVariablePortIDLength(self):
        """
        Display Name: Variable Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderPortIDTLVVariablePortIDLength"]
            ),
        )

    @property
    def TlvheaderPortIDTLVPortID(self):
        """
        Display Name: Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvheaderPortIDTLVPortID"])
        )

    @property
    def TlvheaderPortIDTLVManagementAddressLength(self):
        """
        Display Name: Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderPortIDTLVManagementAddressLength"]
            ),
        )

    @property
    def TlvheaderPortIDTLVManagementAddress(self):
        """
        Display Name: Management Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderPortIDTLVManagementAddress"]
            ),
        )

    @property
    def DataTLVTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataTLVTlvCode"])
        )

    @property
    def DataTLVTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataTLVTlvLength"])
        )

    @property
    def DataTLVData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataTLVData"]))

    @property
    def TlvheaderTlvHeaderEndTLVCode(self):
        """
        Display Name: End TLV code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvheaderTlvHeaderEndTLVCode"])
        )

    @property
    def OamLinkTraceMessegeMdLevel(self):
        """
        Display Name: MD Level
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceMessegeMdLevel"])
        )

    @property
    def OamLinkTraceMessegeVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceMessegeVersion"])
        )

    @property
    def OamLinkTraceMessegeOpCode(self):
        """
        Display Name: OpCode
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceMessegeOpCode"])
        )

    @property
    def FlagsHwonlyField(self):
        """
        Display Name: HWOnly Field
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsHwonlyField"])
        )

    @property
    def OamlinktracemessegeFlagsReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamlinktracemessegeFlagsReserved"]),
        )

    @property
    def OamLinkTraceMessegeFirstTLVOffset(self):
        """
        Display Name: First TLV Offset
        Default Value: 0x11
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceMessegeFirstTLVOffset"]),
        )

    @property
    def OamLinkTraceMessegeTransactionIdentifier(self):
        """
        Display Name: Transaction Identifier
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamLinkTraceMessegeTransactionIdentifier"]
            ),
        )

    @property
    def OamLinkTraceMessegeLtmTTL(self):
        """
        Display Name: LTM TTL
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceMessegeLtmTTL"])
        )

    @property
    def OamLinkTraceMessegeOriginalAddress(self):
        """
        Display Name: Original Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamLinkTraceMessegeOriginalAddress"]
            ),
        )

    @property
    def OamLinkTraceMessegeTargetAddress(self):
        """
        Display Name: Target Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceMessegeTargetAddress"]),
        )

    @property
    def TlvheaderTlvheaderOrganisationSpecificTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderOrganisationSpecificTLVTlvType"]
            ),
        )

    @property
    def TlvheaderTlvheaderOrganisationSpecificTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderOrganisationSpecificTLVTlvLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderOrganisationSpecificTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderOrganisationSpecificTLVOui"]
            ),
        )

    @property
    def TlvheaderTlvheaderOrganisationSpecificTLVSubType(self):
        """
        Display Name: Sub-Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderOrganisationSpecificTLVSubType"]
            ),
        )

    @property
    def TlvheaderOrganisationspecifictlvValueFieldsValueLength(self):
        """
        Display Name: Value length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheaderOrganisationspecifictlvValueFieldsValueLength"
                ]
            ),
        )

    @property
    def TlvheaderOrganisationspecifictlvValueFieldsValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderOrganisationspecifictlvValueFieldsValue"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVTlvType"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVTlvLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVChassisIDLength(self):
        """
        Display Name: Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVChassisIDLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVChassisIDSubtypeField(self):
        """
        Display Name: Chassis ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVChassisIDSubtypeField"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVVariableChassisIDLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVChassisID(self):
        """
        Display Name: Chassis ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVChassisID"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVPortIDLength(self):
        """
        Display Name: Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVPortIDLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVPortIDSubtypeField(self):
        """
        Display Name: Port ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVPortIDSubtypeField"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVVariablePortIDLength(self):
        """
        Display Name: Variable Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVVariablePortIDLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVPortID(self):
        """
        Display Name: Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVPortID"]),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVManagementAddressLength(self):
        """
        Display Name: Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVManagementAddressLength"]
            ),
        )

    @property
    def TlvheaderTlvheaderPortIDTLVManagementAddress(self):
        """
        Display Name: Management Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderTlvheaderPortIDTLVManagementAddress"]
            ),
        )

    @property
    def OamlinktracemessegeTlvheaderTlvHeaderEndTLVCode(self):
        """
        Display Name: End TLV code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamlinktracemessegeTlvheaderTlvHeaderEndTLVCode"]
            ),
        )

    @property
    def OamLinkTraceReplyMdLevel(self):
        """
        Display Name: MD Level
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceReplyMdLevel"])
        )

    @property
    def OamLinkTraceReplyVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceReplyVersion"])
        )

    @property
    def OamLinkTraceReplyOpCode(self):
        """
        Display Name: OpCode
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceReplyOpCode"])
        )

    @property
    def FlagsFwdYesField(self):
        """
        Display Name: FwdYes Field
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsFwdYesField"])
        )

    @property
    def OamlinktracereplyFlagsReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamlinktracereplyFlagsReserved"]),
        )

    @property
    def OamLinkTraceReplyFirstTLVOffset(self):
        """
        Display Name: First TLV Offset
        Default Value: 0x6
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceReplyFirstTLVOffset"]),
        )

    @property
    def OamLinkTraceReplyTransactionIdentifier(self):
        """
        Display Name: Transaction Identifier
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamLinkTraceReplyTransactionIdentifier"]
            ),
        )

    @property
    def OamLinkTraceReplyReplyTTL(self):
        """
        Display Name: Reply TTL
        Default Value: 63
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceReplyReplyTTL"])
        )

    @property
    def OamLinkTraceReplyRelayAction(self):
        """
        Display Name: Relay Action
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OamLinkTraceReplyRelayAction"])
        )

    @property
    def OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVTlvType"
                ]
            ),
        )

    @property
    def OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVTlvLength"
                ]
            ),
        )

    @property
    def OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVOui(self):
        """
        Display Name: OUI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVOui"
                ]
            ),
        )

    @property
    def OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVSubType(self):
        """
        Display Name: Sub-Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OamlinktracereplyTlvheaderTlvheaderOrganisationSpecificTLVSubType"
                ]
            ),
        )

    @property
    def TlvheaderTlvheaderOrganisationspecifictlvValueFieldsValueLength(self):
        """
        Display Name: Value length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheaderTlvheaderOrganisationspecifictlvValueFieldsValueLength"
                ]
            ),
        )

    @property
    def TlvheaderTlvheaderOrganisationspecifictlvValueFieldsValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheaderTlvheaderOrganisationspecifictlvValueFieldsValue"
                ]
            ),
        )

    @property
    def ReplyInformationTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyInformationTLVTlvType"])
        )

    @property
    def ReplyInformationTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyInformationTLVTlvLength"])
        )

    @property
    def ReplyInformationTLVReplyChassisIDLength(self):
        """
        Display Name: Reply Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyInformationTLVReplyChassisIDLength"]
            ),
        )

    @property
    def ChassisInfoReplyChassisIDSubtypeField(self):
        """
        Display Name: Reply Chassis ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChassisInfoReplyChassisIDSubtypeField"]
            ),
        )

    @property
    def ChassisInfoVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChassisInfoVariableChassisIDLength"]
            ),
        )

    @property
    def ChassisInfoReplyChassisID(self):
        """
        Display Name: Reply Chassis ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisInfoReplyChassisID"])
        )

    @property
    def ReplyInformationTLVReplyManagementAddressLength(self):
        """
        Display Name: Reply Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyInformationTLVReplyManagementAddressLength"]
            ),
        )

    @property
    def ReplyInformationTLVReplyManagementAddress(self):
        """
        Display Name: Reply Management Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReplyInformationTLVReplyManagementAddress"]
            ),
        )

    @property
    def ReplyIngressTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVTlvType"])
        )

    @property
    def ReplyIngressTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVTlvLength"])
        )

    @property
    def ReplyIngressTLVIngressAction(self):
        """
        Display Name: Ingress Action
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVIngressAction"])
        )

    @property
    def ReplyIngressTLVIngressMacAddress(self):
        """
        Display Name: Ingress Mac Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyIngressTLVIngressMacAddress"]),
        )

    @property
    def IngressPortIDInfoIngressPortIDLength(self):
        """
        Display Name: Ingress Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IngressPortIDInfoIngressPortIDLength"]
            ),
        )

    @property
    def IngressPortIDInfoIngressPortIDSubtypeField(self):
        """
        Display Name: Ingress Port ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IngressPortIDInfoIngressPortIDSubtypeField"]
            ),
        )

    @property
    def IngressPortIDInfoVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IngressPortIDInfoVariableChassisIDLength"]
            ),
        )

    @property
    def IngressPortIDInfoIngressPortID(self):
        """
        Display Name: Ingress Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IngressPortIDInfoIngressPortID"]),
        )

    @property
    def ReplyEgressTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVTlvType"])
        )

    @property
    def ReplyEgressTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVTlvLength"])
        )

    @property
    def ReplyEgressTLVEgressAction(self):
        """
        Display Name: Egress Action
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVEgressAction"])
        )

    @property
    def ReplyEgressTLVEgressMacAddress(self):
        """
        Display Name: Egress Mac Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReplyEgressTLVEgressMacAddress"]),
        )

    @property
    def EgressPortIDInfoEgressPortIDLength(self):
        """
        Display Name: Egress Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EgressPortIDInfoEgressPortIDLength"]
            ),
        )

    @property
    def EgressPortIDInfoEgressPortIDSubtypeField(self):
        """
        Display Name: Egress Port ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EgressPortIDInfoEgressPortIDSubtypeField"]
            ),
        )

    @property
    def EgressPortIDInfoVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EgressPortIDInfoVariableChassisIDLength"]
            ),
        )

    @property
    def EgressPortIDInfoEgressPortID(self):
        """
        Display Name: Egress Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressPortIDInfoEgressPortID"])
        )

    @property
    def NextHopIdentifierTLVTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopIdentifierTLVTlvType"])
        )

    @property
    def NextHopIdentifierTLVTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NextHopIdentifierTLVTlvLength"]),
        )

    @property
    def NextHopIdentifierTLVChassisIDLength(self):
        """
        Display Name: Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVChassisIDLength"]
            ),
        )

    @property
    def NextHopIdentifierTLVChassisIDSubtypeField(self):
        """
        Display Name: Chassis ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVChassisIDSubtypeField"]
            ),
        )

    @property
    def NextHopIdentifierTLVVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVVariableChassisIDLength"]
            ),
        )

    @property
    def NextHopIdentifierTLVChassisID(self):
        """
        Display Name: Chassis ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NextHopIdentifierTLVChassisID"]),
        )

    @property
    def NextHopIdentifierTLVPortIDLength(self):
        """
        Display Name: Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NextHopIdentifierTLVPortIDLength"]),
        )

    @property
    def NextHopIdentifierTLVPortIDSubtypeField(self):
        """
        Display Name: Port ID Subtype Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVPortIDSubtypeField"]
            ),
        )

    @property
    def NextHopIdentifierTLVVariablePortIDLength(self):
        """
        Display Name: Variable Port ID Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVVariablePortIDLength"]
            ),
        )

    @property
    def NextHopIdentifierTLVPortID(self):
        """
        Display Name: Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopIdentifierTLVPortID"])
        )

    @property
    def NextHopIdentifierTLVManagementAddressLength(self):
        """
        Display Name: Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVManagementAddressLength"]
            ),
        )

    @property
    def NextHopIdentifierTLVManagementAddress(self):
        """
        Display Name: Management Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextHopIdentifierTLVManagementAddress"]
            ),
        )

    @property
    def OamlinktracereplyTlvheaderTlvHeaderEndTLVCode(self):
        """
        Display Name: End TLV code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OamlinktracereplyTlvheaderTlvHeaderEndTLVCode"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
