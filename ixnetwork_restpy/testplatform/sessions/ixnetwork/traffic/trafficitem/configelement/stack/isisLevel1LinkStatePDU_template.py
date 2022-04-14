from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisLevel1LinkStatePDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisLevel1LinkStatePDU"
    _SDM_ATT_MAP = {
        "CommonHeaderIntradomainRoutingProtocolDiscriminator": "isisLevel1LinkStatePDU.isisHeader.commonHeader.intradomainRoutingProtocolDiscriminator-1",
        "CommonHeaderLengthIndicator": "isisLevel1LinkStatePDU.isisHeader.commonHeader.lengthIndicator-2",
        "CommonHeaderVersionProtocolIDExtension": "isisLevel1LinkStatePDU.isisHeader.commonHeader.versionProtocolIDExtension-3",
        "CommonHeaderIdLength": "isisLevel1LinkStatePDU.isisHeader.commonHeader.idLength-4",
        "CommonHeaderReservedBit": "isisLevel1LinkStatePDU.isisHeader.commonHeader.reservedBit-5",
        "CommonHeaderPduType": "isisLevel1LinkStatePDU.isisHeader.commonHeader.pduType-6",
        "CommonHeaderVersion": "isisLevel1LinkStatePDU.isisHeader.commonHeader.version-7",
        "CommonHeaderReserved": "isisLevel1LinkStatePDU.isisHeader.commonHeader.reserved-8",
        "CommonHeaderMaximumAreaAddresses": "isisLevel1LinkStatePDU.isisHeader.commonHeader.maximumAreaAddresses-9",
        "FixedHeaderPduLength": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.pduLength-10",
        "FixedHeaderRemainingLifetime": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.remainingLifetime-11",
        "LspIDPseudonodeID": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.lspID.pseudonodeID-12",
        "LspIDLspNumber": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.lspID.lspNumber-13",
        "FixedHeaderSequenceNumber": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.sequenceNumber-14",
        "FixedHeaderChecksum": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.checksum-15",
        "FixedHeaderPartitionRepairBit": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.partitionRepairBit-16",
        "FixedHeaderAttached": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.attached-17",
        "FixedHeaderLspDatabaseOverload": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.lspDatabaseOverload-18",
        "FixedHeaderIsType": "isisLevel1LinkStatePDU.isisHeader.fixedHeader.isType-19",
        "Tlv1AreaAddressesTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvCode-20",
        "Tlv1AreaAddressesTlvLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvLength-21",
        "ValueFieldsAddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.addressLength-22",
        "ValueFieldsAreaAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.areaAddress-23",
        "Tlv2ISNeighborsTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.tlvCode-24",
        "Tlv2ISNeighborsTlvLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.tlvLength-25",
        "ValueFieldsVirtualFlag": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.virtualFlag-26",
        "Tlv2RepeatingFieldsReservedBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.reservedBit-27",
        "Tlv2RepeatingFieldsInternalMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-28",
        "Tlv2RepeatingFieldsDefaultMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.defaultMetric-29",
        "Tlv2RepeatingFieldsSupportedBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-30",
        "ValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-31",
        "Tlv2RepeatingFieldsDelayMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.delayMetric-32",
        "ValuefieldsTlv2RepeatingFieldsSupportedBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-33",
        "Tlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-34",
        "Tlv2RepeatingFieldsExpenseMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.expenseMetric-35",
        "Tlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-36",
        "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-37",
        "ValuefieldsTlv2RepeatingFieldsExpenseMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.expenseMetric-38",
        "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-39",
        "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-40",
        "Tlv2RepeatingFieldsErrorMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.errorMetric-41",
        "NeighborIDNeighborID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.neighborID.neighborID-42",
        "NeighborIDPadding8Bits": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.neighborID.padding8Bits-43",
        "Tlv3EndSystemNeighborsTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.tlvCode-44",
        "Tlv3EndSystemNeighborsTlvLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.tlvLength-45",
        "ValueFieldsReserved": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.valueFields.reserved-46",
        "ValueFieldsNeighborID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.valueFields.neighborID-47",
        "Tlv10AuthenticationInformationTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvCode-48",
        "Tlv10AuthenticationInformationTlvLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvLength-49",
        "ValueFieldsAuthenticationType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationType-50",
        "ValueFieldsAuthenticationValue": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationValue-51",
        "Tlv14OriginatingLSPBufferSizeTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv14OriginatingLSPBufferSize.tlvCode-52",
        "Tlv14OriginatingLSPBufferSizeTlvLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv14OriginatingLSPBufferSize.tlvLength-53",
        "Tlv14OriginatingLSPBufferSizeValue": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv14OriginatingLSPBufferSize.value-54",
        "Tlv22ExtendedISReachabilityTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.tlvCode-55",
        "Tlv22ExtendedISReachabilityTlvLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.tlvLength-56",
        "ValueFieldSystemIDAndPseudonodeNumber": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.systemIDAndPseudonodeNumber-57",
        "ValueFieldDefaultMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.defaultMetric-58",
        "ValueFieldLengthOfSubTLVs": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.lengthOfSubTLVs-59",
        "SubTLVsNoSubTLVs": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.noSubTLVs-60",
        "SubTLV3AdministrativeGroupSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV3AdministrativeGroup.subTLVCode-61",
        "SubTLV3AdministrativeGroupSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV3AdministrativeGroup.subTLVLength-62",
        "ValueFieldAdministrativeGroup": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV3AdministrativeGroup.valueField.administrativeGroup-63",
        "SubTLV6IPv4InterfaceAddressSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV6IPv4InterfaceAddress.subTLVCode-64",
        "SubTLV6IPv4InterfaceAddressSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV6IPv4InterfaceAddress.subTLVLength-65",
        "ValueFieldIpv4InterfaceAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV6IPv4InterfaceAddress.valueField.ipv4InterfaceAddress-66",
        "SubTLV8IPv4NeighborAddressSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV8IPv4NeighborAddress.subTLVCode-67",
        "SubTLV8IPv4NeighborAddressSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV8IPv4NeighborAddress.subTLVLength-68",
        "ValueFieldIpv4NeighborAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV8IPv4NeighborAddress.valueField.ipv4NeighborAddress-69",
        "SubTLV9MaximumLinkBandwidthSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV9MaximumLinkBandwidth.subTLVCode-70",
        "SubTLV9MaximumLinkBandwidthSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV9MaximumLinkBandwidth.subTLVLength-71",
        "ValueFieldMaximumLinkBandwidthBytessec": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV9MaximumLinkBandwidth.valueField.maximumLinkBandwidthBytessec-72",
        "SubTLV10ReservableLinkBandwidthSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.subTLVCode-73",
        "SubTLV10ReservableLinkBandwidthSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.subTLVLength-74",
        "ValueFieldAuthenticationType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.valueField.authenticationType-75",
        "ValueFieldAuthenticationValue": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.valueField.authenticationValue-76",
        "SubTLV11UnreservedBandwidthSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV11UnreservedBandwidth.subTLVCode-77",
        "SubTLV11UnreservedBandwidthSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV11UnreservedBandwidth.subTLVLength-78",
        "ValueFieldUnreservedBandwidthBytessec": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV11UnreservedBandwidth.valueField.unreservedBandwidthBytessec-79",
        "SubTLV18TEDefaultMetricSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV18TEDefaultMetric.subTLVCode-80",
        "SubTLV18TEDefaultMetricSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV18TEDefaultMetric.subTLVLength-81",
        "ValueFieldTeDefaultMetric": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV18TEDefaultMetric.valueField.teDefaultMetric-82",
        "SubTLV28MTUSubTLVCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV28MTU.subTLVCode-83",
        "SubTLV28MTUSubTLVLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV28MTU.subTLVLength-84",
        "ValueFieldFBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV28MTU.valueField.FBit-85",
        "ValueFieldReserved": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV28MTU.valueField.Reserved-86",
        "ValueFieldMtu": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV28MTU.valueField.mtu-87",
        "Tlv128IPInternalReachabilityCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.code-88",
        "Tlv128IPInternalReachabilityLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.length-89",
        "ValueEntriesZeroBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.zeroBit-90",
        "ValueEntriesIe": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.ie-91",
        "ValueEntriesDefaultMETRIC": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.defaultMETRIC-92",
        "ValueEntriesS": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.s-93",
        "ValueEntriesR": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.r-94",
        "ValueEntriesDelayMETRIC": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.delayMETRIC-95",
        "Tlv128ipinternalreachabilityValueEntriesS": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.s-96",
        "Tlv128ipinternalreachabilityValueEntriesR": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.r-97",
        "ValueEntriesExpenseMETRIC": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.expenseMETRIC-98",
        "TlvheadertypeTlv128ipinternalreachabilityValueEntriesS": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.s-99",
        "TlvheadertypeTlv128ipinternalreachabilityValueEntriesR": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.r-100",
        "ValueEntriesErrorMETRIC": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.errorMETRIC-101",
        "ValueEntriesIpADDRESS": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.ipADDRESS-102",
        "ValueEntriesSubnetMASK": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.subnetMASK-103",
        "Tlv129ProtocolsSupportedCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.code-104",
        "Tlv129ProtocolsSupportedLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.length-105",
        "NlpidEntriesNlpid": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.nlpid-106",
        "Tlv132IPInterfaceAddressCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.code-107",
        "Tlv132IPInterfaceAddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.length-108",
        "IpAddressEntriesIpAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.ipAddressEntries.ipAddress-109",
        "Tlv142GroupAddressType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.type-110",
        "Tlv142GroupAddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.length-111",
        "SubtlvSubTLVsNoSubTLVs": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.noSubTLVs-112",
        "GroupMACAddressType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.type-113",
        "GroupMACAddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.length-114",
        "GroupMACAddressResv": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.resv-115",
        "GroupMACAddressTopologyID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.topologyID-116",
        "GroupMACAddressResv2": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.resv2-117",
        "GroupMACAddressVlanID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.vlanID-118",
        "GroupMACAddressNumGroupRecords": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.numGroupRecords-119",
        "GroupRecordsNumOfSources": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.groupRecords.numOfSources-120",
        "GroupRecordsGroupAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.groupRecords.groupAddress-121",
        "ValueSourceAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupMACAddress.groupRecords.value.sourceAddress-122",
        "GroupIPAddressType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.type-123",
        "GroupIPAddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.length-124",
        "GroupIPAddressResv": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.resv-125",
        "GroupIPAddressTopologyID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.topologyID-126",
        "GroupIPAddressResv2": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.resv2-127",
        "GroupIPAddressVlanID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.vlanID-128",
        "GroupIPAddressNumGroupRecords": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.numGroupRecords-129",
        "GroupipaddressGroupRecordsNumOfSources": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.groupRecords.numOfSources-130",
        "GroupipaddressGroupRecordsGroupAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.groupRecords.groupAddress-131",
        "GrouprecordsValueSourceAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPAddress.groupRecords.value.sourceAddress-132",
        "GroupIPv6AddressType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.type-133",
        "GroupIPv6AddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.length-134",
        "GroupIPv6AddressResv": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.resv-135",
        "GroupIPv6AddressTopologyID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.topologyID-136",
        "GroupIPv6AddressResv2": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.resv2-137",
        "GroupIPv6AddressVlanID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.vlanID-138",
        "GroupIPv6AddressNumGroupRecords": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.numGroupRecords-139",
        "Groupipv6addressGroupRecordsNumOfSources": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.groupRecords.numOfSources-140",
        "Groupipv6addressGroupRecordsGroupAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.groupRecords.groupAddress-141",
        "Groupipv6addressGrouprecordsValueSourceAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv142GroupAddress.valueField.subTLV.subTLVs.groupIPv6Address.groupRecords.value.sourceAddress-142",
        "Tlv232IPv6InterfaceAddressCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.code-143",
        "Tlv232IPv6InterfaceAddressLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.length-144",
        "Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.ipAddressEntries.ipAddress-145",
        "Tlv237MultiTopologyReachableIPv6PrefixesTlvCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.tlvCode-146",
        "Tlv237MultiTopologyReachableIPv6PrefixesLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.length-147",
        "ValueFieldReservedBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.reservedBit-148",
        "ValueFieldExtendedIntermediateSystemTLVFormat": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.extendedIntermediateSystemTLVFormat-149",
        "Tlv242RouterCapabilityCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.code-150",
        "Tlv242RouterCapabilityLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.length-151",
        "ValueRouterID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.routerID-152",
        "ValueFlag": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.flag-153",
        "SubTLVHeaderTypeNoSubTLVs": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.noSubTLVs-154",
        "DeviceIDType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.deviceID.type-155",
        "DeviceIDLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.deviceID.length-156",
        "DeviceIDReserved1": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.deviceID.reserved1-157",
        "DeviceIDPriority": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.deviceID.priority-158",
        "DeviceIDReserved2": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.deviceID.reserved2-159",
        "DeviceIDDeviceID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.deviceID.deviceID-160",
        "TRILLVerType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.TRILLVer.type-161",
        "TRILLVerLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.TRILLVer.length-162",
        "TRILLVerMaxVersion": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.TRILLVer.maxVersion-163",
        "RootPriorityType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootPriority.type-164",
        "RootPriorityLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootPriority.length-165",
        "RootPriorityBroadcastPriority": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootPriority.broadcastPriority-166",
        "RootPriorityNumberOfMultiDestinationTree": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootPriority.numberOfMultiDestinationTree-167",
        "NickNameType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.nickName.type-168",
        "NickNameLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.nickName.length-169",
        "NicknameRecordNickPri": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.nickName.nicknameRecord.nickPri-170",
        "NicknameRecordTreePri": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.nickName.nicknameRecord.treePri-171",
        "NicknameRecordNickname": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.nickName.nicknameRecord.nickname-172",
        "TreesType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.trees.type-173",
        "TreesLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.trees.length-174",
        "TreesNoOfTreesToCompute": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.trees.noOfTreesToCompute-175",
        "TreesMaxNoOfTreesAbleToCompute": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.trees.maxNoOfTreesAbleToCompute-176",
        "TreesNoOfTreesToUse": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.trees.noOfTreesToUse-177",
        "RootIDsType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootIDs.type-178",
        "RootIDsLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootIDs.length-179",
        "RootIDsBroadcastRootSystemID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootIDs.broadcastRootSystemID-180",
        "MulticastRootSystemIDMulticastRootSystemId": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.rootIDs.multicastRootSystemID.multicastRootSystemId-181",
        "TreeRootIDsType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.treeRootIDs.type-182",
        "TreeRootIDsLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.treeRootIDs.length-183",
        "TreeRootIDsStartingTreeNum": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.treeRootIDs.startingTreeNum-184",
        "TreeRtIDNicknameTreeRtidNickname": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.treeRootIDs.treeRtIDNickname.treeRtidNickname-185",
        "IntVLANType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.type-186",
        "IntVLANLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.length-187",
        "IntVLANIntVLANNickname": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.intVLANNickname-188",
        "InterestedVLANsM4bit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.interestedVLANs.m4bit-189",
        "InterestedVLANsM6bit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.interestedVLANs.m6bit-190",
        "InterestedVLANsIntVLANReserved": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.interestedVLANs.intVLANReserved-191",
        "InterestedVLANsIntVLANStart": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.interestedVLANs.intVLANStart-192",
        "InterestedVLANsReserved2": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.interestedVLANs.reserved2-193",
        "InterestedVLANsIntVLANEnd": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.interestedVLANs.intVLANEnd-194",
        "IntVLANIntVLANAppFwderStatus": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.intVLANAppFwderStatus-195",
        "IntVLANRootBridgesIntVLANRootBridge": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.intVLAN.intVLANRootBridges.intVLANRootBridge-196",
        "DceftagType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.dceftag.type-197",
        "DceftagLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.dceftag.length-198",
        "DceftagFtagvalue": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv242RouterCapability.value.subTLVHeader.subTLVHeaderType.dceftag.ftagvalue-199",
        "Tlv144MTCapabilityCode": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.code-200",
        "Tlv144MTCapabilityLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.length-201",
        "ValueOBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.OBit-202",
        "ValueRbit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.rbit-203",
        "ValueMtID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.mtID-204",
        "SubtlvheaderSubTLVHeaderTypeNoSubTLVs": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.noSubTLVs-205",
        "InstanceType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.type-206",
        "InstanceLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.length-207",
        "InstanceCistroot": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.cistroot-208",
        "InstanceCistcost": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.cistcost-209",
        "InstanceBridgepriority": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.bridgepriority-210",
        "InstanceResvbit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.resvbit-211",
        "InstanceVBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.VBit-212",
        "InstanceTrees": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.trees-213",
        "VlanidTupleUBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.UBit-214",
        "VlanidTupleMBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.MBit-215",
        "VlanidTupleABit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.ABit-216",
        "VlanidTupleRbit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.rbit-217",
        "VlanidTupleEct_algo": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.ect_algo-218",
        "VlanidTupleBasevid": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.basevid-219",
        "VlanidTupleSpvid": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.instance.vlanidTuple.spvid-220",
        "ServiceIDType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.type-221",
        "ServiceIDLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.length-222",
        "ServiceIDBmac": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.bmac-223",
        "ServiceIDResvbits": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.resvbits-224",
        "ServiceIDBasevid": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.basevid-225",
        "ServiceIdIsidTBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.serviceIdIsid.TBit-226",
        "ServiceIdIsidRBit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.serviceIdIsid.RBit-227",
        "ServiceIdIsidRsvbit": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.serviceIdIsid.rsvbit-228",
        "ServiceIdIsidIsid": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTCapability.value.subTLVHeader.subTLVHeaderType.serviceID.serviceIdIsid.isid-229",
        "Tlv141MACReachabilityType": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv141MACReachability.type-230",
        "Tlv141MACReachabilityLength": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv141MACReachability.length-231",
        "Tlv141MACReachabilityVlanID": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv141MACReachability.vlanID-232",
        "MacAddressMacAddress": "isisLevel1LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv141MACReachability.macAddress.macAddress-233",
    }

    def __init__(self, parent, list_op=False):
        super(IsisLevel1LinkStatePDU, self).__init__(parent, list_op)

    @property
    def CommonHeaderIntradomainRoutingProtocolDiscriminator(self):
        """
        Display Name: Intradomain routing protocol discriminator
        Default Value: 0x83
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonHeaderIntradomainRoutingProtocolDiscriminator"]
            ),
        )

    @property
    def CommonHeaderLengthIndicator(self):
        """
        Display Name: Length indicator
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderLengthIndicator"])
        )

    @property
    def CommonHeaderVersionProtocolIDExtension(self):
        """
        Display Name: Version/Protocol ID extension
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonHeaderVersionProtocolIDExtension"]
            ),
        )

    @property
    def CommonHeaderIdLength(self):
        """
        Display Name: ID length
        Default Value: 0
        Value Format: decimal
        Available enum values: One, 1, Two, 2, Three, 3, Four, 4, Five, 5, Six, 6, Seven, 7, Eight, 8, 6 Octet ID field, 0, Null ID field, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderIdLength"])
        )

    @property
    def CommonHeaderReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderReservedBit"])
        )

    @property
    def CommonHeaderPduType(self):
        """
        Display Name: PDU type
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderPduType"])
        )

    @property
    def CommonHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderVersion"])
        )

    @property
    def CommonHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderReserved"])
        )

    @property
    def CommonHeaderMaximumAreaAddresses(self):
        """
        Display Name: Maximum area addresses
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHeaderMaximumAreaAddresses"]),
        )

    @property
    def FixedHeaderPduLength(self):
        """
        Display Name: PDU length
        Default Value: 1497
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderPduLength"])
        )

    @property
    def FixedHeaderRemainingLifetime(self):
        """
        Display Name: Remaining lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderRemainingLifetime"])
        )

    @property
    def LspIDPseudonodeID(self):
        """
        Display Name: Pseudonode ID
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LspIDPseudonodeID"])
        )

    @property
    def LspIDLspNumber(self):
        """
        Display Name: LSP number
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LspIDLspNumber"])
        )

    @property
    def FixedHeaderSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderSequenceNumber"])
        )

    @property
    def FixedHeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderChecksum"])
        )

    @property
    def FixedHeaderPartitionRepairBit(self):
        """
        Display Name: Partition repair bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not supported, 0, Supported, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderPartitionRepairBit"]),
        )

    @property
    def FixedHeaderAttached(self):
        """
        Display Name: Attached
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderAttached"])
        )

    @property
    def FixedHeaderLspDatabaseOverload(self):
        """
        Display Name: LSP database overload
        Default Value: 0
        Value Format: decimal
        Available enum values: No overload, 0, Overload, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderLspDatabaseOverload"]),
        )

    @property
    def FixedHeaderIsType(self):
        """
        Display Name: IS type
        Default Value: 1
        Value Format: decimal
        Available enum values: Level 1 IS, 1, Level 2 IS, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderIsType"])
        )

    @property
    def Tlv1AreaAddressesTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv1AreaAddressesTlvCode"])
        )

    @property
    def Tlv1AreaAddressesTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv1AreaAddressesTlvLength"])
        )

    @property
    def ValueFieldsAddressLength(self):
        """
        Display Name: Address length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAddressLength"])
        )

    @property
    def ValueFieldsAreaAddress(self):
        """
        Display Name: Area address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAreaAddress"])
        )

    @property
    def Tlv2ISNeighborsTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2ISNeighborsTlvCode"])
        )

    @property
    def Tlv2ISNeighborsTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2ISNeighborsTlvLength"])
        )

    @property
    def ValueFieldsVirtualFlag(self):
        """
        Display Name: Virtual flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Level 2 path to repair area partition, 0, Level 2 path to repair area partition, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsVirtualFlag"])
        )

    @property
    def Tlv2RepeatingFieldsReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsReservedBit"]),
        )

    @property
    def Tlv2RepeatingFieldsInternalMetric(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsInternalMetric"]),
        )

    @property
    def Tlv2RepeatingFieldsDefaultMetric(self):
        """
        Display Name: Default metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsDefaultMetric"]),
        )

    @property
    def Tlv2RepeatingFieldsSupportedBit(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsSupportedBit"]),
        )

    @property
    def ValuefieldsTlv2RepeatingFieldsInternalMetric(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValuefieldsTlv2RepeatingFieldsInternalMetric"]
            ),
        )

    @property
    def Tlv2RepeatingFieldsDelayMetric(self):
        """
        Display Name: Delay metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsDelayMetric"]),
        )

    @property
    def ValuefieldsTlv2RepeatingFieldsSupportedBit(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValuefieldsTlv2RepeatingFieldsSupportedBit"]
            ),
        )

    @property
    def Tlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric"
                ]
            ),
        )

    @property
    def Tlv2RepeatingFieldsExpenseMetric(self):
        """
        Display Name: Expense metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsExpenseMetric"]),
        )

    @property
    def Tlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric"
                ]
            ),
        )

    @property
    def ValuefieldsTlv2RepeatingFieldsExpenseMetric(self):
        """
        Display Name: Expense metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValuefieldsTlv2RepeatingFieldsExpenseMetric"]
            ),
        )

    @property
    def TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric"
                ]
            ),
        )

    @property
    def Tlv2RepeatingFieldsErrorMetric(self):
        """
        Display Name: Error metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv2RepeatingFieldsErrorMetric"]),
        )

    @property
    def NeighborIDNeighborID(self):
        """
        Display Name: Neighbor ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborIDNeighborID"])
        )

    @property
    def NeighborIDPadding8Bits(self):
        """
        Display Name: Padding - 8 bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborIDPadding8Bits"])
        )

    @property
    def Tlv3EndSystemNeighborsTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv3EndSystemNeighborsTlvCode"]),
        )

    @property
    def Tlv3EndSystemNeighborsTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv3EndSystemNeighborsTlvLength"]),
        )

    @property
    def ValueFieldsReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsReserved"])
        )

    @property
    def ValueFieldsNeighborID(self):
        """
        Display Name: Neighbor ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsNeighborID"])
        )

    @property
    def Tlv10AuthenticationInformationTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv10AuthenticationInformationTlvCode"]
            ),
        )

    @property
    def Tlv10AuthenticationInformationTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv10AuthenticationInformationTlvLength"]
            ),
        )

    @property
    def ValueFieldsAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 1
        Value Format: decimal
        Available enum values: Cleartext password, 1, Routing domain private authentication method, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAuthenticationType"]),
        )

    @property
    def ValueFieldsAuthenticationValue(self):
        """
        Display Name: Authentication value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAuthenticationValue"]),
        )

    @property
    def Tlv14OriginatingLSPBufferSizeTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv14OriginatingLSPBufferSizeTlvCode"]
            ),
        )

    @property
    def Tlv14OriginatingLSPBufferSizeTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv14OriginatingLSPBufferSizeTlvLength"]
            ),
        )

    @property
    def Tlv14OriginatingLSPBufferSizeValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv14OriginatingLSPBufferSizeValue"]
            ),
        )

    @property
    def Tlv22ExtendedISReachabilityTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv22ExtendedISReachabilityTlvCode"]
            ),
        )

    @property
    def Tlv22ExtendedISReachabilityTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv22ExtendedISReachabilityTlvLength"]
            ),
        )

    @property
    def ValueFieldSystemIDAndPseudonodeNumber(self):
        """
        Display Name: System ID and Pseudonode number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValueFieldSystemIDAndPseudonodeNumber"]
            ),
        )

    @property
    def ValueFieldDefaultMetric(self):
        """
        Display Name: Default metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldDefaultMetric"])
        )

    @property
    def ValueFieldLengthOfSubTLVs(self):
        """
        Display Name: Length of Sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldLengthOfSubTLVs"])
        )

    @property
    def SubTLVsNoSubTLVs(self):
        """
        Display Name: No sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubTLVsNoSubTLVs"])
        )

    @property
    def SubTLV3AdministrativeGroupSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV3AdministrativeGroupSubTLVCode"]
            ),
        )

    @property
    def SubTLV3AdministrativeGroupSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV3AdministrativeGroupSubTLVLength"]
            ),
        )

    @property
    def ValueFieldAdministrativeGroup(self):
        """
        Display Name: Administrative group
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldAdministrativeGroup"]),
        )

    @property
    def SubTLV6IPv4InterfaceAddressSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV6IPv4InterfaceAddressSubTLVCode"]
            ),
        )

    @property
    def SubTLV6IPv4InterfaceAddressSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV6IPv4InterfaceAddressSubTLVLength"]
            ),
        )

    @property
    def ValueFieldIpv4InterfaceAddress(self):
        """
        Display Name: IPv4 interface address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldIpv4InterfaceAddress"]),
        )

    @property
    def SubTLV8IPv4NeighborAddressSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV8IPv4NeighborAddressSubTLVCode"]
            ),
        )

    @property
    def SubTLV8IPv4NeighborAddressSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV8IPv4NeighborAddressSubTLVLength"]
            ),
        )

    @property
    def ValueFieldIpv4NeighborAddress(self):
        """
        Display Name: IPv4 neighbor address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldIpv4NeighborAddress"]),
        )

    @property
    def SubTLV9MaximumLinkBandwidthSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV9MaximumLinkBandwidthSubTLVCode"]
            ),
        )

    @property
    def SubTLV9MaximumLinkBandwidthSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV9MaximumLinkBandwidthSubTLVLength"]
            ),
        )

    @property
    def ValueFieldMaximumLinkBandwidthBytessec(self):
        """
        Display Name: Maximum link bandwidth (Bytes/sec)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValueFieldMaximumLinkBandwidthBytessec"]
            ),
        )

    @property
    def SubTLV10ReservableLinkBandwidthSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV10ReservableLinkBandwidthSubTLVCode"]
            ),
        )

    @property
    def SubTLV10ReservableLinkBandwidthSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV10ReservableLinkBandwidthSubTLVLength"]
            ),
        )

    @property
    def ValueFieldAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 1
        Value Format: decimal
        Available enum values: Cleartext password, 1, Routing domain private authentication method, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldAuthenticationType"])
        )

    @property
    def ValueFieldAuthenticationValue(self):
        """
        Display Name: Authentication value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldAuthenticationValue"]),
        )

    @property
    def SubTLV11UnreservedBandwidthSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV11UnreservedBandwidthSubTLVCode"]
            ),
        )

    @property
    def SubTLV11UnreservedBandwidthSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV11UnreservedBandwidthSubTLVLength"]
            ),
        )

    @property
    def ValueFieldUnreservedBandwidthBytessec(self):
        """
        Display Name: Unreserved bandwidth (Bytes/sec)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValueFieldUnreservedBandwidthBytessec"]
            ),
        )

    @property
    def SubTLV18TEDefaultMetricSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SubTLV18TEDefaultMetricSubTLVCode"]),
        )

    @property
    def SubTLV18TEDefaultMetricSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubTLV18TEDefaultMetricSubTLVLength"]
            ),
        )

    @property
    def ValueFieldTeDefaultMetric(self):
        """
        Display Name: TE Default metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldTeDefaultMetric"])
        )

    @property
    def SubTLV28MTUSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 28
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubTLV28MTUSubTLVCode"])
        )

    @property
    def SubTLV28MTUSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubTLV28MTUSubTLVLength"])
        )

    @property
    def ValueFieldFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: F-bit disabled, 0, F-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldFBit"])
        )

    @property
    def ValueFieldReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldReserved"])
        )

    @property
    def ValueFieldMtu(self):
        """
        Display Name: MTU
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldMtu"]))

    @property
    def Tlv128IPInternalReachabilityCode(self):
        """
        Display Name: Code
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv128IPInternalReachabilityCode"]),
        )

    @property
    def Tlv128IPInternalReachabilityLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv128IPInternalReachabilityLength"]
            ),
        )

    @property
    def ValueEntriesZeroBit(self):
        """
        Display Name: Zero Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesZeroBit"])
        )

    @property
    def ValueEntriesIe(self):
        """
        Display Name: I/E
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesIe"])
        )

    @property
    def ValueEntriesDefaultMETRIC(self):
        """
        Display Name: DEFAULT METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesDefaultMETRIC"])
        )

    @property
    def ValueEntriesS(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesS"]))

    @property
    def ValueEntriesR(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesR"]))

    @property
    def ValueEntriesDelayMETRIC(self):
        """
        Display Name: DELAY METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesDelayMETRIC"])
        )

    @property
    def Tlv128ipinternalreachabilityValueEntriesS(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv128ipinternalreachabilityValueEntriesS"]
            ),
        )

    @property
    def Tlv128ipinternalreachabilityValueEntriesR(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv128ipinternalreachabilityValueEntriesR"]
            ),
        )

    @property
    def ValueEntriesExpenseMETRIC(self):
        """
        Display Name: EXPENSE METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesExpenseMETRIC"])
        )

    @property
    def TlvheadertypeTlv128ipinternalreachabilityValueEntriesS(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv128ipinternalreachabilityValueEntriesS"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv128ipinternalreachabilityValueEntriesR(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv128ipinternalreachabilityValueEntriesR"
                ]
            ),
        )

    @property
    def ValueEntriesErrorMETRIC(self):
        """
        Display Name: ERROR METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesErrorMETRIC"])
        )

    @property
    def ValueEntriesIpADDRESS(self):
        """
        Display Name: IP ADDRESS
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesIpADDRESS"])
        )

    @property
    def ValueEntriesSubnetMASK(self):
        """
        Display Name: SUBNET MASK
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueEntriesSubnetMASK"])
        )

    @property
    def Tlv129ProtocolsSupportedCode(self):
        """
        Display Name: Code
        Default Value: 129
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv129ProtocolsSupportedCode"])
        )

    @property
    def Tlv129ProtocolsSupportedLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv129ProtocolsSupportedLength"]),
        )

    @property
    def NlpidEntriesNlpid(self):
        """
        Display Name: NLPID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NlpidEntriesNlpid"])
        )

    @property
    def Tlv132IPInterfaceAddressCode(self):
        """
        Display Name: Code
        Default Value: 132
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv132IPInterfaceAddressCode"])
        )

    @property
    def Tlv132IPInterfaceAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv132IPInterfaceAddressLength"]),
        )

    @property
    def IpAddressEntriesIpAddress(self):
        """
        Display Name: IP Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddressEntriesIpAddress"])
        )

    @property
    def Tlv142GroupAddressType(self):
        """
        Display Name: Type
        Default Value: 142
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv142GroupAddressType"])
        )

    @property
    def Tlv142GroupAddressLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv142GroupAddressLength"])
        )

    @property
    def SubtlvSubTLVsNoSubTLVs(self):
        """
        Display Name: No sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtlvSubTLVsNoSubTLVs"])
        )

    @property
    def GroupMACAddressType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressType"])
        )

    @property
    def GroupMACAddressLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressLength"])
        )

    @property
    def GroupMACAddressResv(self):
        """
        Display Name: Resv
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressResv"])
        )

    @property
    def GroupMACAddressTopologyID(self):
        """
        Display Name: Topology-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressTopologyID"])
        )

    @property
    def GroupMACAddressResv2(self):
        """
        Display Name: Resv2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressResv2"])
        )

    @property
    def GroupMACAddressVlanID(self):
        """
        Display Name: VLAN-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressVlanID"])
        )

    @property
    def GroupMACAddressNumGroupRecords(self):
        """
        Display Name: Num Group Recs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressNumGroupRecords"]),
        )

    @property
    def GroupRecordsNumOfSources(self):
        """
        Display Name: Num of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordsNumOfSources"])
        )

    @property
    def GroupRecordsGroupAddress(self):
        """
        Display Name: Group Address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordsGroupAddress"])
        )

    @property
    def ValueSourceAddress(self):
        """
        Display Name: Source Address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueSourceAddress"])
        )

    @property
    def GroupIPAddressType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressType"])
        )

    @property
    def GroupIPAddressLength(self):
        """
        Display Name: Length
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressLength"])
        )

    @property
    def GroupIPAddressResv(self):
        """
        Display Name: Resv
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressResv"])
        )

    @property
    def GroupIPAddressTopologyID(self):
        """
        Display Name: Topology-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressTopologyID"])
        )

    @property
    def GroupIPAddressResv2(self):
        """
        Display Name: Resv2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressResv2"])
        )

    @property
    def GroupIPAddressVlanID(self):
        """
        Display Name: VLAN-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressVlanID"])
        )

    @property
    def GroupIPAddressNumGroupRecords(self):
        """
        Display Name: Num Group Recs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupIPAddressNumGroupRecords"]),
        )

    @property
    def GroupipaddressGroupRecordsNumOfSources(self):
        """
        Display Name: Num of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupipaddressGroupRecordsNumOfSources"]
            ),
        )

    @property
    def GroupipaddressGroupRecordsGroupAddress(self):
        """
        Display Name: Group Address
        Default Value: 0:0:0:0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupipaddressGroupRecordsGroupAddress"]
            ),
        )

    @property
    def GrouprecordsValueSourceAddress(self):
        """
        Display Name: Source Address
        Default Value: 0:0:0:0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GrouprecordsValueSourceAddress"]),
        )

    @property
    def GroupIPv6AddressType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressType"])
        )

    @property
    def GroupIPv6AddressLength(self):
        """
        Display Name: Length
        Default Value: 38
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressLength"])
        )

    @property
    def GroupIPv6AddressResv(self):
        """
        Display Name: Resv
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressResv"])
        )

    @property
    def GroupIPv6AddressTopologyID(self):
        """
        Display Name: Topology-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressTopologyID"])
        )

    @property
    def GroupIPv6AddressResv2(self):
        """
        Display Name: Resv2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressResv2"])
        )

    @property
    def GroupIPv6AddressVlanID(self):
        """
        Display Name: VLAN-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressVlanID"])
        )

    @property
    def GroupIPv6AddressNumGroupRecords(self):
        """
        Display Name: Num Group Recs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GroupIPv6AddressNumGroupRecords"]),
        )

    @property
    def Groupipv6addressGroupRecordsNumOfSources(self):
        """
        Display Name: Num of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Groupipv6addressGroupRecordsNumOfSources"]
            ),
        )

    @property
    def Groupipv6addressGroupRecordsGroupAddress(self):
        """
        Display Name: Group Address
        Default Value: 0:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Groupipv6addressGroupRecordsGroupAddress"]
            ),
        )

    @property
    def Groupipv6addressGrouprecordsValueSourceAddress(self):
        """
        Display Name: Source Address
        Default Value: 0:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Groupipv6addressGrouprecordsValueSourceAddress"]
            ),
        )

    @property
    def Tlv232IPv6InterfaceAddressCode(self):
        """
        Display Name: Code
        Default Value: 232
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv232IPv6InterfaceAddressCode"]),
        )

    @property
    def Tlv232IPv6InterfaceAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv232IPv6InterfaceAddressLength"]),
        )

    @property
    def Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress(self):
        """
        Display Name: IP Address
        Default Value: 0:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress"]
            ),
        )

    @property
    def Tlv237MultiTopologyReachableIPv6PrefixesTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 237
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv237MultiTopologyReachableIPv6PrefixesTlvCode"]
            ),
        )

    @property
    def Tlv237MultiTopologyReachableIPv6PrefixesLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv237MultiTopologyReachableIPv6PrefixesLength"]
            ),
        )

    @property
    def ValueFieldReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldReservedBit"])
        )

    @property
    def ValueFieldExtendedIntermediateSystemTLVFormat(self):
        """
        Display Name: Extended intermediate system TLV format
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValueFieldExtendedIntermediateSystemTLVFormat"]
            ),
        )

    @property
    def Tlv242RouterCapabilityCode(self):
        """
        Display Name: Code
        Default Value: 242
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv242RouterCapabilityCode"])
        )

    @property
    def Tlv242RouterCapabilityLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv242RouterCapabilityLength"])
        )

    @property
    def ValueRouterID(self):
        """
        Display Name: Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueRouterID"]))

    @property
    def ValueFlag(self):
        """
        Display Name: FLAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueFlag"]))

    @property
    def SubTLVHeaderTypeNoSubTLVs(self):
        """
        Display Name: No sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubTLVHeaderTypeNoSubTLVs"])
        )

    @property
    def DeviceIDType(self):
        """
        Display Name: TYPE
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DeviceIDType"]))

    @property
    def DeviceIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DeviceIDLength"])
        )

    @property
    def DeviceIDReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DeviceIDReserved1"])
        )

    @property
    def DeviceIDPriority(self):
        """
        Display Name: Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DeviceIDPriority"])
        )

    @property
    def DeviceIDReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DeviceIDReserved2"])
        )

    @property
    def DeviceIDDeviceID(self):
        """
        Display Name: Device ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DeviceIDDeviceID"])
        )

    @property
    def TRILLVerType(self):
        """
        Display Name: TYPE
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TRILLVerType"]))

    @property
    def TRILLVerLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TRILLVerLength"])
        )

    @property
    def TRILLVerMaxVersion(self):
        """
        Display Name: Max-Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TRILLVerMaxVersion"])
        )

    @property
    def RootPriorityType(self):
        """
        Display Name: TYPE
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RootPriorityType"])
        )

    @property
    def RootPriorityLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RootPriorityLength"])
        )

    @property
    def RootPriorityBroadcastPriority(self):
        """
        Display Name: Broadcast Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RootPriorityBroadcastPriority"]),
        )

    @property
    def RootPriorityNumberOfMultiDestinationTree(self):
        """
        Display Name: Number of MultiDestination tree
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RootPriorityNumberOfMultiDestinationTree"]
            ),
        )

    @property
    def NickNameType(self):
        """
        Display Name: TYPE
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NickNameType"]))

    @property
    def NickNameLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NickNameLength"])
        )

    @property
    def NicknameRecordNickPri(self):
        """
        Display Name: Nickname.Pri
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NicknameRecordNickPri"])
        )

    @property
    def NicknameRecordTreePri(self):
        """
        Display Name: Tree Root Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NicknameRecordTreePri"])
        )

    @property
    def NicknameRecordNickname(self):
        """
        Display Name: Nickname
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NicknameRecordNickname"])
        )

    @property
    def TreesType(self):
        """
        Display Name: TYPE
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TreesType"]))

    @property
    def TreesLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TreesLength"]))

    @property
    def TreesNoOfTreesToCompute(self):
        """
        Display Name: Number of trees to compute
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TreesNoOfTreesToCompute"])
        )

    @property
    def TreesMaxNoOfTreesAbleToCompute(self):
        """
        Display Name: Number of trees to compute
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TreesMaxNoOfTreesAbleToCompute"]),
        )

    @property
    def TreesNoOfTreesToUse(self):
        """
        Display Name: Number of trees to use
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TreesNoOfTreesToUse"])
        )

    @property
    def RootIDsType(self):
        """
        Display Name: TYPE
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RootIDsType"]))

    @property
    def RootIDsLength(self):
        """
        Display Name: Length
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RootIDsLength"]))

    @property
    def RootIDsBroadcastRootSystemID(self):
        """
        Display Name: Broadcast Root System ID
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RootIDsBroadcastRootSystemID"])
        )

    @property
    def MulticastRootSystemIDMulticastRootSystemId(self):
        """
        Display Name: Multicast Root System Id
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastRootSystemIDMulticastRootSystemId"]
            ),
        )

    @property
    def TreeRootIDsType(self):
        """
        Display Name: TYPE
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TreeRootIDsType"])
        )

    @property
    def TreeRootIDsLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TreeRootIDsLength"])
        )

    @property
    def TreeRootIDsStartingTreeNum(self):
        """
        Display Name: Starting Tree Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TreeRootIDsStartingTreeNum"])
        )

    @property
    def TreeRtIDNicknameTreeRtidNickname(self):
        """
        Display Name: Nickname
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TreeRtIDNicknameTreeRtidNickname"]),
        )

    @property
    def IntVLANType(self):
        """
        Display Name: TYPE
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IntVLANType"]))

    @property
    def IntVLANLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IntVLANLength"]))

    @property
    def IntVLANIntVLANNickname(self):
        """
        Display Name: Nickname
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntVLANIntVLANNickname"])
        )

    @property
    def InterestedVLANsM4bit(self):
        """
        Display Name: M4 bit
        Default Value: 0
        Value Format: decimal
        Available enum values: M4 bit disabled, 0, M4 bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterestedVLANsM4bit"])
        )

    @property
    def InterestedVLANsM6bit(self):
        """
        Display Name: M6 bit
        Default Value: 0
        Value Format: decimal
        Available enum values: M6 bit disabled, 0, M6 bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterestedVLANsM6bit"])
        )

    @property
    def InterestedVLANsIntVLANReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["InterestedVLANsIntVLANReserved"]),
        )

    @property
    def InterestedVLANsIntVLANStart(self):
        """
        Display Name: VLAN.start
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterestedVLANsIntVLANStart"])
        )

    @property
    def InterestedVLANsReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterestedVLANsReserved2"])
        )

    @property
    def InterestedVLANsIntVLANEnd(self):
        """
        Display Name: VLAN.end
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterestedVLANsIntVLANEnd"])
        )

    @property
    def IntVLANIntVLANAppFwderStatus(self):
        """
        Display Name: Appointed Forwarder Status Lost Counter
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntVLANIntVLANAppFwderStatus"])
        )

    @property
    def IntVLANRootBridgesIntVLANRootBridge(self):
        """
        Display Name: Root Bridge
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntVLANRootBridgesIntVLANRootBridge"]
            ),
        )

    @property
    def DceftagType(self):
        """
        Display Name: TYPE
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DceftagType"]))

    @property
    def DceftagLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DceftagLength"]))

    @property
    def DceftagFtagvalue(self):
        """
        Display Name: FTAG-Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DceftagFtagvalue"])
        )

    @property
    def Tlv144MTCapabilityCode(self):
        """
        Display Name: Code
        Default Value: 144
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv144MTCapabilityCode"])
        )

    @property
    def Tlv144MTCapabilityLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv144MTCapabilityLength"])
        )

    @property
    def ValueOBit(self):
        """
        Display Name: O bit
        Default Value: 0
        Value Format: decimal
        Available enum values: O-bit disabled, 0, O-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueOBit"]))

    @property
    def ValueRbit(self):
        """
        Display Name: Reserved Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueRbit"]))

    @property
    def ValueMtID(self):
        """
        Display Name: MT ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueMtID"]))

    @property
    def SubtlvheaderSubTLVHeaderTypeNoSubTLVs(self):
        """
        Display Name: No sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtlvheaderSubTLVHeaderTypeNoSubTLVs"]
            ),
        )

    @property
    def InstanceType(self):
        """
        Display Name: TYPE
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["InstanceType"]))

    @property
    def InstanceLength(self):
        """
        Display Name: Length
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstanceLength"])
        )

    @property
    def InstanceCistroot(self):
        """
        Display Name: CIST Root Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstanceCistroot"])
        )

    @property
    def InstanceCistcost(self):
        """
        Display Name: CIST External Root Cost
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstanceCistcost"])
        )

    @property
    def InstanceBridgepriority(self):
        """
        Display Name: Bridge Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstanceBridgepriority"])
        )

    @property
    def InstanceResvbit(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstanceResvbit"])
        )

    @property
    def InstanceVBit(self):
        """
        Display Name: V bit
        Default Value: 0
        Value Format: decimal
        Available enum values: V-bit disabled, 0, V-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["InstanceVBit"]))

    @property
    def InstanceTrees(self):
        """
        Display Name: No Of Trees
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["InstanceTrees"]))

    @property
    def VlanidTupleUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: U-bit disabled, 0, U-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleUBit"])
        )

    @property
    def VlanidTupleMBit(self):
        """
        Display Name: M bit
        Default Value: 0
        Value Format: decimal
        Available enum values: M-bit disabled, 0, M-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleMBit"])
        )

    @property
    def VlanidTupleABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: A-bit disabled, 0, A-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleABit"])
        )

    @property
    def VlanidTupleRbit(self):
        """
        Display Name: Reserved-Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleRbit"])
        )

    @property
    def VlanidTupleEct_algo(self):
        """
        Display Name: ECT Algorithm
        Default Value: 8438273
        Value Format: decimal
        Available enum values: ECT_ALGORITHM 1, 8438273, ECT_ALGORITHM 2, 8438274, ECT_ALGORITHM 3, 8438275, ECT_ALGORITHM 4, 8438276, ECT_ALGORITHM 5, 8438277, ECT_ALGORITHM 6, 8438278, ECT_ALGORITHM 7, 8438279, ECT_ALGORITHM 8, 8438280, ECT_ALGORITHM 9, 8438281, ECT_ALGORITHM 10, 8438282, ECT_ALGORITHM 11, 8438283, ECT_ALGORITHM 12, 8438284, ECT_ALGORITHM 13, 8438285, ECT_ALGORITHM 14, 8438286, ECT_ALGORITHM 15, 8438287, ECT_ALGORITHM 16, 8438288
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleEct_algo"])
        )

    @property
    def VlanidTupleBasevid(self):
        """
        Display Name: Base-VID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleBasevid"])
        )

    @property
    def VlanidTupleSpvid(self):
        """
        Display Name: SPVID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanidTupleSpvid"])
        )

    @property
    def ServiceIDType(self):
        """
        Display Name: TYPE
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServiceIDType"]))

    @property
    def ServiceIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIDLength"])
        )

    @property
    def ServiceIDBmac(self):
        """
        Display Name: B-MAC
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServiceIDBmac"]))

    @property
    def ServiceIDResvbits(self):
        """
        Display Name: Reserved-BITS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIDResvbits"])
        )

    @property
    def ServiceIDBasevid(self):
        """
        Display Name: Base-VID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIDBasevid"])
        )

    @property
    def ServiceIdIsidTBit(self):
        """
        Display Name: T bit
        Default Value: 0
        Value Format: decimal
        Available enum values: V-bit disabled, 0, V-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIdIsidTBit"])
        )

    @property
    def ServiceIdIsidRBit(self):
        """
        Display Name: R bit
        Default Value: 0
        Value Format: decimal
        Available enum values: R-bit disabled, 0, R-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIdIsidRBit"])
        )

    @property
    def ServiceIdIsidRsvbit(self):
        """
        Display Name: Reserved Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIdIsidRsvbit"])
        )

    @property
    def ServiceIdIsidIsid(self):
        """
        Display Name: ISID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceIdIsidIsid"])
        )

    @property
    def Tlv141MACReachabilityType(self):
        """
        Display Name: Type
        Default Value: 141
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv141MACReachabilityType"])
        )

    @property
    def Tlv141MACReachabilityLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv141MACReachabilityLength"])
        )

    @property
    def Tlv141MACReachabilityVlanID(self):
        """
        Display Name: Vlan-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv141MACReachabilityVlanID"])
        )

    @property
    def MacAddressMacAddress(self):
        """
        Display Name: MAC Address
        Default Value: 0:0:0:0:0:0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacAddressMacAddress"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
