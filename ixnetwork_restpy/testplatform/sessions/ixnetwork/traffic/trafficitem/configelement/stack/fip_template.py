from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Fip(Base):
    __slots__ = ()
    _SDM_NAME = "fip"
    _SDM_ATT_MAP = {
        "Version": "fip.header.version-1",
        "Reserved": "fip.header.reserved-2",
        "CodeDiscovery": "fip.header.operation.code.discovery-3",
        "CodeVirtualLinkInstantiation": "fip.header.operation.code.virtualLinkInstantiation-4",
        "CodeKeepaliveVirtualLink": "fip.header.operation.code.keepaliveVirtualLink-5",
        "CodeVlanDiscovery": "fip.header.operation.code.vlanDiscovery-6",
        "CodeVendorSpecific": "fip.header.operation.code.vendorSpecific-7",
        "OperationReserved1": "fip.header.operation.reserved1-8",
        "SubcodeSubcode01h": "fip.header.operation.subcode.subcode01h-9",
        "SubcodeSubcode02h": "fip.header.operation.subcode.subcode02h-10",
        "SubcodeVendorSpecificSubcode": "fip.header.operation.subcode.vendorSpecificSubcode-11",
        "SubcodeSubcodeCustom": "fip.header.operation.subcode.subcodeCustom-12",
        "OperationDescriptorListLength": "fip.header.operation.descriptorListLength-13",
        "OperationFipFP": "fip.header.operation.fipFP-14",
        "OperationFipSP": "fip.header.operation.fipSP-15",
        "OperationReserved2": "fip.header.operation.reserved2-16",
        "OperationABit": "fip.header.operation.aBit-17",
        "OperationSBit": "fip.header.operation.sBit-18",
        "OperationFBit": "fip.header.operation.fBit-19",
        "PriorityDescriptorType": "fip.header.descriptors.descriptor.priorityDescriptor.type-20",
        "PriorityDescriptorLength": "fip.header.descriptors.descriptor.priorityDescriptor.length-21",
        "PriorityDescriptorReserved": "fip.header.descriptors.descriptor.priorityDescriptor.reserved-22",
        "PriorityDescriptorValue": "fip.header.descriptors.descriptor.priorityDescriptor.value-23",
        "MacAddressDescriptorType": "fip.header.descriptors.descriptor.macAddressDescriptor.type-24",
        "MacAddressDescriptorLength": "fip.header.descriptors.descriptor.macAddressDescriptor.length-25",
        "MacAddressDescriptorValue": "fip.header.descriptors.descriptor.macAddressDescriptor.value-26",
        "FcMapDescriptorType": "fip.header.descriptors.descriptor.fcMapDescriptor.type-27",
        "FcMapDescriptorLength": "fip.header.descriptors.descriptor.fcMapDescriptor.length-28",
        "FcMapDescriptorReserved": "fip.header.descriptors.descriptor.fcMapDescriptor.reserved-29",
        "FcMapDescriptorValue": "fip.header.descriptors.descriptor.fcMapDescriptor.value-30",
        "NameIdentifierDescriptorType": "fip.header.descriptors.descriptor.nameIdentifierDescriptor.type-31",
        "NameIdentifierDescriptorLength": "fip.header.descriptors.descriptor.nameIdentifierDescriptor.length-32",
        "NameIdentifierDescriptorReserved": "fip.header.descriptors.descriptor.nameIdentifierDescriptor.reserved-33",
        "NameIdentifierDescriptorValue": "fip.header.descriptors.descriptor.nameIdentifierDescriptor.value-34",
        "FabricDescriptorType": "fip.header.descriptors.descriptor.fabricDescriptor.type-35",
        "FabricDescriptorLength": "fip.header.descriptors.descriptor.fabricDescriptor.length-36",
        "FabricDescriptorVfID": "fip.header.descriptors.descriptor.fabricDescriptor.vfID-37",
        "FabricDescriptorReserved": "fip.header.descriptors.descriptor.fabricDescriptor.reserved-38",
        "FabricDescriptorFcMap": "fip.header.descriptors.descriptor.fabricDescriptor.fcMap-39",
        "FabricDescriptorValue": "fip.header.descriptors.descriptor.fabricDescriptor.value-40",
        "MaxFcoeSizeDescriptorType": "fip.header.descriptors.descriptor.maxFcoeSizeDescriptor.type-41",
        "MaxFcoeSizeDescriptorLength": "fip.header.descriptors.descriptor.maxFcoeSizeDescriptor.length-42",
        "MaxFcoeSizeDescriptorValue": "fip.header.descriptors.descriptor.maxFcoeSizeDescriptor.value-43",
        "FlogiDescriptorType": "fip.header.descriptors.descriptor.flogiDescriptor.type-44",
        "FlogiDescriptorLength": "fip.header.descriptors.descriptor.flogiDescriptor.length-45",
        "FlogiDescriptorReserved": "fip.header.descriptors.descriptor.flogiDescriptor.reserved-46",
        "DeviceDataFramesDeviceDataInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.deviceDataFrames.deviceDataInfo-47",
        "RCTLReserved": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.reserved-48",
        "ExtendedLinkServicesInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.extendedLinkServices.info-49",
        "Fc4LinkDataInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.fc4LinkData.info-50",
        "VideoDataInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.videoData.info-51",
        "ExtendedHeaderInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.extendedHeader.info-52",
        "BasicLinkServicesInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.basicLinkServices.info-53",
        "LinkControlFramesInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.linkControlFrames.info-54",
        "ExtendedRoutingInfo": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rCTL.extendedRouting.info-55",
        "FibreChannelDID": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.dID-56",
        "FibreChannelCsCTLPriority": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.csCTLPriority-57",
        "FibreChannelSID": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.sID-58",
        "FibreChannelType": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.type-59",
        "FCTLCustom": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.custom-60",
        "FCTLExchangeContext": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.exchangeContext-61",
        "FCTLSequenceContext": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.sequenceContext-62",
        "FCTLFirstSequence": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.firstSequence-63",
        "FCTLLastSequence": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.lastSequence-64",
        "FCTLEndSequence": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.endSequence-65",
        "FCTLEndConnection": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.endConnection-66",
        "FCTLCsCTLPriority": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.csCTLPriority-67",
        "FCTLSequenceInitiative": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.sequenceInitiative-68",
        "FCTLFcXIDReassigned": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.fcXIDReassigned-69",
        "FCTLFcInvalidateXID": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.fcInvalidateXID-70",
        "FCTLAckForm": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.ackForm-71",
        "FCTLFcDataCompression": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.fcDataCompression-72",
        "FCTLFcDataEncryption": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.fcDataEncryption-73",
        "FCTLRetransmittedSequence": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.retransmittedSequence-74",
        "FCTLUnidirectionalTransmit": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.unidirectionalTransmit-75",
        "FCTLContinueSeqCondition": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.continueSeqCondition-76",
        "FCTLAbortSeqCondition": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.abortSeqCondition-77",
        "FCTLRelativeOffsetPresent": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.relativeOffsetPresent-78",
        "FCTLExchangeReassembly": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.exchangeReassembly-79",
        "FCTLFillBytes": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.fCTL.fCTL.fillBytes-80",
        "FibreChannelSeqID": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.seqID-81",
        "FibreChannelDfCTL": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.dfCTL-82",
        "FibreChannelSeqCNT": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.seqCNT-83",
        "FibreChannelOxID": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.oxID-84",
        "FibreChannelRxID": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.rxID-85",
        "FibreChannelParameter": "fip.header.descriptors.descriptor.flogiDescriptor.fibreChannel.parameter-86",
        "CommandCodeFlogi": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commandCode.flogi-87",
        "CommandCodeFdisc": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commandCode.fdisc-88",
        "CommandCodeCustom": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commandCode.custom-89",
        "RequestReserved": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.reserved-90",
        "CommonServiceParametersFcPHVersion": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.fcPHVersion-91",
        "CommonServiceParametersBufferToBufferCredit": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.bufferToBufferCredit-92",
        "CommonServiceParametersCommonFeatures": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.commonFeatures-93",
        "CommonServiceParametersBbSCNumber": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.bbSCNumber-94",
        "CommonServiceParametersBufferToBufferReceiveDataFieldSize": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.bufferToBufferReceiveDataFieldSize-95",
        "CommonServiceParametersRATOV": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.rATOV-96",
        "CommonServiceParametersEDTOV": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.eDTOV-97",
        "CommonServiceParametersNPortPortName": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.nPortPortName-98",
        "CommonServiceParametersFabricNodeName": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.commonServiceParameters.fabricNodeName-99",
        "RequestClass1SvcParameters": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class1SvcParameters-100",
        "RequestClass2SvcParameters": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class2SvcParameters-101",
        "Class3SvcParametersServiceOptions": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.serviceOptions-102",
        "Class3SvcParametersInitiatorControl": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.initiatorControl-103",
        "Class3SvcParametersRecipientControl": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.recipientControl-104",
        "Class3SvcParametersReceiveSize": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.receiveSize-105",
        "Class3SvcParametersTotalConcurrentSequence": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.totalConcurrentSequence-106",
        "Class3SvcParametersEndToEndCredit": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.endToEndCredit-107",
        "Class3SvcParametersOpenSeqPerExchange": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.openSeqPerExchange-108",
        "Class3SvcParametersCrTOV": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class3SvcParameters.crTOV-109",
        "RequestClass4SvcParameters": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.class4SvcParameters-110",
        "RequestVendorVersion": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.request.vendorVersion-111",
        "CommandCodeLsACC": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.acceptReject.commandCode.lsACC-112",
        "CommandCodeLsRJT": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.acceptReject.commandCode.lsRJT-113",
        "AcceptrejectCommandCodeCustom": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.acceptReject.commandCode.custom-114",
        "AcceptRejectReserved": "fip.header.descriptors.descriptor.flogiDescriptor.fcELS.acceptReject.reserved-115",
        "NpivFDISCDescriptorType": "fip.header.descriptors.descriptor.npivFDISCDescriptor.type-116",
        "NpivFDISCDescriptorLength": "fip.header.descriptors.descriptor.npivFDISCDescriptor.length-117",
        "NpivFDISCDescriptorReserved": "fip.header.descriptors.descriptor.npivFDISCDescriptor.reserved-118",
        "DeviceDataFramesInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.deviceDataFrames.info-119",
        "FibrechannelRCTLReserved": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.reserved-120",
        "RctlExtendedLinkServicesInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.extendedLinkServices.info-121",
        "RctlFc4LinkDataInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.fc4LinkData.info-122",
        "RctlVideoDataInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.videoData.info-123",
        "RctlExtendedHeaderInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.extendedHeader.info-124",
        "RctlBasicLinkServicesInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.basicLinkServices.info-125",
        "RctlLinkControlFramesInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.linkControlFrames.info-126",
        "RctlExtendedRoutingInfo": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rCTL.extendedRouting.info-127",
        "NpivfdiscdescriptorFibreChannelDID": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.dID-128",
        "NpivfdiscdescriptorFibreChannelCsCTLPriority": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.csCTLPriority-129",
        "NpivfdiscdescriptorFibreChannelSID": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.sID-130",
        "NpivfdiscdescriptorFibreChannelType": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.type-131",
        "FibrechannelFCTLCustom": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.custom-132",
        "FctlFCTLExchangeContext": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.exchangeContext-133",
        "FctlFCTLSequenceContext": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.sequenceContext-134",
        "FctlFCTLFirstSequence": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.firstSequence-135",
        "FctlFCTLLastSequence": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.lastSequence-136",
        "FctlFCTLEndSequence": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.endSequence-137",
        "FctlFCTLEndConnection": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.endConnection-138",
        "FctlFCTLCsCTLPriority": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.csCTLPriority-139",
        "FctlFCTLSequenceInitiative": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.sequenceInitiative-140",
        "FctlFCTLFcXIDReassigned": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.fcXIDReassigned-141",
        "FctlFCTLFcInvalidateXID": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.fcInvalidateXID-142",
        "FctlFCTLAckForm": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.ackForm-143",
        "FctlFCTLFcDataCompression": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.fcDataCompression-144",
        "FctlFCTLFcDataEncryption": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.fcDataEncryption-145",
        "FctlFCTLRetransmittedSequence": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.retransmittedSequence-146",
        "FctlFCTLUnidirectionalTransmit": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.unidirectionalTransmit-147",
        "FctlFCTLContinueSeqCondition": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.continueSeqCondition-148",
        "FctlFCTLAbortSeqCondition": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.abortSeqCondition-149",
        "FctlFCTLRelativeOffsetPresent": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.relativeOffsetPresent-150",
        "FctlFCTLExchangeReassembly": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.exchangeReassembly-151",
        "FctlFCTLFillBytes": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.fCTL.fCTL.fillBytes-152",
        "NpivfdiscdescriptorFibreChannelSeqID": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.seqID-153",
        "NpivfdiscdescriptorFibreChannelDfCTL": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.dfCTL-154",
        "NpivfdiscdescriptorFibreChannelSeqCNT": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.seqCNT-155",
        "NpivfdiscdescriptorFibreChannelOxID": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.oxID-156",
        "NpivfdiscdescriptorFibreChannelRxID": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.rxID-157",
        "NpivfdiscdescriptorFibreChannelParameter": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fibreChannel.parameter-158",
        "FipfdiscdescriptorfcelsrequestCommandCodeFlogi": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commandCode.flogi-159",
        "FipfdiscdescriptorfcelsrequestCommandCodeFdisc": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commandCode.fdisc-160",
        "FipfdiscdescriptorfcelsrequestCommandCodeCustom": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commandCode.custom-161",
        "FipFdiscDescriptorFcElsRequestReserved": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.reserved-162",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersFcPHVersion": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.fcPHVersion-163",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersBufferToBufferCredit": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.bufferToBufferCredit-164",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersCommonFeatures": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.commonFeatures-165",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersBbSCNumber": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.bbSCNumber-166",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersBufferToBufferReceiveDataFieldSize": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.bufferToBufferReceiveDataFieldSize-167",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersRATOV": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.rATOV-168",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersEDTOV": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.eDTOV-169",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersNPortPortName": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.nPortPortName-170",
        "FipfdiscdescriptorfcelsrequestCommonServiceParametersFabricNodeName": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.commonServiceParameters.fabricNodeName-171",
        "FipFdiscDescriptorFcElsRequestClass1SvcParameters": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class1SvcParameters-172",
        "FipFdiscDescriptorFcElsRequestClass2SvcParameters": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class2SvcParameters-173",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersServiceOptions": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.serviceOptions-174",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersInitiatorControl": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.initiatorControl-175",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersRecipientControl": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.recipientControl-176",
        "Class3SvcParametersClassReceiveSize": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.classReceiveSize-177",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersTotalConcurrentSequence": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.totalConcurrentSequence-178",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersEndToEndCredit": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.endToEndCredit-179",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersOpenSeqPerExchange": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.openSeqPerExchange-180",
        "FipfdiscdescriptorfcelsrequestClass3SvcParametersCrTOV": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class3SvcParameters.crTOV-181",
        "FipFdiscDescriptorFcElsRequestClass4SvcParameters": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.class4SvcParameters-182",
        "FipFdiscDescriptorFcElsRequestVendorVersion": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.fipFdiscDescriptorFcElsRequest.vendorVersion-183",
        "AcceptrejectCommandCodeLsACC": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.acceptReject.commandCode.lsACC-184",
        "AcceptrejectCommandCodeLsRJT": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.acceptReject.commandCode.lsRJT-185",
        "FipfdiscdescriptorfcelsAcceptrejectCommandCodeCustom": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.acceptReject.commandCode.custom-186",
        "FipfdiscdescriptorfcelsAcceptRejectReserved": "fip.header.descriptors.descriptor.npivFDISCDescriptor.fipFdiscDescriptorFcEls.acceptReject.reserved-187",
        "LogoDescriptorType": "fip.header.descriptors.descriptor.logoDescriptor.type-188",
        "LogoDescriptorLength": "fip.header.descriptors.descriptor.logoDescriptor.length-189",
        "LogoDescriptorReserved": "fip.header.descriptors.descriptor.logoDescriptor.reserved-190",
        "RctlDeviceDataFramesInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.deviceDataFrames.info-191",
        "LogodescriptorFibrechannelRCTLReserved": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.reserved-192",
        "FibrechannelRctlExtendedLinkServicesInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.extendedLinkServices.info-193",
        "FibrechannelRctlFc4LinkDataInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.fc4LinkData.info-194",
        "FibrechannelRctlVideoDataInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.videoData.info-195",
        "FibrechannelRctlExtendedHeaderInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.extendedHeader.info-196",
        "FibrechannelRctlBasicLinkServicesInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.basicLinkServices.info-197",
        "FibrechannelRctlLinkControlFramesInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.linkControlFrames.info-198",
        "FibrechannelRctlExtendedRoutingInfo": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rCTL.extendedRouting.info-199",
        "LogodescriptorFibreChannelDID": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.dID-200",
        "LogodescriptorFibreChannelCsCTLPriority": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.csCTLPriority-201",
        "LogodescriptorFibreChannelSID": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.sID-202",
        "LogodescriptorFibreChannelType": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.type-203",
        "LogodescriptorFibrechannelFCTLCustom": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.custom-204",
        "FibrechannelFctlFCTLExchangeContext": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.exchangeContext-205",
        "FibrechannelFctlFCTLSequenceContext": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.sequenceContext-206",
        "FibrechannelFctlFCTLFirstSequence": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.firstSequence-207",
        "FibrechannelFctlFCTLLastSequence": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.lastSequence-208",
        "FibrechannelFctlFCTLEndSequence": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.endSequence-209",
        "FibrechannelFctlFCTLEndConnection": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.endConnection-210",
        "FibrechannelFctlFCTLCsCTLPriority": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.csCTLPriority-211",
        "FibrechannelFctlFCTLSequenceInitiative": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.sequenceInitiative-212",
        "FibrechannelFctlFCTLFcXIDReassigned": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.fcXIDReassigned-213",
        "FibrechannelFctlFCTLFcInvalidateXID": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.fcInvalidateXID-214",
        "FibrechannelFctlFCTLAckForm": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.ackForm-215",
        "FibrechannelFctlFCTLFcDataCompression": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.fcDataCompression-216",
        "FibrechannelFctlFCTLFcDataEncryption": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.fcDataEncryption-217",
        "FibrechannelFctlFCTLRetransmittedSequence": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.retransmittedSequence-218",
        "FibrechannelFctlFCTLUnidirectionalTransmit": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.unidirectionalTransmit-219",
        "FibrechannelFctlFCTLContinueSeqCondition": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.continueSeqCondition-220",
        "FibrechannelFctlFCTLAbortSeqCondition": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.abortSeqCondition-221",
        "FibrechannelFctlFCTLRelativeOffsetPresent": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.relativeOffsetPresent-222",
        "FibrechannelFctlFCTLExchangeReassembly": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.exchangeReassembly-223",
        "FibrechannelFctlFCTLFillBytes": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.fCTL.fCTL.fillBytes-224",
        "LogodescriptorFibreChannelSeqID": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.seqID-225",
        "LogodescriptorFibreChannelDfCTL": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.dfCTL-226",
        "LogodescriptorFibreChannelSeqCNT": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.seqCNT-227",
        "LogodescriptorFibreChannelOxID": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.oxID-228",
        "LogodescriptorFibreChannelRxID": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.rxID-229",
        "LogodescriptorFibreChannelParameter": "fip.header.descriptors.descriptor.logoDescriptor.fibreChannel.parameter-230",
        "CommandCodeLogo": "fip.header.descriptors.descriptor.logoDescriptor.fcELS.commandCode.logo-231",
        "FcelsCommandCodeCustom": "fip.header.descriptors.descriptor.logoDescriptor.fcELS.commandCode.custom-232",
        "FcELSReserved": "fip.header.descriptors.descriptor.logoDescriptor.fcELS.reserved-233",
        "FcELSOriginatorSID": "fip.header.descriptors.descriptor.logoDescriptor.fcELS.originatorSID-234",
        "FcELSNPortPortName": "fip.header.descriptors.descriptor.logoDescriptor.fcELS.nPortPortName-235",
        "ElpDescriptorType": "fip.header.descriptors.descriptor.elpDescriptor.type-236",
        "ElpDescriptorLength": "fip.header.descriptors.descriptor.elpDescriptor.length-237",
        "ElpDescriptorReserved": "fip.header.descriptors.descriptor.elpDescriptor.reserved-238",
        "ExchangeLinkParametersRequestReply": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.rCTL.exchangeLinkParameters.requestReply-239",
        "ElpdescriptorFibreChannelDID": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.dID-240",
        "ElpdescriptorFibreChannelCsCTLPriority": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.csCTLPriority-241",
        "ElpdescriptorFibreChannelSID": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.sID-242",
        "ElpdescriptorFibreChannelType": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.type-243",
        "ElpdescriptorFibrechannelFCTLCustom": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.custom-244",
        "FCtlExchangeContext": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.exchangeContext-245",
        "FCtlSequenceContext": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.sequenceContext-246",
        "FCtlFirstSequence": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.firstSequence-247",
        "FCtlLastSequence": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.lastSequence-248",
        "FCtlEndSequence": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.endSequence-249",
        "FCtlEndConnection": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.endConnection-250",
        "FCtlCsCTLPriority": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.csCTLPriority-251",
        "FCtlSequenceInitiative": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.sequenceInitiative-252",
        "FCtlFcXIDReassigned": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.fcXIDReassigned-253",
        "FCtlFcInvalidateXID": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.fcInvalidateXID-254",
        "FCtlAckForm": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.ackForm-255",
        "FCtlFcDataCompression": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.fcDataCompression-256",
        "FCtlFcDataEncryption": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.fcDataEncryption-257",
        "FCtlRetransmittedSequence": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.retransmittedSequence-258",
        "FCtlUnidirectionalTransmit": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.unidirectionalTransmit-259",
        "FCtlContinueSeqCondition": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.continueSeqCondition-260",
        "FCtlAbortSeqCondition": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.abortSeqCondition-261",
        "FCtlRelativeOffsetPresent": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.relativeOffsetPresent-262",
        "FCtlExchangeReassembly": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.exchangeReassembly-263",
        "FCtlFillBytes": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.fCTL.fCtl.fillBytes-264",
        "ElpdescriptorFibreChannelSeqID": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.seqID-265",
        "ElpdescriptorFibreChannelDfCTL": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.dfCTL-266",
        "ElpdescriptorFibreChannelSeqCNT": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.seqCNT-267",
        "ElpdescriptorFibreChannelOxID": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.oxID-268",
        "ElpdescriptorFibreChannelRxID": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.rxID-269",
        "ElpdescriptorFibreChannelParameter": "fip.header.descriptors.descriptor.elpDescriptor.fibreChannel.parameter-270",
        "CommandCodeExchangeLinkParameters": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commandCode.exchangeLinkParameters-271",
        "CommandCodeElpReply": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commandCode.elpReply-272",
        "RequestreplyCommandCodeCustom": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commandCode.custom-273",
        "CommonServiceParametersRevision": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.revision-274",
        "FlagsBridgePortBit": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.flags.bridgePortBit-275",
        "FlagsBridgeVirtualFabricsBit": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.flags.bridgeVirtualFabricsBit-276",
        "FlagsReserved": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.flags.reserved-277",
        "BbSCNReserved": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.bbSCN.reserved-278",
        "BbSCNBbSNN": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.bbSCN.bbSNN-279",
        "RequestreplyCommonServiceParametersRATOV": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.rATOV-280",
        "RequestreplyCommonServiceParametersEDTOV": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.eDTOV-281",
        "CommonServiceParametersRequesterInterconnectPortName": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.requesterInterconnectPortName-282",
        "CommonServiceParametersRequesterSwitchName": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.commonServiceParameters.requesterSwitchName-283",
        "FabricControllerClassFServiceParametersVal": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.val-284",
        "FabricControllerClassFServiceParametersReserved1": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.reserved1-285",
        "FabricControllerClassFServiceParametersXIDInterlock": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.xIDInterlock-286",
        "FabricControllerClassFServiceParametersReserved2": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.reserved2-287",
        "FabricControllerClassFServiceParametersReceiveDataFieldSize": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.receiveDataFieldSize-288",
        "FabricControllerClassFServiceParametersConcurrentSequences": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.concurrentSequences-289",
        "FabricControllerClassFServiceParametersEndToEndCredit": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.endToEndCredit-290",
        "FabricControllerClassFServiceParametersOpenSequencesPerExchange": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.openSequencesPerExchange-291",
        "FabricControllerClassFServiceParametersReserved3": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.fabricControllerClassFServiceParameters.reserved3-292",
        "RequestReplyClass1InterconnectPortParameters": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.class1InterconnectPortParameters-293",
        "RequestReplyClass2InterconnectPortParameters": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.class2InterconnectPortParameters-294",
        "RequestReplyClass3InterconnectPortParameters": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.class3InterconnectPortParameters-295",
        "RequestReplyReserved": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.reserved-296",
        "IslFlowControlModeVendorSpecific": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.islFlowControlMode.vendorSpecific-297",
        "IslFlowControlModeRRDYFlowControl": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.islFlowControlMode.rRDYFlowControl-298",
        "IslFlowControlModeVcRDYFlowControl": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.islFlowControlMode.vcRDYFlowControl-299",
        "IslFlowControlModeReservedForAEUse": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.islFlowControlMode.reservedForAEUse-300",
        "IslFlowControlModeReserved": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.islFlowControlMode.reserved-301",
        "IslFlowControlModeCustom": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.islFlowControlMode.custom-302",
        "RequestReplyFlowControlParameterLength": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameterLength-303",
        "RRDYFlowControlBbCredit": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.rRDYFlowControl.bbCredit-304",
        "RRDYFlowControlCompatibilityParameters": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.rRDYFlowControl.compatibilityParameters-305",
        "VcRDYFlowControlBbCredit": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.bbCredit-306",
        "AssignmentSchemeSimple": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.assignmentScheme.simple-307",
        "AssignmentSchemeFixed": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.assignmentScheme.fixed-308",
        "AssignmentSchemeVariable": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.assignmentScheme.variable-309",
        "AssignmentSchemeVendorSpecific": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.assignmentScheme.vendorSpecific-310",
        "AssignmentSchemeReserved": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.assignmentScheme.reserved-311",
        "AssignmentSchemeCustom": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.assignmentScheme.custom-312",
        "VcRDYFlowControlVcValue": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.vcValue-313",
        "VcCreditsVcCredit": "fip.header.descriptors.descriptor.elpDescriptor.fcELP.requestReply.flowControlParameters.vcRDYFlowControl.vcCredits.vcCredit-314",
        "VxPortIdentificationDescriptorType": "fip.header.descriptors.descriptor.vxPortIdentificationDescriptor.type-315",
        "VxPortIdentificationDescriptorLength": "fip.header.descriptors.descriptor.vxPortIdentificationDescriptor.length-316",
        "VxPortIdentificationDescriptorMacAddress": "fip.header.descriptors.descriptor.vxPortIdentificationDescriptor.macAddress-317",
        "VxPortIdentificationDescriptorReserved": "fip.header.descriptors.descriptor.vxPortIdentificationDescriptor.reserved-318",
        "VxPortIdentificationDescriptorIdentifier": "fip.header.descriptors.descriptor.vxPortIdentificationDescriptor.identifier-319",
        "VxPortIdentificationDescriptorValue": "fip.header.descriptors.descriptor.vxPortIdentificationDescriptor.value-320",
        "FkaADVPeriodDescriptorType": "fip.header.descriptors.descriptor.fkaADVPeriodDescriptor.type-321",
        "FkaADVPeriodDescriptorLength": "fip.header.descriptors.descriptor.fkaADVPeriodDescriptor.length-322",
        "FkaADVPeriodDescriptorReserved": "fip.header.descriptors.descriptor.fkaADVPeriodDescriptor.reserved-323",
        "FkaADVPeriodDescriptorFipDBit": "fip.header.descriptors.descriptor.fkaADVPeriodDescriptor.fipDBit-324",
        "FkaADVPeriodDescriptorValue": "fip.header.descriptors.descriptor.fkaADVPeriodDescriptor.value-325",
        "VendorIDDescriptorType": "fip.header.descriptors.descriptor.vendorIDDescriptor.type-326",
        "VendorIDDescriptorLength": "fip.header.descriptors.descriptor.vendorIDDescriptor.length-327",
        "VendorIDDescriptorReserved": "fip.header.descriptors.descriptor.vendorIDDescriptor.reserved-328",
        "VendorIDDescriptorValue": "fip.header.descriptors.descriptor.vendorIDDescriptor.value-329",
        "VlanDescriptorType": "fip.header.descriptors.descriptor.vlanDescriptor.type-330",
        "VlanDescriptorLength": "fip.header.descriptors.descriptor.vlanDescriptor.length-331",
        "VlanDescriptorReserved": "fip.header.descriptors.descriptor.vlanDescriptor.reserved-332",
        "VlanDescriptorValue": "fip.header.descriptors.descriptor.vlanDescriptor.value-333",
        "VendorSpecificDescriptorType": "fip.header.descriptors.descriptor.vendorSpecificDescriptor.type-334",
        "VendorSpecificDescriptorLength": "fip.header.descriptors.descriptor.vendorSpecificDescriptor.length-335",
        "VendorSpecificDescriptorReserved": "fip.header.descriptors.descriptor.vendorSpecificDescriptor.reserved-336",
        "VendorSpecificDescriptorVendorID": "fip.header.descriptors.descriptor.vendorSpecificDescriptor.vendorID-337",
        "VendorSpecificDescriptorValue": "fip.header.descriptors.descriptor.vendorSpecificDescriptor.value-338",
        "ReservedDescriptorType": "fip.header.descriptors.descriptor.reservedDescriptor.type-339",
        "ReservedDescriptorLength": "fip.header.descriptors.descriptor.reservedDescriptor.length-340",
        "ReservedDescriptorValue": "fip.header.descriptors.descriptor.reservedDescriptor.value-341",
    }

    def __init__(self, parent, list_op=False):
        super(Fip, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved"]))

    @property
    def CodeDiscovery(self):
        """
        Display Name: Discovery
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CodeDiscovery"]))

    @property
    def CodeVirtualLinkInstantiation(self):
        """
        Display Name: Virtual Link Instantiation
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CodeVirtualLinkInstantiation"])
        )

    @property
    def CodeKeepaliveVirtualLink(self):
        """
        Display Name: Keep Alive/Clear Virtual Links
        Default Value: 0x0003
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CodeKeepaliveVirtualLink"])
        )

    @property
    def CodeVlanDiscovery(self):
        """
        Display Name: FIP VLAN Discovery
        Default Value: 0x0004
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CodeVlanDiscovery"])
        )

    @property
    def CodeVendorSpecific(self):
        """
        Display Name: Vendor Specific
        Default Value: 0xFFF8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CodeVendorSpecific"])
        )

    @property
    def OperationReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OperationReserved1"])
        )

    @property
    def SubcodeSubcode01h(self):
        """
        Display Name: Subcode 01h
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubcodeSubcode01h"])
        )

    @property
    def SubcodeSubcode02h(self):
        """
        Display Name: Subcode 02h
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubcodeSubcode02h"])
        )

    @property
    def SubcodeVendorSpecificSubcode(self):
        """
        Display Name: Vendor Specific
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubcodeVendorSpecificSubcode"])
        )

    @property
    def SubcodeSubcodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubcodeSubcodeCustom"])
        )

    @property
    def OperationDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OperationDescriptorListLength"]),
        )

    @property
    def OperationFipFP(self):
        """
        Display Name: FP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OperationFipFP"])
        )

    @property
    def OperationFipSP(self):
        """
        Display Name: SP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OperationFipSP"])
        )

    @property
    def OperationReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OperationReserved2"])
        )

    @property
    def OperationABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OperationABit"]))

    @property
    def OperationSBit(self):
        """
        Display Name: S bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OperationSBit"]))

    @property
    def OperationFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OperationFBit"]))

    @property
    def PriorityDescriptorType(self):
        """
        Display Name: Priority Descriptor Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityDescriptorType"])
        )

    @property
    def PriorityDescriptorLength(self):
        """
        Display Name: Priority Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityDescriptorLength"])
        )

    @property
    def PriorityDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityDescriptorReserved"])
        )

    @property
    def PriorityDescriptorValue(self):
        """
        Display Name: Priority Descriptor Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PriorityDescriptorValue"])
        )

    @property
    def MacAddressDescriptorType(self):
        """
        Display Name: MAC Address Descriptor Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacAddressDescriptorType"])
        )

    @property
    def MacAddressDescriptorLength(self):
        """
        Display Name: MAC Address Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacAddressDescriptorLength"])
        )

    @property
    def MacAddressDescriptorValue(self):
        """
        Display Name: MAC Address Descriptor Value
        Default Value: 00:EE:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacAddressDescriptorValue"])
        )

    @property
    def FcMapDescriptorType(self):
        """
        Display Name: FC-MAP Descriptor Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcMapDescriptorType"])
        )

    @property
    def FcMapDescriptorLength(self):
        """
        Display Name: FC-MAP Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcMapDescriptorLength"])
        )

    @property
    def FcMapDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcMapDescriptorReserved"])
        )

    @property
    def FcMapDescriptorValue(self):
        """
        Display Name: FC-MAP Descriptor Value
        Default Value: 0x000EFC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcMapDescriptorValue"])
        )

    @property
    def NameIdentifierDescriptorType(self):
        """
        Display Name: Name_Identifier Descriptor Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NameIdentifierDescriptorType"])
        )

    @property
    def NameIdentifierDescriptorLength(self):
        """
        Display Name: Name_Identifier Descriptor Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NameIdentifierDescriptorLength"]),
        )

    @property
    def NameIdentifierDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NameIdentifierDescriptorReserved"]),
        )

    @property
    def NameIdentifierDescriptorValue(self):
        """
        Display Name: Name_Identifier Descriptor Value
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NameIdentifierDescriptorValue"]),
        )

    @property
    def FabricDescriptorType(self):
        """
        Display Name: Fabric Descriptor Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FabricDescriptorType"])
        )

    @property
    def FabricDescriptorLength(self):
        """
        Display Name: Fabric Descriptor Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FabricDescriptorLength"])
        )

    @property
    def FabricDescriptorVfID(self):
        """
        Display Name: Fabric Descriptor VF_ID
        Default Value: 256
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FabricDescriptorVfID"])
        )

    @property
    def FabricDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FabricDescriptorReserved"])
        )

    @property
    def FabricDescriptorFcMap(self):
        """
        Display Name: Fabric Descriptor FC-MAP
        Default Value: 0x000EFC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FabricDescriptorFcMap"])
        )

    @property
    def FabricDescriptorValue(self):
        """
        Display Name: Fabric Descriptor Value
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FabricDescriptorValue"])
        )

    @property
    def MaxFcoeSizeDescriptorType(self):
        """
        Display Name: Max FCoE Size Descriptor Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxFcoeSizeDescriptorType"])
        )

    @property
    def MaxFcoeSizeDescriptorLength(self):
        """
        Display Name: Max FCoE Size Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxFcoeSizeDescriptorLength"])
        )

    @property
    def MaxFcoeSizeDescriptorValue(self):
        """
        Display Name: Max FCoE Size Descriptor Value
        Default Value: 2158
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxFcoeSizeDescriptorValue"])
        )

    @property
    def FlogiDescriptorType(self):
        """
        Display Name: FLOGI Descriptor Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlogiDescriptorType"])
        )

    @property
    def FlogiDescriptorLength(self):
        """
        Display Name: FLOGI Descriptor Length
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlogiDescriptorLength"])
        )

    @property
    def FlogiDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlogiDescriptorReserved"])
        )

    @property
    def DeviceDataFramesDeviceDataInfo(self):
        """
        Display Name: Information
        Default Value: 0
        Value Format: decimal
        Available enum values: Uncategorized Information, 0, Solicited Data, 1, Unsolicited Control, 2, Solicited Control, 3, Unsolicited Data, 4, Data Descriptor, 5, Unsolicited Command, 6, Command Status, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DeviceDataFramesDeviceDataInfo"]),
        )

    @property
    def RCTLReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RCTLReserved"]))

    @property
    def ExtendedLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 33
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedLinkServicesInfo"])
        )

    @property
    def Fc4LinkDataInfo(self):
        """
        Display Name: Information
        Default Value: 48
        Value Format: decimal
        Available enum values: Uncategorized Information, 48, Solicited Data, 49, Unsolicited Control, 50, Solicited Control, 51, Unsolicited Data, 52, Data Descriptor, 53, Unsolicited Command, 54, Command Status, 55
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Fc4LinkDataInfo"])
        )

    @property
    def VideoDataInfo(self):
        """
        Display Name: Information
        Default Value: 68
        Value Format: decimal
        Available enum values: Unsolicited Data, 68
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VideoDataInfo"]))

    @property
    def ExtendedHeaderInfo(self):
        """
        Display Name: Information
        Default Value: 80
        Value Format: decimal
        Available enum values: Virtual Fabric Tagging Header, 80, Inter Fabric Routing Header, 81, Encapsulation Header, 82
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedHeaderInfo"])
        )

    @property
    def BasicLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 128
        Value Format: decimal
        Available enum values: No Operation, 128, Abort Sequence, 129, Remove Connection, 130, Basic Accept, 132, Basic Reject, 133, Dedicated Connection Preempted, 134
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BasicLinkServicesInfo"])
        )

    @property
    def LinkControlFramesInfo(self):
        """
        Display Name: Information
        Default Value: 192
        Value Format: decimal
        Available enum values: Acknowledge_1, 128, Acknowledge_0, 129, Nx Port Reject, 130, Fabric Reject, 131, Nx Port Busy, 132, Fabric Busy to Data Frame, 133, Fabric Busy to Link Control Frame, 134, Link Credit Reset, 135, Notify, 136, End, 137
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkControlFramesInfo"])
        )

    @property
    def ExtendedRoutingInfo(self):
        """
        Display Name: Information
        Default Value: 240
        Value Format: decimal
        Available enum values: Vendor Unique, 240
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedRoutingInfo"])
        )

    @property
    def FibreChannelDID(self):
        """
        Display Name: D_ID
        Default Value: FF.FF.FE
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelDID"])
        )

    @property
    def FibreChannelCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelCsCTLPriority"])
        )

    @property
    def FibreChannelSID(self):
        """
        Display Name: S_ID
        Default Value: 00.00.00
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelSID"])
        )

    @property
    def FibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelType"])
        )

    @property
    def FCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCTLCustom"]))

    @property
    def FCTLExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLExchangeContext"])
        )

    @property
    def FCTLSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLSequenceContext"])
        )

    @property
    def FCTLFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLFirstSequence"])
        )

    @property
    def FCTLLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLLastSequence"])
        )

    @property
    def FCTLEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLEndSequence"])
        )

    @property
    def FCTLEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLEndConnection"])
        )

    @property
    def FCTLCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLCsCTLPriority"])
        )

    @property
    def FCTLSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 1
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLSequenceInitiative"])
        )

    @property
    def FCTLFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLFcXIDReassigned"])
        )

    @property
    def FCTLFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLFcInvalidateXID"])
        )

    @property
    def FCTLAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCTLAckForm"]))

    @property
    def FCTLFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLFcDataCompression"])
        )

    @property
    def FCTLFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLFcDataEncryption"])
        )

    @property
    def FCTLRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLRetransmittedSequence"])
        )

    @property
    def FCTLUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLUnidirectionalTransmit"])
        )

    @property
    def FCTLContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLContinueSeqCondition"])
        )

    @property
    def FCTLAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLAbortSeqCondition"])
        )

    @property
    def FCTLRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLRelativeOffsetPresent"])
        )

    @property
    def FCTLExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCTLExchangeReassembly"])
        )

    @property
    def FCTLFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCTLFillBytes"]))

    @property
    def FibreChannelSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelSeqID"])
        )

    @property
    def FibreChannelDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelDfCTL"])
        )

    @property
    def FibreChannelSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelSeqCNT"])
        )

    @property
    def FibreChannelOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelOxID"])
        )

    @property
    def FibreChannelRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelRxID"])
        )

    @property
    def FibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibreChannelParameter"])
        )

    @property
    def CommandCodeFlogi(self):
        """
        Display Name: FLOGI
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeFlogi"])
        )

    @property
    def CommandCodeFdisc(self):
        """
        Display Name: FDISC
        Default Value: 0x51
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeFdisc"])
        )

    @property
    def CommandCodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeCustom"])
        )

    @property
    def RequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestReserved"])
        )

    @property
    def CommonServiceParametersFcPHVersion(self):
        """
        Display Name: FC-PH Version
        Default Value: 0x2020
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonServiceParametersFcPHVersion"]
            ),
        )

    @property
    def CommonServiceParametersBufferToBufferCredit(self):
        """
        Display Name: Buffer-to-Buffer Credit
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonServiceParametersBufferToBufferCredit"]
            ),
        )

    @property
    def CommonServiceParametersCommonFeatures(self):
        """
        Display Name: Common Features
        Default Value: 0x8000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonServiceParametersCommonFeatures"]
            ),
        )

    @property
    def CommonServiceParametersBbSCNumber(self):
        """
        Display Name: BB_SC_Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonServiceParametersBbSCNumber"]),
        )

    @property
    def CommonServiceParametersBufferToBufferReceiveDataFieldSize(self):
        """
        Display Name: Buffer-to-Buffer Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CommonServiceParametersBufferToBufferReceiveDataFieldSize"
                ]
            ),
        )

    @property
    def CommonServiceParametersRATOV(self):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonServiceParametersRATOV"])
        )

    @property
    def CommonServiceParametersEDTOV(self):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonServiceParametersEDTOV"])
        )

    @property
    def CommonServiceParametersNPortPortName(self):
        """
        Display Name: N_Port Port Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonServiceParametersNPortPortName"]
            ),
        )

    @property
    def CommonServiceParametersFabricNodeName(self):
        """
        Display Name: Fabric/Node Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonServiceParametersFabricNodeName"]
            ),
        )

    @property
    def RequestClass1SvcParameters(self):
        """
        Display Name: Class 1 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestClass1SvcParameters"])
        )

    @property
    def RequestClass2SvcParameters(self):
        """
        Display Name: Class 2 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestClass2SvcParameters"])
        )

    @property
    def Class3SvcParametersServiceOptions(self):
        """
        Display Name: Service Options
        Default Value: 0x8800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Class3SvcParametersServiceOptions"]),
        )

    @property
    def Class3SvcParametersInitiatorControl(self):
        """
        Display Name: Initiator Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Class3SvcParametersInitiatorControl"]
            ),
        )

    @property
    def Class3SvcParametersRecipientControl(self):
        """
        Display Name: Recipient Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Class3SvcParametersRecipientControl"]
            ),
        )

    @property
    def Class3SvcParametersReceiveSize(self):
        """
        Display Name: Class Receive Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Class3SvcParametersReceiveSize"]),
        )

    @property
    def Class3SvcParametersTotalConcurrentSequence(self):
        """
        Display Name: Total Concurrent Sequence
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Class3SvcParametersTotalConcurrentSequence"]
            ),
        )

    @property
    def Class3SvcParametersEndToEndCredit(self):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Class3SvcParametersEndToEndCredit"]),
        )

    @property
    def Class3SvcParametersOpenSeqPerExchange(self):
        """
        Display Name: Open Seq Per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Class3SvcParametersOpenSeqPerExchange"]
            ),
        )

    @property
    def Class3SvcParametersCrTOV(self):
        """
        Display Name: CR_TOV
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Class3SvcParametersCrTOV"])
        )

    @property
    def RequestClass4SvcParameters(self):
        """
        Display Name: Class 4 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestClass4SvcParameters"])
        )

    @property
    def RequestVendorVersion(self):
        """
        Display Name: Vendor Version
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestVendorVersion"])
        )

    @property
    def CommandCodeLsACC(self):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeLsACC"])
        )

    @property
    def CommandCodeLsRJT(self):
        """
        Display Name: LS_RJT
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeLsRJT"])
        )

    @property
    def AcceptrejectCommandCodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AcceptrejectCommandCodeCustom"]),
        )

    @property
    def AcceptRejectReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcceptRejectReserved"])
        )

    @property
    def NpivFDISCDescriptorType(self):
        """
        Display Name: NPIV FDISC Descriptor Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NpivFDISCDescriptorType"])
        )

    @property
    def NpivFDISCDescriptorLength(self):
        """
        Display Name: NPIV FDISC Descriptor Length
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NpivFDISCDescriptorLength"])
        )

    @property
    def NpivFDISCDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NpivFDISCDescriptorReserved"])
        )

    @property
    def DeviceDataFramesInfo(self):
        """
        Display Name: Information
        Default Value: 0
        Value Format: decimal
        Available enum values: Uncategorized Information, 0, Solicited Data, 1, Unsolicited Control, 2, Solicited Control, 3, Unsolicited Data, 4, Data Descriptor, 5, Unsolicited Command, 6, Command Status, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DeviceDataFramesInfo"])
        )

    @property
    def FibrechannelRCTLReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibrechannelRCTLReserved"])
        )

    @property
    def RctlExtendedLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 33
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlExtendedLinkServicesInfo"])
        )

    @property
    def RctlFc4LinkDataInfo(self):
        """
        Display Name: Information
        Default Value: 48
        Value Format: decimal
        Available enum values: Uncategorized Information, 48, Solicited Data, 49, Unsolicited Control, 50, Solicited Control, 51, Unsolicited Data, 52, Data Descriptor, 53, Unsolicited Command, 54, Command Status, 55
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlFc4LinkDataInfo"])
        )

    @property
    def RctlVideoDataInfo(self):
        """
        Display Name: Information
        Default Value: 68
        Value Format: decimal
        Available enum values: Unsolicited Data, 68
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlVideoDataInfo"])
        )

    @property
    def RctlExtendedHeaderInfo(self):
        """
        Display Name: Information
        Default Value: 80
        Value Format: decimal
        Available enum values: Virtual Fabric Tagging Header, 80, Inter Fabric Routing Header, 81, Encapsulation Header, 82
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlExtendedHeaderInfo"])
        )

    @property
    def RctlBasicLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 128
        Value Format: decimal
        Available enum values: No Operation, 128, Abort Sequence, 129, Remove Connection, 130, Basic Accept, 132, Basic Reject, 133, Dedicated Connection Preempted, 134
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlBasicLinkServicesInfo"])
        )

    @property
    def RctlLinkControlFramesInfo(self):
        """
        Display Name: Information
        Default Value: 192
        Value Format: decimal
        Available enum values: Acknowledge_1, 128, Acknowledge_0, 129, Nx Port Reject, 130, Fabric Reject, 131, Nx Port Busy, 132, Fabric Busy to Data Frame, 133, Fabric Busy to Link Control Frame, 134, Link Credit Reset, 135, Notify, 136, End, 137
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlLinkControlFramesInfo"])
        )

    @property
    def RctlExtendedRoutingInfo(self):
        """
        Display Name: Information
        Default Value: 240
        Value Format: decimal
        Available enum values: Vendor Unique, 240
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlExtendedRoutingInfo"])
        )

    @property
    def NpivfdiscdescriptorFibreChannelDID(self):
        """
        Display Name: D_ID
        Default Value: 0xFFFFFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelDID"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelCsCTLPriority"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelSID(self):
        """
        Display Name: S_ID
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelSID"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelType"]
            ),
        )

    @property
    def FibrechannelFCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibrechannelFCTLCustom"])
        )

    @property
    def FctlFCTLExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLExchangeContext"])
        )

    @property
    def FctlFCTLSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLSequenceContext"])
        )

    @property
    def FctlFCTLFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLFirstSequence"])
        )

    @property
    def FctlFCTLLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLLastSequence"])
        )

    @property
    def FctlFCTLEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLEndSequence"])
        )

    @property
    def FctlFCTLEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLEndConnection"])
        )

    @property
    def FctlFCTLCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLCsCTLPriority"])
        )

    @property
    def FctlFCTLSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 1
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLSequenceInitiative"])
        )

    @property
    def FctlFCTLFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLFcXIDReassigned"])
        )

    @property
    def FctlFCTLFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLFcInvalidateXID"])
        )

    @property
    def FctlFCTLAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLAckForm"])
        )

    @property
    def FctlFCTLFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLFcDataCompression"])
        )

    @property
    def FctlFCTLFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLFcDataEncryption"])
        )

    @property
    def FctlFCTLRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FctlFCTLRetransmittedSequence"]),
        )

    @property
    def FctlFCTLUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FctlFCTLUnidirectionalTransmit"]),
        )

    @property
    def FctlFCTLContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLContinueSeqCondition"])
        )

    @property
    def FctlFCTLAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLAbortSeqCondition"])
        )

    @property
    def FctlFCTLRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FctlFCTLRelativeOffsetPresent"]),
        )

    @property
    def FctlFCTLExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLExchangeReassembly"])
        )

    @property
    def FctlFCTLFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FctlFCTLFillBytes"])
        )

    @property
    def NpivfdiscdescriptorFibreChannelSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelSeqID"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelDfCTL"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelSeqCNT"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelOxID"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelRxID"]
            ),
        )

    @property
    def NpivfdiscdescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NpivfdiscdescriptorFibreChannelParameter"]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommandCodeFlogi(self):
        """
        Display Name: FLOGI
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipfdiscdescriptorfcelsrequestCommandCodeFlogi"]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommandCodeFdisc(self):
        """
        Display Name: FDISC
        Default Value: 0x51
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipfdiscdescriptorfcelsrequestCommandCodeFdisc"]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommandCodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipfdiscdescriptorfcelsrequestCommandCodeCustom"]
            ),
        )

    @property
    def FipFdiscDescriptorFcElsRequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFdiscDescriptorFcElsRequestReserved"]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersFcPHVersion(self):
        """
        Display Name: FC-PH Version
        Default Value: 0x2020
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersFcPHVersion"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersBufferToBufferCredit(self):
        """
        Display Name: Buffer-to-Buffer Credit
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersBufferToBufferCredit"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersCommonFeatures(self):
        """
        Display Name: Common Features
        Default Value: 0x8000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersCommonFeatures"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersBbSCNumber(self):
        """
        Display Name: BB_SC_Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersBbSCNumber"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersBufferToBufferReceiveDataFieldSize(
        self,
    ):
        """
        Display Name: Buffer-to-Buffer Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersBufferToBufferReceiveDataFieldSize"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersRATOV(self):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersRATOV"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersEDTOV(self):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersEDTOV"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersNPortPortName(self):
        """
        Display Name: N_Port Port Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersNPortPortName"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestCommonServiceParametersFabricNodeName(self):
        """
        Display Name: Fabric/Node Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestCommonServiceParametersFabricNodeName"
                ]
            ),
        )

    @property
    def FipFdiscDescriptorFcElsRequestClass1SvcParameters(self):
        """
        Display Name: Class 1 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFdiscDescriptorFcElsRequestClass1SvcParameters"]
            ),
        )

    @property
    def FipFdiscDescriptorFcElsRequestClass2SvcParameters(self):
        """
        Display Name: Class 2 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFdiscDescriptorFcElsRequestClass2SvcParameters"]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersServiceOptions(self):
        """
        Display Name: Service Options
        Default Value: 0x8800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersServiceOptions"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersInitiatorControl(self):
        """
        Display Name: Initiator Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersInitiatorControl"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersRecipientControl(self):
        """
        Display Name: Recipient Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersRecipientControl"
                ]
            ),
        )

    @property
    def Class3SvcParametersClassReceiveSize(self):
        """
        Display Name: Class Receive Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Class3SvcParametersClassReceiveSize"]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersTotalConcurrentSequence(self):
        """
        Display Name: Total Concurrent Sequence
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersTotalConcurrentSequence"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersEndToEndCredit(self):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersEndToEndCredit"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersOpenSeqPerExchange(self):
        """
        Display Name: Open Seq Per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersOpenSeqPerExchange"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsrequestClass3SvcParametersCrTOV(self):
        """
        Display Name: CR_TOV
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsrequestClass3SvcParametersCrTOV"
                ]
            ),
        )

    @property
    def FipFdiscDescriptorFcElsRequestClass4SvcParameters(self):
        """
        Display Name: Class 4 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFdiscDescriptorFcElsRequestClass4SvcParameters"]
            ),
        )

    @property
    def FipFdiscDescriptorFcElsRequestVendorVersion(self):
        """
        Display Name: Vendor Version
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFdiscDescriptorFcElsRequestVendorVersion"]
            ),
        )

    @property
    def AcceptrejectCommandCodeLsACC(self):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcceptrejectCommandCodeLsACC"])
        )

    @property
    def AcceptrejectCommandCodeLsRJT(self):
        """
        Display Name: LS_RJT
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcceptrejectCommandCodeLsRJT"])
        )

    @property
    def FipfdiscdescriptorfcelsAcceptrejectCommandCodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipfdiscdescriptorfcelsAcceptrejectCommandCodeCustom"
                ]
            ),
        )

    @property
    def FipfdiscdescriptorfcelsAcceptRejectReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipfdiscdescriptorfcelsAcceptRejectReserved"]
            ),
        )

    @property
    def LogoDescriptorType(self):
        """
        Display Name: LOGO Descriptor Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LogoDescriptorType"])
        )

    @property
    def LogoDescriptorLength(self):
        """
        Display Name: LOGO Descriptor Length
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LogoDescriptorLength"])
        )

    @property
    def LogoDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LogoDescriptorReserved"])
        )

    @property
    def RctlDeviceDataFramesInfo(self):
        """
        Display Name: Information
        Default Value: 0
        Value Format: decimal
        Available enum values: Uncategorized Information, 0, Solicited Data, 1, Unsolicited Control, 2, Solicited Control, 3, Unsolicited Data, 4, Data Descriptor, 5, Unsolicited Command, 6, Command Status, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RctlDeviceDataFramesInfo"])
        )

    @property
    def LogodescriptorFibrechannelRCTLReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LogodescriptorFibrechannelRCTLReserved"]
            ),
        )

    @property
    def FibrechannelRctlExtendedLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 33
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelRctlExtendedLinkServicesInfo"]
            ),
        )

    @property
    def FibrechannelRctlFc4LinkDataInfo(self):
        """
        Display Name: Information
        Default Value: 48
        Value Format: decimal
        Available enum values: Uncategorized Information, 48, Solicited Data, 49, Unsolicited Control, 50, Solicited Control, 51, Unsolicited Data, 52, Data Descriptor, 53, Unsolicited Command, 54, Command Status, 55
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelRctlFc4LinkDataInfo"]),
        )

    @property
    def FibrechannelRctlVideoDataInfo(self):
        """
        Display Name: Information
        Default Value: 68
        Value Format: decimal
        Available enum values: Unsolicited Data, 68
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelRctlVideoDataInfo"]),
        )

    @property
    def FibrechannelRctlExtendedHeaderInfo(self):
        """
        Display Name: Information
        Default Value: 80
        Value Format: decimal
        Available enum values: Virtual Fabric Tagging Header, 80, Inter Fabric Routing Header, 81, Encapsulation Header, 82
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelRctlExtendedHeaderInfo"]
            ),
        )

    @property
    def FibrechannelRctlBasicLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 128
        Value Format: decimal
        Available enum values: No Operation, 128, Abort Sequence, 129, Remove Connection, 130, Basic Accept, 132, Basic Reject, 133, Dedicated Connection Preempted, 134
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelRctlBasicLinkServicesInfo"]
            ),
        )

    @property
    def FibrechannelRctlLinkControlFramesInfo(self):
        """
        Display Name: Information
        Default Value: 192
        Value Format: decimal
        Available enum values: Acknowledge_1, 128, Acknowledge_0, 129, Nx Port Reject, 130, Fabric Reject, 131, Nx Port Busy, 132, Fabric Busy to Data Frame, 133, Fabric Busy to Link Control Frame, 134, Link Credit Reset, 135, Notify, 136, End, 137
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelRctlLinkControlFramesInfo"]
            ),
        )

    @property
    def FibrechannelRctlExtendedRoutingInfo(self):
        """
        Display Name: Information
        Default Value: 240
        Value Format: decimal
        Available enum values: Vendor Unique, 240
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelRctlExtendedRoutingInfo"]
            ),
        )

    @property
    def LogodescriptorFibreChannelDID(self):
        """
        Display Name: D_ID
        Default Value: 0xFFFFFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelDID"]),
        )

    @property
    def LogodescriptorFibreChannelCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LogodescriptorFibreChannelCsCTLPriority"]
            ),
        )

    @property
    def LogodescriptorFibreChannelSID(self):
        """
        Display Name: S_ID
        Default Value: 0x00FC0E
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelSID"]),
        )

    @property
    def LogodescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelType"]),
        )

    @property
    def LogodescriptorFibrechannelFCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LogodescriptorFibrechannelFCTLCustom"]
            ),
        )

    @property
    def FibrechannelFctlFCTLExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLExchangeContext"]
            ),
        )

    @property
    def FibrechannelFctlFCTLSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLSequenceContext"]
            ),
        )

    @property
    def FibrechannelFctlFCTLFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLFirstSequence"]),
        )

    @property
    def FibrechannelFctlFCTLLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLLastSequence"]),
        )

    @property
    def FibrechannelFctlFCTLEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLEndSequence"]),
        )

    @property
    def FibrechannelFctlFCTLEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLEndConnection"]),
        )

    @property
    def FibrechannelFctlFCTLCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLCsCTLPriority"]),
        )

    @property
    def FibrechannelFctlFCTLSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLSequenceInitiative"]
            ),
        )

    @property
    def FibrechannelFctlFCTLFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLFcXIDReassigned"]
            ),
        )

    @property
    def FibrechannelFctlFCTLFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLFcInvalidateXID"]
            ),
        )

    @property
    def FibrechannelFctlFCTLAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLAckForm"])
        )

    @property
    def FibrechannelFctlFCTLFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLFcDataCompression"]
            ),
        )

    @property
    def FibrechannelFctlFCTLFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLFcDataEncryption"]
            ),
        )

    @property
    def FibrechannelFctlFCTLRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLRetransmittedSequence"]
            ),
        )

    @property
    def FibrechannelFctlFCTLUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLUnidirectionalTransmit"]
            ),
        )

    @property
    def FibrechannelFctlFCTLContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLContinueSeqCondition"]
            ),
        )

    @property
    def FibrechannelFctlFCTLAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLAbortSeqCondition"]
            ),
        )

    @property
    def FibrechannelFctlFCTLRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLRelativeOffsetPresent"]
            ),
        )

    @property
    def FibrechannelFctlFCTLExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FibrechannelFctlFCTLExchangeReassembly"]
            ),
        )

    @property
    def FibrechannelFctlFCTLFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FibrechannelFctlFCTLFillBytes"]),
        )

    @property
    def LogodescriptorFibreChannelSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelSeqID"]),
        )

    @property
    def LogodescriptorFibreChannelDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelDfCTL"]),
        )

    @property
    def LogodescriptorFibreChannelSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelSeqCNT"]),
        )

    @property
    def LogodescriptorFibreChannelOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelOxID"]),
        )

    @property
    def LogodescriptorFibreChannelRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LogodescriptorFibreChannelRxID"]),
        )

    @property
    def LogodescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LogodescriptorFibreChannelParameter"]
            ),
        )

    @property
    def CommandCodeLogo(self):
        """
        Display Name: LOGO
        Default Value: 0x05
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeLogo"])
        )

    @property
    def FcelsCommandCodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcelsCommandCodeCustom"])
        )

    @property
    def FcELSReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcELSReserved"]))

    @property
    def FcELSOriginatorSID(self):
        """
        Display Name: Originator S_ID
        Default Value: 0x000EFC
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcELSOriginatorSID"])
        )

    @property
    def FcELSNPortPortName(self):
        """
        Display Name: N_Port Port Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcELSNPortPortName"])
        )

    @property
    def ElpDescriptorType(self):
        """
        Display Name: ELP Descriptor Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElpDescriptorType"])
        )

    @property
    def ElpDescriptorLength(self):
        """
        Display Name: ELP Descriptor Length
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElpDescriptorLength"])
        )

    @property
    def ElpDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElpDescriptorReserved"])
        )

    @property
    def ExchangeLinkParametersRequestReply(self):
        """
        Display Name: Request/Reply
        Default Value: 2
        Value Format: decimal
        Available enum values: Request, 2, Reply, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExchangeLinkParametersRequestReply"]
            ),
        )

    @property
    def ElpdescriptorFibreChannelDID(self):
        """
        Display Name: D_ID
        Default Value: 0xFFFFFD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelDID"])
        )

    @property
    def ElpdescriptorFibreChannelCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ElpdescriptorFibreChannelCsCTLPriority"]
            ),
        )

    @property
    def ElpdescriptorFibreChannelSID(self):
        """
        Display Name: S_ID
        Default Value: 0xFFFFFD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelSID"])
        )

    @property
    def ElpdescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelType"]),
        )

    @property
    def ElpdescriptorFibrechannelFCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ElpdescriptorFibrechannelFCTLCustom"]
            ),
        )

    @property
    def FCtlExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeContext"])
        )

    @property
    def FCtlSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceContext"])
        )

    @property
    def FCtlFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFirstSequence"])
        )

    @property
    def FCtlLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlLastSequence"])
        )

    @property
    def FCtlEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndSequence"])
        )

    @property
    def FCtlEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndConnection"])
        )

    @property
    def FCtlCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlCsCTLPriority"])
        )

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceInitiative"])
        )

    @property
    def FCtlFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcXIDReassigned"])
        )

    @property
    def FCtlFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcInvalidateXID"])
        )

    @property
    def FCtlAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlAckForm"]))

    @property
    def FCtlFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataCompression"])
        )

    @property
    def FCtlFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataEncryption"])
        )

    @property
    def FCtlRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRetransmittedSequence"])
        )

    @property
    def FCtlUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlUnidirectionalTransmit"])
        )

    @property
    def FCtlContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlContinueSeqCondition"])
        )

    @property
    def FCtlAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlAbortSeqCondition"])
        )

    @property
    def FCtlRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRelativeOffsetPresent"])
        )

    @property
    def FCtlExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeReassembly"])
        )

    @property
    def FCtlFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlFillBytes"]))

    @property
    def ElpdescriptorFibreChannelSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelSeqID"]),
        )

    @property
    def ElpdescriptorFibreChannelDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelDfCTL"]),
        )

    @property
    def ElpdescriptorFibreChannelSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelSeqCNT"]),
        )

    @property
    def ElpdescriptorFibreChannelOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelOxID"]),
        )

    @property
    def ElpdescriptorFibreChannelRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ElpdescriptorFibreChannelRxID"]),
        )

    @property
    def ElpdescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ElpdescriptorFibreChannelParameter"]
            ),
        )

    @property
    def CommandCodeExchangeLinkParameters(self):
        """
        Display Name: Exchange Link Parameters
        Default Value: 0x10000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommandCodeExchangeLinkParameters"]),
        )

    @property
    def CommandCodeElpReply(self):
        """
        Display Name: ELP Reply
        Default Value: 0x02000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommandCodeElpReply"])
        )

    @property
    def RequestreplyCommandCodeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RequestreplyCommandCodeCustom"]),
        )

    @property
    def CommonServiceParametersRevision(self):
        """
        Display Name: Revision
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonServiceParametersRevision"]),
        )

    @property
    def FlagsBridgePortBit(self):
        """
        Display Name: Bridge Port Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: E_Port, 0, B_Port, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsBridgePortBit"])
        )

    @property
    def FlagsBridgeVirtualFabricsBit(self):
        """
        Display Name: Bridge Virtual Fabrics Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Does not support VFT tagged frames, 0, Supports VFT tagged frames, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsBridgeVirtualFabricsBit"])
        )

    @property
    def FlagsReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved"]))

    @property
    def BbSCNReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BbSCNReserved"]))

    @property
    def BbSCNBbSNN(self):
        """
        Display Name: BB_SN_N
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BbSCNBbSNN"]))

    @property
    def RequestreplyCommonServiceParametersRATOV(self):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestreplyCommonServiceParametersRATOV"]
            ),
        )

    @property
    def RequestreplyCommonServiceParametersEDTOV(self):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestreplyCommonServiceParametersEDTOV"]
            ),
        )

    @property
    def CommonServiceParametersRequesterInterconnectPortName(self):
        """
        Display Name: Requester Interconnect_Port_Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CommonServiceParametersRequesterInterconnectPortName"
                ]
            ),
        )

    @property
    def CommonServiceParametersRequesterSwitchName(self):
        """
        Display Name: Requester Switch Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonServiceParametersRequesterSwitchName"]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersVal(self):
        """
        Display Name: VAL
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FabricControllerClassFServiceParametersVal"]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FabricControllerClassFServiceParametersReserved1"]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersXIDInterlock(self):
        """
        Display Name: X_ID Interlock
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FabricControllerClassFServiceParametersXIDInterlock"]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FabricControllerClassFServiceParametersReserved2"]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersReceiveDataFieldSize(self):
        """
        Display Name: Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FabricControllerClassFServiceParametersReceiveDataFieldSize"
                ]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersConcurrentSequences(self):
        """
        Display Name: Concurrent Sequences
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FabricControllerClassFServiceParametersConcurrentSequences"
                ]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersEndToEndCredit(self):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FabricControllerClassFServiceParametersEndToEndCredit"
                ]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersOpenSequencesPerExchange(self):
        """
        Display Name: Open Sequences per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FabricControllerClassFServiceParametersOpenSequencesPerExchange"
                ]
            ),
        )

    @property
    def FabricControllerClassFServiceParametersReserved3(self):
        """
        Display Name: Reserved3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FabricControllerClassFServiceParametersReserved3"]
            ),
        )

    @property
    def RequestReplyClass1InterconnectPortParameters(self):
        """
        Display Name: Class 1 Interconnect_Port Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestReplyClass1InterconnectPortParameters"]
            ),
        )

    @property
    def RequestReplyClass2InterconnectPortParameters(self):
        """
        Display Name: Class 2 Interconnect_Port Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestReplyClass2InterconnectPortParameters"]
            ),
        )

    @property
    def RequestReplyClass3InterconnectPortParameters(self):
        """
        Display Name: Class 3 Interconnect_Port Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestReplyClass3InterconnectPortParameters"]
            ),
        )

    @property
    def RequestReplyReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0000000000000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestReplyReserved"])
        )

    @property
    def IslFlowControlModeVendorSpecific(self):
        """
        Display Name: Vendor Specific
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IslFlowControlModeVendorSpecific"]),
        )

    @property
    def IslFlowControlModeRRDYFlowControl(self):
        """
        Display Name: R_RDY Flow Control
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IslFlowControlModeRRDYFlowControl"]),
        )

    @property
    def IslFlowControlModeVcRDYFlowControl(self):
        """
        Display Name: VC_RDY Flow Control
        Default Value: 0x2000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IslFlowControlModeVcRDYFlowControl"]
            ),
        )

    @property
    def IslFlowControlModeReservedForAEUse(self):
        """
        Display Name: Reserved for AE Use
        Default Value: 0xAE02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IslFlowControlModeReservedForAEUse"]
            ),
        )

    @property
    def IslFlowControlModeReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IslFlowControlModeReserved"])
        )

    @property
    def IslFlowControlModeCustom(self):
        """
        Display Name: Custom
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IslFlowControlModeCustom"])
        )

    @property
    def RequestReplyFlowControlParameterLength(self):
        """
        Display Name: Flow Control Parameter Length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestReplyFlowControlParameterLength"]
            ),
        )

    @property
    def RRDYFlowControlBbCredit(self):
        """
        Display Name: BB_Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RRDYFlowControlBbCredit"])
        )

    @property
    def RRDYFlowControlCompatibilityParameters(self):
        """
        Display Name: Compatibility Parameters
        Default Value: 0x0000000000000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RRDYFlowControlCompatibilityParameters"]
            ),
        )

    @property
    def VcRDYFlowControlBbCredit(self):
        """
        Display Name: BB_Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VcRDYFlowControlBbCredit"])
        )

    @property
    def AssignmentSchemeSimple(self):
        """
        Display Name: Simple
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignmentSchemeSimple"])
        )

    @property
    def AssignmentSchemeFixed(self):
        """
        Display Name: Fixed
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignmentSchemeFixed"])
        )

    @property
    def AssignmentSchemeVariable(self):
        """
        Display Name: Variable
        Default Value: 0x0003
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignmentSchemeVariable"])
        )

    @property
    def AssignmentSchemeVendorSpecific(self):
        """
        Display Name: Vendor Specific
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AssignmentSchemeVendorSpecific"]),
        )

    @property
    def AssignmentSchemeReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0004
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignmentSchemeReserved"])
        )

    @property
    def AssignmentSchemeCustom(self):
        """
        Display Name: Custom
        Default Value: 0x00FF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssignmentSchemeCustom"])
        )

    @property
    def VcRDYFlowControlVcValue(self):
        """
        Display Name: VC Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VcRDYFlowControlVcValue"])
        )

    @property
    def VcCreditsVcCredit(self):
        """
        Display Name: VC Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VcCreditsVcCredit"])
        )

    @property
    def VxPortIdentificationDescriptorType(self):
        """
        Display Name: Vx_Port Identification Descriptor Type
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VxPortIdentificationDescriptorType"]
            ),
        )

    @property
    def VxPortIdentificationDescriptorLength(self):
        """
        Display Name: Vx_Port Identification Descriptor Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VxPortIdentificationDescriptorLength"]
            ),
        )

    @property
    def VxPortIdentificationDescriptorMacAddress(self):
        """
        Display Name: Vx_Port Identification Descriptor MAC Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VxPortIdentificationDescriptorMacAddress"]
            ),
        )

    @property
    def VxPortIdentificationDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VxPortIdentificationDescriptorReserved"]
            ),
        )

    @property
    def VxPortIdentificationDescriptorIdentifier(self):
        """
        Display Name: Vx_Port Identification Descriptor Address Identifier
        Default Value: 0x000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VxPortIdentificationDescriptorIdentifier"]
            ),
        )

    @property
    def VxPortIdentificationDescriptorValue(self):
        """
        Display Name: Vx_Port Identification Descriptor Value
        Default Value: 0x0000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VxPortIdentificationDescriptorValue"]
            ),
        )

    @property
    def FkaADVPeriodDescriptorType(self):
        """
        Display Name: FKA_ADV_Period Descriptor Type
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FkaADVPeriodDescriptorType"])
        )

    @property
    def FkaADVPeriodDescriptorLength(self):
        """
        Display Name: FKA_ADV_Period Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FkaADVPeriodDescriptorLength"])
        )

    @property
    def FkaADVPeriodDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FkaADVPeriodDescriptorReserved"]),
        )

    @property
    def FkaADVPeriodDescriptorFipDBit(self):
        """
        Display Name: D bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FkaADVPeriodDescriptorFipDBit"]),
        )

    @property
    def FkaADVPeriodDescriptorValue(self):
        """
        Display Name: FKA_ADV_Period Descriptor Value
        Default Value: 8000
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FkaADVPeriodDescriptorValue"])
        )

    @property
    def VendorIDDescriptorType(self):
        """
        Display Name: Vendor_ID Descriptor Type
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorIDDescriptorType"])
        )

    @property
    def VendorIDDescriptorLength(self):
        """
        Display Name: Vendor_ID Descriptor Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorIDDescriptorLength"])
        )

    @property
    def VendorIDDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorIDDescriptorReserved"])
        )

    @property
    def VendorIDDescriptorValue(self):
        """
        Display Name: Vendor_ID Descriptor Value
        Default Value: 0x0000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorIDDescriptorValue"])
        )

    @property
    def VlanDescriptorType(self):
        """
        Display Name: VLAN Descriptor Type
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanDescriptorType"])
        )

    @property
    def VlanDescriptorLength(self):
        """
        Display Name: VLAN Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanDescriptorLength"])
        )

    @property
    def VlanDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanDescriptorReserved"])
        )

    @property
    def VlanDescriptorValue(self):
        """
        Display Name: VLAN Descriptor Value
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanDescriptorValue"])
        )

    @property
    def VendorSpecificDescriptorType(self):
        """
        Display Name: Vendor Specific Descriptor Type
        Default Value: 241
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorSpecificDescriptorType"])
        )

    @property
    def VendorSpecificDescriptorLength(self):
        """
        Display Name: Vendor Specific Descriptor Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VendorSpecificDescriptorLength"]),
        )

    @property
    def VendorSpecificDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VendorSpecificDescriptorReserved"]),
        )

    @property
    def VendorSpecificDescriptorVendorID(self):
        """
        Display Name: Vendor Specific Descriptor Vendor_ID
        Default Value: 0x000000FFFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VendorSpecificDescriptorVendorID"]),
        )

    @property
    def VendorSpecificDescriptorValue(self):
        """
        Display Name: Vendor Specific Descriptor Value
        Default Value: 123456789
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VendorSpecificDescriptorValue"]),
        )

    @property
    def ReservedDescriptorType(self):
        """
        Display Name: Reserved Descriptor Type
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedDescriptorType"])
        )

    @property
    def ReservedDescriptorLength(self):
        """
        Display Name: Reserved Descriptor Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedDescriptorLength"])
        )

    @property
    def ReservedDescriptorValue(self):
        """
        Display Name: Reserved Descriptor Value
        Default Value: 65535
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedDescriptorValue"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
