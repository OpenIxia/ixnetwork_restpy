from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Lldp(Base):
    __slots__ = ()
    _SDM_NAME = "lldp"
    _SDM_ATT_MAP = {
        "ChassisIdTlvType": "lldp.header.mandatoryTlv.chassisIdTlv.type-1",
        "ChassisIdTlvLength": "lldp.header.mandatoryTlv.chassisIdTlv.length-2",
        "ChassisIdTlvSubtype": "lldp.header.mandatoryTlv.chassisIdTlv.subtype-3",
        "ChassisIdTlvVariableChassisIDLength": "lldp.header.mandatoryTlv.chassisIdTlv.variableChassisIDLength-4",
        "ChassisIdTlvChassisId": "lldp.header.mandatoryTlv.chassisIdTlv.chassisId-5",
        "PortIdTlvType": "lldp.header.mandatoryTlv.portIdTlv.type-6",
        "PortIdTlvLength": "lldp.header.mandatoryTlv.portIdTlv.length-7",
        "PortIdTlvSubtype": "lldp.header.mandatoryTlv.portIdTlv.subtype-8",
        "PortIdTlvVariablePortIDLength": "lldp.header.mandatoryTlv.portIdTlv.variablePortIDLength-9",
        "PortIdTlvPortId": "lldp.header.mandatoryTlv.portIdTlv.portId-10",
        "TtlTlvType": "lldp.header.mandatoryTlv.ttlTlv.type-11",
        "TtlTlvLength": "lldp.header.mandatoryTlv.ttlTlv.length-12",
        "TtlTlvTtl": "lldp.header.mandatoryTlv.ttlTlv.ttl-13",
        "DescriptionTlvType": "lldp.header.optionalTlvs.tlvs.descriptionTlv.type-14",
        "DescriptionTlvLength": "lldp.header.optionalTlvs.tlvs.descriptionTlv.length-15",
        "DescriptionTlvDescription": "lldp.header.optionalTlvs.tlvs.descriptionTlv.description-16",
        "SystemNameTlvType": "lldp.header.optionalTlvs.tlvs.systemNameTlv.type-17",
        "SystemNameTlvLength": "lldp.header.optionalTlvs.tlvs.systemNameTlv.length-18",
        "SystemNameTlvSystemName": "lldp.header.optionalTlvs.tlvs.systemNameTlv.systemName-19",
        "SystemDescriptionTlvType": "lldp.header.optionalTlvs.tlvs.systemDescriptionTlv.type-20",
        "SystemDescriptionTlvLength": "lldp.header.optionalTlvs.tlvs.systemDescriptionTlv.length-21",
        "SystemDescriptionTlvDescription": "lldp.header.optionalTlvs.tlvs.systemDescriptionTlv.description-22",
        "SystemCapabTlvType": "lldp.header.optionalTlvs.tlvs.systemCapabTlv.type-23",
        "SystemCapabTlvLength": "lldp.header.optionalTlvs.tlvs.systemCapabTlv.length-24",
        "SystemCapabTlvSystemCapabilities": "lldp.header.optionalTlvs.tlvs.systemCapabTlv.systemCapabilities-25",
        "SystemCapabTlvEnabledCapabilities": "lldp.header.optionalTlvs.tlvs.systemCapabTlv.enabledCapabilities-26",
        "ManagementTlvType": "lldp.header.optionalTlvs.tlvs.managementTlv.type-27",
        "ManagementTlvLength": "lldp.header.optionalTlvs.tlvs.managementTlv.length-28",
        "ManagementTlvStringLength": "lldp.header.optionalTlvs.tlvs.managementTlv.stringLength-29",
        "ManagementTlvSubtype": "lldp.header.optionalTlvs.tlvs.managementTlv.subtype-30",
        "ManagementTlvVariableMgmtAddressLength": "lldp.header.optionalTlvs.tlvs.managementTlv.variableMgmtAddressLength-31",
        "ManagementTlvMgmtAddress": "lldp.header.optionalTlvs.tlvs.managementTlv.mgmtAddress-32",
        "ManagementTlvNumberingSubtype": "lldp.header.optionalTlvs.tlvs.managementTlv.numberingSubtype-33",
        "ManagementTlvIntNumber": "lldp.header.optionalTlvs.tlvs.managementTlv.intNumber-34",
        "ManagementTlvOidStringLength": "lldp.header.optionalTlvs.tlvs.managementTlv.oidStringLength-35",
        "ManagementTlvOid": "lldp.header.optionalTlvs.tlvs.managementTlv.oid-36",
        "PortVlanIdTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portVlanIdTlv.type-37",
        "PortVlanIdTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portVlanIdTlv.length-38",
        "PortVlanIdTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portVlanIdTlv.oui-39",
        "PortVlanIdTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portVlanIdTlv.subtype-40",
        "PortVlanIdTlvPvid": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portVlanIdTlv.pvid-41",
        "PortProtocolVlanIdTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.type-42",
        "PortProtocolVlanIdTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.length-43",
        "PortProtocolVlanIdTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.oui-44",
        "PortProtocolVlanIdTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.subtype-45",
        "PortProtocolVlanIdTlvFlag_reserved": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.flag_reserved-46",
        "PortProtocolVlanIdTlvVlanSupported": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.vlanSupported-47",
        "PortProtocolVlanIdTlvVlanEnabled": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.vlanEnabled-48",
        "PortProtocolVlanIdTlvFlagZero": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.flagZero-49",
        "PortProtocolVlanIdTlvVlanId": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.portProtocolVlanIdTlv.vlanId-50",
        "VlanNameTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.type-51",
        "VlanNameTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.length-52",
        "VlanNameTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.oui-53",
        "VlanNameTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.subtype-54",
        "VlanNameTlvVlanId": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.vlanId-55",
        "VlanNameTlvVlanNameLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.vlanNameLength-56",
        "VlanNameTlvVlanName": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.vlanNameTlv.vlanName-57",
        "ProtocolIdentityTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.protocolIdentityTlv.type-58",
        "ProtocolIdentityTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.protocolIdentityTlv.length-59",
        "ProtocolIdentityTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.protocolIdentityTlv.oui-60",
        "ProtocolIdentityTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.protocolIdentityTlv.subtype-61",
        "ProtocolIdentityTlvIdentityLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.protocolIdentityTlv.identityLength-62",
        "ProtocolIdentityTlvIdentity": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.protocolIdentityTlv.identity-63",
        "EvbTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.type-64",
        "EvbTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.length-65",
        "EvbTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.oui-66",
        "EvbTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.subtype-67",
        "EvbBridgeStatusReserved": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbBridgeStatus.reserved-68",
        "EvbBridgeStatusBgid": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbBridgeStatus.bgid-69",
        "EvbBridgeStatusRrCap": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbBridgeStatus.rrCap-70",
        "EvbBridgeStatusRrCtl": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbBridgeStatus.rrCtl-71",
        "EvbStationStatusReserved": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbStationStatus.reserved-72",
        "EvbStationStatusSgid": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbStationStatus.sgid-73",
        "EvbStationStatusRrReq": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbStationStatus.rrReq-74",
        "EvbStationStatusRrStat": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbStationStatus.rrStat-75",
        "EvbTlvEvbRetries": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbRetries-76",
        "EvbTlvEvbRte": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbRte-77",
        "EvbTlvEvbMode": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbMode-78",
        "EvbTlvEvbROLRWD": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbROLRWD-79",
        "EvbTlvEvbRWD": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbRWD-80",
        "EvbTlvReserved": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.reserved-81",
        "EvbTlvEvbROLRKA": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbROLRKA-82",
        "EvbTlvEvbRKA": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.evbTlv.evbRKA-83",
        "CdcpTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.type-84",
        "CdcpTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.length-85",
        "CdcpTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.oui-86",
        "CdcpTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.subtype-87",
        "CdcpStationRoleCdcpStationRoleField": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.cdcpRole.cdcpStationRole.cdcpStationRoleField-88",
        "CdcpBridgeRoleCdcpBridgeRoleField": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.cdcpRole.cdcpBridgeRole.cdcpBridgeRoleField-89",
        "CdcpTlvReserved1": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.reserved1-90",
        "CdcpTlvSComp": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.sComp-91",
        "CdcpTlvReserved2": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.reserved2-92",
        "CdcpTlvChannelCap": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.channelCap-93",
        "Scid_svidsScid": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.scid_svids.scid-94",
        "Scid_svidsSvid": "lldp.header.organizationalTlvs.tlvs.optionalDot1Tlvs.dot1.cdcpTlv.scid_svids.svid-95",
        "MacConfigStatusType": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.type-96",
        "MacConfigStatusLength": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.length-97",
        "MacConfigStatusOui": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.oui-98",
        "MacConfigStatusSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.subtype-99",
        "MacConfigStatusAutoNegSupport": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.autoNegSupport-100",
        "MacConfigStatusAutoNegStatus": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.autoNegStatus-101",
        "MacConfigStatusZero": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.zero-102",
        "MacConfigStatusPmdAutoNegCapability": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.pmdAutoNegCapability-103",
        "MacConfigStatusOperationalMauType": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..macConfigStatus.operationalMauType-104",
        "PowerViaMdiTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.type-105",
        "PowerViaMdiTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.length-106",
        "PowerViaMdiTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.oui-107",
        "PowerViaMdiTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.subtype-108",
        "PowerViaMdiTlvMdiPowerSupport": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.mdiPowerSupport-109",
        "PowerViaMdiTlvPsePowerPair": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.psePowerPair-110",
        "PowerViaMdiTlvPowerClass": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..powerViaMdiTlv.powerClass-111",
        "LinkAggregationTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..linkAggregationTlv.type-112",
        "LinkAggregationTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..linkAggregationTlv.length-113",
        "LinkAggregationTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..linkAggregationTlv.oui-114",
        "LinkAggregationTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..linkAggregationTlv.subtype-115",
        "LinkAggregationTlvStatus": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..linkAggregationTlv.status-116",
        "LinkAggregationTlvPortId": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..linkAggregationTlv.portId-117",
        "MaximumFrameSizeTlvType": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..maximumFrameSizeTlv.type-118",
        "MaximumFrameSizeTlvLength": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..maximumFrameSizeTlv.length-119",
        "MaximumFrameSizeTlvOui": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..maximumFrameSizeTlv.oui-120",
        "MaximumFrameSizeTlvSubtype": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..maximumFrameSizeTlv.subtype-121",
        "MaximumFrameSizeTlvFrameSize": "lldp.header.organizationalTlvs.tlvs.optionalDot3Tlvs..maximumFrameSizeTlv.frameSize-122",
        "ProtocolTlvType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.type-123",
        "ProtocolTlvLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.length-124",
        "ProtocolTlvOui": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.oui-125",
        "ProtocolTlvSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.subtype-126",
        "ProtocolControlTlvType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.protocolControlTlv.type-127",
        "ProtocolControlTlvLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.protocolControlTlv.length-128",
        "ProtocolControlTlvOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.protocolControlTlv.operVersion-129",
        "ProtocolControlTlvMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.protocolControlTlv.maxVersion-130",
        "ProtocolControlTlvSeqNo": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.protocolControlTlv.seqNo-131",
        "ProtocolControlTlvAckNo": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.protocolControlTlv.ackNo-132",
        "HeaderType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.type-133",
        "HeaderLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.length-134",
        "HeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.operVersion-135",
        "HeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.maxVersion-136",
        "HeaderEnable": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.enable-137",
        "HeaderWilling": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.willing-138",
        "HeaderError": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.error-139",
        "HeaderReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.reserved-140",
        "HeaderSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.header.subtype-141",
        "Bwg_alloc_tableBwg_bw0": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw0-142",
        "Bwg_alloc_tableBwg_bw1": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw1-143",
        "Bwg_alloc_tableBwg_bw2": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw2-144",
        "Bwg_alloc_tableBwg_bw3": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw3-145",
        "Bwg_alloc_tableBwg_bw4": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw4-146",
        "Bwg_alloc_tableBwg_bw5": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw5-147",
        "Bwg_alloc_tableBwg_bw6": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw6-148",
        "Bwg_alloc_tableBwg_bw7": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.bwg_alloc_table.bwg_bw7-149",
        "PgSet0Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet0.id-150",
        "PgSet0Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet0.prio-151",
        "PgSet0Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet0.unused-152",
        "PgSet0BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet0.bwPer-153",
        "PgSet1Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet1.id-154",
        "PgSet1Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet1.prio-155",
        "PgSet1Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet1.unused-156",
        "PgSet1BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet1.bwPer-157",
        "PgSet2Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet2.id-158",
        "PgSet2Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet2.prio-159",
        "PgSet2Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet2.unused-160",
        "PgSet2BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet2.bwPer-161",
        "PgSet3Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet3.id-162",
        "PgSet3Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet3.prio-163",
        "PgSet3Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet3.unused-164",
        "PgSet3BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet3.bwPer-165",
        "PgSet4Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet4.id-166",
        "PgSet4Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet4.prio-167",
        "PgSet4Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet4.unused-168",
        "PgSet4BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet4.bwPer-169",
        "PgSet5Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet5.id-170",
        "PgSet5Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet5.prio-171",
        "PgSet5Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet5.unused-172",
        "PgSet5BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet5.bwPer-173",
        "PgSet6Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet6.id-174",
        "PgSet6Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet6.prio-175",
        "PgSet6Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet6.unused-176",
        "PgSet6BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet6.bwPer-177",
        "PgSet7Id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet7.id-178",
        "PgSet7Prio": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet7.prio-179",
        "PgSet7Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet7.unused-180",
        "PgSet7BwPer": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgSet7.bwPer-181",
        "PriorityflowtlvHeaderType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.type-182",
        "PriorityflowtlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.length-183",
        "PriorityflowtlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.operVersion-184",
        "PriorityflowtlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.maxVersion-185",
        "PriorityflowtlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.enable-186",
        "PriorityflowtlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.willing-187",
        "PriorityflowtlvHeaderError": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.error-188",
        "PriorityflowtlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.reserved-189",
        "PriorityflowtlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.header.subtype-190",
        "AdminMapPe7": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe7-191",
        "AdminMapPe6": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe6-192",
        "AdminMapPe5": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe5-193",
        "AdminMapPe4": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe4-194",
        "AdminMapPe3": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe3-195",
        "AdminMapPe2": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe2-196",
        "AdminMapPe1": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe1-197",
        "AdminMapPe0": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.priorityFlowTlv.cfg.adminMap.pe0-198",
        "BcntlvHeaderType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.type-199",
        "BcntlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.length-200",
        "BcntlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.operVersion-201",
        "BcntlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.maxVersion-202",
        "BcntlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.enable-203",
        "BcntlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.willing-204",
        "BcntlvHeaderError": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.error-205",
        "BcntlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.reserved-206",
        "BcntlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.header.subtype-207",
        "CfgBcna": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcna-208",
        "Set1CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set1.cpAdmin-209",
        "Set1RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set1.rpAdmin-210",
        "Set1RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set1.rpOper-211",
        "Set1RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set1.remOper-212",
        "Set1Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set1.unused-213",
        "Set2CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set2.cpAdmin-214",
        "Set2RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set2.rpAdmin-215",
        "Set2RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set2.rpOper-216",
        "Set2RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set2.remOper-217",
        "Set2Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set2.unused-218",
        "Set3CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set3.cpAdmin-219",
        "Set3RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set3.rpAdmin-220",
        "Set3RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set3.rpOper-221",
        "Set3RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set3.remOper-222",
        "Set3Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set3.unused-223",
        "Set4CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set4.cpAdmin-224",
        "Set4RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set4.rpAdmin-225",
        "Set4RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set4.rpOper-226",
        "Set4RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set4.remOper-227",
        "Set4Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set4.unused-228",
        "Set5CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set5.cpAdmin-229",
        "Set5RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set5.rpAdmin-230",
        "Set5RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set5.rpOper-231",
        "Set5RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set5.remOper-232",
        "Set5Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set5.unused-233",
        "Set6CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set6.cpAdmin-234",
        "Set6RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set6.rpAdmin-235",
        "Set6RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set6.rpOper-236",
        "Set6RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set6.remOper-237",
        "Set6Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set6.unused-238",
        "Set7CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set7.cpAdmin-239",
        "Set7RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set7.rpAdmin-240",
        "Set7RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set7.rpOper-241",
        "Set7RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set7.remOper-242",
        "Set7Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set7.unused-243",
        "Set8CpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set8.cpAdmin-244",
        "Set8RpAdmin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set8.rpAdmin-245",
        "Set8RpOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set8.rpOper-246",
        "Set8RemOper": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set8.remOper-247",
        "Set8Unused": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.bcnSet.set8.unused-248",
        "CfgRpAlpha": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpAlpha-249",
        "CfgRpBeta": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpBeta-250",
        "CfgRpGd": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpGd-251",
        "CfgRpGi": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpGi-252",
        "CfgRpTmax": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpTmax-253",
        "CfgCpSf": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.cpSf-254",
        "CfgRpTd": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpTd-255",
        "CfgRpMin": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpMin-256",
        "CfgRpW": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpW-257",
        "CfgRpRd": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.bcnTlv.cfg.rpRd-258",
        "ApplicationtlvHeaderType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.type-259",
        "ApplicationtlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.length-260",
        "ApplicationtlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.operVersion-261",
        "ApplicationtlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.maxVersion-262",
        "ApplicationtlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.enable-263",
        "ApplicationtlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.willing-264",
        "ApplicationtlvHeaderError": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.error-265",
        "ApplicationtlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.reserved-266",
        "ApplicationtlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.header.subtype-267",
        "UserPriorityMapPe7": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe7-268",
        "UserPriorityMapPe6": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe6-269",
        "UserPriorityMapPe5": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe5-270",
        "UserPriorityMapPe4": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe4-271",
        "UserPriorityMapPe3": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe3-272",
        "UserPriorityMapPe2": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe2-273",
        "UserPriorityMapPe1": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe1-274",
        "UserPriorityMapPe0": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.applicationTlv.cfg.fcoeTlv.userPriorityMap.pe0-275",
        "LogicallinkdowntlvHeaderType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.type-276",
        "LogicallinkdowntlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.length-277",
        "LogicallinkdowntlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.operVersion-278",
        "LogicallinkdowntlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.maxVersion-279",
        "LogicallinkdowntlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.enable-280",
        "LogicallinkdowntlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.willing-281",
        "LogicallinkdowntlvHeaderError": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.error-282",
        "LogicallinkdowntlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.reserved-283",
        "LogicallinkdowntlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.header.subtype-284",
        "FcoeStatusStatus": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.cfg.fcoeStatus.status-285",
        "FcoeStatusReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.cfg.fcoeStatus.reserved-286",
        "LanStatusStatus": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.cfg.lanStatus.status-287",
        "LanStatusReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.logicalLinkDownTlv.cfg.lanStatus.reserved-288",
        "NivtlvHeaderType": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.type-289",
        "NivtlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.length-290",
        "NivtlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.operVersion-291",
        "NivtlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.maxVersion-292",
        "NivtlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.enable-293",
        "NivtlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.willing-294",
        "NivtlvHeaderError": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.error-295",
        "NivtlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.reserved-296",
        "NivtlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.header.subtype-297",
        "CfgVis": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.cfg.vis-298",
        "CfgVntag_vers": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.cfg.vntag_vers-299",
        "CfgVif_id": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.cfg.vif_id-300",
        "CfgMac_addr": "lldp.header.organizationalTlvs.tlvs.intelDcbxTlvs.protocolTlv.optionalIntelDcbxTlvs.subtlvs.nivTlv.cfg.mac_addr-301",
        "IeeedcbxtlvsProtocolTlvType": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.type-302",
        "IeeedcbxtlvsProtocolTlvLength": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.length-303",
        "IeeedcbxtlvsProtocolTlvOui": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.oui-304",
        "IeeedcbxtlvsProtocolTlvSubtype": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.subtype-305",
        "SubtlvsProtocolControlTlvType": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.protocolControlTlv.type-306",
        "SubtlvsProtocolControlTlvLength": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.protocolControlTlv.length-307",
        "SubtlvsProtocolControlTlvOperVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.protocolControlTlv.operVersion-308",
        "SubtlvsProtocolControlTlvMaxVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.protocolControlTlv.maxVersion-309",
        "SubtlvsProtocolControlTlvSeqNo": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.protocolControlTlv.seqNo-310",
        "SubtlvsProtocolControlTlvAckNo": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.protocolControlTlv.ackNo-311",
        "PrioritygrouptlvHeaderType": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.type-312",
        "PrioritygrouptlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.length-313",
        "PrioritygrouptlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.operVersion-314",
        "PrioritygrouptlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.maxVersion-315",
        "PrioritygrouptlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.enable-316",
        "PrioritygrouptlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.willing-317",
        "PrioritygrouptlvHeaderError": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.error-318",
        "PrioritygrouptlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.reserved-319",
        "PrioritygrouptlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.header.subtype-320",
        "Up_alloc_tablePgid0": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid0-321",
        "Up_alloc_tablePgid1": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid1-322",
        "Up_alloc_tablePgid2": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid2-323",
        "Up_alloc_tablePgid3": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid3-324",
        "Up_alloc_tablePgid4": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid4-325",
        "Up_alloc_tablePgid5": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid5-326",
        "Up_alloc_tablePgid6": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid6-327",
        "Up_alloc_tablePgid7": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.up_alloc_table.pgid7-328",
        "Pg_alloc_tableBwPer0": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer0-329",
        "Pg_alloc_tableBwPer1": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer1-330",
        "Pg_alloc_tableBwPer2": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer2-331",
        "Pg_alloc_tableBwPer3": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer3-332",
        "Pg_alloc_tableBwPer4": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer4-333",
        "Pg_alloc_tableBwPer5": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer5-334",
        "Pg_alloc_tableBwPer6": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer6-335",
        "Pg_alloc_tableBwPer7": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.pg_alloc_table.bwPer7-336",
        "CfgNumTCsupported": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityGroupTlv.cfg.numTCsupported-337",
        "SubtlvsPriorityflowtlvHeaderType": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.type-338",
        "SubtlvsPriorityflowtlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.length-339",
        "SubtlvsPriorityflowtlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.operVersion-340",
        "SubtlvsPriorityflowtlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.maxVersion-341",
        "SubtlvsPriorityflowtlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.enable-342",
        "SubtlvsPriorityflowtlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.willing-343",
        "SubtlvsPriorityflowtlvHeaderError": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.error-344",
        "SubtlvsPriorityflowtlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.reserved-345",
        "SubtlvsPriorityflowtlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.header.subtype-346",
        "PrioMapPe7": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe7-347",
        "PrioMapPe6": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe6-348",
        "PrioMapPe5": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe5-349",
        "PrioMapPe4": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe4-350",
        "PrioMapPe3": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe3-351",
        "PrioMapPe2": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe2-352",
        "PrioMapPe1": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe1-353",
        "PrioMapPe0": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.prioMap.pe0-354",
        "CfgNumTcpfcsSupp": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.priorityFlowTlv.cfg.numTcpfcsSupp-355",
        "SubtlvsApplicationtlvHeaderType": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.type-356",
        "SubtlvsApplicationtlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.length-357",
        "SubtlvsApplicationtlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.operVersion-358",
        "SubtlvsApplicationtlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.maxVersion-359",
        "SubtlvsApplicationtlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.enable-360",
        "SubtlvsApplicationtlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.willing-361",
        "SubtlvsApplicationtlvHeaderError": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.error-362",
        "SubtlvsApplicationtlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.reserved-363",
        "SubtlvsApplicationtlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.header.subtype-364",
        "AppsTlvsAppProtId": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.appProtId-365",
        "AppsTlvsOui6": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.oui6-366",
        "AppsTlvsSf": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.sf-367",
        "AppsTlvsOui16": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.oui16-368",
        "AppstlvsPrioMapPe7": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe7-369",
        "AppstlvsPrioMapPe6": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe6-370",
        "AppstlvsPrioMapPe5": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe5-371",
        "AppstlvsPrioMapPe4": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe4-372",
        "AppstlvsPrioMapPe3": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe3-373",
        "AppstlvsPrioMapPe2": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe2-374",
        "AppstlvsPrioMapPe1": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe1-375",
        "AppstlvsPrioMapPe0": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.applicationTlv.cfg.appsTlvs.prioMap.pe0-376",
        "SubtlvsNivtlvHeaderType": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.type-377",
        "SubtlvsNivtlvHeaderLength": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.length-378",
        "SubtlvsNivtlvHeaderOperVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.operVersion-379",
        "SubtlvsNivtlvHeaderMaxVersion": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.maxVersion-380",
        "SubtlvsNivtlvHeaderEnable": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.enable-381",
        "SubtlvsNivtlvHeaderWilling": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.willing-382",
        "SubtlvsNivtlvHeaderError": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.error-383",
        "SubtlvsNivtlvHeaderReserved": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.reserved-384",
        "SubtlvsNivtlvHeaderSubtype": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.header.subtype-385",
        "NivtlvCfgVis": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.cfg.vis-386",
        "NivtlvCfgVntag_vers": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.cfg.vntag_vers-387",
        "NivtlvCfgVif_id": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.cfg.vif_id-388",
        "NivtlvCfgMac_addr": "lldp.header.organizationalTlvs.tlvs.ieeeDcbxTlvs.protocolTlv.optionalIeeeDcbxTlvs.subtlvs.nivTlv.cfg.mac_addr-389",
        "EtsConfigurationTlvType": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.type-390",
        "EtsConfigurationTlvLength": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.length-391",
        "EtsConfigurationTlvOui": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.oui-392",
        "EtsConfigurationTlvSubtype": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.subtype-393",
        "EtsConfigurationTlvWilling": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.willing-394",
        "EtsConfigurationTlvCbs": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.cbs-395",
        "EtsConfigurationTlvReserved": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.reserved-396",
        "EtsConfigurationTlvMaxTC": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.maxTC-397",
        "PriorityAssignTablePriority0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority0-398",
        "PriorityAssignTablePriority1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority1-399",
        "PriorityAssignTablePriority2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority2-400",
        "PriorityAssignTablePriority3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority3-401",
        "PriorityAssignTablePriority4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority4-402",
        "PriorityAssignTablePriority5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority5-403",
        "PriorityAssignTablePriority6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority6-404",
        "PriorityAssignTablePriority7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.priorityAssignTable.priority7-405",
        "TcBandwidthTableTc0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc0-406",
        "TcBandwidthTableTc1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc1-407",
        "TcBandwidthTableTc2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc2-408",
        "TcBandwidthTableTc3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc3-409",
        "TcBandwidthTableTc4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc4-410",
        "TcBandwidthTableTc5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc5-411",
        "TcBandwidthTableTc6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc6-412",
        "TcBandwidthTableTc7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tcBandwidthTable.tc7-413",
        "TsaAssignmentTableTc0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc0-414",
        "TsaAssignmentTableTc1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc1-415",
        "TsaAssignmentTableTc2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc2-416",
        "TsaAssignmentTableTc3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc3-417",
        "TsaAssignmentTableTc4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc4-418",
        "TsaAssignmentTableTc5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc5-419",
        "TsaAssignmentTableTc6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc6-420",
        "TsaAssignmentTableTc7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsConfigurationTlv.tsaAssignmentTable.tc7-421",
        "EtsRecommandationTlvType": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.type-422",
        "EtsRecommandationTlvLength": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.length-423",
        "EtsRecommandationTlvOui": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.oui-424",
        "EtsRecommandationTlvSubtype": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.subtype-425",
        "EtsRecommandationTlvReserved": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.reserved-426",
        "EtsrecommandationtlvPriorityAssignTablePriority0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority0-427",
        "EtsrecommandationtlvPriorityAssignTablePriority1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority1-428",
        "EtsrecommandationtlvPriorityAssignTablePriority2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority2-429",
        "EtsrecommandationtlvPriorityAssignTablePriority3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority3-430",
        "EtsrecommandationtlvPriorityAssignTablePriority4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority4-431",
        "EtsrecommandationtlvPriorityAssignTablePriority5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority5-432",
        "EtsrecommandationtlvPriorityAssignTablePriority6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority6-433",
        "EtsrecommandationtlvPriorityAssignTablePriority7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.priorityAssignTable.priority7-434",
        "EtsrecommandationtlvTcBandwidthTableTc0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc0-435",
        "EtsrecommandationtlvTcBandwidthTableTc1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc1-436",
        "EtsrecommandationtlvTcBandwidthTableTc2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc2-437",
        "EtsrecommandationtlvTcBandwidthTableTc3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc3-438",
        "EtsrecommandationtlvTcBandwidthTableTc4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc4-439",
        "EtsrecommandationtlvTcBandwidthTableTc5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc5-440",
        "EtsrecommandationtlvTcBandwidthTableTc6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc6-441",
        "EtsrecommandationtlvTcBandwidthTableTc7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tcBandwidthTable.tc7-442",
        "EtsrecommandationtlvTsaAssignmentTableTc0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc0-443",
        "EtsrecommandationtlvTsaAssignmentTableTc1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc1-444",
        "EtsrecommandationtlvTsaAssignmentTableTc2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc2-445",
        "EtsrecommandationtlvTsaAssignmentTableTc3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc3-446",
        "EtsrecommandationtlvTsaAssignmentTableTc4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc4-447",
        "EtsrecommandationtlvTsaAssignmentTableTc5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc5-448",
        "EtsrecommandationtlvTsaAssignmentTableTc6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc6-449",
        "EtsrecommandationtlvTsaAssignmentTableTc7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.etsRecommandationTlv.tsaAssignmentTable.tc7-450",
        "PriorityBasedFlowControlTlvType": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.type-451",
        "PriorityBasedFlowControlTlvLength": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.length-452",
        "PriorityBasedFlowControlTlvOui": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.oui-453",
        "PriorityBasedFlowControlTlvSubtype": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.subtype-454",
        "PriorityBasedFlowControlTlvWilling": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.willing-455",
        "PriorityBasedFlowControlTlvMbc": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.mbc-456",
        "PriorityBasedFlowControlTlvReserved": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.reserved-457",
        "PriorityBasedFlowControlTlvPfcCap": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcCap-458",
        "PfcEnablePriority7": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority7-459",
        "PfcEnablePriority6": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority6-460",
        "PfcEnablePriority5": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority5-461",
        "PfcEnablePriority4": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority4-462",
        "PfcEnablePriority3": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority3-463",
        "PfcEnablePriority2": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority2-464",
        "PfcEnablePriority1": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority1-465",
        "PfcEnablePriority0": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.priorityBasedFlowControlTlv.pfcEnable.priority0-466",
        "ApplicationPriorityTlvType": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.type-467",
        "ApplicationPriorityTlvLength": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.length-468",
        "ApplicationPriorityTlvOui": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.oui-469",
        "ApplicationPriorityTlvSubtype": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.subtype-470",
        "ApplicationPriorityTlvReserved": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.reserved-471",
        "AppPriorityTablePriority": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.appPriorityTable.priority-472",
        "AppPriorityTableReserved": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.appPriorityTable.reserved-473",
        "AppPriorityTableSel": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.appPriorityTable.sel-474",
        "AppPriorityTableProtocolId": "lldp.header.organizationalTlvs.tlvs.dot1qaz.tlvs.applicationPriorityTlv.appPriorityTable.protocolId-475",
        "EndLldpTlvType": "lldp.header.endLldpTlv.type-476",
        "EndLldpTlvLength": "lldp.header.endLldpTlv.length-477",
    }

    def __init__(self, parent, list_op=False):
        super(Lldp, self).__init__(parent, list_op)

    @property
    def ChassisIdTlvType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisIdTlvType"])
        )

    @property
    def ChassisIdTlvLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisIdTlvLength"])
        )

    @property
    def ChassisIdTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 6
        Value Format: decimal
        Available enum values: Chassis component, 1, Interface alias, 2, Port component, 3, MAC address, 4, Network address, 5, Interface name, 6, Locally assigned, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisIdTlvSubtype"])
        )

    @property
    def ChassisIdTlvVariableChassisIDLength(self):
        """
        Display Name: Variable Chassis ID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChassisIdTlvVariableChassisIDLength"]
            ),
        )

    @property
    def ChassisIdTlvChassisId(self):
        """
        Display Name: Chassis ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChassisIdTlvChassisId"])
        )

    @property
    def PortIdTlvType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortIdTlvType"]))

    @property
    def PortIdTlvLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIdTlvLength"])
        )

    @property
    def PortIdTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 5
        Value Format: decimal
        Available enum values: Interface alias, 1, Port component, 2, MAC address, 3, Network address, 4, Interface name, 5, Agent Circuit ID, 6, Locally assigned, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIdTlvSubtype"])
        )

    @property
    def PortIdTlvVariablePortIDLength(self):
        """
        Display Name: Variable Port ID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortIdTlvVariablePortIDLength"]),
        )

    @property
    def PortIdTlvPortId(self):
        """
        Display Name: Port ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortIdTlvPortId"])
        )

    @property
    def TtlTlvType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TtlTlvType"]))

    @property
    def TtlTlvLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TtlTlvLength"]))

    @property
    def TtlTlvTtl(self):
        """
        Display Name: Time To Live
        Default Value: 30
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TtlTlvTtl"]))

    @property
    def DescriptionTlvType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DescriptionTlvType"])
        )

    @property
    def DescriptionTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DescriptionTlvLength"])
        )

    @property
    def DescriptionTlvDescription(self):
        """
        Display Name: Port Description
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DescriptionTlvDescription"])
        )

    @property
    def SystemNameTlvType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemNameTlvType"])
        )

    @property
    def SystemNameTlvLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemNameTlvLength"])
        )

    @property
    def SystemNameTlvSystemName(self):
        """
        Display Name: System Name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemNameTlvSystemName"])
        )

    @property
    def SystemDescriptionTlvType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemDescriptionTlvType"])
        )

    @property
    def SystemDescriptionTlvLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemDescriptionTlvLength"])
        )

    @property
    def SystemDescriptionTlvDescription(self):
        """
        Display Name: System Description
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SystemDescriptionTlvDescription"]),
        )

    @property
    def SystemCapabTlvType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemCapabTlvType"])
        )

    @property
    def SystemCapabTlvLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SystemCapabTlvLength"])
        )

    @property
    def SystemCapabTlvSystemCapabilities(self):
        """
        Display Name: System Capabilities
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SystemCapabTlvSystemCapabilities"]),
        )

    @property
    def SystemCapabTlvEnabledCapabilities(self):
        """
        Display Name: Enabled Capabilities
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SystemCapabTlvEnabledCapabilities"]),
        )

    @property
    def ManagementTlvType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvType"])
        )

    @property
    def ManagementTlvLength(self):
        """
        Display Name: Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvLength"])
        )

    @property
    def ManagementTlvStringLength(self):
        """
        Display Name: Management Address String Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvStringLength"])
        )

    @property
    def ManagementTlvSubtype(self):
        """
        Display Name: Management Address Subtype
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvSubtype"])
        )

    @property
    def ManagementTlvVariableMgmtAddressLength(self):
        """
        Display Name: Variable Management Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ManagementTlvVariableMgmtAddressLength"]
            ),
        )

    @property
    def ManagementTlvMgmtAddress(self):
        """
        Display Name: Management Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvMgmtAddress"])
        )

    @property
    def ManagementTlvNumberingSubtype(self):
        """
        Display Name: Interface Numbering Subtype
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ManagementTlvNumberingSubtype"]),
        )

    @property
    def ManagementTlvIntNumber(self):
        """
        Display Name: Interface Number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvIntNumber"])
        )

    @property
    def ManagementTlvOidStringLength(self):
        """
        Display Name: OID String Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvOidStringLength"])
        )

    @property
    def ManagementTlvOid(self):
        """
        Display Name: OID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManagementTlvOid"])
        )

    @property
    def PortVlanIdTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortVlanIdTlvType"])
        )

    @property
    def PortVlanIdTlvLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortVlanIdTlvLength"])
        )

    @property
    def PortVlanIdTlvOui(self):
        """
        Display Name: 802.1 OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortVlanIdTlvOui"])
        )

    @property
    def PortVlanIdTlvSubtype(self):
        """
        Display Name: 802.1 Subtype
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortVlanIdTlvSubtype"])
        )

    @property
    def PortVlanIdTlvPvid(self):
        """
        Display Name: PVID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortVlanIdTlvPvid"])
        )

    @property
    def PortProtocolVlanIdTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvType"])
        )

    @property
    def PortProtocolVlanIdTlvLength(self):
        """
        Display Name: Length
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvLength"])
        )

    @property
    def PortProtocolVlanIdTlvOui(self):
        """
        Display Name: 802.1 OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvOui"])
        )

    @property
    def PortProtocolVlanIdTlvSubtype(self):
        """
        Display Name: 802.1 Subtype
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvSubtype"])
        )

    @property
    def PortProtocolVlanIdTlvFlag_reserved(self):
        """
        Display Name: Flag_reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PortProtocolVlanIdTlvFlag_reserved"]
            ),
        )

    @property
    def PortProtocolVlanIdTlvVlanSupported(self):
        """
        Display Name: Flag Port and protocol VLAN supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PortProtocolVlanIdTlvVlanSupported"]
            ),
        )

    @property
    def PortProtocolVlanIdTlvVlanEnabled(self):
        """
        Display Name: Flag Port and protocol VLAN enabled
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvVlanEnabled"]),
        )

    @property
    def PortProtocolVlanIdTlvFlagZero(self):
        """
        Display Name: Flag Zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvFlagZero"]),
        )

    @property
    def PortProtocolVlanIdTlvVlanId(self):
        """
        Display Name: Port and protocol VLAN ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PortProtocolVlanIdTlvVlanId"])
        )

    @property
    def VlanNameTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvType"])
        )

    @property
    def VlanNameTlvLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvLength"])
        )

    @property
    def VlanNameTlvOui(self):
        """
        Display Name: 802.1 OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvOui"])
        )

    @property
    def VlanNameTlvSubtype(self):
        """
        Display Name: 802.1 Subtype
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvSubtype"])
        )

    @property
    def VlanNameTlvVlanId(self):
        """
        Display Name: VLAN ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvVlanId"])
        )

    @property
    def VlanNameTlvVlanNameLength(self):
        """
        Display Name: Vlan Name Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvVlanNameLength"])
        )

    @property
    def VlanNameTlvVlanName(self):
        """
        Display Name: Vlan Name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanNameTlvVlanName"])
        )

    @property
    def ProtocolIdentityTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolIdentityTlvType"])
        )

    @property
    def ProtocolIdentityTlvLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolIdentityTlvLength"])
        )

    @property
    def ProtocolIdentityTlvOui(self):
        """
        Display Name: 802.1 OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolIdentityTlvOui"])
        )

    @property
    def ProtocolIdentityTlvSubtype(self):
        """
        Display Name: 802.1 Subtype
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolIdentityTlvSubtype"])
        )

    @property
    def ProtocolIdentityTlvIdentityLength(self):
        """
        Display Name: Protocol Identity Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ProtocolIdentityTlvIdentityLength"]),
        )

    @property
    def ProtocolIdentityTlvIdentity(self):
        """
        Display Name: Protocol Identity
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolIdentityTlvIdentity"])
        )

    @property
    def EvbTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvType"]))

    @property
    def EvbTlvLength(self):
        """
        Display Name: Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvLength"]))

    @property
    def EvbTlvOui(self):
        """
        Display Name: 802.1 OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvOui"]))

    @property
    def EvbTlvSubtype(self):
        """
        Display Name: EVB Subtype
        Default Value: 0x0D
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvSubtype"]))

    @property
    def EvbBridgeStatusReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbBridgeStatusReserved"])
        )

    @property
    def EvbBridgeStatusBgid(self):
        """
        Display Name: BGID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbBridgeStatusBgid"])
        )

    @property
    def EvbBridgeStatusRrCap(self):
        """
        Display Name: Reflective Relay Capable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbBridgeStatusRrCap"])
        )

    @property
    def EvbBridgeStatusRrCtl(self):
        """
        Display Name: Reflective Relay Control
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbBridgeStatusRrCtl"])
        )

    @property
    def EvbStationStatusReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbStationStatusReserved"])
        )

    @property
    def EvbStationStatusSgid(self):
        """
        Display Name: SGID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbStationStatusSgid"])
        )

    @property
    def EvbStationStatusRrReq(self):
        """
        Display Name: Reflective Relay Request
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbStationStatusRrReq"])
        )

    @property
    def EvbStationStatusRrStat(self):
        """
        Display Name: Reflective Relay Status
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbStationStatusRrStat"])
        )

    @property
    def EvbTlvEvbRetries(self):
        """
        Display Name: Retries
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbRetries"])
        )

    @property
    def EvbTlvEvbRte(self):
        """
        Display Name: Retransmission Exponent
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbRte"]))

    @property
    def EvbTlvEvbMode(self):
        """
        Display Name: EVB Mode
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbMode"]))

    @property
    def EvbTlvEvbROLRWD(self):
        """
        Display Name: Remote or Local (RWD)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbROLRWD"])
        )

    @property
    def EvbTlvEvbRWD(self):
        """
        Display Name: Resource Wait Delay
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbRWD"]))

    @property
    def EvbTlvReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvReserved"])
        )

    @property
    def EvbTlvEvbROLRKA(self):
        """
        Display Name: Remote or Local (RKA)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbROLRKA"])
        )

    @property
    def EvbTlvEvbRKA(self):
        """
        Display Name: Reinit Keep Alive
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EvbTlvEvbRKA"]))

    @property
    def CdcpTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvType"]))

    @property
    def CdcpTlvLength(self):
        """
        Display Name: Length
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvLength"]))

    @property
    def CdcpTlvOui(self):
        """
        Display Name: 802.1 OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvOui"]))

    @property
    def CdcpTlvSubtype(self):
        """
        Display Name: EVB Subtype
        Default Value: 0x0E
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvSubtype"])
        )

    @property
    def CdcpStationRoleCdcpStationRoleField(self):
        """
        Display Name: Station Role
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CdcpStationRoleCdcpStationRoleField"]
            ),
        )

    @property
    def CdcpBridgeRoleCdcpBridgeRoleField(self):
        """
        Display Name: Bridge Role
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CdcpBridgeRoleCdcpBridgeRoleField"]),
        )

    @property
    def CdcpTlvReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvReserved1"])
        )

    @property
    def CdcpTlvSComp(self):
        """
        Display Name: SComp
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvSComp"]))

    @property
    def CdcpTlvReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvReserved2"])
        )

    @property
    def CdcpTlvChannelCap(self):
        """
        Display Name: Channel Capacity
        Default Value: 167
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CdcpTlvChannelCap"])
        )

    @property
    def Scid_svidsScid(self):
        """
        Display Name: S-Channel Index
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Scid_svidsScid"])
        )

    @property
    def Scid_svidsSvid(self):
        """
        Display Name: S-Channel VID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Scid_svidsSvid"])
        )

    @property
    def MacConfigStatusType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusType"])
        )

    @property
    def MacConfigStatusLength(self):
        """
        Display Name: Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusLength"])
        )

    @property
    def MacConfigStatusOui(self):
        """
        Display Name: 802.3 OUI
        Default Value: 0x00120F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusOui"])
        )

    @property
    def MacConfigStatusSubtype(self):
        """
        Display Name: 802.3 Subtype
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusSubtype"])
        )

    @property
    def MacConfigStatusAutoNegSupport(self):
        """
        Display Name: Auto-negociation support
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusAutoNegSupport"]),
        )

    @property
    def MacConfigStatusAutoNegStatus(self):
        """
        Display Name: Auto-negociation status
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusAutoNegStatus"])
        )

    @property
    def MacConfigStatusZero(self):
        """
        Display Name: Zero
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusZero"])
        )

    @property
    def MacConfigStatusPmdAutoNegCapability(self):
        """
        Display Name: PMD auto-negociation advertised capability field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MacConfigStatusPmdAutoNegCapability"]
            ),
        )

    @property
    def MacConfigStatusOperationalMauType(self):
        """
        Display Name: Operational MAU type
        Default Value: 29
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MacConfigStatusOperationalMauType"]),
        )

    @property
    def PowerViaMdiTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvType"])
        )

    @property
    def PowerViaMdiTlvLength(self):
        """
        Display Name: Length
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvLength"])
        )

    @property
    def PowerViaMdiTlvOui(self):
        """
        Display Name: 802.3 OUI
        Default Value: 0x00120F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvOui"])
        )

    @property
    def PowerViaMdiTlvSubtype(self):
        """
        Display Name: 802.3 Subtype
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvSubtype"])
        )

    @property
    def PowerViaMdiTlvMdiPowerSupport(self):
        """
        Display Name: MDI Power Support
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvMdiPowerSupport"]),
        )

    @property
    def PowerViaMdiTlvPsePowerPair(self):
        """
        Display Name: PSE Power Pair
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvPsePowerPair"])
        )

    @property
    def PowerViaMdiTlvPowerClass(self):
        """
        Display Name: Power Class
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PowerViaMdiTlvPowerClass"])
        )

    @property
    def LinkAggregationTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkAggregationTlvType"])
        )

    @property
    def LinkAggregationTlvLength(self):
        """
        Display Name: Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkAggregationTlvLength"])
        )

    @property
    def LinkAggregationTlvOui(self):
        """
        Display Name: 802.3 OUI
        Default Value: 0x00120F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkAggregationTlvOui"])
        )

    @property
    def LinkAggregationTlvSubtype(self):
        """
        Display Name: 802.3 Subtype
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkAggregationTlvSubtype"])
        )

    @property
    def LinkAggregationTlvStatus(self):
        """
        Display Name: Aggregation Status
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkAggregationTlvStatus"])
        )

    @property
    def LinkAggregationTlvPortId(self):
        """
        Display Name: Aggregated Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkAggregationTlvPortId"])
        )

    @property
    def MaximumFrameSizeTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumFrameSizeTlvType"])
        )

    @property
    def MaximumFrameSizeTlvLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumFrameSizeTlvLength"])
        )

    @property
    def MaximumFrameSizeTlvOui(self):
        """
        Display Name: 802.3 OUI
        Default Value: 0x00120F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumFrameSizeTlvOui"])
        )

    @property
    def MaximumFrameSizeTlvSubtype(self):
        """
        Display Name: 802.3 Subtype
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumFrameSizeTlvSubtype"])
        )

    @property
    def MaximumFrameSizeTlvFrameSize(self):
        """
        Display Name: Maximum 802.3 Frame Size
        Default Value: 1512
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumFrameSizeTlvFrameSize"])
        )

    @property
    def ProtocolTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolTlvType"])
        )

    @property
    def ProtocolTlvLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolTlvLength"])
        )

    @property
    def ProtocolTlvOui(self):
        """
        Display Name: OUI
        Default Value: 0x001B21
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolTlvOui"])
        )

    @property
    def ProtocolTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolTlvSubtype"])
        )

    @property
    def ProtocolControlTlvType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolControlTlvType"])
        )

    @property
    def ProtocolControlTlvLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolControlTlvLength"])
        )

    @property
    def ProtocolControlTlvOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ProtocolControlTlvOperVersion"]),
        )

    @property
    def ProtocolControlTlvMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolControlTlvMaxVersion"])
        )

    @property
    def ProtocolControlTlvSeqNo(self):
        """
        Display Name: SeqNo
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolControlTlvSeqNo"])
        )

    @property
    def ProtocolControlTlvAckNo(self):
        """
        Display Name: AckNo
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolControlTlvAckNo"])
        )

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 28
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderOperVersion"])
        )

    @property
    def HeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMaxVersion"])
        )

    @property
    def HeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderEnable"]))

    @property
    def HeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderWilling"]))

    @property
    def HeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderError"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSubtype"]))

    @property
    def Bwg_alloc_tableBwg_bw0(self):
        """
        Display Name: BWG% 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw0"])
        )

    @property
    def Bwg_alloc_tableBwg_bw1(self):
        """
        Display Name: BWG% 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw1"])
        )

    @property
    def Bwg_alloc_tableBwg_bw2(self):
        """
        Display Name: BWG% 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw2"])
        )

    @property
    def Bwg_alloc_tableBwg_bw3(self):
        """
        Display Name: BWG% 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw3"])
        )

    @property
    def Bwg_alloc_tableBwg_bw4(self):
        """
        Display Name: BWG% 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw4"])
        )

    @property
    def Bwg_alloc_tableBwg_bw5(self):
        """
        Display Name: BWG% 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw5"])
        )

    @property
    def Bwg_alloc_tableBwg_bw6(self):
        """
        Display Name: BWG% 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw6"])
        )

    @property
    def Bwg_alloc_tableBwg_bw7(self):
        """
        Display Name: BWG% 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bwg_alloc_tableBwg_bw7"])
        )

    @property
    def PgSet0Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet0Id"]))

    @property
    def PgSet0Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet0Prio"]))

    @property
    def PgSet0Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet0Unused"]))

    @property
    def PgSet0BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet0BwPer"]))

    @property
    def PgSet1Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet1Id"]))

    @property
    def PgSet1Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet1Prio"]))

    @property
    def PgSet1Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet1Unused"]))

    @property
    def PgSet1BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet1BwPer"]))

    @property
    def PgSet2Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet2Id"]))

    @property
    def PgSet2Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet2Prio"]))

    @property
    def PgSet2Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet2Unused"]))

    @property
    def PgSet2BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet2BwPer"]))

    @property
    def PgSet3Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet3Id"]))

    @property
    def PgSet3Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet3Prio"]))

    @property
    def PgSet3Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet3Unused"]))

    @property
    def PgSet3BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet3BwPer"]))

    @property
    def PgSet4Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet4Id"]))

    @property
    def PgSet4Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet4Prio"]))

    @property
    def PgSet4Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet4Unused"]))

    @property
    def PgSet4BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet4BwPer"]))

    @property
    def PgSet5Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet5Id"]))

    @property
    def PgSet5Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet5Prio"]))

    @property
    def PgSet5Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet5Unused"]))

    @property
    def PgSet5BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet5BwPer"]))

    @property
    def PgSet6Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet6Id"]))

    @property
    def PgSet6Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet6Prio"]))

    @property
    def PgSet6Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet6Unused"]))

    @property
    def PgSet6BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet6BwPer"]))

    @property
    def PgSet7Id(self):
        """
        Display Name: BWG ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet7Id"]))

    @property
    def PgSet7Prio(self):
        """
        Display Name: Strict Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet7Prio"]))

    @property
    def PgSet7Unused(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet7Unused"]))

    @property
    def PgSet7BwPer(self):
        """
        Display Name: BW%
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PgSet7BwPer"]))

    @property
    def PriorityflowtlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderType"])
        )

    @property
    def PriorityflowtlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderLength"])
        )

    @property
    def PriorityflowtlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderOperVersion"]),
        )

    @property
    def PriorityflowtlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderMaxVersion"]),
        )

    @property
    def PriorityflowtlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderEnable"])
        )

    @property
    def PriorityflowtlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderWilling"])
        )

    @property
    def PriorityflowtlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderError"])
        )

    @property
    def PriorityflowtlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderReserved"]),
        )

    @property
    def PriorityflowtlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityflowtlvHeaderSubtype"])
        )

    @property
    def AdminMapPe7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe7"]))

    @property
    def AdminMapPe6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe6"]))

    @property
    def AdminMapPe5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe5"]))

    @property
    def AdminMapPe4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe4"]))

    @property
    def AdminMapPe3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe3"]))

    @property
    def AdminMapPe2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe2"]))

    @property
    def AdminMapPe1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe1"]))

    @property
    def AdminMapPe0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdminMapPe0"]))

    @property
    def BcntlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderType"])
        )

    @property
    def BcntlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 66
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderLength"])
        )

    @property
    def BcntlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderOperVersion"])
        )

    @property
    def BcntlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderMaxVersion"])
        )

    @property
    def BcntlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderEnable"])
        )

    @property
    def BcntlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderWilling"])
        )

    @property
    def BcntlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderError"])
        )

    @property
    def BcntlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderReserved"])
        )

    @property
    def BcntlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BcntlvHeaderSubtype"])
        )

    @property
    def CfgBcna(self):
        """
        Display Name: bcna
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgBcna"]))

    @property
    def Set1CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set1CpAdmin"]))

    @property
    def Set1RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set1RpAdmin"]))

    @property
    def Set1RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set1RpOper"]))

    @property
    def Set1RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set1RemOper"]))

    @property
    def Set1Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set1Unused"]))

    @property
    def Set2CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set2CpAdmin"]))

    @property
    def Set2RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set2RpAdmin"]))

    @property
    def Set2RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set2RpOper"]))

    @property
    def Set2RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set2RemOper"]))

    @property
    def Set2Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set2Unused"]))

    @property
    def Set3CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set3CpAdmin"]))

    @property
    def Set3RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set3RpAdmin"]))

    @property
    def Set3RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set3RpOper"]))

    @property
    def Set3RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set3RemOper"]))

    @property
    def Set3Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set3Unused"]))

    @property
    def Set4CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set4CpAdmin"]))

    @property
    def Set4RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set4RpAdmin"]))

    @property
    def Set4RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set4RpOper"]))

    @property
    def Set4RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set4RemOper"]))

    @property
    def Set4Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set4Unused"]))

    @property
    def Set5CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set5CpAdmin"]))

    @property
    def Set5RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set5RpAdmin"]))

    @property
    def Set5RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set5RpOper"]))

    @property
    def Set5RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set5RemOper"]))

    @property
    def Set5Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set5Unused"]))

    @property
    def Set6CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set6CpAdmin"]))

    @property
    def Set6RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set6RpAdmin"]))

    @property
    def Set6RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set6RpOper"]))

    @property
    def Set6RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set6RemOper"]))

    @property
    def Set6Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set6Unused"]))

    @property
    def Set7CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set7CpAdmin"]))

    @property
    def Set7RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set7RpAdmin"]))

    @property
    def Set7RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set7RpOper"]))

    @property
    def Set7RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set7RemOper"]))

    @property
    def Set7Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set7Unused"]))

    @property
    def Set8CpAdmin(self):
        """
        Display Name: cp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set8CpAdmin"]))

    @property
    def Set8RpAdmin(self):
        """
        Display Name: rp_admin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set8RpAdmin"]))

    @property
    def Set8RpOper(self):
        """
        Display Name: rp_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set8RpOper"]))

    @property
    def Set8RemOper(self):
        """
        Display Name: rem_tag_oper
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set8RemOper"]))

    @property
    def Set8Unused(self):
        """
        Display Name: unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Set8Unused"]))

    @property
    def CfgRpAlpha(self):
        """
        Display Name: rp_alpha
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpAlpha"]))

    @property
    def CfgRpBeta(self):
        """
        Display Name: rp_beta
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpBeta"]))

    @property
    def CfgRpGd(self):
        """
        Display Name: rp_gd
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpGd"]))

    @property
    def CfgRpGi(self):
        """
        Display Name: rp_gi
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpGi"]))

    @property
    def CfgRpTmax(self):
        """
        Display Name: rp_tmax
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpTmax"]))

    @property
    def CfgCpSf(self):
        """
        Display Name: cp_sf
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgCpSf"]))

    @property
    def CfgRpTd(self):
        """
        Display Name: rp_td
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpTd"]))

    @property
    def CfgRpMin(self):
        """
        Display Name: rp_rmin
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpMin"]))

    @property
    def CfgRpW(self):
        """
        Display Name: rp_w
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpW"]))

    @property
    def CfgRpRd(self):
        """
        Display Name: rp_rd
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgRpRd"]))

    @property
    def ApplicationtlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderType"])
        )

    @property
    def ApplicationtlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderLength"])
        )

    @property
    def ApplicationtlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderOperVersion"]),
        )

    @property
    def ApplicationtlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderMaxVersion"]),
        )

    @property
    def ApplicationtlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderEnable"])
        )

    @property
    def ApplicationtlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderWilling"])
        )

    @property
    def ApplicationtlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderError"])
        )

    @property
    def ApplicationtlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderReserved"])
        )

    @property
    def ApplicationtlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationtlvHeaderSubtype"])
        )

    @property
    def UserPriorityMapPe7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe7"])
        )

    @property
    def UserPriorityMapPe6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe6"])
        )

    @property
    def UserPriorityMapPe5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe5"])
        )

    @property
    def UserPriorityMapPe4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe4"])
        )

    @property
    def UserPriorityMapPe3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe3"])
        )

    @property
    def UserPriorityMapPe2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe2"])
        )

    @property
    def UserPriorityMapPe1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe1"])
        )

    @property
    def UserPriorityMapPe0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPriorityMapPe0"])
        )

    @property
    def LogicallinkdowntlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderType"])
        )

    @property
    def LogicallinkdowntlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderLength"]),
        )

    @property
    def LogicallinkdowntlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LogicallinkdowntlvHeaderOperVersion"]
            ),
        )

    @property
    def LogicallinkdowntlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LogicallinkdowntlvHeaderMaxVersion"]
            ),
        )

    @property
    def LogicallinkdowntlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderEnable"]),
        )

    @property
    def LogicallinkdowntlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderWilling"]),
        )

    @property
    def LogicallinkdowntlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderError"]),
        )

    @property
    def LogicallinkdowntlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderReserved"]),
        )

    @property
    def LogicallinkdowntlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        Available enum values: FCoE Logical Link Status, 0, LAN Logical Link Status, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogicallinkdowntlvHeaderSubtype"]),
        )

    @property
    def FcoeStatusStatus(self):
        """
        Display Name: Logical Link Status
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeStatusStatus"])
        )

    @property
    def FcoeStatusReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeStatusReserved"])
        )

    @property
    def LanStatusStatus(self):
        """
        Display Name: Logical Link Status
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LanStatusStatus"])
        )

    @property
    def LanStatusReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LanStatusReserved"])
        )

    @property
    def NivtlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderType"])
        )

    @property
    def NivtlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderLength"])
        )

    @property
    def NivtlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderOperVersion"])
        )

    @property
    def NivtlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderMaxVersion"])
        )

    @property
    def NivtlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderEnable"])
        )

    @property
    def NivtlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderWilling"])
        )

    @property
    def NivtlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderError"])
        )

    @property
    def NivtlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderReserved"])
        )

    @property
    def NivtlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvHeaderSubtype"])
        )

    @property
    def CfgVis(self):
        """
        Display Name: VIS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgVis"]))

    @property
    def CfgVntag_vers(self):
        """
        Display Name: VN-TAG Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgVntag_vers"]))

    @property
    def CfgVif_id(self):
        """
        Display Name: Control Channel VIF-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgVif_id"]))

    @property
    def CfgMac_addr(self):
        """
        Display Name: Control Channel MAC Address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CfgMac_addr"]))

    @property
    def IeeedcbxtlvsProtocolTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IeeedcbxtlvsProtocolTlvType"])
        )

    @property
    def IeeedcbxtlvsProtocolTlvLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IeeedcbxtlvsProtocolTlvLength"]),
        )

    @property
    def IeeedcbxtlvsProtocolTlvOui(self):
        """
        Display Name: OUI
        Default Value: 0x001B21
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IeeedcbxtlvsProtocolTlvOui"])
        )

    @property
    def IeeedcbxtlvsProtocolTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IeeedcbxtlvsProtocolTlvSubtype"]),
        )

    @property
    def SubtlvsProtocolControlTlvType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsProtocolControlTlvType"]),
        )

    @property
    def SubtlvsProtocolControlTlvLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsProtocolControlTlvLength"]),
        )

    @property
    def SubtlvsProtocolControlTlvOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsProtocolControlTlvOperVersion"]
            ),
        )

    @property
    def SubtlvsProtocolControlTlvMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsProtocolControlTlvMaxVersion"]
            ),
        )

    @property
    def SubtlvsProtocolControlTlvSeqNo(self):
        """
        Display Name: SeqNo
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsProtocolControlTlvSeqNo"]),
        )

    @property
    def SubtlvsProtocolControlTlvAckNo(self):
        """
        Display Name: AckNo
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsProtocolControlTlvAckNo"]),
        )

    @property
    def PrioritygrouptlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderType"])
        )

    @property
    def PrioritygrouptlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderLength"])
        )

    @property
    def PrioritygrouptlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderOperVersion"]),
        )

    @property
    def PrioritygrouptlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderMaxVersion"]),
        )

    @property
    def PrioritygrouptlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderEnable"])
        )

    @property
    def PrioritygrouptlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderWilling"]),
        )

    @property
    def PrioritygrouptlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderError"])
        )

    @property
    def PrioritygrouptlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderReserved"]),
        )

    @property
    def PrioritygrouptlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrioritygrouptlvHeaderSubtype"]),
        )

    @property
    def Up_alloc_tablePgid0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid0"])
        )

    @property
    def Up_alloc_tablePgid1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid1"])
        )

    @property
    def Up_alloc_tablePgid2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid2"])
        )

    @property
    def Up_alloc_tablePgid3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid3"])
        )

    @property
    def Up_alloc_tablePgid4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid4"])
        )

    @property
    def Up_alloc_tablePgid5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid5"])
        )

    @property
    def Up_alloc_tablePgid6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid6"])
        )

    @property
    def Up_alloc_tablePgid7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Up_alloc_tablePgid7"])
        )

    @property
    def Pg_alloc_tableBwPer0(self):
        """
        Display Name: PG% 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer0"])
        )

    @property
    def Pg_alloc_tableBwPer1(self):
        """
        Display Name: PG% 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer1"])
        )

    @property
    def Pg_alloc_tableBwPer2(self):
        """
        Display Name: PG% 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer2"])
        )

    @property
    def Pg_alloc_tableBwPer3(self):
        """
        Display Name: PG% 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer3"])
        )

    @property
    def Pg_alloc_tableBwPer4(self):
        """
        Display Name: PG% 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer4"])
        )

    @property
    def Pg_alloc_tableBwPer5(self):
        """
        Display Name: PG% 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer5"])
        )

    @property
    def Pg_alloc_tableBwPer6(self):
        """
        Display Name: PG% 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer6"])
        )

    @property
    def Pg_alloc_tableBwPer7(self):
        """
        Display Name: PG% 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Pg_alloc_tableBwPer7"])
        )

    @property
    def CfgNumTCsupported(self):
        """
        Display Name: Number of TCs supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CfgNumTCsupported"])
        )

    @property
    def SubtlvsPriorityflowtlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderType"]),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderLength"]
            ),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderOperVersion"]
            ),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderMaxVersion"]
            ),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderEnable"]
            ),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderWilling"]
            ),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderError"]),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderReserved"]
            ),
        )

    @property
    def SubtlvsPriorityflowtlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsPriorityflowtlvHeaderSubtype"]
            ),
        )

    @property
    def PrioMapPe7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe7"]))

    @property
    def PrioMapPe6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe6"]))

    @property
    def PrioMapPe5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe5"]))

    @property
    def PrioMapPe4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe4"]))

    @property
    def PrioMapPe3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe3"]))

    @property
    def PrioMapPe2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe2"]))

    @property
    def PrioMapPe1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe1"]))

    @property
    def PrioMapPe0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrioMapPe0"]))

    @property
    def CfgNumTcpfcsSupp(self):
        """
        Display Name: Number of TCs Supported
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CfgNumTcpfcsSupp"])
        )

    @property
    def SubtlvsApplicationtlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderType"]),
        )

    @property
    def SubtlvsApplicationtlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderLength"]),
        )

    @property
    def SubtlvsApplicationtlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderOperVersion"]
            ),
        )

    @property
    def SubtlvsApplicationtlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderMaxVersion"]
            ),
        )

    @property
    def SubtlvsApplicationtlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderEnable"]),
        )

    @property
    def SubtlvsApplicationtlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderWilling"]
            ),
        )

    @property
    def SubtlvsApplicationtlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderError"]),
        )

    @property
    def SubtlvsApplicationtlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderReserved"]
            ),
        )

    @property
    def SubtlvsApplicationtlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvsApplicationtlvHeaderSubtype"]
            ),
        )

    @property
    def AppsTlvsAppProtId(self):
        """
        Display Name: Application Protocol ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppsTlvsAppProtId"])
        )

    @property
    def AppsTlvsOui6(self):
        """
        Display Name: OUI 23-18 bits
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AppsTlvsOui6"]))

    @property
    def AppsTlvsSf(self):
        """
        Display Name: Selector Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AppsTlvsSf"]))

    @property
    def AppsTlvsOui16(self):
        """
        Display Name: OUI 15-0 bits
        Default Value: 0x1B21
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AppsTlvsOui16"]))

    @property
    def AppstlvsPrioMapPe7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe7"])
        )

    @property
    def AppstlvsPrioMapPe6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe6"])
        )

    @property
    def AppstlvsPrioMapPe5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe5"])
        )

    @property
    def AppstlvsPrioMapPe4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe4"])
        )

    @property
    def AppstlvsPrioMapPe3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe3"])
        )

    @property
    def AppstlvsPrioMapPe2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe2"])
        )

    @property
    def AppstlvsPrioMapPe1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe1"])
        )

    @property
    def AppstlvsPrioMapPe0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppstlvsPrioMapPe0"])
        )

    @property
    def SubtlvsNivtlvHeaderType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderType"])
        )

    @property
    def SubtlvsNivtlvHeaderLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderLength"])
        )

    @property
    def SubtlvsNivtlvHeaderOperVersion(self):
        """
        Display Name: Oper Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderOperVersion"]),
        )

    @property
    def SubtlvsNivtlvHeaderMaxVersion(self):
        """
        Display Name: Max Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderMaxVersion"]),
        )

    @property
    def SubtlvsNivtlvHeaderEnable(self):
        """
        Display Name: Enable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderEnable"])
        )

    @property
    def SubtlvsNivtlvHeaderWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderWilling"])
        )

    @property
    def SubtlvsNivtlvHeaderError(self):
        """
        Display Name: Error
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderError"])
        )

    @property
    def SubtlvsNivtlvHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderReserved"])
        )

    @property
    def SubtlvsNivtlvHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvsNivtlvHeaderSubtype"])
        )

    @property
    def NivtlvCfgVis(self):
        """
        Display Name: VIS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NivtlvCfgVis"]))

    @property
    def NivtlvCfgVntag_vers(self):
        """
        Display Name: VN-TAG Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvCfgVntag_vers"])
        )

    @property
    def NivtlvCfgVif_id(self):
        """
        Display Name: Control Channel VIF-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvCfgVif_id"])
        )

    @property
    def NivtlvCfgMac_addr(self):
        """
        Display Name: Control Channel MAC Address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NivtlvCfgMac_addr"])
        )

    @property
    def EtsConfigurationTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvType"])
        )

    @property
    def EtsConfigurationTlvLength(self):
        """
        Display Name: Length
        Default Value: 25
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvLength"])
        )

    @property
    def EtsConfigurationTlvOui(self):
        """
        Display Name: OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvOui"])
        )

    @property
    def EtsConfigurationTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvSubtype"])
        )

    @property
    def EtsConfigurationTlvWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvWilling"])
        )

    @property
    def EtsConfigurationTlvCbs(self):
        """
        Display Name: CBS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvCbs"])
        )

    @property
    def EtsConfigurationTlvReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvReserved"])
        )

    @property
    def EtsConfigurationTlvMaxTC(self):
        """
        Display Name: Max TCs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsConfigurationTlvMaxTC"])
        )

    @property
    def PriorityAssignTablePriority0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority0"])
        )

    @property
    def PriorityAssignTablePriority1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority1"])
        )

    @property
    def PriorityAssignTablePriority2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority2"])
        )

    @property
    def PriorityAssignTablePriority3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority3"])
        )

    @property
    def PriorityAssignTablePriority4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority4"])
        )

    @property
    def PriorityAssignTablePriority5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority5"])
        )

    @property
    def PriorityAssignTablePriority6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority6"])
        )

    @property
    def PriorityAssignTablePriority7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityAssignTablePriority7"])
        )

    @property
    def TcBandwidthTableTc0(self):
        """
        Display Name: TC% 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc0"])
        )

    @property
    def TcBandwidthTableTc1(self):
        """
        Display Name: TC% 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc1"])
        )

    @property
    def TcBandwidthTableTc2(self):
        """
        Display Name: TC% 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc2"])
        )

    @property
    def TcBandwidthTableTc3(self):
        """
        Display Name: TC% 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc3"])
        )

    @property
    def TcBandwidthTableTc4(self):
        """
        Display Name: TC% 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc4"])
        )

    @property
    def TcBandwidthTableTc5(self):
        """
        Display Name: TC% 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc5"])
        )

    @property
    def TcBandwidthTableTc6(self):
        """
        Display Name: TC% 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc6"])
        )

    @property
    def TcBandwidthTableTc7(self):
        """
        Display Name: TC% 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcBandwidthTableTc7"])
        )

    @property
    def TsaAssignmentTableTc0(self):
        """
        Display Name: Traffic Class 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc0"])
        )

    @property
    def TsaAssignmentTableTc1(self):
        """
        Display Name: Traffic Class 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc1"])
        )

    @property
    def TsaAssignmentTableTc2(self):
        """
        Display Name: Traffic Class 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc2"])
        )

    @property
    def TsaAssignmentTableTc3(self):
        """
        Display Name: Traffic Class 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc3"])
        )

    @property
    def TsaAssignmentTableTc4(self):
        """
        Display Name: Traffic Class 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc4"])
        )

    @property
    def TsaAssignmentTableTc5(self):
        """
        Display Name: Traffic Class 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc5"])
        )

    @property
    def TsaAssignmentTableTc6(self):
        """
        Display Name: Traffic Class 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc6"])
        )

    @property
    def TsaAssignmentTableTc7(self):
        """
        Display Name: Traffic Class 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TsaAssignmentTableTc7"])
        )

    @property
    def EtsRecommandationTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsRecommandationTlvType"])
        )

    @property
    def EtsRecommandationTlvLength(self):
        """
        Display Name: Length
        Default Value: 25
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsRecommandationTlvLength"])
        )

    @property
    def EtsRecommandationTlvOui(self):
        """
        Display Name: OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsRecommandationTlvOui"])
        )

    @property
    def EtsRecommandationTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsRecommandationTlvSubtype"])
        )

    @property
    def EtsRecommandationTlvReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EtsRecommandationTlvReserved"])
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority0"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority1"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority2"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority3"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority4"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority5"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority6"]
            ),
        )

    @property
    def EtsrecommandationtlvPriorityAssignTablePriority7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvPriorityAssignTablePriority7"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc0(self):
        """
        Display Name: TC% 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc0"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc1(self):
        """
        Display Name: TC% 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc1"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc2(self):
        """
        Display Name: TC% 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc2"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc3(self):
        """
        Display Name: TC% 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc3"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc4(self):
        """
        Display Name: TC% 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc4"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc5(self):
        """
        Display Name: TC% 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc5"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc6(self):
        """
        Display Name: TC% 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc6"]
            ),
        )

    @property
    def EtsrecommandationtlvTcBandwidthTableTc7(self):
        """
        Display Name: TC% 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTcBandwidthTableTc7"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc0(self):
        """
        Display Name: Traffic Class 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc0"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc1(self):
        """
        Display Name: Traffic Class 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc1"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc2(self):
        """
        Display Name: Traffic Class 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc2"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc3(self):
        """
        Display Name: Traffic Class 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc3"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc4(self):
        """
        Display Name: Traffic Class 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc4"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc5(self):
        """
        Display Name: Traffic Class 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc5"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc6(self):
        """
        Display Name: Traffic Class 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc6"]
            ),
        )

    @property
    def EtsrecommandationtlvTsaAssignmentTableTc7(self):
        """
        Display Name: Traffic Class 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EtsrecommandationtlvTsaAssignmentTableTc7"]
            ),
        )

    @property
    def PriorityBasedFlowControlTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityBasedFlowControlTlvType"]),
        )

    @property
    def PriorityBasedFlowControlTlvLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityBasedFlowControlTlvLength"]),
        )

    @property
    def PriorityBasedFlowControlTlvOui(self):
        """
        Display Name: OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityBasedFlowControlTlvOui"]),
        )

    @property
    def PriorityBasedFlowControlTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PriorityBasedFlowControlTlvSubtype"]
            ),
        )

    @property
    def PriorityBasedFlowControlTlvWilling(self):
        """
        Display Name: Willing
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PriorityBasedFlowControlTlvWilling"]
            ),
        )

    @property
    def PriorityBasedFlowControlTlvMbc(self):
        """
        Display Name: MBC
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityBasedFlowControlTlvMbc"]),
        )

    @property
    def PriorityBasedFlowControlTlvReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PriorityBasedFlowControlTlvReserved"]
            ),
        )

    @property
    def PriorityBasedFlowControlTlvPfcCap(self):
        """
        Display Name: PFC Capability
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PriorityBasedFlowControlTlvPfcCap"]),
        )

    @property
    def PfcEnablePriority7(self):
        """
        Display Name: Priority 7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority7"])
        )

    @property
    def PfcEnablePriority6(self):
        """
        Display Name: Priority 6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority6"])
        )

    @property
    def PfcEnablePriority5(self):
        """
        Display Name: Priority 5
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority5"])
        )

    @property
    def PfcEnablePriority4(self):
        """
        Display Name: Priority 4
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority4"])
        )

    @property
    def PfcEnablePriority3(self):
        """
        Display Name: Priority 3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority3"])
        )

    @property
    def PfcEnablePriority2(self):
        """
        Display Name: Priority 2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority2"])
        )

    @property
    def PfcEnablePriority1(self):
        """
        Display Name: Priority 1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority1"])
        )

    @property
    def PfcEnablePriority0(self):
        """
        Display Name: Priority 0
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PfcEnablePriority0"])
        )

    @property
    def ApplicationPriorityTlvType(self):
        """
        Display Name: Type
        Default Value: 127
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationPriorityTlvType"])
        )

    @property
    def ApplicationPriorityTlvLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationPriorityTlvLength"])
        )

    @property
    def ApplicationPriorityTlvOui(self):
        """
        Display Name: OUI
        Default Value: 0x0080C2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationPriorityTlvOui"])
        )

    @property
    def ApplicationPriorityTlvSubtype(self):
        """
        Display Name: Subtype
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ApplicationPriorityTlvSubtype"]),
        )

    @property
    def ApplicationPriorityTlvReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ApplicationPriorityTlvReserved"]),
        )

    @property
    def AppPriorityTablePriority(self):
        """
        Display Name: Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppPriorityTablePriority"])
        )

    @property
    def AppPriorityTableReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppPriorityTableReserved"])
        )

    @property
    def AppPriorityTableSel(self):
        """
        Display Name: Sel
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppPriorityTableSel"])
        )

    @property
    def AppPriorityTableProtocolId(self):
        """
        Display Name: Protocol ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppPriorityTableProtocolId"])
        )

    @property
    def EndLldpTlvType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndLldpTlvType"])
        )

    @property
    def EndLldpTlvLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndLldpTlvLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
