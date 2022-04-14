from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Icmpv6(Base):
    __slots__ = ()
    _SDM_NAME = "icmpv6"
    _SDM_ATT_MAP = {
        "DestinationUnreachableMessageMesageType": "icmpv6.icmpv6Message.icmpv6MessegeType.destinationUnreachableMessage.mesageType-1",
        "DestinationUnreachableMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.destinationUnreachableMessage.code-2",
        "DestinationUnreachableMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.destinationUnreachableMessage.checksum-3",
        "DestinationUnreachableMessageUnused": "icmpv6.icmpv6Message.icmpv6MessegeType.destinationUnreachableMessage.unused-4",
        "PacketTooBigMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.packetTooBigMessage.messageType-5",
        "PacketTooBigMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.packetTooBigMessage.code-6",
        "PacketTooBigMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.packetTooBigMessage.checksum-7",
        "PacketTooBigMessageMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.packetTooBigMessage.maximumTransmissionUnit-8",
        "TimeExceededMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.timeExceededMessage.messageType-9",
        "TimeExceededMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.timeExceededMessage.code-10",
        "TimeExceededMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.timeExceededMessage.checksum-11",
        "TimeExceededMessageUnused": "icmpv6.icmpv6Message.icmpv6MessegeType.timeExceededMessage.unused-12",
        "ParameterProblemMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.parameterProblemMessage.messageType-13",
        "ParameterProblemMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.parameterProblemMessage.code-14",
        "ParameterProblemMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.parameterProblemMessage.checksum-15",
        "ParameterProblemMessagePointer": "icmpv6.icmpv6Message.icmpv6MessegeType.parameterProblemMessage.pointer-16",
        "EchoRequestMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.echoRequestMessage.messageType-17",
        "EchoRequestMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.echoRequestMessage.code-18",
        "EchoRequestMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.echoRequestMessage.checksum-19",
        "EchoRequestMessageIdentifier": "icmpv6.icmpv6Message.icmpv6MessegeType.echoRequestMessage.identifier-20",
        "EchoRequestMessageSequenceNumber": "icmpv6.icmpv6Message.icmpv6MessegeType.echoRequestMessage.sequenceNumber-21",
        "EchoReplyMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.echoReplyMessage.messageType-22",
        "EchoReplyMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.echoReplyMessage.code-23",
        "EchoReplyMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.echoReplyMessage.checksum-24",
        "EchoReplyMessageIdentifier": "icmpv6.icmpv6Message.icmpv6MessegeType.echoReplyMessage.identifier-25",
        "EchoReplyMessageSequenceNumber": "icmpv6.icmpv6Message.icmpv6MessegeType.echoReplyMessage.sequenceNumber-26",
        "MulticastListenerQueryMessageVersion1MessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion1.messageType-27",
        "MulticastListenerQueryMessageVersion1Code": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion1.code-28",
        "MulticastListenerQueryMessageVersion1Checksum": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion1.checksum-29",
        "MulticastListenerQueryMessageVersion1MaximumResponseDelaymilliseconds": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion1.maximumResponseDelaymilliseconds-30",
        "MulticastListenerQueryMessageVersion1Reserved": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion1.reserved-31",
        "MulticastListenerQueryMessageVersion1MulticastAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion1.multicastAddress-32",
        "MulticastListenerReportMessageVersion1MessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion1.messageType-33",
        "MulticastListenerReportMessageVersion1Code": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion1.code-34",
        "MulticastListenerReportMessageVersion1Checksum": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion1.checksum-35",
        "MulticastListenerReportMessageVersion1MaximumResponseDelaymilliseconds": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion1.maximumResponseDelaymilliseconds-36",
        "MulticastListenerReportMessageVersion1Reserved": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion1.reserved-37",
        "MulticastListenerReportMessageVersion1MulticastAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion1.multicastAddress-38",
        "MulticastListenerDoneMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerDoneMessage.messageType-39",
        "MulticastListenerDoneMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerDoneMessage.code-40",
        "MulticastListenerDoneMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerDoneMessage.checksum-41",
        "MulticastListenerDoneMessageMaximumResponseDelaymilliseconds": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerDoneMessage.maximumResponseDelaymilliseconds-42",
        "MulticastListenerDoneMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerDoneMessage.reserved-43",
        "MulticastListenerDoneMessageMulticastAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerDoneMessage.multicastAddress-44",
        "MulticastListenerQueryMessageVersion2MessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.messageType-45",
        "MulticastListenerQueryMessageVersion2Code": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.code-46",
        "MulticastListenerQueryMessageVersion2Checksum": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.checksum-47",
        "MulticastListenerQueryMessageVersion2MaximumResponseDelaymilliseconds": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.maximumResponseDelaymilliseconds-48",
        "MulticastListenerQueryMessageVersion2Reserved": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.reserved-49",
        "MulticastListenerQueryMessageVersion2MulticastAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.multicastAddress-50",
        "MulticastListenerQueryMessageVersion2Reserved": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.reserved-51",
        "MulticastListenerQueryMessageVersion2SuppressRoutersideProcessingSFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.suppressRoutersideProcessingSFlag-52",
        "MulticastListenerQueryMessageVersion2Qrv": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.qrv-53",
        "MulticastListenerQueryMessageVersion2Qqic": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.qqic-54",
        "MulticastListenerQueryMessageVersion2NumberOfSources": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.numberOfSources-55",
        "SourceAddressEntriesSourceAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerQueryMessageVersion2.sourceAddressEntries.sourceAddress-56",
        "MulticastListenerReportMessageVersion2MessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.messageType-57",
        "MulticastListenerReportMessageVersion2Code": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.code-58",
        "MulticastListenerReportMessageVersion2Checksum": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.checksum-59",
        "MulticastListenerReportMessageVersion2Reserved": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.reserved-60",
        "MulticastListenerReportMessageVersion2NumberOfMulticastAddressRecords": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.numberOfMulticastAddressRecords-61",
        "MulticastAddressRecordRecordType": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.recordType-62",
        "MulticastAddressRecordAuxiliaryDataLength": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.auxiliaryDataLength-63",
        "MulticastAddressRecordNumberOfSources": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.numberOfSources-64",
        "MulticastAddressRecordMulticastAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.multicastAddress-65",
        "MulticastSourcesMulticastSource": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.multicastSources.multicastSource-66",
        "MulticastAddressRecordDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.dataLengthoctets-67",
        "MulticastAddressRecordAuxiliaryData": "icmpv6.icmpv6Message.icmpv6MessegeType.multicastListenerReportMessageVersion2.multicastAddressRecords.multicastAddressRecord.auxiliaryData-68",
        "NdpRouterSolicitationMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.messageType-69",
        "NdpRouterSolicitationMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.code-70",
        "NdpRouterSolicitationMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.checksum-71",
        "NdpRouterSolicitationMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.reserved-72",
        "SourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-73",
        "SourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-74",
        "SourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-75",
        "TargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-76",
        "TargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.length-77",
        "TargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-78",
        "PrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.optionType-79",
        "PrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.length-80",
        "PrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.prefixLength-81",
        "FlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-82",
        "FlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-83",
        "FlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-84",
        "PrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.reserved-85",
        "PrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.validLifetime-86",
        "PrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.preferredLifetime-87",
        "TlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.reserved-88",
        "PrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.prefixInformationOption.prefix-89",
        "RedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.redirectedHeaderOption.optionType-90",
        "RedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.redirectedHeaderOption.optionLength-91",
        "RedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.redirectedHeaderOption.reserved-92",
        "TlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.redirectedHeaderOption.reserved-93",
        "RedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-94",
        "RedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.redirectedHeaderOption.data-95",
        "MaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-96",
        "MaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.length-97",
        "MaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-98",
        "MaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-99",
        "NdpRouterAdvertisementMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.messageType-100",
        "NdpRouterAdvertisementMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.code-101",
        "NdpRouterAdvertisementMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.checksum-102",
        "NdpRouterAdvertisementMessageCurrentHopLimit": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.currentHopLimit-103",
        "FlagsManagedAddressConfigurationMflag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.flags.managedAddressConfigurationMflag-104",
        "FlagsOtherStatefulConfigurationOflag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.flags.otherStatefulConfigurationOflag-105",
        "FlagsHomeAgentHflag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.flags.homeAgentHflag-106",
        "NdpRouterAdvertisementMessageDefaultRouterPrf": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.defaultRouterPrf-107",
        "NdpRouterAdvertisementMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.reserved-108",
        "NdpRouterAdvertisementMessageRouterLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.routerLifetime-109",
        "NdpRouterAdvertisementMessageReachableTime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.reachableTime-110",
        "NdpRouterAdvertisementMessageRetransmissionTimer": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.retransmissionTimer-111",
        "TlvoptionSourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-112",
        "TlvoptionSourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-113",
        "TlvoptionSourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-114",
        "TlvoptionTargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-115",
        "TlvoptionTargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.length-116",
        "TlvoptionTargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-117",
        "TlvoptionPrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.optionType-118",
        "TlvoptionPrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.length-119",
        "TlvoptionPrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.prefixLength-120",
        "PrefixinformationoptionFlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-121",
        "PrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-122",
        "PrefixinformationoptionFlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-123",
        "OptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.reserved-124",
        "TlvoptionPrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.validLifetime-125",
        "TlvoptionPrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.preferredLifetime-126",
        "NdprouteradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.reserved-127",
        "TlvoptionPrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.prefixInformationOption.prefix-128",
        "TlvoptionRedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.redirectedHeaderOption.optionType-129",
        "TlvoptionRedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.redirectedHeaderOption.optionLength-130",
        "OptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.redirectedHeaderOption.reserved-131",
        "NdprouteradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.redirectedHeaderOption.reserved-132",
        "TlvoptionRedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-133",
        "TlvoptionRedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.redirectedHeaderOption.data-134",
        "TlvoptionMaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-135",
        "TlvoptionMaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.length-136",
        "TlvoptionMaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-137",
        "TlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-138",
        "AdvertisementIntervalOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.advertisementIntervalOption.optionType-139",
        "AdvertisementIntervalOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.advertisementIntervalOption.length-140",
        "AdvertisementIntervalOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.advertisementIntervalOption.reserved-141",
        "AdvertisementIntervalOptionAdvertisementInterval": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.advertisementIntervalOption.advertisementInterval-142",
        "HomeAgentInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.homeAgentInformationOption.optionType-143",
        "HomeAgentInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.homeAgentInformationOption.length-144",
        "HomeAgentInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.homeAgentInformationOption.reserved-145",
        "HomeAgentInformationOptionHomeAgentPreference": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.homeAgentInformationOption.homeAgentPreference-146",
        "HomeAgentInformationOptionHomeAgentLifeTime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRouterAdvertisementMessage.options.tlvOption.homeAgentInformationOption.homeAgentLifeTime-147",
        "NdpNeighborSolicitationMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.messageType-148",
        "NdpNeighborSolicitationMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.code-149",
        "NdpNeighborSolicitationMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.checksum-150",
        "NdpNeighborSolicitationMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.reserved-151",
        "NdpNeighborSolicitationMessageTargetAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.targetAddress-152",
        "OptionsTlvoptionSourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-153",
        "OptionsTlvoptionSourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-154",
        "OptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-155",
        "OptionsTlvoptionTargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-156",
        "OptionsTlvoptionTargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.length-157",
        "OptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-158",
        "OptionsTlvoptionPrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.optionType-159",
        "OptionsTlvoptionPrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.length-160",
        "OptionsTlvoptionPrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.prefixLength-161",
        "TlvoptionPrefixinformationoptionFlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-162",
        "TlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-163",
        "TlvoptionPrefixinformationoptionFlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-164",
        "NdpneighborsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.reserved-165",
        "OptionsTlvoptionPrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.validLifetime-166",
        "OptionsTlvoptionPrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.preferredLifetime-167",
        "NdpneighborsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.reserved-168",
        "OptionsTlvoptionPrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.prefixInformationOption.prefix-169",
        "OptionsTlvoptionRedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.redirectedHeaderOption.optionType-170",
        "OptionsTlvoptionRedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.redirectedHeaderOption.optionLength-171",
        "NdpneighborsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.redirectedHeaderOption.reserved-172",
        "NdpneighborsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.redirectedHeaderOption.reserved-173",
        "OptionsTlvoptionRedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-174",
        "OptionsTlvoptionRedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.redirectedHeaderOption.data-175",
        "OptionsTlvoptionMaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-176",
        "OptionsTlvoptionMaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.length-177",
        "OptionsTlvoptionMaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-178",
        "OptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-179",
        "NdpNeighborAdvertisementMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.messageType-180",
        "NdpNeighborAdvertisementMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.code-181",
        "NdpNeighborAdvertisementMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.checksum-182",
        "FlagsRouterRflag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.flags.routerRflag-183",
        "FlagsNeighborSolicitationSflag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.flags.neighborSolicitationSflag-184",
        "FlagsOverrideExistingCacheEntryOflag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.flags.overrideExistingCacheEntryOflag-185",
        "NdpNeighborAdvertisementMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.reserved-186",
        "NdpNeighborAdvertisementMessageTargetAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.targetAddress-187",
        "NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-188",
        "NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-189",
        "NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-190",
        "NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-191",
        "NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.length-192",
        "NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-193",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.optionType-194",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.length-195",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.prefixLength-196",
        "OptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-197",
        "OptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-198",
        "OptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-199",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.reserved-200",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.validLifetime-201",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.preferredLifetime-202",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.reserved-203",
        "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.prefixInformationOption.prefix-204",
        "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.redirectedHeaderOption.optionType-205",
        "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.redirectedHeaderOption.optionLength-206",
        "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.redirectedHeaderOption.reserved-207",
        "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.redirectedHeaderOption.reserved-208",
        "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-209",
        "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.redirectedHeaderOption.data-210",
        "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-211",
        "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.length-212",
        "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-213",
        "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpNeighborAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-214",
        "NdpRedirectMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.messageType-215",
        "NdpRedirectMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.code-216",
        "NdpRedirectMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.checksum-217",
        "NdpRedirectMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.reserved-218",
        "NdpRedirectMessageTargetAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.targetAddress-219",
        "NdpRedirectMessageDestinationAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.destinationAddress-220",
        "NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-221",
        "NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-222",
        "NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-223",
        "NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-224",
        "NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.targetLinkLayerAddressOption.length-225",
        "NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-226",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.optionType-227",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.length-228",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.prefixLength-229",
        "NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-230",
        "NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-231",
        "NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-232",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.reserved-233",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.validLifetime-234",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.preferredLifetime-235",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.reserved-236",
        "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.prefixInformationOption.prefix-237",
        "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.redirectedHeaderOption.optionType-238",
        "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.redirectedHeaderOption.optionLength-239",
        "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.redirectedHeaderOption.reserved-240",
        "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.redirectedHeaderOption.reserved-241",
        "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-242",
        "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.redirectedHeaderOption.data-243",
        "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-244",
        "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.maximumTransmissionUnitOption.length-245",
        "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-246",
        "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.ndpRedirectMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-247",
        "MobileDHAADRequestMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADRequestMessage.messageType-248",
        "MobileDHAADRequestMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADRequestMessage.code-249",
        "MobileDHAADRequestMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADRequestMessage.checksum-250",
        "MobileDHAADRequestMessageIdentifier": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADRequestMessage.identifier-251",
        "MobileDHAADRequestMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADRequestMessage.reserved-252",
        "MobileDHAADReplyMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADReplyMessage.messageType-253",
        "MobileDHAADReplyMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADReplyMessage.code-254",
        "MobileDHAADReplyMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADReplyMessage.checksum-255",
        "MobileDHAADReplyMessageIdentifier": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADReplyMessage.identifier-256",
        "MobileDHAADReplyMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADReplyMessage.reserved-257",
        "HomeAgentAddressEntriesHomeAgentAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.mobileDHAADReplyMessage.homeAgentAddressEntries.homeAgentAddress-258",
        "MobilePrefixSolicitationMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.messageType-259",
        "MobilePrefixSolicitationMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.code-260",
        "MobilePrefixSolicitationMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.checksum-261",
        "MobilePrefixSolicitationMessageIdentifier": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.identifier-262",
        "MobilePrefixSolicitationMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.reserved-263",
        "MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-264",
        "MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-265",
        "MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-266",
        "MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-267",
        "MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.length-268",
        "MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-269",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.optionType-270",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.length-271",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.prefixLength-272",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-273",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-274",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-275",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.reserved-276",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.validLifetime-277",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.preferredLifetime-278",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.reserved-279",
        "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.prefixInformationOption.prefix-280",
        "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.redirectedHeaderOption.optionType-281",
        "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.redirectedHeaderOption.optionLength-282",
        "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.redirectedHeaderOption.reserved-283",
        "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.redirectedHeaderOption.reserved-284",
        "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-285",
        "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.redirectedHeaderOption.data-286",
        "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-287",
        "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.length-288",
        "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-289",
        "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixSolicitationMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-290",
        "MobilePrefixAdvertisementMessageMessageType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.messageType-291",
        "MobilePrefixAdvertisementMessageCode": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.code-292",
        "MobilePrefixAdvertisementMessageChecksum": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.checksum-293",
        "MobilePrefixAdvertisementMessageIdentifier": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.identifier-294",
        "MobilePrefixAdvertisementMessageMBit": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.mBit-295",
        "MobilePrefixAdvertisementMessageOBit": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.oBit-296",
        "MobilePrefixAdvertisementMessageReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.reserved-297",
        "MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.optionType-298",
        "MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.optionLength-299",
        "MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.sourceLinkLayerAddressOption.linkLayerAddress-300",
        "MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.optionType-301",
        "MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.length-302",
        "MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.targetLinkLayerAddressOption.linkLayerAddress-303",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.optionType-304",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.length-305",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefixLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.prefixLength-306",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.onLinkLFlag-307",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.autonomousAddressConfigurationAFlag-308",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.flags.routerAddressRFlag-309",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.reserved-310",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionValidLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.validLifetime-311",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.preferredLifetime-312",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.reserved-313",
        "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefix": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.prefixInformationOption.prefix-314",
        "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.redirectedHeaderOption.optionType-315",
        "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.redirectedHeaderOption.optionLength-316",
        "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.redirectedHeaderOption.reserved-317",
        "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.redirectedHeaderOption.reserved-318",
        "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.redirectedHeaderOption.dataLengthoctets-319",
        "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionData": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.redirectedHeaderOption.data-320",
        "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.optionType-321",
        "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.length-322",
        "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.reserved-323",
        "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit": "icmpv6.icmpv6Message.icmpv6MessegeType.mobilePrefixAdvertisementMessage.options.tlvOption.maximumTransmissionUnitOption.maximumTransmissionUnit-324",
    }

    def __init__(self, parent, list_op=False):
        super(Icmpv6, self).__init__(parent, list_op)

    @property
    def DestinationUnreachableMessageMesageType(self):
        """
        Display Name: Mesage type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DestinationUnreachableMessageMesageType"]
            ),
        )

    @property
    def DestinationUnreachableMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        Available enum values: No route to destination, 0, Communication with destination administratively prohibited, 1, Not assigned, 2, Address unreachable, 3, Port unreachable, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DestinationUnreachableMessageCode"]),
        )

    @property
    def DestinationUnreachableMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DestinationUnreachableMessageChecksum"]
            ),
        )

    @property
    def DestinationUnreachableMessageUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DestinationUnreachableMessageUnused"]
            ),
        )

    @property
    def PacketTooBigMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PacketTooBigMessageMessageType"]),
        )

    @property
    def PacketTooBigMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PacketTooBigMessageCode"])
        )

    @property
    def PacketTooBigMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PacketTooBigMessageChecksum"])
        )

    @property
    def PacketTooBigMessageMaximumTransmissionUnit(self):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PacketTooBigMessageMaximumTransmissionUnit"]
            ),
        )

    @property
    def TimeExceededMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TimeExceededMessageMessageType"]),
        )

    @property
    def TimeExceededMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        Available enum values: Hop limit exceeded in transit, 0, Fragment reassembly time exceeded, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeExceededMessageCode"])
        )

    @property
    def TimeExceededMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeExceededMessageChecksum"])
        )

    @property
    def TimeExceededMessageUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeExceededMessageUnused"])
        )

    @property
    def ParameterProblemMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ParameterProblemMessageMessageType"]
            ),
        )

    @property
    def ParameterProblemMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        Available enum values: Erroneous header field encountered, 0, Unrecognized Next Header type encountered, 1, Unrecognized IPv6 option encountered, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ParameterProblemMessageCode"])
        )

    @property
    def ParameterProblemMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ParameterProblemMessageChecksum"]),
        )

    @property
    def ParameterProblemMessagePointer(self):
        """
        Display Name: Pointer
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ParameterProblemMessagePointer"]),
        )

    @property
    def EchoRequestMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EchoRequestMessageMessageType"]),
        )

    @property
    def EchoRequestMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoRequestMessageCode"])
        )

    @property
    def EchoRequestMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoRequestMessageChecksum"])
        )

    @property
    def EchoRequestMessageIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoRequestMessageIdentifier"])
        )

    @property
    def EchoRequestMessageSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EchoRequestMessageSequenceNumber"]),
        )

    @property
    def EchoReplyMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 129
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyMessageMessageType"])
        )

    @property
    def EchoReplyMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyMessageCode"])
        )

    @property
    def EchoReplyMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyMessageChecksum"])
        )

    @property
    def EchoReplyMessageIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyMessageIdentifier"])
        )

    @property
    def EchoReplyMessageSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EchoReplyMessageSequenceNumber"]),
        )

    @property
    def MulticastListenerQueryMessageVersion1MessageType(self):
        """
        Display Name: Message type
        Default Value: 130
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion1MessageType"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion1Code(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion1Code"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion1Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion1Checksum"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion1MaximumResponseDelaymilliseconds(self):
        """
        Display Name: Maximum response delay (milliseconds)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerQueryMessageVersion1MaximumResponseDelaymilliseconds"
                ]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion1Reserved"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion1MulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: FF01::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerQueryMessageVersion1MulticastAddress"
                ]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion1MessageType(self):
        """
        Display Name: Message type
        Default Value: 131
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion1MessageType"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion1Code(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion1Code"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion1Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion1Checksum"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion1MaximumResponseDelaymilliseconds(self):
        """
        Display Name: Maximum response delay (milliseconds)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerReportMessageVersion1MaximumResponseDelaymilliseconds"
                ]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion1Reserved"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion1MulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: FF01::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerReportMessageVersion1MulticastAddress"
                ]
            ),
        )

    @property
    def MulticastListenerDoneMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 132
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerDoneMessageMessageType"]
            ),
        )

    @property
    def MulticastListenerDoneMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastListenerDoneMessageCode"]),
        )

    @property
    def MulticastListenerDoneMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerDoneMessageChecksum"]
            ),
        )

    @property
    def MulticastListenerDoneMessageMaximumResponseDelaymilliseconds(self):
        """
        Display Name: Maximum response delay (milliseconds)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerDoneMessageMaximumResponseDelaymilliseconds"
                ]
            ),
        )

    @property
    def MulticastListenerDoneMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerDoneMessageReserved"]
            ),
        )

    @property
    def MulticastListenerDoneMessageMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: FF01::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerDoneMessageMulticastAddress"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2MessageType(self):
        """
        Display Name: Message type
        Default Value: 130
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2MessageType"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2Code(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2Code"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2Checksum"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2MaximumResponseDelaymilliseconds(self):
        """
        Display Name: Maximum response delay (milliseconds)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerQueryMessageVersion2MaximumResponseDelaymilliseconds"
                ]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2Reserved"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2MulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: FF01::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerQueryMessageVersion2MulticastAddress"
                ]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2Reserved"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2SuppressRoutersideProcessingSFlag(self):
        """
        Display Name: Suppress router-side processing (S-flag)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerQueryMessageVersion2SuppressRoutersideProcessingSFlag"
                ]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2Qrv(self):
        """
        Display Name: Querier's Robustness Variable
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2Qrv"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2Qqic(self):
        """
        Display Name: Querier's Query Interval Code
        Default Value: 125
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerQueryMessageVersion2Qqic"]
            ),
        )

    @property
    def MulticastListenerQueryMessageVersion2NumberOfSources(self):
        """
        Display Name: Number of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerQueryMessageVersion2NumberOfSources"
                ]
            ),
        )

    @property
    def SourceAddressEntriesSourceAddress(self):
        """
        Display Name: Source address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SourceAddressEntriesSourceAddress"]),
        )

    @property
    def MulticastListenerReportMessageVersion2MessageType(self):
        """
        Display Name: Message type
        Default Value: 143
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion2MessageType"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion2Code(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion2Code"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion2Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion2Checksum"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastListenerReportMessageVersion2Reserved"]
            ),
        )

    @property
    def MulticastListenerReportMessageVersion2NumberOfMulticastAddressRecords(self):
        """
        Display Name: Number of multicast address records
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MulticastListenerReportMessageVersion2NumberOfMulticastAddressRecords"
                ]
            ),
        )

    @property
    def MulticastAddressRecordRecordType(self):
        """
        Display Name: Record type
        Default Value: 1
        Value Format: decimal
        Available enum values: MODE_IS_INCLUDE, 1, MODE_IS_EXCLUDE, 2, CHANGE_TO_INCLUDE_MODE, 3, CHANGE_TO_EXCLUDE_MODE, 4, ALLOW_NEW_SOURCES, 5, BLOCK_OLD_SOURCES, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastAddressRecordRecordType"]),
        )

    @property
    def MulticastAddressRecordAuxiliaryDataLength(self):
        """
        Display Name: Auxiliary data length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastAddressRecordAuxiliaryDataLength"]
            ),
        )

    @property
    def MulticastAddressRecordNumberOfSources(self):
        """
        Display Name: Number of sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastAddressRecordNumberOfSources"]
            ),
        )

    @property
    def MulticastAddressRecordMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: FF01::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastAddressRecordMulticastAddress"]
            ),
        )

    @property
    def MulticastSourcesMulticastSource(self):
        """
        Display Name: Multicast source
        Default Value: FF01::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastSourcesMulticastSource"]),
        )

    @property
    def MulticastAddressRecordDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastAddressRecordDataLengthoctets"]
            ),
        )

    @property
    def MulticastAddressRecordAuxiliaryData(self):
        """
        Display Name: Auxiliary data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastAddressRecordAuxiliaryData"]
            ),
        )

    @property
    def NdpRouterSolicitationMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 133
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterSolicitationMessageMessageType"]
            ),
        )

    @property
    def NdpRouterSolicitationMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NdpRouterSolicitationMessageCode"]),
        )

    @property
    def NdpRouterSolicitationMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterSolicitationMessageChecksum"]
            ),
        )

    @property
    def NdpRouterSolicitationMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterSolicitationMessageReserved"]
            ),
        )

    @property
    def SourceLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SourceLinkLayerAddressOptionOptionType"]
            ),
        )

    @property
    def SourceLinkLayerAddressOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SourceLinkLayerAddressOptionOptionLength"]
            ),
        )

    @property
    def SourceLinkLayerAddressOptionLinkLayerAddress(self):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SourceLinkLayerAddressOptionLinkLayerAddress"]
            ),
        )

    @property
    def TargetLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TargetLinkLayerAddressOptionOptionType"]
            ),
        )

    @property
    def TargetLinkLayerAddressOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TargetLinkLayerAddressOptionLength"]
            ),
        )

    @property
    def TargetLinkLayerAddressOptionLinkLayerAddress(self):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TargetLinkLayerAddressOptionLinkLayerAddress"]
            ),
        )

    @property
    def PrefixInformationOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrefixInformationOptionOptionType"]),
        )

    @property
    def PrefixInformationOptionLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrefixInformationOptionLength"]),
        )

    @property
    def PrefixInformationOptionPrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PrefixInformationOptionPrefixLength"]
            ),
        )

    @property
    def FlagsOnLinkLFlag(self):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsOnLinkLFlag"])
        )

    @property
    def FlagsAutonomousAddressConfigurationAFlag(self):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FlagsAutonomousAddressConfigurationAFlag"]
            ),
        )

    @property
    def FlagsRouterAddressRFlag(self):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsRouterAddressRFlag"])
        )

    @property
    def PrefixInformationOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrefixInformationOptionReserved"]),
        )

    @property
    def PrefixInformationOptionValidLifetime(self):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PrefixInformationOptionValidLifetime"]
            ),
        )

    @property
    def PrefixInformationOptionPreferredLifetime(self):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PrefixInformationOptionPreferredLifetime"]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionReserved"]
            ),
        )

    @property
    def PrefixInformationOptionPrefix(self):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrefixInformationOptionPrefix"]),
        )

    @property
    def RedirectedHeaderOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RedirectedHeaderOptionOptionType"]),
        )

    @property
    def RedirectedHeaderOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RedirectedHeaderOptionOptionLength"]
            ),
        )

    @property
    def RedirectedHeaderOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RedirectedHeaderOptionReserved"]),
        )

    @property
    def TlvoptionRedirectedHeaderOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionRedirectedHeaderOptionReserved"]
            ),
        )

    @property
    def RedirectedHeaderOptionDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RedirectedHeaderOptionDataLengthoctets"]
            ),
        )

    @property
    def RedirectedHeaderOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RedirectedHeaderOptionData"])
        )

    @property
    def MaximumTransmissionUnitOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaximumTransmissionUnitOptionOptionType"]
            ),
        )

    @property
    def MaximumTransmissionUnitOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaximumTransmissionUnitOptionLength"]
            ),
        )

    @property
    def MaximumTransmissionUnitOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaximumTransmissionUnitOptionReserved"]
            ),
        )

    @property
    def MaximumTransmissionUnitOptionMaximumTransmissionUnit(self):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 134
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageMessageType"]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NdpRouterAdvertisementMessageCode"]),
        )

    @property
    def NdpRouterAdvertisementMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageChecksum"]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageCurrentHopLimit(self):
        """
        Display Name: Current hop limit
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageCurrentHopLimit"]
            ),
        )

    @property
    def FlagsManagedAddressConfigurationMflag(self):
        """
        Display Name: Managed address configuration (M-flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FlagsManagedAddressConfigurationMflag"]
            ),
        )

    @property
    def FlagsOtherStatefulConfigurationOflag(self):
        """
        Display Name: Other stateful configuration (O-flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FlagsOtherStatefulConfigurationOflag"]
            ),
        )

    @property
    def FlagsHomeAgentHflag(self):
        """
        Display Name: Home Agent (H-flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsHomeAgentHflag"])
        )

    @property
    def NdpRouterAdvertisementMessageDefaultRouterPrf(self):
        """
        Display Name: Default Router Preference
        Default Value: 0
        Value Format: decimal
        Available enum values: High, 1, Medium (default), 0, Low, 3, Reserved, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageDefaultRouterPrf"]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageReserved"]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageRouterLifetime(self):
        """
        Display Name: Router lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageRouterLifetime"]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageReachableTime(self):
        """
        Display Name: Reachable time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageReachableTime"]
            ),
        )

    @property
    def NdpRouterAdvertisementMessageRetransmissionTimer(self):
        """
        Display Name: Retransmission timer
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRouterAdvertisementMessageRetransmissionTimer"]
            ),
        )

    @property
    def TlvoptionSourceLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionSourceLinkLayerAddressOptionOptionType"]
            ),
        )

    @property
    def TlvoptionSourceLinkLayerAddressOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionSourceLinkLayerAddressOptionOptionLength"]
            ),
        )

    @property
    def TlvoptionSourceLinkLayerAddressOptionLinkLayerAddress(self):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvoptionSourceLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def TlvoptionTargetLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionTargetLinkLayerAddressOptionOptionType"]
            ),
        )

    @property
    def TlvoptionTargetLinkLayerAddressOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionTargetLinkLayerAddressOptionLength"]
            ),
        )

    @property
    def TlvoptionTargetLinkLayerAddressOptionLinkLayerAddress(self):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvoptionTargetLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionOptionType"]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionLength"]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionPrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionPrefixLength"]
            ),
        )

    @property
    def PrefixinformationoptionFlagsOnLinkLFlag(self):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PrefixinformationoptionFlagsOnLinkLFlag"]
            ),
        )

    @property
    def PrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag(self):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "PrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag"
                ]
            ),
        )

    @property
    def PrefixinformationoptionFlagsRouterAddressRFlag(self):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PrefixinformationoptionFlagsRouterAddressRFlag"]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionPrefixInformationOptionReserved"]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionValidLifetime(self):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionValidLifetime"]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionPreferredLifetime(self):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionPreferredLifetime"]
            ),
        )

    @property
    def NdprouteradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdprouteradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def TlvoptionPrefixInformationOptionPrefix(self):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixInformationOptionPrefix"]
            ),
        )

    @property
    def TlvoptionRedirectedHeaderOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionRedirectedHeaderOptionOptionType"]
            ),
        )

    @property
    def TlvoptionRedirectedHeaderOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionRedirectedHeaderOptionOptionLength"]
            ),
        )

    @property
    def OptionsTlvoptionRedirectedHeaderOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionRedirectedHeaderOptionReserved"]
            ),
        )

    @property
    def NdprouteradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdprouteradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def TlvoptionRedirectedHeaderOptionDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionRedirectedHeaderOptionDataLengthoctets"]
            ),
        )

    @property
    def TlvoptionRedirectedHeaderOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionRedirectedHeaderOptionData"]
            ),
        )

    @property
    def TlvoptionMaximumTransmissionUnitOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionMaximumTransmissionUnitOptionOptionType"]
            ),
        )

    @property
    def TlvoptionMaximumTransmissionUnitOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionMaximumTransmissionUnitOptionLength"]
            ),
        )

    @property
    def TlvoptionMaximumTransmissionUnitOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionMaximumTransmissionUnitOptionReserved"]
            ),
        )

    @property
    def TlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit(self):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    @property
    def AdvertisementIntervalOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AdvertisementIntervalOptionOptionType"]
            ),
        )

    @property
    def AdvertisementIntervalOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AdvertisementIntervalOptionLength"]),
        )

    @property
    def AdvertisementIntervalOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AdvertisementIntervalOptionReserved"]
            ),
        )

    @property
    def AdvertisementIntervalOptionAdvertisementInterval(self):
        """
        Display Name: Advertisement Interval
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AdvertisementIntervalOptionAdvertisementInterval"]
            ),
        )

    @property
    def HomeAgentInformationOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HomeAgentInformationOptionOptionType"]
            ),
        )

    @property
    def HomeAgentInformationOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HomeAgentInformationOptionLength"]),
        )

    @property
    def HomeAgentInformationOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HomeAgentInformationOptionReserved"]
            ),
        )

    @property
    def HomeAgentInformationOptionHomeAgentPreference(self):
        """
        Display Name: Home Agent Preference
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HomeAgentInformationOptionHomeAgentPreference"]
            ),
        )

    @property
    def HomeAgentInformationOptionHomeAgentLifeTime(self):
        """
        Display Name: Home Agent LifeTime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HomeAgentInformationOptionHomeAgentLifeTime"]
            ),
        )

    @property
    def NdpNeighborSolicitationMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 135
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborSolicitationMessageMessageType"]
            ),
        )

    @property
    def NdpNeighborSolicitationMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborSolicitationMessageCode"]
            ),
        )

    @property
    def NdpNeighborSolicitationMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborSolicitationMessageChecksum"]
            ),
        )

    @property
    def NdpNeighborSolicitationMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborSolicitationMessageReserved"]
            ),
        )

    @property
    def NdpNeighborSolicitationMessageTargetAddress(self):
        """
        Display Name: Target address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborSolicitationMessageTargetAddress"]
            ),
        )

    @property
    def OptionsTlvoptionSourceLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionSourceLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def OptionsTlvoptionSourceLinkLayerAddressOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionSourceLinkLayerAddressOptionOptionLength"
                ]
            ),
        )

    @property
    def OptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress(self):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def OptionsTlvoptionTargetLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionTargetLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def OptionsTlvoptionTargetLinkLayerAddressOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionTargetLinkLayerAddressOptionLength"]
            ),
        )

    @property
    def OptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress(self):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionPrefixInformationOptionOptionType"]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionPrefixInformationOptionLength"]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionPrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionPrefixInformationOptionPrefixLength"]
            ),
        )

    @property
    def TlvoptionPrefixinformationoptionFlagsOnLinkLFlag(self):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvoptionPrefixinformationoptionFlagsOnLinkLFlag"]
            ),
        )

    @property
    def TlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag(self):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag"
                ]
            ),
        )

    @property
    def TlvoptionPrefixinformationoptionFlagsRouterAddressRFlag(self):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "TlvoptionPrefixinformationoptionFlagsRouterAddressRFlag"
                ]
            ),
        )

    @property
    def NdpneighborsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
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
                    "NdpneighborsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionValidLifetime(self):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionPrefixInformationOptionValidLifetime"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionPreferredLifetime(self):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionPrefixInformationOptionPreferredLifetime"
                ]
            ),
        )

    @property
    def NdpneighborsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighborsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixInformationOptionPrefix(self):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionPrefixInformationOptionPrefix"]
            ),
        )

    @property
    def OptionsTlvoptionRedirectedHeaderOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionRedirectedHeaderOptionOptionType"]
            ),
        )

    @property
    def OptionsTlvoptionRedirectedHeaderOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionRedirectedHeaderOptionOptionLength"]
            ),
        )

    @property
    def NdpneighborsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighborsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def NdpneighborsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighborsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def OptionsTlvoptionRedirectedHeaderOptionDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionRedirectedHeaderOptionDataLengthoctets"
                ]
            ),
        )

    @property
    def OptionsTlvoptionRedirectedHeaderOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionRedirectedHeaderOptionData"]
            ),
        )

    @property
    def OptionsTlvoptionMaximumTransmissionUnitOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionMaximumTransmissionUnitOptionOptionType"
                ]
            ),
        )

    @property
    def OptionsTlvoptionMaximumTransmissionUnitOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionsTlvoptionMaximumTransmissionUnitOptionLength"]
            ),
        )

    @property
    def OptionsTlvoptionMaximumTransmissionUnitOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionMaximumTransmissionUnitOptionReserved"
                ]
            ),
        )

    @property
    def OptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit(self):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    @property
    def NdpNeighborAdvertisementMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 136
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborAdvertisementMessageMessageType"]
            ),
        )

    @property
    def NdpNeighborAdvertisementMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborAdvertisementMessageCode"]
            ),
        )

    @property
    def NdpNeighborAdvertisementMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborAdvertisementMessageChecksum"]
            ),
        )

    @property
    def FlagsRouterRflag(self):
        """
        Display Name: Router (R-flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsRouterRflag"])
        )

    @property
    def FlagsNeighborSolicitationSflag(self):
        """
        Display Name: Neighbor solicitation (S-flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FlagsNeighborSolicitationSflag"]),
        )

    @property
    def FlagsOverrideExistingCacheEntryOflag(self):
        """
        Display Name: Override existing cache entry (O-flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FlagsOverrideExistingCacheEntryOflag"]
            ),
        )

    @property
    def NdpNeighborAdvertisementMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborAdvertisementMessageReserved"]
            ),
        )

    @property
    def NdpNeighborAdvertisementMessageTargetAddress(self):
        """
        Display Name: Target address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpNeighborAdvertisementMessageTargetAddress"]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionOptionType"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionLength"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefixLength(
        self,
    ):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefixLength"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag(self):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag(
        self,
    ):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag"
                ]
            ),
        )

    @property
    def OptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag(self):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
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
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionValidLifetime(
        self,
    ):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionValidLifetime"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime(
        self,
    ):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefix(
        self,
    ):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefix"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionType"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets(
        self,
    ):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionRedirectedHeaderOptionData"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved"
                ]
            ),
        )

    @property
    def NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit(
        self,
    ):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpneighboradvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    @property
    def NdpRedirectMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 137
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NdpRedirectMessageMessageType"]),
        )

    @property
    def NdpRedirectMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NdpRedirectMessageCode"])
        )

    @property
    def NdpRedirectMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NdpRedirectMessageChecksum"])
        )

    @property
    def NdpRedirectMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NdpRedirectMessageReserved"])
        )

    @property
    def NdpRedirectMessageTargetAddress(self):
        """
        Display Name: Target address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NdpRedirectMessageTargetAddress"]),
        )

    @property
    def NdpRedirectMessageDestinationAddress(self):
        """
        Display Name: Destination address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NdpRedirectMessageDestinationAddress"]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionOptionType"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionLength"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPrefixLength"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag(self):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag(
        self,
    ):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag(
        self,
    ):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionReserved(self):
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
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionValidLifetime(self):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionValidLifetime"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime(
        self,
    ):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPrefix(self):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionPrefixInformationOptionPrefix"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionOptionType"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength(self):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionRedirectedHeaderOptionData"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType(self):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved"
                ]
            ),
        )

    @property
    def NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit(
        self,
    ):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "NdpredirectmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    @property
    def MobileDHAADRequestMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 144
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileDHAADRequestMessageMessageType"]
            ),
        )

    @property
    def MobileDHAADRequestMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileDHAADRequestMessageCode"]),
        )

    @property
    def MobileDHAADRequestMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileDHAADRequestMessageChecksum"]),
        )

    @property
    def MobileDHAADRequestMessageIdentifier(self):
        """
        Display Name: identifier
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileDHAADRequestMessageIdentifier"]
            ),
        )

    @property
    def MobileDHAADRequestMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileDHAADRequestMessageReserved"]),
        )

    @property
    def MobileDHAADReplyMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 145
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileDHAADReplyMessageMessageType"]
            ),
        )

    @property
    def MobileDHAADReplyMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileDHAADReplyMessageCode"])
        )

    @property
    def MobileDHAADReplyMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileDHAADReplyMessageChecksum"]),
        )

    @property
    def MobileDHAADReplyMessageIdentifier(self):
        """
        Display Name: identifier
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileDHAADReplyMessageIdentifier"]),
        )

    @property
    def MobileDHAADReplyMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileDHAADReplyMessageReserved"]),
        )

    @property
    def HomeAgentAddressEntriesHomeAgentAddress(self):
        """
        Display Name: Home Agent Address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HomeAgentAddressEntriesHomeAgentAddress"]
            ),
        )

    @property
    def MobilePrefixSolicitationMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 146
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixSolicitationMessageMessageType"]
            ),
        )

    @property
    def MobilePrefixSolicitationMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixSolicitationMessageCode"]
            ),
        )

    @property
    def MobilePrefixSolicitationMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixSolicitationMessageChecksum"]
            ),
        )

    @property
    def MobilePrefixSolicitationMessageIdentifier(self):
        """
        Display Name: identifier
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixSolicitationMessageIdentifier"]
            ),
        )

    @property
    def MobilePrefixSolicitationMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixSolicitationMessageReserved"]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPrefixLength(
        self,
    ):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPrefixLength"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag(
        self,
    ):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag(
        self,
    ):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag(
        self,
    ):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
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
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionValidLifetime(
        self,
    ):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionValidLifetime"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime(
        self,
    ):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPrefix(
        self,
    ):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionPrefixInformationOptionPrefix"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets(
        self,
    ):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionRedirectedHeaderOptionData"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit(
        self,
    ):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixsolicitationmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 147
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageMessageType"]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageCode"]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageChecksum"]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageIdentifier(self):
        """
        Display Name: identifier
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageIdentifier"]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageMBit(self):
        """
        Display Name: M Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageMBit"]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageOBit(self):
        """
        Display Name: O Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageOBit"]
            ),
        )

    @property
    def MobilePrefixAdvertisementMessageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobilePrefixAdvertisementMessageReserved"]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionSourceLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress(
        self,
    ):
        """
        Display Name: Link Layer Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionTargetLinkLayerAddressOptionLinkLayerAddress"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefixLength(
        self,
    ):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefixLength"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag(
        self,
    ):
        """
        Display Name: On-Link (L flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsOnLinkLFlag"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag(
        self,
    ):
        """
        Display Name: Autonomous Address Configuration (A Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsAutonomousAddressConfigurationAFlag"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag(
        self,
    ):
        """
        Display Name: Router Address (R Flag)
        Default Value: 0
        Value Format: decimal
        Available enum values: Clear, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixinformationoptionFlagsRouterAddressRFlag"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
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
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionValidLifetime(
        self,
    ):
        """
        Display Name: Valid lifetime
        Default Value: 0xffffffff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionValidLifetime"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime(
        self,
    ):
        """
        Display Name: Preferred lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPreferredLifetime"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefix(
        self,
    ):
        """
        Display Name: Prefix
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionPrefixInformationOptionPrefix"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength(
        self,
    ):
        """
        Display Name: Option length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets(
        self,
    ):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionDataLengthoctets"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionData(
        self,
    ):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionRedirectedHeaderOptionData"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType(
        self,
    ):
        """
        Display Name: Option Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionOptionType"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength(
        self,
    ):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionLength"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionReserved"
                ]
            ),
        )

    @property
    def MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit(
        self,
    ):
        """
        Display Name: Maximum Transmission Unit
        Default Value: 1500
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MobileprefixadvertisementmessageOptionsTlvoptionMaximumTransmissionUnitOptionMaximumTransmissionUnit"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
