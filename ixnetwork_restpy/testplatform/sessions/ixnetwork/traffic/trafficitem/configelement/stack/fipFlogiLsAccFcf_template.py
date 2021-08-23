from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipFlogiLsAccFcf(Base):
    __slots__ = ()
    _SDM_NAME = 'fipFlogiLsAccFcf'
    _SDM_ATT_MAP = {
        'HeaderFipVersion': 'fipFlogiLsAccFcf.header.fipVersion-1',
        'HeaderFipReserved': 'fipFlogiLsAccFcf.header.fipReserved-2',
        'FipOperationCodeFipVirtualLinkInstantiation': 'fipFlogiLsAccFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3',
        'FipOperationFipOperationReserved1': 'fipFlogiLsAccFcf.header.fipOperation.fipOperationReserved1-4',
        'FipSubcodeFipSubcode02h': 'fipFlogiLsAccFcf.header.fipOperation.fipSubcode.fipSubcode02h-5',
        'FipOperationFipDescriptorListLength': 'fipFlogiLsAccFcf.header.fipOperation.fipDescriptorListLength-6',
        'FipOperationFipFp': 'fipFlogiLsAccFcf.header.fipOperation.fipFp-7',
        'FipOperationFipSp': 'fipFlogiLsAccFcf.header.fipOperation.fipSp-8',
        'FipOperationFipReserved2': 'fipFlogiLsAccFcf.header.fipOperation.fipReserved2-9',
        'FipOperationFipABit': 'fipFlogiLsAccFcf.header.fipOperation.fipABit-10',
        'FipOperationFipSBit': 'fipFlogiLsAccFcf.header.fipOperation.fipSBit-11',
        'FipOperationFipFBit': 'fipFlogiLsAccFcf.header.fipOperation.fipFBit-12',
        'FipFlogiDescriptorFipFlogiDescriptorType': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorType-13',
        'FipFlogiDescriptorFipFlogiDescriptorLength': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorLength-14',
        'FipFlogiDescriptorFipFlogiDescriptorReserved': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorReserved-15',
        'ExtendedLinkServicesExtendedLinkServiceInfo': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelRCtl.extendedLinkServices.extendedLinkServiceInfo-16',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDId': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelDId-17',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelCsCtlPriority': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelCsCtlPriority-18',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSId': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelSId-19',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelType': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelType-20',
        'FCtlExchangeContext': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.exchangeContext-21',
        'FCtlSequenceContext': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.sequenceContext-22',
        'FCtlFirstSequence': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.firstSequence-23',
        'FCtlLastSequence': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.lastSequence-24',
        'FCtlEndSequence': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.endSequence-25',
        'FCtlEndConnection': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.endConnection-26',
        'FCtlCsCtlPriority': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27',
        'FCtlSequenceInitiative': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28',
        'FCtlFcXidReassigned': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29',
        'FCtlFcInvalidateXid': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30',
        'FCtlAckForm': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.ackForm-31',
        'FCtlFcDataCompression': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32',
        'FCtlFcDataEncryption': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33',
        'FCtlRetransmittedSequence': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34',
        'FCtlUnidirectionalTransmit': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35',
        'FCtlContinueSeqCondition': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36',
        'FCtlAbortSeqCondition': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37',
        'FCtlRelativeOffsetPresent': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38',
        'FCtlExchangeReassembly': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39',
        'FCtlFillBytes': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fillBytes-40',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqId': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelSeqId-41',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDfCtl': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelDfCtl-42',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqCnt': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelSeqCnt-43',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelOxId': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelOxId-44',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelRxId': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelRxId-45',
        'FipFlogiFibreChannelFipFlogiDescriptorFibreChannelParameter': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelParameter-46',
        'FipFlogiDescriptorFcElsCommandCodeFipFlogiDescriptorFcElsCommandCodeLsAcc': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommandCode.fipFlogiDescriptorFcElsCommandCodeLsAcc-47',
        'FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsRequestReserved': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsRequestReserved-48',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersFc-phVersion': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersFc-phVersion-49',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDecriptorFcElsCommonServiceParametersBuffer-to-bufferCredit': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDecriptorFcElsCommonServiceParametersBuffer-to-bufferCredit-50',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersCommonFeatures': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersCommonFeatures-51',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersBbScNumber': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersBbScNumber-52',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize-53',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersRATov': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersRATov-54',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersEDTov': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersEDTov-55',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersNPortPortName': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersNPortPortName-56',
        'FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersFabricNodeName': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommonServiceParameters.fipFlogiDescriptorFcElsCommonServiceParametersFabricNodeName-57',
        'FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsClass1SvcParameters': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass1SvcParameters-58',
        'FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsClass2SvcParameters': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass2SvcParameters-59',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersServiceOptions': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersServiceOptions-60',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersInitiatorControl': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersInitiatorControl-61',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersRecipientControl': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersRecipientControl-62',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersClassReceiveSize': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersClassReceiveSize-63',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersTotalConcurrentSequence': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersTotalConcurrentSequence-64',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersEnd-to-endCredit': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersEnd-to-endCredit-65',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersOpenSeqPerExchange': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersOpenSeqPerExchange-66',
        'FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersCrTov': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsClass3SvcParameters.fipFlogiDescriptorFcElsClass3SvcParametersCrTov-67',
        'FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorClass4SvcParameters': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorClass4SvcParameters-68',
        'FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsVendorVersion': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsVendorVersion-69',
        'FipMacAddressDescriptorFipMacAddressDescriptorType': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-70',
        'FipMacAddressDescriptorFipMacAddressDescriptorLength': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-71',
        'FipMacAddressDescriptorFipMacAddressDescriptorValue': 'fipFlogiLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-72',
    }

    def __init__(self, parent, list_op=False):
        super(FipFlogiLsAccFcf, self).__init__(parent, list_op)

    @property
    def HeaderFipVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderFipVersion']))

    @property
    def HeaderFipReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderFipReserved']))

    @property
    def FipOperationCodeFipVirtualLinkInstantiation(self):
        """
        Display Name: Virtual Link Instantiation
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationCodeFipVirtualLinkInstantiation']))

    @property
    def FipOperationFipOperationReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipOperationReserved1']))

    @property
    def FipSubcodeFipSubcode02h(self):
        """
        Display Name: Subcode 02h
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipSubcodeFipSubcode02h']))

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 38
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipDescriptorListLength']))

    @property
    def FipOperationFipFp(self):
        """
        Display Name: FP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipFp']))

    @property
    def FipOperationFipSp(self):
        """
        Display Name: SP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipSp']))

    @property
    def FipOperationFipReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipReserved2']))

    @property
    def FipOperationFipABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipABit']))

    @property
    def FipOperationFipSBit(self):
        """
        Display Name: S bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipSBit']))

    @property
    def FipOperationFipFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipOperationFipFBit']))

    @property
    def FipFlogiDescriptorFipFlogiDescriptorType(self):
        """
        Display Name: FLOGI Descriptor Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFipFlogiDescriptorType']))

    @property
    def FipFlogiDescriptorFipFlogiDescriptorLength(self):
        """
        Display Name: FLOGI Descriptor Length
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFipFlogiDescriptorLength']))

    @property
    def FipFlogiDescriptorFipFlogiDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFipFlogiDescriptorReserved']))

    @property
    def ExtendedLinkServicesExtendedLinkServiceInfo(self):
        """
        Display Name: Information
        Default Value: 35
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtendedLinkServicesExtendedLinkServiceInfo']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDId(self):
        """
        Display Name: D_ID
        Default Value: 00.00.01
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDId']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelCsCtlPriority']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSId(self):
        """
        Display Name: S_ID
        Default Value: FF.FF.FE
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSId']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelType']))

    @property
    def FCtlExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlExchangeContext']))

    @property
    def FCtlSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlSequenceContext']))

    @property
    def FCtlFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlFirstSequence']))

    @property
    def FCtlLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlLastSequence']))

    @property
    def FCtlEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlEndSequence']))

    @property
    def FCtlEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlEndConnection']))

    @property
    def FCtlCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority Enable, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlCsCtlPriority']))

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 1
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlSequenceInitiative']))

    @property
    def FCtlFcXidReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlFcXidReassigned']))

    @property
    def FCtlFcInvalidateXid(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlFcInvalidateXid']))

    @property
    def FCtlAckForm(self):
        """
        Display Name: ACK
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlAckForm']))

    @property
    def FCtlFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlFcDataCompression']))

    @property
    def FCtlFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlFcDataEncryption']))

    @property
    def FCtlRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlRetransmittedSequence']))

    @property
    def FCtlUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlUnidirectionalTransmit']))

    @property
    def FCtlContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlContinueSeqCondition']))

    @property
    def FCtlAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlAbortSeqCondition']))

    @property
    def FCtlRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlRelativeOffsetPresent']))

    @property
    def FCtlExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlExchangeReassembly']))

    @property
    def FCtlFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlFillBytes']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqId']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDfCtl']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqCnt']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelOxId']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelRxId']))

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiFibreChannelFipFlogiDescriptorFibreChannelParameter']))

    @property
    def FipFlogiDescriptorFcElsCommandCodeFipFlogiDescriptorFcElsCommandCodeLsAcc(self):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommandCodeFipFlogiDescriptorFcElsCommandCodeLsAcc']))

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsRequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsRequestReserved']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersFcphVersion(self):
        """
        Display Name: FC-PH Version
        Default Value: 0x2020
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersFc-phVersion']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDecriptorFcElsCommonServiceParametersBuffertobufferCredit(self):
        """
        Display Name: Buffer-to-Buffer Credit
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDecriptorFcElsCommonServiceParametersBuffer-to-bufferCredit']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersCommonFeatures(self):
        """
        Display Name: Common Features
        Default Value: 0x8000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersCommonFeatures']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersBbScNumber(self):
        """
        Display Name: BB_SC_Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersBbScNumber']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersBuffertobufferReceiveDataFieldSize(self):
        """
        Display Name: Buffer-to-Buffer Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersRATov(self):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersRATov']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersEDTov(self):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersEDTov']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersNPortPortName(self):
        """
        Display Name: N_Port Port Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersNPortPortName']))

    @property
    def FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersFabricNodeName(self):
        """
        Display Name: Fabric/Node Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsCommonServiceParametersFipFlogiDescriptorFcElsCommonServiceParametersFabricNodeName']))

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsClass1SvcParameters(self):
        """
        Display Name: Class 1 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsClass1SvcParameters']))

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsClass2SvcParameters(self):
        """
        Display Name: Class 2 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsClass2SvcParameters']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersServiceOptions(self):
        """
        Display Name: Service Options
        Default Value: 0x8800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersServiceOptions']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersInitiatorControl(self):
        """
        Display Name: Initiator Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersInitiatorControl']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersRecipientControl(self):
        """
        Display Name: Recipient Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersRecipientControl']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersClassReceiveSize(self):
        """
        Display Name: Class Receive Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersClassReceiveSize']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersTotalConcurrentSequence(self):
        """
        Display Name: Total Concurrent Sequence
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersTotalConcurrentSequence']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersEndtoendCredit(self):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersEnd-to-endCredit']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersOpenSeqPerExchange(self):
        """
        Display Name: Open Seq Per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersOpenSeqPerExchange']))

    @property
    def FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersCrTov(self):
        """
        Display Name: CR_TOV
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsClass3SvcParametersFipFlogiDescriptorFcElsClass3SvcParametersCrTov']))

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorClass4SvcParameters(self):
        """
        Display Name: Class 4 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorClass4SvcParameters']))

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsVendorVersion(self):
        """
        Display Name: Vendor Version
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsVendorVersion']))

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorType(self):
        """
        Display Name: MAC Address Descriptor Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipMacAddressDescriptorFipMacAddressDescriptorType']))

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorLength(self):
        """
        Display Name: MAC Address Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipMacAddressDescriptorFipMacAddressDescriptorLength']))

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorValue(self):
        """
        Display Name: MAC Address Descriptor Value
        Default Value: 00:EE:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipMacAddressDescriptorFipMacAddressDescriptorValue']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
