from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipNpivFdicsLsAccFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipNpivFdicsLsAccFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipNpivFdicsLsAccFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipNpivFdicsLsAccFcf.header.fipReserved-2",
        "FipOperationCodeFipVirtualLinkInstantiation": "fipNpivFdicsLsAccFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3",
        "FipOperationFipOperationReserved1": "fipNpivFdicsLsAccFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipNpivFdicsLsAccFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipNpivFdicsLsAccFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipNpivFdicsLsAccFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipNpivFdicsLsAccFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipNpivFdicsLsAccFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipNpivFdicsLsAccFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipNpivFdicsLsAccFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipNpivFdicsLsAccFcf.header.fipOperation.fipFBit-12",
        "FipNpivFdiscDescriptorFipNpivFdiscDescriptorType": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorType-13",
        "FipNpivFdiscDescriptorFipNpivFdiscDescriptorLength": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorLength-14",
        "FipNpivFdiscDescriptorFipNpivFdiscDescriptorReserved": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorReserved-15",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelRCtl.extendedLinkServices.extendedLinkServiceInfo-16",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDId": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelDId-17",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelCsCtlPriority": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelCsCtlPriority-18",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSId": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelSId-19",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelType": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelType-20",
        "FCtlExchangeContext": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.exchangeContext-21",
        "FCtlSequenceContext": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.sequenceContext-22",
        "FCtlFirstSequence": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.firstSequence-23",
        "FCtlLastSequence": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.lastSequence-24",
        "FCtlEndSequence": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.endSequence-25",
        "FCtlEndConnection": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.endConnection-26",
        "FCtlCsCtlPriority": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27",
        "FCtlSequenceInitiative": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28",
        "FCtlFcXidReassigned": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29",
        "FCtlFcInvalidateXid": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30",
        "FCtlAckForm": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.ackForm-31",
        "FCtlFcDataCompression": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32",
        "FCtlFcDataEncryption": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33",
        "FCtlRetransmittedSequence": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34",
        "FCtlUnidirectionalTransmit": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35",
        "FCtlContinueSeqCondition": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36",
        "FCtlAbortSeqCondition": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37",
        "FCtlRelativeOffsetPresent": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38",
        "FCtlExchangeReassembly": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39",
        "FCtlFillBytes": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fillBytes-40",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqId": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelSeqId-41",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDfCtl": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelDfCtl-42",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqCnt": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelSeqCnt-43",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelOxId": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelOxId-44",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelRxId": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelRxId-45",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelParameter": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelParameter-46",
        "FipNpivFdiscDescriptorFcElsCommandCodeFipNpivFdiscDescriptorFcElsCommandCodeLsAcc": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommandCode.fipNpivFdiscDescriptorFcElsCommandCodeLsAcc-47",
        "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsRequestReserved": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsRequestReserved-48",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersFc-phVersion": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersFc-phVersion-49",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDecriptorFcElsCommonServiceParametersBuffer-to-bufferCredit": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDecriptorFcElsCommonServiceParametersBuffer-to-bufferCredit-50",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersCommonFeatures": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersCommonFeatures-51",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersBbScNumber": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersBbScNumber-52",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize-53",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersRATov": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersRATov-54",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersEDTov": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersEDTov-55",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersNPortPortName": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersNPortPortName-56",
        "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersFabricNodeName": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsCommonServiceParameters.fipNpivFdiscDescriptorFcElsCommonServiceParametersFabricNodeName-57",
        "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsClass1SvcParameters": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass1SvcParameters-58",
        "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsClass2SvcParameters": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass2SvcParameters-59",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersServiceOptions": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersServiceOptions-60",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersInitiatorControl": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersInitiatorControl-61",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersRecipientControl": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersRecipientControl-62",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersClassReceiveSize": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersClassReceiveSize-63",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersTotalConcurrentSequence": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersTotalConcurrentSequence-64",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersEnd-to-endCredit": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersEnd-to-endCredit-65",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersOpenSeqPerExchange": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersOpenSeqPerExchange-66",
        "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersCrTov": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsClass3SvcParameters.fipNpivFdiscDescriptorFcElsClass3SvcParametersCrTov-67",
        "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorClass4SvcParameters": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorClass4SvcParameters-68",
        "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsVendorVersion": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsRequestAcceptReject.fipNpivFdiscDescriptorFcElsVendorVersion-69",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-70",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-71",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipNpivFdicsLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-72",
    }

    def __init__(self, parent, list_op=False):
        super(FipNpivFdicsLsAccFcf, self).__init__(parent, list_op)

    @property
    def HeaderFipVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipVersion"])
        )

    @property
    def HeaderFipReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipReserved"])
        )

    @property
    def FipOperationCodeFipVirtualLinkInstantiation(self):
        """
        Display Name: Virtual Link Instantiation
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationCodeFipVirtualLinkInstantiation"]
            ),
        )

    @property
    def FipOperationFipOperationReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FipOperationFipOperationReserved1"]),
        )

    @property
    def FipSubcodeFipSubcode02h(self):
        """
        Display Name: Subcode 02h
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipSubcodeFipSubcode02h"])
        )

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 38
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationFipDescriptorListLength"]
            ),
        )

    @property
    def FipOperationFipFp(self):
        """
        Display Name: FP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFp"])
        )

    @property
    def FipOperationFipSp(self):
        """
        Display Name: SP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSp"])
        )

    @property
    def FipOperationFipReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipReserved2"])
        )

    @property
    def FipOperationFipABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipABit"])
        )

    @property
    def FipOperationFipSBit(self):
        """
        Display Name: S bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSBit"])
        )

    @property
    def FipOperationFipFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFBit"])
        )

    @property
    def FipNpivFdiscDescriptorFipNpivFdiscDescriptorType(self):
        """
        Display Name: FLOGI Descriptor Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipNpivFdiscDescriptorFipNpivFdiscDescriptorType"]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFipNpivFdiscDescriptorLength(self):
        """
        Display Name: FLOGI Descriptor Length
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipNpivFdiscDescriptorFipNpivFdiscDescriptorLength"]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFipNpivFdiscDescriptorReserved(self):
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
                    "FipNpivFdiscDescriptorFipNpivFdiscDescriptorReserved"
                ]
            ),
        )

    @property
    def ExtendedLinkServicesExtendedLinkServiceInfo(self):
        """
        Display Name: Information
        Default Value: 35
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExtendedLinkServicesExtendedLinkServiceInfo"]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDId(self):
        """
        Display Name: D_ID
        Default Value: 00.00.01
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelCsCtlPriority"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSId(self):
        """
        Display Name: S_ID
        Default Value: FF.FF.FE
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelType"
                ]
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
        Default Value: 1
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
        Default Value: 1
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
    def FCtlCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority Enable, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlCsCtlPriority"])
        )

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 1
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceInitiative"])
        )

    @property
    def FCtlFcXidReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcXidReassigned"])
        )

    @property
    def FCtlFcInvalidateXid(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcInvalidateXid"])
        )

    @property
    def FCtlAckForm(self):
        """
        Display Name: ACK
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
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDfCtl"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqCnt"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelOxId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelRxId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelParameter"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommandCodeFipNpivFdiscDescriptorFcElsCommandCodeLsAcc(
        self,
    ):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsCommandCodeFipNpivFdiscDescriptorFcElsCommandCodeLsAcc"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsRequestReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsRequestReserved"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersFcphVersion(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersFc-phVersion"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDecriptorFcElsCommonServiceParametersBuffertobufferCredit(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDecriptorFcElsCommonServiceParametersBuffer-to-bufferCredit"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersCommonFeatures(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersCommonFeatures"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersBbScNumber(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersBbScNumber"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersBuffertobufferReceiveDataFieldSize(
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersRATov(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersRATov"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersEDTov(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersEDTov"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersNPortPortName(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersNPortPortName"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersFabricNodeName(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsCommonServiceParametersFipNpivFdiscDescriptorFcElsCommonServiceParametersFabricNodeName"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsClass1SvcParameters(
        self,
    ):
        """
        Display Name: Class 1 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsClass1SvcParameters"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsClass2SvcParameters(
        self,
    ):
        """
        Display Name: Class 2 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsClass2SvcParameters"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersServiceOptions(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersServiceOptions"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersInitiatorControl(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersInitiatorControl"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersRecipientControl(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersRecipientControl"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersClassReceiveSize(
        self,
    ):
        """
        Display Name: Class Receive Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersClassReceiveSize"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersTotalConcurrentSequence(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersTotalConcurrentSequence"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersEndtoendCredit(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersEnd-to-endCredit"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersOpenSeqPerExchange(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersOpenSeqPerExchange"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersCrTov(
        self,
    ):
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
                    "FipNpivFdiscDescriptorFcElsClass3SvcParametersFipNpivFdiscDescriptorFcElsClass3SvcParametersCrTov"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorClass4SvcParameters(
        self,
    ):
        """
        Display Name: Class 4 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorClass4SvcParameters"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsVendorVersion(
        self,
    ):
        """
        Display Name: Vendor Version
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsRequestAcceptRejectFipNpivFdiscDescriptorFcElsVendorVersion"
                ]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorType(self):
        """
        Display Name: MAC Address Descriptor Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipMacAddressDescriptorFipMacAddressDescriptorType"]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorLength(self):
        """
        Display Name: MAC Address Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipMacAddressDescriptorFipMacAddressDescriptorLength"
                ]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorValue(self):
        """
        Display Name: MAC Address Descriptor Value
        Default Value: 00:EE:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipMacAddressDescriptorFipMacAddressDescriptorValue"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
