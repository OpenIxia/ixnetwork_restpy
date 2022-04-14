from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisLevel2LinkStatePDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisLevel2LinkStatePDU"
    _SDM_ATT_MAP = {
        "CommonHeaderIntradomainRoutingProtocolDiscriminator": "isisLevel2LinkStatePDU.isisHeader.commonHeader.intradomainRoutingProtocolDiscriminator-1",
        "CommonHeaderLengthIndicator": "isisLevel2LinkStatePDU.isisHeader.commonHeader.lengthIndicator-2",
        "CommonHeaderVersionProtocolIDExtension": "isisLevel2LinkStatePDU.isisHeader.commonHeader.versionProtocolIDExtension-3",
        "CommonHeaderIdLength": "isisLevel2LinkStatePDU.isisHeader.commonHeader.idLength-4",
        "CommonHeaderReservedBit": "isisLevel2LinkStatePDU.isisHeader.commonHeader.reservedBit-5",
        "CommonHeaderPduType": "isisLevel2LinkStatePDU.isisHeader.commonHeader.pduType-6",
        "CommonHeaderVersion": "isisLevel2LinkStatePDU.isisHeader.commonHeader.version-7",
        "CommonHeaderReserved": "isisLevel2LinkStatePDU.isisHeader.commonHeader.reserved-8",
        "CommonHeaderMaximumAreaAddresses": "isisLevel2LinkStatePDU.isisHeader.commonHeader.maximumAreaAddresses-9",
        "FixedHeaderPduLength": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.pduLength-10",
        "FixedHeaderRemainingLifetime": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.remainingLifetime-11",
        "LspIDPseudonodeID": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.lspID.pseudonodeID-12",
        "LspIDLspNumber": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.lspID.lspNumber-13",
        "FixedHeaderSequenceNumber": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.sequenceNumber-14",
        "FixedHeaderChecksum": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.checksum-15",
        "FixedHeaderPartitionRepairBit": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.partitionRepairBit-16",
        "FixedHeaderAttached": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.attached-17",
        "FixedHeaderLspDatabaseOverload": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.lspDatabaseOverload-18",
        "FixedHeaderIsType": "isisLevel2LinkStatePDU.isisHeader.fixedHeader.isType-19",
        "Tlv1AreaAddressesTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvCode-20",
        "Tlv1AreaAddressesTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvLength-21",
        "ValueFieldsAddressLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.addressLength-22",
        "ValueFieldsAreaAddress": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.areaAddress-23",
        "Tlv2ISNeighborsTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.tlvCode-24",
        "Tlv2ISNeighborsTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.tlvLength-25",
        "ValueFieldsVirtualFlag": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.virtualFlag-26",
        "Tlv2RepeatingFieldsReservedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.reservedBit-27",
        "Tlv2RepeatingFieldsInternalMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-28",
        "Tlv2RepeatingFieldsDefaultMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.defaultMetric-29",
        "Tlv2RepeatingFieldsSupportedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-30",
        "ValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-31",
        "Tlv2RepeatingFieldsDelayMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.delayMetric-32",
        "ValuefieldsTlv2RepeatingFieldsSupportedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-33",
        "Tlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-34",
        "Tlv2RepeatingFieldsExpenseMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.expenseMetric-35",
        "Tlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-36",
        "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-37",
        "ValuefieldsTlv2RepeatingFieldsExpenseMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.expenseMetric-38",
        "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsSupportedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.supportedBit-39",
        "TlvheadertypeTlv2isneighborsValuefieldsTlv2RepeatingFieldsInternalMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.internalMetric-40",
        "Tlv2RepeatingFieldsErrorMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.errorMetric-41",
        "NeighborIDNeighborID": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.neighborID.neighborID-42",
        "NeighborIDPadding8Bits": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv2ISNeighbors.valueFields.tlv2RepeatingFields.neighborID.padding8Bits-43",
        "Tlv3EndSystemNeighborsTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.tlvCode-44",
        "Tlv3EndSystemNeighborsTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.tlvLength-45",
        "ValueFieldsReserved": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.valueFields.reserved-46",
        "ValueFieldsNeighborID": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv3EndSystemNeighbors.valueFields.neighborID-47",
        "Tlv10AuthenticationInformationTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvCode-48",
        "Tlv10AuthenticationInformationTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvLength-49",
        "ValueFieldsAuthenticationType": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationType-50",
        "ValueFieldsAuthenticationValue": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationValue-51",
        "Tlv14OriginatingLSPBufferSizeTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv14OriginatingLSPBufferSize.tlvCode-52",
        "Tlv14OriginatingLSPBufferSizeTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv14OriginatingLSPBufferSize.tlvLength-53",
        "Tlv14OriginatingLSPBufferSizeValue": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv14OriginatingLSPBufferSize.value-54",
        "Tlv22ExtendedISReachabilityTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.tlvCode-55",
        "Tlv22ExtendedISReachabilityTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.tlvLength-56",
        "ValueFieldSystemIDAndPseudonodeNumber": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.systemIDAndPseudonodeNumber-57",
        "ValueFieldDefaultMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.defaultMetric-58",
        "ValueFieldLengthOfSubTLVs": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.lengthOfSubTLVs-59",
        "SubTLVsNoSubTLVs": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.noSubTLVs-60",
        "SubTLV3AdministrativeGroupSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV3AdministrativeGroup.subTLVCode-61",
        "SubTLV3AdministrativeGroupSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV3AdministrativeGroup.subTLVLength-62",
        "ValueFieldAdministrativeGroup": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV3AdministrativeGroup.valueField.administrativeGroup-63",
        "SubTLV6IPv4InterfaceAddressSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV6IPv4InterfaceAddress.subTLVCode-64",
        "SubTLV6IPv4InterfaceAddressSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV6IPv4InterfaceAddress.subTLVLength-65",
        "ValueFieldIpv4InterfaceAddress": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV6IPv4InterfaceAddress.valueField.ipv4InterfaceAddress-66",
        "SubTLV8IPv4NeighborAddressSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV8IPv4NeighborAddress.subTLVCode-67",
        "SubTLV8IPv4NeighborAddressSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV8IPv4NeighborAddress.subTLVLength-68",
        "ValueFieldIpv4NeighborAddress": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV8IPv4NeighborAddress.valueField.ipv4NeighborAddress-69",
        "SubTLV9MaximumLinkBandwidthSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV9MaximumLinkBandwidth.subTLVCode-70",
        "SubTLV9MaximumLinkBandwidthSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV9MaximumLinkBandwidth.subTLVLength-71",
        "ValueFieldMaximumLinkBandwidthBytessec": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV9MaximumLinkBandwidth.valueField.maximumLinkBandwidthBytessec-72",
        "SubTLV10ReservableLinkBandwidthSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.subTLVCode-73",
        "SubTLV10ReservableLinkBandwidthSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.subTLVLength-74",
        "ValueFieldAuthenticationType": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.valueField.authenticationType-75",
        "ValueFieldAuthenticationValue": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV10ReservableLinkBandwidth.valueField.authenticationValue-76",
        "SubTLV11UnreservedBandwidthSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV11UnreservedBandwidth.subTLVCode-77",
        "SubTLV11UnreservedBandwidthSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV11UnreservedBandwidth.subTLVLength-78",
        "ValueFieldUnreservedBandwidthBytessec": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV11UnreservedBandwidth.valueField.unreservedBandwidthBytessec-79",
        "SubTLV18TEDefaultMetricSubTLVCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV18TEDefaultMetric.subTLVCode-80",
        "SubTLV18TEDefaultMetricSubTLVLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV18TEDefaultMetric.subTLVLength-81",
        "ValueFieldTeDefaultMetric": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv22ExtendedISReachability.valueField.subTLV.subTLVs.subTLV18TEDefaultMetric.valueField.teDefaultMetric-82",
        "Tlv128IPInternalReachabilityCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.code-83",
        "Tlv128IPInternalReachabilityLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.length-84",
        "ValueEntriesZeroBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.zeroBit-85",
        "ValueEntriesIe": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.ie-86",
        "ValueEntriesDefaultMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.defaultMETRIC-87",
        "ValueEntriesS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.s-88",
        "ValueEntriesR": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.r-89",
        "ValueEntriesDelayMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.delayMETRIC-90",
        "Tlv128ipinternalreachabilityValueEntriesS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.s-91",
        "Tlv128ipinternalreachabilityValueEntriesR": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.r-92",
        "ValueEntriesExpenseMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.expenseMETRIC-93",
        "TlvheadertypeTlv128ipinternalreachabilityValueEntriesS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.s-94",
        "TlvheadertypeTlv128ipinternalreachabilityValueEntriesR": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.r-95",
        "ValueEntriesErrorMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.errorMETRIC-96",
        "ValueEntriesIpADDRESS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.ipADDRESS-97",
        "ValueEntriesSubnetMASK": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv128IPInternalReachability.valueEntries.subnetMASK-98",
        "Tlv129ProtocolsSupportedCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.code-99",
        "Tlv129ProtocolsSupportedLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.length-100",
        "NlpidEntriesNlpid": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.nlpid-101",
        "Tlv130IPExternalReachabilityCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.code-102",
        "Tlv130IPExternalReachabilityLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.length-103",
        "Tlv130ipexternalreachabilityValueEntriesZeroBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.zeroBit-104",
        "Tlv130ipexternalreachabilityValueEntriesIe": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.ie-105",
        "Tlv130ipexternalreachabilityValueEntriesDefaultMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.defaultMETRIC-106",
        "Tlv130ipexternalreachabilityValueEntriesS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.s-107",
        "Tlv130ipexternalreachabilityValueEntriesR": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.r-108",
        "Tlv130ipexternalreachabilityValueEntriesDelayMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.delayMETRIC-109",
        "TlvheadertypeTlv130ipexternalreachabilityValueEntriesS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.s-110",
        "TlvheadertypeTlv130ipexternalreachabilityValueEntriesR": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.r-111",
        "Tlv130ipexternalreachabilityValueEntriesExpenseMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.expenseMETRIC-112",
        "TlvheadertypeTlv130ipexternalreachabilityValueEntriesS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.s-113",
        "TlvheadertypeTlv130ipexternalreachabilityValueEntriesR": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.r-114",
        "Tlv130ipexternalreachabilityValueEntriesErrorMETRIC": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.errorMETRIC-115",
        "Tlv130ipexternalreachabilityValueEntriesIpADDRESS": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.ipADDRESS-116",
        "Tlv130ipexternalreachabilityValueEntriesSubnetMASK": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv130IPExternalReachability.valueEntries.subnetMASK-117",
        "Tlv131InterDomainRoutingProtocolInfoCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv131InterDomainRoutingProtocolInfo.code-118",
        "Tlv131InterDomainRoutingProtocolInfoLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv131InterDomainRoutingProtocolInfo.length-119",
        "Tlv131InterDomainRoutingProtocolInfoInterDomainInformationType": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv131InterDomainRoutingProtocolInfo.interDomainInformationType-120",
        "Tlv131InterDomainRoutingProtocolInfoInfoLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv131InterDomainRoutingProtocolInfo.infoLength-121",
        "Tlv131InterDomainRoutingProtocolInfoExternalInformation": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv131InterDomainRoutingProtocolInfo.externalInformation-122",
        "Tlv132IPInterfaceAddressCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.code-123",
        "Tlv132IPInterfaceAddressLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.length-124",
        "IpAddressEntriesIpAddress": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.ipAddressEntries.ipAddress-125",
        "Tlv232IPv6InterfaceAddressCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.code-126",
        "Tlv232IPv6InterfaceAddressLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.length-127",
        "Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.ipAddressEntries.ipAddress-128",
        "Tlv237MultiTopologyReachableIPv6PrefixesTlvCode": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.tlvCode-129",
        "Tlv237MultiTopologyReachableIPv6PrefixesTlvLength": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.tlvLength-130",
        "ValueFieldReservedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.reservedBit-131",
        "Tlv237multitopologyreachableipv6prefixesValueFieldReservedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.reservedBit-132",
        "TlvheadertypeTlv237multitopologyreachableipv6prefixesValueFieldReservedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.reservedBit-133",
        "TlvheadertypeTlv237multitopologyreachableipv6prefixesValueFieldReservedBit": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.reservedBit-134",
        "ValueFieldExtendedIntermediateSystemTLVFormat": "isisLevel2LinkStatePDU.isisHeader.tlvHeader.tlvHeaderType.tlv237MultiTopologyReachableIPv6Prefixes.valueField.extendedIntermediateSystemTLVFormat-135",
    }

    def __init__(self, parent, list_op=False):
        super(IsisLevel2LinkStatePDU, self).__init__(parent, list_op)

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
        Default Value: 20
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
        Value Format: decimal
        Available enum values: Must be Zero, 0
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
        Value Format: decimal
        Available enum values: Zero, indicating Internal Metric, 0
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
        Value Format: decimal
        Available enum values: Zero, indicating Internal Metric, 0
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
        Value Format: decimal
        Available enum values: Zero, indicating Internal Metric, 0
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
        Value Format: decimal
        Available enum values: Zero, indicating Internal Metric, 0
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
        Value Format: decimal
        Available enum values: Zero, indicating Internal Metric, 0
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
        Default Value: 2
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
    def Tlv130IPExternalReachabilityCode(self):
        """
        Display Name: Code
        Default Value: 130
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv130IPExternalReachabilityCode"]),
        )

    @property
    def Tlv130IPExternalReachabilityLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130IPExternalReachabilityLength"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesZeroBit(self):
        """
        Display Name: Zero Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesZeroBit"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesIe(self):
        """
        Display Name: I/E
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesIe"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesDefaultMETRIC(self):
        """
        Display Name: DEFAULT METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv130ipexternalreachabilityValueEntriesDefaultMETRIC"
                ]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesS(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesS"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesR(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesR"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesDelayMETRIC(self):
        """
        Display Name: DELAY METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesDelayMETRIC"]
            ),
        )

    @property
    def TlvheadertypeTlv130ipexternalreachabilityValueEntriesS(self):
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
                    "TlvheadertypeTlv130ipexternalreachabilityValueEntriesS"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv130ipexternalreachabilityValueEntriesR(self):
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
                    "TlvheadertypeTlv130ipexternalreachabilityValueEntriesR"
                ]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesExpenseMETRIC(self):
        """
        Display Name: EXPENSE METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv130ipexternalreachabilityValueEntriesExpenseMETRIC"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv130ipexternalreachabilityValueEntriesS(self):
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
                    "TlvheadertypeTlv130ipexternalreachabilityValueEntriesS"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv130ipexternalreachabilityValueEntriesR(self):
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
                    "TlvheadertypeTlv130ipexternalreachabilityValueEntriesR"
                ]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesErrorMETRIC(self):
        """
        Display Name: ERROR METRIC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesErrorMETRIC"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesIpADDRESS(self):
        """
        Display Name: IP ADDRESS
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesIpADDRESS"]
            ),
        )

    @property
    def Tlv130ipexternalreachabilityValueEntriesSubnetMASK(self):
        """
        Display Name: SUBNET MASK
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv130ipexternalreachabilityValueEntriesSubnetMASK"]
            ),
        )

    @property
    def Tlv131InterDomainRoutingProtocolInfoCode(self):
        """
        Display Name: Code
        Default Value: 131
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv131InterDomainRoutingProtocolInfoCode"]
            ),
        )

    @property
    def Tlv131InterDomainRoutingProtocolInfoLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv131InterDomainRoutingProtocolInfoLength"]
            ),
        )

    @property
    def Tlv131InterDomainRoutingProtocolInfoInterDomainInformationType(self):
        """
        Display Name: Inter-Domain Information Type
        Default Value: 0
        Value Format: decimal
        Available enum values: Reserved, 0, External info follows locally specified format, 1, External info contains autonomous tag, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv131InterDomainRoutingProtocolInfoInterDomainInformationType"
                ]
            ),
        )

    @property
    def Tlv131InterDomainRoutingProtocolInfoInfoLength(self):
        """
        Display Name: Info length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv131InterDomainRoutingProtocolInfoInfoLength"]
            ),
        )

    @property
    def Tlv131InterDomainRoutingProtocolInfoExternalInformation(self):
        """
        Display Name: External Information
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv131InterDomainRoutingProtocolInfoExternalInformation"
                ]
            ),
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
    def Tlv237MultiTopologyReachableIPv6PrefixesTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv237MultiTopologyReachableIPv6PrefixesTlvLength"]
            ),
        )

    @property
    def ValueFieldReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Must be Zero, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldReservedBit"])
        )

    @property
    def Tlv237multitopologyreachableipv6prefixesValueFieldReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Must be Zero, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv237multitopologyreachableipv6prefixesValueFieldReservedBit"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv237multitopologyreachableipv6prefixesValueFieldReservedBit(
        self,
    ):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Must be Zero, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv237multitopologyreachableipv6prefixesValueFieldReservedBit"
                ]
            ),
        )

    @property
    def TlvheadertypeTlv237multitopologyreachableipv6prefixesValueFieldReservedBit(
        self,
    ):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Must be Zero, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvheadertypeTlv237multitopologyreachableipv6prefixesValueFieldReservedBit"
                ]
            ),
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
